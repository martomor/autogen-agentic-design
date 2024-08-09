# filename: visualize_nvda_sp500_comparison.py

import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

# Set the time period
today = datetime.strptime("2024-08-04", "%Y-%m-%d")
one_month_ago = today - timedelta(days=30)

# Fetch historical data for Nvidia and S&P 500
nvda = yf.Ticker("NVDA")
sp500 = yf.Ticker("^GSPC")

nvda_data = nvda.history(start=one_month_ago.strftime("%Y-%m-%d"), end=today.strftime("%Y-%m-%d"))['Close']
sp500_data = sp500.history(start=one_month_ago.strftime("%Y-%m-%d"), end=today.strftime("%Y-%m-%d"))['Close']

# Calculate daily percentage changes
nvda_changes = nvda_data.pct_change()*100
sp500_changes = sp500_data.pct_change()*100

# Combine the data into a DataFrame and drop the first NaN values
comparison_data = pd.DataFrame({'NVDA': nvda_changes, 'S&P 500': sp500_changes}).dropna()

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(comparison_data.index, comparison_data['NVDA'], label='Nvidia', color='blue')
plt.plot(comparison_data.index, comparison_data['S&P 500'], label='S&P 500', color='red')
plt.title('Daily Percentage Change: Nvidia vs S&P 500 Over the Last Month')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()