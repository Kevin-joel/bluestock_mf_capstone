"""
Database Creation Module

Purpose:
Creates the SQLite database and initializes all required tables
using the SQL schema definition.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import sqlite3
from pathlib import Path

DATABASE_PATH = "bluestock_mf.db"
SCHEMA_PATH = Path("sql/schema.sql")


def create_database():
    """
    Create the SQLite database and execute the schema script.
    """
    conn = sqlite3.connect(DATABASE_PATH)

    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
            conn.executescript(schema_file.read())

        conn.commit()
        print("Database schema created successfully.")

    except Exception as error:
        print(f"Database creation failed: {error}")

    finally:
        conn.close()


def main():
    """
    Execute database creation process.
    """
    create_database()


if __name__ == "__main__":
    main()