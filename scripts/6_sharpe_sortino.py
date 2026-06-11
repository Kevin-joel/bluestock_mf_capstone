"""
Risk-Adjusted Performance Analysis Module

Purpose:
Calculates annualized returns, volatility, Sharpe Ratio,
and Sortino Ratio for mutual fund schemes using daily returns.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

RETURNS_FILE = BASE_DIR / "data" / "processed" / "daily_returns.csv"
FUND_FILE = BASE_DIR / "data" / "processed" / "01_fund_master_clean.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "sharpe_sortino.csv"

# --------------------------------------------------
# Configuration
# --------------------------------------------------
RISK_FREE_RATE = 0.065
TRADING_DAYS = 252

# --------------------------------------------------
# Load Data
# --------------------------------------------------
returns_df = pd.read_csv(RETURNS_FILE)
fund_df = pd.read_csv(FUND_FILE)

returns_df["date"] = pd.to_datetime(
    returns_df["date"]
)

# --------------------------------------------------
# Calculate Metrics
# --------------------------------------------------
results = []

for amfi_code, group in returns_df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) < 100:
        continue

    # Annualized Return
    annual_return = returns.mean() * TRADING_DAYS

    # Annualized Volatility
    volatility = (
        returns.std() * np.sqrt(TRADING_DAYS)
    )

    # Sharpe Ratio
    sharpe = (
        (annual_return - RISK_FREE_RATE)
        / volatility
    )

    # Sortino Ratio
    downside = returns[returns < 0]

    if len(downside) > 0:

        downside_std = (
            downside.std()
            * np.sqrt(TRADING_DAYS)
        )

        sortino = (
            (annual_return - RISK_FREE_RATE)
            / downside_std
        )

    else:
        sortino = np.nan

    results.append([
        amfi_code,
        annual_return * 100,
        volatility * 100,
        sharpe,
        sortino
    ])

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------
metrics_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "annual_return_pct",
        "annual_volatility_pct",
        "sharpe_ratio",
        "sortino_ratio"
    ]
)

# --------------------------------------------------
# Merge Fund Information
# --------------------------------------------------
metrics_df = metrics_df.merge(
    fund_df[
        [
            "amfi_code",
            "scheme_name",
            "fund_house"
        ]
    ],
    on="amfi_code",
    how="left"
)

# --------------------------------------------------
# Ranking
# --------------------------------------------------
metrics_df["sharpe_rank"] = (
    metrics_df["sharpe_ratio"]
    .rank(ascending=False)
)

metrics_df["sortino_rank"] = (
    metrics_df["sortino_ratio"]
    .rank(ascending=False)
)

metrics_df = metrics_df.sort_values(
    "sharpe_rank"
)

# --------------------------------------------------
# Save Results
# --------------------------------------------------
metrics_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# --------------------------------------------------
# Summary
# --------------------------------------------------
print("Sharpe-Sortino analysis completed successfully.")
print(f"Funds analyzed : {len(metrics_df)}")
print(f"Output file    : {OUTPUT_FILE}")