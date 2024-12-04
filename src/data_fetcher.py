import requests
import pandas as pd
from typing import List, Dict
from forex_python.converter import CurrencyRates

class DataFetcher:
    def __init__(self):
        self.currency_converter = CurrencyRates()
        self.cryptos = ['bitcoin', 'ethereum', 'cardano', 'binancecoin', 'ripple']

    def fetch_crypto_prices(self) -> pd.DataFrame:
        """Fetch current cryptocurrency prices"""
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(self.cryptos)}&vs_currencies=usd"
            response = requests.get(url)
            prices = response.json()
            
            crypto_data = []
            for crypto in self.cryptos:
                price = prices.get(crypto, {}).get('usd', 0)
                crypto_data.append({
                    'Cryptocurrency': crypto.capitalize(), 
                    'Price (USD)': price
                })
            
            return pd.DataFrame(crypto_data)
        
        except Exception as e:
            print(f"Error fetching crypto prices: {e}")
            return pd.DataFrame()

    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert currency using forex-python"""
        try:
            return self.currency_converter.convert(from_currency, to_currency, amount)
        except Exception as e:
            print(f"Currency conversion error: {e}")
            return 0.0

    def get_supported_currencies(self) -> List[str]:
        """Return list of supported currencies"""
        return ['USD', 'BRL', 'EUR', 'GBP', 'JPY']

    def get_supported_cryptos(self) -> List[str]:
        """Return list of supported cryptocurrencies"""
        return self.cryptos