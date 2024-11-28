import numpy as np


# Функция f(x)
def f(x):
    d = len(x)
    term1 = np.sum(x ** 2)
    term2 = (1 / d * np.sum([i * x[i - 1] for i in range(1, d + 1)])) ** 2
    return term1 + term2


# Градиент функции f(x)
def gradf(x):
    d = 2
    grad = np.zeros_like(x)
    for i in range(d):
        grad[i] = 2 * x[i] + 2 * (1 / d) * (1 / d) * (np.sum([j * x[j - 1] for j in range(1, d + 1)])) * (i + 1)
    return grad


# Реализация ADAGRAD
def adagrad(x0, gamma, epsilon, max_iter=100):
    x = np.array(x0, dtype=float)
    grad_sum = np.zeros_like(x)
    for iteration in range(max_iter):
        grad = gradf(x)
        grad_sum += grad ** 2  # Накопление суммы квадратов градиентов
        adjusted_grad = grad / (np.sqrt(grad_sum) + epsilon)  # Нормализация градиента
        x = x - gamma * adjusted_grad  # Обновление координат

        # Условие остановки
        if np.linalg.norm(grad) < epsilon:
            print(f"Сходимость достигнута за {iteration + 1} итераций.")
            break
    return x, f(x)


# Параметры
x0 = [-1, -1]
gamma = 0.1
epsilon = 1e-4

# Запуск ADAGRAD
x_opt, f_opt = adagrad(x0, gamma, epsilon)
print("Оптимальная точка:", x_opt)
print("Минимальное значение функции:", f_opt)
