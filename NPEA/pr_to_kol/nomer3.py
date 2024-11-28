import numpy as np

# Функция
def f(x):
    return np.exp(x) + np.cos(3 * x)

# Числа Фибоначчи
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Нахождение числа итераций
def calculate_iterations(a, b, eps):
    n = 1
    while fib(n) <= (b - a) / eps:
        n += 1
    return n

# Метод Фибоначчи
def metod_Fib(a, b, eps):
    n = calculate_iterations(a, b, eps)

    # Инициализация точек
    x1 = a + fib(n - 2) / fib(n) * (b - a)
    x2 = a + b - x1

    for i in range(n - 1):
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + fib(n - 2) / fib(n) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1

        # Условие остановки
        if abs(b - a) < eps:
            break

    # Выбор оптимальной точки
    if f(x1) < f(x2):
        x_opt = x1
    else:
        x_opt = x2

    f_opt = f(x_opt)
    return x_opt, f_opt, n

# Заданные параметры
a, b = 0, 10
eps = 0.01

# Вычисление оптимума
x_opt, f_opt, n = metod_Fib(a, b, eps)
print(f"Оптимальная точка: {x_opt:.4f}")
print(f"Минимальное значение функции: {f_opt:.4f}")
print(f"Необходимое число итераций: {n}")

#и плюс 1 к результату итераций
