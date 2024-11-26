import math
import numpy as np
import matplotlib.pyplot as plt

# f(x)=(x−2)^2+sin(x)

def f(x):
    return (x-2)**2+np.sin(x)

def fib(n):
    if(n<3):
        return 1
    else:
        return fib(n-1)+fib(n-2)

def metod_Fib(a,b,eps):
    n=1
    while (abs(a-b)/eps)>fib(n):
        n+=1
        x1 = a+fib(n-2)/fib(n)*(b-a)
        x2 = a+b-x1

    for i in range(n):
        if(f(x1)<f(x2)):
            b=x2
            x1 = a+fib(n-2)/fib(n)*(b-a)
            x2 = a+b - x1
        else:
            if(f(x1)<f(x2)):
                x_opt = x1
            else:
                x_opt = x2
    f_opt = f(x_opt)
    return x_opt,f_opt,n

x_opt,f_opt,n = metod_Fib(0,4,0.001)
print(x_opt, f_opt,n)
