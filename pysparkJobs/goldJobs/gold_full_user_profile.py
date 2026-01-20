from typing import List

from pathlib import Path

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob
from pysparkJobs.warehouse_utils import WarehouseUtils



class GoldUserLifeCycleJob(BaseSparkJob):
    """
    Gold User Value Profile (Skeleton)
    """

    APP_NAME = "Gold User Value Profile"
    
    BASE_DIR = Path(__file__).resolve().parents[2]

    FACT_EVENTS_TABLE        = "gold_fact_events"
    FACT_ORDERS_TABLE        = "gold_fact_orders"
    ORDER_ITEMS              = "crm_silver_order_items"
    DIM_DATE                 = "gold_dim_date"
    USER_DIM                 = "gold_dim_user"
    GEO_DIM                  = "gold_dim_geo"
    DEVICE_DIM               = "gold_dim_device"
    TARGET_TABLE             = "gold_user_value_profile"

    def run(self):
        fact_events_df: DataFrame  = self.read_table(self.FACT_EVENTS_TABLE)
        
        fact_orders_df: DataFrame  = self.read_table(self.FACT_ORDERS_TABLE)
        
        order_items_df: DataFrame  = self.read_table(self.ORDER_ITEMS)
        
        users_df: DataFrame        = (
            self.read_table(self.USER_DIM)
            .select(
                "user_sk",
                "first_name",
                "last_name",
                "email",
                "phone",
                "user_status",
                "pref_language"
            )
        )
        
        geo_df: DataFrame          = (
            self.read_table(self.GEO_DIM)
            .select(
                "geo_sk",
                "latitude",
                "longitude"
            )
        )
        
        device_df: DataFrame       = (
            self.read_table(self.DEVICE_DIM)
            .select(
                "device_sk",
                "device_family",
                "os_family",
                "browser_family"
            )
            
        )
        
        
        
        event_agg = (
            fact_events_df
            .groupBy("user_sk")
            .agg(
                F.min("event_date").alias("first_event_date"),
                F.max("event_date").alias("last_event_date")
            )
        )
        
        order_agg = (
            fact_orders_df
            .groupBy("user_sk")
            .agg(
                F.min("order_date").alias("first_order_date"),
                F.max("order_date").alias("last_order_date"),
                F.count("*").alias("total_orders"),
                F.sum("order_total").alias("total_revenue"),
                F.sum(
                    F.when(F.col("order_status") == "complete", F.col("order_total"))
                     .otherwise(F.lit(0))
                ).alias("actual_revenue"),
                F.sum(
                    F.when(F.col("order_status") == "in-progress", F.col("order_total"))
                     .otherwise(F.lit(0))
                ).alias("expected_revenue"),
                F.sum(
                    F.when(F.col("order_status").isin("canceled", "cancelled"), F.col("order_total"))
                     .otherwise(F.lit(0))
                ).alias("lost_revenue"),
                F.max(
                    F.struct("order_date", "city", "geo_sk")
                ).alias("latest_order_struct")
            )
            .withColumn("primary_city", F.col("latest_order_struct.city"))
            .withColumn("geo_sk", F.col("latest_order_struct.geo_sk"))
            .drop("latest_order_struct")
        )
        
        items_per_order = (
            order_items_df
            .groupBy("order_sk")
            .agg(
                F.sum("qty").alias("items_per_order")
            )
        )
        
        order_user_map = (
            fact_orders_df
            .select("order_sk", "user_sk")
        )
        
        abs_agg = (
            items_per_order
            .join(order_user_map, "order_sk", "inner")
            .groupBy("user_sk")
            .agg(
                F.floor(F.avg("items_per_order")).try_cast("integer").alias("abs")
            )
        )
        
        event_loc = (
            fact_events_df
            .groupBy("user_sk")
            .agg(
                F.max(F.struct("event_date", "city", "geo_sk", "device_sk")).alias("latest_event_struct")
            )
            .select(
                "user_sk",
                F.col("latest_event_struct.city").alias("city"),
                F.col("latest_event_struct.geo_sk").alias("event_geo_sk"),
                F.col("latest_event_struct.device_sk").alias("event_device_sk")
            )
            .drop("latest_event_struct")
        )
        
        final_df = (
            event_agg
            .join(order_agg, "user_sk", "left")
            .join(abs_agg, "user_sk", "left")
            .withColumn(
                "aov",
                F.when(F.col("total_orders") > 0,
                       F.col("total_revenue") / F.col("total_orders")).try_cast("decimal(10,2)")
            )
            .withColumn(
                "is_repeat_customer",
                F.col("total_orders") > 1
            )
            .withColumn(
                "days_to_first_order",
                F.date_diff("first_order_date", "first_event_date")
            )
            .withColumn(
                "conversion_type",
                F.when(F.col("days_to_first_order") < 0, "Offline / Pre-digital customer")
                 .when(F.col("days_to_first_order") == 0, "Instant Converter")
                 .when(F.col("days_to_first_order") > 0, "Digital-first Converter")
            )
            .withColumn(
                "purchase_behavior",
                F.when(F.col("total_orders").isNull(), "Visitor")
                 .when(F.col("total_orders") == 1, "One-time buyer")
                 .when(F.col("total_orders") > 1, "Repeat buyer")
            )
        )
        
        q33, q67 = (
            final_df
            .select("aov")
            .where(F.col("aov").isNotNull())
            .approxQuantile("aov", [0.33, 0.67], 0.01)
        )
        
        final_df = (
            final_df
            .withColumn(
                "value_segment",
                F.when(F.col("aov").isNull(), None)
                 .when(F.col("aov") <= F.lit(q33), "Low value")
                 .when(F.col("aov") <= F.lit(q67), "Medium value")
                 .otherwise("High value")
            )
            .join(event_loc, "user_sk", "left")
            .withColumn(
                "primary_city",
                F.coalesce(F.col("primary_city"), F.col("city"))
            )
            .withColumn(
                "geo_sk",
                F.coalesce(F.col("geo_sk"), F.col("event_geo_sk"))
            )
            .withColumn(
                "device_sk",
                F.col("event_device_sk").alias("device_sk")
            )
            .drop("city", "event_geo_sk", "event_device_sk")
            .join(users_df, "user_sk", "left")
            .join(geo_df, "geo_sk", "left")
            .join(device_df, "device_sk", "left")
            .withColumn(
                "pref_language",
                F.when(F.col("pref_language").isNull(), "en")
                 .otherwise(F.col("pref_language"))
            )
            .withColumn(
                "realized_ltv",
                F.col("actual_revenue")
            )
            .withColumn(
                "potential_ltv",
                F.col("actual_revenue") + F.col("expected_revenue")
            )
            .withColumn(
                "revenue_efficiency_score",
                F.when(
                    (F.col("actual_revenue") + F.col("expected_revenue")) > 0,
                    F.round(
                        F.col("actual_revenue") /
                        (F.col("actual_revenue") + F.col("expected_revenue")),
                        2
                    )
                )
            )
            .withColumn(
                "churn_risk",
                F.when(F.col("lost_revenue").isNull() | (F.col("lost_revenue") == 0), "Low")
                 .when(F.col("lost_revenue") > F.col("actual_revenue"), "High")
                 .otherwise("Medium")
            )
        )
        
        final_df = (
            final_df
            .withColumn(
                "tenure_days",
                F.date_diff(F.current_date(), F.col("first_event_date"))
            )
            .withColumn(
                "tenure_bucket",
                F.when(F.col("tenure_days") < 30, "New")
                 .when(F.col("tenure_days") <= 90, "Early")
                 .when(F.col("tenure_days") <= 180, "Established")
                 .when(F.col("tenure_days") <= 365, "Mature")
                 .otherwise("Long-term")
            )
            .withColumn(
                "purchase_tenure_days",
                F.when(
                    F.col("first_order_date").isNotNull(),
                    F.date_diff(F.current_date(), F.col("first_order_date"))
                )
            )
            .withColumn(
                "purchase_tenure_bucket",
                F.when(F.col("purchase_tenure_days").isNull(), "Non-buyer")
                 .when(F.col("purchase_tenure_days") < 30, "New buyer")
                 .when(F.col("purchase_tenure_days") <= 90, "Early buyer")
                 .when(F.col("purchase_tenure_days") <= 365, "Established buyer")
                 .otherwise("Long-term buyer")
            )
            .withColumn(
                "recency_days",
                F.date_diff(F.current_date(), F.col("last_order_date"))
            )
        )
        
        r_q = (
            final_df
            .where(F.col("recency_days").isNotNull())
            .approxQuantile("recency_days", [0.2, 0.4, 0.6, 0.8], 0.01)
        )
        
        f_q = (
            final_df
            .where(F.col("total_orders").isNotNull())
            .approxQuantile("total_orders", [0.2, 0.4, 0.6, 0.8], 0.01)
        )
        
        m_q = (
            final_df
            .where(F.col("actual_revenue").isNotNull())
            .approxQuantile("actual_revenue", [0.2, 0.4, 0.6, 0.8], 0.01)
        )
        
        clv_q = (
            final_df
            .where(F.col("realized_ltv").isNotNull())
            .approxQuantile("realized_ltv", [0.4, 0.7, 0.9], 0.01)
        )
        
        final_df = (
            final_df
            .withColumn(
                "r_score",
                F.when(F.col("recency_days") <= r_q[0], 5)
                 .when(F.col("recency_days") <= r_q[1], 4)
                 .when(F.col("recency_days") <= r_q[2], 3)
                 .when(F.col("recency_days") <= r_q[3], 2)
                 .when(F.col("recency_days").isNull(), 1)
                 .otherwise(1)
            )
            .withColumn(
                "f_score",
                F.when(F.col("total_orders") <= f_q[0], 1)
                 .when(F.col("total_orders") <= f_q[1], 2)
                 .when(F.col("total_orders") <= f_q[2], 3)
                 .when(F.col("total_orders") <= f_q[3], 4)
                 .when(F.col("total_orders").isNull(), 1)
                 .otherwise(5)
            )
            .withColumn(
                "m_score",
                F.when(F.col("actual_revenue") <= m_q[0], 1)
                 .when(F.col("actual_revenue") <= m_q[1], 2)
                 .when(F.col("actual_revenue") <= m_q[2], 3)
                 .when(F.col("actual_revenue") <= m_q[3], 4)
                 .when(F.col("actual_revenue").isNull(), 1)
                 .otherwise(5)
            )
            .withColumn(
                "rfm_score",
                F.concat_ws(
                    "-",
                    F.col("r_score"),
                    F.col("f_score"),
                    F.col("m_score")
                )
            )
            .withColumn(
                "clv_rank",
                F.when(F.col("realized_ltv").isNull(), "No value yet")
                 .when(F.col("realized_ltv") >= clv_q[2], "Top 10%")
                 .when(F.col("realized_ltv") >= clv_q[1], "High")
                 .when(F.col("realized_ltv") >= clv_q[0], "Medium")
                 .otherwise("Low")
            )
        )
                    
        
        # event_agg.printSchema()
        # event_agg.show(5, False, True)
        
        # print("*+*"*50)
        
        # order_agg.printSchema()
        # order_agg.show(5, False, True)
        
        # print("*+*"*50)
        
        # final_df.printSchema()
        # final_df.show(5, False, True)  
        
        WarehouseUtils.generate_and_create_table(
            df = final_df,
            table_name = self.TARGET_TABLE,
            layer = "gold",
            base_dir = self.BASE_DIR,
            job = self,
            primary_keys = ["user_sk"],
            indexes = [
                ["geo_sk"], ["device_sk"], ["value_segment"],
                ["clv_rank"], ["churn_risk"], ["purchase_behavior"],
                ["recency_days"], ["last_order_date"], ["realized_ltv"],
                ["r_score"], ["f_score"], ["m_score"]
                ]
        )
        
        self.write_table(final_df, self.TARGET_TABLE, mode="overwrite")                              

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldUserLifeCycleJob()
    job.run()
    job.stop()