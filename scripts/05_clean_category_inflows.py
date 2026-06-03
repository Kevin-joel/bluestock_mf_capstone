import pandas as pd

df = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

df["month"] = pd.to_datetime(
    df["month"],
    format="%Y-%m"
)

df.to_csv(
    "data/processed/05_category_inflows_clean.csv",
    index=False
)

print("category inflows cleaned")