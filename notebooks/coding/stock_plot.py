# filename: stock_plot.py
from functions import get_stock_prices, plot_stock_prices
import pandas as pd
import matplotlib.pyplot as plt

# Calculating dates
end_date = "2024-08-04"
start_date = pd.to_datetime(end_date) - pd.DateOffset(months=6)
start_date = str(start_date.date())  # Convert to string in Y-M-D format

# Retrieve stock prices
stock_symbols = ['NVDA', 'TSLA']
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Normalize stock prices by the first price to show gain YTD
normalized_stock_prices = stock_prices / stock_prices.iloc[0]

# Instantiate plot
plt.figure(figsize=(10, 5))
plt.plot(normalized_stock_prices, label=normalized_stock_prices.columns)
plt.title('Six Month Stock Gain YTD for NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('Normalized Price (First Day = 1)')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('stock_prices_YTD.png')
plt.show()