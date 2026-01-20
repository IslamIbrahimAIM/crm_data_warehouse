# from pathlib import Path
# from datetime import datetime, timezone
# import io
# from contextlib import redirect_stdout

# from pysparkJobs.base_spark_job import BaseSparkJob
# from pyspark.sql import functions as F
# from pyspark.sql.window import Window


# class ProfilingJob(BaseSparkJob):
#     APP_NAME = "Discover_Bronze_Tables"


#     def discover_tables(self):
#         tables_df = self.spark.read.jdbc(
#             self.jdbc_url,
#             f"""
#             (SELECT table_name
#              FROM information_schema.tables
#              WHERE table_schema = '{self.mysql_db}'
#                AND table_type = 'BASE TABLE'
#                AND table_name LIKE '%_bronze_%') t
#             """,
#             properties=self.jdbc_props
#         )
#         return [row[0] for row in tables_df.collect()]


#     ####################### SHOW AND SAVE OUTPUT ##########################
#     def show_and_save(self, df, fh, n=None, truncate=False):
#         buffer = io.StringIO()
#         with redirect_stdout(buffer):
#             if n is None:
#                 df.show(truncate=truncate)
#             else:
#                 df.show(n, truncate=truncate)

#         output = buffer.getvalue()
#         print(output, end="")
#         fh.write(output)


#     def run(self):

#         ####################### CREATE DOCUMENTATION FOLDER ##########################
#         project_root = Path(__file__).parents[1]
#         doc_dir = project_root / "documentation"
#         doc_dir.mkdir(parents=True, exist_ok=True)
#         doc_path = doc_dir / "bronze_table_discovery.md"

#         with open(doc_path, "w", encoding="utf-8") as fh:

#             fh.write("# Bronze Table Discovery Report\n\n")
#             fh.write(f"Database: {self.mysql_db}\n")
#             fh.write(
#                 f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n"
#             )
#             fh.write("```text\n")

#             ####################### DISCOVER TABLES ##########################
#             tables = self.discover_tables()

#             if not tables:
#                 print("No matching tables found - existing")
#                 fh.write("No matching tables found - existing\n")
#                 fh.write("```\n")
#                 return

#             print(f"\n Discovered {len(tables)} tables:")
#             fh.write(f"\n Discovered {len(tables)} tables:\n")

#             for t in tables:
#                 print(f"  - {t}")
#                 fh.write(f"  - {t}\n")


#             for table_name in tables:

#                 print("\n" + "=" * 100)
#                 print(f" DISCOVERING TABLE: {table_name}")
#                 print("=" * 100)

#                 fh.write("\n" + "=" * 100 + "\n")
#                 fh.write(f" DISCOVERING TABLE: {table_name}\n")
#                 fh.write("=" * 100 + "\n")

#                 ####################### 1) READ BRONZE ##########################
#                 df = self.read_table(table_name)

#                 print("\n SCHEMA")
#                 fh.write("\n SCHEMA\n")

#                 buffer = io.StringIO()
#                 with redirect_stdout(buffer):
#                     df.printSchema()

#                 schema_output = buffer.getvalue()
#                 print(schema_output, end="")
#                 fh.write(schema_output)

#                 ####################### 2) BASIC ROW COUNT ##########################
#                 total_rows = df.count()
#                 print(f"\n TOTAL ROWS: {total_rows}")
#                 fh.write(f"\n TOTAL ROWS: {total_rows}\n")

#                 if total_rows == 0:
#                     print(" Table is empty — skipping profiling")
#                     fh.write(" Table is empty — skipping profiling\n")
#                     continue

#                 ####################### 3) NULL COUNTS PER COLUMN ##########################
#                 null_counts = df.select([
#                     F.count(F.when(F.col(c).isNull(), 1)).alias(c)
#                     for c in df.columns
#                 ])

#                 print("\n NULL COUNTS")
#                 fh.write("\n NULL COUNTS\n")

#                 self.show_and_save(null_counts, fh, truncate=False)

#                 ####################### 4) STRING SHAPE DISCOVERY ##########################
#                 string_cols = [
#                     f.name for f in df.schema.fields
#                     if f.dataType.simpleString() == "string"
#                 ]

#                 for col_name in string_cols:

#                     print(f"\n VALUE SHAPES — {col_name}")
#                     fh.write(f"\n VALUE SHAPES — {col_name}\n")

#                     shaped = (
#                         df
#                         .select(F.col(col_name))
#                         .filter(F.col(col_name).isNotNull())
#                         .withColumn(
#                             "shape",
#                             F.regexp_replace(
#                                 F.regexp_replace(F.col(col_name), "[0-9]", "9"),
#                                 "[A-Za-z]", "A"
#                             )
#                         )
#                         .groupBy("shape")
#                         .count()
#                         .orderBy(F.desc("count"))
#                         .limit(10)
#                     )

#                     self.show_and_save(shaped, fh, truncate=False)

#                     ####################### SAMPLE VALUES ##########################
#                     w = Window.partitionBy("shape").orderBy(F.col(col_name))

#                     samples = (
#                         df
#                         .select(F.col(col_name))
#                         .filter(F.col(col_name).isNotNull())
#                         .withColumn(
#                             "shape",
#                             F.regexp_replace(
#                                 F.regexp_replace(F.col(col_name), "[0-9]", "9"),
#                                 "[A-Za-z]", "A"
#                             )
#                         )
#                         .withColumn("rn", F.row_number().over(w))
#                         .filter(F.col("rn") <= 3)
#                         .select("shape", F.col(col_name).alias("sample_value"))
#                     )

#                     print(f"\n SAMPLE VALUES — {col_name}")
#                     fh.write(f"\n SAMPLE VALUES — {col_name}\n")

#                     self.show_and_save(samples, fh, n=50, truncate=False)

#                 print(
#                     f"\n Discovery complete for {table_name} — scanned {total_rows} rows"
#                 )
#                 fh.write(
#                     f"\n Discovery complete for {table_name} — scanned {total_rows} rows\n"
#                 )

#             print("\n All bronze table discovery completed")
#             fh.write("\n All bronze table discovery completed\n")
#             fh.write("```\n")


#     def stop(self):
#         self.spark.stop()


# if __name__ == "__main__":
#     job = ProfilingJob()
#     job.run()
#     job.stop()



from pathlib import Path
from datetime import datetime, timezone
import io
import argparse
from contextlib import redirect_stdout

from pysparkJobs.base_spark_job import BaseSparkJob
from pyspark.sql import functions as F
from pyspark.sql.window import Window


class ProfilingJob(BaseSparkJob):
    APP_NAME = "Discover_Tables"

    def __init__(self, table_name=None, table_pattern=None, output_file=None):
        super().__init__()
        self.table_name = table_name
        self.table_pattern = table_pattern or "%_bronze_%"
        self.output_file = output_file or "bronze_table_discovery.md"

    # ==========================================================
    # TABLE DISCOVERY (PATTERN-DRIVEN)
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
    # OUTPUT HELPERS (UNCHANGED)
    # ==========================================================
    def show_and_save(self, df, fh, n=None, truncate=False):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            if n is None:
                df.show(truncate=truncate)
            else:
                df.show(n, truncate=truncate)

        output = buffer.getvalue()
        print(output, end="")
        fh.write(output)

    # ==========================================================
    # MAIN LOGIC
    # ==========================================================
    def run(self):

        # 🔒 UNCHANGED folder logic
        project_root = Path(__file__).parents[1]
        doc_dir = project_root / "documentation"
        doc_dir.mkdir(parents=True, exist_ok=True)
        doc_path = doc_dir / self.output_file

        # 🔒 predictable table resolution
        if self.table_name:
            tables = [self.table_name]
        else:
            tables = self.discover_tables()

        with open(doc_path, "w", encoding="utf-8") as fh:

            fh.write("# Table Discovery Report\n\n")
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

            print(f"\n Discovered {len(tables)} tables:")
            fh.write(f"\n Discovered {len(tables)} tables:\n")

            for t in tables:
                print(f"  - {t}")
                fh.write(f"  - {t}\n")

            for table_name in tables:

                print("\n" + "=" * 100)
                print(f" DISCOVERING TABLE: {table_name}")
                print("=" * 100)

                fh.write("\n" + "=" * 100 + "\n")
                fh.write(f" DISCOVERING TABLE: {table_name}\n")
                fh.write("=" * 100 + "\n")

                df = self.read_table(table_name)

                # ---------- SCHEMA ----------
                print("\n SCHEMA")
                fh.write("\n SCHEMA\n")

                buffer = io.StringIO()
                with redirect_stdout(buffer):
                    df.printSchema()

                schema_output = buffer.getvalue()
                print(schema_output, end="")
                fh.write(schema_output)

                # ---------- ROW COUNT ----------
                total_rows = df.count()
                print(f"\n TOTAL ROWS: {total_rows}")
                fh.write(f"\n TOTAL ROWS: {total_rows}\n")

                if total_rows == 0:
                    print(" Table is empty — skipping profiling")
                    fh.write(" Table is empty — skipping profiling\n")
                    continue

                # ---------- NULL COUNTS ----------
                null_counts = df.select([
                    F.count(F.when(F.col(c).isNull(), 1)).alias(c)
                    for c in df.columns
                ])

                print("\n NULL COUNTS")
                fh.write("\n NULL COUNTS\n")
                self.show_and_save(null_counts, fh, truncate=False)

                # ---------- STRING SHAPES ----------
                string_cols = [
                    f.name for f in df.schema.fields
                    if f.dataType.simpleString() == "string"
                ]

                for col_name in string_cols:

                    print(f"\n VALUE SHAPES — {col_name}")
                    fh.write(f"\n VALUE SHAPES — {col_name}\n")

                    shaped = (
                        df.select(F.col(col_name))
                        .filter(F.col(col_name).isNotNull())
                        .withColumn(
                            "shape",
                            F.regexp_replace(
                                F.regexp_replace(F.col(col_name), "[0-9]", "9"),
                                "[A-Za-z]", "A"
                            )
                        )
                        .groupBy("shape")
                        .count()
                        .orderBy(F.desc("count"))
                        .limit(10)
                    )

                    self.show_and_save(shaped, fh, truncate=False)

                    # ---------- SAMPLE VALUES ----------
                    w = Window.partitionBy("shape").orderBy(F.col(col_name))

                    samples = (
                        df.select(F.col(col_name))
                        .filter(F.col(col_name).isNotNull())
                        .withColumn(
                            "shape",
                            F.regexp_replace(
                                F.regexp_replace(F.col(col_name), "[0-9]", "9"),
                                "[A-Za-z]", "A"
                            )
                        )
                        .withColumn("rn", F.row_number().over(w))
                        .filter(F.col("rn") <= 3)
                        .select("shape", F.col(col_name).alias("sample_value"))
                    )

                    print(f"\n SAMPLE VALUES — {col_name}")
                    fh.write(f"\n SAMPLE VALUES — {col_name}\n")
                    self.show_and_save(samples, fh, n=50, truncate=False)

                print(f"\n Discovery complete for {table_name} — scanned {total_rows} rows")
                fh.write(
                    f"\n Discovery complete for {table_name} — scanned {total_rows} rows\n"
                )

            print("\n All table discovery completed")
            fh.write("\n All table discovery completed\n")
            fh.write("```\n")

    def stop(self):
        self.spark.stop()


# ==========================================================
# ARGPARSE (MINIMAL)
# ==========================================================
def parse_args():
    parser = argparse.ArgumentParser(description="Reusable table profiling")

    parser.add_argument("--table", help="Profile a single table", required=False)
    parser.add_argument(
        "--pattern",
        help="SQL LIKE pattern (default: %%_bronze_%%)",
        required=False
    )
    parser.add_argument(
        "--output",
        help="Output file name (default: bronze_table_discovery.md)",
        required=False
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    job = ProfilingJob(
        table_name=args.table,
        table_pattern=args.pattern,
        output_file=args.output,
    )
    job.run()
    job.stop()
