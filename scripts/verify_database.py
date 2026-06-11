"""
Database Verification Module

Purpose:
Validates successful data loading by checking record counts
for all warehouse tables in the SQLite database.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import sqlite3
import pandas as pd

DATABASE_PATH = "bluestock_mf.db"

TABLES = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_performance",
    "fact_transactions",
]


def verify_table_counts(connection):
    """
    Display row counts for all database tables.

    Parameters
    ----------
    connection : sqlite3.Connection
        Active database connection.
    """

    print("\nDatabase Verification Summary")
    print("-" * 50)

    for table in TABLES:
        query = f"SELECT COUNT(*) AS record_count FROM {table}"

        count = pd.read_sql(query, connection).iloc[0, 0]

        print(f"{table:<20} {count:,} records")


def main():
    """
    Execute database verification checks.
    """

    conn = sqlite3.connect(DATABASE_PATH)

    try:
        verify_table_counts(conn)
        print("\nDatabase verification completed successfully.")

    except Exception as error:
        print(f"Database verification failed: {error}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()