# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:31:16 2020

@author: jiang
"""

def StringClean(InString):
    OutString = ''
    for Counter in range(len(InString)):
        NextChar = InString[Counter].lower()
        if 'a' <= NextChar <= 'z':
            OutString += NextChar
    return OutString
        