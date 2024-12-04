import plotly.graph_objs as go

def plot_stock_data(data):
    """
    Generate a Plotly line chart for stock prices.

    Args:
        data (pd.DataFrame): DataFrame containing stock data.

    Returns:
        go.Figure: Plotly figure object.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Close Price"))
    fig.update_layout(
        title="Stock Price Over Time",
        xaxis_title="Time",
        yaxis_title="Price (USD)",
        template="plotly_dark",
    )
    return fig

import plotly.graph_objs as go

def plot_candlestick(data):
    """
    Generate a candlestick chart using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing stock data.

    Returns:
        go.Figure: Plotly candlestick figure.
    """
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick'
    )])
    fig.update_layout(
        title="Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark"
    )
    return fig
