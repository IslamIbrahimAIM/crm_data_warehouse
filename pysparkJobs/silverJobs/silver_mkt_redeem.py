from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverMktRedeemJob(BaseSparkJob):
    """
    Silver – Redeem (Skeleton)
    """

    APP_NAME = "Silver_Redeem"

    BRONZE_TABLE = "mkt_bronze_coupon_redemptions"
    USERS_TABLE  = "crm_silver_users"
    ORDERS_TABLE = "crm_silver_orders"
    PROMO_TABLE  = "mkt_silver_promotions"
    TARGET_TABLE = "mkt_silver_coupon_redemptions"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"
    
    
    ####################### Helpers ##########################
    
    def incremental_filter(self, candidate: DataFrame) -> DataFrame:
        if not self.table_exists(self.TARGET_TABLE):
            return candidate
        
        existing = (
            self.read_table(self.TARGET_TABLE)
            .select("coupon_redemption_sk")
            .dropDuplicates()
        )
        
        return (
            candidate
            .join(existing, on="coupon_redemption_sk", how="left_anti")
        )
        
    ####################### Guard To be applied in gold ##########################
    
    def enforce_single_promo_per_order(self, df: DataFrame) -> DataFrame:
        w = (
            Window
            .partitionBy("order_id")
            .orderBy(F.col("redeemed_ts").asc_nulls_last())
        )
        canonical = (
            df
            .withColumn("rn", F.row_number().over(w))
            .filter(F.col("rn") == 1)
            .select("order_id", F.col("promotion_sk").alias("canonical_promo_sk"))
        )
        
        return (
            df
            .join(canonical, on="order_id", how="left")
            .filter(
                (F.col("promotion_sk") == F.col("canonical_promo_sk")) |
                F.col("canonical_promo_sk").isNull()
            )
            .drop("canonical_promo_sk")
        )
    
        
    ####################### Main Run ##########################    

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("redemption_id", WarehouseUtils.clean_text(F.col("redemption_id")))
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("order_id", WarehouseUtils.clean_text(F.col("order_id")))
            .withColumn("promotion_code", F.upper(WarehouseUtils.clean_text(F.col("promotion_code"))))
            .withColumn(
                "redeemed_ts",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("redeemed_ts")),
                    self.TS_FMT
                )
            )
        )
        
        users = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("user_sk"),                
            )
            .dropDuplicates(["user_id"])
        )
        
        orders = (
            self.read_table(self.ORDERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("order_id")).alias("order_id"),
                F.col("order_sk")
            )
        )
        
        promo = (
            self.read_table(self.PROMO_TABLE)
            .select(
                F.upper(WarehouseUtils.clean_text(F.col("promotion_code"))).alias("promotion_code"),
                F.col("promotion_sk"),
                F.col("valid_to")
            )
        )
        
        df = bronze.join(users, on="user_id", how="left")
        df = df.join(orders, on="order_id", how="left")
        df = df.join(promo, on="promotion_code", how="left")
        
        df = (
            df
            .withColumn(
                "is_valid_redeem",
                F.when(
                    F.col("redeemed_ts").isNotNull() & (F.col("redeemed_ts") <= F.col("valid_to")),
                    F.lit(1)
                ).otherwise(F.lit(0))
            )
            .withColumn(
                "coupon_redemption_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("redemption_id"),
                        F.col("order_id"),
                        F.col("user_id"),
                        F.col("redeemed_ts")
                    )
                )
            )
        ).drop("valid_to")
        
        promo_counts = (
            df
            .groupBy("order_id")
            .agg(
                F.countDistinct("promotion_code").alias("promo_count_per_order")
            )
        )
        
        df = (
            df
            .join(promo_counts, on="order_id", how="left")
            .withColumn(
                "has_multiple_promos",
                # F.when(F.col("promo_count_per_order") > 1, F.lit(1)).otherwise(F.lit(0))
                F.when(F.col("promo_count_per_order") > 1, F.lit(1)).otherwise(F.lit(0))
            )
        )
        
        final_df = (
            df
            .select(
                "coupon_redemption_sk",
                "user_sk",
                "order_sk",
                "promotion_sk",
                "redemption_id",
                "user_id",
                "promotion_code",
                "order_id",
                "redeemed_ts",
                F.col("is_valid_redeem").cast("int"),
                F.col("has_multiple_promos").cast("int"),                
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        incremental = self.incremental_filter(final_df)
        
        if not incremental.take(1):
            print("No new coupon redemptions detected. Skipping write.")
            return
        if not self.table_exists(self.TARGET_TABLE):
            write_df = incremental
        else:
            existing = self.read_table(self.TARGET_TABLE).select(final_df.columns)
            existing = (
                existing
                .withColumn("is_valid_redeem", F.col("is_valid_redeem").cast("int"))
                .withColumn("has_multiple_promos", F.col("has_multiple_promos").cast("int"))
            )
            incremental = (
                incremental
                .withColumn("is_valid_redeem", F.col("is_valid_redeem").cast("int"))
                .withColumn("has_multiple_promos", F.col("has_multiple_promos").cast("int"))
            )            
            write_df = existing.unionByName(incremental)
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverMktRedeemJob()
    job.run()
    job.stop()