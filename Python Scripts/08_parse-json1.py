# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:48:32 2020

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
print(json_data)