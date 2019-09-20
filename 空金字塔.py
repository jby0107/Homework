# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:36:54 2019

@author: jiang
"""

Symbol=input('a symbol: ')
while True:
    MaxNumOfSymbols=int(input('an odd Num: '))
    if MaxNumOfSymbols%2==1:
        break
    else:
        print('an odd num pls')
NumberOfSpaces=int((MaxNumOfSymbols-1)/2)
MidSpaces=1
NumberOfSymbols=1
while NumberOfSymbols<=MaxNumOfSymbols:
    if NumberOfSymbols==MaxNumOfSymbols:
        print(NumberOfSymbols*Symbol)
    elif NumberOfSymbols==1:
        print(NumberOfSpaces*' '+Symbol)
    else:
        print(NumberOfSpaces*' '+Symbol+MidSpaces*' '+Symbol)
        MidSpaces+=2
    NumberOfSymbols+=2
    NumberOfSpaces-=1