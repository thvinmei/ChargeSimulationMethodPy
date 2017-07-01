#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:37:04 2017
@author: toshiaki
Charge Simulation Method (Method of Fundamental Solutions) for 2D-Laplace's equation in Square area.
"""
import numpy as np
from scipy.linalg import solve as solve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from BoundaryCondition import BoundaryConditionH as BoundaryCondition
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

    G = np.zeros((N,N))
    q = np.zeros(N) 
    f = np.zeros(N)
    psi = np.zeros((NX,NY))
    dL = 4 * L / N
    
    for i in range(N):
        l = dL * i
        
        if 0<l<2: # West area
            CollocationPoints[i,0] = minX
            CollocationPoints[i,1] = minY+l
        elif 2<l<4: # North area
            CollocationPoints[i,0] = minX+(l-L)
            CollocationPoints[i,1] = maxY
        elif 4<l<6: # East area
            CollocationPoints[i,0] = maxX
            CollocationPoints[i,1] = maxY-(l-(2*L))
        elif 6<l<8: # East area
            CollocationPoints[i,0] = maxX-(l-(3*L))
            CollocationPoints[i,1] = minY
        elif l == 0:
            CollocationPoints[i,0] = minX
            CollocationPoints[i,1] = minY
        elif l == 2:
            CollocationPoints[i,0] = minX
            CollocationPoints[i,1] = maxY
        elif l == 4:
            CollocationPoints[i,0] = maxX
            CollocationPoints[i,1] = maxY
        elif l == 6:
            CollocationPoints[i,0] = maxX
            CollocationPoints[i,1] = minY
        
        ChargePoints = np.dot(CollocationPoints,1+delta)
        f[i] = BoundaryCondition(CollocationPoints[i,0],CollocationPoints[i,1])
    
    for i in range(N):
        for j in range(N):
            G[i,j] = Green(CollocationPoints[i,0],CollocationPoints[i,1],ChargePoints[j,0],ChargePoints[j,1])
    
    q = solve(G,f)
    
    for x in range(NX):
        for y in range(NY):
            for i in range(N):
                psi[x,y] = psi[x,y] + q[i] * Green(X[x],Y[y],ChargePoints[i,0],ChargePoints[i,1])

    graph = Axes3D(plt.figure()).plot_surface(GX,GY,psi)
    plt.show()