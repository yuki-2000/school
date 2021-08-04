# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:19:16 2020

@author: yuki
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 0.05, 0.0001)

def y1(t):
    y =  np.sin(2 * np.pi * 80 *t)
    return y

def y2(t):
    y =  1.4 * np.sin((2 * np.pi * 80 *t)-0.1)
    return y

def y3(t):
    y =  np.sin(2 * np.pi * 160 *t)
    return y

def y4(t):
    y =  15 * np.sin((2 * np.pi * 160 *t) - np.pi/2)
    return y

def yy1(t):
    y =  y1(t) + y3(t)
    return y

def yy2(t):
    y =  y2(t) + y4(t)
    return y


plt.plot(t,y1(t))
plt.xlabel("t [sec]")
plt.ylabel("y [m]")
plt.legend()
plt.show()

plt.plot(t,y2(t))
plt.xlabel("t [sec]")
plt.ylabel("y [m]")
plt.legend()
plt.show()

plt.plot(t,y3(t))
plt.xlabel("t [sec]")
plt.ylabel("y [m]")
plt.legend()
plt.show()

plt.plot(t,y4(t))
plt.xlabel("t [sec]")
plt.ylabel("y [m]")
plt.legend()
plt.show()

plt.plot(t,yy1(t))
plt.xlabel("t [sec]")
plt.ylabel("y [m]")
plt.legend()
plt.show()

plt.plot(t,yy2(t))
plt.xlabel("t [sec]")
plt.ylabel("y [m]")
plt.legend()
plt.show()