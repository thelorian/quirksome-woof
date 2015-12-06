import numpy as np
from scipy.constants import C2K


class Data:

    def __init__(self, temp, pres):
        self.temp = C2K(temp)
        self.pres = pres * 1e2

low_pres = Data(*np.genfromtxt('./Werte1.dat', unpack=True))
