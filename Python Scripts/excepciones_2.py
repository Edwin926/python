# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:51:56 2020

@author: CEC
"""

try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("you cannot divide by zero, sorry")
except ValueError:
    print("You mus enter an integer value")
except:
    print("oh dear, something went worng...")
print("THE END")
        