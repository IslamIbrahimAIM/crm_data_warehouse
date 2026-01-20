from pathlib import Path
from datetime import datetime, timezone
import io
import argparse
from contextlib import redirect_stdout

from pysparkJobs.base_spark_job import BaseSparkJob


class SchemaDiscoveryJob(BaseSparkJob):
    APP_NAME = "Discover_Table_Schemas"

    def __init__(self, table_name=None, table_pattern=None, output_file=None):
        super().__init__()
        self.table_name = table_name
        self.table_pattern = table_pattern or "%_bronze_%"
        self.output_file = output_file or "table_schema_discovery.md"

    # ==========================================================
    # TABLE DISCOVERY
    # ==========================================================
    def discover_tables(self):
        tables_df = self.spark.read.jdbc(
            self.jdbc_url,
            f"""
            (SELECT table_name
             FROM information_schema.tables
             WHERE table_schema = '{self.mysql_db}'
               AND table_type = 'BASE TABLE'
               AND table_name LIKE '{self.table_pattern}') t
            """,
            properties=self.jdbc_props
        )
        return [row[0] for row in tables_df.collect()]

    # ==========================================================
    # MAIN LOGIC
    # ==========================================================
    def run(self):

        project_root = Path(__file__).parents[1]
        doc_dir = project_root / "documentation"
        doc_dir.mkdir(parents=True, exist_ok=True)
        doc_path = doc_dir / self.output_file

        tables = (
            [self.table_name]
            if self.table_name
            else self.discover_tables()
        )

        with open(doc_path, "w", encoding="utf-8") as fh:

            fh.write("# Table Schema Discovery Report\n\n")
            fh.write(f"Database: {self.mysql_db}\n")
            fh.write(f"Table pattern: {self.table_pattern}\n")
            fh.write(
                f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n"
            )
            fh.write("```text\n")

            if not tables:
                print("No matching tables found — exiting")
                fh.write("No matching tables found — exiting\n")
                fh.write("```\n")
                return

            for table_name in tables:

                print("\n" + "=" * 100)
                print(f" TABLE: {table_name}")
                print("=" * 100)

                fh.write("\n" + "=" * 100 + "\n")
                fh.write(f" TABLE: {table_name}\n")
                fh.write("=" * 100 + "\n")

                df = self.read_table(table_name)

                buffer = io.StringIO()
                with redirect_stdout(buffer):
                    df.printSchema()

                schema_output = buffer.getvalue()
                print(schema_output, end="")
                fh.write(schema_output)

            fh.write("```\n")
            print("\n Schema discovery completed")

    def stop(self):
        self.spark.stop()


# ==========================================================
# ARGPARSE
# ==========================================================
def parse_args():
    parser = argparse.ArgumentParser(description="Table schema discovery")

    parser.add_argument("--table", help="Inspect a single table", required=False)
    parser.add_argument(
        "--pattern",
        help="SQL LIKE pattern (default: %%_bronze_%%)",
        required=False
    )
    parser.add_argument(
        "--output",
        help="Output file name (default: table_schema_discovery.md)",
        required=False
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    job = SchemaDiscoveryJob(
        table_name=args.table,
        table_pattern=args.pattern,
        output_file=args.output,
    )
    job.run()
    job.stop()
