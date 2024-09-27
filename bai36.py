# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:37:20 2024

@author: ASUS
"""

n=int(input("Nhập số nguyên dương n:"))
s=0
for i in range(1,n+1):
    s+=i**2
print("Tổng=",s)