# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 20:54:17 2021

@author: yuki
"""

import pandas as pd

for i in range(1,7):
    print("図4.{0}.1　迎え角{1}°における揚力係数Cp分布".format(i, (i-1)*5))
    print("図4.{0}.2　迎え角{1}°における圧力分布".format(i, (i-1)*5))
    print("図4.{0}.3　迎え角{1}°における速度分布".format(i, (i-1)*5))
    print("図4.{0}.4　迎え角{1}°における流線".format(i, (i-1)*5))
    
    
    print("---------------------")
    
df = pd.read_excel("係数.xlsx")


df.plot(x="迎角[°]", y = "CDp", xlim = [0,25], legend = False, xlabel="Angle of attack [degree]", ylabel="CDp",style=['o-'])
df.plot(x="迎角[°]", y = "CDf", xlim = [0,25], legend = False, xlabel="Angle of attack [degree]", ylabel="CDf",style=['o-'])
df.plot(x="迎角[°]", y = "CD", xlim = [0,25], legend = False, xlabel="Angle of attack [degree]", ylabel="CD",style=['o-'])
df.plot(x="迎角[°]", y = "CL", xlim = [0,25], legend = False, xlabel="Angle of attack [degree]", ylabel="CL",style=['o-'])
df.plot(x="迎角[°]", y = "CL/CD", xlim = [0,25], legend = False, xlabel="Angle of attack [degree]", ylabel="CL/CD",style=['o-'])
df.plot(x="迎角[°]", y = ["CL", "CD"], xlim = [0,25], legend = True, xlabel="Angle of attack [degree]", ylabel="CL, CD",style=['o-','o-'])
df.plot(x="迎角[°]", y = ["CDf","CDp"], xlim = [0,25],ylim=[0,0.42] ,legend = True, xlabel="Angle of attack [degree]", ylabel="CL, CD",kind='area', stacked=True)
for i in range(1,7):
    print("図4.7.{0}　CDpの迎え角変化".format(i))