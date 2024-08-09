# filename: fetch_nvidia_stock_data.py
import yfinance as yf
import pandas as pd

# Define the ticker symbol for Nvidia
nvidia_ticker = 'NVDA'

# Set the date range for the past month
start_date = '2024-07-04'
end_date = '2024-08-04'

# Fetch the historical data from Yahoo Finance
data = yf.download(nvidia_ticker, start=start_date, end=end_date)

# Check if the data frame is not empty and print the tail to verify the download
if not data.empty:
    print(data.tail())  # Show the last few rows of the data
else:
    print("No data retrieved. Please check the ticker symbol and date range.")