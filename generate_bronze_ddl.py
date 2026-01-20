import re
from pathlib import Path
from decouple import config
from pyspark.sql import SparkSession
from pyspark.sql.types import *


####################### CONFIG ##########################

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "dummy_data"

DDL_DIR = BASE_DIR / "db_ddls" / "bronze"
DDL_DIR.mkdir(parents=True, exist_ok=True)

DB_NAME = config("MYSQL_DATABASE", default="washmen_dw")

TABLE_PREFIX_MAP = {
    "raw_users": "crm_bronze_users",
    "raw_orders": "crm_bronze_orders",
    "raw_order_items": "crm_bronze_order_items",
    "raw_devices": "crm_bronze_devices",
    "raw_events": "crm_bronze_events",
    "raw_geo": "crm_bronze_geo",
    "raw_promotions": "mkt_bronze_promotions",
    "raw_coupon_redemptions": "mkt_bronze_coupon_redemptions",
    "raw_referrals": "crm_bronze_referrals",
    "raw_user_preferences": "crm_bronze_user_preferences",
    "raw_order_status_history": "crm_bronze_order_status_history",
    "raw_payment_attempts": "crm_bronze_payment_attempts",
    "raw_marketing_cost": "mkt_bronze_marketing_cost",
    "raw_marketing_attribution": "mkt_bronze_marketing_attribution",
}


####################### Spark : MySQL type mapping ##########################

def spark_to_mysql(datatype) -> str:
    if isinstance(datatype, IntegerType):
        return "INT"
    if isinstance(datatype, LongType):
        return "BIGINT"
    if isinstance(datatype, DoubleType):
        return "DOUBLE"
    if isinstance(datatype, FloatType):
        return "DOUBLE"
    if isinstance(datatype, DecimalType):
        return f"DECIMAL({datatype.precision},{datatype.scale})"
    if isinstance(datatype, BooleanType):
        return "TINYINT"
    return "VARCHAR(255)"  # Bronze default (raw)


####################### Spark Session ##########################

spark = (
    SparkSession.builder
    .appName("Generate_Bronze_DDLs")
    .master("local[*]")
    .getOrCreate()
)


####################### DDL Generation ##########################

master_sql = [f"USE {DB_NAME};\n"]

for csv_path in sorted(RAW_DIR.glob("*.csv")):
    raw_name = csv_path.stem
    table_name = TABLE_PREFIX_MAP.get(raw_name)

    if not table_name:
        continue

    df = spark.read.option("header", True).csv(str(csv_path))
    fields = df.schema.fields

    columns = []
    for field in fields:
        col_name = re.sub(r"[^\w]", "_", field.name)
        col_type = spark_to_mysql(field.dataType)
        columns.append(f"    {col_name} {col_type}")

    ddl = f"""DROP TABLE IF EXISTS {table_name};
CREATE TABLE IF NOT EXISTS {table_name} (
{',\n'.join(columns)}
);
"""
 
    (DDL_DIR / f"{table_name}.sql").write_text(ddl)
    master_sql.append(ddl)

(DDL_DIR / "_all_bronze_tables.sql").write_text("\n".join(master_sql))

spark.stop()

print(f"✅ Bronze DDLs created successfully in: {DDL_DIR.resolve()}")
