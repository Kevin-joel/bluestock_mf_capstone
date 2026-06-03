import pandas as pd

df = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

print("Before:", len(df))

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df = df.sort_values(
    ["amfi_code", "date"]
)

df = df.drop_duplicates()

df = df[df["nav"] > 0]

df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

print("After:", len(df))

df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("nav_history cleaned")