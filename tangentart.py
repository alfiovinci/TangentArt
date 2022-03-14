#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:07:23 2022

@author: alfio
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')


# Define tangent lines determination algorithm
def tangentart(x1,x2,y,N):

    x = np.linspace(x1,x2,N)
    
    dy = []
    for i in range(0,len(x)-1):
        temp = np.polyfit([x[i],x[i+1]],[y(x[i]),y(x[i+1])],1)
        dy.append(np.poly1d(temp)(x))
    
    return x, y, dy


# Compute variables
[x,y,dy] = tangentart(x1=float(sys.argv[1]), x2=float(sys.argv[2]), y=lambda x: eval(sys.argv[3]), N=int(sys.argv[4]))

# Initialize figure
fig, ax = plt.subplots(figsize=(6,6))

# Plot
ax.plot(x,y(x),'r',lw=0.7,zorder=3)

for i in range(0,len(dy)):
    ax.plot(x,dy[i],'k',lw=0.2)

ax.axis('equal')
ax.set_ylim([x[0],x[-1]])
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

plt.axis('off')

plt.show()