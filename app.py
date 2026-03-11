import streamlit as st

st.set_page_config(
    page_title="Cross Market Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Cross Market Analysis Dashboard")
st.subheader("Crypto, Oil & Stock Market Analysis")

st.markdown("""
This Streamlit app contains 3 main pages:

### 1. Filters & Data Exploration
- Select a date range
- View average Bitcoin, Oil, S&P 500, and NIFTY prices
- View combined daily market snapshot

### 2. SQL Query Runner
- Choose a predefined SQL query
- Run the query directly inside Streamlit
- See results in table format

### 3. Top 3 Crypto Analysis
- Choose one cryptocurrency
- Filter by date range
- View daily prices and trend
""")

st.info("Use the left sidebar to open a page.")
