# Day 2 Data Quality Report

## Project

Bluestock Mutual Fund Analytics Capstone

## Date

03 June 2026

---

# Objective

The objective of Day 2 was to clean, validate, and transform raw mutual fund datasets into analytics-ready datasets and load them into a structured SQLite database.

---

# Datasets Processed

| Dataset               | Records |
| --------------------- | ------: |
| Fund Master           |      40 |
| NAV History           |  46,000 |
| AUM by Fund House     |      90 |
| Monthly SIP Inflows   |      48 |
| Category Inflows      |      60 |
| Industry Folio Count  |      48 |
| Scheme Performance    |      40 |
| Investor Transactions |  32,778 |
| Portfolio Holdings    |  1,000+ |
| Benchmark Indices     |  1,000+ |

---

# Data Cleaning Activities

## 1. Fund Master

Checks Performed:

* Validated AMFI scheme codes
* Removed duplicate records
* Verified fund categories
* Standardized risk categories
* Checked expense ratio values

Result:

* Records before cleaning: 40
* Records after cleaning: 40
* No duplicate AMFI codes found

---

## 2. NAV History

Checks Performed:

* Converted date column to datetime format
* Sorted by AMFI code and date
* Removed duplicate records
* Validated NAV values > 0
* Forward-filled missing NAV values where necessary

Result:

* Records before cleaning: 46,000
* Records after cleaning: 46,000
* No invalid NAV values detected

---

## 3. AUM Dataset

Checks Performed:

* Validated AUM values
* Verified fund house names
* Standardized date format

Result:

* Records successfully cleaned and validated

---

## 4. SIP Inflows Dataset

Checks Performed:

* Converted month column
* Validated SIP inflow values
* Checked YoY growth metrics

Result:

* Dataset cleaned successfully

---

## 5. Category Inflows Dataset

Checks Performed:

* Standardized category names
* Validated inflow values

Result:

* Dataset cleaned successfully

---

## 6. Industry Folio Dataset

Checks Performed:

* Verified folio counts
* Standardized month format

Result:

* Dataset cleaned successfully

---

## 7. Scheme Performance Dataset

Checks Performed:

* Converted return metrics to numeric values
* Validated Sharpe Ratio
* Validated Alpha and Beta metrics
* Checked expense ratio range (0.1%–2.5%)

Result:

* Records before cleaning: 40
* Records after cleaning: 40
* Expense ratio anomalies exported for review

Generated File:

expense_ratio_anomalies.csv

---

## 8. Investor Transactions Dataset

Checks Performed:

* Standardized transaction types

  * SIP
  * Lumpsum
  * Redemption
* Validated transaction amounts
* Converted transaction dates
* Verified KYC status values

Allowed KYC Values:

* Verified
* Pending
* Rejected

Result:

* Records after cleaning: 32,778
* Invalid transaction records removed

---

## 9. Portfolio Holdings Dataset

Checks Performed:

* Validated stock weights
* Verified market values
* Checked positive stock prices

Result:

* Dataset cleaned successfully

---

## 10. Benchmark Indices Dataset

Checks Performed:

* Converted date format
* Validated closing index values

Result:

* Dataset cleaned successfully

---

# Database Validation

SQLite Database Created:

bluestock_mf.db

## Table Row Counts

| Table             |   Rows |
| ----------------- | -----: |
| dim_fund          |     40 |
| fact_nav          | 46,000 |
| fact_aum          |     90 |
| fact_performance  |     40 |
| fact_transactions | 32,778 |

Validation completed using:

* verify_cleaned_data.py
* verify_database.py

---

# SQL Validation

Implemented and tested 10 analytical SQL queries:

1. Top 5 Fund Houses by AUM
2. Average NAV by Fund
3. Highest 5-Year Return Funds
4. Lowest Expense Ratio Funds
5. Funds with Expense Ratio Below 1%
6. Transaction Count by State
7. Transaction Volume by Type
8. Top States by Investment Amount
9. Average Fund Performance
10. KYC Status Distribution

Result:

All SQL queries executed successfully against the SQLite database.

---

# Data Quality Summary

| Check                       | Status |
| --------------------------- | ------ |
| Duplicate Detection         | Passed |
| Missing Value Handling      | Passed |
| Date Validation             | Passed |
| Numeric Validation          | Passed |
| Expense Ratio Validation    | Passed |
| NAV Validation              | Passed |
| Transaction Validation      | Passed |
| Database Loading Validation | Passed |
| SQL Query Validation        | Passed |

---

# Conclusion

All mutual fund datasets were successfully cleaned, validated, and loaded into a structured SQLite database. Data quality checks confirmed consistency, valid business rules, and analytics readiness. The project is prepared for Exploratory Data Analysis (EDA), KPI generation, and Power BI dashboard development.
