# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:02:25 2020

@author: jiang
"""

def addNewBook():
    FileHandle = open('BookInfo_New.txt', 'a')
    FileHandle.write(input('Input New Book Info: ') + '\n')
    FileHandle.close()
def SearchBookByAuthor():
    FileHandle = open('BookInfo_New.txt', 'r')
    Found = False
    Name = input('Author Name: ')
    for i in FileHandle.readlines():
        if i[17:17 + len(Name)] == Name:
            Found = True
            print (i.strip()[19 + len(Name):])
    if Found == False:
        print('Not found')
    FileHandle.close()
    
    
    
    
while True:
    while True:
        Flag = input('Add a new book to the text file press 1, Search for books written by a given author press 2, End the program press 3: ')
        if Flag == '1' or Flag == '2' or Flag == '3':
            break
    if Flag == '1':
        addNewBook()
    elif Flag == '2':
        SearchBookByAuthor()
    elif Flag == '3':
        break

