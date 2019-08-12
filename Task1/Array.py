# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:01:15 2019

@author: jiang
"""
import matplotlib.pyplot as plt
import copy
bitmap_initial=[[80,80,255,80,80,255,80,80],\
                [80,80,255,80,80,255,80,80],\
                [255,80,120,120,120,120,255,80],\
                [255,80,255,255,255,255,80,80],\
                [255,80,120,120,120,120,80,80]]


def task1(bitmap):
    bitmap1=copy.copy(bitmap)
    burnt_out=False
    for i in range(len(bitmap1)):
        for x in range(len(bitmap1[i])):
            bitmap1[i][x]*=1.1
            if bitmap1[i][x]==255:
                burnt_out=True
    if burnt_out==False:
        return bitmap1
    else:
        return True





def task2(bitmap):
    bitmap2=copy.copy(bitmap)
    for i in range(len(bitmap2)):
        bitmap2[i]=bitmap2[i][::-1]
    return bitmap2


def task3(bitmap):
    MaxVal=int(input("What's the max value for the pixel:"))
    bitmap3=copy.copy(bitmap)
    for i in range(len(bitmap3)):
        for x in range(len(bitmap3[i])):
            if bitmap3[i][x]>MaxVal:
                bitmap3[i][x]=MaxVal
    return bitmap3


fig,(ax1,ax2,ax3)=plt.subplots(1,3)        
ax1.imshow(task1(bitmap_initial),cmap='gray',vmin=0,vmax=255)
ax2.imshow(task2(bitmap_initial),cmap='gray',vmin=0,vmax=255)
ax3.imshow(task3(bitmap_initial),cmap='gray',vmin=0,vmax=255)
plt.show()            
            
    

















