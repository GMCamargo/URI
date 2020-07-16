# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:59:42 2020

@author: BielM
"""


class Node:
    
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
        
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def search(self, k):
        if r is None or r.data == k:
            return r
        elif r.data < k:
            return search(r.right, k)
        else:
            return search(r.left, k)
        
#r = Node(2)
#r.insert(5)
#r.printTree()
#b = r.search(7)

#print(b.data if b != None else 'Not Found')

while True:
    n,q = [int (s) for s in input().split(' ')]
    if(n == 0 and q == 0):
        break
    
    #colocar a posição e o num na árvore
    r = None
    for i in range(n):
        if i == 0:
            r = Node(int(input()))
        else:
            r.insert(int(input()))
    
    r.printTree()


