# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:16:22 2019

@author: jiang
"""

def Sequential(list1, target):
    global a
    a=False
    for i in range(len(list1)):
        if list1[i]==target:
            a=True
            break
    if a==False:
        missing_words.append(target)
    return missing_words
        

    



        