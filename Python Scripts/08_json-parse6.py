# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:27:44 2020

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
    json_status=json_data["info"]["statuscode"]
    if (json_data["route"]["routeError"]["errorCode"])==-400:
        print("datos incorrectos")
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("Has Highways: " + str(((json_data["route"]["hasHighway"]))))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        