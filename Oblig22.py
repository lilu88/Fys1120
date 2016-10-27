# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:03:52 2016

@author: Laila
"""
from pylab import*
from mpl_toolkits.mplot3d import Axes3D


dt = 1000e-15             #str. paa tidsteg
t_tot = 300e-9          #total tid
n = t_tot/dt;           #antall tidssteg

t = zeros(n)        
a = zeros((n,3))    
v = zeros((n,3))
r = zeros((n,3))

r[0] = array([.0,.0,.0]) 
v[0] = array([.0,.0,.0]) #10 km/s = 10 000 m/s

mp = 1.67e-27           
qe = 1.6e-19 
B = array([.0,.0,2])

E0 = 25000/(90.0e-6)

rd = 50e-3
w = qe*norm(B)/mp
d = 90.0e-6
    
def a_(r,v,time):
    F0 = qe*(cross(v,B))  #ref boka
    ex = array([1,0,0])
    if norm(r)<rd:
        if abs(r[0])<d/2.:
            E = E0*cos(w*time)*ex
        else:
            E = 0
        F = qe*E + F0
    else:
        
        F = 0
    return F/mp

#Numerical solution: Euler-Cromers
for i in range(0,int(n-1)):
    a[i] = a_(r[i,:],v[i,:],t[i])
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + (v[i+1])*dt
    t[i+1] = t[i] + dt

    print (float(i)/int(n-1))*100, "%            \r",


print " "

print "Protonet har tilslutt en fart: ", norm(v[-1,:])/(3e9)


plot(t, r[:,0])
hold('on')
plot(t, r[:,1])
hold('on')
plot(t, r[:,2])
legend(['x(t)', 'y(t)','z(t)'])
xlabel('t[s]')
ylabel('r[m]')
title('Bevegelsen til et protonet')
show()


plot(t, v[:,0], 'b')
hold('on')
plot(t, v[:,1], 'g')
hold('on')
plot(t, v[:,2], 'r' )
legend(['$v_x(t)$', '$v_y(t)$','$v_z(t)$'])
xlabel('t[s]')
ylabel('v[m/s]')
title('Hastigheten til protonet')
show()


'''
fig = figure()
ax = fig.gca(projection = '3d')

ax.plot(r[:,0], r[:,1], r[:,2] )
xlabel('x')
ylabel('y')
title('Bevegelsen til et elektronet')
show()
'''


'''
plot(t,r[:,0])
xlabel('t')
ylabel('x')
title('Bevegelsen til et elektronet')
show()
show()
 '''

