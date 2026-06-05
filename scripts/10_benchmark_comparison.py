import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

NAV_FILE = BASE_DIR / "data" / "processed" / "02_nav_history_clean.csv"
BENCH_FILE = BASE_DIR / "data" / "processed" / "10_benchmark_indices_clean.csv"
SCORECARD_FILE = BASE_DIR / "data" / "processed" / "fund_scorecard.csv"

REPORT_DIR = BASE_DIR / "reports" / "day4"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

CHART_FILE = REPORT_DIR / "benchmark_comparison.png"
TRACKING_FILE = BASE_DIR / "data" / "processed" / "tracking_error.csv"

# --------------------------------------------------
# Load
# --------------------------------------------------

nav_df = pd.read_csv(NAV_FILE)
bench_df = pd.read_csv(BENCH_FILE)
scorecard = pd.read_csv(SCORECARD_FILE)

nav_df["date"] = pd.to_datetime(nav_df["date"])
bench_df["date"] = pd.to_datetime(bench_df["date"])

# --------------------------------------------------
# Top 5 Funds
# --------------------------------------------------

top5 = scorecard.sort_values(
    "overall_rank"
).head(5)

print("\nTop 5 Funds Used:\n")
print(
    top5[
        [
            "overall_rank",
            "scheme_name"
        ]
    ]
)

# --------------------------------------------------
# Last 3 Years
# --------------------------------------------------

end_date = nav_df["date"].max()
start_date = end_date - pd.DateOffset(years=3)

nav_df = nav_df[
    nav_df["date"] >= start_date
]

bench_df = bench_df[
    bench_df["date"] >= start_date
]

# --------------------------------------------------
# Plot Setup
# --------------------------------------------------

plt.figure(figsize=(16,8))

tracking_results = []

# --------------------------------------------------
# Plot Funds
# --------------------------------------------------

for _, row in top5.iterrows():

    amfi_code = row["amfi_code"]
    fund_name = row["scheme_name"]

    fund = nav_df[
        nav_df["amfi_code"] == amfi_code
    ].copy()

    fund = fund.sort_values("date")

    base_nav = fund["nav"].iloc[0]

    fund["normalized"] = (
        fund["nav"] / base_nav
    ) * 100

    plt.plot(
        fund["date"],
        fund["normalized"],
        label=fund_name[:35]
    )

# --------------------------------------------------
# NIFTY50
# --------------------------------------------------

nifty50 = bench_df[
    bench_df["index_name"] == "NIFTY50"
].copy()

nifty50 = nifty50.sort_values("date")

base50 = nifty50["close_value"].iloc[0]

nifty50["normalized"] = (
    nifty50["close_value"] / base50
) * 100

plt.plot(
    nifty50["date"],
    nifty50["normalized"],
    linewidth=3,
    linestyle="--",
    label="NIFTY50"
)

# --------------------------------------------------
# NIFTY100
# --------------------------------------------------

nifty100 = bench_df[
    bench_df["index_name"] == "NIFTY100"
].copy()

nifty100 = nifty100.sort_values("date")

base100 = nifty100["close_value"].iloc[0]

nifty100["normalized"] = (
    nifty100["close_value"] / base100
) * 100

plt.plot(
    nifty100["date"],
    nifty100["normalized"],
    linewidth=3,
    linestyle=":",
    label="NIFTY100"
)

# --------------------------------------------------
# Tracking Error
# --------------------------------------------------

nifty100["benchmark_return"] = (
    nifty100["close_value"].pct_change()
)

for _, row in top5.iterrows():

    amfi_code = row["amfi_code"]

    fund = nav_df[
        nav_df["amfi_code"] == amfi_code
    ].copy()

    fund = fund.sort_values("date")

    fund["fund_return"] = (
        fund["nav"].pct_change()
    )

    merged = fund.merge(
        nifty100[
            [
                "date",
                "benchmark_return"
            ]
        ],
        on="date",
        how="inner"
    )

    merged = merged.dropna()

    tracking_error = (
        (
            merged["fund_return"]
            - merged["benchmark_return"]
        ).std()
    ) * np.sqrt(252)

    tracking_results.append([
        row["scheme_name"],
        tracking_error
    ])

# --------------------------------------------------
# Save Tracking Error
# --------------------------------------------------

tracking_df = pd.DataFrame(
    tracking_results,
    columns=[
        "scheme_name",
        "tracking_error"
    ]
)

tracking_df.to_csv(
    TRACKING_FILE,
    index=False
)

# --------------------------------------------------
# Final Chart
# --------------------------------------------------

plt.title(
    "Top 5 Funds vs NIFTY50 vs NIFTY100 (Normalized = 100)",
    fontsize=14
)

plt.xlabel("Date")
plt.ylabel("Growth Index")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    CHART_FILE,
    dpi=300
)

plt.close()

print(f"\nChart Saved: {CHART_FILE}")
print(f"Tracking Error Saved: {TRACKING_FILE}")

print("\nTracking Error\n")
print(tracking_df)