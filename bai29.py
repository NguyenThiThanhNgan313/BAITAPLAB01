# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:03:49 2024

@author: ASUS
"""

n = int(input("Nhập các số N nguyên dương = "))
while n<=0:
    n=int(input("Nhập lại n:"))
s=0
for i in range(1,n+1):
    s += n % 10
    n //= 10
print("Tổng các chữ số của =", s)