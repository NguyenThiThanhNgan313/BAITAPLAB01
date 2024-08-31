# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:18:16 2024

@author: ASUS
"""


a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
if a>b and a>c:
    print("Số lớn nhất là:",a)
elif b>a and b>c:
    print("Số lớn nhất là:",b)
elif c>a and c>b:
    print("Số lớn nhất là:",c)
else:
    print("Lựa chọn không hợp lệ")