# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:01:04 2019

@author: jiang
"""

def Merge(vocab,word):
    global x, y
    x=[0]
    y=[0]
    result=[]
    xi=0
    yi=0
    while True:
        if xi>=len(vocab):
            result.extend(word[yi:])
            x.append(x[-1]+len(word[yi:]))
            y.append(y[-1]+len(word[yi:]))
            return result
        if yi>=len(word):
            return result
        if vocab[xi]==word[yi]:
            yi+=1
            x.append(x[-1]+1)
            y.append(y[-1])
        elif vocab[xi]<word[yi]:
            xi+=1
        else:
            result.append(word[yi])
            x.append(x[-1]+1)
            y.append(y[-1]+1)
            yi+=1