# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:16:45 2019

@author: jiang
"""
#Symbol of type String
#MaxNumOfSymbols,NumberOfSpaces,NumberOfSymbols of type Integer
Symbol=input('a symbol: ')
while True:
    MaxNumOfSymbols=int(input('an odd Num: '))
    if MaxNumOfSymbols%2==1:
        break
    else:
        print('an odd num pls')
NumberOfSpaces=int((MaxNumOfSymbols-1)/2)
NumberOfSymbols=1
while NumberOfSymbols<=MaxNumOfSymbols:
    for i in range(NumberOfSpaces):
        print(' ',end='')
    for i in range(NumberOfSymbols):
        print(Symbol,end='')
    print('')
    NumberOfSymbols+=2
    NumberOfSpaces-=1
    
    
