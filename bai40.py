# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:45:16 2024

@author: ASUS
"""

n=int(input("Nhập n:"))
s=0
if n<=0 or n%2!=0:
    print(" Nhập n: ")
else:
   for i in range(2,n+1,2):
    s+=1/i
print("Tổng=",round(s,3))