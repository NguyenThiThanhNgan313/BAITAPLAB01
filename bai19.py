# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:40:41 2024

@author: ASUS
"""

a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
d=int(input("Nhập d:"))
if a<b and a<c and a<d:
    print("Số nhỏ nhất là:",a)
elif b<a and b<c and b<d:
    print("Số nhỏ nhất là:",b)
elif c<a and c<b and c<d:
    print("Số nhỏ nhất là:",c)
elif d<a and d<b and d<c:
    print("Số nhỏ nhất là",d)
else:
    print("Lựa chọn không hợp lệ")
    
    