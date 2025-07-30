import time
import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame

# === CONFIGURATION ===
API_KEY = 'PKZ40F87LMZ0SRE16MRD'
API_SECRET = 'ofkfqh8zB8JC3mz21oNAVHuVbsmfuPKxL8yUah7L'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use for testing; switch to live URL when ready

STOCK_SYMBOL = 'AAPL'
SHORT_WINDOW = 20  # Short SMA
LONG_WINDOW = 50   # Long SMA
TRADE_QUANTITY = 1

# === INIT ALPACA API ===
api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def get_sma_data(symbol, short_window, long_window):
    barset = api.get_bars(symbol, TimeFrame.Day, limit=long_window + 1).df
    df = barset[barset['symbol'] == symbol]
    df['sma_short'] = df['close'].rolling(window=short_window).mean()
    df['sma_long'] = df['close'].rolling(window=long_window).mean()
    return df

def check_position(symbol):
    try:
        position = api.get_position(symbol)
        return int(position.qty)
    except:
        return 0

def trade_logic():
    df = get_sma_data(STOCK_SYMBOL, SHORT_WINDOW, LONG_WINDOW)
    latest = df.iloc[-1]

    position = check_position(STOCK_SYMBOL)
    print(f"[INFO] Current Position: {position} shares")

    if latest['sma_short'] > latest['sma_long'] and position == 0:
        print("[BUY SIGNAL] Placing market buy order...")
        api.submit_order(symbol=STOCK_SYMBOL, qty=TRADE_QUANTITY, side='buy', type='market', time_in_force='gtc')

    elif latest['sma_short'] < latest['sma_long'] and position > 0:
        print("[SELL SIGNAL] Placing market sell order...")
        api.submit_order(symbol=STOCK_SYMBOL, qty=TRADE_QUANTITY, side='sell', type='market', time_in_force='gtc')
    else:
        print("[HOLD] No trade signal today.")

# === MAIN LOOP (once per day) ===
if __name__ == '__main__':
    while True:
        print("\n[Running strategy check]")
        trade_logic()
        time.sleep(60)  # Wait 1 day (use smaller interval for testing)
