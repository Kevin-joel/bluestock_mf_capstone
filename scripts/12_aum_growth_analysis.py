import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "03_aum_by_fund_house_clean.csv")
    aum_df = pd.read_csv(path)

    aum_df["date"] = pd.to_datetime(aum_df["date"])
    aum_df["year"] = aum_df["date"].dt.year

    yearly = aum_df.groupby(["fund_house", "year"])["aum_crore"].sum().reset_index()

    pivot = yearly.pivot(index="fund_house", columns="year", values="aum_crore").fillna(0)

    pivot.plot(kind="bar", figsize=(12,6))
    plt.title("AUM Growth by Fund House")
    plt.ylabel("AUM (Crore)")
    plt.show()

if __name__ == "__main__":
    run()