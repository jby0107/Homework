# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:04:41 2019

@author: jiang
"""

def AND(a, b):
    if a == 1:
        if b == 1:
            return 1
    return 0


def OR(a, b):
    if a == 1:
        return 1
    if b == 1:
        return 1
    return 0


def XOR(a, b):
    if a != b:
        return 1
    return 0


def ADDER(NUM1, NUM2):
    Result = ''
    C0 = 0
    n = -1
    while n >= -(len(NUM1)):
        S = XOR(int(NUM1[n]), int(NUM2[n]))
        C = OR(AND(S, C0), AND(int(NUM1[n]), int(NUM2[n])))
        S = XOR(S, C0)
        C0 = C
        Result += str(S)
        n -= 1
    Result += str(C0)
    Result = Result[::-1]
    return Result
        


















