from array import array

import numpy as np
import math
import matplotlib.pyplot as ptl

#f(x,y)=4x^2+y^2+2xy−6x−4y+9
#df/dx = 8x+2y-6
#df/dy = 2y+2x-4

def gradf(x):
    x = np.array(x).reshape(np.size(x))
    return np.array([[8*x[0]+2*x[1]-6],
                     [2*x[1]+2*x[0]-4]])

def ADAM(x0,eps1,eps2,n,gamma,om1,om2):
    x = np.array(x0).reshape(len(x0),1)
    nak_grad = np.zeros_like(x,dtype=np.float64)
    v=1
    m=1

    #eps = 1e-8

    for i in range(n):
        grad = gradf(x)
        m=om1*m+(1-om1)*grad
        v=om2*v+(1-om2)* grad**2
        hat_v = np.abs(v/(1-om2))
        hat_m = m/(1-om1)
        x = x - gamma*hat_m/np.sqrt(hat_v+eps2)

        if np.linalg.norm(grad)<eps1:
            break
    return x

print("min",ADAM(x0 = [-2,2],eps1=0.01,eps2=1e-4,n=100,gamma=0.1,om1=0.1,om2=0.9))
