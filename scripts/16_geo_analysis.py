import pandas as pd
import matplotlib.pyplot as plt
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "08_investor_transactions_clean.csv")
    df = pd.read_csv(path)

    state = df.groupby("state")["amount_inr"].sum().sort_values()

    plt.figure(figsize=(10,6))
    state.plot(kind="barh")
    plt.title("Investment by State")
    plt.show()

    df["city_tier"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("T30 vs B30 Cities")
    plt.show()

if __name__ == "__main__":
    run()