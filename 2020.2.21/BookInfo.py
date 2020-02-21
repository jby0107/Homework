# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:35:09 2020

@author: jiang
"""

FileHandle = open('BookInfo.txt', 'r', encoding = 'utf-8')
List = FileHandle.readlines()
NewList = []
for i in range(len(List)):
    Index = 0
    while True:
        if List[i].strip()[Index] == ',':
            String = '#' + (2 - len(str(i))) * '0' + str(i + 1) + ' book author: ' + List[i].strip()[:Index + 1] + ' book title: "' + List[i].strip()[Index + 1:] + '"'
            while True:
                if List[i].strip()[Index] == ' ':
                    Copy = str(ord(List[i].strip()[Index + 1]))
                    break
                else:
                    Index -= 1
            print(String)
            String += ', number of copies: ' + Copy
            NewList.append(String)
            break
        else:
            Index += 1
FileHandle.close()
    
FileHandle = open('BookInfo_new.txt', 'w', encoding = 'utf-8')
for i in NewList:
    FileHandle.write(i + '\n')
FileHandle.close()














