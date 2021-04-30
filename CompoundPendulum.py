#
# Compound Pendulum Simulation
# Benedict Callander(Primary) & James Brooks (Secondary)
#
import numpy as np
import matplotlib.pyplot as plt
import math

m1=1.4
d1=0.5
m2=1.0
d2=0.25
g=9.812

inertia=m1*(d1**2)+m2*(d2**2)

def torque(theta, v):
    dragtorque1=d1*coeff*(v*d1)**2
    dragtorque2=d2*coeff*(v*d2)**2
    #print(str(dragtorque1) + " + " + str(dragtorque2))
    if (v<0):
        T=g*math.sin(theta)*(m2*d2-m1*d1)+dragtorque1+dragtorque2
    else:
        T=g*math.sin(theta)*(m2*d2-m1*d1)-dragtorque1-dragtorque2

    return T


times = np.linspace(0,10,10000)
tstep = (max(times)-min(times))/len(times)

theta=math.radians(170)
v=0    
vs=[]
thetas=[]
timer=0
period=[]
x_values=[]
x=0
every_other=0

rho=1.225 #density of air
Cd = 0.45 #coefficient of drag of sphere
coeff=0.5*Cd*rho*(0.03*2)

for i in times:
    a=(torque(theta, v)/inertia) 
    vprev=v
    v=v+a*tstep
    theta=theta+v*tstep
    vs.append(v)
    thetas.append(theta)
    
    if ((vprev<0 and v>0) or (vprev>0 and v<0)):
        if (every_other==1):
            period.append(timer)
            x_values.append(x)
            #print(timer)
            #print(x)
            timer=0
            x=x+1
            every_other=0
        else:
            every_other=1
        
    
    timer=timer+tstep
    vprev=v
    #print(every_other)
  
fig, ax1 = plt.subplots()    
plt.figure(figsize=(10,10))
ax1.plot(times,vs,label="V", color='red') 
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Speed [rad/s]", color='red')
ax2 = ax1.twinx()
ax2.plot(times,thetas,label="Theta", color='blue')
ax2.set_ylabel("Theta[rad]", color='blue')
fig.set_figheight(10)
fig.set_figwidth(10)
plt.savefig("trace.png", dpi=500)
plt.grid()
plt.show()

plt.plot(x_values,period) 
plt.xlabel("Oscillation number")
plt.ylabel("Period[s]")
#plt.ylim([1.92,1.93])
plt.grid()
plt.show()


plt.figure(figsize=(10,10))
plt.plot(thetas, vs, 'r-')
plt.tick_params(direction='in',      
                length=7,            
                bottom='on',         
                left='on',
                top='on',
                right='on',
                
               )
plt.rcParams.update({'font.size':30})
plt.xlabel("$\Theta$")
plt.ylabel("${\Theta}.$")
plt.savefig("Phasecomp.png", dpi=500)
plt.show()
plt.close()