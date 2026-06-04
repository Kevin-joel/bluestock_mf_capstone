import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "05_category_inflows_clean.csv")
    df = pd.read_csv(path)

    pivot = df.pivot_table(
        index="category",
        columns="month",
        values="net_inflow_crore",
        aggfunc="sum"
    )

    plt.figure(figsize=(14,6))
    sns.heatmap(pivot, cmap="YlGnBu")
    plt.title("Category Inflows Heatmap")
    plt.show()

if __name__ == "__main__":
    run()