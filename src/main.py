import streamlit as st
import pandas as pd
from data_fetcher import DataFetcher
from visualizations import CryptoVisualizations

class CryptoDashboard:
    def __init__(self):
        self.data_fetcher = DataFetcher()
        self.visualizations = CryptoVisualizations()
        self._setup_page()

    def _setup_page(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="Crypto Dashboard", 
            page_icon="💰", 
            layout="wide"
        )

    def run(self):
        """Main dashboard application"""
        st.title("💰 Cryptocurrency and Currency Dashboard")
        
        # Sidebar navigation
        menu = ["Currency Conversion", "Crypto Prices", "Currency Rates"]
        choice = st.sidebar.selectbox("Navigation", menu)
        
        # Fetch crypto prices
        crypto_df = self.data_fetcher.fetch_crypto_prices()
        
        if choice == "Currency Conversion":
            self._currency_conversion_page()
        elif choice == "Crypto Prices":
            self._crypto_prices_page(crypto_df)
        else:
            self._currency_rates_page()

    def _currency_conversion_page(self):
        """Currency conversion interface"""
        st.header("💱 Currency Converter")
        
        col1, col2 = st.columns(2)
        
        with col1:
            from_currency = st.selectbox(
                "Source Currency", 
                self.data_fetcher.get_supported_currencies()
            )
            amount = st.number_input("Amount to Convert", min_value=1.0, value=100.0)
        
        with col2:
            to_currency = st.selectbox(
                "Target Currency", 
                self.data_fetcher.get_supported_currencies()
            )
        
        # Perform conversion
        converted_amount = self.data_fetcher.convert_currency(
            amount, from_currency, to_currency
        )
        
        st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    def _crypto_prices_page(self, crypto_df):
        """Cryptocurrency prices visualization page"""
        st.header("📊 Cryptocurrency Prices")
        
        # Bar chart of crypto prices
        fig = self.visualizations.create_crypto_bar_chart(crypto_df)
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed price table
        st.dataframe(crypto_df.style.highlight_max(axis=0))

    def _currency_rates_page(self):
        """Currency exchange rates page"""
        st.header("💹 Current Exchange Rates")
        
        base_currency = st.selectbox(
            "Base Currency", 
            self.data_fetcher.get_supported_currencies()
        )
        
        rates_data = []
        for currency in self.data_fetcher.get_supported_currencies():
            if currency != base_currency:
                rate = self.data_fetcher.convert_currency(1, base_currency, currency)
                rates_data.append({
                    'Currency': currency, 
                    'Rate': rate
                })
        
        rates_df = pd.DataFrame(rates_data)
        st.dataframe(rates_df)

def main():
    dashboard = CryptoDashboard()
    dashboard.run()

if __name__ == "__main__":
    main()