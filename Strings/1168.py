# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:09:00 2020

@author: BielM
"""

dic = {'1': 2,
       '2': 5,
       '3': 5,
       '4': 4,
       '5': 5,
       '6': 6,
       '7': 3,
       '8': 7,
       '9': 6,
       '0' : 6}
n = int(input())
for i in range(n):
    res = 0
    s = input()
    for i in range(len(s)):
        res += dic[s[i]]
    print(res, "leds")