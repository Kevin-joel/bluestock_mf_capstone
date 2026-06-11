"""
Maximum Drawdown Analysis Module

Purpose:
Calculates the maximum drawdown experienced by each mutual fund,
identifies the worst drawdown period, and ranks funds based on
downside risk.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

NAV_FILE = BASE_DIR / "data" / "processed" / "02_nav_history_clean.csv"
FUND_FILE = BASE_DIR / "data" / "processed" / "01_fund_master_clean.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "max_drawdown.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------
nav_df = pd.read_csv(NAV_FILE)
fund_df = pd.read_csv(FUND_FILE)

nav_df["date"] = pd.to_datetime(
    nav_df["date"]
)

# --------------------------------------------------
# Maximum Drawdown Calculation
# --------------------------------------------------
results = []

for amfi_code, group in nav_df.groupby("amfi_code"):

    group = group.sort_values(
        "date"
    ).copy()

    # Running peak NAV
    group["running_max"] = (
        group["nav"].cummax()
    )

    # Drawdown
    group["drawdown"] = (
        group["nav"]
        / group["running_max"]
    ) - 1

    # Worst drawdown
    max_drawdown = (
        group["drawdown"].min()
    )

    worst_idx = (
        group["drawdown"].idxmin()
    )

    worst_date = group.loc[
        worst_idx,
        "date"
    ]

    results.append([
        amfi_code,
        max_drawdown * 100,
        worst_date
    ])

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------
dd_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown_pct",
        "worst_drawdown_date"
    ]
)

# --------------------------------------------------
# Merge Fund Information
# --------------------------------------------------
dd_df = dd_df.merge(
    fund_df[
        [
            "amfi_code",
            "scheme_name",
            "fund_house",
            "category"
        ]
    ],
    on="amfi_code",
    how="left"
)

# --------------------------------------------------
# Ranking
# Smaller drawdown = better
# --------------------------------------------------
dd_df["drawdown_rank"] = (
    dd_df["max_drawdown_pct"]
    .rank(
        ascending=False
    )
)

# --------------------------------------------------
# Sort by Worst Drawdown
# --------------------------------------------------
dd_df = dd_df.sort_values(
    "max_drawdown_pct"
)

# --------------------------------------------------
# Save Results
# --------------------------------------------------
dd_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# --------------------------------------------------
# Summary
# --------------------------------------------------
print("Maximum Drawdown analysis completed successfully.")
print(f"Funds analyzed : {len(dd_df)}")
print(f"Output file    : {OUTPUT_FILE}")