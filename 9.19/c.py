# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:57:41 2019

@author: jiang
"""
#Code, Line of type String
#FoundCode of type Boolean
FileHandle=open('Newqb.txt','r')
Code=input('Four Digit code: ')
FoundCode=False
for Line in FileHandle.readlines():
    if Line[:4]==Code:
        print(Line)
        FoundCode=True
        break
if FoundCode==False:
    print('Code not found in file')