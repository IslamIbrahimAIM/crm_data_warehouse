from .base_spark_job import BaseSparkJob


class MySQLConnectionTestJob(BaseSparkJob):
    APP_NAME = "MySQL_Connection_Test_DB_Only"

    def run(self):
        print("🔌 Testing MySQL database connection (no tables assumed)...")

        # Pure connectivity test — INFORMATION_SCHEMA always exists
        df = self.read_query("""
            SELECT
                schema_name
            FROM information_schema.schemata
            WHERE schema_name = '{db}'
        """.format(db=self.mysql_db))

        df.show(truncate=False)

        if df.count() == 1:
            print("✅ Database connection successful")
        else:
            raise RuntimeError("❌ Database not found or connection failed")


if __name__ == "__main__":
    job = MySQLConnectionTestJob()
    job.run()
    job.stop()
