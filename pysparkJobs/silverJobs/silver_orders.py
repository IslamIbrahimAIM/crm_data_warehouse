from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils



class SilverOrdersJob(BaseSparkJob):
    """
    Silver – Orders (Skeleton)
    """

    APP_NAME = "Silver_Orders"

    BRONZE_TABLE     = "crm_bronze_orders"
    USERS_TABLE      = "crm_silver_users"
    TARGET_TABLE     = "crm_silver_orders"
    
    CREATED_AT_FORMATS = [
        "dd-MM-yyyy HH:mm:ss",
        "MM-dd-yyyy HH:mm:ss",
        "dd/MM/yyyy HH:mm",
        "yyyy-MM-dd HH:mm:ss",
        "MMM dd yyyy HH:mm",        
    ]
    
    ####################### Helpers ##########################
    
    def parse_multi(self, col: F.Column, formats: list[str]) -> F.Column:
        ts = F.to_timestamp(col, formats[0])
        for fmt in formats[1:]:
            ts = F.coalesce(ts, F.to_timestamp(col, fmt))
        return ts
    


    def enforce_order_user_guard(self, df: DataFrame) -> DataFrame:
        """
        Docstring for enforce_order_user_guard
        
        Ensure a single canonical user per order_id
        Oldest create_at wins
        """
        
        w = (
            Window
            .partitionBy("order_id")
            .orderBy(F.col("created_at").asc_nulls_last())
        )
        canonical_user = (
            df
            .withColumn("rn", F.row_number().over(w))
            .filter(F.col("rn") == 1)
            .select("order_id", F.col("user_id").alias("canonical_user_id"))
        )
        return (
            df
            .join(canonical_user, on="order_id", how="inner")
            .filter(F.col("user_id") == F.col("canonical_user_id"))
            .drop("canonical_user_id")
        )
        
    def incremental_filter(self, candidate: DataFrame) -> DataFrame:
        if not self.table_exists(self.TARGET_TABLE):
            return candidate
        
        existing = (
            self.read_table(self.TARGET_TABLE)
            .select("order_id", "user_id", "order_status", "created_at")
            .dropDuplicates()
        )
        
        return (
            candidate
            .join(
                existing,
                on=["order_id", "user_id", "order_status", "created_at"],
                how="left_anti"
            )
        )


    ####################### Main Run ##########################
    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("order_id", WarehouseUtils.clean_text(F.col("order_id")))
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn(
                "created_at",
                self.parse_multi(
                    WarehouseUtils.clean_text(F.col("created_at")),
                    self.CREATED_AT_FORMATS
                )
            )
            .withColumn("order_status", WarehouseUtils.normalize_order_status(F.col("order_status")))
            .withColumn("payment_provider", WarehouseUtils.normalize_provider(F.col("payment_provider")))
            .withColumn("line_total", WarehouseUtils.clean_text(F.col("line_total")).cast("decimal(10,2)"))
            .withColumn("payment_method", WarehouseUtils.normalize_payment_method(F.col("payment_provider")))
        )
                
        guarded = self.enforce_order_user_guard(bronze)
        
        users = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("user_sk"),                
            )
            .dropDuplicates(["user_id"])
        )
        df = (
           guarded
           .join(
               users,
               on="user_id",
               how="left"
           ) 
        )
        
        df = (
            df
            .withColumn(
                "order_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("order_id"),
                        F.col("user_id"),
                        F.col("created_at")
                    )
                )
            )
            .withColumn(
                "provider_sk",
                WarehouseUtils.surrogate_key(F.col("payment_provider"))
            )
        )
        
        final_df = (
            df
            .select(
                "order_sk",
                "user_sk",
                "provider_sk",
                "order_id",
                "user_id",
                "created_at",
                "order_status",
                "payment_provider",
                "payment_method",
                "line_total",                
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        incremental = self.incremental_filter(final_df)
        
        if not incremental.take(1):
            print("No new crm_silver_orders rows detected. Skipping write.")
            return
        if not self.table_exists(self.TARGET_TABLE):
            write_df = incremental
        else:
            existing = self.read_table(self.TARGET_TABLE)
            write_df = existing.unionByName(incremental)
            
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")
        print("crm_silver_orders reconciled incrementally")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverOrdersJob()
    job.run()
    job.stop()