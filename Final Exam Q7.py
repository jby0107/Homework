# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:26:56 2020

@author: jiang
"""

def Clean(InString):
    AfterSpace = False
    NewString = ''
    for i in range(len(InString)):
        NextChar = InString[i]
        if AfterSpace == True:
            if NextChar != ' ':
                NewString = NewString + NextChar
                AfterSpace = False
        else:
            NewString = NewString + NextChar
            if NextChar == ' ':
                AfterSpace = True
    return NewString