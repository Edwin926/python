# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:40:56 2020

@author: CEC
"""

import numpy as np

#crear una matriz de unos
unos=np.ones((3,4))
print(unos)

#Crear una matriz de ceros
ceros=np.zeros((3,4))
print(ceros)

#crear matriz con valores aleatorios
aleatorios=np.random.random((2,2))
print(aleatorios)

#Crear una matriz vacia
vacia=np.empty((3,2))
print(vacia)

#Matriz llenas de un valor
full=np.full((2,2),8)
print(full)

#comando similar a linspace, datos espaciados
espacio1=np.arange(0,30+1,5)
print(espacio1)

#linspace 5 valores entre 0 y 2
espacio2=np.linspace(0,2,5)
print(espacio2)
#Matriz identidad
identidad1=np.identity(4)
print(identidad1)
#Dimensiones de una matriz
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#Conocer el tipo de datos
a=np.array([1,2,3])
print(a.dtype)

#Conocer el tamaño y la forma de la matriz

#cambiar forma de una matriz transpuesta)
a=np.array([(18,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)


print("\n"*2)
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])

#Tomar todos los elementos
print("\n"*2)
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,1])

#Operaciones con matrices
a=np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())

#Raiz cuadrada y la desviacion estandar de la matriz
a=np.array([(1,2,3),(3,4,5)])
print("\n"*2)
print(np.sqrt(a))

#operaciones
x=np.array([(1,2,3)],[(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])
print(x+y)
print("\n"*2)
print(x-y)
print("\n"*2)
print(x*y)
print("\n"*2)
print(x/y)
print("\n"*2)


#documentacion en numpy.org/doc/

