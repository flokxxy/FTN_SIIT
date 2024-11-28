import numpy as np

# Определение функции f(x)
def f(x):
    return np.exp(x) + np.cos(3 * x)

# Первая производная функции f(x)
def f_pr1(x):
    return np.exp(x) - 3 * np.sin(3 * x)

# Метод хорд (метод секущих)
def metod_sech(x0, x, eps):
    x1 = x
    x = x0
    while abs(x1 - x) > eps:
        x0 = x
        x = x1
        x1 = x - f_pr1(x) * (x - x0) / (f_pr1(x) - f_pr1(x0))
    return x1

# Запуск метода секущих
result = metod_sech(x0=1, x=3, eps=0.01)
print(f"Результат: {result}")
print(f(result))
