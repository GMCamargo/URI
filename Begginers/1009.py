# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:49:20 2020

@author: BielM
"""
a = input().split('\n')

for line in a:
    line.split('\n')
    for i in range(len(a)):
        A,B = [int(s) for s in a[i].split(' ')]
        A = "{:032b}".format(A)
        B = "{:032b}".format(B)
        C = ""

    for i,c in enumerate(A):
        if(A[i] != B[i]):
            C += '1'
        else:
            C += '0'


    print(int(C,2))