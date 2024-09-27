# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:00:47 2024

@author: ASUS
"""

n=int(input("Nhập n:"))
s=0
while n<=0:
    n=int(input("Nhập n:"))
for i in range(1,n+1):
    s+=1/(i*(i+1))
    print("Tổng",s)