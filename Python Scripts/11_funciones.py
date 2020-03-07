# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:22:21 2020

@author: CEC
"""

def message():
    print("Enter a value: ")
    
message()
a=int(input())
message()
b=int(input())
message()
c=int(input())

#Funciones con parametros

name=input("name")

def hi(name):
    print("Hi, ",name)

hi(name)

#Funciones con multiples parametros
def hiAll(name1,name2):
    print("hi, ",name2)
    print("hi, ",name1)
hiAll("Sebastian","Leo")

#Funciones con multiples parametros
def subtra(a,b):
    print(a-b)

subtra(5,2)
#Se puede definir el valor de las variables de las funciones asignando su valor a los parametros
subtra(b=2,a=5)
#Python asigna de derecha a izquierda
subtra(5,b=2)


#Uso de return, si solo pongo return me devuelve none

def multiply(a,b):
    return a*b

print(multiply(3,4))

#Return de la funcion wishes
def wishes():
    print("my wishes")
    return "Happy birthday"

wishes()

print(wishes())

#Lista como argumento de una funcion
def hiEverybody(myList):
    for name in myList:
        print("Hi, ",name)
hiEverybody(["Adam","John","Lucy"])

#Lista como return de una funcion
def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))

#Funciones lambda funciones sin nombre, super cortas
x=1
y=2
def a(x,y):
    return x+y
b=lambda x,y: x+y
print(str(b))

