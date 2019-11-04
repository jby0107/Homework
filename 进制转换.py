# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:05:37 2019

@author: jiang
"""


def Convert(BeforeType, AfterType, Number):
    Sub = ['A', 'B', 'C', 'D', 'E', 'F']
    Deci = 0
    for i in range(len(Number) - 1):
        if Number[i] in Sub:
            Num = Sub.index(Number[i]) + 10
        else:
            Num = int(Number[i])
        Deci = (Deci + Num) * BeforeType
    if Number[-1] in Sub:
        Num = Sub.index(Number[-1]) + 10
    else:
        Num = int(Number[-1])
    Deci += Num
    After = ''
    while Deci >= AfterType:
        if Deci % AfterType > 9:
            Num = Sub[Deci % AfterType - 10]
        else:
            Num = str(Deci % AfterType)
        After += Num
        Deci = Deci // AfterType
    if Deci > 9:
        Num = Sub[Deci - 10]
    else:
        Num = str(Deci)
    After += Num
    n = -1
    for i in range(len(After)):
        print(After[n], end = '')
        n -= 1


BeforeType = int(input('decimal type before convertion: '))
AfterType = int(input('decimal type after convertion: '))
Number = input('Number to convert: ')
Convert(BeforeType, AfterType, Number)

























