# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:22:15 2020

@author: z
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:36:04 2020

@author: yuki
"""
from math import log 
from math import sqrt
from math import pi
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def H(a,b,l,N,I,x,ur1):
    y1 = ur1*N*I/2*l*(b-a)
    #print(y1)
    y2 = x*log((b+sqrt(b*b+x*x))/(a+sqrt(a*a+x*x)))
    #print(y2)
    y3 = (x-l)*log((b+sqrt(b*b+(x-l)*(x-l)))/(a+sqrt(a*a+(x-l)*(x-l))))
    #print(y3)
    H = y1*(y2-y3)
    return H

def f(u0,u,B):
    f = (1/2)*((1/u0)-(1/u))*B*B
    return f

def B(H,u):
    B = H*u
    return B

def N2(l2,a2):
    N2 = 1-(l2/sqrt(l2*l2+4*a2*a2))
    return N2

def F(f,a2):
    F = f*pi*a2*a2
    return F

def R(p,l,a,b,r0):
    R = (4*p*l*(b-a)*(a+b))/(r0**4)
    return R

def m(p2,a2,l2):
    m = p2*pi*a2*a2*l2
    return m

def I(S,Wmm,R):
    W = S*Wmm
    I = W/(R*R)
    return I


#以下SI単位系

#電磁石のパラメータ
a = 0.005#内半径
b = 0.05#外半径
l = 0.2#長さ
r0 = 0.004#線の直径
p =1.68/(10**8)#線の抵抗率(銅)
I = 100#電流
S = 0.03 #太陽光パネル面積
Wmm = 448#単位面積当たり太陽光パネル発電量
ur1 = 200000#芯の比透磁率（鉄）
L = (pi*l*(b-a)*(a+b))/(r0*r0)#線の総延長
N = (l*(b-a))/(r0*r0)#巻き数
print("総延長")
print(L)
print("巻き数")
print(N)



#対象物体のパラメータ
x = 10#電磁石からの距離
u0 = 1.257/(10**6)#真空中の透磁率
ur = 1000#対象物の比透磁率（ステンレス）
u = u0*ur#対象物の透磁率
kx = u-u0#対象物の磁化率
a2 = 0.002#対象物が円柱として、半径
l2 = 0.01#対象物が円柱として、長さ
p2 = 7700#対象物の比重（ステンレス）



print("距離[m]")
print(x)

W = S*Wmm
print("発電量[W]")
print(W)

R = R(p,l,a,b,r0)
print("抵抗値[Ω]")
print(R)    

#I = I(S,Wmm,R)
print("電流[A]")
print(I)   

print("消費電力[W]")
print(I*R*R)


H = H(a,b,l,N,I,x,ur1)
print("磁界")
print(H)

N2 = N2(l2,a2)
#N2 =0
print("自己減磁率")
print(N2)

B =B(H,u)
print("磁束密度")
print(B)

f = f(u0,u,B)
print("力[N/m*m]")
print(f)

#もし円柱部品なら
print("力[N]")
F = F(f,a2)
print(F)

m = m(p2,a2,l2)
print("対象物質量[kg]")
print(m)

print("対象物加速度[m/s*s]")
print(F/m)


"""
def A(a,b,l,N,I,x,ur1,l2,a2,u0,kx,u,p2):
    HH = H(a,b,l,N,I,x,ur1)
    N2N2 = N2(l2,a2)
    BB =B(HH,u)
    ff = f(u0,u,BB)
    FF = F(ff,a2)
    mm = m(p2,a2,l2)
    return FF/mm


x = [i/100 for i in range(100, 1000)]
y = [A(a,b,l,N,I,x,ur1,l2,a2,u0,kx,u,p2) for x in x]
plt.plot(x,y)
plt.show()

#対数
fig, ax = plt.subplots()
ax.plot(x, y,'.')
ax.set_yscale('log')
plt.show()
 
for x in range(10):    
    print(A(a,b,l,N,I,x,ur1,l2,a2,u0,kx,u,p2))   
"""
"""
def AA(x):
    #以下SI単位系
    
    #電磁石のパラメータ
    a = 0.005#内半径
    b = 0.05#外半径
    l = 0.2#長さ
    r0 = 0.004#線の直径
    p =1.68/(10**8)#線の抵抗率(銅)
    I = 100#電流
    S = 0.06 #太陽光パネル面積
    Wmm = 350#単位面積当たり太陽光パネル発電量
    ur1 = 200000#芯の比透磁率（鉄）
    L = (pi*l*(b-a)*(a+b))/(r0*r0)#線の総延長
    N = (l*(b-a))/(r0*r0)#巻き数
    
    
    
    
    #対象物体のパラメータ
    #x = 5#電磁石からの距離
    u0 = 1.257/(10**6)#真空中の透磁率
    ur = 1000#対象物の比透磁率（ステンレス）
    u = u0*ur#対象物の透磁率
    kx = u-u0#対象物の磁化率
    a2 = 0.002#対象物が円柱として、半径
    l2 = 0.01#対象物が円柱として、長さ
    p2 = 7700#対象物の比重（ステンレス）
    
    HH = H(a,b,l,N,I,x,ur1)
    N2N2 = N2(l2,a2)
    BB =B(HH,u)
    ff = f(u0,u,BB)
    FF = F(ff,a2)
    mm = m(p2,a2,l2)
    return (FF/mm)

print("最終的な速さは")
print(integrate.quad(AA, 1, 5))
"""