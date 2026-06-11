import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"
REPORT_DIR = BASE_DIR / "reports" / "day 6"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

transactions = pd.read_csv(
    DATA_DIR / "08_investor_transactions_clean.csv"
)

funds = pd.read_csv(
    DATA_DIR / "01_fund_master_clean.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# First transaction year for each investor
first_year = (
    transactions
    .groupby("investor_id")["transaction_date"]
    .min()
    .dt.year
    .reset_index()
)

first_year.columns = [
    "investor_id",
    "cohort_year"
]

transactions = transactions.merge(
    first_year,
    on="investor_id"
)

# Cohort metrics
cohort_summary = (
    transactions
    .groupby("cohort_year")
    .agg(
        avg_investment=("amount_inr", "mean"),
        total_invested=("amount_inr", "sum"),
        investors=("investor_id", "nunique")
    )
    .reset_index()
)

# Top fund preference
fund_pref = (
    transactions
    .groupby(
        ["cohort_year", "amfi_code"]
    )
    .size()
    .reset_index(name="txn_count")
)

fund_pref = (
    fund_pref
    .sort_values(
        ["cohort_year", "txn_count"],
        ascending=False
    )
    .groupby("cohort_year")
    .head(1)
)

fund_pref = fund_pref.merge(
    funds[["amfi_code", "scheme_name"]],
    on="amfi_code"
)

final = cohort_summary.merge(
    fund_pref[
        ["cohort_year", "scheme_name"]
    ],
    on="cohort_year"
)

final.rename(
    columns={
        "scheme_name": "top_fund_preference"
    },
    inplace=True
)

final.to_csv(
    REPORT_DIR / "investor_cohort_analysis.csv",
    index=False
)

print(final)