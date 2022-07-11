# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:40:32 2022

@author: ni664326
"""

import numpy as np
    
help(np.random.uniform)
  
points = 1000000
pi = np.random.uniform(0,1,points)

circlepoints = 0
squarepoints = 0

for i in range(points):
    xpoint = np.random.uniform(0,1)
    ypoint = np.random.uniform(0,1)
    
    dist = (((xpoint-.5)**2) + (ypoint-.5)**2)**(1/2)
    
    if dist <= .5:
        circlepoints += 1
    
    squarepoints += 1

    
pi = (4 *(circlepoints/squarepoints))

print(pi)
