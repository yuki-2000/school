# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:19:16 2020

@author: yuki
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(300, 1000, 1)

def y(x):
    y =  3.78245636 + (-0.00299673415*x)+ (0.0000098473200*x*x)+ (-0.00000000968129508*x*x*x)+ (0.00000000000324372836*x*x*x*x)
    z = y/(y-1)
    
    return z


plt.plot(x,y(x))
plt.xlabel("T(K)")
plt.ylabel("k")
plt.legend()
plt.show()


print("300Kの時比熱比は")
print(y(300))

print("1000Kの時比熱比は")
print(y(1000))

