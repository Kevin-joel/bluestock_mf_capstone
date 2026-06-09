import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"
REPORT_DIR = BASE_DIR / "reports" / "day 6"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

holdings = pd.read_csv(
    DATA_DIR / "09_portfolio_holdings_clean.csv"
)

funds = pd.read_csv(
    DATA_DIR / "01_fund_master_clean.csv"
)

holdings["weight_pct"] = (
    holdings["weight_pct"] / 100
)

hhi = (
    holdings
    .groupby("amfi_code")
    .apply(
        lambda x:
        np.sum(
            x["weight_pct"] ** 2
        )
    )
    .reset_index(
        name="HHI"
    )
)

hhi = hhi.merge(
    funds[
        ["amfi_code", "scheme_name"]
    ],
    on="amfi_code"
)

hhi = hhi.sort_values(
    "HHI",
    ascending=False
)

hhi.to_csv(
    REPORT_DIR / "sector_hhi_report.csv",
    index=False
)

print(
    hhi.head(10)
)