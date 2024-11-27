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

def ADAGRAD(x0,eps,n,gamma):
    x = np.array(x0).reshape(len(x0),1)
    nak_grad = np.zeros_like(x,dtype=np.float64)

    eps = 1e-8

    for i in range(n):
        grad = gradf(x)
        nak_grad +=grad**2
        adjusted_grad = grad*gamma/(np.sqrt(nak_grad)+eps)
        x = x - adjusted_grad
        if np.linalg.norm(grad)<eps:
            break
    return x

print("min",ADAGRAD(x0 = [-2,2],eps=1e-4,n=100,gamma=0.1))
