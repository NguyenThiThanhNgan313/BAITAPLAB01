# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:56:15 2024

@author: ASUS
"""

n=int(input("Nhập số nguyên dương n:"))
s=0
for i in range(1,n+1):
    s+=1/i
print("Tổng=",round(s,3))