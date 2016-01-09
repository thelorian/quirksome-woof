import numpy as np
from scipy.constants import C2K
from uncertainties import ufloat


class Data_temp:

    def __init__(self, time, temp1, temp2, pres1, pres2, power):
        self.time = time
        self.temp1 = C2K(temp1)
        self.temp2 = C2K(temp2)
        self.pres1 = pres1 * 10 ** 5
        self.pres2 = pres2 * 10 ** 5
        self.power = power

temp = Data_temp(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V206_pumpe/Werte/Werte1.dat',
                                unpack=True))
print(temp.temp1)
print(temp.temp2)
print(temp.pres1)
print(temp.pres2)
print(temp.power)


class Data_L:

    def __init__(self, pres, temp):
        self.pres = np.log(pres * 1e5)
        self.temp = 1 / C2K(temp)

verdampf = Data_L(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V206_pumpe/Werte/Werte2.dat', unpack=True))

print('L', verdampf.pres)
print('L', verdampf.temp)
