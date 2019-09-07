# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:51:19 2019

@author: jiang
"""

import random

PlainText='Hello world'
Num=[]
for i in range(1,129):
    Num.append(i)
#generate Lookup array
def RandomLookup():
    Lookup=[]
    Flag=True
    while Flag:
        i=random.choice(Num)
        Temp=chr(i)
        Lookup.append(Temp)
        Num.remove(i)
        if len(Num)==0:
            Flag=False
    return Lookup

#main function

def EncryptString(PlainText,Lookup):
    OutString=''
    for n in range(len(PlainText)):
        OldChar=PlainText[n]
        OldCharValue=ord(OldChar)
        NewChar=Lookup[OldCharValue]
        OutString+=NewChar
    return OutString

Lookup=RandomLookup()
print('OutString: ',EncryptString(PlainText,Lookup))
    
    