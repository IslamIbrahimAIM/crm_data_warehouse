from typing import List

from pathlib import Path

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob
from pysparkJobs.warehouse_utils import WarehouseUtils



class GoldDimProvidersJob(BaseSparkJob):
    """
    Gold Dim Providers (Skeleton)
    """

    APP_NAME = "Gold Dim Providers"
    
    BASE_DIR = Path(__file__).resolve().parents[2]

    ORDERS_TABLE = "crm_silver_orders"
    TARGET_TABLE = "gold_dim_providers"

    def run(self):
        silver_df: DataFrame = self.read_table(self.ORDERS_TABLE)
        
        final_df = (
            silver_df
            .select(
                "provider_sk",
                "payment_provider"
            )
            .dropDuplicates(["provider_sk"])
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        
        final_df.printSchema()
        final_df.show(5, False, True)
        
        WarehouseUtils.generate_and_create_table(
            df = final_df,
            table_name = self.TARGET_TABLE,
            layer = "gold",
            base_dir = self.BASE_DIR,
            job = self,
            primary_keys = ["provider_sk"],
        )
        
        self.write_table(final_df, self.TARGET_TABLE, mode="overwrite")               

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldDimProvidersJob()
    job.run()
    job.stop()