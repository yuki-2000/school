# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:23:51 2021

@author: yuki
"""

import numpy as np
from scipy import optimize

#https://qiita.com/Tusnori/items/ceebfb2cdbaf694f95f7
#https://cearun.grc.nasa.gov/ThermoBuild/


def H_balance(nH2O, nH2, nH, nOH):
    y = 2*nH2O + 2*nH2 + nOH + nH -2
    return y


def O_balance(nH2O, nO2, nO, nOH):
    y = nH2O + 2*nO2 + nOH + nO -1
    return y

def eq1(Kp1, Pm, nsum, nO, nO2):
    y = Kp1 * ((nO2/nsum)**0.5) - (nO/nsum)*(Pm**0.5)
    return y
    
    
def eq2(Kp2, Pm, nsum, nH, nH2):
    y = Kp2 * ((nH2/nsum)**0.5) - (nH/nsum)*(Pm**0.5)  
    return y
    


def eq3(Kp3, Pm, nsum, nOH, nH2, nO2):
    y = Kp3 * ((nH2 * nO2)**0.5) - nOH  
    return y


def eq4(Kp4, Pm, nsum, nH2O, nH2, nO2):
    y = Kp4 * (nH2/nsum) * ((nO2/nsum)**0.5) - (nH2O/nsum)*(Pm**-0.5)  
    return y




# 解きたい関数をリストで戻す
def func(x):
    global nsum,Pm, Kp1, Kp2, Kp3, Kp4
    #print(nsum,Pm, Kp1, Kp2, Kp3, Kp4)
    #print(nsum)
    nH2O, nH2, nH, nO2, nO, nOH = x    
    
    a = H_balance(nH2O, nH2, nH, nOH)
    b = O_balance(nH2O, nO2, nO, nOH)
    c = eq1(Kp1, Pm, nsum, nO, nO2)
    d = eq2(Kp2, Pm, nsum, nH, nH2)
    e = eq3(Kp3, Pm, nsum, nOH, nH2, nO2)
    f = eq4(Kp4, Pm, nsum, nH2O, nH2, nO2)
    return [a,b,c,d,e,f]





def get_middle_value(xa,ya,xb,yb,xx):
    slope = (yb-ya)/(xb-xa)
    return ya + slope*(xx-xa)



"""
#3000K
#Tw4084
nsum = 1.1
for i in range(100):

    Tf0 = 3000
    
    Pm = 20
    #3000K
    Kp1 = 10 ** -0.949
    Kp2 = 10 ** -0.803
    Kp3 = 10 ** 0.074
    Kp4 = 10 ** 1.343
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    #print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3000K
    Cp = nH2O*56.823 +  nH2*37.078 + nH*20.786 + nO2*39.980 + nO*20.939 + nOH*37.038
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH

"""



"""
#3500K
#Tw2998
nsum = 1.1
for i in range(10):

    Tf0 = 3500
    
    Pm = 20
    #3500K
    Kp1 = 10 ** -0.31
    Kp2 = 10 ** -0.231
    Kp3 = 10 ** 0.16
    Kp4 = 10 ** 0.712
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3500K
    Cp = nH2O*58.252 +  nH2*38.135 + nH*20.786 + nO2*40.904 + nO*21.094 + nOH*37.840
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH
"""





"""
#3300K
#結果はTw3532
nsum = 1.1
for i in range(10):

    Tf0 = 3300
    
    Pm = 20
    #3300K
    Kp1 = 10 ** -0.543
    Kp2 = 10 ** -0.439
    Kp3 = 10 ** 0.129
    Kp4 = 10 ** 0.942
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3300K
    Cp = nH2O*57.736 +  nH2*37.728 + nH*20.786 + nO2*40.549 + nO*21.025 + nOH*37.535
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH

"""




"""

#3400K
#結果はTw3285
nsum = 1.1
for i in range(10):

    Tf0 = 3400
    
    Pm = 20
    #3400K
    Kp1 = 10 ** -0.423
    Kp2 = 10 ** -0.332
    Kp3 = 10 ** 0.145
    Kp4 = 10 ** 0.824
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3400K
    Cp = nH2O*58.002 +  nH2*37.934 + nH*20.786 + nO2*40.549 + nO*21.058 + nOH*37.690
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH


"""


"""



#3350K
#結果はTw3408
nsum = 1.1
for i in range(10):

    Tf0 = 3350
    
    Pm = 20
    

    
    #3350K
    Kp1 = 10 ** get_middle_value(xa=3300,ya=-0.543,xb=3400,yb=-0.423,xx=3350)
    Kp2 = 10 ** get_middle_value(xa=3300,ya=-0.439,xb=3400,yb= -0.332,xx=3350)
    Kp3 = 10 ** get_middle_value(xa=3300,ya=0.129,xb=3400,yb=0.145,xx=3350)
    Kp4 = 10 ** get_middle_value(xa=3300,ya=0.942,xb=3400,yb=0.824,xx=3350)
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3400Kここは一定にする
    Cp = nH2O*58.002 +  nH2*37.934 + nH*20.786 + nO2*40.549 + nO*21.058 + nOH*37.690
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH

"""


"""

#3375K
#結果はTw3348
nsum = 1.1
for i in range(10):

    Tf0 = 3375
    
    Pm = 20
    

    
    #3350K
    Kp1 = 10 ** get_middle_value(xa=3300,ya=-0.543,xb=3400,yb=-0.423,xx=3375)
    Kp2 = 10 ** get_middle_value(xa=3300,ya=-0.439,xb=3400,yb= -0.332,xx=3375)
    Kp3 = 10 ** get_middle_value(xa=3300,ya=0.129,xb=3400,yb=0.145,xx=3375)
    Kp4 = 10 ** get_middle_value(xa=3300,ya=0.942,xb=3400,yb=0.824,xx=3375)
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3400Kここは一定にする
    Cp = nH2O*58.002 +  nH2*37.934 + nH*20.786 + nO2*40.549 + nO*21.058 + nOH*37.690
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH

"""


"""
#3360K
#結果はTw3384
nsum = 1.1
for i in range(10):

    Tf0 = 3360
    
    Pm = 20
    

    
    #3350K
    Kp1 = 10 ** get_middle_value(xa=3300,ya=-0.543,xb=3400,yb=-0.423,xx=3360)
    Kp2 = 10 ** get_middle_value(xa=3300,ya=-0.439,xb=3400,yb=-0.332,xx=3360)
    Kp3 = 10 ** get_middle_value(xa=3300,ya=0.129,xb=3400,yb=0.145,xx=3360)
    Kp4 = 10 ** get_middle_value(xa=3300,ya=0.942,xb=3400,yb=0.824,xx=3360)
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3400Kここは一定にする
    Cp = nH2O*58.002 +  nH2*37.934 + nH*20.786 + nO2*40.549 + nO*21.058 + nOH*37.690
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH

"""



"""
#3370K
#結果はTw3360
nsum = 1.1
for i in range(10):

    Tf0 = 3370
    
    Pm = 20
    

    
    #3350K
    Kp1 = 10 ** get_middle_value(xa=3300,ya=-0.543,xb=3400,yb=-0.423,xx=3370)
    Kp2 = 10 ** get_middle_value(xa=3300,ya=-0.439,xb=3400,yb=-0.332,xx=3370)
    Kp3 = 10 ** get_middle_value(xa=3300,ya=0.129,xb=3400,yb=0.145,xx=3370)
    Kp4 = 10 ** get_middle_value(xa=3300,ya=0.942,xb=3400,yb=0.824,xx=3370)
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3400Kここは一定にする
    Cp = nH2O*58.002 +  nH2*37.934 + nH*20.786 + nO2*40.549 + nO*21.058 + nOH*37.690
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH

"""






"""
#3365K
#結果はTw3372
nsum = 1.1
for i in range(10):

    Tf0 = 3365
    
    Pm = 20
    

    
    #3350K
    Kp1 = 10 ** get_middle_value(xa=3300,ya=-0.543,xb=3400,yb=-0.423,xx=3365)
    Kp2 = 10 ** get_middle_value(xa=3300,ya=-0.439,xb=3400,yb=-0.332,xx=3365)
    Kp3 = 10 ** get_middle_value(xa=3300,ya=0.129,xb=3400,yb=0.145,xx=3365)
    Kp4 = 10 ** get_middle_value(xa=3300,ya=0.942,xb=3400,yb=0.824,xx=3365)
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3400Kここは一定にする
    Cp = nH2O*58.002 +  nH2*37.934 + nH*20.786 + nO2*40.549 + nO*21.058 + nOH*37.690
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH
"""


"""
#3368K
#結果はTw3365
nsum = 1.1
for i in range(10):

    Tf0 = 3368
    
    Pm = 20
    

    
    #3350K
    Kp1 = 10 ** get_middle_value(xa=3300,ya=-0.543,xb=3400,yb=-0.423,xx=3368)
    Kp2 = 10 ** get_middle_value(xa=3300,ya=-0.439,xb=3400,yb=-0.332,xx=3368)
    Kp3 = 10 ** get_middle_value(xa=3300,ya=0.129,xb=3400,yb=0.145,xx=3368)
    Kp4 = 10 ** get_middle_value(xa=3300,ya=0.942,xb=3400,yb=0.824,xx=3368)
    
    
    
    
    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
    print(result)
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3400Kここは一定にする
    Cp = nH2O*58.002 +  nH2*37.934 + nH*20.786 + nO2*40.549 + nO*21.058 + nOH*37.690
    
    #温度異存なし
    #noの標準生成エンタルピーは何？
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH



"""




#3300K
#結果はTw3532
#3400K
#結果はTw3285

#よって3300Kから3400Kまでの間に存在することが分かる。
#よって比熱とエンタルピーを線形補完して考える。
#このプログラムは3300Kから3400K専用


Kp1 = 0
Kp2 = 0
Kp3 = 0
Kp4 = 0
Pm = 20
nsum=1.1
result0 = 0


#自動化
def Tw(Tf0):
    
    #funk内で無理やり使うため
    global nsum,Pm, Kp1, Kp2, Kp3, Kp4,result0
        
    for i in range(100):
    
        #Tf0 = 3368
    
        

        
        #3350K
        Kp1 = 10 ** get_middle_value(xa=3300,ya=-0.543,xb=3500,yb=-0.31,xx=Tf0)
        Kp2 = 10 ** get_middle_value(xa=3300,ya=-0.439,xb=3500,yb=-0.231,xx=Tf0)
        Kp3 = 10 ** get_middle_value(xa=3300,ya=0.129,xb=3500,yb= 0.16,xx=Tf0)
        Kp4 = 10 ** get_middle_value(xa=3300,ya=0.942,xb=3500,yb=0.712,xx=Tf0)
        
        
        
        
        
        
        result0 = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
        #print(result0)
        
        
        nH2O, nH2, nH, nO2, nO, nOH = result0.x
        
        
        print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
        
        

        
        CpH2O = get_middle_value(xa=3300,ya=57.736,xb=3400,yb=58.002,xx=Tf0)
        CpH2 = get_middle_value(xa=3300,ya=37.728,xb=3400,yb=37.934,xx=Tf0)
        CpH = get_middle_value(xa=3300,ya=20.786,xb=3400,yb=20.786,xx=Tf0)
        CpO2 = get_middle_value(xa=3300,ya=40.549,xb=3400,yb=40.549,xx=Tf0)
        CpO = get_middle_value(xa=3300,ya=21.025,xb=3400,yb=21.058,xx=Tf0)
        CpOH = get_middle_value(xa=3300,ya=37.535,xb=3400,yb=37.690,xx=Tf0)


        #3300と3340から線形に
        Cp = nH2O*CpH2O +  nH2*CpH2 + nH*CpH + nO2*CpO2 + nO*CpO + nOH*CpOH

        #温度異存なし
        #noの標準生成エンタルピーは何？
        enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
        enth *=1000
        
        Tw = 298.16 -(enth/Cp)
        print("Tw" + str(Tw))
        
        

        
        
        #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
            #break
            
        nsum = nH2O +  nH2 + nH + nO2 + nO + nOH
    
    return Tf0-Tw



result = optimize.root(Tw, 3350,tol = 0.0000001)
print(result)






#ここまでは流入分の比熱を考えていない。
#が、今回はガスタービンエンジンではないので、問題なしとあとでわかった。
#---------------------------------------------------



"""

#流入分の比熱を考えていなかったので、3400~3500にあるっぽい



Kp1 = 0
Kp2 = 0
Kp3 = 0
Kp4 = 0
Pm = 20
nsum=1.1
result0 = 0


#自動化
def Tw(Tf0):
    
    #funk内で無理やり使うため
    global nsum,Pm, Kp1, Kp2, Kp3, Kp4,result0
        
    for i in range(10):
    
        #Tf0 = 3368
    
        
    
        
        #3350K
        Kp1 = 10 ** get_middle_value(xa=3400,ya=-0.423,xb=3500,yb=-0.423,xx=Tf0)
        Kp2 = 10 ** get_middle_value(xa=3400,ya=-0.332,xb=3500,yb=-0.332,xx=Tf0)
        Kp3 = 10 ** get_middle_value(xa=3400,ya=0.145,xb=3500,yb=0.145,xx=Tf0)
        Kp4 = 10 ** get_middle_value(xa=3400,ya=0.824,xb=3500,yb=0.824,xx=Tf0)
        
        
        
        
        
        
        result0 = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
        #print(result0)
        
        
        nH2O, nH2, nH, nO2, nO, nOH = result0.x
        
        
        print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
        
        #3500K
        Cp = nH2O*58.252 +  nH2*38.135 + nH*20.786 + nO2*40.904 + nO*21.094 + nOH*37.840

        
        CpH2O = get_middle_value(xa=3400,ya=58.002,xb=3500,yb=58.252,xx=Tf0)
        CpH2 = get_middle_value(xa=3400,ya=37.934,xb=3500,yb=38.135,xx=Tf0)
        CpH = get_middle_value(xa=3400,ya=20.786,xb=3500,yb=20.786,xx=Tf0)
        CpO2 = get_middle_value(xa=3400,ya=40.549,xb=3500,yb=40.904,xx=Tf0)
        CpO = get_middle_value(xa=3400,ya=21.058,xb=3500,yb=21.094,xx=Tf0)
        CpOH = get_middle_value(xa=3400,ya=37.690,xb=3500,yb=37.840,xx=Tf0)


        #3300と3340から線形に
        Cp = nH2O*CpH2O +  nH2*CpH2 + nH*CpH + nO2*CpO2 + nO*CpO + nOH*CpOH

        #温度異存なし
        #noの標準生成エンタルピーは何？
        enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
        enth *=1000
        
        #Tw = 298.16 -(enth/Cp)
        #print("Tw" + str(Tw))
        
        #ここへんこう
        cpin = 29.629*1 +33.745*0.5
        Tw = 298.16 -(enth/Cp) + cpin*(800-298.16)/Cp
        print("Tw" + str(Tw))
        
        
        #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
            #break
            
        nsum = nH2O +  nH2 + nH + nO2 + nO + nOH
    
    return Tf0-Tw



result = optimize.root(Tw, 3450,tol = 0.0000001)
print(result)

"""

"""


Tf0 = 4429.507526434881
nsum = 1.0135607700086877
Pm = 20
#4000
Kp1 = 10 ** 0.17
Kp2 = 10 ** 0.201
Kp3 = 10 ** 0.223
Kp4 = 10 ** 0.238






# 解きたい関数をリストで戻す
def func(x):
    nH2O, nH2, nH, nO2, nO, nOH = x    
    
    a = H_balance(nH2O, nH2, nH, nOH)
    b = O_balance(nH2O, nO2, nO, nOH)
    c = eq1(Kp1, Pm, nsum, nO, nO2)
    d = eq2(Kp2, Pm, nsum, nH, nH2)
    e = eq3(Kp3, Pm, nsum, nOH, nH2, nO2)
    f = eq4(Kp4, Pm, nsum, nH2O, nH2, nO2)


    return [a,b,c,d,e,f]


result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1],tol = 0.0000001)
print(result)


nH2O, nH2, nH, nO2, nO, nOH = result.x

print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))



#3000K
Cp = nH2O*56.823 +  nH2*37.078 + nH*20.786 + nO2*39.980 + nO*20.939 + nOH*37.038

#温度異存なし
enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
enth *=1000

Tw = 298.16 -(enth/Cp)
print("Tw" + str(Tw))

"""


"""
Cp =39*12.42

#温度異存なし
enth = -802.3
enth *=1000

Tw = 298.16 -(enth/Cp)
print("Tw" + str(Tw))



a = H_balance(nH2O, nH2, nH, nOH)
b = O_balance(nH2O, nO2, nO, nOH)
c = eq1(Kp1, Pm, nsum, nO, nO2)
d = eq2(Kp2, Pm, nsum, nH, nH2)
e = eq3(Kp3, Pm, nsum, nOH, nH2, nO2)
f = eq4(Kp4, Pm, nsum, nH2O, nH2, nO2)

print(a,b,c,d,e,f)


print("---------------")

nH2O, nH2, nH, nO2, nO, nOH = [0.749,0.159,0.057,0.049,0.026,0.127]
nsum= 1.167

a = H_balance(nH2O, nH2, nH, nOH)
b = O_balance(nH2O, nO2, nO, nOH)
c = eq1(Kp1, Pm, nsum, nO, nO2)
d = eq2(Kp2, Pm, nsum, nH, nH2)
e = eq3(Kp3, Pm, nsum, nOH, nH2, nO2)
f = eq4(Kp4, Pm, nsum, nH2O, nH2, nO2)

print(a,b,c,d,e,f)

"""



"""
#池下の条件




    
# 解きたい関数をリストで戻す
def func(x):
    global nsum,Pm, Kp1, Kp2, Kp3, Kp4
    print(nsum,Pm, Kp1, Kp2, Kp3, Kp4)
    print(nsum)
    nH2O, nH2, nH, nO2, nO, nOH = x    
    
    a = H_balance(nH2O, nH2, nH, nOH)
    b = O_balance(nH2O, nO2, nO, nOH)
    c = eq1(Kp1, Pm, nsum, nO, nO2)
    d = eq2(Kp2, Pm, nsum, nH, nH2)
    e = eq3(Kp3, Pm, nsum, nOH, nH2, nO2)
    f = eq4(Kp4, Pm, nsum, nH2O, nH2, nO2)
    return [a,b,c,d,e,f]



nsum = 1.1
for i in range(100):

    Tf0 = 3400
    
    Pm = 20
    #3000K
    Kp1 = 10 ** -0.31
    Kp2 = 10 ** -0.231
    Kp3 = 10 ** 0.16
    Kp4 = 10 ** 0.712
    

    
    

    
    
    result = optimize.root(func, [0.75, 0.15, 0.05, 0.05, 0.02, 0.1], method="hybr", jac = False, tol=0.001,options = {"maxfev":1000})
    
    print(result)
    #うまくいった　"df-sane" ただし誤差はまだ大きい。初期値依存か
    #初期値から更新されない"broyden1""broyden2" "anderson" "linearmixing""excitingmixing"
    #nan "diagbroyden"
    #その他　変な値に収束
    
    
    nH2O, nH2, nH, nO2, nO, nOH = result.x
    
    
    print("nsum =" + str( nH2O +  nH2 + nH + nO2 + nO + nOH))
    
    
    
    #3000K
    Cp = nH2O*56.823 +  nH2*37.078 + nH*20.786 + nO2*39.980 + nO*20.939 + nOH*37.038
    
    #温度異存なし
    enth = nH2O*-241.827 +  nH2*0 + nH*217.999 + nO2*0 + nO*249.17 + nOH*39.463
    enth *=1000
    
    Tw = 298.16 -(enth/Cp)
    print("Tw" + str(Tw))
    
    
    #if nsum-(nH2O +  nH2 + nH + nO2 + nO + nOH) <00000.1:
        #break
        
    nsum = nH2O +  nH2 + nH + nO2 + nO + nOH
"""