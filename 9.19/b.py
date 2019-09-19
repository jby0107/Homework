# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:47:20 2019

@author: jiang
"""
#Name, NewName, i, Line of type String
#n, Num of type Integer
FileHandle=open('Newqb.txt','w')
Original=open('qb.txt','r')
Name=input('Remove name: ')
NewName=''
n=0
Num=4-len(str(n))
for i in Name:
    if i == ' ':
        NewName+='&'
    else:
        NewName+=i
for Line in Original.readlines():
    if Line[:len(Name)]!=NewName:
        n+=1
        FileHandle.write(Num*'0'+str(n)+Line)
FileHandle.close()
Original.close()
    