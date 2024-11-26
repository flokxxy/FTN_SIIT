import numpy as np
import math
import matplotlib.pyplot as plt



#f(x)=x^3−2x^2−5

def f(x):
    return x**2 - np.sin(2*x)
def f_pr1(x):
    return 2*x - 2*np.cos(2*x)


# Метод хорд (метод секущих)
def metod_sech(x0, x, eps):
    x1 = x
    x = x0
    while abs(x1 - x) >eps:
        x0 = x
        x = x1
        x1 = x - f_pr1(x)*(x-x0)/(f_pr1(x)-f_pr1(x0))
    return x1

print(metod_sech(x0= -1, x= 1,eps=0.01))

