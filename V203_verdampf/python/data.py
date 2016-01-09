import numpy as np
from scipy.constants import C2K


class Data:

    def __init__(self, temp, pres):
        self.temp = C2K(temp)
        self.pres = pres * 10 ** 2

low_pres = Data(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V203_verdampf/Werte1.dat',
                               unpack=True))
low_presnew = Data(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V203_verdampf/Werte1.dat',
                                  unpack=True))
low_presnew.temp = 1 / low_presnew.temp
low_presnew.pres = np.log(low_presnew.pres)

print(low_pres.temp)
print(low_pres.pres)

print(low_presnew.temp)
print(low_presnew.pres)

high_pres = Data(*np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V203_verdampf/Werte2.dat',
                                unpack=True))

high_pres.pres -= high_pres.pres[0] - 100000
print(high_pres.temp)
print(high_pres.pres)
