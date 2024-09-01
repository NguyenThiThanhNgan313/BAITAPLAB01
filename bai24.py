# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:45:48 2024

@author: ASUS
"""

h=int(input("Nhập giờ:"))
p=int(input("Nhập phút:"))
s=int(input("Nhập giây:"))
print("Giây,phút,giây",h,p,s)
if h < 0 or h >23:
    print("Giờ không hợp lệ!")
elif p < 0 or p > 59 :
    print("Phút không hợp lệ!")
elif s < 0 or s > 59:
    print("Giây không hợp lệ!")
else:
    print("Giờ, phút, giây đều hợp lệ!")