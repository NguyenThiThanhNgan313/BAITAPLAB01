# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:45:51 2024

@author: ASUS
"""

#gan y,z=1 
#2*x+7*1 +9*1 = 979
#=> x = (979 - (7+9)/2= 485.5
#2*1+7*y +9*1 = 979
#=> y =(979-(2+9))/7=138.5
#2*1+7*1+9*z=979
#=> z = (979-(2+7))/9 = 108
bo_nghiem =[]
for x in range (1,490):
    for y in range (1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                bo_nghiem +=[(x,y,z)]
print(bo_nghiem)

