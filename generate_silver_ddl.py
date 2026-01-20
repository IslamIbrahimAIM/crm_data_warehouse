from pathlib import Path
from decouple import config



BASE_DIR = Path(__file__).resolve().parent
PROFILING_FILE = BASE_DIR / "documentation" / "bronze_profiling.md"

assert PROFILING_FILE.exists(), f"Missing file: {PROFILING_FILE}"

DDL_BASE_DIR = BASE_DIR / "db_ddls" / "silver"
DDL_BASE_DIR.mkdir(parents=True, exist_ok=True)

DB_NAME = config("MYSQL_DATABASE", default="washit_dw")



def parse_bronze_profiling(md_text: str) -> dict:
    tables = {}
    current_table = None

    for raw in md_text.splitlines():
        line = raw.strip()

        if line.startswith("DISCOVERING TABLE:"):
            current_table = line.split("DISCOVERING TABLE:")[1].strip()
            tables[current_table] = []
            continue

        if current_table and line.startswith("|--"):
            col = line.split(":")[0].replace("|--", "").strip()
            tables[current_table].append(col)

    return tables



def silver_type(column: str) -> str:
    c = column.lower()

    if c.endswith("_ts") or "timestamp" in c:
        return "DATETIME"
    if c.endswith("_date"):
        return "DATE"
    if "amount" in c or "price" in c:
        return "DECIMAL(12,2)"
    if c.startswith("is_"):
        return "BOOLEAN"
    if c.endswith("_count") or c.endswith("_qty") or c == "qty":
        return "INT"
    if c.endswith("_id"):
        return "VARCHAR(50)"
    return "VARCHAR(255)"


def build_silver_ddl(silver_table: str, columns: list[str]) -> str:
    ddl_cols = []
    constraints = []
    entity = silver_table.split("_silver_")[1].rstrip("s")
    sk = f"{entity}_sk"

    ddl_cols.append(f"    {sk} CHAR(26) NOT NULL")
    constraints.append(f"PRIMARY KEY ({sk})")

    for col in columns:
        ddl_cols.append(f"    {col} {silver_type(col)}")

        if col.endswith("_id"):
            constraints.append(f"KEY idx_{silver_table}_{col} ({col})")

    ddl_cols.append("    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP")

    return f"""
DROP TABLE IF EXISTS {silver_table};
CREATE TABLE IF NOT EXISTS {silver_table} (
{",\n".join(ddl_cols)},
{",\n".join(constraints)}
)
ENGINE=InnoDB;
""".strip()


# ==================== MAIN ====================

profiling_text = PROFILING_FILE.read_text(encoding="utf-8")
tables = parse_bronze_profiling(profiling_text)

if not tables:
    raise RuntimeError("bronze_profiling.md parsed but ZERO tables detected")

master_sql = [f"USE {DB_NAME};"]

for bronze_table, cols in tables.items():
    silver_table = bronze_table.replace("_bronze_", "_silver_")

    ddl = build_silver_ddl(silver_table, cols)

    (DDL_BASE_DIR / f"{silver_table}.sql").write_text(ddl + "\n", encoding="utf-8")
    master_sql.append(ddl)

(DDL_BASE_DIR / "_all_silver_tables.sql").write_text(
    "\n\n".join(master_sql) + "\n",
    encoding="utf-8"
)

print(f"OK: {len(tables)} silver tables generated")
print(f"OK: SK format = entity_sk")
