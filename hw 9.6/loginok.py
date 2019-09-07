# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:10:18 2019

@author: jiang
"""

def Login(UserList, PasswordList):
    MaxIndex=20
    MyUserID=str(input('input user id: '))
    MyPassword=str(input('inoput password: '))
    UserIDFound=False
    LoginOK=False
    Index=0
    while True:
        Index+=1
        if UserList[Index-1]==MyUserID:
            UserIDFound=True
        if Index=MaxIndex or UserIDFound==True:
            break
    if UserIDFound==True:
        if PasswordList[Index-1]==MyPassword:
            LoginOK=True
    if LoginOK==True:
        print('Login successful')
    else:
        print('User ID and/or password incorrect')