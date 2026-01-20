from pyspark.sql import functions as F
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob
from pysparkJobs.warehouse_utils import WarehouseUtils


class DimUserJob(BaseSparkJob):
    """
    Silver – Dim User (Skeleton)
    """

    APP_NAME = "Dim User"

    SILVER_TABLE = "crm_silver_users"
    PREF_TABLE   = "crm_silver_user_preferences"
    TARGET_TABLE = "gold_dim_user"

    def run(self):
        silver_df: DataFrame = self.read_table(self.SILVER_TABLE)
        
        df = (
            silver_df
            .select(
                "user_sk",
                "full_name",
                "first_name",
                "last_name",
                "email",
                "phone",
                "signup_date",
                F.col("status").alias("user_status"),
                "city"  
            )
        )
        
        pref = (
            self.read_table(self.PREF_TABLE)
            .select(
                "user_sk",
                "pref_key",
                "pref_value"
            )
        )

        pref_pivot = (
            pref
            .groupBy("user_sk")
            .pivot("pref_key",["language", "offers", "notifications"])
            .agg(F.first("pref_value"))
        )
        
        pref_final = (
            pref_pivot
            .withColumnRenamed("language", "pref_language")
            .withColumn(
                "offers_enabled",
                F.when(F.col("offers") == "yes", F.lit(1))
                 .when(F.col("offers") == "no", F.lit(0))
                 .otherwise(None)
                 .try_cast("int")
            )
            .withColumn(
                "notifications_enabled",
                F.when(F.col("notifications") == "yes", F.lit(1))
                 .when(F.col("notifications") == "no", F.lit(0))
                 .otherwise(None)
                 .try_cast("int")
            )
            .drop("offers", "notifications")
        )
        
        final_df = (
            df.join(pref_final, on="user_sk", how="left")
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        
        # final_df = (
        #     final_df
        #     .select(
                
        #     )
        # )
        
        
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
                .withColumn("offers_enabled", F.col("offers_enabled").cast("int"))
                .withColumn("notifications_enabled", F.col("notifications_enabled").cast("int"))
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["user_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["user_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")
            
        
        # final_df.show(20, False)
    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = DimUserJob()
    job.run()
    job.stop()