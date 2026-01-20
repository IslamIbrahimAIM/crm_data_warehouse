from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    input_file_name,
    current_timestamp,
    col,
    sum as _sum,
)
import os
import glob


RAW_DATA_DIR = "dummy_data"  

spark = (
    SparkSession.builder
    .appName("bronze_raw_ingestion_dynamic")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")


####################### DISCOVER ALL CSV FILES ##########################

csv_files = glob.glob(os.path.join(RAW_DATA_DIR, "*.csv"))

if not csv_files:
    raise RuntimeError(f"No CSV files found in {RAW_DATA_DIR}")

print("\n===== CSV FILES DISCOVERED =====")
for f in csv_files:
    print(f" - {os.path.basename(f)}")


####################### READING ALL BRONZE DATA ##########################

bronze_tables = {}

for file_path in csv_files:
    table_name = os.path.basename(file_path).replace(".csv", "")

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", False)     
        .option("mode", "PERMISSIVE")
        .csv(file_path)
        # .withColumn("_source_file", input_file_name())
        # .withColumn("_ingest_ts", current_timestamp())
    )

    bronze_tables[table_name] = df

    ####################### BASIC OBSERVABILITY ##########################
    
    print("\n" + "=" * 80)
    print(f"TABLE: {table_name}")
    print("=" * 80)

    print("\nSchema:")
    df.printSchema()

    row_count = df.count()
    print(f"\nRow count: {row_count}")

    ####################### NULL PROFILING ##########################
    
    print("\nNull counts per column:")
    df.select([
        _sum(col(c).isNull().cast("int")).alias(c)
        for c in df.columns
    ]).show(truncate=False)


    ####################### SAMPLE RAW CHECK ##########################
    
    print("\nSample rows:")
    df.show(5, truncate=False)


####################### SUMMARY ##########################

print("\n===== INGESTION SUMMARY =====")
print(f"Total CSV files ingested: {len(bronze_tables)}")
print("Tables available in memory:")

for t in bronze_tables:
    print(f" - {t}")

print("\n✔ RAW BRONZE INGESTION & PROFILING COMPLETE")
print("✔ NO SCHEMA ASSUMPTIONS MADE")
print("✔ READY TO DESIGN BRONZE SCHEMAS")
