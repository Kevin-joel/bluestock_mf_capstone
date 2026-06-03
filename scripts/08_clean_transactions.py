import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

df = df[df["amount_inr"] > 0]

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC:", len(invalid))

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("transactions cleaned")