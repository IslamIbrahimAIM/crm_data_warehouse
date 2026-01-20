from typing import List

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame
from pyspark.storagelevel import StorageLevel

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverEventsJob(BaseSparkJob):
    """
    Silver – Events (Skeleton)
    """

    APP_NAME = "Silver_Events"

    BRONZE_TABLE  = "crm_bronze_events"
    USERS_TABLE   = "crm_silver_users"
    DEVICES_TABLE = "crm_silver_devices"
    TARGET_TABLE  = "crm_silver_events"
    
    EVENT_TS_FORMATS = [
        "dd/MM/yyyy HH:mm",
        "MM/dd/yyyy HH:mm",
        "yyyy-MM-dd HH:mm:ss",
        "MMM dd yyyy HH:mm"
    ]
    
    SIGNUP_TYPES    = ["signup", "signup_started", "signup-started"]
    COMMERCE_TYPES  = ["order_start", "order_completed", "add-to-cart", "order-complete"]
    ENGAGEMET_TYPES = ["open", "app_open", "open_app", "open","view", "view_page", "app-open"]
    
    ####################### Helpers ##########################
    
    def parse_multi(self, col: F.Column, formats: list[str]) -> F.Column:
        ts = F.to_timestamp(col, formats[0])
        for fmt in formats[1:]:
            ts = F.coalesce(ts, F.to_timestamp(col, fmt))
        return ts
    
    
    def normalize_event(self, col_clean):
        return (
            F.when(col_clean.isNull() | (col_clean == ""), None)
             .when(col_clean.isin(*self.SIGNUP_TYPES), F.lit("Signup-Started"))
             .when(col_clean.isin("open", "app_open", "open_app", "open"), F.lit("App-Open"))
             .when(col_clean.isin("view", "view_page"), F.lit("View"))
             .when(col_clean == "order_start", F.lit("Add-To-Cart"))
             .when(col_clean == "order_completed", F.lit("Order-Complete"))
             .otherwise(col_clean)
        )

    def categorize_event(self, event_type_clean):
        return (
            F.when(event_type_clean.isNull() | (event_type_clean == ""), None)
             .when(event_type_clean.isin(*self.SIGNUP_TYPES), F.lit("Signup"))
             .when(event_type_clean.isin(*self.COMMERCE_TYPES), F.lit("Commerce"))
             .when(event_type_clean.isin(*self.ENGAGEMET_TYPES), F.lit("Engagement"))
             .otherwise(F.lit("Other"))
        )
        
 
    
    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("event_id", WarehouseUtils.clean_text(F.col("event_id")))
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("event_type", WarehouseUtils.clean_text(F.col("event_type")))
            .withColumn("event_ts",
                        self.parse_multi(WarehouseUtils.clean_text(F.col("event_ts"))
                                         ,self.EVENT_TS_FORMATS))
            .withColumn("device_id", WarehouseUtils.clean_text(F.col("device_id")))
            .withColumn("event_type", self.normalize_event(WarehouseUtils.clean_text(F.col("event_type"))))
            .withColumn("event_category", self.categorize_event(WarehouseUtils.clean_text(F.col("event_type"))))
        )
        
        event_device_counts = (
            bronze
            .filter(F.col("device_id").isNotNull())
            .groupBy("user_id", "device_id")
            .agg(
                F.count("*").alias("event_cnt"),
                F.max("event_ts").alias("last_seen_ts")
            )
        )
        
        w = Window.partitionBy("user_id").orderBy(
            F.col("event_cnt").desc(),
            F.col("last_seen_ts").desc()
        )
        
        most_used_device = (
            event_device_counts
            .withColumn("rn", F.row_number().over(w))
            .filter(F.col("rn") == 1)
            .select(
                "user_id",
                F.col("device_id").alias("event_device_id")
            )
        )
        
        bronze_backfilled = (
            bronze
            .join(
                most_used_device, on="user_id", how="left"
            )
            .withColumn(
                "device_id",
                F.when(
                    F.col("device_id").isNull() & F.col("event_device_id").isNotNull(),
                    F.col("event_device_id")
                ).otherwise(F.col("device_id"))
            )
            .drop("event_device_id")
        )
        
        ####################### confirmation ##########################
        null_before = bronze.filter(F.col("device_id").isNull()).count()
        null_after = bronze_backfilled.filter(F.col("device_id").isNull()).count()
        total_events = bronze.count()
        
        
        print(f"Before backfill NULL device_id: {null_before} / {total_events}")
        print(f"After backfill NULL device_id: {null_after} / {total_events}")
        print(f"Resolved by events derived backfill: {null_before - null_after}")
        
        if null_after > 0:
            print("events still missing device_id")
            (
                bronze_backfilled
                .filter(F.col("device_id").isNull())
                .select("user_id", "event_id", "event_type", "event_ts")
                .show(20, False)
            )
        
        signup_users = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("signup_date")
            )
        )
        
        signup_events = (
            bronze_backfilled
            .filter(F.col("event_category") == F.lit("Signup"))
            .join(signup_users, on="user_id", how="left")
            .withColumn(
                "event_ts",
                F.when(
                    F.col("event_category") == F.lit("Signup"),
                    F.col("signup_date")
                )
                .otherwise(F.col("event_ts"))
            )
        )
        
        w_signup = Window.partitionBy("user_id").orderBy(
            F.col("event_ts").asc_nulls_last(),
            F.col("event_id").asc_nulls_last()
        )
        
        signup_only = (
            signup_events
            .withColumn("rn", F.row_number().over(w_signup))
            .filter(F.col("rn") == 1)
            .drop("rn", "signup_date")
        )
        
        non_signup_events = bronze_backfilled.filter(F.col("event_category") != F.lit("Signup"))
        
        final_events = non_signup_events.unionByName(signup_only)
        
        user_key = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("user_sk")
            )
        )
        
        devices_key = (
            self.read_table(self.DEVICES_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("device_id")).alias("device_id"),
                F.col("device_sk")
            )
        )
        
        df = (
            final_events
            .join(
                user_key,
                on="user_id",
                how="left"
            )
            .join(
                devices_key,
                on="device_id",
                how="left"
            )
            .withColumn(
                "event_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("event_id"),
                        F.col("user_sk"),
                        F.col("device_sk"),
                        F.col("event_ts")
                    )
                )
            )
        )
        
        
        final_df = (
            df
            .select(
               "event_sk",
               "device_sk",
               "user_sk",
               "event_id",
               "user_id",
               "device_id",
               "event_type",
               "event_category",
               "event_ts", 
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        
        
        # if self.table_exists(self.TARGET_TABLE):
        #     existing = (
        #         self.read_table(self.TARGET_TABLE)
        #         .select(
        #             "event_sk",
        #             "device_sk",
        #             "user_sk",
        #             "event_id",
        #             "user_id",
        #             "device_id",
        #             "event_type",
        #             "event_category",
        #             "event_ts",
        #             "dw_created_at"                     
        #         )
                
        #     )
            
            
        #     incremental = WarehouseUtils.incremental_filter(
        #         candidate=final_df,
        #         existing=existing,
        #         key_cols=["event_sk"]
        #     )
            
        #     write_df = WarehouseUtils.preserve_unaffected_existing(
        #         existing=existing,
        #         incoming=incremental,
        #         key_cols=["event_sk"]
        #     )
        # else:
        #     write_df = final_df
        self.write_table(final_df.coalesce(4), self.TARGET_TABLE, mode="append")
        
        # print(f"count of bronze_df {bronze_backfilled.count()}")
        # print(f"count of final events {final_events.count()}")
        
        # bronze.show(50, truncate=False)

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverEventsJob()
    job.run()
    job.stop()


