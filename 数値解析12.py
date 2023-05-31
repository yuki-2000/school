# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 22:36:06 2022

@author: yuki
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('数値解析12.xlsx')




plt.plot(df["x"],df["y1"], label="y1")
plt.plot(df["x"],df["y2"], label="y2")
plt.plot(df["x"],df["y3"], label="y3")
plt.scatter(df["x"],df["y"], label="y data")

plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0,5)
plt.ylim(-2,5)
plt.legend()

plt.show()
