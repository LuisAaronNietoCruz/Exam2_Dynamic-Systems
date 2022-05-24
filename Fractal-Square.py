#!/usr/bin/env python
# coding: utf-8

# In[26]:


# !/usr/bin/env python3

# Copyright (C) 2022 aaronnicruz@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import numpy as np
import math
import matplotlib.pyplot as plt


# def square(x,y,l,s):
#     Q1 = [x, y]  #el primer punto
#     Q2 = [x+l, y]  #el de la drecha
#     Q3 = [x+l, y+l] #el de la esquina con respecto al origen
#     Q4 = [x, y+l] # el de arriba del origen 
    
#     return [Q1[0],Q2[0],Q3[0],Q4[0], Q1[0] ] , [Q1[1],Q2[1],Q3[1],Q4[1], Q1[1]]
                                         
# fig = plt.figure()
# ax = fig.add_subplot()

# ax.set_aspect('equal')

# x=0.0
# y=0.0
# l=1.0

# X, Y = square(x,y,l,1)

# ax.plot(X, Y)
# l1 = l / 3.0

# x_r1= (X[0]+X[2])*-0.34
# y_r1= (Y[0]+Y[2])*0.33

# #print(x_r1,y_r1)


# x_r2 = (X[2]+X[1])*0.17
# y_r2 = (Y[2]+Y[1])*0.99

# x_r3 = (X[2]+X[1])*0.50
# y_r3 = (Y[2]+Y[1])*0.33

# x_r4 = (X[2]+X[1])*0.17
# y_r4 = (Y[2]+Y[1])*-0.33


# X, Y = square(x_r1,y_r1, l1, 1) 
# ax.plot(X,Y)
# X, Y = square(x_r2,y_r2, l1, 1) 
# ax.plot(X,Y)
# X, Y = square(x_r3,y_r3 ,l1, -1)    
# ax.plot(X, Y)
# X, Y = square(x_r4,y_r4 ,l1, -1)    
# ax.plot(X, Y)

#plt.show()


fig, ax = plt.subplots()
ax.set_aspect(1)

def square(x,y,l):
    Q1 = [x, y]  #el primer punto
    Q2 = [x+l, y]  #el de la drecha
    Q3 = [x+l, y+l] #el de la esquina con respecto al origen
    Q4 = [x, y+l] # el de arriba del origen 
    
    ax.plot ([Q1[0],Q2[0],Q3[0],Q4[0], Q1[0] ] , [Q1[1],Q2[1],Q3[1],Q4[1], Q1[1]])


def fractal(n, x, y, l):
    square(x, y, l)
    if n > 0:
        A_1 = x + l
        A_2 = y + l/3
        fractal(n - 1, A_1, A_2, l/3)

        B_1 = x + l/3
        B_2 = y - l/3
        fractal(n - 1, B_1, B_2, l/3)

        C_1 = x - l/3
        C_2 = y + l/3
        fractal(n - 1, C_1, C_2, l/3)

        D_1 = x + l/3
        D_2 = y + l
        fractal(n - 1, D_1, D_2, l/3)


fractal(4, 0, 0, 1)
plt.show()

