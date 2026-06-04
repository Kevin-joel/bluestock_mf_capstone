import pandas as pd
import plotly.express as px
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "06_industry_folio_count_clean.csv")
    df = pd.read_csv(path)

    df["month"] = pd.to_datetime(df["month"])

    fig = px.line(
        df,
        x="month",
        y="total_folios_crore",
        title="Folio Growth Trend"
    )

    fig.show()

if __name__ == "__main__":
    run()