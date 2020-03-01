# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:56:02 2020

@author: jiang
"""

import random

def Generate():
    List = []
    n = 1
    Sum = 0
    for i in range(12):
        X = random.randint(0, 9)
        List.append(X)
        Sum += X * n
        if n == 1:
            n = 3
        else:
            n = 1
    CheckDigit = 10 - Sum % 10
    List.append(CheckDigit)
    print('Correct List: ', List)
    if random.randint(0, 1) == 1:
        List[random.randint(0, 11)] = 1
    return List


def ISBN13(Input):
    print('Received List: ', Input)
    n = 1
    Sum = 0
    for i in Input[0:-1]:
        Sum += i * n
        if n == 1:
            n = 3
        else:
            n = 1
    CheckDigit = 10 - Sum % 10
    if CheckDigit == Input[-1]:
        print('Data Correct')
    else:
        print('Data Error')
    
    
    
ISBN13(Generate())
    
    
    
    
    
    
    
    