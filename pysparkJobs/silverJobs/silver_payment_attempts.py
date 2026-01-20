from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils


class SilvePaymentAttemptsJob(BaseSparkJob):
    """
    Silver – Payment Attempts (Skeleton)
    """

    APP_NAME = "Payment Attempts"

    BRONZE_TABLE = "crm_bronze_payment_attempts"
    ORDERS_TABEL = "crm_silver_orders"
    TARGET_TABLE = "crm_silver_payment_attempts"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("attempt_id", WarehouseUtils.clean_text(F.col("attempt_id")))
            .withColumn("order_id", WarehouseUtils.clean_text(F.col("order_id")))
            .withColumn("payment_provider", WarehouseUtils.normalize_provider(F.col("provider")))
            .withColumn("payment_method", WarehouseUtils.normalize_payment_method(F.col("payment_provider")))
            .withColumn("amount_attempted", WarehouseUtils.clean_text(F.col("amount_attempted").cast("decimal(10,2)")))
            .withColumn("is_success", WarehouseUtils.clean_text(F.col("success").cast("int")))
            .withColumn(
                "attempt_ts",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("attempt_ts")),
                    self.TS_FMT
                )
            )
            
        ).drop("provider", "success")
        
        orders = (
            self.read_table(self.ORDERS_TABEL)
            .select(
                WarehouseUtils.clean_text(F.col("order_id")).alias("order_id"),
                F.col("order_sk")
            )
        )
        
        df = (
            bronze.join(orders, on="order_id", how="left")
            .withColumn(
                "payment_attempt_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("attempt_id"),
                        F.col("order_sk"),
                        F.col("attempt_ts")
                    )
                )
            )
        )
        

        # columns = df.columns
        
        # for c in columns:
        #     print(f'"{c}",')
        
        final_df = (
            df
            .select(
                "payment_attempt_sk",
                "order_sk",
                "attempt_id",
                "order_id",
                "payment_provider",
                "payment_method",
                "amount_attempted",
                "is_success",
                "attempt_ts"
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        if self.table_exists(self.TARGET_TABLE):
            existing = (
                self.read_table(self.TARGET_TABLE)
                .withColumn("is_success", F.col("is_success").cast("int"))
            )
            
            
            incremental = WarehouseUtils.incremental_filter(
                candidate=final_df,
                existing=existing,
                key_cols=["payment_attempt_sk"]
            )
            write_df = WarehouseUtils.preserve_unaffected_existing(
                existing=existing,
                incoming=incremental,
                key_cols=["payment_attempt_sk"]
            )
        else:
            write_df = final_df
        self.write_table(write_df, self.TARGET_TABLE, mode="overwrite")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilvePaymentAttemptsJob()
    job.run()
    job.stop()