# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:58:18 2023

@author: yuki
"""

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation





#グラフ設定

#フォント設定
plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
#plt.rcParams['mathtext.fontset'] = 'stix' # math fontの設定
#plt.rcParams["font.size"] = 15 # 全体のフォントサイズが変更されます。
#plt.rcParams['xtick.labelsize'] = 9 # 軸だけ変更されます。
#plt.rcParams['ytick.labelsize'] = 24 # 軸だけ変更されます



#軸設定
plt.rcParams['xtick.direction'] = 'in' # x axis in
plt.rcParams['ytick.direction'] = 'in' # y axis in 
#plt.rcParams['axes.grid'] = True # make grid
#plt.rcParams['grid.linestyle']='--' #グリッドの線種
plt.rcParams["xtick.minor.visible"] = True  #x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True  #y軸補助目盛りの追加
plt.rcParams['xtick.top'] = True                   #x軸の上部目盛り
plt.rcParams['ytick.right'] = True                 #y軸の右部目盛り



#軸大きさ
#plt.rcParams["xtick.major.width"] = 1.0             #x軸主目盛り線の線幅
#plt.rcParams["ytick.major.width"] = 1.0             #y軸主目盛り線の線幅
#plt.rcParams["xtick.minor.width"] = 1.0             #x軸補助目盛り線の線幅
#plt.rcParams["ytick.minor.width"] = 1.0             #y軸補助目盛り線の線幅
#plt.rcParams["xtick.major.size"] = 10               #x軸主目盛り線の長さ
#plt.rcParams["ytick.major.size"] = 10               #y軸主目盛り線の長さ
#plt.rcParams["xtick.minor.size"] = 5                #x軸補助目盛り線の長さ
#plt.rcParams["ytick.minor.size"] = 5                #y軸補助目盛り線の長さ
#plt.rcParams["axes.linewidth"] = 1.0                #囲みの太さ




#凡例設定
plt.rcParams["legend.fancybox"] = False  # 丸角OFF
plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'black'  # edgeの色を変更
plt.rcParams["legend.markerscale"] = 5 #markerサイズの倍率





plt.figure(figsize=(1.4*3.8,3.8),dpi=300)

plt.xlabel("Iteration")
plt.ylabel("Failure ratio")
#軸の範囲
plt.xlim(0,10000000)
plt.ylim(0, 0.0002)

#軸の指定
#plt.xticks(np.arange(0, 0.021, 0.005))
#plt.yticks(np.arange(0, 61, 10))
plt.tight_layout()
#plt.legend(fontsize=10)






random.seed(1)

ite = []
g1s = []
fail_rates = []

num_fail = 0



for i in range(1, 10000000):
    x1 = random.normalvariate(22.5, 1.3)
    x2 = random.normalvariate(5, 0.5)
    x3 = random.normalvariate(330, 3)
    x4 = random.normalvariate(220, 8.2)
    x5 = random.normalvariate(0, 55)
    
    y1 = 0.4*x1*x3/x2
    if x4 < 500:
        y2 = -0.9*x4+1200+x5
    else:
        y2 = 750 + x5
    
    g1= y2-y1
    if g1 < 0:
        num_fail += 1
    
    fail_rate =  num_fail / i
    
    ite.append(i)
    g1s.append(g1)
    fail_rates.append(fail_rate)
    
    
    
    


#plt.scatter(ite, g1s, s=1)
plt.plot(ite, fail_rates, c="r")
plt.show()