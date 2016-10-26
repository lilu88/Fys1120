# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:03:52 2016

@author: Laila
"""
from pylab import*
from mpl_toolkits.mplot3d import Axes3D

dt = 1e-15             #str. på tidsteg
time = 30e-12          #total tid
n = time/dt;           #antall tidssteg

t = zeros(n)        
a = zeros((n,3))    
v = zeros((n,3))
r = zeros((n,3))

r[0] = array([.0,.0,.0]) 
v[0] = array([5000.0,.0, 200.0]) #10 km/s = 10 000 m/s

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

'''
#Analytical solution 
r_tx= 0.5*a0[0]*t**2
r_ty= 0.5*a0[1]*t**2
r_tz= 0.5*a0[2]*t**2

'''

'''
plot(t, r[:,0], 'b')
hold('on')
plot(t, r[:,1], 'g')
hold('on')
plot(t, r[:,2], 'r' )
legend(['x(t)', 'y(t)','z(t)'])
xlabel('Tid, t')
ylabel('Avstand, r')
title('Bevegelsen til et elektronet')
'''

'''
plot(t, v[:,0], 'b')
hold('on')
plot(t, v[:,1], 'g')
hold('on')
plot(t, v[:,2], 'r' )
legend(['$v_x(t)$', '$v_y(t)$','$v_z(t)$'])
xlabel('t[s]')
ylabel('v[m/s]')
title('Hastigheten til elektronet')
'''



fig = figure()
ax = fig.gca(projection = '3d')

ax.plot(r[:,0], r[:,1], r[:,2] )
xlabel('x')
ylabel('y')
title('Bevegelsen til et elektronet')
show()


'''
plot(t,r[:,0])
xlabel('t')
ylabel('x')
title('Bevegelsen til et elektronet')
show()
show()
 '''

