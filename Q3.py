# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:12:07 2019

@author: jiang
"""

import random


def GenerateResult():
    Result = []
    for i in range(100):
        Result.append(random.uniform(-100, 100))
    return Result


def ScanArray(AverageValue, ZeroCount, ArrayName):
    Total = 0
    for i in ArrayName:
        if i == 0:
            ZeroCount += 1
        Total += i
    AverageValue = Total / 100
    print('ZeroCount: ', ZeroCount)
    print('Average: ', AverageValue)


ScanArray(AverageValue = 0, ZeroCount = 0, ArrayName = GenerateResult())
        