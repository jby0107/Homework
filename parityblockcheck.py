# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:40:45 2020

@author: jiang
"""
import random


def CreateBlock():
    Block = []
    for i in range(7):
        Byte = []
        Count = 0
        for x in range(7):
            Bit = random.randint(0, 1)
            Byte.append(Bit)
            Count += Bit
        if Count % 2 == 1:
            Byte.append(0)
        else:
            Byte.append(1)
        Block.append(Byte)
    Byte = []
    for Column in range(8):
        Count = 0
        for Row in range(7):
            Count += Block[Row][Column]
        if Count % 2 == 1:
            Byte.append(0)
        else:
            Byte.append(1)
    Block.append(Byte)
    return Block

def RandomError(List):
    x = random.randint(0,7)
    y = random.randint(0,7)
    if List[x][y] == 0:
        List[x][y] = 1
    else:
        List[x][y] = 0
    print('x: ', str(x))
    print('y: ', str(y))
    return List


def BlockCheck(Input):
    RowNum = None
    ColumnNum = None
    for Row in range(len(Input)):
        Count = 0
        for Bit in Input[Row]:
            Count += Bit
        if Count % 2 == 0:
            RowNum = Row
            break
    for Column in range(8):
        Count = 0
        for bit in range(8):
            Count += Input[bit][Column]
        if Count % 2 == 0:
            ColumnNum = Column
            break
    if RowNum == None:
        print('No error')
    else:
        print('Error: ', '['+ str(RowNum) + ',' + str(ColumnNum) + ']')
        if Input[RowNum][ColumnNum] == 0:
            Input[RowNum][ColumnNum] = 1
        else:
            Input[RowNum][ColumnNum] = 0
    print('Correct: ',Input)
    return Input
    
    
    
BlockCheck(RandomError(CreateBlock()))
    
    
    
    
    
    
    
    
    