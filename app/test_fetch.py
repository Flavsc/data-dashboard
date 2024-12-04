from app.data_fetcher import get_stock_data

if __name__ == "__main__":
    ticker = "AAPL"
    try:
        data = get_stock_data(ticker, period="1d", interval="1m")
        print(data.head()) 
    except Exception as e:
        print(f"An error occurred: {e}")
