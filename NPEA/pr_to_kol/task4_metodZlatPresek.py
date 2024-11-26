import math
import numpy as np
import matplotlib.pyplot as plt

# f(x)=(x−2)^2+sin(x)

def f(x):
    return (x-2)**2+np.sin(x)

def metod_zlatPresek(a,b,eps):
    c = 0.381
    n = 0
    x1 = a+c*(b-a)
    x2 = a+b - x1
    while b-a>eps:
        n+=1
        if(f(x1)<f(x2)):
            b = x2
        else:
            a = x1
        x1 = a+c*(b-a)
        x2 = a+b -x1
    if(f(x1)<f(x2)):
        x_opt = x1
    else:
        x_opt = x2
    f_opt = f(x_opt)
    return x_opt,f_opt,n

print(metod_zlatPresek(a = 0, b = 4, eps = 0.001))
