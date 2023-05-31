# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:56:01 2021

@author: yuki
"""


import numpy as np
from time import sleep
import pandas as pd





def get_sonic(gamma, R, T):
    return np.sqrt(gamma * R * T)




#(9.30)
def shock_wave_pressure(p2_p1, a1_a4, gamma1, gamma4, p4_p1):
    index = -2*gamma4/(gamma4-1)
    denominater = np.sqrt(2*gamma1* (2*gamma1 + (gamma1+1)*(p2_p1-1) ) )
    numerator = (gamma4-1) * a1_a4 * (p2_p1-1)
    y = p2_p1 * ((1- numerator/denominater) ** index)
    return p4_p1 -y


#(9.30)
def get_p2_p1(left, right, a1_a4, gamma1, gamma4, p4_p1):
    while True:
        #sleep(1)
        # 点$ (a,f(a)) $ と 点 $ (b,f(b)) $ を結ぶ直線と $ x $ 軸の交点
        c  = (left * shock_wave_pressure(right, a1_a4, gamma1, gamma4, p4_p1) - right * shock_wave_pressure(left, a1_a4, gamma1, gamma4, p4_p1)) / (shock_wave_pressure(right, a1_a4, gamma1, gamma4, p4_p1) - shock_wave_pressure(left, a1_a4, gamma1, gamma4, p4_p1))
        #print (c, c - math.sqrt(2))
        #print (c)
        #print(c)
        fc = shock_wave_pressure(c, a1_a4, gamma1, gamma4, p4_p1) 
        #print("sabunn" + str(fc))
        if (abs(fc) < 0.00000001):
            break

        if (fc< 0):
            # f(c) < 0 であれば, 解は区間 (c, b) の中に存在
            left = c
        else:
            # f(c) > 0 であれば, 解は区間 (a, c) の中に存在
            right = c
    print(c)
    return c




#(9.31)
def get_Ms(gamma1, p2_p1):
    Ms = (gamma1+1)/(2*gamma1)
    Ms *= p2_p1
    Ms += (gamma1-1)/(2*gamma1)
    Ms = np.sqrt(Ms)
    
    return Ms


#(4.42)より、上流のマッハ数、相対速度から実験室座標のm\sを求める
def MsR2vs(Ms, u1, a1):
    return Ms*a1 + u1

def MsL2vs(Ms, u1, a1):
    return u1 - Ms*a1


#(9.32)
def get_ro2_ro1(gamma1, p2_p1):
    a = (gamma1-1) / (gamma1+1)
    ro2_ro1 = (p2_p1+a) / (p2_p1*a + 1)
    return ro2_ro1



#(9.33)
def get_a2_a1(p2_p1, ro2_ro1):
    a2_a1 = (p2_p1**0.5) * (ro2_ro1**-0.5)
    return a2_a1


#(9.34)
def get_ro3_ro4(gamma4, p2_p4):
    ro3_ro4 = p2_p4**(1/gamma4)    
    return ro3_ro4


#(9.35)
def get_a3_a4(gamma4, p2_p4):
    a3_a4 = p2_p4**((gamma4-1)/(2*gamma4))    
    return a3_a4

#(9.27)
def get_u2(a1, p2_p1, gamma1):
    a = p2_p1 - 1
    b = 2/(gamma1*(gamma1+1))
    c = p2_p1 + (gamma1-1)/(gamma1+1)
    y = a1 * a * (b/c)**0.5
    return y
    

#(9.26)
def get_u3(a4, p3_p4, gamma4):
    a = 2*a4/(gamma4-1)
    index = (gamma4 -1)/(2*gamma4)
    b = 1-p3_p4**index
    y = a*b
    return y



#(9.41)
def get_p5_p2(gamma1, u2, a2):
    b = (gamma1+1)/4
    ua = u2/a2
    y = np.sqrt((b*ua)**2 +1)
    y += b*ua
    y *= ua*gamma1
    y +=1
    
    return y


#(9.42)
def get_Msr(gamma1, p5_p2):
    a = (gamma1+1)/(2*gamma1)
    b = (gamma1-1)/(2*gamma1)
    y = np.sqrt(a*p5_p2+b)
    return y



#(9.43)
def get_ro5_ro2(gamma1, p5_p2):
    b = (gamma1-1)/(gamma1+1)
    y = (p5_p2 + b) / (b*p5_p2 +1)
    return y



#(9.53)
def get_p8_p4(gamma4, M3):
    a = (gamma4-1)*M3/2
    index = 2*gamma4/(gamma4-1)
    y = ((1-a) / (1+a))**index
    return y



#(9.64)
def get_tX_tA(aX,aA, gamma4):
    index = gamma4+1
    index /= gamma4-1
    index /= -2
    
    return (aX/aA)**index







#応用


#イクスパンションと衝撃波の時
#(9.30)を参考に
def shock_wave_pressure2(p7_p3, a3, a5, gamma1, gamma4, p3_p5, u3, u5):
    index = gamma1-1
    index /= 2*gamma1
    
    y1 = p7_p3 -1
    y1 *=a3
    denominater = p7_p3 + ( (gamma4-1)/(gamma4+1) )
    numerator = 2/(gamma4*(gamma4+1))   

    
    y2 = np.sqrt(numerator/denominater)
    
    y3 = 2*a5/(gamma1-1)
    y3 *=( (p7_p3 * p3_p5) ** index ) -1
    
    y = u3 - y1 * y2 -u5 - y3
    return y
    
    
#(9.30)
def get_p7_p3(left, right, a3, a5, gamma1, gamma4, p3_p5, u3, u5):
    while True:
        #sleep(1)
        # 点$ (a,f(a)) $ と 点 $ (b,f(b)) $ を結ぶ直線と $ x $ 軸の交点
        c  = (left * shock_wave_pressure2(right, a3, a5, gamma1, gamma4, p3_p5, u3, u5) - right * shock_wave_pressure2(left, a3, a5, gamma1, gamma4, p3_p5, u3, u5)) / (shock_wave_pressure2(right, a3, a5, gamma1, gamma4, p3_p5, u3, u5) - shock_wave_pressure2(left, a3, a5, gamma1, gamma4, p3_p5, u3, u5))
        #print (c, c - math.sqrt(2))
        #print (c)
        #print(c)
        fc = shock_wave_pressure2(c,  a3, a5, gamma1, gamma4, p3_p5, u3, u5) 
        #print("sabunn" + str(fc))
        if (abs(fc) < 0.00000001):
            break

        if (fc< 0):
            # f(c) < 0 であれば, 解は区間 (c, b) の中に存在
            left = c
        else:
            # f(c) > 0 であれば, 解は区間 (a, c) の中に存在
            right = c
    print(c)
    return c    
    






#衝撃波と衝撃波の時



#(9.30)を参考に
def shock_wave_pressure3(p7_p3, a3, a5, gamma1, gamma4, p3_p5, u3, u5):

    
    y1 = p7_p3 -1
    y1 *=a3
    denominater = p7_p3 + ( (gamma4-1)/(gamma4+1) )
    numerator = 2/(gamma4*(gamma4+1))   
    y2 = np.sqrt(numerator/denominater)
    y3 = y1*y2
    
    z1 = p7_p3*p3_p5 -1
    z1 *=a5
    denominater2 = p7_p3*p3_p5 + ( (gamma1-1)/(gamma1+1) )
    numerator2 = 2/(gamma1*(gamma1+1))   
    z2 = np.sqrt(numerator2/denominater2)
    z3 = z1*z2
    
    y = u3 - y3 -u5 - z3
    return y
    
    
#(9.30)
def get_p7_p3_2nd(left, right, a3, a5, gamma1, gamma4, p3_p5, u3, u5):
    while True:
        #sleep(1)
        # 点$ (a,f(a)) $ と 点 $ (b,f(b)) $ を結ぶ直線と $ x $ 軸の交点
        c  = (left * shock_wave_pressure3(right, a3, a5, gamma1, gamma4, p3_p5, u3, u5) - right * shock_wave_pressure3(left, a3, a5, gamma1, gamma4, p3_p5, u3, u5)) / (shock_wave_pressure3(right, a3, a5, gamma1, gamma4, p3_p5, u3, u5) - shock_wave_pressure3(left, a3, a5, gamma1, gamma4, p3_p5, u3, u5))
        #print (c, c - math.sqrt(2))
        #print (c)
        #print(c)
        fc = shock_wave_pressure3(c,  a3, a5, gamma1, gamma4, p3_p5, u3, u5) 
        #print("sabunn" + str(fc))
        if (abs(fc) < 0.00000001):
            break

        if (fc< 0):
            # f(c) < 0 であれば, 解は区間 (c, b) の中に存在
            left = c
        else:
            # f(c) > 0 であれば, 解は区間 (a, c) の中に存在
            right = c
    print(c)
    return c    




def clear_extra(data, min_value, max_value):
    for i in range(len(data)):
        if data[i]> max_value:
            data[i] = np.nan
        if data[i]< min_value:
            data[i] = np.nan
























#左


#宮川
p4 = 4*1000000 #各自
T4 = 864 #各自
Ar = 40 #各自
gamma4 = 1.67 #各自

"""
#田中
p4 = 3*1000000 #各自
T4 = 432 #各自
Ar = 40 #各自
gamma4 = 1.67 #各自
"""



"""
#池下
p4 = 4*1000000 #各自
T4 = 360 #各自
Ar = 29 #各自
gamma4 = 1.4 #各自
"""

"""
#杉浦
p4 = 3.5*1000000 #各自
T4 = 288 #各自
Ar = 4 #各自
gamma4 = 1.67 #各自
"""

"""
#教科書
p4 = 1*100000 #各自
T4 = 290 #各自
Ar = 4 #各自
gamma4 = 1.67 #各自
"""

L4 = 2
u4 = 0
R4 = 8.31 / (Ar*0.001)
ro4 = p4/(R4*T4)
a4 = get_sonic(gamma4, R4, T4)




#右
p1 = 100000
T1 = 288
L1 = 4
Air = 29
gamma1 = 1.4
u1 = 0
R1 = 8.31 / (Air*0.001)
ro1 = p1/(R1*T1)
a1 = get_sonic(gamma1, R1, T1)
 




p2_p1 = get_p2_p1(left=5.8, right=6, a1_a4=a1/a4, gamma1=gamma1, gamma4=gamma4, p4_p1=p4/p1)
#上流に対する相対速度
Ms = get_Ms(gamma1, p2_p1)
#実験室座標のm\s
vs1 = MsR2vs(Ms, u1, a1)
ro2_ro1 = get_ro2_ro1(gamma1, p2_p1)
a2_a1 = get_a2_a1(p2_p1, ro2_ro1)
ro3_ro4 = get_ro3_ro4(gamma4, p2_p1*p1/p4)
a3_a4 = get_a3_a4(gamma4, p2_p1*p1/p4)






p3 = (ro3_ro4**gamma4)*p4 #(9.34)
R3 = 8.31 / (Ar*0.001)
ro3 = ro3_ro4 * ro4
u3 = get_u3(a4 = a4, p3_p4=p3/p4, gamma4=gamma4)
T3 = p3/(ro3*R3)
a3 = get_sonic(gamma4, R3, T3)






p2 = p3 #(9.28) 
R2 = 8.31 / (Air*0.001)
ro2 = ro2_ro1 * ro1
T2 = p2/(ro2*R2)
a2 = a1*a2_a1
u2 = get_u2(a1, p2_p1, gamma1)





p5_p2 = get_p5_p2(gamma1, u2, a2)
p5 = p2 * p5_p2
#上流に対する相対速度
Msr = get_Msr(gamma1, p5_p2)
ro5_ro2 = get_ro5_ro2(gamma1, p5_p2)
ro5 = ro2*ro5_ro2
R5 = R1
T5 = p5/(ro5*R5)
a5_a2 = (T5/T2)**0.5 #(9.44)
a5 = a2 * a5_a2
u5 = 0
#実験室座標のm\s
vs2 = MsL2vs(Msr, u2, a2)


p8_p4 = get_p8_p4(gamma4, M3=u3/a3)
p8 = p8_p4*p4
ro8_ro4 = p8_p4**(1/gamma4) #9.54
ro8 = ro8_ro4 * ro4
R8 = R4
T8 = p8/(ro8*R8)
u8 = 0
a8 = np.sqrt(gamma4*R8*T8)








#左側のイクスパンションファンの内部について

n =10
c_R = [["nan" for i in range(n+1)] for j in range(n+1)]
cplusL= [["nan" for i in range(n+1)] for j in range(n+1)]
u= [["nan" for i in range(n+1)] for j in range(n+1)]
a= [["nan" for i in range(n+1)] for j in range(n+1)]
J_minus = ["nan" for i in range(n+1)] 
J_plus = ["nan" for i in range(n+1)]
x_cross =  [["nan" for i in range(n+1)] for j in range(n+1)]
t_cross =  [["nan" for i in range(n+1)] for j in range(n+1)]



#(10.38)~
for i in range(1,n+1):
    c_R[i][0] = -a4+(u3-a3+a4)*(i-1)/(n-1)
    a[i][0] = -(gamma4-1)*c_R[i][0]/(gamma4+1) + 2*a4/(gamma4+1)
    u[i][0] = 2*c_R[i][0]/(gamma4+1) + 2*a4/(gamma4+1)
    J_minus[i] = 4*c_R[i][0]/(gamma4+1) + 2*(gamma4-3)*a4/((gamma4+1)*(gamma4-1))
    u[i][i]=0 #(10.45)
    a[i][i] = -(gamma4-1)*J_minus[i]/2
    J_plus[i] = 2*a[i][i]/(gamma4-1)
    cplusL[i][i] = a[i][i] #リストのコピーに注意
    c_R[i][i] = -a[i][i] #リストのコピーに注意
    
    
    #オリジナル
    t_cross[i][0] = 0
    x_cross[i][0] = 0
    x_cross[i][i] = -L4
    
    


#(50.53~)
for j in range(1,n+1):
    for i in range(j+1,n+1):
       a[i][j] = (gamma4-1)*(J_plus[j] - J_minus[i])/4
       u[i][j] = (J_plus[j] + J_minus[i])/2


#教科書間違い
#c_R(i,i)求めていない
#(10.53)(10.54)ではアルゴリズム足りないので(ij)に変更

for j in range(1,n+1):
    for i in range(j+1,n+1):
       cplusL[i][j] = u[i][j] + a[i][j]
       c_R[i][j] = u[i][j] - a[i][j]


#(10.55)
#オリジナル
#漸化式的に交点を求める

for j in range(1,n+1):
    t_cross[j][j] =  t_cross[j][j-1] - (x_cross[j][j-1] + L4)/c_R[j][j-1]
    for i in range(j+1,n+1):
        t_cross[i][j] = (x_cross[i][j-1] - x_cross[i-1][j] + cplusL[i-1][j]*t_cross[i-1][j] -c_R[i][j-1]*t_cross[i][j-1])/(cplusL[i-1][j] - c_R[i][j-1])
        x_cross[i][j] = x_cross[i][j-1] +c_R[i][j-1] * (t_cross[i][j] - t_cross[i][j-1])
        print(i,j)





"""
#ミックスでテストしたが、色分けできないので却下
mixed = []
for j in range(1,n+1):
    for i in range(j+1,n+1):
        mixed.append([x_cross[i][j], t_cross[i][j]]) 
aaa = pd.DataFrame(mixed, columns=["x", "t"])
aaa.plot.scatter(x="x",y = "t", xlim=[-L4, L1], ylim=[0,0.02])

"""


#expanshon fanのi番目の点を保存
ex_line = [[] for j in range(n+1)]
#無理やりそれぞれのラインの要素を追加
for i in range(n+1):
    for j in range(n+1):
        print(i,j)
        try:
            if x_cross[i][j] != "nan":
                ex_line[i].append([x_cross[i][j], t_cross[i][j]]) 
        except:
            pass
for i in range(n+1):
    for j in range(n+1):
        print(i,j)
        try:
            if x_cross[j][i] != "nan":
                ex_line[i].append([x_cross[j][i], t_cross[j][i]]) 
        except:
            pass

"""
#左端が重複するので削除,なくてもよさそう
#https://note.nkmk.me/python-list-unique-duplicate/
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

for i in range(1, n+1):
    ex_line[i] = get_unique_list(ex_line[i])
"""





#cccは統合後
inner_expansion_fan = pd.DataFrame([0], columns=["x"]) 
for i in range(1,n+1):  
    label = "ex" + str(i)
    each_expansion_fan = pd.DataFrame(ex_line[i], columns=["x", label])
    
    #交点から先
    x = np.linspace(x_cross[-1][i], L1, 100)
    exi = t_cross[-1][i] +  (x-x_cross[-1][i])/cplusL[-1][i]
    each_expansion_fan= each_expansion_fan.append(pd.DataFrame({"x":x, label:exi}))
    
    
    #bbb.plot(x="x", xlim=[-L4, L1], ylim=[0,0.01])
    #交点ににおいてmerge時に順番が飛び、うまく書けない
    #ccc = pd.merge(ccc,bbb, on="x", how='outer')
    #下につなげるだけでうまくいく
    inner_expansion_fan = inner_expansion_fan.append(each_expansion_fan)
    
    

#ccc= ccc.sort_values("x")
#ccc.plot(x="x", xlim=[-L4, L1], ylim=[0,0.02])
#ccc.plot.scatter(x="x", y="ex1", xlim=[-L4, L1], ylim=[0,0.01])
#ccc.plot(x="x", y="ex3", xlim=[-L4, L1], ylim=[0,0.02])
    






#(9.73)
acimp3 = ro3*a3
acimp2 = ro2*a2


if acimp3 > acimp2:
    print("低いほうから高いほうです、つまり衝撃波です")

    #7について
    p3_p5=p3/p5
    p7_p3 = get_p7_p3_2nd(5, 10, a3, a5, gamma1, gamma4, p3_p5, u3, u5) #
    



#共通

    
    
    
    p7 = p7_p3 * p3
    
    Ms3 = get_Ms(gamma4, p7_p3)
    ro7_ro3 = get_ro2_ro1(gamma4, p7_p3)
    ro7 = ro7_ro3 * ro3
    T7 = p7/(ro7*R4)
    a7_a3 = get_a2_a1(p7_p3, ro7_ro3)
    a7 = a3* a7_a3
    #(9.27)
    u7 = u3 - get_u2(a3, p7_p3, gamma4)
    vs3 = MsL2vs(Ms3, u3, a3)
    R7 = R4
    
    #6について
    #7と同じような方法
    u6 = u7
    p6 = p7
    R6 = R1
    ro6_ro5 = get_ro2_ro1(gamma1, p6/p5)
    ro6 = ro6_ro5 * ro5
    T6 = p6/(ro6*R6)
    a6 = get_sonic(gamma1, R6, T6)
    
 
    
#共通 
    
 
    #ここ
    Ms4 = get_Ms(gamma1, p6/p5)
    vs4 = MsR2vs(Ms4, u5, a5)
    
    
    
    
    
    
    
    




    x = np.linspace(-L4, L1, 10000)

    swi_line = x/vs1
    contact_surface23 = x/u3
    expL_line = x/-a4
    expR_line = x/(u3-a3) #p166
    swr_line = swi_line[-1] - (L1-x)/vs2

    #567の場所
    contact_sw_refre_x = (L1*u3 - u3*vs2*swi_line[-1]) / (u3-vs2)
    contact_sw_refre_t = contact_sw_refre_x / u3
    

    
    sw3 = (x-contact_sw_refre_x)/vs3 + contact_sw_refre_t
    sw4 = (x-contact_sw_refre_x)/vs4 + contact_sw_refre_t
    contact_surface67 = (x-contact_sw_refre_x)/u7 + contact_sw_refre_t



    clear_extra(swi_line, 0, 100)
    clear_extra(contact_surface23, min_value=0, max_value=contact_sw_refre_t)
    clear_extra(expL_line, 0, 100)
    clear_extra(expR_line, 0, 100)
    clear_extra(swr_line, min_value=0, max_value=contact_sw_refre_t)
    clear_extra(sw3, min_value=contact_sw_refre_t, max_value=100)
    clear_extra(sw4, min_value=contact_sw_refre_t, max_value=100)
    clear_extra(contact_surface67, min_value=contact_sw_refre_t, max_value=100)






    tA = L4/a4
    tB_tA = get_tX_tA(a3,a4, gamma4)
    tB = tA * tB_tA
    xB = tB*(u3-a3)
    tD = 2*tB
    xm = tD * u3
    valid_test_t = sw4[-1] - swi_line[-1]

    #理論値(図9.16)
    ref_ex_head = tB + (tD-tB)*(x-xB)/(xm-xB)
    clear_extra(ref_ex_head, min_value=tB, max_value=1)
    
 
    
    print("n=" + str(n))
    print("イクスパンションファンの先頭が抜ける時間は、")
    print("理論値")
    print(tB)
    print("折れ曲がったやつでは")
    #作成時に一行多いので
    print(inner_expansion_fan.iloc[n+2, 1])
        
    
    
    #エクスパンションの左右は折れ曲がるので削除、テストも削除、
    df = pd.DataFrame({
        "x" : x,
        "swi_line" : swi_line ,
        "contact_surface23" : contact_surface23,    
        "swr_line" : swr_line,
        "sw3" : sw3,
        "sw4":sw4,
        "contact_surface67":contact_surface67,
        "ref_ex_head" : ref_ex_head,
    })
    
    df = df.append(inner_expansion_fan)
    #https://own-search-and-study.xyz/2016/08/03/pandas%E3%81%AEplot%E3%81%AE%E5%85%A8%E5%BC%95%E6%95%B0%E3%82%92%E4%BD%BF%E3%81%84%E3%81%93%E3%81%AA%E3%81%99/
    df.plot(x="x",xlim=[-L4, L1], ylim=[0,0.014], figsize=(10, 10), legend = False)
    df.plot(x="x",xlim=[-L4, L1], ylim=[0,0.014], figsize=(10, 10), legend = True, style=[':'],lw=10)
    img = df.plot(x="x",xlim=[-L4, L1], ylim=[0,0.014], figsize=(10, 10), legend = False).get_figure()
    img.savefig("img")
    
    
    
    
    
    
    
    
    
    
    
    
    #axのテスト
    dfsw = pd.DataFrame({
        "x" : x,
        "swi_line" : swi_line ,  
        "swr_line" : swr_line,
        "sw3" : sw3,
        "sw4":sw4,
    })
    
    dfcontact = pd.DataFrame({
        "x" : x,
        "contact_surface23" : contact_surface23,    
        "contact_surface67":contact_surface67,
    })
    
    
    inner_expansion_fan = inner_expansion_fan.append(pd.DataFrame({
            "x" : x,
            "ref_ex_head" : ref_ex_head,
        }))
    

    axsw = dfsw.plot(x="x",lw=5, legend = False,)
    ax2 = dfcontact.plot(x="x", style=[':',':'],ax =axsw, legend = False,)
    inner_expansion_fan.plot(x="x",xlim=[-L4, L1], ylim=[0,0.014], figsize=(10, 10), legend = False, ax =ax2, xlabel="x [m]", ylabel="t [s]", title="shock tube" )




    
    
else:
    print("高いほうから低いほうです、つまりイクスパンションファンです")
    #7について
    p3_p5=p3/p5
    #(9.30)を
    p7_p3 = get_p7_p3(5, 10, a3, a5, gamma1, gamma4, p3_p5, u3, u5)
    p7 = p7_p3 * p3
    Ms3 = get_Ms(gamma4, p7_p3)
    ro7_ro3 = get_ro2_ro1(gamma4, p7_p3)
    ro7 = ro7_ro3 * ro3
    T7 = p7/(ro7*R4)
    a7_a3 = get_a2_a1(p7_p3, ro7_ro3)
    a7 = a3* a7_a3
    #(9.27)
    u7 = u3 - get_u2(a3, p7_p3, gamma4)
    vs3 = MsL2vs(Ms3, u3, a3)
    R7 = R4




    #6について
    u6 = u7
    p6 = p7
    R6 = R1
    ro6_ro5 = (p6/p5)**(1/gamma1) #(9.12)
    ro6 = ro6_ro5 * ro5
    T6 = p6/(ro6*R6)
    a6 = get_sonic(gamma1, R6, T6)



    tA = L4/a4
    tB_tA = get_tX_tA(a3,a4, gamma4)
    tB = tA * tB_tA
    xB = tB*(u3-a3)
    tD = 2*tB
    xm = tD * u3










    x = np.linspace(-L4, L1, 1000)

    swi_line = x/vs1
    contact_surface23 = x/u3
    expL_line = x/-a4
    expR_line = x/(u3-a3) #p166
    swr_line = swi_line[-1] - (L1-x)/vs2

    #567の場所
    contact_sw_refre_x = (L1*u3 - u3*vs2*swi_line[-1]) / (u3-vs2)
    contact_sw_refre_t = contact_sw_refre_x / u3
    
    sw3 = (x-contact_sw_refre_x)/vs3 + contact_sw_refre_t
    contact_surface67 = (x-contact_sw_refre_x)/u7 + contact_sw_refre_t

    #佐宗先生のメールの結果、右に進むものはc+で考えている。
    expR2_line = (x-contact_sw_refre_x)/(u5+a5) + contact_sw_refre_t
    expL2_line = (x-contact_sw_refre_x)/(u6+a6) + contact_sw_refre_t


    ref_ex_head = tB + (tD-tB)*(x-xB)/(xm-xB)
    clear_extra(ref_ex_head, min_value=tB, max_value=1)
    
    
    
    clear_extra(swi_line, 0, 100)
    clear_extra(contact_surface23, min_value=0, max_value=contact_sw_refre_t)
    clear_extra(expL_line, 0, 100)
    clear_extra(expR_line, 0, 100)
    clear_extra(swr_line, min_value=0, max_value=contact_sw_refre_t)
    clear_extra(sw3, min_value=contact_sw_refre_t, max_value=100)
    clear_extra(expR2_line, min_value=contact_sw_refre_t, max_value=100)
    clear_extra(expL2_line, min_value=contact_sw_refre_t, max_value=100)
    clear_extra(contact_surface67, min_value=contact_sw_refre_t, max_value=100)
    
    

    df = pd.DataFrame({
        "x" : x,
        "swi_line" : swi_line ,
        "contact_surface23" : contact_surface23,    
        #"expL_line" : expL_line,
        #"expR_line" : expR_line,
        "swr_line" : swr_line,
        "sw3" : sw3,
        "contact_surface67": contact_surface67,
        "expL2_line" : expL2_line,
        "expR2_line" : expR2_line,
        "ref_ex_head" : ref_ex_head
    })


    df.plot()
    df.plot(x="x")
    df.plot(x="x",xlim=[-L4, L1], ylim=[0,0.03])
    #df.to_excel('圧縮レポート9_0.xlsx')





    df = df.append(inner_expansion_fan)
    #https://own-search-and-study.xyz/2016/08/03/pandas%E3%81%AEplot%E3%81%AE%E5%85%A8%E5%BC%95%E6%95%B0%E3%82%92%E4%BD%BF%E3%81%84%E3%81%93%E3%81%AA%E3%81%99/
    df.plot(x="x",xlim=[-L4, L1], ylim=[0,0.014], figsize=(10, 10), legend = True)
    #img = df.plot(x="x",xlim=[-L4, L1], ylim=[0,0.014], figsize=(10, 10), legend = False).get_figure()
    #img.savefig("img")












#1番の量の表

fluid_property = pd.DataFrame(
    data = np.array([[p1,ro1,T1,u1, a1],
                   [p2,ro2,T2,u2, a2],
                   [p3,ro3,T3,u3, a3],
                   [p4,ro4,T4,u4, a4],
                   [p5,ro5,T5,u5, a5],
                   [p6,ro6,T6,u6, a6],
                   [p7,ro7,T7,u7, a7],
                   [p8,ro8,T8,u8, a8]]),
    index = [1,2,3,4,5,6,7,8],
    columns = ["圧力[Pa]", "密度[kg/m^3]", "温度[K]", "流速[m/s]", "音速[m/s]"]
    )

print(fluid_property)