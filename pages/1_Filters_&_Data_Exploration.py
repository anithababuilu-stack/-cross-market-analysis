import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Filters & Data Exploration", page_icon="📅", layout="wide")
st.title("📅 Filters & Data Exploration")

conn = sqlite3.connect("Market.db")

# Date range options
date_df = pd.read_sql("SELECT MIN(date) AS min_date, MAX(date) AS max_date FROM crypto_prices", conn)
min_date = pd.to_datetime(date_df.loc[0, "min_date"])
max_date = pd.to_datetime(date_df.loc[0, "max_date"])

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", min_date)
with col2:
    end_date = st.date_input("End Date", max_date)

# Metrics queries
bitcoin_query = f"""
SELECT ROUND(AVG(price_inr), 2) AS avg_bitcoin
FROM crypto_prices 
WHERE coin_id = 'bitcoin'
AND date BETWEEN '{start_date}' AND '{end_date}'
"""

oil_query = f"""
SELECT ROUND(AVG(Price), 2) AS avg_oil
FROM oil_prices
WHERE Date BETWEEN '{start_date}' AND '{end_date}'
"""

sp500_query = f"""
SELECT ROUND(AVG(Close), 2) AS avg_sp500
FROM stock_prices
WHERE ticker = '^GSPC'
AND Date BETWEEN '{start_date}' AND '{end_date}'
"""

nifty_query = f"""
SELECT ROUND(AVG(Close), 2) AS avg_nifty
FROM stock_prices
WHERE ticker = '^NSEI'
AND Date BETWEEN '{start_date}' AND '{end_date}'
"""

btc = pd.read_sql(bitcoin_query, conn).iloc[0, 0]
oil = pd.read_sql(oil_query, conn).iloc[0, 0]
sp500 = pd.read_sql(sp500_query, conn).iloc[0, 0]
nifty = pd.read_sql(nifty_query, conn).iloc[0, 0]

m1, m2, m3, m4 = st.columns(4)
m1.metric("Bitcoin Avg Price", btc)
m2.metric("Oil Avg Price", oil)
m3.metric("S&P 500 Avg Close", sp500)
m4.metric("NIFTY Avg Close", nifty)

st.subheader("Daily Market Snapshot")

snapshot_query = f"""
SELECT
    cp.date,
    cp.price_inr AS bitcoin_price,
    op.Price AS oil_price,
    sp.Close AS sp500_close,
    ns.Close AS nifty_close
FROM crypto_prices cp
LEFT JOIN oil_prices op
    ON cp.date = op.date
LEFT JOIN stock_prices sp
    ON cp.date = sp.date AND sp.ticker = '^GSPC'
LEFT JOIN stock_prices ns
    ON cp.date = ns.date AND ns.ticker = '^NSEI'
WHERE cp.coin_id = 'bitcoin'
AND cp.date BETWEEN '{start_date}' AND '{end_date}'
ORDER BY cp.date
"""

snapshot_df = pd.read_sql(snapshot_query, conn)
st.dataframe(snapshot_df, use_container_width=True)

conn.close()
