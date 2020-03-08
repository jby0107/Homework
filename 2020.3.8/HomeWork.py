# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:05:35 2020

@author: jiang
"""

def GetInfo():
    while True:
        ID = input('UserID: ')
        if 'A' <= ID[0] <= 'Z' and '0000' <= ID[1:] <= '9999':
            break
    PreferredName = input('Preferred name: ')
    return ID + '*' + PreferredName


def WriteInfo(Info):
    if 'A' <= Info[0] <= 'M':
        FileHandle = open('File1.txt', 'a')
    else:
        FileHandle = open('File2.txt', 'a')
    try:
        FileHandle.write(Info + '\n')
        FileHandle.close()
        return True
    except Exception:
        FileHandle.close()
        return False
    
    
def TopLevel():
    while True:
        Info = GetInfo()
        X = WriteInfo(Info)
        if X == False:
            print('Error when writing into file')
            return ''
        Flag = input('Repeat?(Y/N): ')
        if Flag == 'N':
            return ''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    