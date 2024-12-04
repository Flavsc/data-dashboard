import yfinance as yf
import pandas as pd
from pycoingecko import CoinGeckoAPI
import requests
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_stock_data(ticker: str, period: str = "1d", interval: str = "1m") -> pd.DataFrame:
    """
    Fetch stock price data from Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL' for Apple).
        period (str): Period of data (e.g., '1d', '1mo', '1y').
        interval (str): Interval of data (e.g., '1m', '5m', '1h').

    Returns:
        pd.DataFrame: DataFrame containing stock price data.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period, interval=interval)
        if data.empty:
            raise ValueError(f"No data found for ticker '{ticker}'.")
        return data
    except Exception as e:
        raise RuntimeError(f"Error fetching data for {ticker}: {e}")


def get_crypto_data(crypto_id: str) -> dict:
    """
    Fetch cryptocurrency data from CoinGecko.

    Args:
        crypto_id (str): Cryptocurrency id (e.g., 'bitcoin' or 'ethereum').

    Returns:
        dict: Dictionary containing cryptocurrency data.
    """
    try:
        cg = CoinGeckoAPI()
        data = cg.get_price(ids=crypto_id, vs_currencies='usd')
        if not data:
            raise ValueError(f"No data found for cryptocurrency '{crypto_id}'.")
        return data
    except Exception as e:
        raise RuntimeError(f"Error fetching cryptocurrency data for {crypto_id}: {e}")


def get_financial_news(api_key: str) -> list:
    """
    Fetch the latest financial news from NewsAPI.

    Args:
        api_key (str): NewsAPI API key.

    Returns:
        list: List of news articles.
    """
    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        news = response.json().get("articles", [])
        return news
    else:
        raise RuntimeError(f"Error fetching financial news: {response.json()}")
