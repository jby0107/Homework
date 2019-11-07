# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:37:32 2019

@author: jiang
"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


img = Image.open('image.jpg')
width, height = img.size
img=img.convert('L')
data = np.matrix(img)
print(data)
plt.imshow(data, cmap = 'gray', vmin = 0, vmax = 255)













