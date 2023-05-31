
import numpy as np
from matplotlib import pyplot as plt


# LOX/LH2

g = 9.81 #[m/s^2]
Ro = 8.31451 #[J/molK] 一般気体定数

#比熱比　仮においている
k = 1.217
M = 11.5
Tc = 3250

def gamma_from_cp(cp, Ro):
    return cp/(cp-Ro)


x = np.linspace(35,40,100)
y = gamma_from_cp(cp=x, Ro=Ro)

plt.plot(x, y)
plt.show()



print(gamma_from_cp(cp=36,Ro=Ro))



target_Isp = 481.85 #[s]
target_thrust = 100*g*(10**3)  #[N] 推力


#p18より適当に決めた p22に図ありp155
mixture_ratio = 6 #混合比 wo/wf 燃料と酸化剤の質量流量比


#　水生成後に、残った水素/酸素との平均分子量  ロケット推進工学p155
#p22と違うのはおそらくロケット推進工学p161より、酸素原子や水素原子も生じているから
def get_ave_molecular_weight(mixture_ratio):
    #水素が残るとき
    return 2*(1+mixture_ratio)
    
    #if mixture_ratio <= 8: 
        #return 2*(1+mixture_ratio)
    #if mixture_ratio > 8: 
        #  return 32*(1+mixture_ratio)/(8+mixture_ratio)
    

x = np.linspace(1,10,10)
y = np.zeros(10)
for i,xx in enumerate(x):
    y[i] = get_ave_molecular_weight(xx)
plt.plot(x, y)
plt.show()


ave_molecular_weight = get_ave_molecular_weight(mixture_ratio)




#p15
w = target_thrust/(target_Isp*g) #推進薬質量流量[kg/s] wo(酸化剤流量)+wf(燃料流量)







# 膨張比　p20 ロケット推進工学(3-25) 3-35が普通、100km以上では40-100,400もあり
#ラバールノズルのことを考えた式
def get_expansion_ratio(k, pc, pe):
    a = 2/(k+1)
    a = a** (1/(k-1))
    b = pc/pe
    b = b**(1/k)
    c = (k+1)/(k-1)
    d = 1- (pe/pc)**((k-1)/k)
    ratio = a*b /np.sqrt(c*d)
    return ratio


x = np.linspace(10,2000,1000)
y = get_expansion_ratio(k=1.1, pc=x, pe=1)


plt.xlabel("pc/pe")
plt.ylabel("epsiron")
plt.plot(x, y)
plt.show()









#23 pe = paとしている [s]
def get_Isp(k, M, Tc, Ro, g, pe, pc):
    a = 2*k/(k-1)
    #Jとgの関係で1000をかけている
    b = Ro*1000/M
    index = (k-1)/k
    c = 1- (pe/pc)**index
    
    isp = (1/g) * np.sqrt(a*b*Tc*c) 
    
    return isp
    


print(get_Isp(k=k, M=ave_molecular_weight, Tc=1000, pe=5, pc=100, Ro=Ro, g=g))




x = np.linspace(10,10000,100)
y = get_Isp(k, M, Tc, Ro, g, pe=1, pc=x)


plt.xlabel("pc/pe")
plt.ylabel("Isp")
plt.plot(x, y)
plt.show()




x = np.linspace(10,10000,100)
xr = get_expansion_ratio(k, pc=x, pe=1)
y = get_Isp(k, M, Tc, Ro, g, pe=1, pc=x)


plt.xlabel("ε")
plt.ylabel("Isp")
plt.plot(xr, y)
plt.show()







#p16 [m/s]
#Jとgの関係で1000をかけている
def get_c_star(k, M, Ro, Tc):
    a = 1000*Ro*Tc/M
    index = (k+1)/(k-1)
    b = k * (2/(k+1))**index
    
    c = np.sqrt(a) / np.sqrt(b)
    
    return c


print("c*= ", get_c_star(k=1.25, M=8, Ro=Ro, Tc=2477))



x = np.linspace(1000,10000,1000)
y = get_c_star(k, M, Ro, Tc=x)


plt.xlabel("Tc")
plt.ylabel("c*")
plt.plot(x, y)
plt.show()









    








#p20 推力係数　p54(3-30) 123は
#pe: emmission, pc: combustion, pa: atomosphere eps:ε 
def get_CF(k,pe,pc,pa):
    a = 2*k*k /(k-1)
    index1 = (k+1)/(k-1)
    b = (2/(k+1))**index1
    index2 = (k-1)/k
    c = 1-(pe/pc)**index2
    d = (pe-pa)/pc
    
    eps = get_expansion_ratio(k, pc, pe)
    
    cf = np.sqrt(a*b*c) + eps*d
    return cf


#p19のグラフはこれのεバージョンか？媒介変数で行けるか？
x = np.linspace(10,100000,1000)
y = get_CF(k=1.25,pe=1,pc=x,pa=1)
plt.xscale('log')
plt.xlabel("pc/pe")
plt.ylabel("CF")
plt.plot(x, y)
plt.show()


    


target_CF = g*target_Isp/2438



print(get_expansion_ratio(k=1.25,pc=25000,pe=1))












#p17より読み取り

Pcns = 1000 #[psi] 6.9MPa
mixture_ratio = 4.83
k=1.217
Tc = 2977.778 +273  #5392F 
M = 11.5


c_star= get_c_star(k, M, Ro, Tc)


#23 pe = paとしている [s]
prop_Isp = get_Isp(k, M, Tc, Ro, g, pe=1, pc=800)
#prop_Isp = get_Isp(k=k, M=M, Tc=Tc, Ro=Ro, g=g, pe=1, pc=800)
prop_eps = get_expansion_ratio(k, pc=800, pe=1)












#ここより上は、rocketCEAでできることが判明したため、googlecolabで計算




#pump、タービン
Ro = 8.31451 #[J/molK] 一般気体定数
ro_H2 = 70.8 #[kg/m^3] @20K
ro_O2 = 1140 #[kg/m^3] @90K
M_H2 = 2 #[g/mol]
M_O2 = 32 #[g/mol]


#roは[kg/m^3]で与えること
def pump_power(Pd, Pi, wp, ro, etap):
    Lp = (Pd-Pi)*wp/(ro*etap)
    return Lp #[J/s]





#CpはMとkから計算するように変更
def turbine_power(P2_P1, etat, wt, M, Tg, k):
    R = 1000*Ro/M #[J/kgK] gからkgに変更のため1000倍
    Cp = R*k/(k-1) 
    index = (k-1)/k
    Lt = etat*wt*Cp*Tg*(1-P2_P1**index)
    return Lt #[J/s]
    
 

#p294
Hpump_power = pump_power(Pd=26.9*10**6, Pi=0.34*10**6, wp=35, ro=ro_H2, etap=0.7)
Opump_power = pump_power(Pd=17.5*10**6, Pi=0.74*10**6, wp=210, ro=ro_O2, etap=0.7)
sumpump_power = Hpump_power + Opump_power




x = np.linspace(1,2,1000)
y = turbine_power(P2_P1=1/x, etat=0.7, wt=35, M=M_H2, Tg=1000, k=1.4)

plt.hlines(y=sumpump_power, xmin=1, xmax=2)
#plt.xscale('log')
plt.xlabel("P2/P1")
plt.ylabel("L")
plt.plot(x, y)
plt.show()







#p43 30-40inch @LH2
L_star = 30 * 25.4 /1000 #[m]












#p50

def sigma(Twg, Tc, k, Mx):
    a = Twg/Tc
    b = 1 + (k-1)*Mx**2 /2
    c = (0.5*a*b + 0.5)**0.68
    d = b**0.12
    
    sigm = 1/(c*d)
    return sigm



def hg(Cg, Dt, mu0, Cp0, Pr0, Pc, c_star, rc, At, Ax,    Twg, Tc, k, Mx):
    a = Cg/Dt
    b = mu0**0.2 * Cp0/ Pr0 ** 0.6
    c = (Pc/c_star) ** 0.8
    d = (Dt/rc)**0.1
    e = (At/Ax)**0.9
    sigm = sigma(Twg, Tc, k, Mx)
    
    hg = a*b*c*d*e*sigm
    return hg





#mu[Pa s]: 粘性係数   cp[J/(KgK)]: 比熱   k[W/(mK)]: 熱伝導率
#https://www.hess.jp/Search/data/30-02-016.pdf
#https://www.jstage.jst.go.jp/article/jcsj1966/9/6/9_6_252/_pdf
#https://jaxa.repo.nii.ac.jp/?action=repository_uri&item_id=44147&file_id=31&file_no=1&nc_session=48444ja67uakakt1lm93lblek7%20target=
def Prandtl_number(k=1.55*10**-2,Cp=0.01,mu=1.73*10**-6):
    return mu*Cp*k


def hc( G, d, Tco, Twc, k=1.55*10**-2,Cp=0.01,mu=1.73*10**-6):
    Pr = Prandtl_number(k,Cp,mu)
    a = 0.029*Cp*mu**0.2 /Pr**(2/3)
    b = G**0.8 / d** 0.2
    c = (Tco/Twc)**0.55
    return a*b*c


    


    








