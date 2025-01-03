import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def prvi():
    x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
    y = np.array([1, 2, 3, 2, 2, 2, 1.5, 2, 2, 2.5])

    pl = plt.plot(x, y)
    plt.show()


def two():
    x = np.arange(0, 2 * np.pi, 0.1)
    y = np.sin(x)

    pl = plt.plot(x, y)
    plt.show()


def three():
    x2 = np.arange(0, 2 * np.pi, 0.1)
    x1 = np.arange(0, 2 * np.pi, 0.1)
    x1, x2 = np.meshgrid(x1, x2)
    y = np.sin(x1) + np.cos(x2)

    figura = plt.figure()
    a = figura.add_subplot(111, projection='3d')  # 11 - koliko prozora imam, 1 - pristupimo
    # tip 1 stolbik, 1-polosa

    a.plot_surface(x1, x2, y)
    # pl = plt.plot(y)
    plt.show()


def four():
    x = np.arange(-10, 10)
    y = np.sin(x) + (1 / 25 * np.pow(x, 2))

    pl = plt.plot(x, y)
    plt.show()

def five():
    x1 = np.arange(-5, 5)
    x2 = np.arange(-5, 5)
    x1, x2 = np.meshgrid(x1, x2)

    a = 20
    b = 0.2
    n = np.arange(-5,5)
    y1 = -a*np.exp(1/2*np.sqrt(x1**2+x2**2))
    y2 = np.exp(1/2*np.sqrt(np.cos(np.pi*x1)+np.cos(np.pi*x2)))
    y=y1-y2+a+np.exp(1)

    figura = plt.figure()
    a = figura.add_subplot(111, projection='3d')

    a.plot_surface(x1, x2, y)
    plt.show()


if __name__ == '__main__':
    # prvi()
    # two()
    # three()
    # four()

    print(np.arange(0, 4.5, 0.5))  # lybie znachenija
