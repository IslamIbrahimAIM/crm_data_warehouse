from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils



class GoldFactEventsJob(BaseSparkJob):
    """
    Gold Fact Events (Skeleton)
    """

    APP_NAME = "Gold Fact Events"

    SILVER_TABLE      = "crm_silver_events"
    DIM_USER          = "gold_dim_user"
    DIM_GEO           = "gold_dim_geo"
    DIM_DEVICE        = "gold_dim_device"
    DIM_DATE          = "gold_dim_date"
    TARGET_TABLE      = "gold_fact_events"

    def run(self):
        silver_df: DataFrame = self.read_table(self.SILVER_TABLE)
        
        silver = (
            silver_df
            .select(
                "event_sk",
                "user_sk",
                "device_sk",
                "event_type",
                "event_category",
                F.col("event_ts").alias("event_date")
            )
        )
        
        users = (
            self.read_table(self.DIM_USER)
            .select(
                "user_sk",
                "city"
            )
        )
        
        geo = (
            self.read_table(self.DIM_GEO)
            .select(
                "geo_sk",
                "city"
            )
        )
        
        device = (
            self.read_table(self.DIM_DEVICE)
            .select(
                "device_sk",
                "device_family",
                "os_family",
                "os_major_version",
                "browser_family",
                "browser_major_version",
            )
        )
        
        dates = (
            self.read_table(self.DIM_DATE)
            .select(
                "date_sk",
                "date_actual"
            )
        )
        
        df = (
            silver
            .join(users, on="user_sk", how="left")
            .join(geo, on="city", how="left")
            .join(device, on="device_sk", how="left")
            .join(dates, F.try_to_date(F.col("event_date")) == F.col("date_actual"), "left")
            .withColumnRenamed("date_sk", "event_date_sk")
            .drop("date_actual")
            .withColumn("dw_created_at", F.current_timestamp())            
        )
        
        
        cols = df.columns
        
        sk_cols = [c for c in cols if c.endswith("_sk")]
        other_cols = [c for c in cols if not c.endswith("_sk")]
        
        for c in sk_cols + other_cols:
            print(f'"{c}",')
        
        # df.show(20, False)
        
        final_df = (
            df
            .select(
                "event_sk",
                "event_date_sk",
                "user_sk",
                "device_sk",
                "geo_sk",
                "event_date",
                "city",
                "event_type",
                "event_category",
                "device_family",
                "os_family",
                "os_major_version",
                "browser_family",
                "browser_major_version",
                "dw_created_at"
            )
        )
        
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["event_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["event_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")         

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldFactEventsJob()
    job.run()
    job.stop()