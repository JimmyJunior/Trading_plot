import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf
from matplotlib.font_manager import fontManager
from datetime import datetime

plt.rcParams['font.sans-serif'] = 'Taipei Sans TC Beta'
plt.rcParams["axes.unicode_minus"] = False

Stocks = ['00690.tw','00728.tw','0050.tw','2330.tw','2303.tw']
#'00690.tw'(兆豐藍籌30),'00728.tw'(第一金工業30),'0050.tw'(元大台灣50),'2330.tw'(台積電),'2303.tw'(聯電)]
def MDD(D):
	df = yf.Ticker(D)
	#print(df.history().columns)
	#print(df.history().Close)
	dr = df.history().Close.pct_change(1)
	r = dr.add(1).cumprod() #return 連乘
	dd = r.div(r.cummax()).sub(1) #drawdown 1+r/1+R
	mdd = dd.min() #Maxdrwdown
	end = dd.idxmin()
	print(r)
	#print(r.loc[0].idxmax())
	#print(r.loc[1].idxmax())
	start = r.idxmax() #最高點
	#start = r.loc[:end[0]].idxmax() 
	#print(start)
	days = end - start
	#print(days)
	return [mdd, start, end, days]

color1=['b','orange','g','r','m']
color2=['r','yellow','black','b','orange']

ax1 = plt.figure(figsize = (10,5)).add_subplot()
plt.title('『Max Drawdown』 vs 『持續天數』 ',fontsize=18,color="r")
plt.xlabel('股價名稱',fontsize=15)
ax2 = ax1.twinx()

days_period=[294,291,281,281,395]
max_drawdown=[31.46,43.34,36.38,45.68,49.5]
#x_axis=np.arange(len(Stocks))
for i in range(5):
	bar1=ax1.bar(Stocks, max_drawdown,color=color1,width=0.4, align='edge',label='Maxdrwdown')
	bar2=ax2.bar(Stocks, days_period,color=color1,width=0.4, align='edge',label='Days')
	
plt.show()