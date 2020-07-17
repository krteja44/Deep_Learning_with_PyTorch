# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:32:00 2020

@author: ravit
"""


import numpy as np

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result