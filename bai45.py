# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:58:24 2024

@author: ASUS
"""
ts=1
ms=0
s=0
n=int(input(" Nhập số n:"))
while n<=0:
    n=int(input("Nhập lại n:"))
x=float(input("Nhập x:"))
    


for i in range (1,n+1):
    ts=x**i
    ms=ms+i
    s+=ts/ms
print(round(s,2))
    
    