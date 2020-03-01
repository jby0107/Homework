# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:21:13 2020

@author: jiang
"""

import random


def Generate():
    String = ''
    Sum = 0
    for i in range(1, 11):
        Num = random.randint(0,9)
        Sum += Num * i
        String += str(Num)
    print('Correct data: ', String)
    if random.randint(0, 1) == 1:
        String = String[:4] + '1' + String[5:]
    return String, 11 - Sum % 11


def CheckSum(String, Sum):
    CheckSum = 0
    print('Received data: ', String)
    for i in range(len(String)):
        CheckSum += int(String[i]) * (i + 1)
    CheckSum = 11 - CheckSum % 11
    if CheckSum == Sum:
        print('Data correct')
    else:
        print('Data error')
    

Data = Generate()
CheckSum(Data[0], Data[1])   
    
    
    
    
