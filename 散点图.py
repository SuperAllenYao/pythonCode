#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:55:12 2019

@author: superallen
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 3, 5, 6, 3, 4, 5, 2, 5, 7]

plt.scatter(x, y, label='ssssss')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sc')
plt.legend()
plt.show()