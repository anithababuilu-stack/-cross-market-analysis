import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Crypto vs Stocks", page_icon="📈", layout="wide")
st.title("📈 Crypto vs Stocks Analysis")

conn = sqlite3.connect("Market.db")

st.write("This page compares average crypto prices with stock closing prices.")

# Crypto data
crypto_query = """
SELECT date, AVG(price_usd) AS crypto_price
FROM crypto_prices
GROUP BY date
"""
crypto_df = pd.read_sql(crypto_query, conn)

# Stock data
stock_query = """
SELECT date, AVG(close) AS stock_price
FROM stocks
GROUP BY date
"""
stock_df = pd.read_sql(stock_query, conn)

# Merge both
comparison_df = pd.merge(crypto_df, stock_df, on="date", how="inner")

st.subheader("Crypto vs Stocks Data")
st.dataframe(comparison_df.head())

st.subheader("Trend Comparison")
st.line_chart(comparison_df.set_index("date")[["crypto_price", "stock_price"]])

# Daily difference
comparison_df["difference"] = comparison_df["crypto_price"] - comparison_df["stock_price"]

st.subheader("Difference Between Crypto and Stocks")
st.dataframe(comparison_df[["date", "difference"]].head())

st.subheader("Difference Trend")
st.line_chart(comparison_df.set_index("date")[["difference"]])

conn.close()
