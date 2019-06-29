# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:16:10 2019

@author: jiang
"""

from random import choice

class RandomWalk():
    def __init__(self,num_of_points=5000):
        self.num=num_of_points
        self.x_value=[0]
        self.y_value=[0]
        
        
    def random_walk(self):
        while len(self.x_value)<self.num:
            x_direction=choice([-1,1])
            x_step=choice([0,1,2,3,4])
            x_distance=x_step*x_direction
            
            y_direction=choice([-1,1])
            y_step=choice([0,1,2,3,4])
            y_distance=y_step*y_direction
            
            if x_distance==0 and y_distance==0:
                continue
            
            next_x=self.x_value[-1]+x_distance
            next_y=self.y_value[-1]+y_distance
            
            self.x_value.append(next_x)
            self.y_value.append(next_y)
            
            
            
import matplotlib.pyplot as plt

rw=RandomWalk(10000)
rw.random_walk()
point_numbers = list(range(rw.num))
plt.figure(dpi=128, figsize=(10, 6))
plt.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap='jet',edgecolor='none',s=15)
plt.scatter(0, 0, c='red', edgecolors='none', s=100)
plt.scatter(rw.x_value[-1], rw.y_value[-1], c='green', edgecolors='none',
s=100)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
            
            