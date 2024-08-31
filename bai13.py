# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:35:47 2024

@author: ASUS
"""

ngay=int(input("Ngày sinh:"))
thang=int(input("Tháng sinh:"))
nam=int(input("Năm sinh:"))
print(f"{ngay}/{thang}/{nam}")
namrutgon=nam%100
print(f"{ngay}/{thang}/{namrutgon:02}")
print(f"{nam}/{thang}/{ngay}")