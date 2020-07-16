# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:55:16 2020

@author: BielM
"""

while True:
    a, b = [str(s) for s in input().split(' ')]
    if(a == '0' and b == '0'): break
    b = b.replace(a,'')
    print(int(b) if b.isalnum() else '0')
    