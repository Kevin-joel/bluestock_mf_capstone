import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

NAV_FILE = BASE_DIR / "data" / "processed" / "02_nav_history_clean.csv"
FUND_FILE = BASE_DIR / "data" / "processed" / "01_fund_master_clean.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "cagr_summary.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------
nav_df = pd.read_csv(NAV_FILE)

fund_df = pd.read_csv(FUND_FILE)

nav_df["date"] = pd.to_datetime(nav_df["date"])

# --------------------------------------------------
# CAGR Function
# --------------------------------------------------
def calculate_cagr(nav_data, years):

    end_date = nav_data["date"].max()
    start_date = end_date - pd.DateOffset(years=years)

    period_df = nav_data[
        nav_data["date"] >= start_date
    ].copy()

    if len(period_df) < 2:
        return np.nan

    start_nav = period_df.iloc[0]["nav"]
    end_nav = period_df.iloc[-1]["nav"]

    if start_nav <= 0:
        return np.nan

    return ((end_nav / start_nav) ** (1 / years)) - 1


# --------------------------------------------------
# Calculate CAGR
# --------------------------------------------------
results = []

for amfi_code, group in nav_df.groupby("amfi_code"):

    group = group.sort_values("date")

    cagr_1yr = calculate_cagr(group, 1)
    cagr_3yr = calculate_cagr(group, 3)

    # Check if 5 years available
    years_available = (
        (group["date"].max() - group["date"].min()).days
        / 365.25
    )

    if years_available >= 5:
        cagr_5yr = calculate_cagr(group, 5)
    else:
        cagr_5yr = np.nan

    results.append([
        amfi_code,
        cagr_1yr,
        cagr_3yr,
        cagr_5yr
    ])

# --------------------------------------------------
# Create Table
# --------------------------------------------------
cagr_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr_1yr",
        "cagr_3yr",
        "cagr_5yr"
    ]
)

cagr_df = cagr_df.merge(
    fund_df[
        ["amfi_code", "scheme_name", "fund_house"]
    ],
    on="amfi_code",
    how="left"
)

# Convert to %
for col in ["cagr_1yr", "cagr_3yr", "cagr_5yr"]:
    cagr_df[col] = cagr_df[col] * 100

# --------------------------------------------------
# Ranking
# --------------------------------------------------
cagr_df["rank_3yr"] = (
    cagr_df["cagr_3yr"]
    .rank(ascending=False)
)

cagr_df = cagr_df.sort_values(
    "rank_3yr"
)

# --------------------------------------------------
# Save
# --------------------------------------------------
cagr_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nTop 10 Funds by 3Y CAGR\n")

print(
    cagr_df[
        [
            "scheme_name",
            "cagr_3yr",
            "rank_3yr"
        ]
    ].head(10)
)

print(f"\nSaved: {OUTPUT_FILE}")