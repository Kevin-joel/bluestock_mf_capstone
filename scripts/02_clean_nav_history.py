"""
NAV History Data Cleaning Module

Purpose:
Cleans historical NAV data by standardizing date formats,
removing duplicates, validating NAV values, and handling
missing NAV observations using forward-fill.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/02_nav_history.csv"
OUTPUT_FILE = "data/processed/02_nav_history_clean.csv"


def clean_nav_history():
    """
    Clean and validate NAV history data.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Sort records for proper time-series processing
    df = df.sort_values(
        ["amfi_code", "date"]
    )

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove invalid NAV values
    df = df[df["nav"] > 0]

    # Forward-fill missing NAV values within each scheme
    df["nav"] = (
        df.groupby("amfi_code")["nav"]
        .ffill()
    )

    final_records = len(df)
    removed_records = initial_records - final_records

    # Save cleaned dataset
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("NAV history data cleaned successfully.")
    print(f"Records processed : {initial_records}")
    print(f"Records retained  : {final_records}")
    print(f"Records removed   : {removed_records}")


def main():
    """
    Execute NAV history data cleaning.
    """
    clean_nav_history()


if __name__ == "__main__":
    main()