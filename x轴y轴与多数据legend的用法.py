#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:37:01 2019

@author: superallen
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [6, 2, 2, 5, 6, 8, 9, 6, 4, 7, 9, 12]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y2 = [8, 4, 4, 7, 8, 10, 11, 8, 6, 9, 11, 14]

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Whole year ')

plt.plot(x, y, label='Copy1')
plt.plot(x2, y2, label='Copy2')
plt.legend()
plt.show