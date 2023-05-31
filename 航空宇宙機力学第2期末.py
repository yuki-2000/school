# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:01:43 2022

@author: yuki
"""

import numpy as np

#円軌道
def parking_v(r, mu):
    return np.sqrt(mu/r)

#muはm^3なのでkm/sを求めるには10^-9する
print(parking_v(r=500+6378, mu=3.986*(10**5)))
print(parking_v(r=1.496*(10**8), mu=1.327*(10**11)))
print(parking_v(r=2*1.496*(10**8), mu=1.327*(10**11)))
print(parking_v(r=6378+600, mu=3.986*(10**5)))
print(parking_v(r=10000+1000, mu=3*3.986*(10**5)))

#a = (ra+rp)/2
#

#楕円近地点速度1
def ellipse_vp(mu, rp, ra):
    a = np.sqrt(mu/rp)
    b = np.sqrt(2*ra/(ra+rp))
    return a*b

#楕円近地点速度2
def ellipse_vp2(mu, a, e):
    aa = np.sqrt(mu/a)
    bb = np.sqrt((1+e)/(1-e))
    return aa*bb


print(ellipse_vp(mu=3.986*(10**5), rp=500+6378, ra=3000+6378))
print(ellipse_vp(mu=1.327*(10**11), rp=1.496*(10**8), ra=2*1.496*(10**8)))

#楕円遠地点速度1
def ellipse_va(mu, rp, ra):
    a = np.sqrt(mu/ra)
    b = np.sqrt(2*rp/(ra+rp))
    return a*b

#楕円遠地点速度2
def ellipse_va2(mu, a, e):
    aa = np.sqrt(mu/a)
    bb = np.sqrt((1-e)/(1+e))
    return aa*bb

print(ellipse_va(mu=3.986*(10**5), rp=500+6378, ra=3000+6378))
print(ellipse_va(mu=1.327*(10**11), rp=1.496*(10**8), ra=2*1.496*(10**8)))


#軌道面が傾いているトランスファー
def delta_v(vi, vf, delta_i):
    c = 2*vi*vf*np.cos(np.deg2rad(delta_i))
    d = vi**2 + vf**2 - c
    return np.sqrt(d)

print(delta_v(vi=7.1834, vf=8.0043, delta_i=3.12))
print(delta_v(vi=7.1364, vf=7.3502, delta_i=30.4-3.12))

#おまけ、delta_i変化におけるv変化
y = []
for i in range(300):
    v1 = delta_v(vi=7.1834, vf=8.0043, delta_i=i/10)
    v2 = delta_v(vi=7.1364, vf=7.3502, delta_i=30.4-i/10)
    y.append(v1+v2)


from matplotlib import pyplot as plt
# データの定義(サンプルなのでテキトー)
x = list(range(300))
# グラフの描画
plt.plot(x, y)
plt.show()





#-----------------------------------------------------------------------------
print("-------------------------------------")

#地球から脱出する絶対速度...太陽中心楕円軌道の近地点速度
vp_sun = ellipse_vp(mu=1.387*(10**11), rp=1.496*(10**8), ra=2.28*(10**8))
print(vp_sun)
#地球の公転速度
vplus = parking_v(r=1.496*(10**8), mu=1.387*(10**11))
print(vplus)
#地球視点の双曲線∞速度
v8_plus = vp_sun - vplus
print(v8_plus)


#双曲線軌道、∞速度から近地点速度を求める
def hyperbola_vp(v8, mu, rp):
    a = v8**2 + 2*mu/rp
    return np.sqrt(a)

#地球から脱出するときの近地点速度（もちろん地球視点）
vp = hyperbola_vp(v8= v8_plus, mu=3.986*(10**5), rp=6578)
print(vp)
#地球でのパーキング軌道の速度
v_parking = parking_v(r=6587, mu=3.986*(10**5))
print(v_parking)
#差分が必要な速度増速
delta_v1 = vp-v_parking
print(delta_v1)

#------------------
print("----------")
#太陽から見た楕円軌道遠地点速度
va_sun = ellipse_va(mu=1.387*(10**11), rp=1.496*(10**8), ra=2.28*(10**8))
print(va_sun)
#火星の公転速度
va = parking_v(r=2.28*(10**8), mu=1.387*(10**11))
print(va)
#火星から見た双曲線∞速度、速度の大小からこっちの引き算
v8_x = va-va_sun
print(v8_x)
#火星双曲線近地点速度
v_mars = hyperbola_vp(v8=v8_x, mu=4.283*(10**4), rp=3500)
print(v_mars)
#火星パーキング速度
v_mars_parking = parking_v(r=3500, mu=4.283*(10**4))
print(v_mars_parking)
#火星軌道で回るため二必要な速度増速
delta_v2 = v_mars - v_mars_parking
print(delta_v2)



print(hyperbola_vp(v8=4.607, mu=3.986*(10**5), rp=6378+600))
print(hyperbola_vp(v8=3.8648, mu=3*3.986*(10**5), rp=10000+1000))



