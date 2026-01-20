from typing import List

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverDevicesJob(BaseSparkJob):
    """
    Silver – Devices (Skeleton)
    """

    APP_NAME = "Silver_Devices"

    BRONZE_TABLE = "crm_bronze_devices"
    USERS_TABLE  = "crm_silver_users"
    TARGET_TABLE = "crm_silver_devices"

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("device_id", WarehouseUtils.clean_text(F.col("device_id")))
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("device_model", WarehouseUtils.clean_text(F.col("device_model")))
            .withColumn("mac_addr", WarehouseUtils.clean_text(F.col("mac_addr")))
            .withColumn(
                "platform",
                F.when(
                     WarehouseUtils.clean_text(F.col("platform")).isin("iphone", "ios", "apple"),
                     "ios"
                )
                .when(
                     WarehouseUtils.clean_text(F.col("platform")).isin("andriod", "androidd"),
                     "android"
                )
                .otherwise("web")        
                        )
            .withColumn(
                "os_family",
                F.when(F.col("device_model").rlike("windows nt"), "windows")
                 .when(F.col("device_model").rlike("android"), "android")
                 .when(F.col("device_model").rlike("iphone|ipad|cpu iphone os"), "ios")
                 .when(F.col("device_model").rlike("mac os x"), "macos")
                 .when(F.col("device_model").rlike("linux"), "linux")
                 .otherwise("unknown")
            )
            .withColumn(
                "os_major_version",
                F.regexp_extract(
                    F.col("device_model"),
                    r"(android|windows nt|os x|iphone os|ipad os)[ /_]?(\d+)",
                    2
                ).cast("int")
            )
            .withColumn(
                "browser_family",
                F.when(F.col("device_model").rlike("chrome|crios"), "chrome")
                 .when(F.col("device_model").rlike("firefox|fxios"), "firefox")
                 .when(F.col("device_model").rlike("safari") & ~F.col("device_model").rlike("chrome"), "safari")
                 .when(F.col("device_model").rlike("msie|trident"), "internet_explorer")
                 .when(F.col("device_model").rlike("opera"), "opera")
                 .otherwise("unknown")
            )
            .withColumn(
                "browser_major_version",
                F.regexp_extract(
                    F.col("device_model"),
                    r"(chrome|crios|firefox|fxios|msie|version|opera)[/ ](\d+)",
                    2
                ).cast("int")
            )
            .withColumn(
                "device_family",
                F.when(F.col("device_model").rlike("iphone"), "iphone")
                 .when(F.col("device_model").rlike("ipad"), "ipad")
                 .when(F.col("device_model").rlike("android"), "android")
                 .when(F.col("device_model").rlike("mac os x"), "mac")
                 .when(F.col("device_model").rlike("windows nt"), "windows_pc")
                 .otherwise("unknown")
            )
            .withColumn(
                "platform_os_mismatch",
                F.when(
                    (F.col("platform") == "ios") & (F.col("os_family") != "os"),
                    F.lit(1)
                )
                .when(
                    (F.col("platform") == "andriod") & (F.col("os_family") !="android"),
                    F.lit(1)
                )
                .when(
                    (F.col("platform") == "web") & (F.col("os_family").isin("ios", "android")),
                    F.lit(1)
                )
                .otherwise(0)
                .cast("int")
            )
            
        )
        
        users = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("user_sk")
            )           
        )
        
        df = (
            bronze
            .join(
                users,
                on="user_id",
                how="left"
            )
            .withColumn(
                "device_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("user_sk"),
                        F.col("device_id"),
                        F.col("os_family"),
                        F.col("device_family")
                    )
                )
            )
        )
        
        final_df = (
            df
            .select(
                "device_sk",
                "user_sk",
                "device_id",
                "user_id",
                "platform",
                "device_model",
                "device_family",
                "mac_addr",
                "os_family",
                "os_major_version",
                "browser_family",
                "browser_major_version",
                "platform_os_mismatch",                
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        # bronze.show(50, truncate=False)
        # bronze.select("platform").distinct().show(truncate=False)
        # for c in df.columns:
        #     print(f'"{c}",')
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
                .withColumn("platform_os_mismatch", F.col("platform_os_mismatch").cast("int"))
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
    job = SilverDevicesJob()
    job.run()
    job.stop()