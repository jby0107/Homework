# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:55:59 2019

@author: jiang
"""

import jieba
FileHandle=open('三国演义.txt','r',encoding='UTF-8')
FileHandle1=FileHandle.read()
WordList=jieba.lcut(FileHandle1)
FileHandle.close()
FrequenceDict={}
for i in WordList:
    if len(i)>=2:
        if i in FrequenceDict:
            FrequenceDict[i]+=1
        else:
            FrequenceDict[i]=1
SortedDict=sorted(FrequenceDict.items(),key=lambda x:x[1],reverse=True)
for i in range(100):
    print('{0:<20}{1:>4}'.format(SortedDict[i][0],SortedDict[i][1]))