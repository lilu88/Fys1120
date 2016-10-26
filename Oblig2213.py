# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:03:52 2016

@author: Laila
"""
from pylab import*
from mpl_toolkits.mplot3d import Axes3D

dt = 1e-15             #str. på tidsteg
time = 30e-12           #total tid
n = time/dt;           #antall tidssteg

t = zeros(n)        
a = zeros((n,3))    
v = zeros((n,3))
r = zeros((n,3))

r[0] = array([.0,.0,.0]) 
v[0] = array([10000.0,.0,.0]) #10 km/s = 10 000 m/s

me = 9.11e-31           
pe = -1.6e-19 
B = array([.0,.0,2.0])

def a_(r,v):
    F0 = pe*(cross(v,B))  #ref boka
    a0 = F0/me              #N2L
    return a0

#Numerical solution: Euler-Cromers
for i in range(0,int(n-1)):
    a[i] = a_(r[i,:],v[i,:])
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + (v[i+1])*dt
    t[i+1] = t[i] + dt


#Analytical solution 
r_tx= 0.5*a0[0]*t**2
r_ty= 0.5*a0[1]*t**2
r_tz= 0.5*a0[2]*t**2


fig = figure()
ax = fig.gca(projection = '3d')

ax.plot(r[:,0], r[:,1], r[:,2] )
xlabel('x')
ylabel('y')
show()

