import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def calculate_bollinger_bands(prices,window_size=20,num_std = 2):
    """
    calculate Bollinger bands usinng vectorized Numpy operations

    Parameters:

    prices: np.ndarray(Array of closing prices)
    window_size: int(Rolling window size)
    num_std : int(Number of standard deviations)

    returns
    upper_band,sma,lower_band: np.ndarray

    """

    #1.create sliding window view
    # this turns arrayy into 20 windows ,ex:window 3 ,[1,2,3,4,5] =[[1,2,3], [2,3,4], [3,4,5]]
    windows = sliding_window_view(prices,window_size)

    #2.calculate mean and std dev for each window(row)
    #axis = 1 means "calculate across the row"
    #sma - simple moving average
    sma = np.mean(windows,axis=1)
    std = np.std(windows,axis=1)

    # calculate the Bands

    upper_band = sma + (std * num_std)
    lower_band = sma - (std * num_std)

    return upper_band, sma,lower_band
# Because the function returns three values (upper_band, sma, lower_band), Python packs them into a tuple and we can assign them to three variables using tuple unpacking.
def calculate_daily_return(prices):
    """calculates the percentages between each day
          formula: (Price_t - price_t-1)/price_t-1
    """
    # np.diff(prices) gives prices[1:]-prices[:-1]
    returns = np.diff(prices)/prices[:-1]
    # Example: [100, 110, 121] → [10/100, 11/110] → [0.10, 0.10]
    return returns * 100
