import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

class CryptoVisualizations:
    @staticmethod
    def create_crypto_bar_chart(df: pd.DataFrame):
        """Create a bar chart of cryptocurrency prices"""
        fig = px.bar(
            df, 
            x='Cryptocurrency', 
            y='Price (USD)', 
            title='Current Cryptocurrency Prices',
            labels={'Cryptocurrency': 'Cryptocurrency', 'Price (USD)': 'Price in USD'},
            color='Cryptocurrency'
        )
        return fig

    @staticmethod
    def create_line_chart(df: pd.DataFrame):
        """Create a line chart (placeholder for future historical data)"""
        fig = go.Figure()
        for crypto in df['Cryptocurrency'].unique():
            crypto_data = df[df['Cryptocurrency'] == crypto]
            fig.add_trace(go.Scatter(
                x=crypto_data.index, 
                y=crypto_data['Price (USD)'],
                mode='lines', 
                name=crypto
            ))
        return fig