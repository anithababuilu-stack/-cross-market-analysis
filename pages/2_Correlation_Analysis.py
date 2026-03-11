import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Correlation Analysis", page_icon="📊", layout="wide")
st.title("📊 Correlation Analysis")

conn = sqlite3.connect("Market.db")

st.write("This page shows correlation between crypto, oil, and stock markets.")

# Load crypto data
crypto_query = """
SELECT date, AVG(price_inr) AS crypto_price
FROM crypto_prices
GROUP BY date
"""
crypto_df = pd.read_sql(crypto_query, conn)

# Load oil data
oil_query = """
SELECT date, AVG(price) AS oil_price
FROM oil_prices
GROUP BY date
"""
oil_df = pd.read_sql(oil_query, conn)

# Load stock data
stock_query = """
SELECT date, AVG(close) AS stock_price
FROM stocks
GROUP BY date
"""
stock_df = pd.read_sql(stock_query, conn)

# Merge data
merged_df = crypto_df.merge(oil_df, on="date", how="inner")
merged_df = merged_df.merge(stock_df, on="date", how="inner")

st.subheader("Merged Market Data")
st.dataframe(merged_df.head())

# Correlation
corr_df = merged_df[["crypto_price", "oil_price", "stock_price"]].corr()

st.subheader("Correlation Matrix")
st.dataframe(corr_df)

st.subheader("Price Trends Comparison")
st.line_chart(merged_df.set_index("date")[["crypto_price", "oil_price", "stock_price"]])

conn.close()
