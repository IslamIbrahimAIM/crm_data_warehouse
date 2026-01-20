from typing import List

from pathlib import Path

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob
from pysparkJobs.warehouse_utils import WarehouseUtils



class GoldDimPromotionsJob(BaseSparkJob):
    """
    Gold Dim Promotions (Skeleton)
    """

    APP_NAME = "Gold Dim Promotions"

    BASE_DIR = Path(__file__).resolve().parents[2]
    
    BRONZE_TABLE = "mkt_silver_promotions"
    DIM_DATE     = "gold_dim_date"
    TARGET_TABLE = "gold_dim_promotion"

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        dim_date: DataFrame = (
            self.read_table(self.DIM_DATE)
            .select(
                "date_sk",
                "date_actual"
            )
        )
        
        final_df = (
            bronze_df
            .join(dim_date, F.try_to_date(F.col("valid_from")) == F.col("date_actual"), "left")
            .withColumnRenamed("date_sk", "valid_from_date_sk")
            .drop("date_actual")
            .join(dim_date, F.try_to_date(F.col("valid_to")) == F.col("date_actual"), "left")
            .withColumnRenamed("date_sk", "valid_to_date_sk")
            .drop("date_actual")
            .select(
                "promotion_sk",
                "valid_from_date_sk",
                "valid_to_date_sk",
                "promotion_code",
                "discount_pct",
                "valid_from",
                "valid_to",
                "valid_days",
                "promotion_status",
                "is_invalid_window",
                "is_active",
                "is_scheduled",
                "is_expired"
            )
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
            primary_keys = ["promotion_sk"],
            indexes = [
                ["valid_from_date_sk"], ["valid_to_date_sk"]
                ]
        )
        
        self.write_table(final_df, self.TARGET_TABLE, mode="overwrite")        

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldDimPromotionsJob()
    job.run()
    job.stop()