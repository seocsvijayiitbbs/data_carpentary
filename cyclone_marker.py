#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author      : Vijay Vishwakarma
@designation : Research Scholar
@institution : Indian Institute of Technology-Bhubaneswar

"""

#%%%

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath

def get_hurricane():
    u = np.array([  [2.444,7.553],
                    [0.513,7.046],
                    [-1.243,5.433],
                    [-2.353,2.975],
                    [-2.578,0.092],
                    [-2.075,-1.795],
                    [-0.336,-2.870],
                    [2.609,-2.016]  ])
    u[:,0] -= 0.098
    codes = [1] + [2]*(len(u)-2) + [2] 
    u = np.append(u, -u[::-1], axis=0)
    codes += codes

    return mpath.Path(3*u, codes, closed=False)

hurricane = get_hurricane()

#%%
plt.scatter([1,1,2],[1.4,2.3,2.8], s=350, marker=hurricane, 
            edgecolors="crimson", facecolors='none', linewidth=2)
plt.scatter([0,1,2],[1,3,1], s=150, marker=hurricane, 
            edgecolors="k", facecolors='none')
plt.scatter([0,1.8,3],[0,2,4], s=150, marker="o", 
            edgecolors="k", facecolors='none')

plt.show()

#%%