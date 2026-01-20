from pathlib import Path
import argparse

from pysparkJobs.base_spark_job import BaseSparkJob


class ProfilingColumnsJob(BaseSparkJob):
    APP_NAME = "List_Table_Columns"

    def __init__(self, table_name=None, table_pattern=None):
        super().__init__()
        self.table_name = table_name
        self.table_pattern = table_pattern or "%_bronze_%"

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


    def run(self):

        if self.table_name:
            tables = [self.table_name]
        else:
            tables = self.discover_tables()

        if not tables:
            print("No matching tables found — exiting")
            return

        print(f"\nDiscovered {len(tables)} tables\n")

        for table_name in tables:
            print("=" * 80)
            print(f"TABLE: {table_name}")
            print("COLUMNS:")

            df = self.read_table(table_name)

            for col in df.columns:
                print(f' "{col}",')

            print() 

        print("Done.")

    def stop(self):
        self.spark.stop()



def parse_args():
    parser = argparse.ArgumentParser(description="List table column names only")

    parser.add_argument("--table", help="Inspect a single table", required=False)
    parser.add_argument(
        "--pattern",
        help="SQL LIKE pattern (default: %%_bronze_%%)",
        required=False
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    job = ProfilingColumnsJob(
        table_name=args.table,
        table_pattern=args.pattern,
    )
    job.run()
    job.stop()
