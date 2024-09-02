# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:42:50 2024

@author: ASUS
"""

a=int(input("Nhập a = "))
b=int(input("Nhập b = "))
c=int(input("Nhập c = "))
if a>b:
    a,b=b,a
elif a>c:
    a,c=c,a
elif b>c:
    b,c=c,b
print("Thứ tự tăng dần của các số: ",a,b,c)
