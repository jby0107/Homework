# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:03:12 2019

@author: jiang
"""

def EggsIntoBoxes(Num):
    return Num // 6, Num % 6


NumberOfBoxes, EggsLeftOver = EggsIntoBoxes(13)
print(NumberOfBoxes, EggsLeftOver)