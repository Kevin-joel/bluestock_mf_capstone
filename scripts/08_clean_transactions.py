"""
Investor Transactions Data Cleaning Module

Purpose:
Cleans investor transaction records by validating dates,
standardizing transaction types, validating KYC status,
and removing invalid transaction amounts.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/08_investor_transactions.csv"
OUTPUT_FILE = "data/processed/08_investor_transactions_clean.csv"

VALID_KYC_STATUS = [
    "Verified",
    "Pending",
    "Rejected"
]


def clean_transactions():
    """
    Clean and validate investor transaction data.
    """

    df = pd.read_csv(INPUT_FILE)

    initial_records = len(df)

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.title()
    )

    df = df[df["amount_inr"] > 0]

    invalid_kyc = df[
        ~df["kyc_status"].isin(VALID_KYC_STATUS)
    ]

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Investor transactions cleaned successfully.")
    print(f"Records processed : {initial_records}")
    print(f"Records retained  : {len(df)}")
    print(f"Invalid KYC rows  : {len(invalid_kyc)}")


def main():
    """Execute transaction data cleaning."""
    clean_transactions()


if __name__ == "__main__":
    main()