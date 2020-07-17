# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:56:54 2020

@author: ravit
"""


import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))