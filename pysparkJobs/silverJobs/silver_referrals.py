from pyspark.sql import functions as F
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverReferralJob(BaseSparkJob):
    """
    Silver – Rreferrals (Skeleton)
    """

    APP_NAME = "Silver_Geo"

    BRONZE_TABLE = "crm_bronze_referrals"
    USERS_TABLE  = "crm_silver_users"
    TARGET_TABLE = "crm_silver_referrals"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"
    
    

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("referral_id", WarehouseUtils.clean_text(F.col("referral_id")))
            .withColumn("referrer_user_id", WarehouseUtils.clean_text(F.col("referrer_user_id")))
            .withColumn("referred_user_id", WarehouseUtils.clean_text(F.col("referred_user_id")))
            .withColumn("referral_ts_raw", WarehouseUtils.clean_text(F.col("referral_ts")))
            .withColumn(
                "referral_ts",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("referral_ts")),
                    self.TS_FMT
                )
            )
            .withColumn(
                "referral_ts_parse_status",
                F.when(F.col("referral_ts_raw").isNull(), F.lit("null_raw"))
                 .when(F.col("referral_ts").isNotNull(), F.lit("parsed"))
                 .otherwise(F.lit("failed"))
            )
        )
        
        users = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("user_sk")
            )
            .dropDuplicates(["user_id"])
        )
        
        df = (
            bronze
            .join(
                users.withColumnRenamed("user_id", "referrer_user_id"),
                on="referrer_user_id",
                how="left"
            )
            .withColumnRenamed("user_sk", "referrer_user_sk")
            .join(
                users.withColumnRenamed("user_id", "referred_user_id"),
                on="referred_user_id",
                how="left"
            )
            .withColumnRenamed("user_sk", "referred_user_sk")
        )
        
        df = (
            df
            .withColumn(
                "is_self_referral",
                F.when(F.col("referrer_user_id") == F.col("referred_user_id"), 1)
                 .otherwise(0)
            )
            .withColumn(
                "referral_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("referral_id"),
                        F.col("referrer_user_id"),
                        F.col("referred_user_id"),
                        F.col("referral_ts").cast("string")
                    )
                )
            )
        )
        
        final_df = (
            df
            .select(
                "referral_sk",
                "referral_id",
                "referrer_user_id",
                "referrer_user_sk",
                "referred_user_id",
                "referred_user_sk",
                "referral_ts",
                "is_self_referral",
                "referral_ts_parse_status",
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        if self.table_exists(self.TARGET_TABLE):
            existing = self.read_table(self.TARGET_TABLE).select("referral_id")
            final_df = final_df.join(existing, on="referral_id", how="left_anti")
        self.write_table(final_df, self.TARGET_TABLE, mode="append")
        print("crm_silver_referrals loaded successfully")
        
    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverReferralJob()
    job.run()
    job.stop()