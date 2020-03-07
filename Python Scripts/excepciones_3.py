# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:24:58 2020

@author: CEC
"""

def reciproco(n):
    try:
        n=1/n
    except ZeroDivisionError:
        print("Division fallida")
        return None
    else:
        print("Todo salió bien")
        return n
print(reciproco(2))
print(reciproco(0))