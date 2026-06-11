import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "processed")

files = [
    "01_fund_master_clean.csv",
    "02_nav_history_clean.csv",
    "03_aum_by_fund_house_clean.csv",
    "04_monthly_sip_inflows_clean.csv",
    "05_category_inflows_clean.csv",
    "06_industry_folio_count_clean.csv",
    "07_scheme_performance_clean.csv",
    "08_investor_transactions_clean.csv",
    "09_portfolio_holdings_clean.csv",
    "10_benchmark_indices_clean.csv"
]

def inspect_columns():

    print("\n================ DATASET COLUMN INSPECTOR ================\n")

    for file in files:
        file_path = os.path.join(DATA_PATH, file)

        try:
            df = pd.read_csv(file_path)

            print(f"\n📁 FILE: {file}")
            print("-" * 60)
            print("COLUMNS:", list(df.columns))
            print("SHAPE:", df.shape)

        except Exception as e:
            print(f"\n❌ ERROR reading {file}: {e}")

    print("\n================ INSPECTION COMPLETE ================\n")


if __name__ == "__main__":
    inspect_columns()