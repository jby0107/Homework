# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:53:51 2019

@author: jiang
"""
import subprogram




InitialiseBoard()
SetUpGame()
while True:
    OutputBoard()
    ThisPlayerMakesMove()
    if CheckForFullBoard()==True or CheckIfThisPlayerHasWon()==True:
        break
    else:
        ThisPlayer=SwapThisPlayer()

