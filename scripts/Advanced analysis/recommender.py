import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

performance = pd.read_csv(
    BASE_DIR /
    "data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "\nEnter Risk Appetite (Low / Moderate / High): "
)

result = (
    performance[
        performance["risk_grade"]
        .str.lower()
        ==
        risk.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop Recommended Funds\n")

print(
    result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_5yr_pct"
        ]
    ]
)