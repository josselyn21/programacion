# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:24:54 2020

@author: User
"""

while True:
    x=input("ingrese un #: ")
    if x== "q" or x== "quit":
        break
    x= int(x)
    y=1
    
    while True:
        print(y)
        y=y+1
        if y>x:
            break