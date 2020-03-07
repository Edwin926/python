# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:25:49 2020

@author: CEC
"""

string='x'
try:
    while True:
        string=string+string
        print(len(string))
except MemoryError:
    print('Esto no es gracioso')