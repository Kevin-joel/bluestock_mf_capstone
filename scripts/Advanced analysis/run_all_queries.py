import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

queries = {

    "Query 1 - Top 5 Fund Houses by AUM": """
    SELECT
        fund_house,
        MAX(aum_crore) AS max_aum
    FROM fact_aum
    GROUP BY fund_house
    ORDER BY max_aum DESC
    LIMIT 5;
    """,

    "Query 2 - Average NAV by Fund": """
    SELECT
        amfi_code,
        ROUND(AVG(nav),2) AS avg_nav
    FROM fact_nav
    GROUP BY amfi_code
    ORDER BY avg_nav DESC;
    """,

    "Query 3 - Highest 5 Year Return Funds": """
    SELECT
        amfi_code,
        return_5yr_pct
    FROM fact_performance
    ORDER BY return_5yr_pct DESC
    LIMIT 10;
    """,

    "Query 4 - Lowest Expense Ratio Funds": """
    SELECT
        amfi_code,
        expense_ratio_pct
    FROM fact_performance
    ORDER BY expense_ratio_pct ASC
    LIMIT 10;
    """,

    "Query 5 - Funds With Expense Ratio Below 1%": """
    SELECT
        amfi_code,
        expense_ratio_pct
    FROM fact_performance
    WHERE expense_ratio_pct < 1;
    """,

    "Query 6 - Transaction Count By State": """
    SELECT
        state,
        COUNT(*) AS total_transactions
    FROM fact_transactions
    GROUP BY state
    ORDER BY total_transactions DESC;
    """,

    "Query 7 - Transaction Volume By Type": """
    SELECT
        transaction_type,
        ROUND(SUM(amount_inr),2) AS total_amount
    FROM fact_transactions
    GROUP BY transaction_type;
    """,

    "Query 8 - Top States By Investment Amount": """
    SELECT
        state,
        ROUND(SUM(amount_inr),2) AS investment_amount
    FROM fact_transactions
    GROUP BY state
    ORDER BY investment_amount DESC
    LIMIT 10;
    """,

    "Query 9 - Average Fund Performance": """
    SELECT
        ROUND(AVG(return_1yr_pct),2) AS avg_1yr_return,
        ROUND(AVG(return_3yr_pct),2) AS avg_3yr_return,
        ROUND(AVG(return_5yr_pct),2) AS avg_5yr_return
    FROM fact_performance;
    """,

    "Query 10 - KYC Status Distribution": """
    SELECT
        kyc_status,
        COUNT(*) AS investor_count
    FROM fact_transactions
    GROUP BY kyc_status;
    """
}

for title, query in queries.items():

    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)

    df = pd.read_sql(query, conn)

    print(df)

conn.close()

print("\nAll 10 queries executed successfully.")