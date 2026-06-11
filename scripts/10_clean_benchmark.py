"""
Benchmark Index Data Cleaning Module

Purpose:
Validates benchmark index data by standardizing dates
and removing records with invalid closing values.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/10_benchmark_indices.csv"
OUTPUT_FILE = "data/processed/10_benchmark_indices_clean.csv"


def clean_benchmark_data():
    """
    Clean and validate benchmark index data.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    df = df[df["close_value"] > 0]

    final_records = len(df)

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Benchmark index data cleaned successfully.")
    print(f"Records processed : {initial_records}")
    print(f"Records retained  : {final_records}")


def main():
    """Execute benchmark data cleaning."""
    clean_benchmark_data()


if __name__ == "__main__":
    main()