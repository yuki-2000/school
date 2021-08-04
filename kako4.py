# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:20:37 2021

@author: yuki
"""

#https://qiita.com/trami/items/b501abe7667e55ab2c9f

"""複数のグラフを重ねて描画するプログラム"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

t = np.linspace(1, 300, 1000)
y1 = 6*(10**6)*(t**(2/3))
y2 = (2.04*(10**10))/t
y3 = y1+y2


c1,c2,c3 = "blue","green","red"     # 各プロットの色
l1,l2,l3 = "Ct","Cm","Ctotal"   # 各ラベル

ax.set_xlabel('Vw')  # x軸ラベル
ax.set_ylabel('C')  # y軸ラベル
ax.set_title('') # グラフタイトル
# ax.set_aspect('equal') # スケールを揃える
ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
ax.set_ylim([0, 0.08*10**10])    # y方向の描画範囲を指定
ax.plot(t, y1, color=c1, label=l1)
ax.plot(t, y2, color=c2, label=l2)
ax.plot(t, y3, color=c3, label=l3)
ax.legend(loc=0)    # 凡例
fig.tight_layout()  # レイアウトの設定
# plt.savefig('hoge.png') # 画像の保存
plt.show()