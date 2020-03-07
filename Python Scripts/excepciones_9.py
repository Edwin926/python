# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:57:57 2020

@author: CEC
"""

def readint(prompt,mini,maxi):
    flag=True

    
    while flag==True:
        try:
            num=int(input("Enter a number from "+str(mini)+"to"+str(maxi)+": "))
            assert num>=mini and num<=maxi
            return num
            break
          
        except:
            print("Error:Wrong input")
        finally:
            print("Error: the value is not within permitted range ("+str(mini)+"..."+str(maxi)+")")
            
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)