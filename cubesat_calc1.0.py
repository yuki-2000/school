# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:36:04 2020

@author: yuki
"""
from math import log 
from math import sqrt
from math import pi

def H(a,b,l,N,I,x,ur1):
    y1 = ur1*N*I/2*l*(b-a)
    #print(y1)
    y2 = x*log((b+sqrt(b*b+x*x))/(a+sqrt(a*a+x*x)))
    #print(y2)
    y3 = (x-l)*log((b+sqrt(b*b+(x-l)*(x-l)))/(a+sqrt(a*a+(x-l)*(x-l))))
    #print(y3)
    h = y1*(y2-y3)
    return h

def f(u0,u,B):
    f = (1/2)*((1/u0)-(1/u))*B*B
    return f

def B(H,u0,kx,N):
    B = H*(u0+(kx*(1-N))/(1+kx*(N/u0)))
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


#以下SI単位系

#電磁石のパラメータ
a = 0.005#内半径
b = 0.05#外半径
l = 0.3#長さ
r0 = 0.001#線の直径
p =1.68/(10**8)#線の抵抗率(銅)
I = 100#電流
ur1 = 200000#芯の比透磁率（鉄）
N = (l*(b-a))/(r0*r0)#巻き数



#対象物体のパラメータ
x = 1000#電磁石からの距離
u0 = 1.257/(10**6)#真空中の透磁率
ur = 1000#対象物の比透磁率（ステンレス）
u = u0*ur#対象物の透磁率
kx = u-u0#対象物の磁化率
a2 = 0.001#対象物が円柱として、半径
l2 = 0.01#対象物が円柱として、長さ
p2 = 7700#対象物の比重（ステンレス）



print("距離[m]")
print(x)

H = H(a,b,l,N,I,x,ur1)
print("磁界")
print(H)

N2 = N2(l2,a2)
#N2 =0
print("自己減磁率")
print(N2)

B =B(H,u0,kx,N2)
print("磁束密度")
print(B)

f = f(u0,u,B)
print("力[N/m*m]")
print(f)

#もし円柱部品なら
print("力[N]")
F = F(f,a2)
print(F)


R = R(p,l,a,b,r0)
print("抵抗値[Ω]")
print(R)    

m = m(p2,a2,l2)
print("対象物質量[kg]")
print(m)

print("対象物加速度[m/s*s]")
print(F/m)



