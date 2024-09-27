# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:02:43 2024

@author: ASUS
"""

n=int(input(" Nhập số n:"))
while n<=0:
    n=int(input("Nhập lại n:"))
    
if n==2:
    print("Số 2 không phải là số nguyên tố")
for i in range(2,n+1):
    if n%i==0:
        print("Không là số nguyên tố")
        break
    else:
        print("Là số nguyên tố")    
        break