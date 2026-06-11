"""
Alpha-Beta Analysis Module

Purpose:
Measures fund performance relative to the benchmark by
calculating Alpha, Beta, and R-Squared using linear regression
against NIFTY100 benchmark returns.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd
from pathlib import Path
from scipy.stats import linregress

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

RETURNS_FILE = BASE_DIR / "data" / "processed" / "daily_returns.csv"
BENCH_FILE = BASE_DIR / "data" / "processed" / "10_benchmark_indices_clean.csv"
FUND_FILE = BASE_DIR / "data" / "processed" / "01_fund_master_clean.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "alpha_beta.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------
returns_df = pd.read_csv(RETURNS_FILE)

bench_df = pd.read_csv(BENCH_FILE)

fund_df = pd.read_csv(FUND_FILE)

returns_df["date"] = pd.to_datetime(
    returns_df["date"]
)

bench_df["date"] = pd.to_datetime(
    bench_df["date"]
)

# --------------------------------------------------
# Benchmark Preparation (NIFTY100)
# --------------------------------------------------
nifty100 = bench_df[
    bench_df["index_name"] == "NIFTY100"
].copy()

nifty100 = nifty100.sort_values(
    "date"
)

nifty100["benchmark_return"] = (
    nifty100["close_value"]
    .pct_change()
)

benchmark_returns = nifty100[
    ["date", "benchmark_return"]
]

# --------------------------------------------------
# Alpha-Beta Calculation
# --------------------------------------------------
results = []

for amfi_code, group in returns_df.groupby("amfi_code"):

    merged = group.merge(
        benchmark_returns,
        on="date",
        how="inner"
    )

    merged = merged.dropna(
        subset=[
            "daily_return",
            "benchmark_return"
        ]
    )

    if len(merged) < 100:
        continue

    x = merged["benchmark_return"]
    y = merged["daily_return"]

    regression = linregress(
        x,
        y
    )

    beta = regression.slope

    daily_alpha = regression.intercept

    annual_alpha = daily_alpha * 252

    r_squared = regression.rvalue ** 2

    results.append([
        amfi_code,
        annual_alpha * 100,
        beta,
        r_squared
    ])

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------
alpha_beta_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha_pct",
        "beta",
        "r_squared"
    ]
)

# --------------------------------------------------
# Merge Fund Information
# --------------------------------------------------
alpha_beta_df = alpha_beta_df.merge(
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
alpha_beta_df["alpha_rank"] = (
    alpha_beta_df["alpha_pct"]
    .rank(
        ascending=False
    )
)

alpha_beta_df = alpha_beta_df.sort_values(
    "alpha_rank"
)

# --------------------------------------------------
# Save Results
# --------------------------------------------------
alpha_beta_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# --------------------------------------------------
# Summary
# --------------------------------------------------
print("Alpha-Beta analysis completed successfully.")
print(f"Funds analyzed : {len(alpha_beta_df)}")
print(f"Output file    : {OUTPUT_FILE}")