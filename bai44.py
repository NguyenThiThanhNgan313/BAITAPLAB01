# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:16:34 2024

@author: ASUS
"""
s=0
n=int(input(" Nhập số n:"))
while n<=0:
    n=int(input("Nhập lại n:"))
for i in range (1,n+1):
    s+=(2*i+1)/(2*i+2)
print(round(s,2))
    