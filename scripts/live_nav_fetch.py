import pandas as pd
import requests
from pathlib import Path

# AMFI codes provided in the project
funds = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Create output folder
output_folder = Path("data/raw/live_nav")
output_folder.mkdir(parents=True, exist_ok=True)

print(f"Saving files to: {output_folder.resolve()}\n")

for fund_name, amfi_code in funds.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # NAV history data
        nav_df = pd.DataFrame(data["data"])

        output_file = output_folder / f"{fund_name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"✓ {fund_name} saved")

    except Exception as e:
        print(f"✗ Error downloading {fund_name}: {e}")

print("\nLive NAV fetch completed.")