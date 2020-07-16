# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:00:17 2020

@author: BielM
"""

a = int(input())

for i in range(a):
    s = input()
    c = list(s)
    for i in range(len(c)):
        if(not(c[i].isspace()) and c[i].isalpha()):
            c[i] = chr(ord(c[i]) + 3)
    c = c[::-1]
    
    if(len(c)%2==0):
        for i in range(round(len(c)/2), len(c)):
            c[i] = chr(ord(c[i]) - 1)
    else:
        for i in range(round(len(c)/2 - 0.5), len(c)):
            c[i] = chr(ord(c[i]) - 1)
    
    print(*c, sep='')
