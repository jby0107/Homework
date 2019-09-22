# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:53:51 2019

@author: jiang
"""


def InitialiseBoard():
    global Board
    Board=[[' ' for i in range(7)] for i in range(6)]

def SetUpGame():
    global ThisPlayer
    ThisPlayer='O'

def OutputBoard():
    print('  0123456')
    for Row in range(6):
        print(str(Row)+' ',end='')
        for Column in range(7):
            print(Board[Row][Column],end='')
        print('')
        
def ThisPlayerMakesMove():
    global ValidRow,ValidColumn
    ValidColumn=ThisPlayerChoosesColumn()
    ValidRow=FindNextFreePositionInColumn()
    Board[ValidRow][ValidColumn]=ThisPlayer

def ThisPlayerChoosesColumn():
    print('Player '+ThisPlayer+"'s turn")
    while True:
        ColumnNumber=int(input('Input column number: '))
        if ColumnNumberValid(ColumnNumber)==True:
            break
    return ColumnNumber

def ColumnNumberValid(ColumnNumber):
    Valid=False
    if 6>=ColumnNumber>=0:
        if Board[0][ColumnNumber]==' ':
            Valid=True
    return Valid

def FindNextFreePositionInColumn():
    ThisRow=5
    while Board[ThisRow][ValidColumn]!=' ':
        ThisRow-=1
    return ThisRow

def CheckIfThisPlayerHasWon():
    WinnerFound=False
    WinnerFound=CheckHorizontalLineInValidRow()
    if WinnerFound==False:
        WinnerFound=CheckVerticalLineInValidColumn()
    if WinnerFound==True:
        OutputBoard()
        print(ThisPlayer+' is the winner')
    return WinnerFound

def CheckHorizontalLineInValidRow():
    WinnerFoundHor=False
    for i in range(4):
        if Board[ValidRow][i]==ThisPlayer and Board[ValidRow][i+1]==ThisPlayer and Board[ValidRow][i+2]==ThisPlayer and Board[ValidRow][i+3]==ThisPlayer:
            WinnerFoundHor=True
    return WinnerFoundHor

def CheckVerticalLineInValidColumn():
    WinnerFoundVer=False
    if ValidRow==0 or ValidRow==1 or ValidRow==2:
        if Board[ValidRow][ValidColumn]==ThisPlayer and Board[ValidRow+1][ValidColumn]==ThisPlayer and Board[ValidRow+2][ValidColumn]==ThisPlayer and Board[ValidRow+3][ValidColumn]==ThisPlayer:
            WinnerFoundVer=True
    return WinnerFoundVer

def CheckForFullBoard():
    GameFinished=False
    BlankFound=False
    ThisRow=-1
    while True:
        ThisColumn=-1
        ThisRow+=1
        while True:
            ThisColumn+=1
            if Board[ThisRow][ThisColumn]==' ':
                BlankFound=True
            if ThisColumn==6 or BlankFound==True:
                break
        if ThisRow==5 or BlankFound==True:
            break
    if BlankFound==False:
        OutputBoard()
        print('It is a draw')
        GameFinished=True
    return GameFinished

def SwapThisPlayer():
    if ThisPlayer=='O':
        ThisPlayer1='X'
    else:
        ThisPlayer1='O'
    return ThisPlayer1


InitialiseBoard()
SetUpGame()
while True:
    OutputBoard()
    ThisPlayerMakesMove()
    if CheckForFullBoard()==True or CheckIfThisPlayerHasWon()==True:
        break
    else:
        ThisPlayer=SwapThisPlayer()

