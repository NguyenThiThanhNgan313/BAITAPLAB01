# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:58:25 2024

@author: ASUS
"""

n=int(input("Nhập số nguyên dương n:"))
s=0
for i in range(1,n+1):
    s+=1/(2*i+1)
print("Tổng=",round(s,3))