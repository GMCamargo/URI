# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:43:05 2020

@author: BielM
"""

def busca(l, a, p):
    if(p > 5): return 0
    return 1

while True:
    a = int(input())
    if(a == 0): break
    cont = 0
    l = []
    for i in range(a):
        l.append(input())
    
    l = sorted(l, key = len)
    

    dic = {}
    for e in l:
        count = 0
        for i in range(len(l)-1, 0, -1):
            if(l[i] in e):
                count += 1
            dic[e] = count
    print(dic[max(dic, key=dic.get)])