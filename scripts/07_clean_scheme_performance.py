"""
Scheme Performance Data Cleaning Module

Purpose:
Validates scheme performance metrics, converts numerical fields,
identifies expense ratio anomalies, and exports cleaned datasets.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd

INPUT_FILE = "data/raw/07_scheme_performance.csv"
OUTPUT_FILE = "data/processed/07_scheme_performance_clean.csv"
ANOMALY_FILE = "data/processed/expense_ratio_anomalies.csv"

NUMERIC_COLUMNS = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]


def clean_scheme_performance():
    """
    Clean and validate scheme performance data.
    """

    df = pd.read_csv(INPUT_FILE)

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    anomalies = df[
        (df["expense_ratio_pct"] < 0.1)
        |
        (df["expense_ratio_pct"] > 2.5)
    ]

    anomalies.to_csv(
        ANOMALY_FILE,
        index=False
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Scheme performance data cleaned successfully.")
    print(f"Records processed : {len(df)}")
    print(f"Expense anomalies : {len(anomalies)}")


def main():
    """Execute scheme performance cleaning."""
    clean_scheme_performance()


if __name__ == "__main__":
    main()