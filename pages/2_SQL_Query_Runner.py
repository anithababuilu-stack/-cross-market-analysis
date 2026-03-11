import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="SQL Query Runner", page_icon="🧠", layout="wide")
st.title("🧠 SQL Query Runner")

conn = sqlite3.connect("Market.db")

queries = {
    "Average Bitcoin Price": """
        SELECT ROUND(AVG(price_inr), 2) AS avg_bitcoin_price
        FROM crypto_prices
        WHERE coin_id = 'bitcoin'
    """,
    "Top 10 Bitcoin Prices": """
        SELECT date, price_inr
        FROM crypto_prices
        WHERE coin_id = 'bitcoin'
        ORDER BY price_inr DESC
        LIMIT 10
    """,
    "Average Oil Price by Year": """
        SELECT SUBSTR(date, 1, 4) AS year, ROUND(AVG(Price), 2) AS avg_oil_price
        FROM oil_prices
        GROUP BY year
        ORDER BY year
    """,
    "Average Close by Stock Ticker": """
        SELECT ticker, ROUND(AVG(Close), 2) AS avg_close
        FROM stock_prices
        GROUP BY ticker
    """,
    "S&P 500 vs NIFTY": """
        SELECT date, ticker, Close
        FROM stock_prices
        WHERE ticker IN ('^GSPC', '^NSEI')
        ORDER BY date
    """
}

selected_query_name = st.selectbox("Select SQL Query", list(queries.keys()))
st.code(queries[selected_query_name], language="sql")

if st.button("Run Query"):
    result_df = pd.read_sql(queries[selected_query_name], conn)
    st.subheader("Query Result")
    st.dataframe(result_df, use_container_width=True)

conn.close()
