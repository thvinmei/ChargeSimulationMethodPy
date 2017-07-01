#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:39:04 2017
@author: toshiaki
Charge Simulation Method (Method of Fundamental Solutions) for 2D-Laplace's equation in Circular area.
"""
import numpy as np
from scipy.linalg import solve as solve
import math as math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from BoundaryCondition import BoundaryConditionP as BoundaryCondition
from Green import DoubleDimension as Green


if __name__ == '__main__':
    N = int(input())
    delta = 0.3
    
    # Grid config
    NX = 100
    NY = 100
    minX = -1
    maxX = 1
    minY = -1
    maxY = 1
    L = maxX - minX
    dx = (maxX - minX ) / NX
    dy = (maxY - minY ) / NY
    X = np.arange(minX, maxX, dx)
    Y = np.arange(minY, maxY, dy)
    GX,GY = np.meshgrid(X,Y)
    
    CollocationPoints = np.zeros((N,2)) #Collocation points init.
    ChargePoints = np.zeros((N,2)) #Charge Points init.
    dTheta = 2 * math.pi / N
    G = np.zeros((N,N))
    q = np.zeros(N) 
    f = np.zeros(N)
    psi = np.zeros((NX,NY))
    
    for i in range(N):
        CollocationPoints[i,0] = math.cos(dTheta*i)
        CollocationPoints[i,1] = math.sin(dTheta*i)

        ChargePoints[i,0] = (1+delta) * math.cos(dTheta*i)
        ChargePoints[i,1] = (1+delta) * math.sin(dTheta*i)
        
        f[i] = BoundaryCondition(CollocationPoints[i,0],CollocationPoints[i,1])
    
    for i in range(N):
        for j in range(N):
            G[i,j] = Green(CollocationPoints[i,0],CollocationPoints[i,1],ChargePoints[j,0],ChargePoints[j,1])
    
    q = solve(G,f)
    
    for x in range(NX):
        for y in range(NY):
            for i in range(N):
                psi[x,y] = psi[x,y] + q[i] * Green(X[x],Y[y],ChargePoints[i,0],ChargePoints[i,1])

    graph = Axes3D(plt.figure()).plot_surface(GY,GX,psi)
    plt.show()