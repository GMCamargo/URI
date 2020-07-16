# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:02:23 2020

@author: BielM
"""


import matplotlib.pyplot as plt
# custo médio
x = []
y = []

for i in range(1,10):
    x.append(i)
    y.append((4*i)+(16/i))
    
# custo marginal

x1 = []
y1 = []

for j in range(10):
    x1.append(j)
    y1.append(8*j)
    
# custo variável médio

x2 = []
y2 = []

for k in range(10):
    x2.append(k)
    y2.append(k*4)

plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)


