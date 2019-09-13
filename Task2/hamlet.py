# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:09:17 2019

@author: jiang
"""

FileHandle=open('hamlet.txt','r')
FileHandle1=FileHandle.read()
my_substitutions = FileHandle1.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",\
                                      "abcdefghijklmnopqrstuvwxyz                                          ")
cleaned_text = FileHandle1.translate(my_substitutions)
wds = cleaned_text.split()
FileHandle.close()

FrequenceDict={}
for i in wds:
    if i in FrequenceDict:
        FrequenceDict[i]+=1
    else:
        FrequenceDict[i]=1
SortedDict=sorted(FrequenceDict.items(),key=lambda x:x[1],reverse=True)
for i in range(100):
    print('{0:<15}{1:>4}'.format(SortedDict[i][0],SortedDict[i][1]))