# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:33:05 2020

@author: jiang
"""

def ValidatePassword(Pass):
    Lower = 0
    Upper = 0
    Num = 0
    for i in Pass:
        if 'a' <= i <= 'z':
            Lower += 1
        elif 'A' <= i <= 'Z':
            Upper += 1
        elif '0' <= i <= '9':
            Num +=1
        else:
            return False
    if Lower >=2 and Upper >= 2 and Num >= 3:
        return True
    return False