import pandas as pd

df = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

df["month"] = pd.to_datetime(
    df["month"],
    format="%Y-%m"
)

df.to_csv(
    "data/processed/06_industry_folio_count_clean.csv",
    index=False
)

print("folio count cleaned")