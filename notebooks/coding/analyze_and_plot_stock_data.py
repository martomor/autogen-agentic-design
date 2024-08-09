# filename: analyze_and_plot_stock_data.py
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import datetime

# Dates
today = datetime.datetime(2024, 8, 4)
one_month_ago = today - datetime.timedelta(days=30)

# Downloading the stock data
nvda_data = yf.download('NVDA', start=one_month_ago, end=today)
sp500_data = yf.download('^GSPC', start=one_month_ago, end=today)

# Calculate percentage changes
nvda_data['Pct Change'] = nvda_data['Adj Close'].pct_change()
sp500_data['Pct Change'] = sp500_data['Adj Close'].pct_change()

# Plotting the closing prices
plt.figure(figsize=(14, 7))
plt.plot(nvda_data['Adj Close'], label='Nvidia')
plt.plot(sp500_data['Adj Close'], label='S&P 500')
plt.title('Nvidia vs S&P 500 - Last Month')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.show()

# Statistical Summary
print("\nNvidia's Statistical Summary:")
print(nvda_data['Adj Close'].describe())

print("\nS&P 500's Statistical Summary:")
print(sp500_data['Adj Close'].describe())