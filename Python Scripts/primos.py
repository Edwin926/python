# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:18:19 2020

@author: CEC
"""
n=int(input("Ingrese el numero a validar: "))
def isPrime(n):
    valor=True
    for i in range (2, n):

        if n%i==0:
            valor=False
    return valor
print(str(isPrime(n)))


for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")

