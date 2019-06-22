#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:17:59 2019

@author: superallen
"""

import matplotlib.pyplot as plt

a_CityAge = [1, 2, 5, 6, 7, 10, 11, 13, 11, 16, 18, 20, 22, 45, 34, 12]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

plt.hist(a_CityAge, bins, histtype='bar', rwidth=0.8)
plt.xlabel('Age')
plt.ylabel('Num')
plt.title('CityAge')
plt.show