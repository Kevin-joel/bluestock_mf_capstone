import pandas as pd

df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

df["date"] = pd.to_datetime(df["date"])

df = df[df["aum_crore"] > 0]
df = df[df["num_schemes"] > 0]

df.to_csv(
    "data/processed/03_aum_by_fund_house_clean.csv",
    index=False
)

print("aum cleaned")