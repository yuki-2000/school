# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:43:18 2021

@author: yuki
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


#データ読み込み及び平均0に修正
df = pd.read_csv('j.csv', header=1)
print(df)

#print(df.iloc[5]["second"])

Vol_mean = df["Volt"].mean()
print(Vol_mean)

Vol1_mean = df["Volt.1"].mean()
print(Vol1_mean)



#平均を0にするように平行移動
#https://deepage.net/features/pandas-iteration.html
for j, i in df.iterrows():
    i["Volt.1"] = i["Volt.1"] - Vol1_mean
    i["Volt"] = i["Volt"] - Vol_mean



#グラフを書いてみる
#https://note.nkmk.me/python-pandas-plot/
df.plot()
df.plot(x="second")
df.plot(x="second", y="Volt.1")
df.plot(x="second", y="Volt")




#最大値のみ取り出す
new = pd.DataFrame()

for i in range(len(df)-2):
    if (df.loc[i]["Volt.1"] < df.loc[i+1]["Volt.1"]) and (df.loc[i+1]["Volt.1"] > df.loc[i+2]["Volt.1"]):
        #print(df.loc[i+1])
        print(df[i+1:i+2])
        new = new.append(df[i+1:i+2])




diffsec_mean=new["second"].diff().mean()
print(new["second"].diff())
print("時間差平均は"+str(diffsec_mean))
print("周波数は"+str(1/diffsec_mean))


new.plot(x="second")
new.plot.scatter(x='second', y='Volt.1', alpha=0.5)
new.to_csv("newj.csv")
