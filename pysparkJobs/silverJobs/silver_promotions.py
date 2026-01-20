from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils



class SilverPromoJob(BaseSparkJob):
    """
    Silver – Promotions (Skeleton)
    """

    APP_NAME = "Silver_Promotions"

    BRONZE_TABLE = "mkt_bronze_promotions"
    TARGET_TABLE = "mkt_silver_promotions"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("promotion_code", F.upper(WarehouseUtils.clean_text(F.col("promotion_code"))))
            .withColumn("discount_pct", WarehouseUtils.clean_text(F.col("discount_pct")).cast("INT"))
            .withColumn(
                "valid_from",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("valid_from")),
                    self.TS_FMT
                )
            )
            .withColumn(
                "valid_to",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("valid_to")),
                    self.TS_FMT
                )
            )
        )
        
        w_version = Window.partitionBy("promotion_code").orderBy(F.col("valid_from"))
        now_ts = F.current_timestamp()
        
        df = (
            bronze
            .withColumn("promotion_version", F.row_number().over(w_version))
            .withColumn(
                "is_invalid_window",
                F.col("valid_to").isNotNull() & (F.col("valid_to") < F.col("valid_from"))
            )
            .withColumn(
                "valid_days",
                F.when(
                    F.col("valid_to").isNotNull(),
                    F.date_diff(F.col("valid_to"), F.col("valid_from"))
                )
            )
            .withColumn("is_scheduled", F.col("valid_from") > now_ts)
            .withColumn("is_expired", F.col("valid_to").isNotNull() & (F.col("valid_to") < now_ts))
            .withColumn(
                "is_active",
                (~F.col("is_invalid_window")) &
                (F.col("valid_from") <= now_ts) &
                (F.col("valid_to").isNull() | (F.col("valid_to") >= now_ts))
            )
            .withColumn(
                "promotion_status",
                F.when(F.col("is_invalid_window"), F.lit("invalid"))
                 .when(F.col("is_scheduled"), F.lit("scheduled"))
                 .when(F.col("is_expired"), F.lit("expired"))
                 .when(F.col("is_active"), F.lit("active"))
                 .otherwise(F.lit("disabled"))
            )
            .withColumn(
                "promotion_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("promotion_code"),
                        F.col("promotion_version"),
                        F.col("valid_from")
                    )
                )
            )
        )
        
        final_df = (
            df
            .select(
                "promotion_sk",
                "promotion_code",
                "discount_pct",
                "valid_from",
                "valid_to",
                "valid_days",
                "promotion_status",
                "is_invalid_window",
                "is_active",
                "is_scheduled",
                "is_expired",                
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        self.write_table(final_df, self.TARGET_TABLE, mode="append")
        print("mkt_silver_promotions loaded successfully")
    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverPromoJob()
    job.run()
    job.stop()