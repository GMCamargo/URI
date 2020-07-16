# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:48:19 2020

@author: BielM
"""


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
def printCase(l):
    for k,v in l.items():
        if v != -1:
            print(k, 'found at', (v+1))
        else:
            print(k, 'not found')
cont = 1

while True:
    n,q = [int (s) for s in input().split(' ')]
    if(n == 0 and q == 0):
        break
    
    #colocar a posição e o num na árvore
    l = []
    for i in range(n):
        l.append(int(input()))
    
    l.sort()
    
    l2 = {}
    for j in range(q):
        num = int(input())
        l2[num] = BinarySearch(l, num)
    
        
    print('CASE#', cont)
    printCase(l2)
    cont += 1
        
        