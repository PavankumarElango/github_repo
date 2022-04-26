# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:52:18 2022

@author: pavan
"""
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)