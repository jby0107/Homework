# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:34:10 2019

@author: jiang
"""

INPUT = [(0, 0), (0, 1), (1, 0), (1, 1)]


def AND():
    print('a | b | x')
    for i in INPUT:
        a, b = i[0], i[1]
        print(str(a) + ' | ' + str(b) + ' | ', end = '')
        if a == 1:
            if b == 1:
                print('1')
            else:
                print('0')
        else:
            print('0')


def OR():
    print('a | b | x')
    for i in INPUT:
        a, b = i[0], i[1]
        print(str(a) + ' | ' + str(b) + ' | ', end = '')
        if a == 1:
            print('1')
        elif b == 1:
            print('1')
        else:
            print('0')


def NOT(a):
    if a == 1:
        return 0
    return 1


def NAND():
    print('a | b | x')
    for i in INPUT:
        a, b = i[0], i[1]
        print(str(a) + ' | ' + str(b) + ' | ', end = '')
        if a == 1:
            if b == 1:
                print('0')
            else:
                print('1')
        else:
            print('1')


def NOR():
    print('a | b | x')
    for i in INPUT:
        a, b = i[0], i[1]
        print(str(a) + ' | ' + str(b) + ' | ', end = '')
        if a == 0:
            if b == 0:
                print('1')
            else:
                print('0')
        else:
            print('0')


def XOR():
    print('a | b | x')
    for i in INPUT:
        a, b = i[0], i[1]
        print(str(a) + ' | ' + str(b) + ' | ', end = '')
        if a != b:
            print('1')
        else:
            print('0')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























