#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:02:06 2017
@author: toshiaki
set BoundaryCondition
"""
import math

def BoundaryConditionS(x,y):
    if y == -1:
        return (1-math.fabs(x))/2
    elif y == 1:
        return math.sin(math.pi * x /2 + 0.5 * math.pi )
    else:
        return 0   

def BoundaryConditionC(x,y):
    return math.sin(math.pi * x)

def BoundaryConditionP(x,y):
    return (x+y)/2

def BoundaryConditionH(x,y):
    if y == 1:
        return 10
    else:
        return 0