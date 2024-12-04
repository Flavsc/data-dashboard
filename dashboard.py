import streamlit as st
import pandas as pd
import plotly.express as px
from app.data_fetcher import get_stock_data, get_crypto_data, get_financial_news

# Set page title
st.title("Real-Time Financial Dashboard")

# Section for cryptocurrency data
st.header("Cryptocurrency Data")
crypto_id = st.text_input("Enter Cryptocurrency (e.g., bitcoin, ethereum)", "bitcoin")
if crypto_id:
    try:
        crypto_data = get_crypto_data(crypto_id)
        st.write(f"Current {crypto_id.capitalize()} Price in USD: {crypto_data[crypto_id]['usd']}")
    except Exception as e:
        st.error(f"Error: {e}")

# Section for stock data
st.header("Stock Data")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", "AAPL")
period = st.selectbox("Select Data Period", ["1d", "5d", "1mo", "1y"])
interval = st.selectbox("Select Data Interval", ["1m", "5m", "1h", "1d"])

if ticker:
    try:
        stock_data = get_stock_data(ticker, period=period, interval=interval)
        st.write(stock_data)
        fig = px.line(stock_data, x=stock_data.index, y="Close", title=f"Stock Price: {ticker}")
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error: {e}")

# Section for financial news
st.header("Financial News")
api_key = st.text_input("Enter NewsAPI Key (Get it from https://newsapi.org/)", "")
if api_key:
    try:
        news = get_financial_news(api_key)
        for article in news[:5]:  # Display top 5 news articles
            st.subheader(article["title"])
            st.write(article["description"])
            st.write(f"[Read more]({article['url']})")
    except Exception as e:
        st.error(f"Error: {e}")
