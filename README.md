# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone is an end-to-end data analytics project focused on analyzing mutual fund performance, investor behavior, fund categories, portfolio holdings, and benchmark indices. The project combines data engineering, exploratory data analysis, performance analytics, SQL, and dashboarding to generate actionable investment insights.

---

## Project Objectives

* Analyze mutual fund performance across different categories.
* Evaluate historical NAV trends and fund returns.
* Study investor transaction patterns and SIP inflows.
* Compare fund performance against benchmark indices.
* Calculate performance metrics such as CAGR, Volatility, Sharpe Ratio, Beta, and Value at Risk (VaR).
* Build interactive dashboards for data-driven decision-making.

---

## Tools and Technologies

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Requests API
* Matplotlib
* Seaborn
* Plotly
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Structure

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

## Datasets Used

The project utilizes 10 mutual fund datasets covering:

* Fund Master Information
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Count
* Scheme Performance
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

Additionally, live NAV data is fetched using the mfapi.in API.

---

## Day 1 Progress

### Completed Tasks

* Project folder structure creation
* Virtual environment setup
* Dependency installation
* Data ingestion pipeline development
* Dataset quality assessment
* Fund Master exploration
* AMFI code validation
* Live NAV API integration

### Key Findings

* 40 mutual fund schemes identified.
* 10 unique fund houses analyzed.
* Five risk categories observed:

  * Low
  * Moderate
  * Moderately High
  * High
  * Very High
* AMFI validation achieved a 100% match rate.
* Live NAV data successfully retrieved and stored for selected schemes.

# Day 2 – Data Cleaning & SQLite Database Design

## Objective

Transform raw mutual fund datasets into analytics-ready datasets through data cleaning, validation, database modeling, and SQL-based analysis.

---

## Data Cleaning

The following datasets were cleaned and validated:

* Fund Master
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Count
* Scheme Performance
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

### Cleaning Activities Performed

#### Fund Master

* Removed duplicate AMFI codes
* Validated expense ratios
* Validated minimum SIP and lumpsum amounts

#### NAV History

* Converted date column to datetime format
* Sorted records by AMFI code and date
* Removed duplicate records
* Validated NAV values greater than zero
* Forward-filled missing NAV values where required

#### Investor Transactions

* Standardized transaction types:

  * SIP
  * Lumpsum
  * Redemption
* Converted transaction dates
* Validated positive transaction amounts
* Verified KYC status values

#### Scheme Performance

* Converted return metrics to numeric format
* Validated performance indicators
* Checked expense ratio range (0.1%–2.5%)
* Flagged anomalies into a separate review file

#### Portfolio Holdings

* Validated portfolio weights
* Validated market values and stock prices

---

## Data Validation

Validation scripts were executed to ensure data quality.

Checks included:

* Duplicate detection
* Missing value analysis
* Data type validation
* Business rule validation
* Range validation
* Category standardization

### Validation Results

* No duplicate records remained after cleaning
* Invalid values were removed
* Data types were standardized
* Clean datasets were generated successfully

---

## SQLite Star Schema Design

A star schema was designed for analytical processing.

### Dimension Tables

#### dim_fund

Stores mutual fund scheme information.

Columns:

* amfi_code
* fund_house
* scheme_name
* category
* sub_category
* plan
* fund_manager
* risk_category

#### dim_date

Stores calendar attributes for time-based analysis.

Columns:

* date_id
* full_date
* year
* quarter
* month
* day

### Fact Tables

#### fact_nav

Stores daily NAV history.

#### fact_transactions

Stores investor transaction records.

#### fact_performance

Stores scheme performance metrics.

#### fact_aum

Stores fund house AUM information.

---

## Database Loading

Cleaned datasets were loaded into SQLite using:

* SQLAlchemy
* Pandas `to_sql()`

Database created:

```text
bluestock_mf.db
```

### Row Counts

| Table             |   Rows |
| ----------------- | -----: |
| dim_fund          |     40 |
| fact_nav          | 46,000 |
| fact_aum          |     90 |
| fact_performance  |     40 |
| fact_transactions | 32,778 |

---

## SQL Analytics

Ten analytical SQL queries were implemented and validated.

Examples:

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

All queries executed successfully against the SQLite database.

---

## Deliverables

* 10 cleaned CSV datasets
* SQLite database (`bluestock_mf.db`)
* `schema.sql`
* `queries.sql`
* Data quality report
* Database verification scripts
* SQL query execution scripts

---

## Outcome

The raw mutual fund datasets were successfully transformed into a validated, analytics-ready database. The project is now prepared for Exploratory Data Analysis (EDA), KPI generation, and Power BI dashboard development.



## Day 3 – Exploratory Data Analysis (EDA)

### Objective

Perform comprehensive exploratory data analysis on the processed mutual fund datasets to uncover industry trends, investor behavior, fund performance patterns, and portfolio allocation insights.

### Datasets Used

* Fund Master
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Counts
* Scheme Performance
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

### Analysis Performed

#### 1. NAV Trend Analysis

* Visualized daily NAV movement for all 40 mutual fund schemes.
* Highlighted the 2023 market bull run.
* Marked the 2024 market correction period.
* Implemented using Plotly interactive visualizations.

#### 2. AUM Growth Analysis

* Analyzed Assets Under Management (AUM) growth across fund houses.
* Compared yearly AUM trends.
* Identified SBI Mutual Fund as the industry leader.

#### 3. SIP Inflow Analysis

* Evaluated monthly SIP inflow trends from 2022–2025.
* Identified the highest SIP inflow period.
* Visualized long-term growth in retail participation.

#### 4. Category-Wise Inflow Analysis

* Created heatmaps to analyze inflow patterns across fund categories.
* Compared category performance over multiple time periods.
* Identified categories with consistently high investor interest.

#### 5. Investor Demographics Analysis

* Studied investor age-group distribution.
* Compared investment behavior across age groups.
* Analyzed gender participation in mutual fund investments.

#### 6. Geographic Analysis

* Examined state-wise investment distribution.
* Compared T30 and B30 city participation.
* Evaluated regional mutual fund adoption trends.

#### 7. Folio Growth Analysis

* Visualized growth in mutual fund folio counts.
* Tracked expansion of retail investor participation.
* Identified major growth milestones.

#### 8. Return Correlation Analysis

* Generated correlation matrices for fund performance metrics.
* Explored relationships between returns across schemes.
* Identified diversification opportunities.

#### 9. Sector Allocation Analysis

* Aggregated portfolio holdings by sector.
* Created sector allocation donut charts.
* Identified dominant sectors in mutual fund portfolios.

### Key Findings

1. Mutual fund NAVs experienced strong growth during the 2023 bull market.
2. Market corrections were visible across several schemes during 2024.
3. SBI Mutual Fund maintained the highest AUM among major fund houses.
4. SIP participation continued to increase throughout the study period.
5. Retail investor activity showed consistent long-term growth.
6. Folio counts increased significantly, indicating rising investor participation.
7. Younger investors formed a substantial portion of the investor base.
8. B30 cities contributed meaningfully to industry growth.
9. Correlation analysis highlighted diversification opportunities.
10. Financial and related sectors represented a major share of portfolio allocations.

### Deliverables

* EDA_Analysis.ipynb
* EDA_Report.pdf
* Multiple visualization scripts
* Exported charts for reporting and presentation
* Documented EDA insights and observations

### Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Jupyter Notebook

### Outcome

Successfully completed a full-scale exploratory data analysis pipeline, generating actionable insights and visual reports that will support subsequent dashboard development and predictive analytics phases.





## Day 4 – Fund Performance Analytics

### Objective

Evaluate the performance of 40 mutual fund schemes using return-based, risk-adjusted, benchmark-relative, and predictive analytics techniques.

### Tasks Completed

#### 1. Daily Return Analysis

* Computed daily returns for all mutual fund schemes using:

  `daily_return = NAV(t) / NAV(t-1) - 1`

* Generated return distribution statistics to validate data quality and identify volatility characteristics.

* Processed approximately 46,000 NAV observations.

#### 2. CAGR Analysis

* Calculated annualized returns (CAGR) across available periods.
* Generated comparative rankings for all funds.
* Identified top-performing schemes based on long-term growth metrics.

#### 3. Risk-Adjusted Performance Metrics

Implemented industry-standard risk measures:

* **Sharpe Ratio**

  * Risk-free rate assumed at 6.5%.
  * Ranked funds based on excess return per unit of risk.

* **Sortino Ratio**

  * Measured downside-risk-adjusted performance.
  * Focused on negative return volatility only.

#### 4. Alpha & Beta Analysis

* Used linear regression against the NIFTY100 benchmark.
* Calculated:

  * Alpha (benchmark outperformance)
  * Beta (market sensitivity)
  * R² (benchmark correlation strength)

#### 5. Maximum Drawdown Analysis

* Measured largest peak-to-trough decline for every fund.
* Identified highest-risk and lowest-risk schemes.
* Generated drawdown rankings and summary statistics.

#### 6. Composite Fund Scorecard

Developed a weighted scoring framework (0–100):

* 30% → 3-Year CAGR Rank
* 25% → Sharpe Ratio Rank
* 20% → Alpha Rank
* 15% → Expense Ratio Rank (Inverse)
* 10% → Maximum Drawdown Rank (Inverse)

Generated:

* Overall Fund Score
* Fund Rankings
* Top and Bottom Performing Funds

#### 7. Benchmark Comparison

Compared top-ranked funds against:

* NIFTY50
* NIFTY100

Performed:

* Normalized growth comparison
* Benchmark performance analysis
* Tracking Error calculation

#### 8. Predictive Analytics (Bonus)

Implemented ARIMA-based NAV forecasting for top-performing funds.

Outputs:

* Forecasted 1-Year NAV
* Projected Return
* Forecasted 5-Year CAGR

Note:
Actual historical 5-Year CAGR could not be computed due to insufficient historical data (2022–2026). Forecasted values were generated separately using time-series modeling.

### Deliverables Generated

#### Processed Datasets

* daily_returns.csv
* cagr_summary.csv
* sharpe_sortino.csv
* alpha_beta.csv
* max_drawdown.csv
* fund_scorecard.csv
* tracking_error.csv
* cagr_forecast.csv

#### Visual Outputs

* Benchmark Comparison Chart
* Return Distribution Analysis
* CAGR Rankings
* Sharpe Ratio Rankings
* Alpha Rankings
* Drawdown Analysis
* Fund Scorecard Visualizations
* Forecasted CAGR Analysis

### Key Outcomes

* Ranked all 40 mutual fund schemes using quantitative performance metrics.
* Identified top-performing funds based on return, risk, and benchmark-adjusted measures.
* Evaluated benchmark tracking efficiency using tracking error.
* Added predictive analytics capability through ARIMA forecasting.
* Built a comprehensive performance evaluation framework suitable for investment analytics and reporting.


---

## Current Status

Day 1 Completed

<<<<<<< HEAD
Day 2 – Data Cleaning & Database Creation [ COMPLETED]

Day 3 – Exploratory Data Analysis [COMPLETED] " Refer chart images of day 3 pngs"
=======
Day 2 – Data Cleaning & Database Creation [COMPLETED]

Day 3 – Exploratory Data Analysis [COMPLETED]
>>>>>>> 76c9f7f (Update README with Day 4 performance analytics)

Day 4 – Performance Analytics [COMPLETED]

Day 5 – Dashboard Development

Day 6 – Advanced Analytics

Day 7 – Final Report & Presentation

---

## Author

Kevin Joel Velevela
velevelakevinjoel@gmail.com


Bluestock Mutual Fund Analytics Capstone Project





