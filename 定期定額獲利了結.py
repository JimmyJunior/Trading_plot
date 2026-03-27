import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.font_manager import fontManager
from datetime import datetime

import pandas as pd
import numpy as np


fig = plt.figure(figsize = (10,5))
data = pd.read_csv('00690.csv')
data.set_index(pd.to_datetime(data['Date'],format='%Y/%m/%d'),inplace=True)

## �????�?�?
PMT=3000
start='2017-3-31'
end='2020-8-31'
take_profit=0.1
df= data.copy()
dfm=df.resample('BM').last()
dfm=dfm.loc[start:end]
#dfm
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
    pre_NAV_list.append(pre_NAV)
    #TR_check_list.append(TR_check)

dfm['total_cost']=total_cost_list
dfm['unit']=unit_list
#dfm['pre_NAV']=pre_NAV_list
#dfm['TR_check']=TR_check_list

dfm.head(50)
#dfm['total_return(%)']=(dfm['pre_NAV']/(dfm['total_cost']-PMT)-1)*100
