# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:21:23 2024

@author: ASUS
"""

# a) S = 1 + 2 + 3 + ...... + n
def a(n):
    s = 0
    for i in range(1,n+1):
        s = s + i
    return s
print(a(3))
# b) S = 1^2 + 2^2 + 3^2 + ...... + n^2
def b(n):
    s = 0
    for i in range(1,n+1):
        s = s + i**2
    return s
print(b(6))

# c) S = 1 + 1/2 + 1/3 + ...... + 1/n
def c(n):
    s = 0
    for i in range(1,n+1):
        s = s + (1/i)
    return s

print(c(8))


# d) S = 1! + 2! + 3! + ...... + n!
def d(n):
    s = 0
    giaithua = 1
    for i in range(1,n+1):
        giaithua += i 
        s += giaithua
    return s

print(d(5))  
# e) S = 1 * 2 * 3 * ...... * n
def e(n):
    giaithua = 1
    for i in range(1,n+1):
        giaithua *= i 
    return giaithua


print(e(3))