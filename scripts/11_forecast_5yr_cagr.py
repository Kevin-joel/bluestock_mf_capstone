import pandas as pd
import numpy as np
from pathlib import Path
from statsmodels.tsa.arima.model import ARIMA
import warnings

warnings.filterwarnings("ignore")

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

NAV_FILE = BASE_DIR / "data" / "processed" / "02_nav_history_clean.csv"
SCORECARD_FILE = BASE_DIR / "data" / "processed" / "fund_scorecard.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "cagr_forecast.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------

nav_df = pd.read_csv(NAV_FILE)
scorecard = pd.read_csv(SCORECARD_FILE)

nav_df["date"] = pd.to_datetime(nav_df["date"])

# --------------------------------------------------
# Top 10 Funds
# --------------------------------------------------

top10 = (
    scorecard
    .sort_values("overall_rank")
    .head(10)
)

results = []

print("\nForecasting Top 10 Funds...\n")

# --------------------------------------------------
# Forecast Loop
# --------------------------------------------------

for _, row in top10.iterrows():

    amfi_code = row["amfi_code"]
    scheme_name = row["scheme_name"]

    fund = (
        nav_df[
            nav_df["amfi_code"] == amfi_code
        ]
        .sort_values("date")
        .copy()
    )

    nav_series = fund["nav"]

    try:

        model = ARIMA(
            nav_series,
            order=(5, 1, 0)
        )

        fitted = model.fit()

        forecast = fitted.forecast(
            steps=252
        )

        last_nav = nav_series.iloc[-1]

        forecast_nav = forecast.iloc[-1]

        projected_return = (
            (forecast_nav / last_nav) - 1
        ) * 100

        years_available = (
            (fund["date"].max() -
             fund["date"].min()).days
        ) / 365.25

        total_years = years_available + 1

        projected_cagr = (

            (forecast_nav /
             nav_series.iloc[0])

            **

            (1 / total_years)

            - 1

        ) * 100

        results.append([
            amfi_code,
            scheme_name,
            round(last_nav, 2),
            round(forecast_nav, 2),
            round(projected_return, 2),
            "Insufficient Data",
            round(projected_cagr, 2)
        ])

        print(
            f"✓ {scheme_name[:40]}"
        )

    except Exception as e:

        print(
            f"✗ Failed: {scheme_name}"
        )

# --------------------------------------------------
# Save
# --------------------------------------------------

forecast_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "scheme_name",
        "last_nav",
        "forecast_nav_1yr",
        "projected_return_1yr_pct",
        "cagr_5yr_actual",
        "cagr_5yr_forecast"
    ]
)

forecast_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nForecast Summary\n")

print(
    forecast_df[
        [
            "scheme_name",
            "forecast_nav_1yr",
            "projected_return_1yr_pct",
            "cagr_5yr_forecast"
        ]
    ]
)

print(f"\nSaved: {OUTPUT_FILE}")