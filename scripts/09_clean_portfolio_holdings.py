"""
Portfolio Holdings Data Cleaning Module

Purpose:
Validates portfolio holdings data by checking holding weights,
market values, and security prices before exporting a cleaned dataset.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/09_portfolio_holdings.csv"
OUTPUT_FILE = "data/processed/09_portfolio_holdings_clean.csv"


def clean_portfolio_holdings():
    """
    Clean and validate portfolio holdings data.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    df["portfolio_date"] = pd.to_datetime(
        df["portfolio_date"],
        errors="coerce"
    )

    df = df[
        (df["weight_pct"] >= 0)
        &
        (df["weight_pct"] <= 100)
    ]

    df = df[df["market_value_cr"] > 0]
    df = df[df["current_price_inr"] > 0]

    final_records = len(df)

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Portfolio holdings data cleaned successfully.")
    print(f"Records processed : {initial_records}")
    print(f"Records retained  : {final_records}")


def main():
    """Execute portfolio holdings cleaning."""
    clean_portfolio_holdings()


if __name__ == "__main__":
    main()