# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:36:19 2023

@author: yuki
"""

import numpy as np

#機械システム入門シリーズ8複合材料　を参照
#20230513 航空機設計開発特論レポート4　用に作成

Ex = 61
Ey = 61
nux = 0.05
G = 4.2
m = 1/(1-nux*nux*Ey/Ex)

Qxx = m * Ex
Qyy = m * Ey
Qxy = m * nux * Ey
Qss = G
 


U_Qxy_mat = np.array([[3/8, 3/8, 1/4, 1/2],
                      [1/2, -1/2, 0, 0],
                      [1/8, 1/8, -1/4, -1/2],
                      [1/8, 1/8, 3/4, -1/2],
                      [1/8, 1/8, -1/4, 1/2]])

Qxy_mat = np.array([Qxx, Qyy, Qxy, Qss])

U_mat = U_Qxy_mat  @ Qxy_mat.T


def calc_Qij(theta, U_mat):
    U1,U2,U3,U4,U5 = U_mat
    #print(U1,U2,U3,U4,U5)
    Qij_U_mat =  np.array([[U1, np.cos(2*theta), np.cos(4*theta)],
                           [U1, -np.cos(2*theta), np.cos(4*theta)],
                           [U4, 0, -np.cos(4*theta)],
                           [U5, 0, -np.cos(4*theta)],
                           [0, np.sin(2*theta)/2, np.sin(4*theta)],
                           [0, np.sin(2*theta)/2, -np.sin(4*theta)]])
    
    Qij_mat = Qij_U_mat @ np.array([1,U2,U3]).T
    
    return Qij_mat 


h=1
Qij_mat_1ply = calc_Qij(np.deg2rad(45), U_mat)
Qij_mat_2ply = calc_Qij(np.deg2rad(0), U_mat)




A_star = 2*(h*Qij_mat_1ply + h*Qij_mat_2ply) /(4*h)

A_star_mat = np.array([[A_star[0],A_star[2],A_star[4]],
                       [A_star[2],A_star[1],A_star[5]],
                       [A_star[4],A_star[5],A_star[3]]])

a_star_mat = np.linalg.inv(A_star_mat)

print("E1:", 1/a_star_mat[0,0])
print("比剛性[x10^6 m]", 1/a_star_mat[0,0]/1.6/9.8)