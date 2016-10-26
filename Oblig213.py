# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:04:23 2016

@author: Laila
"""


from pylab import*
from mpl_toolkits.mplot3d import Axes3D


me = 9.11e-31           #mass of electron in kg
e = -1.6e-19            #charge of electron in C
E = array([-1., -2., 5.]) #electrical field N/C 
F0 = E*e
a0 = F0/me

dt = 1e-9               #dt=1ns = nanosek
time = 1e-6             #time = mikrosek
n = time/dt;            #n = number of steps

def a_(r):
    return a0

#HusK ref: Elementary Mechanics Using Python side 163-164

t = zeros(n)
a = zeros((n,3))
v = zeros((n,3))
r = zeros((n,3))

r[0] = array([.0,.0,.0]) #init_position x0=0,y0=0,z0=0
v[0] = array([.0,.0,.0]) #init_velocity

#Sumerical solution: Euler-Cromers
for i in range(0,int(n-1)):
    a[i] = a_(r)
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + (v[i+1])*dt
    t[i+1] = t[i] + dt

fig = figure()
ax = fig.gca(projection = '3d')

ax.plot(r[:,0], r[:,1], r[:,2], '.' )
xlabel('x')
ylabel('y')

show()