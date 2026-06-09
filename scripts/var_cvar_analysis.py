import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================
# Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"
REPORT_DIR = BASE_DIR / "reports" / "day 6"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# Load Data
# ==========================================

funds = pd.read_csv(
    DATA_DIR / "01_fund_master_clean.csv"
)

nav = pd.read_csv(
    DATA_DIR / "02_nav_history_clean.csv"
)

# ==========================================
# NAV Preparation
# ==========================================

nav["date"] = pd.to_datetime(nav["date"])

pivot_nav = nav.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

daily_returns = pivot_nav.pct_change()

# ==========================================
# VaR & CVaR
# ==========================================

results = []

for fund in daily_returns.columns:

    returns = daily_returns[fund].dropna()

    if len(returns) < 30:
        continue

    var95 = np.percentile(returns, 5)

    cvar95 = returns[returns <= var95].mean()

    results.append({
        "amfi_code": fund,
        "VaR_95": round(var95, 6),
        "CVaR_95": round(cvar95, 6)
    })

risk_df = pd.DataFrame(results)

risk_df = risk_df.merge(
    funds[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

risk_df = risk_df[
    [
        "amfi_code",
        "scheme_name",
        "VaR_95",
        "CVaR_95"
    ]
]

risk_df.to_csv(
    REPORT_DIR / "var_cvar_report.csv",
    index=False
)

print("\nSaved:")
print(REPORT_DIR / "var_cvar_report.csv")

print("\nTop 10 Highest Risk Funds")
print(
    risk_df.sort_values("VaR_95")
    .head(10)
)