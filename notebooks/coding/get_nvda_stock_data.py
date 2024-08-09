# filename: get_nvda_stock_data.py
import pandas_datareader as pdr
from datetime import datetime

# Define the time period
start_date = datetime(2024, 7, 4)
end_date = datetime(2024, 8, 4)

# Get data from Yahoo Finance
nvidia_stock_data = pdr.get_data_yahoo('NVDA', start=start_date, end=end_date)
print(nvidia_stock_data)