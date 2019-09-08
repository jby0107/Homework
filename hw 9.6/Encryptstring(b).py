# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:48:33 2019

@author: jiang
"""
def sub(Lookup):
    StartPos=int(input('start position: '))
    NumToChange=int(input('NumToChange: '))
    n=0
    while True:
        print('pls input the subsititution: ')
        NewChar=str(input())
        Lookup[StartPos+n]=NewChar
        n+=1
        if n==NumToChange:
            break
    print('Num of elements changed: '+str(NumToChange))