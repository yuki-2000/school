# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:43:10 2021

@author: yuki
"""

import math
import numpy as np


#使い方
#1.グローバル変数の部分を条件通りに書き換える
#2alfa = np.linspace(0, 45, 100)の第二変数がαの最大値であり、45度ぐらいから初めて実行してみる
#3.結果がM1=1を下回るあたりで止まるので、その時に表示されているα以下の値にnp.linspace(0, 45, 100)の第二変数を変える
#4.実行すればプロット、そしてエクセルの保存がされる。


#グローバル変数（ただし関数内で無断使用）

M0 = 6
gamma=1.4
phi = 6






def ff(x):
    return x * x - 2.0


#dgree入力
def oblique01(alfa, beta):
    

    #radに変換
    beta = np.radians(beta)
    
    
    
    y = 2*(M0*M0*(np.sin(beta))*(np.sin(beta))-1)
    y /= (np.tan(beta))  *  (M0*M0*(gamma+np.cos(2*beta)) +2)
    y -= np.tan(np.radians(alfa+phi))
    
    return y



def oblique01falseposition(left, right, alfa):
    while True:
        # 点$ (a,f(a)) $ と 点 $ (b,f(b)) $ を結ぶ直線と $ x $ 軸の交点
        c  = (left * oblique01(alfa=alfa, beta=right) - right * oblique01(alfa=alfa, beta=left)) / (oblique01(alfa=alfa, beta=right) - oblique01(alfa=alfa, beta=left))
        #print (c, c - math.sqrt(2))
        #print (c)

        fc = oblique01(alfa=alfa, beta=c)
        if (abs(fc) < 0.0000000001):
            break

        if (fc < 0):
            # f(c) < 0 であれば, 解は区間 (c, b) の中に存在
            left = c
        else:
            # f(c) > 0 であれば, 解は区間 (a, c) の中に存在
            right = c
    print(c)
    return c


#print("最終結果")
#print(oblique01falseposition(left= 0.1, right= 1, alfa=15))



    
def p1p0(beta):
    y = (2*gamma/(gamma+1))
    y *= M0*M0*(np.sin(np.radians(beta))) * (np.sin(np.radians(beta))) -1
    y +=1
    
    return y
    
   
def M1(alfa,beta):
    y = 1
    y /= np.sin(np.radians(beta-alfa-phi)) 
    y *= np.sqrt(  (gamma-1)  *  M0*M0*  (np.sin(np.radians(beta)))*(np.sin(np.radians(beta)))  +2  )
    y /= np.sqrt(  2*gamma*M0*M0*(np.sin(np.radians(beta)))*(np.sin(np.radians(beta)))    -gamma+1  )
    return y
    

def nu(M):
    #mm = M*M
    #y = (np.sqrt((gamma+1)/(gamma-1)))  *   (np.arctan(np.sqrt(((gamma-1)*(M*M-1))/(gamma+1))))  -   (np.arctan(np.sqrt(M*M-1)))
    y = np.sqrt((gamma+1)/(gamma-1))
    y *=   np.arctan(  np.sqrt(  ((gamma-1)*(M*M-1)) / (gamma+1)  )  )
    y -=   np.arctan(  np.sqrt(M*M-1)  )
    #print(y)
    return y
    
    
    
    
def expansion03(alfa, M3):
    y = nu(M3)-np.radians(alfa)-nu(M0)
    return y
    
    
    


def expansion03falseposition(left, right, alfa):
    while True:
        # 点$ (a,f(a)) $ と 点 $ (b,f(b)) $ を結ぶ直線と $ x $ 軸の交点
        c  = (left * expansion03(alfa=alfa, M3=right) - right * expansion03(alfa=alfa,M3=left)) / (expansion03(alfa=alfa, M3=right) - expansion03(alfa=alfa, M3=left))
        #print (c, c - math.sqrt(2))
        #print (c)

        fc = expansion03(alfa=alfa, M3=c)
        if (abs(fc) <  0.0000000001):
            break

        if (fc < 0):
            # f(c) < 0 であれば, 解は区間 (c, b) の中に存在
            left = c
        else:
            # f(c) > 0 であれば, 解は区間 (a, c) の中に存在
            right = c
    print(c)
    return c





def p3p0(M3):
    #mm= M3*M3
    y = ((M0*M0+(2/(gamma-1))) / (M3*M3+(2/(gamma-1))) )**(gamma/(gamma-1))
    return y
    
    



def expansion12(M1,M2):
    y = nu(M2)-np.radians(phi*2)-nu(M1)
    return y
 






def expansion12falseposition(left, right, M1):
    while True:
        # 点$ (a,f(a)) $ と 点 $ (b,f(b)) $ を結ぶ直線と $ x $ 軸の交点
        c  = (left * expansion12(M1 = M1, M2=right) - right * expansion12(M1 = M1,M2=left)) / (expansion12(M1 = M1, M2=right) - expansion12(M1 = M1, M2=left))
        #print (c, c - math.sqrt(2))
        #print (c)

        fc = expansion12(M1=M1, M2=c)
        if (abs(fc) <  0.0000000001):
            break

        if (fc < 0):
            # f(c) < 0 であれば, 解は区間 (c, b) の中に存在
            left = c
        else:
            # f(c) > 0 であれば, 解は区間 (a, c) の中に存在
            right = c
    print(c)
    return c




def p2p1(M1,M2):
    y = ((M1*M1+2/(gamma-1)) / (M2*M2+(2/(gamma-1))) )**(gamma/(gamma-1))
    return y




def CL(p1_p0, p2_p0, p3_p0, alfa):
    
    y = p1_p0*np.cos(np.radians(alfa+phi)) / (2*np.cos(np.radians(phi)))
    y += p2_p0*np.cos(np.radians(alfa-phi))/(2*np.cos(np.radians(phi)))
    y -= p3_p0*np.cos(np.radians(alfa))
    y *=2
    y /= gamma*M0*M0
    
    return y
        
def CD(p1_p0, p2_p0, p3_p0, alfa):
    
    y = p1_p0*np.sin(np.radians(alfa+phi)) / (2*np.cos(np.radians(phi)))
    y += p2_p0*np.sin(np.radians(alfa-phi))/(2*np.cos(np.radians(phi)))
    y -= p3_p0*np.sin(np.radians(alfa))
    y *=2
    y /= gamma*M0*M0
    
    return y




# 成績表の生成
import numpy as np
import pandas as pd


# 二つ目の変数はαの最大値で、M1=1を下回るところが最大

alfa = np.linspace(0, 36, 100)
beta = []
for i in alfa:
    print("α={}".format(i))
    beta.append(oblique01falseposition(left= 0.1, right= 1, alfa=i))
beta = np.array(beta)
print("beta終了")


p1_p0 = p1p0(np.array(beta))


M1 = M1(alfa,beta)

print("M1終了")

M3 = []
for i in alfa:
    print("α={}".format(i))
    M3.append(expansion03falseposition(left= 2, right= 5, alfa=i))
M3 = np.array(M3)

p3_p0 = p3p0(M3)



M2 = []
for i,j in enumerate(M1):
    print("α={}".format(alfa[i]))
    print("M1={}".format(j))
    M2.append(expansion12falseposition(left= 2, right= 5, M1=j))
M2 = np.array(M2)

p2_p1 = p2p1(M1,M2)


p2_p0 = p2_p1*p1_p0



CL = CL(p1_p0, p2_p0, p3_p0, alfa)

CD = CD(p1_p0, p2_p0, p3_p0, alfa)

L_D = CL/CD



# 成績表データフレームの作成
df = pd.DataFrame({
    "alfa" : alfa,
    "beta" : beta,    
    "M1" : M1,
    "M2" : M2,
    "M3" : M3,
    "p1/p0" : p1_p0,    
    "p2/p0":p2_p0,
    "p3/p0" : p3_p0,
    "p2/p1":p2_p1,
    "CL":CL,
    "CD":CD,
    "L/D":L_D,
    "L/D/5":L_D/5

})



df.plot()
df.plot(x="alfa")
df.plot(x="alfa", y=["M1","M2", "M3"])
df.plot(x="alfa", y=["p1/p0","p2/p0", "p3/p0"])
df.plot(x="alfa", y=["CL","CD","L/D/5"])
df.plot(x="alfa", y=["CL","CD","L/D"])


# 表示
print(df)
#df.to_excel('圧縮レポート7_2.xlsx')
