# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:43:04 2019

@author: jiang
"""

FileHandle=open('qbdata.txt','r')
NameList=[]
ScoreList=[]
for Line in FileHandle.readlines():
    word=Line.strip()
    a=word[-5:]
    if a[0]==' ':
        ScoreList.append(a[1:])
    else:
        ScoreList.append(a)
    Space=0
    for i in range(len(word)):
        if word[i]==' ':
            Space+=1
            if Space==2:
                NameList.append(word[:i])
                break
FileHandle.close()
FileHandle=open('NewList.txt','w')
for i in range(len(NameList)):
    if float(ScoreList[i])>=60:
        FileHandle.write('{0} has a rating of {1}'.format(NameList[i],ScoreList[i])+'\n')
        print('{0} has a rating of {1}'.format(NameList[i],ScoreList[i]))
FileHandle.close()
           
        
    