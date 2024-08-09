# filename: fetch_nvda_stock_data.py

import yfinance as yf
from datetime import datetime, timedelta

# Get today's date and calculate the date one month ago
today = datetime.strptime("2024-08-04", "%Y-%m-%d")
one_month_ago = today - timedelta(days=30)

# Fetch historical data for Nvidia
nvda = yf.Ticker("NVDA")
historical_data = nvda.history(start=one_month_ago.strftime("%Y-%m-%d"), end=today.strftime("%Y-%m-%d"))

print(historical_data)