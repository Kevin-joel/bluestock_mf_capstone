"""
Bluestock Mutual Fund Analytics Capstone
Master Execution Pipeline

Author: Kevin Joel

Description:
Runs the complete ETL and validation workflow for the
Bluestock Mutual Fund Analytics project.
"""

import subprocess
import sys
from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).resolve().parent

# Core ETL + Validation Pipeline
PIPELINE = [
    "scripts/data_ingestion.py",
    "scripts/create_database.py",

    "scripts/01_clean_fund_master.py",
    "scripts/02_clean_nav_history.py",
    "scripts/03_clean_aum.py",
    "scripts/04_clean_sip_inflows.py",
    "scripts/06_clean_folio_count.py",
    "scripts/07_clean_scheme_performance.py",
    "scripts/08_clean_transactions.py",
    "scripts/09_clean_portfolio_holdings.py",
    "scripts/10_clean_benchmark.py",

    "scripts/load_database.py",

    "scripts/amfi_validation.py",
    "scripts/verify_cleaned_data.py",
    "scripts/verify_database.py"
]


def run_script(script_path):
    """
    Execute a Python script and return success status.
    """
    full_path = ROOT_DIR / script_path

    if not full_path.exists():
        print(f"❌ File not found: {script_path}")
        return False

    print("\n" + "=" * 70)
    print(f"Running: {script_path}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, str(full_path)]
    )

    return result.returncode == 0


def main():
    """
    Run the entire Bluestock ETL pipeline.
    """

    print("\n" + "#" * 70)
    print("BLUESTOCK MUTUAL FUND ANALYTICS CAPSTONE")
    print("MASTER PIPELINE EXECUTION")
    print("#" * 70)

    successful = []
    failed = []

    for script in PIPELINE:

        if run_script(script):
            print(f"✅ Completed: {script}")
            successful.append(script)
        else:
            print(f"❌ Failed: {script}")
            failed.append(script)

    print("\n" + "#" * 70)
    print("PIPELINE SUMMARY")
    print("#" * 70)

    print(f"Total Scripts : {len(PIPELINE)}")
    print(f"Successful    : {len(successful)}")
    print(f"Failed        : {len(failed)}")

    if failed:
        print("\nFailed Scripts:")
        for script in failed:
            print(f" - {script}")
    else:
        print("\n🎉 All scripts executed successfully!")

    print("\nPipeline execution finished.")


if __name__ == "__main__":
    main()