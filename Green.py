#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:06:12 2017
@author: toshiaki
Green Functions
"""
import math

def SingleDimension(x,xi):
    return -1 / 2 * math.fabs(x-xi)

def DoubleDimension(x,y,xi,eta):
    inrt = pow(x-xi,2) + pow(y-eta,2)
    return -1 * math.log(math.sqrt(inrt)) / (2 * math.pi)

def TripleDimension(x,y,z,xi,eta,zeta):
    inrt = pow(x-xi,2) + pow(y-eta,2) + pow(z-zeta,2)
    return 1 / (4 * math.pi) / math.sqrt(inrt)