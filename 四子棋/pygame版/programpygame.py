# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:53:51 2019

@author: jiang
"""
import subprogrampygame
import pygame, sys
from pygame.locals import *


InitialiseBoard()
SetUpGame()
BackgroundColor = (255, 255, 255)
Black = (255, 255, 255)
Blue = (0, 0, 255)
CellWidth = 100
CellHeight = 100
PieceWidth = 94
PieceHeight = 94


pygame.init()
MainClock = pygame.time.Clock()
BoardImage=pygame.image.load('Board.png')
BoardRect=BoardImage.get_rect()
WhiteImage=pygame.image.load('White.png')
WhiteRect=WhiteImage.get_rect()
BlackImage=pygame.image.load('Black.png')
BlackRect=BlackImage.get_rect()

basicFont = pygame.font.SysFont(None, 48)

WindowSurface = pygame.display.set_mode((BoardRect.width, BoardRect.height))
pygame.display.set_caption('四子棋')
RowNumber=0
ColumnNumber=0
WindowSurface.fill(BackgroundColor)
WindowSurface.blit(BoardImage, BoardRect, BoardRect)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            ColumnNumber = int(x/CellWidth)
            if ColumnNumberValid(ColumnNumber)==True:
                RowNumber=FindNextFreePositionInColumn()
                Board[RowNumber][ColumnNumber]=ThisPlayer
                UpdateBoard()
                if CheckIfThisPlayerHasWon()==True:
                    WonOutput()
                elif CheckForFullBoard()==True:
                    DrawOutput()
                else:
                    ThisPlayer=SwapThisPlayer()

    

    
    
    pygame.display.update()

