# realtime_dashboard.py
# Streamlit untuk baca candlestick real-time dari file CSV

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
import os

st.set_page_config(page_title="📊 Real-time Terminal MeexKemod", layout="wide")

st.title("📈 Live Candlestick BTC/USDT")

# Loop real-time update
placeholder = st.empty()

while True:
    if os.path.exists("candles.csv"):
        df = pd.read_csv("candles.csv")
        df["time"] = pd.to_datetime(df["time"])

        fig = go.Figure(data=[go.Candlestick(
            x=df["time"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"]
        )])
        fig.update_layout(
            xaxis_rangeslider_visible=False,
            margin=dict(l=10, r=10, t=30, b=10),
            height=600
        )
        placeholder.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⏳ Menunggu data real-time dari Binance WebSocket...")

    time.sleep(5)  # update setiap 5 detik
