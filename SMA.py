import yfinance as yf
import pandas as pd
import subprocess
import datetime

def calculate_sma_signals(symbol, start_date, end_date, short_sma_period, long_sma_period):
    data = yf.download(symbol, start=start_date, end=end_date)
    data['Short_SMA'] = data['Close'].rolling(window=short_sma_period).mean()
    data['Long_SMA'] = data['Close'].rolling(window=long_sma_period).mean()

    position = None
    signals = []

    for i in range(len(data)):
        if data['Short_SMA'][i] > data['Long_SMA'][i]:
            if position != 'Buy':
                signals.append(('Buy', data.index[i], data['Close'][i]))
                position = 'Buy'
        elif data['Short_SMA'][i] < data['Long_SMA'][i]:
            if position != 'Sell':
                signals.append(('Sell', data.index[i], data['Close'][i]))
                position = 'Sell'

    return pd.DataFrame(signals, columns=['Action', 'Date', 'Price'])

def send_notification(title, message):
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])

def execute_sma_strategy():
    symbol = "AAPL"
    start_date = datetime.date.today() - datetime.timedelta(days=365)
    end_date = datetime.date.today()
    short_sma_period = 50
    long_sma_period = 200

    signals_df = calculate_sma_signals(symbol, start_date, end_date, short_sma_period, long_sma_period)

    for _, row in signals_df.iterrows():
        if row['Action'] == 'Buy':
            send_notification("Buy Signal", f"Buy at {row['Price']} on {row['Date']}")
        elif row['Action'] == 'Sell':
            send_notification("Sell Signal", f"Sell at {row['Price']} on {row['Date']}")

if __name__ == "__main__":
    execute_sma_strategy()
