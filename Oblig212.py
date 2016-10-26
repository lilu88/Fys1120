# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:51:42 2016

@author: Laila
"""


from pylab import*


me = 9.11e-31           
e = -1.6e-19            
E = array([-1., -2., 5.])
F0 = E*e
a0 = F0/me              #=[*,*,*]

dt = 1e-9               #str. på tidsteg
time = 1e-6             #total tid
n = time/dt;            #antall tidssteg

def a_(r):
    return a0

t = zeros(n)        #null-array med lik str. som ant. tidssteg
a = zeros((n,3))    #samme men matrise-lignende, hvor aksel virker i 3D - 3 retn
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

''' 
#Analytical solution  
r_tx= 0.5*a0[0]*t**2
r_ty= 0.5*a0[1]*t**2
r_tz= 0.5*a0[2]*t**2
'''

plot(t, r[:,0], 'b', t, r[:,1], 'g',t, r[:,2], 'r', )
xlabel('t, time [s]')
ylabel('position[m]')
legend(['x(t)', 'y(t)', 'z(t)'])


show()
