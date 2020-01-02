# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 21:51:13 2020

@author: jiang
"""

import random


Mark = []
for i in range(20):
    Mark.append(random.randint(0, 100))


def ProcessMark(Mark):
    Total = 0
    Highest = 0
    for i in range(len(Mark)):
        Total += Mark[i]
        if Mark[i] >= Highest:
            Highest = Mark[i]
            n = i
    print('The average mark is ' + str(Total / 20) + 'and the highest mark is ' + str(Highest))
    return n