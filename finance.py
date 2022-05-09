import sys 
sys.executable
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start=dt.datetime(2020,1,1)
end=dt.datetime(2022,4,1)

df=web.DataReader('TSLA', 'yahoo', start, end)
df=pd.read_csv('TSLA',parse_dates=True, index_col=0)
print(df[['Open','High']].head)
df['Adj Close'].plot()#orange
df['Open'].plot()#blue
plt.show()
