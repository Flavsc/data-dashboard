import yfinance as yf
import pandas as pd
import requests

def get_stock_data(ticker: str, period: str = "1d", interval: str = "1m") -> pd.DataFrame:
    """
    Fetch stock price data from Yahoo Finance.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple).
        period (str): Time period for data (e.g., '1d', '5d', '1mo', '1y').
        interval (str): Data interval (e.g., '1m', '5m', '1h', '1d').

    Returns:
        pd.DataFrame: DataFrame containing stock data with date-time index.
    """
    try:
        # Adjust the interval if the period exceeds Yahoo's 1m data limit
        if period in ["1mo", "3mo", "6mo", "1y", "5y", "10y"] and interval == "1m":
            interval = "1h"  # Use hourly data for longer periods

        stock = yf.Ticker(ticker)
        data = stock.history(period=period, interval=interval)

        if data.empty:
            raise ValueError(f"No data found for ticker '{ticker}'.")
        return data
    except Exception as e:
        raise RuntimeError(f"Error fetching data for {ticker}: {e}")

def get_weather_data(city: str, api_key: str) -> dict:
    """
    Fetch real-time weather data from OpenWeatherMap.

    Args:
        city (str): Name of the city.
        api_key (str): API key for OpenWeatherMap.

    Returns:
        dict: JSON response containing weather data.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"Error fetching weather data: {response.json()}")
