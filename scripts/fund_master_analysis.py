import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nTotal Schemes:")
print(df.shape[0])

print("\nColumns:")
print(df.columns.tolist())

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

print("\nRisk Categories:")
print(df["risk_category"].unique())