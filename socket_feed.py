# socket_feed.py
# Narik data real-time candlestick dari Binance WebSocket

import asyncio
import websockets
import json
import pandas as pd
from datetime import datetime

candles = []  # Simpan max 100 candle terakhir

async def get_candlestick():
    uri = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
    async with websockets.connect(uri) as ws:
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            k = data['k']  # kline
            candle = {
                'time': datetime.fromtimestamp(k['t'] / 1000),
                'open': float(k['o']),
                'high': float(k['h']),
                'low': float(k['l']),
                'close': float(k['c']),
                'volume': float(k['v'])
            }
            candles.append(candle)
            if len(candles) > 100:
                candles.pop(0)

            # Simpan ke file
            df = pd.DataFrame(candles)
            df.to_csv("candles.csv", index=False)

if __name__ == "__main__":
    asyncio.run(get_candlestick())
