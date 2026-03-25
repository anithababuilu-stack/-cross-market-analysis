import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="SQL Query Runner", page_icon="🧠", layout="wide")
st.title("🧠 SQL Query Runner")

conn = sqlite3.connect("Market.db")

queries = {

# ---- CRYPTO TABLE ----
"1. Find the top 3 cryptocurrencies by market cap":
"""
SELECT id, symbol, name, market_cap
FROM Cryptocurrencies
ORDER BY market_cap DESC
LIMIT 3
""",

"2. List all coins where circulating supply exceeds 90% of total supply":
"""
SELECT id, symbol, name,circulating_supply,total_supply
FROM Cryptocurrencies
WHERE circulating_supply >= 0.9 * total_supply
""",

"3. Get coins that are within 10% of their all-time-high (ATH)":
"""
SELECT id, symbol, name,current_price,ath
FROM Cryptocurrencies
WHERE current_price >= 0.9 * ath
""",

"4. Get the most recently updated coin":
"""
SELECT id, symbol, name, date
FROM Cryptocurrencies
ORDER BY date DESC
LIMIT 1
""",

"5. Find the average market cap rank of coins with volume above $1B":
"""
SELECT AVG(market_cap_rank) AS avg_market_cap_rank
FROM Cryptocurrencies
WHERE total_volume > 1000000000
""",

# ---- CRYPTO PRICES ----
"6. Find the highest daily price of Bitcoin in the last 365 days":
"""
SELECT date, price_inr
FROM Crypto_Prices
WHERE coin_id = 'bitcoin'
ORDER BY price_inr DESC
LIMIT 1
""",

"7. .Caculate the average daily price of Ethereum in the past 1 year":
"""
SELECT AVG(price_inr) AS avg_price
FROM Crypto_Prices
WHERE coin_id = 'ethereum'
""",

"8. Show the daily price trend of Bitcoin in March 2025 ":
"""
SELECT date, price_inr
FROM Crypto_Prices
WHERE coin_id = 'bitcoin'
AND date BETWEEN '2025-03-01' AND '2025-03-31'
ORDER BY date;
""",

 "9. Find the coin with the highest average price over 1 year ":
"""
SELECT coin_id, AVG(price_inr) AS avg_price
FROM Crypto_Prices
GROUP BY coin_id
ORDER BY avg_price DESC
LIMIT 1;
""",

# ---- OIL ----
"11.Find the highest oil price in the last 5 years.":
"""
SELECT date, price
FROM Oil_prices
WHERE date BETWEEN '2021-01-01' AND '2026-01-31'
ORDER BY price DESC
LIMIT 1
""",

"12. Get the average oil price per year":
"""
SELECT strftime('%Y', date) AS year,AVG(price) AS avg_price
FROM Oil_prices
GROUP BY year
ORDER BY year
""",

"13. Show oil prices during COVID crash (March–April 2020":
"""
SELECT date, price
FROM Oil_prices
WHERE date BETWEEN '2020-03-01' AND '2020-04-30'
ORDER BY date;
""",

"14.Find the lowest price of oil in the last 10 years.":
"""
SELECT date, price
FROM Oil_prices
WHERE date BETWEEN '2016-01-01' AND '2026-01-31'
ORDER BY price ASC
LIMIT 1
""",

"15.Calculate the volatility of oil prices (max-min difference per year)":
"""
SELECT strftime('%Y', date) AS year,MAX(price) - MIN(price) AS volatility
FROM Oil_prices
GROUP BY year
""",

# ---- STOCKS ----
"16. S&P 500 Trend":
"""
SELECT Date, Close
FROM stock_prices
WHERE ticker='^GSPC'
ORDER BY Date
""",

"17. NASDAQ Trend":
"""
SELECT Date, Close
FROM stock_prices
WHERE ticker='^IXIC'
ORDER BY Date
""",

"18. NIFTY Trend":
"""
SELECT Date, Close
FROM stock_prices
WHERE ticker='^NSEI'
ORDER BY Date
""",

"19. Average Close by Index":
"""
SELECT ticker, AVG(Close)
FROM stock_prices
GROUP BY ticker
""",

"20. Highest Stock Close":
"""
SELECT ticker, MAX(Close)
FROM stock_prices
GROUP BY ticker
""",

# ---- CROSS MARKET ----
"21. Bitcoin vs Oil":
"""
SELECT cp.date, cp.price_inr, op.Price
FROM Crypto_prices cp
JOIN oil_prices op
ON cp.date = op.Date
WHERE cp.coin_id='bitcoin'
""",

"22. Bitcoin vs S&P500":
"""
SELECT cp.date, cp.price_inr, sp.Close
FROM Crypto_prices cp
JOIN stock_prices sp
ON cp.date = sp.Date
WHERE cp.coin_id='bitcoin'
AND sp.ticker='^GSPC'
""",

"23. Bitcoin vs NASDAQ":
"""
SELECT cp.date, cp.price_inr, sp.Close
FROM Crypto_prices cp
JOIN stock_prices sp
ON cp.date = sp.Date
WHERE cp.coin_id='bitcoin'
AND sp.ticker='^IXIC'
""",

"24. Bitcoin vs NIFTY":
"""
SELECT cp.date, cp.price_inr, sp.Close
FROM Crypto_prices cp
JOIN stock_prices sp
ON cp.date = sp.Date
WHERE cp.coin_id='bitcoin'
AND sp.ticker='^NSEI'
""",

"25. Oil vs S&P500":
"""
SELECT op.Date, op.Price, sp.Close
FROM oil_prices op
JOIN stock_prices sp
ON op.Date = sp.Date
WHERE sp.ticker='^GSPC'
""",

# ---- DATA ANALYSIS ----
"26. Crypto Records Count":
"SELECT COUNT(*) FROM Crypto_prices",

"27. Oil Records Count":
"SELECT COUNT(*) FROM oil_prices",

"28. Stock Records Count":
"SELECT COUNT(*) FROM stock_prices",

"29. Earliest Crypto Date":
"SELECT MIN(date) FROM Crypto_prices",

"30. Latest Crypto Date":
"SELECT MAX(date) FROM Crypto_prices"

}
selected_query_name = st.selectbox("Select SQL Query", list(queries.keys()))
st.code(queries[selected_query_name], language="sql")

if st.button("Run Query"):
    result_df = pd.read_sql(queries[selected_query_name], conn)
    st.subheader("Query Result")
    st.dataframe(result_df, use_container_width=True)

conn.close()
