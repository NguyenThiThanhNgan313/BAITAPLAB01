# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:44:52 2024

@author: ASUS
"""

bo_nghiem =[]
max=0
for x in range (1,490):
    for y in range (1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                sum=x+y+z
                if sum>max:
                    max=sum
                bo_nghiem +=[(x,y,z)]
print(f"{bo_nghiem} có giá trị lớn nhất {x+y+z}={max}")

