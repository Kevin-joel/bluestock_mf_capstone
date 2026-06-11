"""
Industry Folio Count Data Cleaning Module

Purpose:
Cleans industry folio count data by standardizing
the month field and exporting a validated dataset.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/06_industry_folio_count.csv"
OUTPUT_FILE = "data/processed/06_industry_folio_count_clean.csv"


def clean_folio_count():
    """
    Clean and validate folio count data.
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

    print("Industry folio count data cleaned successfully.")
    print(f"Records processed : {initial_records}")


def main():
    """Execute folio count data cleaning."""
    clean_folio_count()


if __name__ == "__main__":
    main()