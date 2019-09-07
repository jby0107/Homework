# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:01:36 2019

@author: jiang
"""

def CheckDigit():
    Count=1
    Total=0
    Weighting=10
    while True:
        Digit=int(input('Input Digit: '))
        Value= Digit*Weighting
        Total+=Value
        Weighting-=1
        Count+=1
        if Count==10:
            break
    Remainder=Total%11
    CheckDigit=11-Remainder
    if CheckDigit==10:
        CheckDigit='X'
    return CheckDigit

print(CheckDigit())