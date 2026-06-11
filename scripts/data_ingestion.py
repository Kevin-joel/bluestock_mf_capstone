"""
Data Ingestion Module

Purpose:
Loads and validates raw CSV files available in the data/raw directory
and provides a high-level summary of each dataset.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")


def inspect_csv_file(file_path: Path) -> None:
    """
    Read a CSV file and display a summary.

    Parameters
    ----------
    file_path : Path
        Path to the CSV file.
    """
    try:
        df = pd.read_csv(file_path)

        print("\n" + "=" * 60)
        print(f"Dataset: {file_path.name}")
        print("=" * 60)

        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")
        print(f"Missing Values: {df.isnull().sum().sum()}")
        print(f"Duplicate Rows: {df.duplicated().sum()}")

    except Exception as error:
        print(f"Error reading {file_path.name}: {error}")


def main():
    """
    Execute data ingestion and dataset inspection.
    """
    csv_files = list(RAW_PATH.glob("*.csv"))

    print(f"\nFound {len(csv_files)} CSV file(s) in '{RAW_PATH}'.")

    for file in csv_files:
        inspect_csv_file(file)

    print("\nData ingestion completed successfully.")


if __name__ == "__main__":
    main()