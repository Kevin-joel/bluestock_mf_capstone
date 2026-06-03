-- =====================================================
-- QUERY 1 : Top 5 Fund Houses by AUM
-- =====================================================

SELECT
    fund_house,
    MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;


-- =====================================================
-- QUERY 2 : Average NAV by Fund
-- =====================================================

SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;


-- =====================================================
-- QUERY 3 : Highest 5-Year Return Funds
-- =====================================================

SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- =====================================================
-- QUERY 4 : Lowest Expense Ratio Funds
-- =====================================================

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 10;


-- =====================================================
-- QUERY 5 : Funds With Expense Ratio Below 1%
-- =====================================================

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- =====================================================
-- QUERY 6 : Transaction Count By State
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- =====================================================
-- QUERY 7 : Transaction Volume By Type
-- =====================================================

SELECT
    transaction_type,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- =====================================================
-- QUERY 8 : Top States By Investment Amount
-- =====================================================

SELECT
    state,
    ROUND(SUM(amount_inr),2) AS investment_amount
FROM fact_transactions
GROUP BY state
ORDER BY investment_amount DESC
LIMIT 10;


-- =====================================================
-- QUERY 9 : Average Fund Performance
-- =====================================================

SELECT
    ROUND(AVG(return_1yr_pct),2) AS avg_1yr_return,
    ROUND(AVG(return_3yr_pct),2) AS avg_3yr_return,
    ROUND(AVG(return_5yr_pct),2) AS avg_5yr_return
FROM fact_performance;


-- =====================================================
-- QUERY 10 : KYC Status Distribution
-- =====================================================

SELECT
    kyc_status,
    COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY kyc_status;