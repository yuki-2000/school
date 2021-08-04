# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:52:42 2021

@author: yuki
"""

import matplotlib.pyplot as plt
import numpy as np


cos10 = np.cos(np.radians(10))
sin10 = np.sin(np.radians(10))



def Rx(i):
    rx = cos10 + sin10*np.cos(i)/np.sqrt(3)
    return rx

def Ry(i):
    ry = np.sin(i)/np.sqrt(3)
    return ry

def Rz(i):
    rz = cos10 * np.cos(i)/np.sqrt(3) - sin10
    return rz

def n0(i):
    n0 = np.arctan(Rz(i)/Rx(i))
    return np.degrees(n0)

def i0(i):
    i0 = np.arctan(Ry(i) / (np.sqrt(Rx(i)**2 + Rz(i)**2)))
    return np.degrees(i0)





i = np.linspace(0, 90, 1000)

plt.plot(i,n0(np.radians(i)))
plt.xlabel("deg")
plt.ylabel("0n")
plt.legend()
plt.show()

plt.plot(i,i0(np.radians(i)))
plt.xlabel("deg")
plt.ylabel("0i")
plt.legend()
plt.show()