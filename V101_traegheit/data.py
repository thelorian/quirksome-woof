import numpy as np
from scipy.constants import C2K


class D_stat:

    def __init__(self, angle, force):
        self.angle = angle / 360 * 2 * np.pi
        self.force = force

stat = D_stat(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V101_traegheit/Werte1.dat',
                             unpack=True))
print(stat.angle)
print(stat.force)


class D_dyn:

    def __init__(self, radius, time):
        self.radius = radius ** 2
        self.time = time ** 2

dyn = D_dyn(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V101_traegheit/Werte2.dat',
                           unpack=True))

print(dyn.radius)
print(dyn.time)
