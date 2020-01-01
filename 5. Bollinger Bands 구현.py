import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from datetime import datetime
import pandas_datareader.data as wb
 
start = datetime(2018,1,1)
end = datetime(2018,12,30)
stock_data = wb.DataReader('005930.KS', 'yahoo',start,end)
stock_data['Close'].plot()
last_price = stock_data['Close']

last_price.plot()
print(stock_data)


def bollinger_band(stock_data,n = 20):
    Mov_N = stock_data['Close'].rolling(n).mean()
    Stock_Avg = stock_data['Close'].mean()
    Stock_std = stock_data['Close'].rolling(20).std()
    
    std_high_std2 = Mov_N + Stock_std * 2
    std_low_std2 = Mov_N - Stock_std * 2
    
    fig = plt.figure()
    plt.show()
    fig = plt.figure(figsize=(12,8))
    return Mov_N.plot(), std_high_std2.plot(), std_low_std2.plot()

bollinger_band(stock_data)


import pandas as pd
import matplotlib.pyplot as plt

def bb(x, w=20, k=2):
    """
    Calculate Bollinger Bands
    ubb = MA_w(x) + k * sd(x)
    mbb = MA_w(x)
    lbb = MA_w(x) - k * sd(x)
    :param x:
    :return: (ubb, mbb, lbb)
    """
    x = pd.Series(x)
    mbb = x.rolling(w).mean()
    ubb = mbb + k * x.rolling(w).std()
    lbb = mbb - k * x.rolling(w).std()
    ubb.plot(x='Date', y='UBB')
    mbb.plot(x='Date', y='MBB')
    lbb.plot(x='Date', y='LBB')
    plt.show()

bb(stock_data['Close'])
