# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:46:01 2019

@author: jiang
"""

from PIL import Image
import math
import matplotlib
#matplotlib.rcParams['backend'] = 'SVG'
import matplotlib.pyplot as plt


List = []
n = 50
for i in range(500):
    List.append(math.sin(n))
    n -= 0.1
plt.plot(List)
plt.savefig('img.svg',format = 'svg')

img = Image.open('img.jpg')
img.save('img.bmp')
















