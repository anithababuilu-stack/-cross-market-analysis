import streamlit as st

st.set_page_config(
    page_title="Cross Market Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Cross Market Analysis Dashboard")
st.subheader("Crypto, Oil & Stocks")

st.write("""
Welcome to the Cross Market Analysis project.

Use the sidebar to explore:
- Market Overview
- Crypto Analysis
- Stock Analysis
- Oil Analysis
- Cross Market Comparison
""")

st.info("Select a page from the left sidebar.")
