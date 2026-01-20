from typing import List

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilverOrderStatusJob(BaseSparkJob):
    """
    Silver – Order Status History (Skeleton)
    """

    APP_NAME = "Order Status History"

    BRONZE_TABLE = "crm_bronze_order_status_history"
    ORDERS_TABLE  = "crm_silver_orders"
    TARGET_TABLE = "crm_silver_order_status_history"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"
    
    
    ####################### Main Run ##########################

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("change_id", WarehouseUtils.clean_text(F.col("id")))
            .withColumn("order_id", WarehouseUtils.clean_text(F.col("order_id")))
            .withColumn("order_status", WarehouseUtils.normalize_order_status(F.col("status")))
            .withColumn(
                "changed_ts",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("changed_ts")),
                    self.TS_FMT
                )
            )
        ).drop("id", "status")
        
        orders = (
            self.read_table(self.ORDERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("order_id")).alias("order_id"),
                F.col("order_sk")
            )
        )
        
        df = bronze.join(orders, on="order_id", how="left")
        df = (
            df
            .withColumn(
                "order_status_history_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("order_sk"),
                        F.col("change_id"),
                        F.col("order_status"),
                        F.col("changed_ts")
                    )
                )
            )
        )
        
        ######## order_id Shouldn't Have Same status on different times ##############
        
        w_status_dedupe = (
            Window
            .partitionBy("order_id", "order_status")
            .orderBy(F.col("changed_ts").asc_nulls_last())
        )
        
        df = (
            df
            .withColumn("rn", F.row_number().over(w_status_dedupe))
            .filter(F.col("rn") == 1)
            .drop("rn")
        )
        
        df = WarehouseUtils.flag_invalid_lifecycle(
            df=df,
            partition_cols=["order_id"],
            status_col="order_status",
            ts_col="changed_ts",
            terminal_statuses=["complete", "completed", "cancelled", "canceled"],
            regression_statuses=["in-progress"]
        )
        
        final_df = (
            df
            .select(
                "order_status_history_sk",
                "order_sk",
                "order_id",
                "change_id",
                "order_status",
                "changed_ts",
                "has_terminal_before",
                "is_invalid_stage"
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        
        
        
        # df.show(50, truncate=False)
        # print(f"*******************")
        # bronze.show(50, truncate=False)
        
        # for c in df.columns:
        #     print(f'"{c}",')
            
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
                .withColumn("has_terminal_before", F.col("has_terminal_before").cast("int"))
                .withColumn("is_invalid_stage", F.col("is_invalid_stage").cast("int"))
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["order_status_history_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["order_status_history_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverOrderStatusJob()
    job.run()
    job.stop()