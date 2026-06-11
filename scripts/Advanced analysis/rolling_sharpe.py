import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"
REPORT_DIR = BASE_DIR / "reports" / "day 6"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load data
nav = pd.read_csv(
    DATA_DIR / "02_nav_history_clean.csv"
)

performance = pd.read_csv(
    DATA_DIR / "07_scheme_performance_clean.csv"
)

# Prepare NAV
nav["date"] = pd.to_datetime(nav["date"])

pivot_nav = nav.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

daily_returns = pivot_nav.pct_change()

# Top 5 funds by AUM
top5 = (
    performance
    .sort_values(
        "aum_crore",
        ascending=False
    )
    .head(5)
)

plt.figure(figsize=(14, 7))

for _, row in top5.iterrows():

    code = row["amfi_code"]

    returns = daily_returns[code]

    rolling_sharpe = (
        returns.rolling(90).mean()
        /
        returns.rolling(90).std()
    ) * np.sqrt(252)

    plt.plot(
        rolling_sharpe.index,
        rolling_sharpe,
        label=row["scheme_name"]
    )

plt.title("Rolling 90-Day Sharpe Ratio")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend()

plt.tight_layout()

plt.savefig(
    REPORT_DIR / "rolling_sharpe_chart.png",
    dpi=300
)

plt.close()

print(
    "\nSaved:"
)

print(
    REPORT_DIR / "rolling_sharpe_chart.png"
)