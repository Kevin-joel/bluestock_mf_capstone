import pandas as pd

df = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

df["month"] = pd.to_datetime(
    df["month"],
    format="%Y-%m"
)

df.to_csv(
    "data/processed/04_monthly_sip_inflows_clean.csv",
    index=False
)

print("sip inflows cleaned")