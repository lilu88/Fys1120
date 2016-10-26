# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:39:11 2016

@author: Laila
"""

from pylab import*

me = 9.11e-31           #mass of electron in kg
e = -1.6e-19            #charge of electron in C
E = array([-5, .0, .0]) #electrical field N/C 
F0 = E*e
a0 = F0/me

def a_(r):
    return a0

dt = 100e-9             #dt=1ns = nanosek
time = 1e-6             #time = mikrosek
n = time/dt;            #n = number of steps

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
 
#Analytical solution  
r_tx= 0.5*a0[0]*t**2
r_ty= 0.5*a0[1]*t**2
r_tz= 0.5*a0[2]*t**2

plot(t, r, 'b')
hold('on')
plot( t, r_tx,'r--')
xlabel('t, time [s]')
ylabel('r, position[m] in x-direction')
#legend(['numerical solution','analytical solution'])
show()


    
    
