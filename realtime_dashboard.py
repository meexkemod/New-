# realtime_dashboard.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
import requests

st.set_page_config(page_title="📊 Real-time Terminal MeexKemod", layout="wide")
st.title("📈 Live Candlestick BTC/USDT")

placeholder = st.empty()

API_URL = "https://21db6963-dcd8-4b48-8f98-be314770a418-00-1747jbty2r5ej.pike.replit.dev/candles"

while True:
    try:
        response = requests.get(API_URL)
        data = response.json()
        df = pd.DataFrame(data)
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
    except Exception as e:
        st.warning(f"⏳ Menunggu data real-time... ({e})")

    time.sleep(5)
