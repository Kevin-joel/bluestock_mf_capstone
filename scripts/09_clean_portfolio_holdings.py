import pandas as pd

df = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"]
)

df = df[
    (df["weight_pct"] >= 0)
    &
    (df["weight_pct"] <= 100)
]

df = df[df["market_value_cr"] > 0]
df = df[df["current_price_inr"] > 0]

df.to_csv(
    "data/processed/09_portfolio_holdings_clean.csv",
    index=False
)

print("portfolio cleaned")