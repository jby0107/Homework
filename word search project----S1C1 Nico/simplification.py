# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:49:05 2019

@author: jiang
"""

def simplify(list1):
    simple=[]
    repeat=None
    for i in list1:
        if i!=repeat:
            simple.append(i)
            repeat=i
    return simple


