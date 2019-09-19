# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:39:14 2019

@author: jiang
"""
#Character, Line, NewLine, i of type String
FileHandle=open('qb.txt','r')
Temp=open('Temp.txt','w')
Character=input('a Charater: ')
for Line in FileHandle.readlines():
    NewLine=''
    for i in Line:
        if i==' ':
            NewLine+=Character
        else:
            NewLine+=i
    Temp.write(NewLine)
FileHandle.close()
Temp.close()
FileHandle=open('qb.txt','w')
Temp=open('Temp.txt','r')
for Line in Temp.readlines():
    FileHandle.write(Line)
FileHandle.close()
Temp.close()