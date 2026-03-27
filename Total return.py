import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.font_manager import fontManager
from datetime import datetime

import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = 'Taipei Sans TC Beta'
plt.rcParams["axes.unicode_minus"] = False

#調整曲線圖尺寸
fig = plt.figure(figsize = (10,5))
data = pd.read_csv('')
data.set_index(pd.to_datetime(data['Date'],format='%Y/%m/%d'),inplace=True)

## 定期定額
PMT=3000
start='2017-3-31'
end='2020-8-31'
take_profit=0.1
df= data.copy()
dfm=df.resample('BM').last()
dfm=dfm.loc[start:end]

total_cost_list=[PMT]
unit_list=[PMT/dfm['price'].iloc[0]]
pre_NAV_list=[0]
TR_check_list=[0]

for i,price in enumerate(dfm['price'].iloc[1:]):
    total_cost=total_cost_list[i]+PMT
    unit=unit_list[i]+(PMT/price)
    pre_NAV=unit_list[i]*price
    TR=pre_NAV/total_cost_list[i]-1

    total_cost_list.append(total_cost)
    unit_list.append(unit)
    pre_NAV_list.append(preNAV)
    TR_check_list.append(TR_check)

dfm['total_cost']=total_cost_list
dfm['unit']=unit_list
dfm['pre_NAV']=pre_NAV_list
dfm['TR_check']=TR_check_list

dfm.head(50)
#dfm['total_return(%)']=(dfm['pre_NAV']/(dfm['total_cost']-PMT)-1)*100
"""
#設定Y軸
y1=dfm['total_return(%)'] #定期定額
y2=dfm['price']         #股價
y3=tr                    #單筆

#設定X軸
#要設成日期格式,日期區間設定才會生效
#x = pd.to_datetime(x)
x = dfm.index

#font1 = font(fname='C:\Python\Python38\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\NotoSansSC-Bold.otf')
ax1 = fig.add_subplot()
plt.title('(第一金工業30)『定期定額 && 單筆投資』v.s.股價',fontsize=20,color="brown")
plt.xlabel('日期',fontsize=15)

# one line for 定期定額
color1 = 'red'
ax1.set_ylabel('報酬',fontsize=15,color="red")
line1 = ax1.plot(x,y1, color = color1, label = '報酬')
ax1.tick_params(axis = 'y', labelcolor = color1)
#ax1.set_ylim(1.2*y1.min(),1.2*y1.max())


# two line for 股價
ax2 = ax1.twinx()

color2 = 'blue'
ax2.set_ylabel('股價',fontsize=15,color="blue")
line2 = ax2.plot(x,y2, color = color2, label = '股價')
#line2 = ax2.plot(ETF1_std['Price'], color = color2, label = '股價')
ax2.tick_params(axis = 'y', labelcolor = color2)
ax2.set_ylim(0.9*y2.min(), 1.1*y2.max())
ax2.legend(["股價"],fontsize=15,loc="upper center")

# one line for 單筆投資(與ax1共用x,y軸)
color3 = 'green'
line3 = ax1.plot(x,y3, color = color3)

ax1.legend(["定期定額","單筆投資"],fontsize=15,loc="upper left")

#設定x軸主刻度顯示格式（日期）
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
#設定x軸主刻度間距
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6)) 

#ax1.tick_params(axis = 'y', labelcolor = color3)
#ax1.set_ylim(1.2*y1.min(),1.2*y1.max())
#ax1.legend(["定期定額"],fontsize=15,loc="upper left")

plt.show()

