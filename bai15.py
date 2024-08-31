# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:27:36 2024

@author: ASUS
"""

import math
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
bt1=a+b
bt2=a**(1/3)+b**(1/3)
bt3=(a*b)**(1/3)
bt4=a**(1/3)
bt5=b**(1/3)
ketqua=((bt1/bt2)-bt3)/(bt4-bt5)**2
print("kết quả =",round(ketqua,3))