from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils



class GoldDimGeoJob(BaseSparkJob):
    """
    Silver – Gold Dim Geo (Skeleton)
    """

    APP_NAME = "Gold Dim Geo"

    SILVER_TABLE = "crm_silver_geo"
    TARGET_TABLE = "gold_dim_geo"

    def run(self):
        silver_df: DataFrame = self.read_table(self.SILVER_TABLE)
        
        silver = (
            silver_df
            .select(
                "geo_sk",
                "city",
                "country",
                "latitude",
                "longitude"
            )
        )
        
        final_df = (
            silver
            .groupBy("geo_sk","country","city")
            .agg(
                F.try_avg("latitude").alias("latitude"),
                F.try_avg("longitude").alias("longitude")
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
                key_cols=["geo_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["geo_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")  

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldDimGeoJob()
    job.run()
    job.stop()