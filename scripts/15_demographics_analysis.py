import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "08_investor_transactions_clean.csv")
    df = pd.read_csv(path)

    # Age distribution
    df["age_group"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Age Distribution")
    plt.show()

    # SIP by age group
    plt.figure(figsize=(10,5))
    sns.boxplot(data=df, x="age_group", y="amount_inr")
    plt.title("Investment Amount by Age Group")
    plt.show()

    # Gender split
    df["gender"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Gender Split")
    plt.show()

if __name__ == "__main__":
    run()