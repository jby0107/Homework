# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:06:22 2019

@author: jiang
"""

import random
Name=['Daniel Chu','Harry Fang','Nico Jiang','Jack Jin','James Liu','Brian Shan',\
      'Tim Xing','Lisa Xu','Cathy Yang','Julian Ye','Shirley Zeng','Andy Zhang']
FileHandle=open("AS_CS_opt2_gradebook.txt",'w')
MathTotal=90*len(Name)
CSTotal=95*len(Name)
PhyTotal=88*len(Name)
def RandomScore(Total,Subject):
    for i in range(len(Name)):
        if i==(len(Name)-1):
            Subject.append(str(Total))
            break
        while True:
            Score=random.randint(80,100)
            if (Total-Score)/(len(Name)-1-i)<=100:
                Total-=Score
                Subject.append(str(Score))
                break
    return Subject


def insertID(NumberOfStudent):
    ID=[]
    for i in range(1,NumberOfStudent+1):
        ID.append(i)
    return ID


def CalAverage(MathScore,CSScore,PhyScore):
    Average=[]
    for i in range(len(Name)):
        Average.append(str(round((int(MathScore[i])+int(CSScore[i])+int(PhyScore[i]))/3)))
    return Average


def Daniel():
    for i in range(len(Name)):
        if 'Daniel' in Name[i]:
            MathScore[i]=str(round(int(MathScore[i])*1.1))
    return MathScore

def LowPhy():
    Temp=None
    for i in range(len(PhyScore)-1):
        if int(PhyScore[i])>=int(PhyScore[i+1]):
            Temp=i+1
        else:
            Temp=i
    return Temp
        



MathScore=RandomScore(MathTotal,[])
CSScore=RandomScore(CSTotal,[])
PhyScore=RandomScore(PhyTotal,[])


#Task1
for i in range(len(Name)):
    FileHandle.write(Name[i]+' '+MathScore[i]+' '+CSScore[i]+' '+PhyScore[i]+'\n')


FileHandle.close()   
Cont=input('press enter to continue: ')   
#Task2
FileHandle=open("AS_CS_opt2_gradebook.txt",'w')
ID=insertID(len(Name))
for i in range(len(Name)):
    FileHandle.write(str(ID[i])+Name[i]+' '+MathScore[i]+' '+CSScore[i]+' '+PhyScore[i]+'\n')

FileHandle.close()
Cont=input('press enter to continue: ')
#Task3
FileHandle=open("AS_CS_opt2_gradebook.txt",'w')
Average=CalAverage(MathScore,CSScore,PhyScore)
for i in range(len(Name)):
    FileHandle.write(str(ID[i])+Name[i]+' '+\
                     MathScore[i]+' '+CSScore[i]+' '+PhyScore[i]+' '+Average[i]+'\n')

FileHandle.close()
Cont=input('press enter to continue: ')
#Task4
FileHandle=open("AS_CS_opt2_gradebook.txt",'w')
MathScore=Daniel()
Average=CalAverage(MathScore,CSScore,PhyScore)
for i in range(len(Name)):
    FileHandle.write(str(ID[i])+Name[i]+' '+\
                     MathScore[i]+' '+CSScore[i]+' '+PhyScore[i]+' '+Average[i]+'\n')

FileHandle.close()
Cont=input('press enter to continue: ')
#Task5
FileHandle1=open('new-gradebook.txt','w')
ID=insertID(len(Name)-1)
Lowest=LowPhy()
for i in range(len(Name)):
    if i != Lowest:
        FileHandle1.write(str(ID[i])+Name[i]+' '+\
                         MathScore[i]+' '+CSScore[i]+' '+PhyScore[i]+' '+Average[i]+'\n')
FileHandle.close()
FileHandle1.close()
    


