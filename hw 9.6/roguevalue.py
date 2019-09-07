# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:43:44 2019

@author: jiang
"""

def RogueValue():
    Total=1
    Count=1
    RogueValue=-1
    Number=int(input('Number: '))
    while Number!=RogueValue:
        Count+=1
        Total+=Number
        Number=int(input('Number: '))
    if Count>0:
        Average=Total/Count
        print(Average)