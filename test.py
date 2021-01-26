import numpy as np
import matplotlib.pyplot as plt
import math


lx = 10
ly = 10
nx = 30
ny = 10
m = .01
w = 1
h = 1

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *=i
    return res
def H(x,n):
    
    k = 1 if n%2 == 0 else -1
    return k*np.exp(x*x)
    #todo implement the rest of the hermite polynomials
def wave(x,n):
    return (1/(math.sqrt(math.pow(2,n)*fact(n)))*math.pow((m*w)/(math.pi*h),.25))*pow(math.e,-1*m*w*(x*x)/2*h)*H(x*math.sqrt(m*w/h),n)



px = np.arange(0,lx,0.004)
py = np.arange(0,ly,0.004)
xs,ys = np.meshgrid(px,py)
z = np.multiply(np.sin(xs*nx*math.pi/lx),np.sin(ys*ny*math.pi/ly))
#z = [wave(x,nx) for x in xs]
z = np.multiply(z,z)
plt.imshow(z)
plt.show()
