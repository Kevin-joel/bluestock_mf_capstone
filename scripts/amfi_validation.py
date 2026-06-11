"""
AMFI Code Validation Module

Purpose:
Validates the consistency of AMFI codes between the fund master
dataset and NAV history dataset to ensure referential integrity.

Author: Kevin Joel
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd


FUND_MASTER_PATH = "data/raw/01_fund_master.csv"
NAV_HISTORY_PATH = "data/raw/02_nav_history.csv"


def validate_amfi_codes():
    """
    Compare AMFI codes across datasets and report match statistics.
    """

    fund_master = pd.read_csv(FUND_MASTER_PATH)
    nav_history = pd.read_csv(NAV_HISTORY_PATH)

    fund_codes = set(fund_master["amfi_code"])
    nav_codes = set(nav_history["amfi_code"])

    matched_codes = fund_codes.intersection(nav_codes)
    missing_codes = fund_codes.difference(nav_codes)

    match_rate = (len(matched_codes) / len(fund_codes)) * 100

    print("\nAMFI Code Validation Summary")
    print("-" * 40)
    print(f"Total Fund Master Codes : {len(fund_codes)}")
    print(f"Matched NAV Codes       : {len(matched_codes)}")
    print(f"Missing Codes           : {len(missing_codes)}")
    print(f"Match Rate              : {match_rate:.2f}%")

    if missing_codes:
        print("\nValidation Status: WARNING")
        print(
            f"{len(missing_codes)} AMFI code(s) from the fund master "
            "dataset were not found in NAV history."
        )
    else:
        print("\nValidation Status: PASSED")
        print("All AMFI codes are present in NAV history.")


def main():
    """
    Execute AMFI code validation.
    """
    validate_amfi_codes()


if __name__ == "__main__":
    main()