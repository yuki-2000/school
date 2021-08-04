# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:52:42 2021

@author: yuki
"""

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


cos20 = np.cos(np.radians(20))
sin20 = np.sin(np.radians(20))
tan20 = sin20/cos20
a = np.linspace(0, 0.7896, 100000)
aa = np.linspace(0.7896, 5, 100000)
aaa = np.linspace(0, 5, 1000)
r = 1.2
y1 = np.degrees(np.arctan((a-0.02)/(0.219+np.sqrt(r**2-(r-a)**2))))
y2 = np.degrees(np.arctan((aa-0.02)/(0.219+r*cos20+tan20*(aa-r*(r-sin20)))))
y3 =70*aaa/aaa


c1,c2,c3 = "blue","green","red"     # 各プロットの色
#l1,l2,l3 = "Ct","Cm","Ctotal"   # 各ラベル

ax.set_xlabel('a')  # x軸ラベル
ax.set_ylabel('角度')  # y軸ラベル
ax.set_title('') # グラフタイトル
# ax.set_aspect('equal') # スケールを揃える
ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
ax.set_ylim([0, 90])    # y方向の描画範囲を指定
#ax.plot(a, y1, color=c1, label=l1)
#ax.plot(aa, y2, color=c2, label=l2)
#x.plot(aaa, y3, color=c3, label=l3)

ax.plot(a, y1, color=c1)
ax.plot(aa, y2, color=c2)
ax.plot(aaa, y3, color=c3)
ax.legend(loc=0)    # 凡例
fig.tight_layout()  # レイアウトの設定
# plt.savefig('hoge.png') # 画像の保存
plt.show()



