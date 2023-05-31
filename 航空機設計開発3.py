# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 21:16:09 2023

@author: yuki
"""

import numpy as np
import matplotlib.pyplot as plt


def calc_dv(mi, mf, ue):
    dV= ue * np.log(mi/mf)
    return dV



def get_dV(payload, refill):
    mf3 = payload + 100
    mi3 = mf3 + refill
    dv3 = calc_dv(mi3, mf3, 361*9.8)
    
    mf2 = payload + 100
    mi2 = mf2 + 1200
    dv2 = calc_dv(mi2, mf2, 361*9.8)
    
    mf1 = mi2 + 200
    mi1 = mf1 + 3400
    dv1 = calc_dv(mi1, mf1, 334*9.8)
    
    return (dv1 + dv2 + dv3)/1000


x_, y_ = np.arange(0, 500, 0.1), np.arange(0, 2000, 10)
x, y = np.meshgrid(x_, y_)
z = get_dV(payload=x, refill=y)

plt.figure(figsize=(1.4*3.8,3.8),dpi=300)    
#plt.contour(x,y,z,cmap="viridis")
plt.contour(x,y,z,cmap="rainbow")
plt.colorbar(label="ΔV [km/s]")
plt.xlabel("Payload [ton]")
plt.ylabel("Refill fuel [ton]")
plt.show()


fig, ax = plt.subplots(figsize=(1.4*3.8,3.8),dpi=300)
cs = ax.contour(x,y,z,cmap="rainbow")
fig.colorbar(cs, label="ΔV [km/s]")
ax.clabel(cs)
ax.set_xlabel("Payload [ton]")
ax.set_ylabel("Refill fuel [ton]")
plt.show()


plt.figure(figsize=(1.4*3.8,3.8),dpi=300) 
plt.pcolormesh(x,y,z,cmap="rainbow")
plt.colorbar(label="ΔV [km/s]")
plt.xlabel("Payload [ton]")
plt.ylabel("Refill fuel [ton]")
plt.show()



plt.figure(figsize=(1.4*3.8,3.8),dpi=300)    
#plt.contour(x,y,z,cmap="viridis")
plt.contour(y,x,z,cmap="rainbow")
plt.colorbar(label="ΔV [km/s]")
plt.xlabel("Refill fuel [ton]")
plt.ylabel("Payload [ton]")
plt.show()



