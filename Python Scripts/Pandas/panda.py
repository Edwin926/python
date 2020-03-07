# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:18:55 2020

@author: CEC
"""

import pandas as pd
titulos=pd.read_csv('data/titles.csv')
print(titulos.head(100))
print("\n"*2)
elenco=pd.read_csv('data/cast.csv',encoding='utf-8')
print(elenco.head(10))

#Cuantas peliculas estan listadas en el datafram de titles
print(len(titulos))
#Cual fue la primer pelicula hecha titulada "Romeo and Juliet"
print(titulos[titulos.title=="Romeo and Juliet"].sort_values('year').head(5))
#Listar todas las peliculas que contenfan la palabra "Exorcist"
#ordendads de la mas viej a la mas reciente
#print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))
#print(titulos[titulos.title.str.contains("Star Wars")].sort_values('year'))
#print(titulos[titulos.title=="Star Wars"].sort_values('year').head(5))


print(titulos[titulos.year==1980].sort_values('year'))
total=0
for i in range(1980,2001):
    print(titulos[titulos.year==i].sort_values('year'))
    total=total+len(titulos[titulos.year==i].sort_values('year'))
print(total)
print(titulos[titulos.year.between(1980,2000)])

print(elenco[elenco.title=="The Godfather"])
#print(titulos[titulos.title=="Taxi Driver"].sort_values('year').head(5))