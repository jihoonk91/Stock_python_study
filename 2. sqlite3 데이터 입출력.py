
from datetime import datetime
import pandas_datareader.data as wb
 
start = datetime(2018,11,1)
end = datetime(2018,11,30)
 
df = wb.DataReader('005930.KS', 'yahoo',start,end)


import sqlite3 as sq

if __name__ == '__main__':

    ### DB 연결
    conn = sq.connect("testPython.db")
    cur = conn.cursor() 
    

import sqlite3 as sq
import pandas.io.sql as pd_sql
from pandas import DataFrame
# from subDS import subStockChart # 위에 작성한 subStockChart 불러오기

if __name__ == "__main__":
    ### DB 연결
    conn = sq.connect("testPython.db")
    cur = conn.cursor()
    ### 자료가져오기
    code ='A005930' # 삼성전자 종목코드
    numHist =100 # 과거 100일치 데이터
    df1 = wb.DataReader('005930.KS', 'yahoo',start,end)
    print(df)
    tableName = 'table_samsung2'
    pd_sql.to_sql(df1, tableName, conn, if_exists='append', index=True)
    conn.close()
    
import pandas as pd
if __name__ == "__main__":
    ### DB 연결
    conn = sq.connect("testPython.db")
    cur = conn.cursor()
    ### 자료가져오기
    df.to_sql('005930', conn, if_exists='replace')
    readed_df = pd.read_sql("SELECT * FROM 'table_samsung'", conn, index_col = 'Date')
    print(readed_df)

df1 = wb.DataReader('005930.KS', 'yahoo',start,end)    
newDf = pd.merge(df, df1, on='Date', how='outer')
print(newDf)


sql ="DELETE FROM " + tableName +" WHERE rowid NOT IN  (SELECT Max(rowid) FROM " + tableName +" GROUP BY date order by date)"
pd_sql.execute(sql, con)
con.execute("VACUUM")



