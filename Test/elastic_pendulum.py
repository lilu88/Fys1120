import numpy as np
import matplotlib.pyplot as plt

def simulate(
    beta=0.9,                 # dimensionless parameter
    Theta=30,                 # initial angle in degrees
    epsilon=0,                # initial stretch of wire
    num_periods=6,            # simulate for num_periods
    time_steps_per_period=60, # time step resolution
    plot=True,                # make plots or not
    ):
    
    
    P=2*np.pi
    time_of_simulation = num_periods*P
    num_timeSteps = int((time_steps_per_period*num_periods))
    t = np.linspace(0,time_of_simulation, num_timeSteps)
    
    position = np.zeros((num_timeSteps,2))
    velocity = np.zeros_like(position)
    
    Th0 = Theta*np.pi/float(180)                 #initial angle in radians
    position[0,0] = (1+epsilon)*np.sin(Th0)      #x(0)
    position[0,1] = 1 - (1+epsilon)*np.cos(Th0)  #y(0)
    
    velocity[0,0] = 0   #v_x(0)=0
    velocity[0,1] = 0   #v_y(0)=0

    dt = P/float(time_steps_per_period)

    #Euler-Cromer:
    for i in xrange(num_timeSteps-1):
        velocity[i+1,:] = velocity[i,:] + dt*scaledAcceleration(
                                                position[i,0],
                                                position[i,1],
                                                beta)
        position[i+1,:] = position[i,:] + dt*velocity[i+1,:]

    x = position[:,0]
    y = position[:,1]
    theta = np.arctan(x/(1-y))*180./np.pi

    if plot:
        plt.plot(position[:,0],position[:,1])
        plt.axis('equal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Position of pendulum')
        plt.show()
        
        if Theta < 10:
            theta_pendulum = Th0*np.cos(2*np.pi/P*t)*180./np.pi
            plt.plot(t,theta_pendulum, label="Non-elastic")
            
        plt.plot(t,theta,label="Elastic")
        plt.xlabel('tid')
        plt.ylabel(r"$\theta$")
        plt.legend()
        plt.title('Angle of pendulum')
        plt.show()
    else:
        return x,y,theta,t
        
def scaledAcceleration(x,y,beta):
    L = np.sqrt(x**2 +(y-1)**2)
    acc_x = -beta/(1-beta)*(1.-beta/float(L))*x
    acc_y = -beta/(1-beta)*(1.-beta/float(L))*(y-1) - beta 
    return np.array([acc_x,acc_y])

#oppgave b
def test_trivial():
    x,y,theta,t = simulate(plot=False,Theta=0,epsilon=0)
    eps = 1e-6
    assert np.sum(np.abs(x)) + np.sum(np.abs(y)) < eps

#oppgave c
def test_pure():
    beta = 0.9
    freq = np.sqrt(beta/(1-beta))
    x,y,theta,t = simulate(plot=False,Theta=180, epsilon=0,time_steps_per_period=90000,num_periods=2,beta=0.9)
    A = (np.max(y) - np.min(y))/2. #Amplitude (ad hoc)
    orig = 2 - A                   #Nullpunkt til pendelen
    vib_sol = orig - A*np.sin(freq*t - np.pi/2.)
    eps = 1e-4
    assert np.sum((y-vib_sol)**2) < eps

#oppgave d    
def demo(beta,Theta):
    simulate(Theta=Theta,beta=beta,num_periods=3,time_steps_per_period=600)
    
    

if __name__ == "__main__":
    demo(0.9,20)
    
"""
Nose-test kjoreeksempel:

C:\Users\laila\Documents\INF5620>nosetests elastic_pendulum.py
..
----------------------------------------------------------------------
Ran 2 tests in 5.027s

OK
    
"""