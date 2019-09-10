# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:54:31 2019

@author: jiang
"""
#a
Tally=[0 for i in range(5)]

'''b
while True:
    Choice=int(input('1 for Reading, 2 for computer games, 3 for Sports,\
                     4 for Programming, 5 for TV, 0 to end input'))
    if Choice==0:
        break
    else:
        Tally[Choice-1]+=1
for i in range(5):
    print(Tally[i])
'''

#c
Title=['1 Reading books       ', '2 Play computer games ', '3 Sport               ',\
       '4 Programming         ', '5 Watching TV         ']
while True:
    Choice=int(input('1 for Reading, 2 for computer games, 3 for Sports,\
                     4 for Programming, 5 for TV, 0 to end input: '))
    if Choice==0:
        break
    else:
        Tally[Choice-1]+=1
FileHandle=open('TallyResult.TXT','w')
for i in range(5):
    print(Title[i]+Tally[i]*'/')
#d
    FileHandle.write(Title[i]+Tally[i]*'/'+'\n')
FileHandle.close()

#e
FileHandle=open('TallyResult.txt','r')
Tally=[]
n=0
for line in FileHandle.readlines():
    Tally.append(line.strip())
    print(Tally[n])
    n+=1
FileHandle.close()







