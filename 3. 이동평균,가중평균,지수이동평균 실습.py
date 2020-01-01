import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas_datareader.data as wb
 
start = datetime(2018,1,1)
end = datetime(2018,12,30)
 
stock_data = wb.DataReader('005930.KS', 'yahoo',start,end)


stock_data['Close'].plot()


last_price = stock_data['Close']


## 단순이동평균
mov5 = last_price.rolling(5).mean()
mov20 = last_price.rolling(20).mean()

mov5.plot()
mov20.plot()


## 선형가중 이동평균 구하기
def weightedMean(weightArray):
    def inner(x):
        return (weightArray * x).mean()
    return inner


n = 5
t = [v for v in np.arange(1, n+1)]
print(t)
sumv = sum(t) / n
print(sumv)
wts = np.array(t) / sumv
print(wts)

wMov5 = last_price.rolling(n).apply(weightedMean(wts), raw=True)
wMov5.plot()


##지수이동평균 구하기
eMov5 = last_price.ewm(span=5).mean()
eMov20 = last_price.ewm(span=20).mean()

print(eMov5)
print(eMov20)


## 단순이동평균, 선형가중평균, 지수이동평균 비교
fig = plt.figure()
plt.show()
fig = plt.figure(figsize=(12,8))
last_price.plot()
mov5.plot()
wMov5.plot()
eMov5.plot()









