# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:27:54 2020

@author: CEC
"""

import numpy as np
import sys
print("USO DE MEMORIA PYTHON")
S=range(1000)
print(sys.getsizeof(5)*len(S))
print("\n"*1)
print("USO DE MEMORIA NUMPY")
D=np.arange(1000)
print(D.size*D.itemsize)

array=np.array([[1,2,3,4],[5,6,7,8]],dtype=np.int64)
print (array)