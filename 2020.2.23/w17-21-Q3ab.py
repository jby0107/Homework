# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:28:21 2020

@author: jiang
"""

import random

UserNameArray = []
for i in range(100):
    x = random.randint(0, 100)
    String = (6 - len(str(x))) * '0' + str(x) + 'AAAAA'
    UserNameArray.append(String)

def BubbleSort(UserNameArray):
    Minus = 0
    Flag = True
    while Flag == True:
        Minus += 1
        Flag = False
        for i in range(len(UserNameArray) - Minus):
            if UserNameArray[i] > UserNameArray[i + 1]:
                Flag = True
                Temp = UserNameArray[i]
                UserNameArray[i] = UserNameArray[i + 1]
                UserNameArray[i + 1] = Temp
    return UserNameArray

NewList = BubbleSort(UserNameArray)

def FindRepeats(NewList):
    Current = None
    Count = 0
    for i in NewList:
        if i != Current:
            Current = i
        else:
            Count += 1
    return Count
    
    
Count = FindRepeats(NewList)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    