# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:51:47 2024

@author: ASUS
"""

n=int(input("Nhập n:"))
while n<=0:
    n=int(input("Nhập lại n:"))

for i in range(1,n+1):
    if n%i ==0:
        print(i)