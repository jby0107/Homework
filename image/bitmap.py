# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:53:03 2019

@author: jiang
"""

import matplotlib.pyplot as plt
from PIL import Image

Array = [[]for i in range(50)]
for i in range(50):
    if i % 2 == 0:
        n = 0
    else:
        n = 255
    for x in range(50):
        Array[i].append(n)
        if n == 0:
            n = 255
        else:
            n = 0



plt.imshow(Array, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
plt.savefig('bitmap.jpg')
plt.savefig('bitmap.svg')
plt.savefig('bitmap.png')
img = Image.open('bitmap.png')
img.save('bitmap.bmp')
img.save('bitmap.gif')