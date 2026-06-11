"""
Monthly SIP Inflows Data Cleaning Module

Purpose:
Cleans monthly SIP inflow data by standardizing the month
column and exporting a validated dataset for analysis.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/04_monthly_sip_inflows.csv"
OUTPUT_FILE = "data/processed/04_monthly_sip_inflows_clean.csv"


def clean_sip_inflows():
    """
    Clean and validate monthly SIP inflow data.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    # Convert month column to datetime format
    df["month"] = pd.to_datetime(
        df["month"],
        format="%Y-%m",
        errors="coerce"
    )

    final_records = len(df)

    # Save cleaned dataset
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Monthly SIP inflows data cleaned successfully.")
    print(f"Records processed : {initial_records}")
    print(f"Records retained  : {final_records}")


def main():
    """
    Execute SIP inflow data cleaning.
    """
    clean_sip_inflows()


if __name__ == "__main__":
    main()