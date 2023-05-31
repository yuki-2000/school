
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:43:18 2021

@author: yuki
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math







def make_ave0(df):

    Vol_mean = df["Volt"].mean()
    print(Vol_mean)
    
    Vol1_mean = df["Volt.1"].mean()
    print(Vol1_mean)
    
    
    #平均を0にするように平行移動
    #https://deepage.net/features/pandas-iteration.html
    for j, i in df.iterrows():
        i["Volt.1"] = i["Volt.1"] - Vol1_mean
        i["Volt"] = i["Volt"] - Vol_mean

    return df


def make_value_small(df, gain):

    Vol_mean = df["Volt"].mean()
    print(Vol_mean)
    
    for j, i in df.iterrows():
        i["Volt"] = i["Volt"] *gain

    return df



def make_mv_ave(df, fre, in_colname, out_colname):
    sample= int(1000//(fre*2*0.25))
    if sample % 2 == 0:
        sample+=1
        sample = int(sample)
    
    
    """
    for i in range(int((sample-1)/2) , int(len(df)-(sample-1)/2)):
        df.iloc[i,3]=i
    """  
        
    #https://note.nkmk.me/python-pandas-rolling/
    print(type(df[in_colname].rolling(sample,center=True).mean()))
    #https://note.nkmk.me/python-pandas-assign-append/
    df[out_colname]=df[in_colname].rolling(sample,center=True).mean()

    return df



def find_01(df, in_label, out_label):
    new01in = pd.DataFrame()
    new01out = pd.DataFrame()
    for i in range(len(df)-1):
        if (df.loc[i][in_label] <= 0) and (df.loc[i+1][in_label] > 0):
            #print(df.loc[i+1])
            print(df[i:i+1][in_label])
            new01in = pd.concat([new01in, df[i:i+1]["second"]])
            
            
        if (df.loc[i][out_label] <= 0) and (df.loc[i+1][out_label] > 0):
          #print(df.loc[i+1])
          print(df[i:i+1][out_label])
          new01out = pd.concat([new01out, df[i:i+1]["second"]])
          
    #new01in = new01in.rename(columns={0: in_label})
    #new01out = new01out.rename(columns={0: out_label})       
    print(new01in)
    print(pd.concat([new01in, new01out], axis=1, ignore_index=False))
    new01 = pd.concat([new01in, new01out], axis=0, ignore_index=False)
    new01 = new01.sort_index()
    new01 = new01.rename(columns={0: "second"})
    print(new01)
    #new01.plot.line(x='second', style=['ro', 'g+', 'bs'], alpha=0.5)
    #ax = new01.plot.scatter(x='second', y=in_label, alpha=0.5)
    #new01.plot.scatter(x='index', y="0", alpha=0.5)
    #new01.plot.scatter()
    print(new01.diff())
    
    
    test = list(new01.diff()["second"])
    sec_sum=0
    num=0
    if len(test)<3:
        sec = test[1]
    elif test[1]<test[2]:
        for i in range(1,len(test), 2):
            sec_sum+=test[i]
            num+=1
        sec = sec_sum/num
    elif test[1]>test[2]:
        for i in range(2,len(test), 2):
            sec_sum+=test[i]
            num+=1
        sec = sec_sum/num
    
    
    
    
    return sec




def get_max_min(df, in_label, out_label):
    

    #入力volt
    max0=df[in_label].max()
    print(max0)
    min0=df[in_label].min()
    print(min0)
    amp0=max0-min0
    print(amp0)
    
    #出力volt
    max1=df[out_label].max()
    print(max1)
    min1=df[out_label].min()
    print(min1)
    amp1=max1-min1
    print(amp1)
    
    
    print("ゲイン"+str(abs(amp1/amp0)))    






"""
#最大値のみ取り出す
maxnew = pd.DataFrame()
#最小値のみ取り出す
minnew = pd.DataFrame()

label = "in_mv_ave"

for i in range(len(df)-2):
    if (df.loc[i][label] < df.loc[i+1][label]) and (df.loc[i+1][label] > df.loc[i+2][label]):
        #print(df.loc[i+1])
        print(df[i+1:i+2])
        maxnew = maxnew.append(df[i+1:i+2])

    if (df.loc[i][label] > df.loc[i+1][label]) and (df.loc[i+1][label] < df.loc[i+2][label]):
        #print(df.loc[i+1])
        print(df[i+1:i+2])
        minnew = minnew.append(df[i+1:i+2])


maxnew.plot.scatter(x='second', y=label, alpha=0.5)
minnew.plot.scatter(x='second', y=label, alpha=0.5)

"""


#データ読み込み及び平均0に修正
df = pd.read_csv('./20211028/d20.csv', header=1)
print(df)
fre = 20

#difsec=[0.02250, 0.02375, 0.02300]
#sec = sum(difsec)/len(difsec)
#print(df.iloc[5]["second"])
make_ave0(df)

#追加　入力が大きすぎて振幅比べられないよう
make_value_small(df, 0.01)

#グラフを書いてみる
#https://note.nkmk.me/python-pandas-plot/
df.plot()
df.plot(x="second")
df.plot(x="second", y="Volt.1")
df.plot(x="second", y="Volt")


#移動平均をとる
df = make_mv_ave(df, fre, "Volt", "in_mv_ave")
df = make_mv_ave(df, fre, "Volt.1", "out_mv_ave")


df.plot()
df.plot(x="second", y=["Volt", "in_mv_ave"])
df.plot(x="second", y=["Volt.1", "out_mv_ave"])
df.plot(x="second")


print("-------------------")


#df.to_csv("newkdafa.csv")

sec = find_01(df, in_label="in_mv_ave", out_label="out_mv_ave")


  

print("---------------------")
get_max_min(df, in_label="in_mv_ave", out_label="out_mv_ave")
print("位相遅れ" + str((sec/(1/fre))*360))
print("もしくは相遅れ" + str(360-((sec/(1/fre))*360)))



"""
#入力volt
diffsec_mean=new["second"].diff().mean()
print(new["second"].diff())
print("時間差平均は"+str(diffsec_mean))
print("周波数は"+str(1/diffsec_mean))


#出力volt.1
diffsec_mean=new["second"].diff().mean()
print(new["second"].diff())
print("時間差平均は"+str(diffsec_mean))
print("周波数は"+str(1/diffsec_mean))


new.plot(x="second")
new.plot.scatter(x='second', y='Volt.1', alpha=0.5)
new.to_csv("newj.csv")
"""
