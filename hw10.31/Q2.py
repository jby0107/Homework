# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:01:59 2019

@author: jiang
"""

FileHandle = open('PRODUCTS.txt', 'r')
List = FileHandle.readlines()
PCode = ['' for i in range(int(len(List) / 3))]
PDescription = ['' for i in range(int(len(List) / 3))]
PRetailPrice = ['' for i in range(int(len(List) / 3))]
C = 0
D = 1
R = 2
for i in range(int(len(List) / 3)):
    PCode[i] = List[C].strip()
    PDescription[i] = List[D].strip()
    PRetailPrice[i] = float(List[R].strip())
    C += 3
    D += 3
    R += 3
FileHandle.close()
    
    
PCode1 = ['' for i in range(int(len(List) / 3))]
PDescription1 = ['' for i in range(int(len(List) / 3))]
PRetailPrice1 = ['' for i in range(int(len(List) / 3))]
FileHandle = open('PRODUCTS2.txt', 'r')
List = FileHandle.readlines()
FileHandle.close()
for String in range(len(List)):
    SpaceNum = 0
    for Char in range(len(List[String])):
        if List[String][Char] == ' ':
            SpaceNum += 1
            if SpaceNum == 1:
                PCode1[String] = List[String][:Char]
                FirstSpace = Char
            elif SpaceNum == 2:
                PDescription1[String] = List[String][FirstSpace + 1:Char]
                PRetailPrice1[String] = float(List[String][Char + 1:].strip())
                break


def ProductCodeSearch(SearchCode):
    for ThisIndex in range(len(PCode)):
        if PCode[ThisIndex] == SearchCode:
            return ThisIndex
    return -1

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                