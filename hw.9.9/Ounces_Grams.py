# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:34:31 2019

@author: jiang
"""

def Ounce_Gram():
    print('Ounces|Grames')
    for Ounces in range(1,31):
        Grams = round(Ounces*28.35)
        print(str(Ounces)+'     |'+str(Grams))


Ounce_Gram()