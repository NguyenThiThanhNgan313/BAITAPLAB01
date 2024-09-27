# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:01:34 2024

@author: ASUS
"""

thang = int(input("Nhập vào tháng: "))
nam = int(input("Nhập vào năm: "))
if 1 <= thang <= 12: 
    if thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            ngay = 29
        else:
            ngay = 28
    if thang in [1,3,5,7,8,10,12] :
         ngay = 31 
    elif thang in [4,6,9,11] :
         ngay = 30 
    print(f"Tháng {thang} năm {nam} có {ngay} ngày.")