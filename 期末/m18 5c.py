# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:44:14 2020

@author: jiang
"""

def AddNewScore():
    FileHandle = open('ScoreDetails.txt', 'w')
    Date = input('Date: ')
    while True:
        MemberShipNumber = input('MemberShipNumber: ')
        if MemberShipNumber == '':
            FileHandle.close()
            break
        else:
            Score = input('Score: ')
            while int(Score) > 99 or int(Score) < 50:
                Score = input('Score: ')
            String = MemberShipNumber + Date + Score
            FileHandle.write(String + '\n')