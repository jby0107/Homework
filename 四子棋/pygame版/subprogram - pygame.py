# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:11:19 2019

@author: jiang
"""

def InitialiseBoard():
    global Board
    Board=[[' ' for i in range(7)] for i in range(6)]

def SetUpGame():
    global ThisPlayer
    ThisPlayer='White'

def ColumnNumberValid(ColumnNumber):
    Valid=False
    if 6>=ColumnNumber>=0:
        if Board[0][ColumnNumber]==' ':
            Valid=True
    return Valid

def FindNextFreePositionInColumn():
    ThisRow=5
    while Board[ThisRow][ColumnNumber]!=' ':
        ThisRow-=1
    return ThisRow

def CheckIfThisPlayerHasWon():
    WinnerFound=False
    WinnerFound=CheckHorizontalLineInValidRow()
    if WinnerFound==False:
        WinnerFound=CheckVerticalLineInValidColumn()
    return WinnerFound
def CheckHorizontalLineInValidRow():
    WinnerFoundHor=False
    for i in range(4):
        if Board[RowNumber][i]==ThisPlayer and Board[RowNumber][i+1]==ThisPlayer and Board[RowNumber][i+2]==ThisPlayer and Board[RowNumber][i+3]==ThisPlayer:
            WinnerFoundHor=True
    return WinnerFoundHor

def CheckVerticalLineInValidColumn():
    WinnerFoundVer=False
    if RowNumber==0 or RowNumber==1 or RowNumber==2:
        if Board[RowNumber][ColumnNumber]==ThisPlayer and Board[RowNumber+1][ColumnNumber]==ThisPlayer and Board[RowNumber+2][ColumnNumber]==ThisPlayer and Board[RowNumber+3][ColumnNumber]==ThisPlayer:
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
        GameFinished=True
    return GameFinished

def SwapThisPlayer():
    if ThisPlayer=='White':
        ThisPlayer1='Black'
    else:
        ThisPlayer1='White'
    return ThisPlayer1

def WonOutput():
    outputStr = ('Game over|The winner is '+ThisPlayer+'!')
    text = basicFont.render(outputStr, True, Black, Blue)
    textRect = text.get_rect()
    textRect.centerx = WindowSurface.get_rect().centerx
    textRect.centery = WindowSurface.get_rect().centery
    WindowSurface.blit(text, textRect)

def DrawOutput():
    outputStr=("It's a draw!")
    text = basicFont.render(outputStr, True, Black, Blue)
    textRect = text.get_rect()
    textRect.centerx = WindowSurface.get_rect().centerx
    textRect.centery = WindowSurface.get_rect().centery
    WindowSurface.blit(text, textRect)
def UpdateBoard():
    rectDst = pygame.Rect(ColumnNumber*CellWidth+4, RowNumber*CellHeight+4, PieceWidth, PieceHeight)
    if Board[RowNumber][ColumnNumber] == 'White':
        WindowSurface.blit(WhiteImage, rectDst, WhiteRect)
    else:
        WindowSurface.blit(BlackImage, rectDst, BlackRect)

def terminate():
    pygame.quit()
    sys.exit()