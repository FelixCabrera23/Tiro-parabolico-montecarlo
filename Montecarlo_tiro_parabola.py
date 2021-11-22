#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:00:44 2021

@author: walberto

Este programa calcula una trayectoria de tiro parabolico por medio del 
metodo de montecarlo, conservando la energia.

"""


import matplotlib.pyplot as plt
import numpy as np
import random

v0 = 8 # Velocidad inicial en m/s
ang = np.radians(45) # Angulo de salida
dt = 0.001 # Espacio de tiempo entre paso montecarlo en segundos
n = 300 # pasos montecarlo

Err = 0.00001
ang_err = np.pi/10

# posiciones
x = [0]
y = [0]
vt = [v0]

def Energia (v,y):
    
    """
    Esta función calcula la energia de la particula en todo momento
    """
    
    E = 0.5*v**2 + 9.81*y
    
    return E

def Vel_n (x,y,xn,yn):
    """
    Esta función toma las posisiones originales y finales y calcula la velocidad

    """
    Vx = v0*np.cos(ang)
    t = (xn-x)/Vx
    
    Vy = (yn-y)/t
    
    V = np.sqrt(Vx**2+Vy**2)
    
    return V


def Mov (x,y,ang):
    """ 
    Esta función mueve aliatoriamente la particula
    """
    
    angn = random.choice([-1,1])*random.random()*ang_err + ang 
    r = random.random()*0.05
    
    xn = x + r*np.cos(angn)
    yn = y + r*np.sin(angn)
    
    # xn = x + v0*np.cos(ang)*dt
    # yn = y +  random.choice([-1,1])*random.random()*0.05
    # angn = ang
    
    return xn, yn, angn


Eo = Energia(v0,y[0])
i = 0
ang_0 = ang

print("Procesando:")
print("..................................................")

while i < n:
    
    Xn, Yn, ang_n = Mov(x[i], y[i],ang_0)
    
    Vn = Vel_n(x[i],y[i],Xn,Yn)
    
    En = Energia(Vn,Yn)
    
    if (En < Eo+Err) and (En > Eo - Err):
        vt.append(Vn)
        x.append(Xn)
        y.append(Yn)
        
        ang_0 = ang_n
        
        i += 1
        
        if Yn < 0: break
        print(".",end=(""))
        
        
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.plot(x,y)
    
    
   
    
    












