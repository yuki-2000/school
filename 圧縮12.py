# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:20:53 2021

@author: yuki
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import pandas as pd


#宮川
Mi = 0.55
Me = 3.3



#池下
Mi = 0.3
Me = 3

"""
#田中
Mi = 0.5
Me = 2.4
"""

gamma = 1.4
y0 =1

#適当に決めた
#長すぎるとどうやら最初の反射波が膨張部にあたってしまうみたいだ。
xa =0.5
#分割数
n =9





#p113
#rad
def nu(M):
    global gamma
    #mm = M*M
    #y = (np.sqrt((gamma+1)/(gamma-1)))  *   (np.arctan(np.sqrt(((gamma-1)*(M*M-1))/(gamma+1))))  -   (np.arctan(np.sqrt(M*M-1)))
    y = np.sqrt((gamma+1)/(gamma-1))
    y *=   np.arctan(  np.sqrt(  ((gamma-1)*(M*M-1)) / (gamma+1)  )  )
    y -=   np.arctan(  np.sqrt(M*M-1)  )
    #print(y)
    return y



#差をとって0に持っていくよう
def get_M_from_nu(input_M, goal_nu):
    return goal_nu - nu(input_M)


print(nu(Me)/2)
print(np.rad2deg(nu(Me)/2))
#陽的に求まる
theta_max=np.rad2deg(nu(Me)/2)
theta_max_rad = np.deg2rad(theta_max)



#断面積比

def outer_area(y0, Me, gamma):
    index = (gamma+1) / (2*(gamma-1))
    a = (gamma-1)*(Me**2) + 2
    a/=gamma+1
    
    ye = a**index
    ye*=y0/Me
    return ye


def getM_from_y(Me,y):
    global y0,gamma
    return outer_area(y0, Me, gamma) - y





#マッハ数と高さののグラフ化
MMMM = np.linspace(0, 2, 100)
yyyy = outer_area(y0, MMMM, gamma)
plt.plot(MMMM, yyyy)
plt.title("yyyy")
plt.show()






#(10.32)
#3次関数
#theta_maxのみdeg
def throat(y0, xa, theta_max, x):
    y = (x/xa)**2 -((x/xa)**3)/3
    y *= np.tan(np.deg2rad(theta_max))
    y *= xa
    y += y0
    
    return y



def get_throat_x_from_y(x,y):
    global y0, xa, theta_max
    return throat(y0, xa, theta_max, x) -y



#出口の高さ
ye = outer_area(y0, Me, gamma)
#入り口の高さ
yi = outer_area(y0, Mi, gamma)
xi = optimize.bisect(get_throat_x_from_y, -10, 0, args=(yi))






#rad
#3次関数を直線近似するときの角度
def get_theta(xl, xr):
    global y0, xa, theta_max
    
    yl = throat(y0, xa, theta_max, xl)
    yr = throat(y0, xa, theta_max, xr)
    
    theta = np.arctan((yr-yl)/(xr-xl))
    #theta = np.rad2deg(theta)
    
    return theta






#nuのグラフ化
xx = np.linspace(1, 30, 100)
nu_test = nu(xx)
plt.plot(xx, nu_test)
plt.title("nu")
plt.show()


#betaのグラフ化
xx = np.linspace(1, 3.3, 100)
nu_test = np.arcsin(1/xx)
plt.plot(xx, nu_test)
plt.title("beta")
plt.show()








#5番
#膨張部をn本で近似して壁角度を求める


#n本で区切ったらn+1この領域
x = np.linspace(0, xa, n)
x_smooth=np.linspace(0, xa, 10000)
#ノズル形状の図示
y_nozzle = throat(y0, xa, theta_max, x)
y_nozzle_smooth = throat(y0, xa, theta_max, x_smooth)

plt.plot(x, y_nozzle, '-o')
plt.plot(x_smooth, y_nozzle_smooth)
#plt.axis([0, xa, 0, 1.5])
plt.show()



theta_area = [["nan" for j in range(n+2)] for i in range(n+2)]
#スローとではまっすぐ
theta_area[1][1] = 0
#壁面は直線近似、壁面での領域は流れの方向も平行
#(10.24)
for i in range(2,n+1):
    theta_area[i][1] = get_theta(xl = x[i-1], xr = x[i-2])

theta_area[n+1][1] = np.deg2rad(theta_max)









#6番
#nuとthetaの内部での値を求める
#(10.24)(10.25)
nu_area =  [["nan" for j in range(n+2)] for i in range(n+2)]
for i in range(1,n+1):
    for j in range(1,i+1):
        #(10.24)
        nu_area[i][j] = theta_area[i][1] + theta_area[j][1]
        theta_area[i][j] = theta_area[i][1] - theta_area[j][1]










#7番
#相殺部の設計
#図10.3より
#n+1分割したとして求めた角度
nu_area[n+1][1] = theta_area[n+1][1] + theta_area[1][1]



#教科書の番号のつけ方間違っている


for j in range(2, n+2):
    #(10.24)(10.25)
    nu_area[n+1][j] = theta_area[n+1][1] + theta_area[j][1]
    theta_area[n+1][j] = theta_area[n+1][1] - theta_area[j][1]
    
    #(10.3)(10.4)
    #j=nまで子か計算できない
    #nu_area[n+1][j] = (nu_area[n+1][j-1] + nu_area[n][j] + theta_area[n+1][j-1] - theta_area[n][j])/2
    #theta_area[n+1][j] = (nu_area[n+1][j-1] - nu_area[n][j] + theta_area[n+1][j-1] + theta_area[n][j])/2




print(theta_max_rad)
print(theta_area[n+1][1])







#8番
#交点を求めていく

#角度を求めるのに必要な状態を求める
M_area = [["nan" for j in range(n+2)] for i in range(n+2)]
#rad
beta_area = [["nan" for j in range(n+2)] for i in range(n+2)]


#p115,p178,180
#イクスパンションファン近似の二等分時にわざわざc_は求めなくてもよい。図10.3に従えばよし

for i in range(1,n+2):
    for j in range(1,i+1):
        #p115
        #https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html
        M_area[i][j] = optimize.bisect(get_M_from_nu, 1, 50, args=(nu_area[i][j]))
        #p180
        beta_area[i][j] = np.arcsin(1/M_area[i][j])




print("目標出口マッハ数は"+str(Me))
print("今回の結果" + str(M_area[n+1][n+1]))
print("θmaxにより変動")








#p185に倣って番号をつける
#lineについてはrad、交点(i,j)に向かう線を[i][j]とした。        
       
expi_line_rad= [["nan" for j in range(n+2)] for i in range(n+2)]
expr_line_rad= [["nan" for j in range(n+2)] for i in range(n+2)]
cross_point_x= [["nan" for j in range(n+2)] for i in range(n+2)]
cross_point_y= [["nan" for j in range(n+2)] for i in range(n+2)]


for i in range(1,n+1):
    for j in range(1,i+1):
        expi_line_rad[i][j] = (theta_area[i][j] + theta_area[i+1][j] -beta_area[i][j] -beta_area[i+1][j])/2
        
for i in range(2,n+2):
    for j in range(1,i):
        expr_line_rad[i][j] = (theta_area[i][j] + theta_area[i][j+1] + beta_area[i][j] + beta_area[i][j+1])/2



for i in range(1,n+1):
    #壁側の座標
    cross_point_x[i][0]= x[i-1]
    cross_point_y[i][0]= throat(y0, xa, theta_max, cross_point_x[i][0])
    #中心の座標
    cross_point_y[i][i] = 0

for i in range(1,n+1):
    for j in range(1,i+1):
        if i == j:
            cross_point_x[i][j] = cross_point_x[i][j-1] - cross_point_y[i][j-1]/np.tan(expi_line_rad[i][j])
        else:
            numerator = cross_point_y[i][j-1] - cross_point_y[i-1][j] - cross_point_x[i][j-1]*np.tan(expi_line_rad[i][j]) + cross_point_x[i-1][j]*np.tan(expr_line_rad[i][j])
            denominator = np.tan(expr_line_rad[i][j]) - np.tan(expi_line_rad[i][j])
            cross_point_x[i][j] = numerator/denominator
            cross_point_y[i][j] = cross_point_y[i][j-1] + (cross_point_x[i][j]-cross_point_x[i][j-1])*np.tan(expi_line_rad[i][j])
            





cross_point_x[n+1][0] = xa
ya = throat(y0, xa, theta_max, xa)
cross_point_y[n+1][0] = ya

for j in range(1,n+1):
    numerator = cross_point_y[n+1][j-1] - cross_point_y[n][j] - cross_point_x[n+1][j-1]*np.tan(theta_area[n+1][j]) + cross_point_x[n][j]*np.tan(expr_line_rad[n+1][j])
    denominator = np.tan(expr_line_rad[n+1][j]) - np.tan(theta_area[n+1][j])
    cross_point_x[n+1][j] = numerator/denominator
    cross_point_y[n+1][j] = cross_point_y[n+1][j-1] + (cross_point_x[n+1][j]-cross_point_x[n+1][j-1])*np.tan(theta_area[n+1][j])






#交点が全部わかったので図示してみる、ただし順番適当

xxx, yyy = np.array(cross_point_x).reshape(-1, 1), np.array(cross_point_y).reshape(-1, 1)
xxx = [float(s[0]) for s in xxx if s != 'nan']
yyy = [float(s[0]) for s in yyy if s != 'nan']

plt.scatter(xxx,yyy)
plt.show()
plt.plot(xxx,yyy, '-o')
plt.show()



















#交点が全部わかったので図示してみる

#expanshon fanのi番目の点を保存
ex_line = [[] for j in range(n+1)]
#無理やりそれぞれのラインの要素を追加

for i in range(1,n+1):
    for j in range(0,i+1):
        if cross_point_x[i][j] != "nan":
            ex_line[i].append([cross_point_x[i][j], cross_point_y[i][j]]) 

for i in range(1,n+1):
    for j in range(1,n+2):
        if cross_point_x[j][i] != "nan":
            ex_line[i].append([cross_point_x[j][i], cross_point_y[j][i]]) 
     
        
inner_expansion_fan = pd.DataFrame([0], columns=["x"]) 
for i in range(1,n+1):  
    label = "ex" + str(i)
    each_expansion_fan = pd.DataFrame(ex_line[i], columns=["x", label])
    inner_expansion_fan = inner_expansion_fan.append(each_expansion_fan)





#壁について


#スロート以前
x_wall_minus = np.linspace(xi, 0, 100)
y_wall_minus = throat(y0, xa, theta_max, x_wall_minus)

wall = []
for i,j in zip(x_wall_minus, y_wall_minus):
    wall.append([i,j])



for i in range(1,n+1):
        if cross_point_x[i][0] != "nan":
            wall.append([cross_point_x[i][0], cross_point_y[i][0]]) 
            
for i in range(1,n+1):
        if cross_point_x[n+1][i] != "nan":
            wall.append([cross_point_x[n+1][i], cross_point_y[n+1][i]])        

inner_expansion_fan = inner_expansion_fan.append(pd.DataFrame(wall, columns=["x", "wall"]))
 




#中心軸について
xe = cross_point_x[n+1][n]


central_axis = []
central_axis.append([xi,0])
central_axis.append([xe,0])



inner_expansion_fan = inner_expansion_fan.append(pd.DataFrame(central_axis, columns=["x", "central_axis"]))



#inner_expansion_fan.plot(x="x")      
#inner_expansion_fan.plot(x="x", legend = False)    

img = inner_expansion_fan.plot(x="x", ylim=[0,6], figsize=(15, 10), legend = False,  xlabel="x [m]", ylabel="y [m]", title="Laval nozzle n={}".format(n),lw=1,style='o-').get_figure() 
img = inner_expansion_fan.plot(x="x", ylim=[0,6], figsize=(15, 10), legend = False,  xlabel="x [m]", ylabel="y [m]", title="Laval nozzle n={}".format(n),lw=1).get_figure()         
img = inner_expansion_fan.plot(x="x", ylim=[0,6], figsize=(15, 10), legend = False,  xlabel="x [m]", ylabel="y [m]", title="Laval nozzle n={}".format(n),lw=1, color ="k").get_figure()   



print("出口高さについて")
print(ye)
print(cross_point_y[n+1][n])























color_Mmax = Me
color_Mmin = Mi

#color_Mmax = 4
#color_Mmin = 0



#マッハ数を塗ってみる
#ここを引きずってしまっている
#img = inner_expansion_fan.plot(x="x", ylim=[0,6], figsize=(15, 10), legend = False,  xlabel="x [m]", ylabel="x [m]", title="Laval nozzle n={}".format(n),lw=1).get_figure()   


import matplotlib.cm as cm
#マッハ数変化
#https://cranethree.hatenablog.com/entry/2015/07/25/204608
#https://qiita.com/hokekiyoo/items/cea310b2c36a01b970a6




#スロ―ト以前
for i in range(len(x_wall_minus)-1):
       
    testx = [x_wall_minus[i], x_wall_minus[i+1], x_wall_minus[i+1], x_wall_minus[i]]
    testy = [0, 0, y_wall_minus[i+1], y_wall_minus[i]]
    MM = optimize.bisect(getM_from_y, 0.1, 0.999, args=(y_wall_minus[i]))
    plt.fill(testx,testy,color=cm.jet((MM-color_Mmin)/(color_Mmax-color_Mmin)))



#四角形
for i in range(2,n+2):
    for j in range(1,i):

        testx = [cross_point_x[i-1][j-1], cross_point_x[i-1][j], cross_point_x[i][j], cross_point_x[i][j-1]]
        testy = [cross_point_y[i-1][j-1], cross_point_y[i-1][j], cross_point_y[i][j], cross_point_y[i][j-1]]
        #plt.fill(testx,testy,color="y",alpha=(M_area[i][j]-1)/(Me-Mi))
        plt.fill(testx,testy,color=cm.jet((M_area[i][j]-color_Mmin)/(color_Mmax-color_Mmin)))
      
#三角形 
for i in range(2,n+1): 
        testx = [cross_point_x[i-1][i-1], cross_point_x[i][i], cross_point_x[i][i-1]]
        testy = [cross_point_y[i-1][i-1], cross_point_y[i][i], cross_point_y[i][i-1]]
        plt.fill(testx,testy,color=cm.jet((M_area[i][i]-color_Mmin)/(color_Mmax-color_Mmin)))

#(1,1)
testx = [0, cross_point_x[1][1], cross_point_x[1][0]]
testy = [0, cross_point_y[1][1], cross_point_y[1][0]]
plt.fill(testx,testy,color=cm.jet((M_area[1][1]-color_Mmin)/(color_Mmax-color_Mmin)))

#(n+1,n+1)
testx = [cross_point_x[n][n], cross_point_x[n+1][n], cross_point_x[n+1][n]]
testy = [cross_point_y[n][n], 0, cross_point_y[n+1][n]]
plt.fill(testx,testy,color=cm.jet((M_area[n+1][n+1]-color_Mmin)/(color_Mmax-color_Mmin)))




#カラーバーを無理やり表示外にかく
a=np.linspace(-1,-1,100)
b=np.linspace(-1,-1,100)
c=np.linspace(color_Mmin,color_Mmax,100).reshape(10,10)


sc = plt.scatter(a,b,c=c,cmap=plt.cm.jet,alpha=1)
plt.colorbar(sc,label="Mach number")
plt.show()




























#横に二つ並べてみる

#https://www.delftstack.com/ja/howto/matplotlib/how-to-make-different-subplot-sizes-in-matplotlib/
from matplotlib import gridspec

fig = plt.figure(figsize=(15, 10),dpi = 1000)
#fig = plt.figure()
spec = gridspec.GridSpec(ncols=2, nrows=1,
                         width_ratios=[50, 1])


ax1 = fig.add_subplot(spec[0])
ax2 = fig.add_subplot(spec[1])



import matplotlib.cm as cm
#マッハ数変化
#https://cranethree.hatenablog.com/entry/2015/07/25/204608
#https://qiita.com/hokekiyoo/items/cea310b2c36a01b970a6


#スロ―ト以前
for i in range(len(x_wall_minus)-1):
       
    testx = [x_wall_minus[i], x_wall_minus[i+1], x_wall_minus[i+1], x_wall_minus[i]]
    testy = [0, 0, y_wall_minus[i+1], y_wall_minus[i]]
    MM = optimize.bisect(getM_from_y, 0.1, 0.999, args=(y_wall_minus[i]))
    ax1.fill(testx,testy,color=cm.jet((MM-color_Mmin)/(color_Mmax-color_Mmin)))


#四角形
for i in range(2,n+2):
    for j in range(1,i):

        testx = [cross_point_x[i-1][j-1], cross_point_x[i-1][j], cross_point_x[i][j], cross_point_x[i][j-1]]
        testy = [cross_point_y[i-1][j-1], cross_point_y[i-1][j], cross_point_y[i][j], cross_point_y[i][j-1]]
        #plt.fill(testx,testy,color="y",alpha=(M_area[i][j]-1)/(Me-Mi))
        ax1.fill(testx,testy,color=cm.jet((M_area[i][j]-color_Mmin)/(color_Mmax-color_Mmin)))
#三角形            
for i in range(2,n+1): 
        testx = [cross_point_x[i-1][i-1], cross_point_x[i][i], cross_point_x[i][i-1]]
        testy = [cross_point_y[i-1][i-1], cross_point_y[i][i], cross_point_y[i][i-1]]
        ax1.fill(testx,testy,color=cm.jet((M_area[i][i]-color_Mmin)/(color_Mmax-color_Mmin)))

#(1,1)
testx = [0, cross_point_x[1][1], cross_point_x[1][0]]
testy = [0, cross_point_y[1][1], cross_point_y[1][0]]
ax1.fill(testx,testy,color=cm.jet((M_area[1][1]-color_Mmin)/(color_Mmax-color_Mmin)))

#(n+1,n+1)
testx = [cross_point_x[n][n], cross_point_x[n+1][n], cross_point_x[n+1][n]]
testy = [cross_point_y[n][n], 0, cross_point_y[n+1][n]]
ax1.fill(testx,testy,color=cm.jet((M_area[n+1][n+1]-color_Mmin)/(color_Mmax-color_Mmin)))




#https://bourbaki.biz/matplotlib-colorbarbase-document/
#https://illumination-k.dev/posts/python/colorbar_and_normvalue
import matplotlib as mpl
vmin = Mi
vmax = Me
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

cbar = mpl.colorbar.ColorbarBase(
    ax=ax2,
    cmap=plt.cm.jet,
    norm=norm,
    orientation="vertical",
    label="Mach number",
)



plt.show()






















#θを矢印で表示したい

#https://phst.hateblo.jp/entry/2020/12/22/000000

px=[]
py=[]
vx=[]
vy=[]
colors=[]



for i in range(2,n+2):
    for j in range(1,i):
        testx = [cross_point_x[i-1][j-1], cross_point_x[i-1][j], cross_point_x[i][j], cross_point_x[i][j-1]]
        testy = [cross_point_y[i-1][j-1], cross_point_y[i-1][j], cross_point_y[i][j], cross_point_y[i][j-1]]
        px.append(sum(testx)/len(testx))
        py.append(sum(testy)/len(testy))
        vx.append(np.cos(theta_area[i][j]) * (M_area[i][j]-Mi)/(Me-Mi))
        vy.append(np.sin(theta_area[i][j]) * (M_area[i][j]-Mi)/(Me-Mi))
        colors.append((M_area[i][j]-Mi)/(Me-Mi))



for i in range(2,n+1): 
        testx = [cross_point_x[i-1][i-1], cross_point_x[i][i], cross_point_x[i][i-1]]
        testy = [cross_point_y[i-1][i-1], cross_point_y[i][i], cross_point_y[i][i-1]]
        px.append(sum(testx)/len(testx))
        py.append(sum(testy)/len(testy))
        vx.append(np.cos(theta_area[i][i]) * (M_area[i][i]-Mi)/(Me-Mi))
        vy.append(np.sin(theta_area[i][i]) * (M_area[i][i]-Mi)/(Me-Mi))
        colors.append((M_area[i][i]-Mi)/(Me-Mi))




#(1,1)
testx = [0, cross_point_x[1][1], cross_point_x[1][0]]
testy = [0, cross_point_y[1][1], cross_point_y[1][0]]
px.append(sum(testx)/len(testx))
py.append(sum(testy)/len(testy))
vx.append(np.cos(theta_area[1][1]) * (M_area[1][1]-Mi)/(Me-Mi))
vy.append(np.sin(theta_area[1][1]) * (M_area[1][1]-Mi)/(Me-Mi))
colors.append((M_area[1][1]-Mi)/(Me-Mi))

#(n+1,n+1)
testx = [cross_point_x[n][n], cross_point_x[n+1][n], cross_point_x[n+1][n]]
testy = [cross_point_y[n][n], 0, cross_point_y[n+1][n]]
px.append(sum(testx)/len(testx))
py.append(sum(testy)/len(testy))
vx.append(np.cos(theta_area[n+1][n+1]) * (M_area[n+1][n+1]-Mi)/(Me-Mi))
vy.append(np.sin(theta_area[n+1][n+1]) * (M_area[n+1][n+1]-Mi)/(Me-Mi))
colors.append((M_area[n+1][n+1]-Mi)/(Me-Mi))



fig = plt.figure()
ax3 = fig.add_subplot(111) 
#ax.gca().set_aspect('equal')
im = ax3.quiver(px,py,vx,vy,colors, cmap=cm.jet, scale = 1,scale_units='xy',headwidth=3,width=0.005)
ax3.set_xlim(0,7.5)
ax3.set_ylim(0,1.5)
fig.colorbar(im,label="Mach number")
#im.set_clim(0,16)
plt.show()

img = inner_expansion_fan.plot(x="x",ax = ax3, ylim=[0,4], figsize=(30, 20),  legend = False,  xlabel="x [m]", ylabel="x [m]", title="Laval nozzle n={}".format(n),lw=1).get_figure()   
#img.savefig("圧縮12")
inner_expansion_fan.plot(x="x",ax = ax3, ylim=[0,6], figsize=(15, 10), legend = False,  xlabel="x [m]", ylabel="x [m]", title="Laval nozzle n={}".format(n),lw=1)
plt.show()









#エクセルへの書き込み

excel_list = [cross_point_x, cross_point_y, M_area, theta_area, beta_area, expi_line_rad, expr_line_rad, nu_area]
excel_name_list = ["x coordinate", "y coordinate", "mach number", "theta", "beta", "alfa-", "alfa+", "nu"]
excel_name_list = ["交点x座標", "交点y座標", "マッハ数", "θ", "β", "α-", "α+", "ν"]

with pd.ExcelWriter("圧縮12.xlsx") as writer:
    for v,name in zip(excel_list, excel_name_list):
        df = pd.DataFrame(v)
        df = df.replace('nan',np.nan)
        df = df.round(3)
        df.fillna('')
        print(df)
        df.to_excel(writer, sheet_name=name, index=True, header=True)



#表の画像化
#dpiいいぞ
#https://www.yutaka-note.com/entry/matplotlib_japanese#rcParams%E3%82%92%E8%A8%AD%E5%AE%9A
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

for v,name in zip(excel_list, excel_name_list):
    #ここめちゃくちゃ大変
    df = pd.DataFrame(v)
    df = df.replace('nan',np.nan)
    df = df.round(3)
    df = df.replace(np.nan,"")


    fig, ax = plt.subplots(figsize=(4,3), dpi=1000)
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
    ax.set_title(name)
    
    plt.show()
    #plt.savefig('table.png')

















#陽的に求まったのでいらなくなった
#θmaxを求める


def get_theta_max(theta_max):

    global Mi, Me, gamma, y0
    
    
    
    
    ye = outer_area(y0, Me, gamma)
    
    
    
    
    #適当に決めた
    #長すぎるとどうやら最初の反射波が膨張部にあたってしまうみたいだ。
    xa =0.5
    

    theta_max_rad = np.deg2rad(theta_max)
    
    
    
    
    
    
    
    #nuのグラフ化
    xx = np.linspace(1, 30, 100)
    nu_test = nu(xx)
    plt.plot(xx, nu_test)
    plt.title("nu")
    plt.show()
    
    
    #betaのグラフ化
    xx = np.linspace(1, 3.3, 100)
    nu_test = np.arcsin(1/xx)
    plt.plot(xx, nu_test)
    plt.title("beta")
    plt.show()
    
    
    
    
    
    
    
    #(10.24)
    n = 9
    #n本で区切ったらn+1この領域
    x = np.linspace(0, xa, n)
    
    #ノズル形状の図示
    y_nozzle = throat(y0, xa, theta_max, x)
    plt.plot(x, y_nozzle, '-o')
    #plt.axis([0, xa, 0, 1.5])
    plt.show()
    
    nu_area =  [["nan" for j in range(n+2)] for i in range(n+2)]
    theta_area = [["nan" for j in range(n+2)] for i in range(n+2)]
    
    #5番
    theta_area[1][1] = 0
    for i in range(2,n+1):
        theta_area[i][1] = get_theta(xl = x[i-1], xr = x[i-2])
    
    theta_area[n+1][1] = np.deg2rad(theta_max)
    
    
    #6番
    #(10.24)(10.25)
    for i in range(1,n+1):
        for j in range(1,i+1):
            #(10.24)
            nu_area[i][j] = theta_area[i][1] + theta_area[j][1]
            theta_area[i][j] = theta_area[i][1] - theta_area[j][1]
    
    
    
    #7番
    #図10.3より
    #n+1分割したとして求めた角度
    nu_area[n+1][1] = theta_area[n+1][1] + theta_area[1][1]
    
    
    
    #教科書の番号のつけ方間違っている
    
    
    for j in range(2, n+2):
        #(10.24)(10.25)
        nu_area[n+1][j] = theta_area[n+1][1] + theta_area[j][1]
        theta_area[n+1][j] = theta_area[n+1][1] - theta_area[j][1]
    
         
        #(10.3)(10.4)
        #j=nまで子か計算できない
        #nu_area[n+1][j] = (nu_area[n+1][j-1] + nu_area[n][j] + theta_area[n+1][j-1] - theta_area[n][j])/2
        #theta_area[n+1][j] = (nu_area[n+1][j-1] - nu_area[n][j] + theta_area[n+1][j-1] + theta_area[n][j])/2
    
    
    
    
    print(theta_max_rad)
    print(theta_area[n+1][1])
    
    
    
    #8番
    
    #角度を求めるのに必要な状態を求める
    M_area = [["nan" for j in range(n+2)] for i in range(n+2)]
    #rad
    beta_area = [["nan" for j in range(n+2)] for i in range(n+2)]
    
    
    #p115,p178,180
    #イクスパンションファン近似の二等分時にわざわざc_は求めなくてもよい。図10.3に従えばよし
    
    for i in range(1,n+2):
        for j in range(1,i+1):
            #p115
            #https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html
            M_area[i][j] = optimize.bisect(get_M_from_nu, 1, 50, args=(nu_area[i][j]))
            #p180
            beta_area[i][j] = np.arcsin(1/M_area[i][j])
    
    
    
    
    print("目標出口マッハ数は"+str(Me))
    print("今回の結果" + str(M_area[n+1][n+1]))
    print("θmaxにより変動")
    
    
    return Me -M_area[n+1][n+1]


#theta_max = optimize.bisect(get_theta_max, 0, 50)
#print(theta_max)




