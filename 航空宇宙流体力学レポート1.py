# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:11:11 2023

@author: yukiuniv
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Ndata = 2000000

#with open('Vdata_r.txt') as f:
    #print(f.read())

f = np.loadtxt('Vdata_r.txt', skiprows=1)
time = f[:,0]
U = f[:,1]
dtime = time[1]-time[0]

Umean = np.sum(U) / Ndata #平均速度
Uf = U - Umean #速度変動



dUfdt = np.zeros(Ndata) #速度の微分
dUfdt[0] = (Uf[1]-Uf[0])/dtime   #一次精度差分
dUfdt[-1] = (Uf[-1]-Uf[-2])/dtime #一次精度差分
for i in range(1,Ndata-1):    
    dUfdt[i] = (Uf[i+1]-Uf[i-1]) / dtime / 2.0 #二次精度中心差分



Uf_rms = np.sqrt(np.sum(Uf**2) / Ndata)  #速度変動RMS値（実質的には標準偏差）
turbulence_intensity = Uf_rms / Umean #乱れ強度
Uf_Strain = (np.sum(Uf**3) / Ndata) / (Uf_rms**3) #速度変動のひずみ度
Uf_Flatness = (np.sum(Uf**4) / Ndata) / (Uf_rms**4) #速度変動の平坦度


dUfdt_rms = np.sqrt(np.sum(dUfdt**2) / Ndata)  #速度の微分のRMS値（実質的には速度の微分の標準偏差）
dUfdt_Strain = (np.sum(dUfdt**3) / Ndata) / (dUfdt_rms**3) #速度の微分のひずみ度
dUfdt_Flatness = (np.sum(dUfdt**4) / Ndata) / (dUfdt_rms**4) #速度の微分の平坦度



#確率密度関数
Uf_min = Uf.min()
Uf_max = Uf.max()
dx = 0.05
num_Ufdata = np.zeros(int((Uf_max-Uf_min)/dx)+1)

for i in range(Ndata):
    Ufdata_index = int((Uf[i] - Uf_min)/dx)
    num_Ufdata[Ufdata_index] += 1    


x = np.arange(Uf_min, Uf_max, dx)
x += dx/2
plt.figure(dpi=300) #
plt.plot(x, num_Ufdata/(Ndata*dx), c="k")
plt.xlabel("u [m/s]")
plt.ylabel("Probability")
plt.xlim(-2,2)
plt.ylim(0,1)
plt.show()


#pltバージョン
#plt.hist(Uf, bins=len(num_Ufdata), density=True)
plt.hist(Uf, bins=10000, density=True)
plt.show()

#seabornバージョン
import seaborn as sns
sns.kdeplot(data=Uf)
plt.show()

plt.figure(dpi=300) #
sns.kdeplot(data=dUfdt, c="k")
plt.xlabel("du/dt [m/s^2]")
plt.ylabel("Probability")
plt.show()



print("速度変動rms値", Uf_rms)
print("乱れ強度", turbulence_intensity)
print("歪み度", Uf_Strain)
print("平坦度", Uf_Flatness)
print("𝜕𝑢/𝜕𝑥の歪み度", dUfdt_Strain)
print("𝜕𝑢/𝜕𝑥の平坦度", dUfdt_Flatness)


plt.plot(time, U)
plt.xlabel("Time [s]")
plt.ylabel("U [m/s]")
plt.show()

plt.figure(figsize=(10,3.8), dpi=300) #
plt.plot(time, Uf, c="k")
plt.xlabel("Time [s]")
plt.ylabel("u [m/s]")
plt.xlim(0,40)
plt.ylim(-2,2)
plt.show()



plt.figure(figsize=(10,3.8), dpi=300) #
plt.plot(time, dUfdt, c="k")
plt.xlabel("Time [s]")
plt.ylabel("du/dt [m/s^2]")
plt.xlim(0,40)
plt.ylim(-4000,4000)
plt.show()



df = pd.DataFrame()
df["Time[s]"] = time
df["U[m/s]"] = U
df["速度変動"] = Uf
df["速度勾配"] = dUfdt

df.to_csv('TimeSeriesData.txt', header=True, index=False)


