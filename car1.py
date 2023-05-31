# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 12:07:13 2022

@author: HikaruSekiya
"""

import pandas as pd
import numpy as np

df = pd.read_csv("pressure.csv")


#m
L = 150/1000
r = 43/1000
D = 86/1000
Vc = 50/1000000
m = 0.7



A = D*D*3.14/4
Vs = A*2*r
print(Vs)



def V(theta):
    x = r*(1-np.cos(np.deg2rad(theta)))
    x += L
    x -= np.sqrt(L**2 - (r*np.sin(np.deg2rad(theta)))**2)
    
    V = Vc + x*A
    return V

print(df)



df["Volume(m^3)"] = V(df["THETA (degree)"])
df["Volume(cc)"] = V(df["THETA (degree)"])*1000000
df.plot(x="Volume(cc)", y ="Pressure (Pa)" )

#theta[deg]
def torque(theta, w):
    #rpm⇒rad/s
    w = w * 2*np.pi/60
    thetarad = np.deg2rad(theta)
    
    Tcgt = np.pi * D*D * r/4
    Tcgt *= df["Pressure (Pa)"][theta]
    Tcgt *= np.sin(thetarad) + r * (np.sin(2*thetarad))/(2*L) 
    
    
    Tcrt = -r*(np.sin(thetarad))/(4*L)
    Tcrt += (np.sin(2*thetarad))/2
    Tcrt += 3*r*(np.sin(3*thetarad))/(4*L)
    Tcrt *= -1* m * r*r * w*w
    
    
    T = Tcgt + Tcrt
    return T
    
    
#トルクルート  
    
df["Torque@2000rpm(Nm)"] = torque(df["THETA (degree)"],2000)
df.plot(x="THETA (degree)", y ="Torque@2000rpm(Nm)" )    
df["Torque@4000rpm(Nm)"] = torque(df["THETA (degree)"],4000)
df.plot(x="THETA (degree)", y ="Torque@4000rpm(Nm)" )    
df["Torque@6000rpm(Nm)"] = torque(df["THETA (degree)"],6000)
df.plot(x="THETA (degree)", y ="Torque@6000rpm(Nm)" )    

df.plot(x="THETA (degree)", y =["Torque@2000rpm(Nm)","Torque@4000rpm(Nm)","Torque@6000rpm(Nm)"] )    
    
#時間平均や体積平均でなく、回転角平均を求めた    
meanT = sum(df["Torque@2000rpm(Nm)"])  /len(df["Torque@2000rpm(Nm)"])
print("有効圧力@2000")
print(meanT * 4 * np.pi/Vs)

meanT = sum(df["Torque@4000rpm(Nm)"])  /len(df["Torque@4000rpm(Nm)"])
print("有効圧力@4000")
print(meanT * 4 * np.pi/Vs)

meanT = sum(df["Torque@6000rpm(Nm)"])  /len(df["Torque@6000rpm(Nm)"])
print("有効圧力@6000")
print(meanT * 4 * np.pi/Vs)



#pv線図ルート

P = df["Pressure (Pa)"]
V = df["Volume(m^3)"]

#planA
Work = 0
for i in range(720):
    Work += P[i] * (V[i+1]-V[i])

#Work += P[720] * (V[0]-V[720])
print("左のP")
print(Work/Vs)


#planB台刑法
Work = 0
for i in range(720):
    Work += ((P[i]+P[i+1])/2) * (V[i+1]-V[i])

#Work += (P[720]+P[0])/2 * (V[0]-V[720])
print("平均・台形のP")
print(Work/Vs)


#planC
Work = 0
for i in range(720):
    Work += P[i+1] * (V[i+1]-V[i])

#Work += P[0] * (V[0]-V[720])
print("右のP")
print(Work/Vs)

df.plot(x="THETA (degree)", y ="Volume(cc)" )

df.to_csv("car1.csv")



