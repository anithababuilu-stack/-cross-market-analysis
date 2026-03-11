import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Top 5 Crypto Analysis", page_icon="🪙", layout="wide")
st.title("🪙 Top 5 Crypto Analysis")

conn = sqlite3.connect("Market.db")

# Get top 5 coins from your data
coins_df = pd.read_sql("""
    SELECT DISTINCT coin_id
    FROM crypto_prices
    LIMIT 5
""", conn)

coin_list = coins_df["coin_id"].tolist()

selected_coin = st.selectbox("Select Cryptocurrency", coin_list)

date_df = pd.read_sql(f"""
    SELECT MIN(date) AS min_date, MAX(date) AS max_date
    FROM crypto_prices
    WHERE coin_id = '{selected_coin}'
""", conn)

min_date = pd.to_datetime(date_df.loc[0, "min_date"])
max_date = pd.to_datetime(date_df.loc[0, "max_date"])

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", min_date, key="crypto_start")
with col2:
    end_date = st.date_input("End Date", max_date, key="crypto_end")

crypto_query = f"""
SELECT date, price_inr
FROM crypto_prices
WHERE coin_id = '{selected_coin}'
AND date BETWEEN '{start_date}' AND '{end_date}'
ORDER BY date
"""

crypto_df = pd.read_sql(crypto_query, conn)

st.subheader(f"{selected_coin.title()} Daily Price Table")
st.dataframe(crypto_df, use_container_width=True)

st.subheader(f"{selected_coin.title()} Daily Price Trend")
if not crypto_df.empty:
    chart_df = crypto_df.copy()
    chart_df["date"] = pd.to_datetime(chart_df["date"])
    chart_df = chart_df.set_index("date")
    st.line_chart(chart_df["price_inr"])
else:
    st.warning("No data found for selected date range.")

conn.close()
