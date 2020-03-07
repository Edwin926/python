# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:51:36 2020

@author: CEC
"""

import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Escuela politecnica nacional"
dest="Escuela politecnica del ejercito"
key="BsWVSJ24QpyrtBo50H4wF7i745pgkR7g"
url=main_api+urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data=requests.get(url).json()
#print(json_data)
print("URL_ "+(url))
json_status=json_data["info"]["statuscode"]
if json_status==0:
    print("API Status: "+str(json_status)+"=A succesful route call.\n")