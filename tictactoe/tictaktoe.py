# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:59:18 2019

@author: jiang
"""

import pygame, sys
from pygame.locals import *

def InitialiseBoard():
    global Board
    Board=[[' ' for i in range(3)] for i in range(3)]

def SetUpGame():
    global ThisPlayer
    ThisPlayer='White'
    
def Check(RowNumber,ColumnNumber):
    if Board[RowNumber][ColumnNumber]==' ':
        return True

def CheckVertical(ColumnNumber):
    if Board[0][ColumnNumber]==Board[1][ColumnNumber]==Board[2][ColumnNumber]:
        return True

def CheckHorizontal(RowNumber):
    if Board[RowNumber][0]==Board[RowNumber][1]==Board[RowNumber][2]:
        return True

def CheckDiagnol():
    if Board[1][1]!=' ':
        if Board[0][0]==Board[1][1]==Board[2][2] or Board[0][2]==Board[1][1]==Board[2][0]:
            return True

def CheckWon():
    if CheckVertical(ColumnNumber)==True or CheckHorizontal(RowNumber)==True or CheckDiagnol()==True:
        return True

def CheckFull():
    for i in range(3):
        if ' ' in Board[i]:
            return False
    return True

def SwapPlayer():
    if ThisPlayer=='White':
        ThisPlayerNew='Black'
    else:
        ThisPlayerNew='White'
    return ThisPlayerNew

def WonOutput():
    outputStr = (ThisPlayer+' Won!')
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
    Rect=pygame.Rect(ColumnNumber*CellWidth+4,RowNumber*CellHeight+4,PieceWidth,PieceHeight)
    if Board[RowNumber][ColumnNumber]=='White':
        WindowSurface.blit(WhiteImage,Rect)
    else:
        WindowSurface.blit(BlackImage,Rect)

def terminate():
    pygame.quit()
    sys.exit()
    
InitialiseBoard()
SetUpGame()
Black = (255, 255, 255)
Blue = (0, 0, 255)
CellWidth = 100
CellHeight = 100
PieceWidth = 94
PieceHeight = 94    

pygame.init()
BoardImage=pygame.image.load('Board.png')
BoardRect=BoardImage.get_rect()
WhiteImage=pygame.image.load('White.png')
BlackImage=pygame.image.load('Black.png')
basicFont = pygame.font.SysFont(None, 48)

WindowSurface=pygame.display.set_mode((BoardRect.width,BoardRect.height))
pygame.display.set_caption('Tic-Tak-Toe')

WindowSurface.blit(BoardImage, BoardRect)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            terminate()
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            x,y=pygame.mouse.get_pos()
            ColumnNumber=int(x/CellWidth)
            RowNumber=int(y/CellHeight)
            if Check(RowNumber,ColumnNumber)==True:
                Board[RowNumber][ColumnNumber]=ThisPlayer
                UpdateBoard()
                if CheckWon()==True:
                    WonOutput()
                elif CheckFull()==True:
                    DrawOutput()
                else:
                    ThisPlayer=SwapPlayer()
    pygame.display.update()
        
    