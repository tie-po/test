# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 12:00:23 2025

@author: cathal
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint #solve ode
#from mpl_toolkits.mplo3d import Axes3D #3d plotting

"""
constants, we dont need to understand the physical implications of these 
"""
frho = 28
fsigma = 10
fbeta =8/3

#to use odeint we need a function to return the first derivative
# of each of the coupled equations 
#eg. the right hand sides of the lorentz system of equations

def f1(state, t ,rho, sigma, beta):
    x,y,z = state #unpact state vector 
    return sigma * (y-x), x*(rho-z)-y, x*y-beta*z #dx/dt, dy/dt, dz/dt

#first two arguemnte are detirmined by what odient expects 
#remaining arguments are other values needed to perform the calculation

#we then call odient with a suitable initial condition and list of times to
#find the evaluated solution at these times

state0 = np.array([1,1,1])
timesteps=5000
t = np.linspace(0,50,timesteps)
states = odeint(f1,state0,t,args=(frho,fsigma,fbeta))

#output
print(states.shape)
(1000,3)


#plot of x vs t
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(states[:,0], states[:,1])
ax.set_xlabel('x(t)')
ax.set_ylabel('t')
plt.show

#3d plot
fig=plt.figure(figsize=(5,8))
ax = fig.add_subplot(projection='3d')
ax.plot(states[:,0], states[:,1], states[:,2], linewidth=1, rasterized=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#ax.axis('off')
plt.tight_layout()
plt.show
