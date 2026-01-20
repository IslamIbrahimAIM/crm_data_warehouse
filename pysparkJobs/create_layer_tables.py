from pathlib import Path
import argparse

from pysparkJobs.base_spark_job import BaseSparkJob


class CreateTablesJob(BaseSparkJob):
    APP_NAME = "Create_Tables_From_DDL"

    def __init__(self, layer: str):
        super().__init__()
        self.layer = layer.lower()

    def run(self):
        self.spark._jvm.org.apache.spark.sql.execution.datasources.jdbc.DriverRegistry.register(
            self.JDBC_DRIVER
        )

        base_dir = Path(__file__).resolve().parents[1]

        ddl_path = (
            base_dir
            / "db_ddls"
            / self.layer
            / f"_all_{self.layer}_tables.sql"
        )

        if not ddl_path.exists():
            raise FileNotFoundError(f"DDL file not found: {ddl_path}")

        raw_sql = ddl_path.read_text()

        raw_sql = "\n".join(
            line for line in raw_sql.splitlines()
            if not line.strip().upper().startswith("USE ")
        )

        statements = [
            stmt.strip()
            for stmt in raw_sql.split(";")
            if stmt.strip()
        ]

        for stmt in statements:
            self.execute_sql(stmt)

        print(f"✅ {self.layer.upper()} tables created successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create database tables from DDL files by layer"
    )

    parser.add_argument(
        "--layer",
        required=True,
        help="Data layer name (bronze | silver | gold | etc.)"
    )

    args = parser.parse_args()

    job = CreateTablesJob(layer=args.layer)
    job.run()
    job.stop()
