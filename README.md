## 📊 Cross Market Analysis: Crypto, Oil & Stocks

This project analyzes the relationship between cryptocurrency prices, oil prices, and stock market indices using **SQL analytics and a Streamlit dashboard**.

The goal is to collect financial data from multiple sources, store it in a relational database, and perform cross-market analysis.

---

# 🚀 Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- CoinGecko API
- Yahoo Finance API
- SQL

---

# 📂 Project Structure

cross-market-analysis/

│

├── app.py

├── analysis.py

├── Market.db

├── requirements.txt

└── pages/

&nbsp;&nbsp;&nbsp;&nbsp;├── 1_Filters_&_Data_Exploration.py

&nbsp;&nbsp;&nbsp;&nbsp;├── 2_SQL_Query_Runner.py

&nbsp;&nbsp;&nbsp;&nbsp;└── 3_Top_3_Crypto_Analysis.py

---

# 📊 Streamlit App Pages

## 1️⃣ Filters & Data Exploration

Users can filter market data by selecting a **date range**.

The dashboard displays:

- Average Bitcoin price
- Average Oil price
- Average S&P 500 closing price
- Average NIFTY closing price

A **daily market snapshot table** combines crypto, oil, and stock data using SQL JOIN queries.

---

## 2️⃣ SQL Query Runner

This page demonstrates **SQL analytics inside Streamlit**.

Features:

- Dropdown menu with **30 predefined SQL queries**
- Run SQL queries directly from the dashboard
- Query results displayed as tables

Example queries include:

- Top cryptocurrencies by market cap
- Oil price trends
- Stock index analysis
- Bitcoin vs Oil comparison
- Cross-market joins

---

## 3️⃣ Top 3 Crypto Analysis

Users can:

- Select one cryptocurrency
- Filter by date range
- View price data

The page displays:

- Daily price table
- Optional price trend chart

---

# 🛠 Data Sources

## Cryptocurrency Data
Collected from **CoinGecko API**

Includes:

- market_cap
- market_cap_rank
- total_volume
- circulating_supply
- ATH / ATL prices

---

## Oil Prices

Historical oil price dataset covering multiple years.

---

## Stock Market Data

Collected using **Yahoo Finance API**.

Includes:

- S&P 500 (^GSPC)
- NASDAQ (^IXIC)
- NIFTY (^NSEI)

---

# 📈 SQL Analytics

The project includes **30 SQL analytical queries** for exploring financial data.

Examples:

- Average crypto price
- Highest oil price
- Stock index comparison
- Bitcoin vs stock market
- Cross-market trend analysis

---

# ⚙️ How to Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
## 📸 Dashboard Preview

### Home Dashboard
![Home Dashboard](screenshots/home_dashboard.png)

### Filters & Data Exploration
![Filters Page](screenshots/filters_page.png)

### SQL Query Runner
![SQL Query Runner](screenshots/sql_runner.png)

### Crypto Analysis
![Crypto Analysis](screenshots/crypto_analysis.png)
