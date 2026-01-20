from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverUserJob(BaseSparkJob):
    """
    Silver – User (Skeleton)
    """

    APP_NAME = "Silver_Users"

    BRONZE_TABLE  = "crm_bronze_users"
    EVENTS_TABLE  = "crm_bronze_events"
    GEO_TABLE     = "crm_silver_geo"
    TARGET_TABLE  = "crm_silver_users"
    
    CANONICAL_SIGNUP_EVENT_TYPES = ["signup", "signup_started"]
    
    SIGNUP_DATE_FORMATS = [
        "yyyy-MM-dd"
    ]
    
    EVENT_TS_FORMATS = [
        "dd/MM/yyyy HH:mm",
        "MM/dd/yyyy HH:mm",
        "yyyy-MM-dd HH:mm:ss",
        "yyyy-MM-dd HH:mm:ss.SSSSSS",
        "MMM dd yyyy HH:mm",        
    ]
    
    
    ####################### HELPERS ##########################
    
    def parse_multi(self, col: F.Column, formats: list[str]) -> F.Column:
        ts = F.to_timestamp(col, formats[0])
        for fmt in formats[1:]:
            ts = F.coalesce(ts, F.to_timestamp(col, fmt))
        return ts
    
    def canonical_ts(self, user_ts: F.Column, event_ts: F.Column) -> F.Column:
        return (
            F.when(user_ts.isNull(), event_ts)
             .when(event_ts.isNull(), user_ts)
             .otherwise(F.least(user_ts, event_ts))
        )
        
    @staticmethod
    def normalize_status(col: F.Column) -> F.Column:
        s = WarehouseUtils.clean_text(col)
        return (
            F.when(s.isNull() | (s == ""), None)
             .when(s.isin("active", "enabled", "verified", "activ"), "active")
             .when(s.isin("inactive", "disabled", "in-active", "in-actve"), "inactive")
             .when(s.isin("blocked", "banned", "suspended"), "blocked")
             .when(s.isin("deleted", "removed"), "deleted")
             .when(s.isin("pending", "pending_verification"), "pending")
             .otherwise(None)
        )
        
    def incremental_filter(self, candidate_df: DataFrame) -> DataFrame:
        if not self.table_exists(self.TARGET_TABLE):
            return candidate_df
        existing = (
            self.read_table(self.TARGET_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("signup_date").alias("signup_date_existing"),
            )
            .dropDuplicates(["user_id"])
        )
        return (
            candidate_df
            .join(existing, on="user_id", how="left")
            .filter(
                F.col("signup_date_existing").isNull()
                | (
                    F.col("signup_date").isNotNull()
                    & (F.col("signup_date") != F.col("signup_date_existing"))
                )
            )
            .drop("signup_date_existing")
        )
    
    def preserve_unaffected_existing(self, incremental_users: DataFrame) -> DataFrame:
        if not self.table_exists(self.TARGET_TABLE):
            return None
        existing = self.read_table(self.TARGET_TABLE)
        
        return (
            existing.join(
                incremental_users.select("user_id").dropDuplicates(["user_id"]),
                on="user_id",
                how="left_anti"
            )
        )
        
    def oldest_signup_wins(self) -> DataFrame:
        e = (
            self.read_table(self.EVENTS_TABLE)
            .select("user_id", "event_type", "event_ts")
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("event_type_clean", WarehouseUtils.clean_text(F.col("event_type")))
            .withColumn("event_ts_raw", F.col("event_ts").cast("string"))
            .withColumn("event_ts_parsed", self.parse_multi(F.col("event_ts_raw"), self.EVENT_TS_FORMATS))
            .filter(F.col("user_id").isNotNull() & (F.col("user_id") != ""))
            .filter(F.col("event_type_clean").isin(*self.CANONICAL_SIGNUP_EVENT_TYPES))
            .filter(F.col("event_ts_parsed").isNotNull())
        )
        oldest = (
            e.groupBy("user_id")
             .agg(F.min("event_ts_parsed").alias("event_signup_ts"))
        )
        
        return oldest
    ####################### MAIN RUN ##########################
    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("full_name", WarehouseUtils.clean_text(F.col("full_name")))
            .withColumn("email", WarehouseUtils.clean_text(F.col("email")))
            .withColumn("phone", WarehouseUtils.clean_text(F.col("phone")))
            .withColumn("status_raw", WarehouseUtils.clean_text(F.col("status")))
            .withColumn("city", WarehouseUtils.clean_text(F.col("city_raw")))
            .withColumn("address_raw", WarehouseUtils.clean_text(F.col("address_raw")))
            .withColumn("signup_ts_raw", F.col("signup_date").cast("string"))
            .withColumn("user_signup_ts", self.parse_multi(F.col("signup_ts_raw"), self.SIGNUP_DATE_FORMATS))
            .filter(F.col("user_id").isNotNull() & (F.col("user_id") != ""))
            .dropDuplicates(["user_id"])
        )
        oldest_event = self.oldest_signup_wins()
        
        candidate = (
            bronze
            .join(F.broadcast(oldest_event), on="user_id", how="left")
            .withColumn(
                "signup_date",
                self.canonical_ts(F.col("user_signup_ts"), F.col("event_signup_ts"))
            )
            .drop("event_signup_ts")
            .filter(F.col("signup_date").isNotNull())
        )
        
        candidate = (
            candidate
            .withColumn("status", self.normalize_status(F.col("status_raw")))
            .withColumn("city_key", WarehouseUtils.normalize_city(F.col("city_raw")))
            .drop("status_raw")
        )
        
        geo = (
            self.read_table(self.GEO_TABLE)
            .select(
                F.col("geo_sk"),
                F.col("city")
            )
            .withColumn("city_key", WarehouseUtils.normalize_city(F.col("city")))
            .dropDuplicates(["city_key"])
        )
        
        candidate = candidate.join(F.broadcast(geo.select("geo_sk", "city_key")), on="city_key", how="left")

        
        incr = self.incremental_filter(candidate)
        
        if not incr.take(1):
            print("No Incremental crm_silver_users changes detected. Skipping write.")
            return
        
        initials, first_name, last_name = WarehouseUtils.parse_name(F.col("full_name"))
        
        incr = (
            incr
            .withColumn("initials", initials)
            .withColumn("first_name", first_name)
            .withColumn("last_name", last_name)
            .withColumn("user_sk", WarehouseUtils.surrogate_key(F.col("user_id")))
        )
        
        w = (
            Window.partitionBy("user_id")
            .orderBy(F.col("signup_date").asc_nulls_last(), F.col("user_sk").desc_nulls_last())
        )
        
        incr_silver = (
            incr
            .withColumn("rn", F.row_number().over(w))
            .filter(F.col("rn") == 1)
            .drop("rn")
        )
        
        
        incr_silver = incr_silver.withColumn("dw_created_at", F.current_timestamp())
        
        incr_silver = incr_silver.select(
            "user_sk",
            "geo_sk",
            "user_id",
            "full_name",
            "initials",
            "first_name",
            "last_name",
            "email",
            "phone",
            "signup_date",
            "status",
            "city_raw",
            WarehouseUtils.normalize_city(F.col("city")).alias("city"),
            "address_raw",
            "dw_created_at",
        )
        
        unaffected = self.preserve_unaffected_existing(incr_silver)
        
        final_df = (
            incr_silver
            if unaffected is None
            else unaffected.select(incr_silver.columns).unionByName(incr_silver)
        )
        
        self.write_table(final_df, self.TARGET_TABLE, mode="overwrite")
        print("crm_silver_users reconciled")
        
    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverUserJob()
    job.run()
    job.stop()