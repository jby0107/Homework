# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:02:18 2019

@author: jiang
"""

FileHandle=open('NewEmailDetails.txt','w')
FileHandle1=open('EmailDetails.txt','r')
for Lines in FileHandle1.readlines():
    FileHandle.write('00'+Lines)
FileHandle.close()
FileHandle1.close()
