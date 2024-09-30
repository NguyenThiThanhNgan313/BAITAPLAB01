# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:33:09 2024

@author: ASUS
"""

n=int(input("Nhập số = "))
def chanam(a):
    return a < 0 and a % 2 == 0
print(chanam(n))