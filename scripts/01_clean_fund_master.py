import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Before:", len(df))

# Remove duplicate AMFI codes
df = df.drop_duplicates(subset=["amfi_code"])

# Convert date
df["launch_date"] = pd.to_datetime(
    df["launch_date"],
    errors="coerce"
)

# Validate numeric fields
df = df[df["expense_ratio_pct"] > 0]
df = df[df["min_sip_amount"] > 0]
df = df[df["min_lumpsum_amount"] > 0]

print("After:", len(df))

df.to_csv(
    "data/processed/01_fund_master_clean.csv",
    index=False
)

print("fund_master cleaned")