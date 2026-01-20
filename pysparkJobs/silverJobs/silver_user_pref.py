from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils



class SilverUserPrefJob(BaseSparkJob):
    """
    Silver – User_Pref (Skeleton)
    """

    APP_NAME = "Silver_User_Pref"

    BRONZE_TABLE = "crm_bronze_user_preferences"
    USERS_TABLE  = "crm_silver_users"
    TARGET_TABLE = "crm_silver_user_preferences"
    
    TS_FMT = "yyyy-MM-dd HH:mm:ss.SSSSSS"
    
    ####################### HELPERS ##########################
    
    def incremental_filter(self, candidate_df: DataFrame) -> DataFrame:
        if not self.table_exists(self.TARGET_TABLE):
            return candidate_df
        existing = (
            self.read_table(self.TARGET_TABLE)
            .select(
                "user_sk",
                "pref_key",
                F.col("updated_ts").alias("updated_ts_current")
            )
            .dropDuplicates(["user_sk", "pref_key"])
        )
        return (
            candidate_df.alias("b")
            .join(
                existing.alias("c"),
                on=["user_sk", "pref_key"],
                how="left"
            )
            .filter(
                F.col("updated_ts_current").isNull()
                | (F.col("b.updated_ts") > F.col("updated_ts_current"))
            )
            .drop("updated_ts_current")
        )
        
    def preserve_unaffected_existing(self, incr_df: DataFrame) -> DataFrame:
        if not self.table_exists(self.TARGET_TABLE):
            return None
        existing = self.read_table(self.TARGET_TABLE)
        
        unaffected = (
            existing
            .join(
                incr_df
                .select("user_sk", "pref_key")
                .dropDuplicates(),
                on=["user_sk", "pref_key"],
                how="left_anti"
            )
        )
        return unaffected

    def run(self):
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        bronze = (
            bronze_df
            .withColumn("pref_id", WarehouseUtils.clean_text(F.col("pref_id")))
            .withColumn("user_id", WarehouseUtils.clean_text(F.col("user_id")))
            .withColumn("pref_key", WarehouseUtils.clean_text(F.col("pref_key")))
            .withColumn("pref_value", WarehouseUtils.clean_text(F.col("pref_value")))
            .withColumn(
                "updated_ts",
                F.to_timestamp(
                    WarehouseUtils.clean_text(F.col("updated_ts")),
                    self.TS_FMT
                )
            )
            .withColumn(
                "user_preference_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        WarehouseUtils.clean_text(F.col("pref_id")),
                        WarehouseUtils.clean_text(F.col("pref_key")),
                        WarehouseUtils.clean_text(F.col("user_id")),
                    )
                )
            )
        )
        
        users = (
            self.read_table(self.USERS_TABLE)
            .select(
                WarehouseUtils.clean_text(F.col("user_id")).alias("user_id"),
                F.col("user_sk")
            )
            .dropDuplicates(["user_id"])
        )
        
        df = (
            bronze
            .join(users, on="user_id", how="inner")
            .select(
                 "user_preference_sk",
                 "user_sk",
                 "pref_id",
                 "user_id",
                 "pref_key",
                 "pref_value",
                 "updated_ts",
            )
        )
        
        pk = F.col("pref_key")
        pv = F.col("pref_value")
        
        df = df.withColumn(
            "pref_value",
            F.when((pk == "language") & (pv.isin("yes", "no")), F.lit("en"))
             .when((pk == "offers") & (pv.isin("en", "ar")), F.lit("yes"))
             .when((pk == "notifications") & (pv == "en"), F.lit("yes"))
             .when((pk == "notifications") & (pv == "ar"), F.lit("no"))
             .otherwise(pv)
        )
        
        w = (
            Window
            .partitionBy("user_sk", "pref_key")
            .orderBy(
                F.col("updated_ts").desc_nulls_last(),
                F.col("pref_id").desc_nulls_last()
            )
        )
        
        latest = (
            df
            .withColumn("rn", F.row_number().over(w))
            .filter(F.col("rn") == 1)
            .drop("rn")
        )
        
        incr = self.incremental_filter(latest)
        
        if not incr.take(1):
            print("No Incremental crm_silver_user_preferences changes detected.")
            return
        incr = incr.withColumn("dw_created_at", F.current_timestamp())
        
        unaffected = self.preserve_unaffected_existing(incr)
        
        if unaffected is None:
            final_df = incr
        else:
            unaffected = unaffected.select(incr.columns)
            final_df = unaffected.unionByName(incr)
            
        self.write_table(final_df, self.TARGET_TABLE, mode="overwrite")
        
        print("crm_silver_user_preferences snapshot updated successfully.")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverUserPrefJob()
    job.run()
    job.stop()