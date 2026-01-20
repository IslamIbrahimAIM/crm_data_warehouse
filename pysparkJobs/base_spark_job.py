from __future__ import annotations

import math
from typing import Dict

from decouple import config
from pyspark.sql import SparkSession, DataFrame, functions as F


class BaseSparkJob:
    
    ####################### DEFAULTS ##########################
    
    DEFAULT_PARTITIONS = 8
    DEFAULT_BATCH_SIZE = 10_000
    JDBC_DRIVER = "com.mysql.cj.jdbc.Driver"

    
    ####################### SAFETY LIMITS ##########################
    
    MAX_ROWS_PER_RUN = 100_000
    MAX_ROWS_PER_PARTITION = 15_000
    MIN_BATCH_SIZE = 1_000
    MAX_BATCH_SIZE = 10_000


    COUNT_BEFORE_WRITE = False

    ENABLE_CHUNKING = False

    APP_NAME = "BaseSparkJob"

    def __init__(self, batch_size: int | None = None, partitions: int | None = None):
        
        ####################### MySQL connection config ##########################
        
        self.mysql_host = config("MYSQL_HOST", default="127.0.0.1")
        self.mysql_port = config("PORT", default="3306")
        self.mysql_db   = config("MYSQL_DATABASE", default="washmen_dw")
        self.mysql_user = config("MYSQL_USER", default="root")
        self.mysql_pass = config("MYSQL_PASSWORD", default="password")

        self.base_batch_size = int(
            batch_size
            or config("SPARK_JDBC_BATCH_SIZE", default=str(self.DEFAULT_BATCH_SIZE))
        )

        self.base_partitions = int(
            partitions
            or config("SPARK_DEFAULT_PARTITIONS", default=str(self.DEFAULT_PARTITIONS))
        )

        
        ####################### JDBC URL ##########################
        
        self.jdbc_url = (
            f"jdbc:mysql://{self.mysql_host}:{self.mysql_port}/{self.mysql_db}"
            "?useSSL=false"
            "&rewriteBatchedStatements=true"
            "&useServerPrepStmts=true"
            "&cachePrepStmts=true"
            "&prepStmtCacheSize=250"
            "&prepStmtCacheSqlLimit=2048"
            "&allowMultiQueries=true"
        )

        self.jdbc_props: Dict[str, str] = {
            "user": self.mysql_user,
            "password": self.mysql_pass,
            "driver": self.JDBC_DRIVER,
            "batchsize": str(self.base_batch_size),
        }

        
        ####################### SparkSession ##########################
        
        self.spark = (
            SparkSession.builder
            .appName(self.APP_NAME)
            .config("spark.jars.packages", "mysql:mysql-connector-java:8.0.33")
            .config("spark.sql.shuffle.partitions", str(self.base_partitions))
            .config("spark.sql.adaptive.enabled", "true")
            .config("spark.sql.codegen.wholeStage", "false")
            .config("spark.sql.ansi.enabled", "false")
            .getOrCreate()
        )

        # self.spark.sparkContext.setLogLevel("WARN")
        self.spark.sparkContext.setLogLevel("ERROR")

        print(
            f"⚙️ Spark initialized | "
            f"batch_size={self.base_batch_size} | "
            f"partitions={self.base_partitions} | "
            f"max_rows_per_run={self.MAX_ROWS_PER_RUN} | "
            f"count_before_write={self.COUNT_BEFORE_WRITE} | "
            f"chunking={self.ENABLE_CHUNKING}"
        )

    ####################### READ HELPERS ##########################
    
    
    def read_table(self, table_name: str) -> DataFrame:
        return self.spark.read.jdbc(
            self.jdbc_url,
            table_name,
            properties=self.jdbc_props
        )

    def read_query(self, sql: str) -> DataFrame:
        query = f"({sql}) t"
        return self.spark.read.jdbc(
            self.jdbc_url,
            query,
            properties=self.jdbc_props
        )

    def table_exists(self, table_name: str) -> bool:
        q = f"""
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = '{self.mysql_db}'
          AND table_name = '{table_name}'
        LIMIT 1
        """
        return not self.read_query(q).rdd.isEmpty()

    ####################### WRITE PLANNER ##########################
    
    def _plan_write(self, row_count: int) -> dict:
        if row_count <= 0:
            return {"rows": 0, "partitions": 1, "batch_size": self.MIN_BATCH_SIZE}

        partitions = min(
            self.base_partitions,
            max(1, math.ceil(row_count / self.MAX_ROWS_PER_PARTITION))
        )

        rows_per_partition = math.ceil(row_count / partitions)

        batch_size = min(
            self.MAX_BATCH_SIZE,
            max(self.MIN_BATCH_SIZE, rows_per_partition // 2)
        )

        batch_size = min(batch_size, self.base_batch_size)

        return {
            "rows": row_count,
            "partitions": partitions,
            "batch_size": batch_size,
        }

    
    ####################### WRITE TABLE ##########################
    
    def write_table(self, df: DataFrame, table_name: str, mode: str = "append") -> None:
        """
        FINAL write strategy:

        FAST MODE (default):
        - NO driver-side codegen explosion
        - Spark/JDBC safely handles empty DataFrames
        """

        
        ####################### FAST MODE ##########################
        
        if not self.COUNT_BEFORE_WRITE:
            jdbc_props = dict(self.jdbc_props)
            jdbc_props["batchsize"] = str(self.base_batch_size)

            (
                df
                .repartition(self.base_partitions)
                .write
                .mode(mode)
                .jdbc(self.jdbc_url, table_name, properties=jdbc_props)
            )

            print(
                f"✅ JDBC write completed | "
                f"table={table_name} | "
                f"partitions={self.base_partitions} | "
                f"batch={self.base_batch_size}"
            )
            return

        
        ####################### SAFE MODE (EXPLICIT, SLOWER) ##########################
        
        total_rows = df.count()
        if total_rows == 0:
            print("ℹ️ No rows to write")
            return

        plan = self._plan_write(total_rows)

        jdbc_props = dict(self.jdbc_props)
        jdbc_props["batchsize"] = str(plan["batch_size"])

        (
            df
            .repartition(plan["partitions"])
            .write
            .mode(mode)
            .jdbc(self.jdbc_url, table_name, properties=jdbc_props)
        )

        print(
            f"✅ JDBC write completed (safe mode) | "
            f"rows={total_rows} | "
            f"partitions={plan['partitions']} | "
            f"batch={plan['batch_size']}"
        )

    
    ####################### EXECUTE RAW SQL ##########################
    
    def execute_sql(self, sql: str) -> None:
        jvm = self.spark._sc._jvm
        DriverManager = jvm.java.sql.DriverManager
        Properties = jvm.java.util.Properties

        props = Properties()
        props.setProperty("user", self.mysql_user)
        props.setProperty("password", self.mysql_pass)

        conn = None
        stmt = None
        try:
            conn = DriverManager.getConnection(self.jdbc_url, props)
            stmt = conn.createStatement()
            stmt.execute(sql)
        finally:
            if stmt:
                stmt.close()
            if conn:
                conn.close()

    def stop(self):
        self.spark.stop()
