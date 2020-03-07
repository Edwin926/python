# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:51:36 2020

@author: CEC
"""

import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
key="BsWVSJ24QpyrtBo50H4wF7i745pgkR7g"
while True:
    orig=input("Starting Location: ")
    if orig=="quit" or orig=="q":
        break
    dest=input("Destination: ")
    if dest=="quit" or dest=="q":
        break
    
    url=main_api+urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: "+(url))

json_data=requests.get(url).json()
#print(json_data)

#json_status=json_data["info"]["statuscode"]
#if json_status==0:
    #print("API Status: "+str(json_status)+"=A succesful route call.\n")