# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:11:27 2019

@author: jiang
"""


from PIL import Image
import matplotlib.pyplot as plt


IMG = Image.open('image.jpg')
One = IMG.convert('1')
P = IMG.convert('P')
RGB = IMG.convert('RGB')
RGBA = IMG.convert('RGBA')
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.set_title('1bit')
ax2 = fig.add_subplot(222)
ax2.set_title('8bits')
ax3 = fig.add_subplot(223)
ax3.set_title('24bits')
ax4 = fig.add_subplot(224)
ax4.set_title('32bits')
ax1.imshow(One)
ax2.imshow(P)
ax3.imshow(RGB)
ax4.imshow(RGBA)
plt.show()
plt.savefig('convert.jpg')




















