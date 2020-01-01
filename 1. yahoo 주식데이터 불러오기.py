# pip install yahoo-finance

from datetime import datetime
import pandas_datareader.data as wb
 
start = datetime(2018,11,1)
end = datetime(2018,11,30)
 
df = wb.DataReader('005930.KS', 'yahoo',start,end)

print(df)


df['Close'].plot()

