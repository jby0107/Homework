# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:51:11 2020

@author: jiang
"""
import random

Result = []
for i in range(100):
    Result.append(round(random.uniform(-100, 100), 1))

Total = 0
ZeroCount = 0

for i in Result:
    Total += i
    if i == 0:
        ZeroCount += 1
Average = Total / 100
print('Average: ', Average)
print('Zero: ', ZeroCount)




























