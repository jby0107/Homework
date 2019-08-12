# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:19:46 2019

@author: jiang
"""

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
print(foo(3, 0))
