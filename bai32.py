# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:42:15 2024

@author: ASUS
"""

km=float(input("Nhập số km:"))
tien=0
if km==1:
    tien=15000
    print("Số tiền:", tien)
elif 1<=km<=5:
    tien = 15000+(km-1)*13500
    print("Số tiền:", tien)
elif km>=6:
    tien= 15000+4*13500+(km-5)*11000
    print("Số tiền:", tien)
elif km>120:
    #tien+=0.9 
    tien= ( 15000+4*13500+(km-5)*11000)*0.9
    print("Số tiền:",tien)
else:
    print("Không hợp lệ")