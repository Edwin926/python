# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:57:14 2020

@author: CEC
"""

devices=[]
file=open("devices.txt","a")
while True:
    newitem=input("ingrese nuevo dispositivo, exit para temrinar: ")
    if newitem=="exit":
        break
    else:
        file.write(newitem+"\n")
file.close()
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
print(file)
print(devices)
file.close()
