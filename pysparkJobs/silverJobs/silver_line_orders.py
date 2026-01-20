from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverOrderLineJob(BaseSparkJob):
    """
    Silver – Order Items (Skeleton)
    """

    APP_NAME = "Silver Order Items"

    BRONZE_TABLE = "crm_bronze_order_items"
    ORDERS_TABLE  = "crm_silver_orders"
    TARGET_TABLE = "crm_silver_order_items"
    
    ####################### HELPERS ##########################
    
    def incremental_filter(self, candidate: DataFrame) -> DataFrame:
        if not self.table_exists(self.TARGET_TABLE):
            return candidate
        
        existing = (
            self.read_table(self.TARGET_TABLE)
            .select("order_item_sk")
            .dropDuplicates()
        )
        
        return (
            candidate
            .join(existing, on="order_item_sk", how="left_anti")
        )    

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("order_id", WarehouseUtils.clean_text(F.col("order_id")))
            .withColumn("order_item_id", WarehouseUtils.clean_text(F.col("order_item_id")))
            .withColumn("product_name", WarehouseUtils.clean_text(F.col("product_name")))
            .withColumn("qty", WarehouseUtils.clean_text(F.col("qty")).cast("int"))
            .withColumn("unit_price", WarehouseUtils.clean_text(F.col("unit_price")).cast("decimal(10,2)"))
            .withColumn("line_total", WarehouseUtils.clean_text(F.col("line_total")).cast("decimal(10,2)"))
            .withColumn(
                "order_item_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        WarehouseUtils.clean_text(F.col("product_name")),
                        WarehouseUtils.clean_text(F.col("order_item_id")),
                        WarehouseUtils.clean_text(F.col("unit_price")).cast("decimal(10,2)") 
                        
                    )
                )
            )
            .withColumn(
                "is_total_valid",
                ((
                    WarehouseUtils.clean_text(F.col("qty")).cast("int")
                    * 
                    WarehouseUtils.clean_text(F.col("unit_price")).cast("decimal(10,2)")
                )   == 
                    WarehouseUtils.clean_text(F.col("line_total")).cast("decimal(10,2)")
                ).cast("int")
            )
        )
        
        orders = (
            self.read_table(self.ORDERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("order_id")).alias("order_id"),
                F.col("order_sk")
            )
        )
        
        df = (
            bronze
            .join(orders, on="order_id", how="left")
        )
        
        final_df = (
            df
            .select(
                "order_item_sk",
                "order_sk",
                "order_item_id",
                "order_id",
                "product_name",
                "qty",
                "unit_price",
                "line_total",
                "is_total_valid",            
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        incremental = self.incremental_filter(final_df)
        
        if not incremental.take(1):
            print("No new item was detected. Skipping write.")
            return
        
        self.write_table(incremental, self.TARGET_TABLE, mode="append")
        
    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverOrderLineJob()
    job.run()
    job.stop()