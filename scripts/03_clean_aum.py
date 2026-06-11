"""
AUM Data Cleaning Module

Purpose:
Cleans Assets Under Management (AUM) data by validating
date formats and removing records with invalid AUM or
scheme count values.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/03_aum_by_fund_house.csv"
OUTPUT_FILE = "data/processed/03_aum_by_fund_house_clean.csv"


def clean_aum_data():
    """
    Clean and validate AUM dataset.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    # Convert date column to datetime format
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Remove invalid records
    df = df[df["aum_crore"] > 0]
    df = df[df["num_schemes"] > 0]

    final_records = len(df)
    removed_records = initial_records - final_records

    # Save cleaned dataset
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("AUM data cleaned successfully.")
    print(f"Records processed : {initial_records}")
    print(f"Records retained  : {final_records}")
    print(f"Records removed   : {removed_records}")


def main():
    """
    Execute AUM data cleaning.
    """
    clean_aum_data()


if __name__ == "__main__":
    main()