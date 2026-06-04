import pandas as pd
import plotly.graph_objects as go
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "09_portfolio_holdings_clean.csv")
    df = pd.read_csv(path)

    sector = df.groupby("sector")["weight_pct"].sum().reset_index()

    fig = go.Figure(data=[go.Pie(
        labels=sector["sector"],
        values=sector["weight_pct"],
        hole=0.5
    )])

    fig.update_layout(title="Sector Allocation")
    fig.show()

if __name__ == "__main__":
    run()