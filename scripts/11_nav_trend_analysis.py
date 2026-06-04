import pandas as pd
import plotly.express as px
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "02_nav_history_clean.csv")
    nav_df = pd.read_csv(path)

    nav_df["date"] = pd.to_datetime(nav_df["date"])

    # Join scheme name from fund master (IMPORTANT FIX)
    master_path = os.path.join(BASE, "data", "processed", "01_fund_master_clean.csv")
    master_df = pd.read_csv(master_path)

    nav_df = nav_df.merge(master_df[["amfi_code", "scheme_name"]], on="amfi_code", how="left")

    nav_daily = nav_df.groupby(["date", "scheme_name"])["nav"].mean().reset_index()

    fig = px.line(
        nav_daily,
        x="date",
        y="nav",
        color="scheme_name",
        title="NAV Trend (2022–2026)"
    )

    fig.add_vrect(
        x0="2023-01-01",
        x1="2023-12-31",
        fillcolor="green",
        opacity=0.15,
        annotation_text="Bull Run 2023"
    )

    fig.add_vrect(
        x0="2024-01-01",
        x1="2024-12-31",
        fillcolor="red",
        opacity=0.15,
        annotation_text="Correction 2024"
    )

    fig.show()

if __name__ == "__main__":
    run()