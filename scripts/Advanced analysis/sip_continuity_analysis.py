import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"
REPORT_DIR = BASE_DIR / "reports" / "day 6"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

transactions = pd.read_csv(
    DATA_DIR / "08_investor_transactions_clean.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Only SIPs
sip_df = transactions[
    transactions["transaction_type"]
    .str.upper()
    .str.contains("SIP", na=False)
].copy()

sip_df = sip_df.sort_values(
    ["investor_id", "transaction_date"]
)

results = []

for investor, grp in sip_df.groupby("investor_id"):

    if len(grp) < 6:
        continue

    avg_gap = (
        grp["transaction_date"]
        .diff()
        .dt.days
        .mean()
    )

    results.append({
        "investor_id": investor,
        "sip_transactions": len(grp),
        "avg_gap_days": round(avg_gap, 2),
        "status":
            "at-risk"
            if avg_gap > 35
            else "healthy"
    })

gap_df = pd.DataFrame(results)

gap_df.to_csv(
    REPORT_DIR / "sip_continuity_report.csv",
    index=False
)

continuity_rate = (
    (gap_df["status"] == "healthy")
    .mean()
    * 100
)

print(
    f"\nSIP Continuity Rate: {continuity_rate:.2f}%"
)

print(
    "\nAt-Risk Investors:"
)

print(
    gap_df[
        gap_df["status"] == "at-risk"
    ].head()
)