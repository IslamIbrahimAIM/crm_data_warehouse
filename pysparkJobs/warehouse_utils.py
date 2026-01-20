from pathlib import Path
from typing import List, Optional
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame
from pyspark.sql.types import (
    StringType, IntegerType, LongType, DecimalType, DoubleType,
    BooleanType, DateType, TimestampType
)


class WarehouseUtils:
    
    ####################### TRAILING ? CLEANING ##########################
    
    @staticmethod
    def clean_text(col):
        return (
            F.when(col.isNull(), None)
             .otherwise(
                 F.lower(
                     F.trim(
                         F.regexp_replace(
                             F.regexp_replace(col, r"\?+", ""),
                             r"\s+", " "
                         )
                     )
                 )
             )
        )
        
    ####################### EXTRACTING HOURS ##########################
    
    @staticmethod
    def extract_hour_24(col):
        return F.when(col.isNull(), None).otherwise(F.hour(col))
    
    
    ####################### Normalize Cities ##########################
    
    @staticmethod
    def normalize_city(col):
        c = WarehouseUtils.clean_text(col)
        
        return (
            F.when(c.isNull(), None)
            .when(c == "ajman", "Ajman")
            .when(c.isin("abudhabi", "abu dhabi"), "Abu Dhabi")
            .when(c == "al ain", "Al Ain")
            .when(c.isin("sharjah", "shj"), "Sharjah")
            .when(c.isin("dubai", "dubayy", "dxb"), "Dubai")
            .when(c.isin("fujairah", "fujaira", "fu jairah"), "Fujairah")
            .when(c.isin("rak", "ras al khaimah"), "Ras Al Khaimah")
            .otherwise(F.initcap(c))
        )
        
        
    ####################### Normalize Providers ##########################
    
    @staticmethod
    def normalize_provider(col):
        c = WarehouseUtils.clean_text(col)
        
        return (
            F.when(c.isNull(), None)
             .when(c == "cash", "cash")
             .when(c == "tap", "tap")
             .when(c.isin("stripee", "stripe"), "stripe")
             .when(c == "apple_pay", "apple-pay")
             .otherwise(c)
        )
        
    ####################### Normalize Payment Method ##########################
    
    @staticmethod
    def normalize_payment_method(col):
        c = WarehouseUtils.clean_text(col)
        
        return (
            F.when(c.isNull(), None)
             .when(c.isin("cash", "tap"), "Cash On Delivery")
             .when(c.isin("stripee", "stripe", "apple_pay", "apple-pay"), "Online")
             .otherwise(c)
        )
        
    ####################### Normalize Order Status ##########################
    
    @staticmethod
    def normalize_order_status(col):
        c = WarehouseUtils.clean_text(col)
        
        return (
            F.when(c.isNull(), None)
             .when(c.isin("canceled", "cancelled"), "canceled")
             .when(c.isin("in_progress", "in-progress", "inprogress", "pending"), "in-progress")
             .when(c.isin("confirmed", "done", "complete", "completed"), "complete")
             .otherwise(c)
        )
    
    ####################### Generating Surrogate Key ##########################
    
    @staticmethod
    def surrogate_key(col):
        return (
            F.when(col.isNull(), None)
            .otherwise(
                F.lower(
                    F.substring(
                        F.base64(F.sha2(WarehouseUtils.clean_text(col), 256)),
                        1,
                        26
                    )
                )
            )
        )
        
    ####################### Name Parser ##########################
    
    @staticmethod
    def parse_name(full_name_col):
        honorifics = ["mr", "mr.", "ms", "ms.", "mrs", "mrs.", "dr", "dr.", "prof", "prof."]
        
        cleaned     = WarehouseUtils.clean_text(full_name_col)
        tokens      = F.split(cleaned, " ")
        first_token = tokens.getItem(0)
        
        name_wo_title = F.when(
            first_token.isin(honorifics),
            F.trim(
                F.expr(
                    f"substring({full_name_col._jc.toString()}, instr({full_name_col._jc.toString()}, ' ') + 1)"
                )
            )
        ).otherwise(cleaned)
        
        first_name = F.split(name_wo_title, " ").getItem(0)
        
        last_name = F.when(
            F.size(F.split(name_wo_title, " ")) > 1,
            F.trim(
                F.expr(
                    f"substring({name_wo_title._jc.toString()}, length({first_name._jc.toString()}) + 2)"
                )
            )
        ).otherwise(None)
        
        initials = F.when(
            first_token.isin(honorifics),
            F.initcap(F.regexp_replace(first_token, r"\.",""))
        ).otherwise(None)
        
        return (
            initials.alias("initials"),
            first_name.alias("first_name"),
            last_name.alias("last_name")
        )
        
        
        ####################### Lifecycle Validation ##########################
        
    @staticmethod
    def flag_invalid_lifecycle(
        *,
        df: DataFrame,
        partition_cols: List[str],
        status_col: str,
        ts_col: str,
        terminal_statuses: List[str],
        regression_statuses: List[str],
        terminal_flag_col: str = "has_terminal_before",
        invalid_flag_col: str = "is_invalid_stage"
    ) -> DataFrame:
        w = (
            Window
            .partitionBy(*partition_cols)
            .orderBy(F.col(ts_col))
            .rowsBetween(Window.unboundedPreceding, -1)
        )
        df = (
            df
            .withColumn(
            terminal_flag_col,
            F.max(
                F.when(
                    F.col(status_col).isin(*terminal_statuses),
                    F.lit(1)
                ).otherwise(F.lit(0))
              )
            .over(w)
            )
            .withColumn(
                invalid_flag_col,
                F.when(
                    (F.col(status_col).isin(*regression_statuses)) &
                    (F.col(terminal_flag_col) == 1),
                    F.lit(1)
                ).otherwise(F.lit(0))
            )
        )
        return df
    
    
    ####################### Incremental Filter ##########################
    
    @staticmethod
    def incremental_filter(*,candidate: DataFrame, existing: DataFrame, key_cols: List[str]) -> DataFrame:
        """
        Docstring for incremental_filter
        
        :param candidate: Description
        :type candidate: DataFrame
        :param existing: Description
        :type existing: DataFrame
        :param key_cols: Description
        :type key_cols: List[str]
        :return: Description
        :rtype: DataFrame
        Keep only rows not present in existing dataset
        """
        return (
            candidate
            .join(
                existing.select(*key_cols).dropDuplicates(),
                on=key_cols,
                how="left_anti"
            )
        )
        
    ####################### Preserve Unaffected Existing ##########################
    @staticmethod
    def preserve_unaffected_existing(*, existing: DataFrame, incoming: DataFrame, key_cols: List[str]) -> DataFrame:
        """
        Docstring for preserve_unaffected_existing
        
        :param existing: Description
        :type existing: DataFrame
        :param incoming: Description
        :type incoming: DataFrame
        :param key_cols: Description
        :type key_cols: List[str]
        :return: Description
        :rtype: DataFrame
        Preserve rows not touched by incoming changes
        """
        unaffected = (
            existing
            .join(
                incoming.select(*key_cols).dropDuplicates(),
                on=key_cols,
                how="left_anti"
            )
        )
        return unaffected.unionByName(incoming)
    
    
    ####################### Creating DDL Per Table ##########################
    
    @staticmethod
    def spark_type_to_sql(dtype) -> str:
        if isinstance(dtype, IntegerType):
            return "INT"
        if isinstance(dtype, LongType):
            return "BIGINT"
        if isinstance(dtype, DecimalType):
            return f"DECIMAL({dtype.precision},{dtype.scale})"
        if isinstance(dtype, DoubleType):
            return "DOUBLE"
        if isinstance(dtype, DateType):
            return "DATE"
        if isinstance(dtype, TimestampType):
            return "DATETIME"
        if isinstance(dtype, BooleanType):
            return "BOOLEAN"
        return "VARCHAR(255)"


    @staticmethod
    def generate_and_create_table(
        *,
        df: DataFrame,
        table_name: str,
        layer: str,
        base_dir: Path,
        job,
        primary_keys: Optional[List[str]] = None,
        indexes: Optional[List[List[str]]] = None,
        column_type_overrrides: dict | None = None
    ):
        ddl_dir = base_dir / "db_ddls" / layer
        ddl_dir.mkdir(parents=True, exist_ok=True)
        
        column_type_overrrides = column_type_overrrides or {}

        ddl_lines: List[str] = []

        for field in df.schema.fields:
            if field.name in column_type_overrrides:
                meta = column_type_overrrides[field.name]
                sql_type = f"{meta['type']}({meta['length']})"
            else:
                sql_type = WarehouseUtils.spark_type_to_sql(field.dataType)
            nullable = "" if field.nullable else " NOT NULL"
            ddl_lines.append(f"    `{field.name}` {sql_type}{nullable}")


        if primary_keys:
            pk_cols = ", ".join(f"`{c}`" for c in primary_keys)
            ddl_lines.append(f"    PRIMARY KEY ({pk_cols})")


        if indexes:
            for cols in indexes:
                idx_name = f"idx_{table_name}_{'_'.join(cols)}"
                col_list = ", ".join(f"`{c}`" for c in cols)
                ddl_lines.append(f"    KEY `{idx_name}` ({col_list})")


        ddl = (
            f"DROP TABLE IF EXISTS {table_name};\n"
            f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
            + ",\n".join(ddl_lines)
            + "\n) ENGINE=InnoDB;"
        )

        ddl_file = ddl_dir / f"{table_name}.sql"
        ddl_file.write_text(ddl)
        
        job.spark._jvm.org.apache.spark.sql.execution.datasources.jdbc.DriverRegistry.register(
            job.JDBC_DRIVER
        )

        statements = [
            stmt.strip()
            for stmt in ddl.split(";")
            if stmt.strip()
        ]

        for stmt in statements:
            job.execute_sql(stmt)

        return ddl
    
    
    