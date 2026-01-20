from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class GoldFactOrdersJob(BaseSparkJob):
    """
    Silver – Gold Fact Orders (Skeleton)
    """

    APP_NAME = "Gold Fact Orders"

    ORDERS_TABLE      = "crm_silver_orders"
    PAYMENTS_TABLE    = "crm_silver_payment_attempts"
    COUPONS_TABLE     = "mkt_silver_coupon_redemptions"
    DIM_USER          = "gold_dim_user"
    DIM_GEO           = "gold_dim_geo"
    DIM_DATE          = "gold_dim_date"
    TARGET_TABLE      = "gold_fact_orders"

    def run(self):
        silver_df: DataFrame = self.read_table(self.ORDERS_TABLE)
        
        silver = (
            silver_df
            .select(
                "order_sk",
                "user_sk",
                "provider_sk",
                "order_status",
                "payment_provider",
                "payment_method",
                F.col("line_total").alias("order_total"),
                F.col("created_at").alias("order_date")
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
        
        coupons = (
            self.read_table(self.COUPONS_TABLE)
            .select(
                "coupon_redemption_sk",
                "order_sk",
                "promotion_sk"
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
            .join(coupons, on="order_sk", how="left")
            .join(dates, F.try_to_date(F.col("order_date")) == F.col("date_actual"), "left")
            .withColumnRenamed("date_sk", "order_date_sk")
            .drop("date_actual")
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        
        
        
        final_df = df
        
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["order_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["order_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")                   

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldFactOrdersJob()
    job.run()
    job.stop()