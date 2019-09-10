# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:42:09 2019

@author: jiang
"""

def ValidUserID(UserID):
    Upper = 0
    Digit = 0
    for i in UserID:
        if 65 <= ord(i) <= 90:
            Upper+=1
        elif 48 <= ord(i) <= 57:
            Digit+=1
    if Upper == 3 and Digit == 4:
        return('UserID valid')
    else:
        return('UserID invalid')
        
print(ValidUserID(input('UserID: ')))