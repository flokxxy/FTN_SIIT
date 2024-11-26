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


///////////////////////////////////


import numpy as np
import math
import matplotlib.pyplot as plt

#f(x)=e^x−3x^2

def f(x):
    return np.exp(x)-3*x**2
def f_pr1(x):
    return math.exp(x)-6*x

def metod_NR(x,eps):
    x1=x
    x=math.inf
    while abs(x1-x)>eps:
        x=x1
        x1 = x - f(x)/f_pr1(x)
    return x1

print(metod_NR(x=0.5,eps = 1e-6))
print(metod_NR(x=0.3,eps = 1e-6))



#проверка корней -->

#диапазон значений х
x = np.linspace(-1, 2, 500)
y = np.exp(x)-3*x**2


#построение графика
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Ось X
plt.plot(x, y, label=f(x))
plt.title("График функции")
plt.xlabel("x")
plt.ylabel("f(x)")
#plt.legend()
plt.grid()
plt.show()

///////////////////


import numpy as np
import math
import matplotlib.pyplot as plt

# f(x) = x^2 - 5

def f(x):
    return x**2 - 5

def f_pr1(x):
    return 2 * x

# Метод Ньютона-Рапсона
def metod_NR(x, eps):
    x1 = x
    x = math.inf
    while abs(x1 - x) > eps:
        x = x1
        x1 = x - f(x) / f_pr1(x)
    return x1

# Решение уравнения
print(metod_NR(x=0.5, eps=0.01))

# Построение графика
x = np.linspace(-1, 3, 500)  # Диапазон значений для графика
y = f(x)

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Ось X
plt.plot(x, y, label=f(x))
plt.title("График функции")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()
plt.show()


//////////////////

import numpy as np
import matplotlib.pyplot as plt
import math

#f(x)=sin(x)−0.5
def f(x):
    return np.sin(x)-0.5

def f_pr1(x):
    return np.cos(x)

def metod_NR(x,eps):
    x1=x
    x=math.inf
    while (abs(x1-x)>eps):
        x = x1
        x1 = x - f(x)/f_pr1(x)
    return x1

print(metod_NR(x = 0.5,eps = 0.01))

