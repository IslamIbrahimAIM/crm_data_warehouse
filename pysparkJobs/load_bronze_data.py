from pathlib import Path
from pysparkJobs.base_spark_job import BaseSparkJob


class LoadBronzeDataJob(BaseSparkJob):
    APP_NAME = "Load_Bronze_Data"

    ####################### Bronze table mapping ##########################
    
    TABLES = {
        "raw_users.csv": "crm_bronze_users",
        "raw_orders.csv": "crm_bronze_orders",
        "raw_order_items.csv": "crm_bronze_order_items",
        "raw_devices.csv": "crm_bronze_devices",
        "raw_events.csv": "crm_bronze_events",
        "raw_geo.csv": "crm_bronze_geo",
        "raw_promotions.csv": "mkt_bronze_promotions",
        "raw_coupon_redemptions.csv": "mkt_bronze_coupon_redemptions",
        "raw_referrals.csv": "crm_bronze_referrals",
        "raw_user_preferences.csv": "crm_bronze_user_preferences",
        "raw_order_status_history.csv": "crm_bronze_order_status_history",
        "raw_payment_attempts.csv": "crm_bronze_payment_attempts",
        "raw_marketing_cost.csv": "mkt_bronze_marketing_cost",
        "raw_marketing_attribution.csv": "mkt_bronze_marketing_attribution",
    }

    def run(self):
        base_dir = Path(__file__).resolve().parents[1]
        raw_dir = base_dir / "dummy_data"

        if not raw_dir.exists():
            raise FileNotFoundError(f"CSV directory not found: {raw_dir}")

        for csv_file, table in self.TABLES.items():
            csv_path = raw_dir / csv_file

            if not csv_path.exists():
                print(f"Missing CSV: {csv_file}, skipping")
                continue

            df = (
                self.spark.read
                .option("header", True)
                .option("mode", "PERMISSIVE")
                .option("nullValue", "")
                .csv(str(csv_path))
            )

            if df.rdd.isEmpty():
                print(f"{csv_file} is empty, skipping")
                continue

            self.write_table(
                df=df,
                table_name=table,
                mode="overwrite"
            )

            print(f"✅ Loaded {csv_file} => {table}")

        print("✅ All Bronze CSVs loaded successfully")


if __name__ == "__main__":
    job = LoadBronzeDataJob()
    job.run()
    job.stop()
