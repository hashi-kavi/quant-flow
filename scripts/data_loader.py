import yfinance as yf
import numpy as np

def get_stock_data(ticker,start_date,end_date):
    #downloads stock data and return a Numpy array of Close prices
    try:
        df = yf.download(ticker,start = start_date, end = end_date)
        if df.empty:
            print(f"Error: No data found for {ticker}")
            return None
            
        prices = df['Close'].to_numpy().flatten()
        return prices
    except Exception as e:
        print(f"An error occured: {e}")
        return None