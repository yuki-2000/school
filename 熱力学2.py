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
    y *= 259.82
    
    return y


plt.plot(x,y(x))
plt.xlabel("T(K)")
plt.ylabel("Cp(J/kg*K)")
plt.legend()
plt.show()


print("300Kの時")
print(y(300))


print("5%増えると")
print(y(300)*1.05)

print("477Kの時")
print(y(477))
print("478Kの時")
print(y(478))
print("よって約477K")
