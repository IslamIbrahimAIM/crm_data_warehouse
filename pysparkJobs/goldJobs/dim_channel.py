from pyspark.sql import functions as F
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob
from pysparkJobs.warehouse_utils import WarehouseUtils


class DimChannelJob(BaseSparkJob):
    """
    Gold – Dim Channel
    Grain: 1 row per normalized channel
    """

    APP_NAME = "Gold_Dim_Channel"

    ATTR_TABLE = "mkt_silver_marketing_attribution"
    COST_TABLE = "mkt_silver_marketing_cost"
    TARGET_TABLE = "gold_dim_channel"

    def run(self):
        attrib = (
            self.read_table(self.ATTR_TABLE)
            .select(WarehouseUtils.clean_text(F.col("channel")).alias("channel_name"))
            .filter(F.col("channel_name").isNotNull() & (F.col("channel_name") != ""))
        )

        cost = (
            self.read_table(self.COST_TABLE)
            .select(WarehouseUtils.clean_text(F.col("channel")).alias("channel_name"))
            .filter(F.col("channel_name").isNotNull() & (F.col("channel_name") != ""))
        )

        dim = (
            attrib.unionByName(cost)
            .dropDuplicates(["channel_name"])
            .withColumn(
                "channel_sk",
                WarehouseUtils.surrogate_key(F.col("channel_name"))
            )
            .select("channel_sk", "channel_name")
            .withColumn("dw_created_at", F.current_timestamp())
        )

        
        if self.table_exists(self.TARGET_TABLE):
            existing = self.read_table(self.TARGET_TABLE).select("channel_name")
            dim = dim.join(existing, on="channel_name", how="left_anti")

            if dim.rdd.isEmpty():
                print("dim_channel: no new rows to insert")
                return

            self.write_table(dim, self.TARGET_TABLE, mode="append")
        else:
            self.write_table(dim, self.TARGET_TABLE, mode="overwrite")

        print("dim_channel built successfully")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = DimChannelJob()
    job.run()
    job.stop()
