import matplotlib.pyplot as plt
import numpy as np

def euler(t,dt):
	n = int(t/dt)
	t = np.zeros(n, float)
	x = np.zeros(n, float)
	v = np.zeros(n, float)
	a = np.zeros(n, float)
	for i in range(n-1):
		a[i+1] = acceleration(t[i],x[i],v[i])
		v[i+1] = v[i] + a[i+1]*dt
		x[i+1] = x[i] + v[i]*dt
		t[i+1] = t[i] + dt			
	return t, x, v, a

#updated function for acceleration:
def acceleration(t,x,v):
	#setting constants and defining forces
	t_c = 0.67; f_c = 488; f_v = 25.8 
	A = 0.45; C_D = 1.2; m=80
	rho = 1.293; F = 400
	F_C = f_c*np.exp(-t/t_c)**2 
	F_V = -f_v*v
	D = 0.5*A*(1-0.25*np.exp(-t/t_c)**2)*rho*C_D*(v-1)**2
	Fnet = F + F_C + F_V - D
	return Fnet/m
	
		
t,x,v,a = euler(t=10,dt=0.001) 


plt.plot(t,x)
plt.ylabel("x(t) [m]")
plt.title("Sprinter plot")
plt.show()


