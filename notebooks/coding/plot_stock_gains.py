# filename: plot_stock_gains.py

import matplotlib.pyplot as plt
import yfinance as yf
import sys

# Function to download and process data
def download_stock_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        if 'Adj Close' not in data.columns:
            raise ValueError("Adjusted close price not available in the downloaded data.")
        return data['Adj Close']
    except Exception as e:
        print(f"Failed to download stock data for {symbol}: {str(e)}")
        sys.exit(1)

# Function to compute YTD gains from stock data
def compute_ytd_gains(data):
    return (data - data.iloc[0]) / data.iloc[0] * 100

# Main execution function
def main():
    start_date = '2024-02-01'
    end_date = '2024-08-04'

    # Download data
    nvda_prices = download_stock_data('NVDA', start_date, end_date)
    tsla_prices = download_stock_data('TSLA', start_date, end_date)

    # Compute YTD Gains
    nvda_gains = compute_ytd_gains(nvda_prices)
    tsla_gains = compute_ytd_gains(tsla_prices)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(nvda_gains, label='NVDA YTD Gain', color='blue')
    plt.plot(tsla_gains, label='TSLA YTD Gain', color='green')
    plt.title('YTD Stock Gains for NVDA and TSLA')
    plt.xlabel('Date')
    plt.ylabel('Percentage Gain (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig('ytd_stock_gains.png')
    plt.show()

if __name__ == '__main__':
    main()