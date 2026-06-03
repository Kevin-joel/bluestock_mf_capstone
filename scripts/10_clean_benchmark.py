import pandas as pd

df = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

df["date"] = pd.to_datetime(
    df["date"]
)

df = df[df["close_value"] > 0]

df.to_csv(
    "data/processed/10_benchmark_indices_clean.csv",
    index=False
)

print("benchmark cleaned")