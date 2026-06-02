import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

matched_codes = fund_codes.intersection(nav_codes)
missing_codes = fund_codes - nav_codes

print("\nAMFI CODE VALIDATION")
print("-" * 40)

print(f"Total Fund Master Codes : {len(fund_codes)}")
print(f"Codes Found in NAV     : {len(matched_codes)}")
print(f"Missing Codes          : {len(missing_codes)}")

match_rate = (len(matched_codes) / len(fund_codes)) * 100

print(f"Match Rate             : {match_rate:.2f}%")

if missing_codes:
    print("\nMissing Codes:")
    print(sorted(missing_codes))
else:
    print("\nAll AMFI codes are present in NAV history.")