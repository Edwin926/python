# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:52:54 2020

@author: CEC
"""
def fibonacci(n):
    serie=[0,1]
    for i in range(1,n):
        serie.append(serie[i-1]+serie[i])
    return serie
#print(fibonacci(int(input("Ingrese un numero: "))))
