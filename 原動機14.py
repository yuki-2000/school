# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:19:48 2022

@author: yuki
"""

import numpy as np
from scipy import optimize


n = 6
gamma = 1.4


def get_P0_p(M):
    index = gamma/(gamma-1)
    a = 1 + (gamma-1)*M*M/2
    return a ** index 

def get_p2_p1(beta, M1):
    a = (gamma-1)/(gamma+1)
    b = 2*gamma/(gamma+1)
    b *= M1*M1
    b *= (np.sin(beta))**2
    return b-a


def get_theta(beta,M1):
    a = 1 + gamma*M1*M1/2
    a += 0.5*M1*M1*np.cos(2*beta)
    b = M1**2
    b *= (np.sin(beta))**2
    b -= 1
    b /= np.tan(beta)
    return np.arctan(b/a)


def get_M2(beta,theta,M1):
    a = (gamma-1)/2
    a *= (np.sin(beta))**2
    a *= M1**2
    a += 1
    b = gamma
    b *= (np.sin(beta))**2
    b *= M1**2
    b -= (gamma-1)/2
    b *= (np.sin(beta-theta))**2
    
    print("a=%s" % a)
    print("b=%s" % b)
    return np.sqrt(a/b)


def get_T2_T1(beta,M1):
    a = (gamma-1)/2
    a *= (np.sin(beta))**2
    a *= M1**2
    a += 1
    
    b = (gamma+1)/2
    b *= (np.sin(beta))**2
    b *= M1**2
    
     
    c = 2*gamma/(gamma+1)
    c *= (np.sin(beta))**2
    c *= M1**2
    c -= (gamma-1)/(gamma+1)
    
    return c*a/b
    
    
    
def diff_for_beta(beta,M1):
    theta = get_theta(beta,M1)
    M2 = get_M2(beta,theta,M1)
    p2_p1 = get_p2_p1(beta, M1)
    P01_p1 = get_P0_p(M1)
    P02_p2 = get_P0_p(M2)
    
    return P02_p2*p2_p1/P01_p1 - 0.9
    


M = np.zeros(n+1)
theta_rad = np.zeros(n+1)
theta_deg = np.zeros(n+1)
beta_rad = np.zeros(n+1)
beta_deg = np.zeros(n+1)
p = np.zeros(n+1)
T = np.zeros(n+1)
P0 = np.zeros(n+1)

M[0] = 8
p[0] = 1.2
T[0] = 227


for i in range(n):
    try:
        
        print(i)
        print("\n\n\n\n")
        if i == 0:
            beta_rad[i] = optimize.bisect(diff_for_beta, 0.199, 0.78, args=(M[i]))
        else:
            beta_rad[i] = optimize.bisect(diff_for_beta, beta_rad[i-1], 0.78, args=(M[i]))
    
        beta_deg[i] = np.rad2deg(beta_rad[i])
        theta_rad[i] = get_theta(beta_rad[i],M[i])
        theta_deg[i] = np.rad2deg(theta_rad[i])
        M[i+1] = get_M2(beta_rad[i],theta_rad[i],M[i])
        p[i+1] = p[i]*get_p2_p1(beta_rad[i], M[i])
        T[i+1] = T[i]*get_T2_T1(beta_rad[i],M[i])
        P0[i] = get_P0_p(M[i])*p[i]

    except:
        break







print(get_p2_p1(beta_rad[0], M[0]))


for i in range(n):
    print(p[i+1]/p[i])
    
print(1*(2.77**5))

import pandas as pd

df = pd.DataFrame({'M':M,
                   'β[rad]':beta_rad,
                   'β[deg]':beta_deg,
                   'θ[rad]': theta_rad,
                   'θ[deg]': theta_deg,
                   'T[K]':T,
                   'p[kPa]':p,
                   'Pt[kPa]':P0,            
                   },
                  index=[i for i in range(1,n+2)])

df = df.drop(index=n+1)


#表の画像化
#dpiいいぞ
#https://www.yutaka-note.com/entry/matplotlib_japanese#rcParams%E3%82%92%E8%A8%AD%E5%AE%9A
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"


df = df.round(4)



fig, ax = plt.subplots(figsize=(6,3), dpi=1000)
#fig, ax = plt.subplots()
ax.axis('off')
ax.axis('tight')
table = ax.table(cellText=df.values,
         colLabels=df.columns,
         rowLabels = df.index,
         loc='center',
         #bbox=[0,0,1,1]
         )
table.set_fontsize(14)
ax.set_title("表　各状態における値")

plt.show()
#plt.savefig('table.png')








def get_ue(gamma, pp, R,Tc):
    index = (gamma-1)/gamma
    
    b = 1- (pp**index)
    b *= 2*gamma*R*Tc/(gamma-1)
    b **= 0.5
    
    return b


print(get_ue(1.4, 1.2/6917, 287,4981))
