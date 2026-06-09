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

## Day 5 – Dashboard Development (Power BI)

### Objective

Develop an interactive business intelligence dashboard to analyze mutual fund industry trends, fund performance, investor behavior, and SIP market insights using Power BI.

### Data Sources

The dashboard was built using the cleaned datasets generated during previous project phases:

* Fund Master Data
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Counts
* Scheme Performance Metrics
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

### Dashboard Pages

#### 1. Industry Overview

* KPI Cards for Total AUM, SIP Inflows, Folios, and Schemes
* Industry AUM Trend Analysis
* AUM Distribution by Fund House
* Interactive Year Filtering

#### 2. Fund Performance

* Risk vs Return Scatter Plot
* Fund Performance Scorecard
* NAV Trend Analysis
* Fund House, Category, and Plan Filters

#### 3. Investor Analytics

* State-wise Transaction Analysis
* Transaction Type Distribution (SIP, Lumpsum, Redemption)
* Average Investment by Age Group
* Monthly Transaction Volume Trends
* Demographic and Geographic Filters

#### 4. SIP & Market Trends

* SIP Inflow Trend Analysis
* Category Inflow Heatmap
* Top Categories by Net Inflow
* Market Trend Monitoring Dashboard

### Key Features

* Interactive filtering and cross-visual analysis
* Dynamic KPI monitoring
* Demographic and geographic investor insights
* Mutual fund performance benchmarking
* SIP and market trend visualization

### Deliverables

* `bluestock_mf_dashboard.pbix`
* `bluestock_mf_dashboard.pdf`
* Industry Overview Screenshot
* Fund Performance Screenshot
* Investor Analytics Screenshot
* SIP & Market Trends Screenshot

### Technologies Used

* Power BI Desktop
* DAX Measures
* Data Modeling
* Interactive Visualizations
* Business Intelligence Reporting

### Outcome

Successfully developed a multi-page Power BI dashboard providing comprehensive insights into mutual fund industry performance, investor behavior, SIP trends, and fund analytics for business decision-making and reporting.


# Day 6 — Advanced Analytics & Risk Metrics

## Objective

The goal of Day 6 was to move beyond descriptive analytics and implement advanced risk analysis, investor behavior analytics, portfolio concentration measurement, and a recommendation system for mutual funds.

---

## Tasks Completed

### 1. Historical VaR & CVaR Analysis

Calculated historical Value at Risk (VaR 95%) and Conditional Value at Risk (CVaR 95%) using daily NAV return distributions for all 40 mutual fund schemes.

**Metrics Computed**

* VaR (95%) = 5th percentile of daily returns
* CVaR (95%) = Average return below the VaR threshold

**Output**

* `reports/day 6/var_cvar_report.csv`

**Key Finding**
Small-cap funds such as SBI Small Cap Fund, Axis Small Cap Fund, and ABSL Small Cap Fund exhibited the highest downside risk with the most negative VaR and CVaR values.

---

### 2. Rolling 90-Day Sharpe Ratio

Calculated rolling risk-adjusted performance using a 90-day rolling window of daily returns.

**Formula**

Rolling Sharpe Ratio =

(Rolling Mean Return / Rolling Standard Deviation) × √252

**Analysis**

* Selected top 5 funds based on AUM.
* Visualized risk-adjusted performance over time.

**Output**

* `reports/day 6/rolling_sharpe_chart.png`

---

### 3. Investor Cohort Analysis

Segmented investors based on the year of their first transaction and analyzed investment behavior across cohorts.

**Metrics**

* Average Investment Amount
* Total Invested Amount
* Number of Investors
* Most Preferred Fund

**Output**

* `reports/day 6/investor_cohort_analysis.csv`

**Key Finding**
The 2024 investor cohort accounted for the majority of total investments and showed a strong preference for Mirae Asset Emerging Bluechip Fund.

---

### 4. SIP Continuity Analysis

Evaluated consistency of SIP investments by analyzing transaction gaps for investors with at least six SIP transactions.

**Logic**

* Computed average gap between SIP transactions.
* Investors with an average gap greater than 35 days were flagged as "At-Risk".

**Output**

* `reports/day 6/sip_continuity_report.csv`

**Key Finding**
Only 2.20% of eligible investors maintained healthy SIP continuity, indicating significant discontinuity risk among SIP investors.

---

### 5. Sector Concentration Analysis (HHI)

Measured portfolio concentration using the Herfindahl-Hirschman Index (HHI).

**Formula**

HHI = Σ(weight²)

Higher HHI values indicate greater portfolio concentration.

**Output**

* `reports/day 6/sector_hhi_report.csv`

**Key Finding**
Axis Bluechip Fund exhibited the highest portfolio concentration among analyzed funds.

---

### 6. Mutual Fund Recommendation System

Built a rule-based recommendation engine that suggests mutual funds according to investor risk appetite.

**Inputs**

* Low Risk
* Moderate Risk
* High Risk

**Ranking Criteria**

* Sharpe Ratio
* Historical Performance
* Risk Grade

**Output**

* `src/recommender.py`

**Sample Recommendation (High Risk)**

1. Kotak Emerging Equity Fund
2. ICICI Prudential Midcap Fund
3. DSP Midcap Fund

---

## Deliverables

* Advanced_Analytics.ipynb
* var_cvar_report.csv
* rolling_sharpe_chart.png
* investor_cohort_analysis.csv
* sip_continuity_report.csv
* sector_hhi_report.csv
* recommender.py

---

## Key Business Insights

1. Small-cap mutual funds demonstrated the highest downside risk based on VaR and CVaR analysis.
2. Investor participation was heavily concentrated in the 2024 cohort, which contributed the largest investment volume.
3. SIP continuity analysis revealed that most investors exhibit irregular contribution behavior.
4. Portfolio concentration analysis identified Axis Bluechip Fund as the most concentrated equity portfolio.
5. High-risk mid-cap and emerging equity funds delivered the strongest risk-adjusted returns according to Sharpe ratio rankings.

---

## Skills Demonstrated

* Financial Risk Analytics
* VaR & CVaR Modeling
* Sharpe Ratio Analysis
* Time-Series Analysis
* Investor Segmentation
* Cohort Analysis
* SIP Behavior Analytics
* Portfolio Concentration Measurement (HHI)
* Recommendation Systems
* Python (Pandas, NumPy, Matplotlib)
* Business Insight Generation


## Current Status

Day 1 Completed

Day 2 – Data Cleaning & Database Creation [ COMPLETED]

Day 3 – Exploratory Data Analysis [COMPLETED] " Refer chart images of day 3 pngs"

Day 4 – Performance Analytics [COMPLETED]

Day 5 – Dashboard Development [ COMPLETED ]

Day 6 – Advanced Analytics [ COMPLETED ]

Day 7 – Final Report & Presentation

## Author

Kevin Joel Velevela
velevelakevinjoel@gmail.com


Bluestock Mutual Fund Analytics Capstone Project





