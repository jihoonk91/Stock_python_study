# Stochastic(스토캐스틱)

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

def Stochastic_Oscillator(stock_data,n):
    Last_price_today = stock_data['Close']
    High_nday_price = stock_data["High"].rolling(n).max()
    Low_nday_price = stock_data["Low"].rolling(n).min()
    
    Fast_K = ((Last_price_today - Low_nday_price) * 100)/ (High_nday_price - Low_nday_price)
    Slow_K = Fast_K.rolling(5).mean()
    
    #Slow_D = Fast_K.rolling(3).mean()
    
    fig = plt.figure()
    plt.show()
    fig = plt.figure(figsize=(12,8))
    return Fast_K.plot(), Slow_K.plot(), Slow_D.plot()


Stochastic_Oscillator(stock_data,10)











