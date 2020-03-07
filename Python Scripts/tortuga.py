# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:30:03 2020

@author: CEC
"""

#Modulos excepciones, try-except
#https://docs.python.org/3/library/index.html
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()