# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:22:58 2020

@author: jiang
"""

def SearchFile():
    MyArrayRow = 0
    FileHandle = open('LoginFile.txt', 'r')
    SearchID = input('ID: ')
    for i in FileHandle.readlines():
        if SearchID == i.strip():
            LoginEvents[MyArrayRow, 0] = i.strip()[5:9]
            LoginEvents[MyArrayRow, 1] = i.strip()[-14:]
            MyArrayRow += 1
    FileHandle.close()