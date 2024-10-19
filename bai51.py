# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:43:56 2024

@author: ASUS
"""

def ktra_giatri():
    n= input("Nhập n:")
    if n.replace('.','',1).replace('-','',1).isdigit():
      n=float(n)
    #if n.lstrip('-').isdigit():(-)123
    #n = int(n)
    #if n.strip('-').isdigit():(-)123
    #n = int(n)
      
    if -89 <=n<= 90:
        return n
    print("Không hợp lệ, nhập lại")
    return ktra_giatri()

print(ktra_giatri())