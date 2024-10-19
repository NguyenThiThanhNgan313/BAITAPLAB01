# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:48:30 2024

@author: ASUS
"""
#52/a
def canbac (x,n):
    return x**(1/n)


if __name__=="__main__":
    print(canbac (8,3))
    


#b
def sodao(n):
    #str:chuỗi, chữ số
    #return str(n)[::-1]
    return int(str(n)[::-1])
if __name__=="__main__":
    print(sodao(123450))


#cách3
def dao(n):
    dao=0
    while n>0:
        dao=dao*10+n%10
        n//=10
    return dao
if __name__=="__main__":
    print(dao(123450))


#c
import math
def chinhphuong(n):
    return int(math.sqrt(n))**2 == n
if __name__=="__main__":
    print(chinhphuong(1))



#d số nguyên tố chia hết cho 1 và chính nó, số 2 là số nguyên tố 
def ktra_ngto(n):
    if n<2:
        return False 
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
if __name__=="__main__":
    print( ktra_ngto(2))


#e

def tich_sole(n):
    tich=1
    for i in str(n):
        if n%2 !=0:
            tich *= int(i)
    return tich
if __name__=="__main__":
    print( tich_sole(195))
    

#f 
def tong_ngto(n):
    tong_ngto=0
    for i in range(2,n):
        if ktra_ngto(i):
            tong_ngto += i
    return tong_ngto

if __name__=="__main__":
    print( tong_ngto(20))
    


#g
def tong_chinhphuong(n):
    tong=0
    for i in range(1,n):
        if chinhphuong(i):
            tong+= i
    return tong 
if __name__=="__main__":
    print(tong_chinhphuong(17))#tính những số nhỏ hơn n(17:1,4,9,16)
    
    
#h
def tong_uoc(n):
    tong = 0
    for i in range(1,n+1):
        if n%i == 0:
            tong += i
    return tong
    
if __name__=="__main__":
    print(tong_uoc(4))#chia hết cho nó (4=>1,2,4=>Tổng:7)import math

    



    