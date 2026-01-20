from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils



class GoldDimDevicesJob(BaseSparkJob):
    """
    Silver – Gold Dim Device (Skeleton)
    """

    APP_NAME = "Gold Dim Device"

    SILVER_TABLE = "crm_silver_devices"
    TARGET_TABLE = "gold_dim_device"

    def run(self):
        silver_df: DataFrame = self.read_table(self.SILVER_TABLE)
        
        silver = (
            silver_df
            .select(
                "device_sk",
                "device_family",
                "os_family",
                "os_major_version",
                "browser_family",
                "browser_major_version",
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        final_df = silver
        
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["device_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["device_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")        

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldDimDevicesJob()
    job.run()
    job.stop()