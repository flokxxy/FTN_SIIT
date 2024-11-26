import numpy as np
import matplotlib.pyplot as plt
import math

#f(x)=x^3−x−2=0

def f(x):
    return x**3-x-2

def pr1(x):
    return 3*x**2-1  #3x^2-1

def pr2(x):
    return 6*x

def Metod_NR(x,epsilon):
    x1=x
    x=math.inf
    while (abs(x1-x)>epsilon):
        x=x1
        x1 = x - f(x)/pr1(x)
    return x1

/////////////////////////////////////

import numpy as np
import matplotlib.pyplot as plt
import math

#f(x)=cos(x)−x

def f(x):
    return math.cos(x)-x
def f_pr1(x):
    return -math.sin(x)-1

def metod_NR(x,epsilon):
    x1 = x
    x = math.inf
    while ( abs(x1-x)>epsilon):
        x=x1
        x1=x-f(x)/f_pr1(x)
    return x1


print(metod_NR(x=-1,epsilon=0.01))

