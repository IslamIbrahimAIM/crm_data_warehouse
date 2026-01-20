from pyspark.sql import functions as F
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob
from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverEventsJob(BaseSparkJob):
    """
    Silver – Events
    Includes PySpark-only data quality checks for users & devices
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

    SIGNUP_TYPES     = ["signup", "signup_started"]
    COMMERCE_TYPES   = ["order_start", "order_completed"]
    ENGAGEMET_TYPES  = ["open", "app_open", "open_app", "open", "view", "view_page"]

    ####################### Helpers ##########################

    def parse_multi(self, col: F.Column, formats: list[str]) -> F.Column:
        ts = F.to_timestamp(col, formats[0])
        for fmt in formats[1:]:
            ts = F.coalesce(ts, F.to_timestamp(col, fmt))
        return ts

    ####################### Main Run ##########################

    def run(self):

        # -----------------------------
        # 1️⃣ Read & CLEAN bronze events
        # -----------------------------
        bronze = (
            self.read_table(self.BRONZE_TABLE)
            .withColumn("event_id", WarehouseUtils.clean_text(F.col("event_id")))
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("device_id", WarehouseUtils.clean_text(F.col("device_id")))
            .withColumn("event_type", WarehouseUtils.clean_text(F.col("event_type")))
            .withColumn(
                "event_ts",
                self.parse_multi(
                    WarehouseUtils.clean_text(F.col("event_ts")),
                    self.EVENT_TS_FORMATS
                )
            )
            .filter(F.col("user_id").isNotNull())
            .filter(F.col("event_ts").isNotNull())
        )

        # -----------------------------
        # 2️⃣ Load SILVER dimensions
        # -----------------------------
        users   = self.read_table(self.USERS_TABLE).select("user_id").dropDuplicates()
        devices = self.read_table(self.DEVICES_TABLE).select("device_id", "user_id").dropDuplicates()

        # =====================================================
        # 🔎 DATA QUALITY CHECKS (PySpark)
        # =====================================================

        # 1️⃣ Events → missing users
        missing_users = (
            bronze.select("user_id").distinct()
            .join(users, on="user_id", how="left_anti")
        )
        print("❌ Users in events but missing in silver_users:")
        missing_users.show(20, False)

        # 2️⃣ Users → never seen in events
        orphan_users = (
            users.join(bronze.select("user_id").distinct(),
                       on="user_id",
                       how="left_anti")
        )
        print("⚠️ Users in silver_users but never in events:")
        orphan_users.show(20, False)

        # 3️⃣ Events → missing devices
        missing_devices = (
            bronze
            .filter(F.col("device_id").isNotNull())
            .select("device_id").distinct()
            .join(devices.select("device_id"), on="device_id", how="left_anti")
        )
        print("❌ Devices in events but missing in silver_devices:")
        missing_devices.show(20, False)

        # 4️⃣ Devices → never used in events
        orphan_devices = (
            devices.select("device_id").distinct()
            .join(bronze.select("device_id").distinct(),
                  on="device_id",
                  how="left_anti")
        )
        print("⚠️ Devices in silver_devices but never in events:")
        orphan_devices.show(20, False)

        # 5️⃣ Users whose device exists BUT events.device_id IS NULL
        users_with_null_event_device = (
            devices
            .join(bronze, on="user_id", how="inner")
            .filter(bronze.device_id.isNull())
            .select(devices.user_id, devices.device_id)
            .distinct()
        )
        print("🚨 Users with devices but events.device_id is NULL:")
        users_with_null_event_device.show(20, False)

        # 6️⃣ Mixed device attribution per user
        mixed_device_users = (
            bronze
            .groupBy("user_id")
            .agg(
                F.count("*").alias("total_events"),
                F.sum(F.when(F.col("device_id").isNull(), 1).otherwise(0)).alias("null_device_events"),
                F.sum(F.when(F.col("device_id").isNotNull(), 1).otherwise(0)).alias("with_device_events")
            )
            .filter(
                (F.col("null_device_events") > 0) &
                (F.col("with_device_events") > 0)
            )
        )
        print("⚠️ Users with mixed device attribution:")
        mixed_device_users.show(20, False)

        print("✅ PySpark data-quality checks completed.")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverEventsJob()
    job.run()
    job.stop()
