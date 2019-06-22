#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:57:27 2019

@author: superallen
"""

import matplotlib.pyplot as plt

x = [1, 3, 5]
y = [1, 2, 3]

x2 = [2, 4, 6]
y2 = [3, 2, 1]


plt.bar(x, y, label='Bar_1', color='b')
plt.bar(x2, y2, label='Bar_2', color='c')

plt.xlabel('\nCompy Name')
plt.ylabel('2018 sales')
plt.title('A --> B')
plt.legend()

plt.show