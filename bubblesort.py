# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:47:34 2019

@author: jiang
"""

def bubble(n):
    swap=True
    while swap==True:
        swap=False
        for i in range(0,len(n)-1):
            if n[i]>n[i+1]:
                temp=n[i+1]
                n[i+1]=n[i]
                n[i]=temp
                swap=True
    print(n)
n=[4,6,3,8,6,7,2,3,9,4,0,6]    
bubble(n)
            