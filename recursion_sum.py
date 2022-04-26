# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:41:51 2022

@author: pavan
"""
l=[]
def sum_digits(b):
    if(b==0):
        return l
    dig=b%10
    l.append(dig)
    sum_digits(b//10)
n=int(input("Enter a number: "))
sum_digits(n)
print(sum(l))