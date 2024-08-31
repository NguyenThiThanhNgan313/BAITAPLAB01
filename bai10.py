# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:48:54 2024

@author: ASUS
"""

n=int(input("Nhập biển số xe của bạn:"))
n=str(n) ; s=0
for i in range(len(n)) :
    s+=int(n[i])
print("Biển số xe của bạn có số nút là :", s%10)