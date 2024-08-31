# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:19:27 2024

@author: ASUS
"""

giờ1 = int(input("Nhập giờ đầu tiên: "))
phút1 = int(input("Nhập phút đầu tiên: "))
giây1 = int(input("Nhập giây đầu tiên: "))
giờ2 = int(input("Nhập giờ thứ hai: "))
phút2 = int(input("Nhập phút thứ hai: "))
giây2 = int(input("Nhập giây thứ hai: "))
giờ_cộng = giờ1 + giờ2
phút_cộng = phút1 + phút2
giây_cộng = giây1 + giây2
giờ_trừ = giờ1 - giờ2
phút_trừ = phút1 - phút2
giây_trừ = giây1 - giây2
print(f"Kết quả cộng: {giờ_cộng} giờ {phút_cộng} phút {giây_cộng} giây")
print(f"Kết quả trừ: {giờ_trừ} giờ {phút_trừ} phút {giây_trừ} giây")