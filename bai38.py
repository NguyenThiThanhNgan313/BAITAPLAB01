# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:38:09 2024

@author: ASUS
"""

n=int(input("Nhập số nguyên dương n:"))
s=1
for i in range(1,n+1):
    s*=i
print("Tổng=",s)