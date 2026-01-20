from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverMktAttributeJob(BaseSparkJob):
    """
    Silver – Marketing Attribute (Skeleton)
    """

    APP_NAME = "Marketing Attribute"

    BRONZE_TABLE = "mkt_bronze_marketing_attribution"
    USERS_TABLE  = "crm_silver_users"
    TARGET_TABLE = "mkt_silver_marketing_attribution"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("attrib_id", WarehouseUtils.clean_text(F.col("attrib_id")))
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("channel", WarehouseUtils.clean_text(F.col("channel")))
            .withColumn("campaign", WarehouseUtils.clean_text(F.col("campaign")))
            .withColumn("medium", WarehouseUtils.clean_text(F.col("medium")))
            .withColumn("source", WarehouseUtils.clean_text(F.col("source")))
            .withColumn(
                "touch_ts",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("touch_ts")),
                    self.TS_FMT
                )
            )
        )

        w = Window.partitionBy("user_id").orderBy(F.col("touch_ts").asc_nulls_last())
        
        bronze = (
            bronze
            .withColumn("rn", F.row_number().over(w))
            .withColumn(
                "is_first_touch",
                F.when(F.col("rn") == 1, F.lit(1)).otherwise(F.lit(0))
            )
            .drop("rn")
        )
        
        users = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("user_sk")
            )
        )
        
        df = (
            bronze.join(users, on="user_id", how="left")
            .withColumn(
                "marketing_attribution_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("attrib_id"),
                        F.col("user_sk"),
                        F.col("channel"),
                        F.col("campaign"),
                        F.col("medium"),
                        F.col("source"),
                        F.col("touch_ts")
                    )
                )
            )
        )
        
        final_df = (
            df
            .select(
                "marketing_attribution_sk",
                "user_sk",
                "attrib_id",
                "user_id",
                "channel",
                "campaign",
                "medium",
                "source",
                "is_first_touch",
                "touch_ts"
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
                .withColumn("is_first_touch", F.col("is_first_touch").cast("int"))
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["marketing_attribution_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["marketing_attribution_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")
        
            
    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverMktAttributeJob()
    job.run()
    job.stop()