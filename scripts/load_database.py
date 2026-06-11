"""
Database Loading Module

Purpose:
Loads cleaned mutual fund datasets from the processed data directory
into the SQLite data warehouse.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "sqlite:///bluestock_mf.db"


def load_dim_fund(engine):
    """Load fund master data into the dim_fund table."""

    funds = pd.read_csv("data/processed/01_fund_master_clean.csv")

    funds[
        [
            "amfi_code",
            "fund_house",
            "scheme_name",
            "category",
            "sub_category",
            "plan",
            "fund_manager",
            "risk_category",
        ]
    ].to_sql(
        "dim_fund",
        engine,
        if_exists="append",
        index=False,
    )

    print("✓ dim_fund loaded successfully")


def load_fact_nav(engine):
    """Load NAV history data into the fact_nav table."""

    nav = pd.read_csv("data/processed/02_nav_history_clean.csv")

    nav.rename(
        columns={"date": "nav_date"},
        inplace=True,
    )

    nav.to_sql(
        "fact_nav",
        engine,
        if_exists="append",
        index=False,
    )

    print("✓ fact_nav loaded successfully")


def load_fact_aum(engine):
    """Load AUM data into the fact_aum table."""

    aum = pd.read_csv("data/processed/03_aum_by_fund_house_clean.csv")

    aum.rename(
        columns={"date": "report_date"},
        inplace=True,
    )

    aum[
        [
            "fund_house",
            "report_date",
            "aum_crore",
        ]
    ].to_sql(
        "fact_aum",
        engine,
        if_exists="append",
        index=False,
    )

    print("✓ fact_aum loaded successfully")


def load_fact_performance(engine):
    """Load scheme performance metrics into the fact_performance table."""

    perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

    perf[
        [
            "amfi_code",
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "alpha",
            "beta",
            "sharpe_ratio",
            "expense_ratio_pct",
        ]
    ].to_sql(
        "fact_performance",
        engine,
        if_exists="append",
        index=False,
    )

    print("✓ fact_performance loaded successfully")


def load_fact_transactions(engine):
    """Load investor transaction data into the fact_transactions table."""

    txn = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

    txn[
        [
            "investor_id",
            "amfi_code",
            "transaction_date",
            "transaction_type",
            "amount_inr",
            "state",
            "city",
            "kyc_status",
        ]
    ].to_sql(
        "fact_transactions",
        engine,
        if_exists="append",
        index=False,
    )

    print("✓ fact_transactions loaded successfully")


def main():
    """Execute database loading workflow."""

    engine = create_engine(DATABASE_URL)

    load_dim_fund(engine)
    load_fact_nav(engine)
    load_fact_aum(engine)
    load_fact_performance(engine)
    load_fact_transactions(engine)

    print("\nDatabase loading completed successfully.")


if __name__ == "__main__":
    main()