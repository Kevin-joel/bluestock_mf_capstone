import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

cagr = pd.read_csv(BASE_DIR / "data/processed/cagr_summary.csv")
sharpe = pd.read_csv(BASE_DIR / "data/processed/sharpe_sortino.csv")
alpha = pd.read_csv(BASE_DIR / "data/processed/alpha_beta.csv")
drawdown = pd.read_csv(BASE_DIR / "data/processed/max_drawdown.csv")
funds = pd.read_csv(BASE_DIR / "data/processed/01_fund_master_clean.csv")

# --------------------------------------------------
# Merge
# --------------------------------------------------

scorecard = funds[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "expense_ratio_pct"
    ]
]

scorecard = scorecard.merge(
    cagr[["amfi_code", "cagr_3yr"]],
    on="amfi_code",
    how="left"
)

scorecard = scorecard.merge(
    sharpe[["amfi_code", "sharpe_ratio"]],
    on="amfi_code",
    how="left"
)

scorecard = scorecard.merge(
    alpha[["amfi_code", "alpha_pct"]],
    on="amfi_code",
    how="left"
)

scorecard = scorecard.merge(
    drawdown[["amfi_code", "max_drawdown_pct"]],
    on="amfi_code",
    how="left"
)

# --------------------------------------------------
# Ranking
# --------------------------------------------------

scorecard["cagr_rank"] = scorecard["cagr_3yr"].rank(
    ascending=False,
    method="dense"
)

scorecard["sharpe_rank"] = scorecard["sharpe_ratio"].rank(
    ascending=False,
    method="dense"
)

scorecard["alpha_rank"] = scorecard["alpha_pct"].rank(
    ascending=False,
    method="dense"
)

scorecard["expense_rank"] = scorecard["expense_ratio_pct"].rank(
    ascending=True,
    method="dense"
)

scorecard["drawdown_rank"] = scorecard["max_drawdown_pct"].rank(
    ascending=False,
    method="dense"
)

n = len(scorecard)

scorecard["cagr_score"] = n + 1 - scorecard["cagr_rank"]
scorecard["sharpe_score"] = n + 1 - scorecard["sharpe_rank"]
scorecard["alpha_score"] = n + 1 - scorecard["alpha_rank"]
scorecard["expense_score"] = n + 1 - scorecard["expense_rank"]
scorecard["drawdown_score"] = n + 1 - scorecard["drawdown_rank"]

# --------------------------------------------------
# Weighted Composite
# --------------------------------------------------

scorecard["fund_score"] = (

    scorecard["cagr_score"] * 0.30 +

    scorecard["sharpe_score"] * 0.25 +

    scorecard["alpha_score"] * 0.20 +

    scorecard["expense_score"] * 0.15 +

    scorecard["drawdown_score"] * 0.10

)

# Normalize to 100

scorecard["fund_score"] = (
    scorecard["fund_score"] /
    scorecard["fund_score"].max()
) * 100

scorecard["fund_score"] = scorecard["fund_score"].round(2)

# --------------------------------------------------
# Final Rank
# --------------------------------------------------

scorecard["overall_rank"] = scorecard[
    "fund_score"
].rank(
    ascending=False,
    method="dense"
)

scorecard = scorecard.sort_values(
    "overall_rank"
)

# --------------------------------------------------
# Save
# --------------------------------------------------

output = BASE_DIR / "data/processed/fund_scorecard.csv"

scorecard.to_csv(
    output,
    index=False
)

print("\nTOP 10 FUNDS\n")

print(
    scorecard[
        [
            "overall_rank",
            "scheme_name",
            "fund_score",
            "cagr_3yr",
            "sharpe_ratio",
            "alpha_pct"
        ]
    ].head(10)
)

print(f"\nSaved: {output}")