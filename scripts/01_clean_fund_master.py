"""
Fund Master Data Cleaning Module

Purpose:
Cleans the fund master dataset by removing duplicate records,
validating numeric fields, standardizing date formats, and
exporting the cleaned dataset.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/01_fund_master.csv"
OUTPUT_FILE = "data/processed/01_fund_master_clean.csv"


def clean_fund_master():
    """
    Clean and validate the fund master dataset.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    # Remove duplicate AMFI codes
    df = df.drop_duplicates(subset=["amfi_code"])

    # Convert launch date to datetime format
    df["launch_date"] = pd.to_datetime(
        df["launch_date"],
        errors="coerce"
    )

    # Validate numeric fields
    df = df[df["expense_ratio_pct"] > 0]
    df = df[df["min_sip_amount"] > 0]
    df = df[df["min_lumpsum_amount"] > 0]

    final_records = len(df)
    removed_records = initial_records - final_records

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Fund master data cleaned successfully.")
    print(f"Records processed : {initial_records}")
    print(f"Records retained  : {final_records}")
    print(f"Records removed   : {removed_records}")


def main():
    """
    Execute fund master data cleaning.
    """
    clean_fund_master()


if __name__ == "__main__":
    main()