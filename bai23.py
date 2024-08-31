# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:06:31 2024

@author: ASUS
"""

import math
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
delta =b**2-4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    x=-b/(2*a)
    print ("Phương trình có nghiệm kép x1= x2=",x)
elif delta >0:
    x1=(-b + math.sqrt(delta)/2*a)
    x2=(-b - math.sqrt(delta)/2*a)
    print ("Phương trình có hai nghiệm phân biệt x1= x2=",x1,x2)