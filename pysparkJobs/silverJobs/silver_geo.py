from pyspark.sql import functions as F
from pyspark.sql import DataFrame

from pysparkJobs.base_spark_job import BaseSparkJob

from pysparkJobs.warehouse_utils import WarehouseUtils

class SilverGeoJob(BaseSparkJob):
    """
    Silver – Geo (Skeleton)
    """

    APP_NAME = "Silver_Geo"

    BRONZE_TABLE = "crm_bronze_geo"
    TARGET_TABLE = "crm_silver_geo"

    def run(self):
        
        bronze_df: DataFrame = self.read_table(self.BRONZE_TABLE)
        
        geo_clean = (
            bronze_df
            .select(
                F.col("city_raw"),
                F.col("country_raw"),
                F.col("latitude"),
                F.col("longitude"),
            )
            .filter(F.col("city_raw").isNotNull())
            .withColumn(
                "city",
                WarehouseUtils.normalize_city(F.col("city_raw"))
            )
            .withColumn(
                "country",
                F.when(
                WarehouseUtils.clean_text(F.col("country_raw")).isin(
                    "u.a.e", "emirates", "united arab emirates"
                    ),
                    F.lit("uae")
                ).otherwise(
                    WarehouseUtils.clean_text(F.col("country_raw"))
                )
            )
            .withColumn(
                "country",
                F.coalesce(F.col("country"), F.lit("unknown"))
            )
        )
        
        city_unique = (
            geo_clean
            .select(
                "city"
            ).distinct()
        )
        
        area_unique = (
            geo_clean
            .select(
                "city",
                "city_raw",
                "country_raw",
                "country",
                "latitude",
                "longitude",
            ).distinct()
        )
        
        city_keys = (
            city_unique
            .withColumn(
                "geo_sk",
                WarehouseUtils.surrogate_key(F.col("city"))
            )
        )
        
        area_keys = (
            area_unique
            .join(
                city_keys,
                on="city",
                how="inner"
            )
            .withColumn(
                "area_sk",
                WarehouseUtils.surrogate_key(
                    F.concat_ws(
                        "|",
                        F.col("geo_sk"),
                        F.col("latitude").cast("string"),
                        F.col("longitude").cast("string")
                    )
                )
            )
        )
        
        bounds = area_keys.select(
            F.min("latitude").alias("lat_min"),
            F.max("latitude").alias("lat_max"),
            F.min("longitude").alias("lon_min"),
            F.max("longitude").alias("lon_max")
        )
        
        geo_df = area_keys.crossJoin(bounds)
        
        geo_df = geo_df.withColumn(
            "is_geo_valid",
            F.when(
                F.col("latitude").isNotNull()
                & F.col("longitude").isNotNull()
                & F.col("latitude").between(F.col("lat_min"), F.col("lat_max"))
                & F.col("longitude").between(F.col("lon_min"), F.col("lon_max")),
                F.lit(1)
            ).otherwise(F.lit(0))
        )
        
        geo_df = (
            geo_df
            .withColumn("is_city_resolved", F.lit(1))
            .withColumn(
                "is_country_resolved",
                F.when(F.col("country") != "unknown", F.lit(1)).otherwise(F.lit(0))
            )
        )
        
        geo_df = geo_df.withColumn(
            "geo_percision",
            F.when(F.col("is_geo_valid") == 1, F.lit("exact"))
            .when(F.col("is_city_resolved") == 1, F.lit("city-level"))
            .when(F.col("is_country_resolved") == 1, F.lit("country-level"))
            .otherwise(F.lit("unknown"))
        )
        
        geo_df = geo_df.withColumn(
            "geo_quality_score",
            F.when(F.col("geo_percision") == "exact", 100)
            .when(F.col("geo_percision") == "city-level", 70)
            .when(F.col("geo_percision") == "country-level", 40)
            .otherwise(0)
        )
        
        geo_df = geo_df.dropDuplicates(
            ["geo_sk", "latitude", "longitude"]
        )
        
        final_df = geo_df.select(
            "area_sk",
            "geo_sk",
            "city_raw",
            "country_raw",
            "city",
            "country",
            F.col("latitude").cast("double").alias("latitude"),
            F.col("longitude").cast("double").alias("longitude"),
            "geo_percision",
            "is_city_resolved",
            "is_country_resolved",
            "is_geo_valid",
            "geo_quality_score",
            F.current_timestamp().alias("dw_created_at")    
        )
        
        if self.table_exists(self.TARGET_TABLE):
            existing = self.read_table(self.TARGET_TABLE).select("area_sk")
            
            final_df = final_df.join(
                existing,
                on="area_sk",
                how="left_anti"
            )
        self.write_table(final_df, self.TARGET_TABLE, mode="append")
        

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = SilverGeoJob()
    job.run()
    job.stop()