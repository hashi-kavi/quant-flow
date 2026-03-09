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
#Relative Strength Index-how strong recent price movements are.Overbought (price may drop soon),Oversold (price may rise soon)
def calculate_rsi(prices,window = 20):
    change = np.diff(prices)
    
    #np.where(condition, value_if_true, value_if_false)
    gains = np.where(change>0,change,0)
    
    losses = np.where(change<0,-change,0)

    avg_gain = np.convolve(gains,np.ones(window)/window,mode='valid')
    avg_loss = np.convolve(losses,np.ones(window)/window,mode='valid')

    rs = avg_gain/avg_loss
    rsi = 100-(100/(1+rs))
    return rsi
#Moving Average Convergence Divergence-measures trend momentum using two exponential moving averages (EMA).

def calculate_ema(prices,window):
    alpha = 2 / (window +1)
    ema = np.zeros_like(prices)
    ema[0] = prices[0]

    for i in range(1,len(prices)):
        ema[i]= alpha*prices[i]+(1-alpha)*ema[i-1]
    return ema
def calculate_macd(prices):
    ema12 = calculate_ema(prices,12)
    ema26 = calculate_ema(prices,26)

    macd_line = ema12-ema26
    signal_line = calculate_ema(macd_line,9)
    histogram = macd_line - signal_line

    return macd_line,signal_line,histogram