import pandas as pd
import plotly.express as px
import os

BASE = os.path.dirname(os.path.dirname(__file__))

def run():

    path = os.path.join(BASE, "data", "processed", "04_monthly_sip_inflows_clean.csv")
    sip_df = pd.read_csv(path)

    sip_df["month"] = pd.to_datetime(sip_df["month"])

    sip_monthly = sip_df.groupby("month")["sip_inflow_crore"].sum().reset_index()

    fig = px.line(
        sip_monthly,
        x="month",
        y="sip_inflow_crore",
        title="SIP Inflows Trend"
    )

    max_row = sip_monthly.loc[sip_monthly["sip_inflow_crore"].idxmax()]

    fig.add_annotation(
        x=max_row["month"],
        y=max_row["sip_inflow_crore"],
        text="ATH SIP Inflow",
        showarrow=True
    )

    fig.show()

if __name__ == "__main__":
    run()