# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:23:00 2019

@author: jiang
"""

def zero():
    NegNum=0
    PosNum=0
    A=int(input('input a number: '))
    while A!=0:
        if A>0:
            PosNum+=1
        else:
            NegNum+=1
        A=int(input('input a number: '))
    return PosNum, NegNum