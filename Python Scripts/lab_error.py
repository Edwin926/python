# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:29:52 2020

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
        
                
        except ValueError:
            print("Error:Wrong input")
        except:
            print("Error: the value is not within permitted range ("+str(mini)+"..."+str(maxi)+")")
            
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
