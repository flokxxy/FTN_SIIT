import numpy as np
import math
import matplotlib.pyplot as plt
from fontTools.misc.cython import returns


#f(x,y)=4x^2+y^2+2xy−6x−4y+9
#df/dx = 8x+2y-6
#df/dy = 2y+2x-4

def gradf(x):
    x = np.array(x).reshape(np.size(x))
    return np.array([[8*x[0]+2*x[1]-6],
                     [2*x[1]+2*x[0]-4]])
#def f(x):

def metod_NajbPad(x0, eps, n, gamma):
    x = np.array(x0).reshape(len(x0), 1)  # Начальная точка
    for i in range(n):
        grad = gradf(x)
        x = x - gamma * grad  # Обновление координат
        if np.linalg.norm(grad)<eps:  # Условие остановки
            break
    return x


 #print(metod_NajbPad(x0 = [-2,2],eps = 1e-4,n = 100,gamma = 0.1))
print(metod_NajbPad(x0=[-2, 2], eps=1e-4, n=100, gamma=0.1))

