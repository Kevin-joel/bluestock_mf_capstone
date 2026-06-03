import pandas as pd

df = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

print("Negative NAVs:")
print((df["nav"] <= 0).sum())

print("Duplicate Rows:")
print(df.duplicated().sum())

print("Missing NAV:")
print(df["nav"].isnull().sum())