# filename: fetch_stock_data.py
import yfinance as yf
import datetime

# Calculate the date one month ago
today = datetime.datetime(2024, 8, 4)
one_month_ago = today - datetime.timedelta(days=30)

# Define the ticker symbols
nvda_ticker = 'NVDA'  # Nvidia
sp500_ticker = '^GSPC'  # S&P 500 index

# Fetch historical data from yfinance
nvda_data = yf.download(nvda_ticker, start=one_month_ago, end=today)
sp500_data = yf.download(sp500_ticker, start=one_month_ago, end=today)

# Print the data
print("Nvidia Stock Data:")
print(nvda_data)
print("\nS&P 500 Data:")
print(sp500_data)