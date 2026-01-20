from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType

from pysparkJobs.base_spark_job import BaseSparkJob



class GoldDimDateJob(BaseSparkJob):
    """
    Silver – Dim Date (Skeleton)
    """

    APP_NAME = "Gold Dim Date"
    TARGET_TABLE = "gold_dim_date"

    def run(self):
        spark = self.spark
        
        start_date = F.add_months(F.current_date(), -60)
        end_date   = F.add_months(F.current_date(),  60)
        
        dates = (
            spark.range(1)
            .select(F.explode(F.sequence(start_date, end_date)).alias("date_actual"))
        )
        
        ####################### Basic Date Attributes ##########################
        df = (
            dates
            .withColumn("date_sk", F.date_format("date_actual", "yyyyMMdd").cast(IntegerType()))
            .withColumn("day_of_month", F.dayofmonth("date_actual"))
            .withColumn("month_num", F.month("date_actual"))
            .withColumn("year_num", F.year("date_actual"))
            .withColumn("day_name", F.date_format("date_actual", "EEEE"))
            .withColumn("calendar_week", F.weekofyear("date_actual"))
        )
        
        ####################### Fiscal Year start July Monday Aligned ##########################
        
        fy_start_year = (
            F.when(F.month("date_actual") >= 7, F.year("date_actual"))
             .otherwise(F.year("date_actual") - 1)
        )
        
        fy_start_raw = F.to_date(
            F.concat(fy_start_year.cast("string"), F.lit("-07-01"))
        )
        
        fy_start_monday = F.date_add(
            fy_start_raw,
            F.when(F.dayofweek(fy_start_raw) == 1, 1)
             .when(F.dayofweek(fy_start_raw) == 2, 0)
             .when(F.dayofweek(fy_start_raw) == 3, 6)
             .when(F.dayofweek(fy_start_raw) == 4, 5)
             .when(F.dayofweek(fy_start_raw) == 5, 4)
             .when(F.dayofweek(fy_start_raw) == 6, 3)
             .when(F.dayofweek(fy_start_raw) == 7, 2)
        )
        
        prev_fy_year = fy_start_year - 1
        
        prev_fy_start_raw = F.to_date(
            F.concat(prev_fy_year.cast("string"), F.lit("-07-01"))
        )
        
        prev_fy_start_monday = F.date_add(
            prev_fy_start_raw,
            F.when(F.dayofweek(prev_fy_start_raw) == 1, 1)
             .when(F.dayofweek(prev_fy_start_raw) == 2, 0)
             .when(F.dayofweek(prev_fy_start_raw) == 3, 6)
             .when(F.dayofweek(prev_fy_start_raw) == 4, 5)
             .when(F.dayofweek(prev_fy_start_raw) == 5, 4)
             .when(F.dayofweek(prev_fy_start_raw) == 6, 3)
             .when(F.dayofweek(prev_fy_start_raw) == 7, 2)
        )
        
        df = (
            df
            .withColumn(
                "fiscal_year",
                F.when(F.col("date_actual") < fy_start_monday, fy_start_year)
                 .otherwise(fy_start_year + 1)
            )
            .withColumn(
                "fiscal_year_start_date",
                F.when(F.col("date_actual") < fy_start_monday, prev_fy_start_monday)
                 .otherwise(fy_start_monday)
            )
            .withColumn(
                "fiscal_week",
                (
                    F.floor(
                        F.datediff("date_actual", F.col("fiscal_year_start_date")) / 7
                    ) + 1
                ).cast("int")
            )
        )
        
        ####################### Salary 24th Shifted if weekend ##########################
        
        salary_base = F.to_date(
            F.concat(
                F.year("date_actual").cast("string"),
                F.lit("-"),
                F.format_string("%02d", F.month("date_actual")),
                F.lit("-24")
            )
        )
        
        salary_shift = (
            F.when(F.dayofweek(salary_base) == 7, 2)
             .when(F.dayofweek(salary_base) == 1, 1)
             .otherwise(0)
        )
        
        salary_day = F.date_add(salary_base, salary_shift)
        
        df = (
            df
            .withColumn("salary_day", salary_day)
            .withColumn("is_salary_day", (F.col("date_actual") == salary_day).cast("boolean"))
        )
        
        ####################### Black Friday ##########################
        
        nov_last_day = F.last_day(
            F.to_date(
                F.concat(F.year("date_actual").cast("string"), F.lit("-11-01"))
            )
        )
        
        bf_shift = (
            F.when(F.dayofweek(nov_last_day) == 6, 0)
             .when(F.dayofweek(nov_last_day) == 7, 1)
             .when(F.dayofweek(nov_last_day) == 1, 2)
             .when(F.dayofweek(nov_last_day) == 2, 3)
             .when(F.dayofweek(nov_last_day) == 3, 4)
             .when(F.dayofweek(nov_last_day) == 4, 5)
             .when(F.dayofweek(nov_last_day) == 5, 6)
        )
        
        black_friday = F.date_sub(nov_last_day, bf_shift)
        
        df = df.withColumn(
            "is_black_friday",
            (F.col("date_actual") == black_friday).cast("boolean")
        )
        
        final_df = (
            df
            .select(
                "date_sk",
                "date_actual",
                "day_of_month",
                "month_num",
                "year_num",
                "day_name",
                "calendar_week",
                "fiscal_year",
                "fiscal_year_start_date",
                "fiscal_week",
                "salary_day",
                "is_salary_day",
                "is_black_friday",
            )
            .withColumn("dw_created_at", F.current_timestamp())
        )
        
        if self.table_exists(self.TARGET_TABLE):
            existing = self.read_table(self.TARGET_TABLE).select("date_actual")
            final_df = final_df.join(existing, on="date_actual", how="left_anti")

        self.write_table(final_df, self.TARGET_TABLE, mode="append")
        print("✅ dim_date built successfully (100% PySpark)")

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = GoldDimDateJob()
    job.run()
    job.stop()