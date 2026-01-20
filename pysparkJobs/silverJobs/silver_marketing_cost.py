from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverMktCostJob(BaseSparkJob):
    """
    Silver – Marketing Cost (Skeleton)
    """

    APP_NAME = "Marketing Cost"

    BRONZE_TABLE = "mkt_bronze_marketing_cost"
    TARGET_TABLE = "mkt_silver_marketing_cost"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"
    
    

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("spend_id", WarehouseUtils.clean_text(F.col("spend_id")))
            .withColumn("channel", WarehouseUtils.clean_text(F.col("channel")))
            .withColumn("spend", WarehouseUtils.clean_text(F.col("spend")).cast("decimal(10,2)"))
            .withColumn(
                "spend_date",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("spend_date")),
                    self.TS_FMT
                )
            )
            .withColumn(
                "marketing_cost_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("spend_id"),
                        F.col("channel"),
                        F.col("spend_date")
                    )
                )
            )
        )
        
        final_df = (
            bronze
            .select(
                "marketing_cost_sk",
                "spend_id",
                "channel",
                "spend",
                "spend_date",
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["marketing_cost_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["marketing_cost_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverMktCostJob()
    job.run()
    job.stop()