# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:22:34 2024

@author: ASUS
"""

import math 
n=int(input("Nhập số nguyên dương n:"))
if math.sqrt(n)==int(math.sqrt(n)):
    print(f"{n} là số chính phương")
else:
    print(f"{n} không là số chính phương")
