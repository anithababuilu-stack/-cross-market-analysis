import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="SQL Query Runner", page_icon="🧠", layout="wide")
st.title("🧠 SQL Query Runner")

conn = sqlite3.connect("Market.db")

queries = {

# ---- CRYPTO TABLE ----
"1. List All Cryptocurrencies":
"SELECT * FROM Cryptocurrencies",

"2. Top 10 Cryptos by Market Cap":
"""
SELECT name, market_cap
FROM Cryptocurrencies
ORDER BY market_cap DESC
LIMIT 10
""",

"3. Highest ATH Crypto":
"""
SELECT name, ath
FROM Cryptocurrencies
ORDER BY ath DESC
LIMIT 10
""",

"4. Crypto with Highest Volume":
"""
SELECT name, total_volume
FROM Cryptocurrencies
ORDER BY total_volume DESC
LIMIT 10
""",

"5. Top 5 Market Cap Rank":
"""
SELECT name, market_cap_rank
FROM Cryptocurrencies
ORDER BY market_cap_rank ASC
LIMIT 5
""",

# ---- CRYPTO PRICES ----
"6. Bitcoin Price Trend":
"""
SELECT date, price_inr
FROM Crypto_prices
WHERE coin_id='bitcoin'
ORDER BY date
""",

"7. Ethereum Price Trend":
"""
SELECT date, price_inr
FROM Crypto_prices
WHERE coin_id='ethereum'
ORDER BY date
""",

"8. Average Crypto Price":
"""
SELECT coin_id, AVG(price_inr) as avg_price
FROM Crypto_prices
GROUP BY coin_id
""",

"9. Highest Crypto Price":
"""
SELECT coin_id, MAX(price_inr)
FROM Crypto_prices
GROUP BY coin_id
""",

"10. Lowest Crypto Price":
"""
SELECT coin_id, MIN(price_inr)
FROM Crypto_prices
GROUP BY coin_id
""",

# ---- OIL ----
"11. Oil Price Trend":
"""
SELECT Date, Price
FROM oil_prices
ORDER BY Date
""",

"12. Average Oil Price":
"""
SELECT AVG(Price)
FROM oil_prices
""",

"13. Highest Oil Price":
"""
SELECT MAX(Price)
FROM oil_prices
""",

"14. Oil Price by Year":
"""
SELECT SUBSTR(Date,1,4) AS year, AVG(Price)
FROM oil_prices
GROUP BY year
""",

"15. Top 10 Oil Prices":
"""
SELECT Date, Price
FROM oil_prices
ORDER BY Price DESC
LIMIT 10
""",

# ---- STOCKS ----
"16. S&P 500 Trend":
"""
SELECT Date, Close
FROM stocks_all
WHERE ticker='^GSPC'
ORDER BY Date
""",

"17. NASDAQ Trend":
"""
SELECT Date, Close
FROM stocks_all
WHERE ticker='^IXIC'
ORDER BY Date
""",

"18. NIFTY Trend":
"""
SELECT Date, Close
FROM stocks_all
WHERE ticker='^NSEI'
ORDER BY Date
""",

"19. Average Close by Index":
"""
SELECT ticker, AVG(Close)
FROM stocks_all
GROUP BY ticker
""",

"20. Highest Stock Close":
"""
SELECT ticker, MAX(Close)
FROM stocks_all
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
JOIN stocks_all sp
ON cp.date = sp.Date
WHERE cp.coin_id='bitcoin'
AND sp.ticker='^GSPC'
""",

"23. Bitcoin vs NASDAQ":
"""
SELECT cp.date, cp.price_inr, sp.Close
FROM Crypto_prices cp
JOIN stocks_all sp
ON cp.date = sp.Date
WHERE cp.coin_id='bitcoin'
AND sp.ticker='^IXIC'
""",

"24. Bitcoin vs NIFTY":
"""
SELECT cp.date, cp.price_inr, sp.Close
FROM Crypto_prices cp
JOIN stocks_all sp
ON cp.date = sp.Date
WHERE cp.coin_id='bitcoin'
AND sp.ticker='^NSEI'
""",

"25. Oil vs S&P500":
"""
SELECT op.Date, op.Price, sp.Close
FROM oil_prices op
JOIN stocks_all sp
ON op.Date = sp.Date
WHERE sp.ticker='^GSPC'
""",

# ---- DATA ANALYSIS ----
"26. Crypto Records Count":
"SELECT COUNT(*) FROM Crypto_prices",

"27. Oil Records Count":
"SELECT COUNT(*) FROM oil_prices",

"28. Stock Records Count":
"SELECT COUNT(*) FROM stocks_all",

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
