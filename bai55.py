# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:23:01 2024

@author: ASUS
"""

def chu_vi(dai,rong): 
    return 2*(dai+rong)
def dien_tich(dai,rong):
    return dai*rong
def hinh_ve(dai,rong):
    for i in range(dai):
            print('*' * rong)
     
dai = int(input("Nhập chiều dài hình chữ nhật: "))
rong = int(input("Nhập chiều rộng hình chữ nhật: "))

chuvi = chu_vi(dai,rong)
dientich = dien_tich(dai,rong)

print(f"Chu vi hình chữ nhật là: {chuvi}")
print(f"Diện tích hình chữ nhật là: {dientich}")

print("Hình chữ nhật:")
hinh_ve(dai,rong)