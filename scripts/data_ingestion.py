from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")

csv_files = list(RAW_PATH.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 60)
    print(f"FILE: {file.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n")

    except Exception as e:
        print(f"Error reading {file.name}: {e}")