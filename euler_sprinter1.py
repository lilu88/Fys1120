import matplotlib.pyplot as plt
import numpy as np

def euler(t,dt):
	n = int(t/dt)
	t = np.zeros(n, float)
	x = np.zeros(n, float)
	v = np.zeros(n, float)
	x[0] = 0
	v[0] = 0
	for i in range(n-1):
		v[i+1] = v[i] + a(t[i],x[i],v[i])*dt
		x[i+1] = x[i] + v[i+1]*dt
		t[i+1] = t[i] + dt			
	return t, x, v

#We have a function for the acceleration from the previous exercise:
def a(t,x,v):
	return (400 - 0.34911*v**2)/(80)
		
t,x,v = euler(t=30,dt=0.01) 

plt.figure(1)
plt.subplot(211)
plt.plot(t,x)
plt.ylabel("x(t) [m]")
plt.title("Sprinter plot")

plt.subplot(212)
plt.plot(t,v)
plt.xlabel("t")
plt.ylabel("v(t) [m/s]")
plt.show()
