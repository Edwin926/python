# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:22:13 2020

@author: CEC
"""

devices=["R1","R2","R3","S1","S2"]
for i in devices:
    if "R" in i:
        print(i)
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)