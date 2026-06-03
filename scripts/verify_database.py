import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "bluestock_mf.db"
)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_performance",
    "fact_transactions"
]

for table in tables:

    q = f"""
    SELECT COUNT(*)
    FROM {table}
    """

    count = pd.read_sql(
        q,
        conn
    ).iloc[0,0]

    print(
        table,
        count
    )

conn.close()