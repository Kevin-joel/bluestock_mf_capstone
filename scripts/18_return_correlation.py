import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "07_scheme_performance_clean.csv")
    df = pd.read_csv(path)

    pivot = df.pivot_table(
        index="scheme_name",
        values=["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]
    )

    corr = pivot.corr()

    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Return Correlation Matrix")
    plt.show()

if __name__ == "__main__":
    run()