import numpy as np
from uncertainties import ufloat


class Data:

    def __init__(self, curr, time):
        self.curr = curr * 1e-3
        self.time = 1 / ((time) ** 2)


m_k = ufloat(512.2e-3, 0.20488)
R_k = ufloat(50.76e-3, 3.5532e-7) / 2
L = ufloat(0.60, 0.1)
T = ufloat(18.059, 0.006)
R = ufloat(0.188e-3, 0.001e-3)
G = 16 / 5 * np.pi * m_k * R_k ** 2 * L / (T ** 2 * R ** 4)
print(G)


magn = Data(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V102_drehschwingungen/Werte2.dat',
                           unpack=True))
print(magn.curr)
print(magn.time)
