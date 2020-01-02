# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 21:41:58 2020

@author: jiang
"""

import random


Picture = [[''for i in range(8)]for i in range(8) ]
for Row in range(8):
    for Column in range(8):
        Picture[Row][Column] = random.randint(0,255)

print(Picture)
def Lighten():
    Flag = False
    for Row in range(8):
        for Column in range(8):
            Pixel = int(Picture[Row][Column] * 1.1)
            if Pixel > 255:
                Flag = True
                Pixel = 255
            Picture[Row][Column] = Pixel
    print(Picture)
    return Flag