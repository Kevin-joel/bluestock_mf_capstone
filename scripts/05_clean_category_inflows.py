"""
Category Inflows Data Cleaning Module

Purpose:
Cleans category-wise mutual fund inflow data by standardizing
the month field and exporting a validated dataset.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/05_category_inflows.csv"
OUTPUT_FILE = "data/processed/05_category_inflows_clean.csv"


def clean_category_inflows():
    """
    Clean and validate category inflow data.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    df["month"] = pd.to_datetime(
        df["month"],
        format="%Y-%m",
        errors="coerce"
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Category inflows data cleaned successfully.")
    print(f"Records processed : {initial_records}")


def main():
    """Execute category inflow data cleaning."""
    clean_category_inflows()


if __name__ == "__main__":
    main()