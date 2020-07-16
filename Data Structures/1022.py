# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:57:03 2020

@author: BielM
"""

from fractions import Fraction
def opera(n1,n2,d1,d2,op):
    l = []
    if(op == '+'):
        l.append(int(n1*d2 + n2*d1))
        l.append(int(d1*d2))
        return l
    if(op == '-'):
        l.append(n1*d2 - n2*d1)
        l.append(d1*d2)
        return l
    if(op == '*'):
        l.append(n1*n2)
        l.append(d1*d2)
        return l
    if(op == '/'):
        l.append(n1*d2)
        l.append(d1*n2)
        return l
    

    
n = int(input())
for i in range(n):
    inp = input().split(' ')
    
    n1,d1,op,n2,d2 = int(inp[0]),int(inp[2]),inp[3],int(inp[4]),int(inp[6])
    
    ff=opera(n1,n2,d1,d2,op)
    sdf = Fraction(ff[0],ff[1]).denominator
    snf = Fraction(ff[0],ff[1]).numerator
    print(str(ff[0])+"/"+str(ff[1]) +' = '+ str(snf)+'/'+str(sdf))
    
    
    