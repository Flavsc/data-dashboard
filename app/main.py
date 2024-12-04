import streamlit as st
from data_fetcher import get_stock_data
from plots import plot_stock_data

# App Title
st.title("Real-Time Stock Price Dashboard")

# Sidebar for Filters
st.sidebar.header("Filters")
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")  # Default: Apple
period = st.sidebar.selectbox(
    "Select Time Period", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"]
)
interval = st.sidebar.selectbox(
    "Select Data Interval", ["1m", "2m", "5m", "15m", "1h", "1d", "1wk", "1mo"]
)

# Fetch and Display Data
if ticker:
    st.subheader(f"Stock Data for {ticker.upper()}")
    try:
        # Fetch data
        data = get_stock_data(ticker, period=period, interval=interval)
        if data.empty:
            st.warning("No data found. Please check the ticker or adjust filters.")
        else:
            # Display the raw data
            st.dataframe(data)

            # Plot the 'Close' prices
            st.subheader("Stock Price Chart")
            fig = plot_stock_data(data)
            st.plotly_chart(fig)

            # Additional Statistics
            st.subheader("Summary Statistics")
            st.write(data.describe())
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Enter a valid stock ticker symbol to view data.")
