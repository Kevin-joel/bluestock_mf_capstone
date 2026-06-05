import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

NAV_FILE = BASE_DIR / "data" / "processed" / "02_nav_history_clean.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "daily_returns.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------
nav_df = pd.read_csv(NAV_FILE)

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

# --------------------------------------------------
# Daily Returns
# --------------------------------------------------
nav_df["daily_return"] = (
    nav_df.groupby("amfi_code")["nav"]
    .pct_change()
)

# --------------------------------------------------
# Validation
# --------------------------------------------------
print("\nDaily Return Summary")
print(nav_df["daily_return"].describe())

print("\nExtreme Returns")
print(
    nav_df["daily_return"].agg(
        ["min", "max"]
    )
)

# --------------------------------------------------
# Save
# --------------------------------------------------
nav_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(f"\nSaved: {OUTPUT_FILE}")
print(f"Rows: {len(nav_df):,}")