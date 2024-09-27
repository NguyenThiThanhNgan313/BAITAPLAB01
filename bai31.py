# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:33:50 2024

@author: ASUS
"""

a= int(input(" Nhập vào a="))
b= int(input(" Nhập vào b="))
c= int(input(" Nhập vào c="))
if a+b>c or a+c>b or c+b>a:
    print(" Ba cạnh này tạo thành một tam giác")
else:
    print("Ba cạnh này không tạo thành một tam giác")
if a==b==c:
    print("Ba cạnh tạo thành tam giác đều")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
    print("Ba cạnh tạo thành tam giác vuông")
elif a==b or a==c or c==b:
    print("Ba cạnh tạo thành tam giác cân")
else:
    print("Ba cạnh tạo thành tam giác thường")