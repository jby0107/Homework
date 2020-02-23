# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:49:13 2020

@author: jiang
"""

LookUp = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'\
          , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

def Decrypt(CipherChar, LookUp):
    for i in range(len(LookUp)):
        if LookUp[i] == CipherChar:
            OriginalChar = chr(i + 65)
            return OriginalChar
    return 'Not Found'


X = Decrypt('A', LookUp)      