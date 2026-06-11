"""
Cleaned Data Verification Module

Purpose:
Performs quality checks on all processed datasets by validating
row counts, missing values, duplicate records, and dataset structure.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

from pathlib import Path
import pandas as pd

PROCESSED_PATH = Path("data/processed")


def verify_dataset(file_path: Path) -> None:
    """
    Validate a processed dataset and display summary statistics.

    Parameters
    ----------
    file_path : Path
        Path to the processed CSV file.
    """

    df = pd.read_csv(file_path)

    total_missing = df.isnull().sum().sum()
    total_duplicates = df.duplicated().sum()

    print("\n" + "=" * 70)
    print(f"Dataset: {file_path.name}")
    print("=" * 70)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(f"Missing Values: {total_missing}")
    print(f"Duplicate Rows: {total_duplicates}")


def main():
    """
    Execute validation checks for all processed datasets.
    """

    csv_files = sorted(PROCESSED_PATH.glob("*.csv"))

    print(f"\nFound {len(csv_files)} processed dataset(s).")

    for file_path in csv_files:
        verify_dataset(file_path)

    print("\nProcessed data verification completed successfully.")


if __name__ == "__main__":
    main()