#
#   Free Falling Body Model
#   Benedict Callander - 199194504
#

import numpy as np
import matplotlib.pyplot as plt

#define constants 
mp = float(input("Input a Mass in Kg:   "))
m= mp/1000 #kg
g = 9.81 #ms^-2
cd = 0.5
p = 1.225 # density of air
d= float(input("Input a Diameter in m:   "))
r = d/2000
A = np.pi*(r/2)**2 # CS area
k=cd*p*A*1/2 #drag coeff

def fallingdrag(t):
    return ((m*g*0.5)/k)*(1-(np.exp((-k*t)/m)))*t
def fallingnodrag(r):
    return (1/2)*g*(r**2)

timevals = np.arange(0.25, 0.65, 0.001)
drag_distances = fallingdrag(timevals)
no_drag = fallingnodrag(timevals)
#plot distances and times with drag
plt.figure(figsize =(15,12))
plt.plot(timevals, drag_distances, 'k-')
plt.tick_params(direction='in',      
                length=7,            
                bottom='on',         
                left='on',
                top='on',
                right='on',
                )
plt.xlabel("Time [s]")
plt.ylabel("distance fallen [m]")
plt.savefig("dfallingbody.png")
plt.show()
plt.close()

#plot distances and times without drag

plt.figure(figsize =(15,12))
plt.plot(timevals, no_drag, 'k-')
plt.tick_params(direction='in',      
                length=7,            
                bottom='on',         
                left='on',
                top='on',
                right='on',
                )
plt.xlabel("Time [s]")
plt.ylabel("distance fallen [m]")
plt.savefig("ndfallingbody.png")
plt.show()
plt.close()

#plot comparison

plt.figure(figsize =(10,10))
plt.plot(timevals, drag_distances, 'b-', label = "Drag Included")
plt.plot(timevals, no_drag, 'g-', label = "Drag excluded")
plt.tick_params(direction='in',      
                length=7,            
                bottom='on',         
                left='on',
                top='on',
                right='on',
                )
plt.legend(fancybox=True, loc = 'upper left')
plt.rcParams.update({'font.size':30})
plt.xlabel("Time [s]")
plt.ylabel("Distance fallen [m]")
plt.savefig("fallingexptimes.png")
plt.show()
plt.close()