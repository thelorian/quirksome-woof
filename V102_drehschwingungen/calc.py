import numpy as np
from scipy.optimize import curve_fit
import scipy.constants
import data
from uncertainties import ufloat

m_k = ufloat(512.2e-3, 0.20488)
R_k = ufloat(50.76e-3, 3.5532e-7) / 2
L = ufloat(0.60, 0.1)
T = ufloat(18.059, 0.006)
R = ufloat(0.188e-3, 0.001e-3)
G = 16 / 5 * np.pi * m_k * R_k ** 2 * L / (T ** 2 * R ** 4)


def p(T, m, a):
    return m * T + a
params, covar = curve_fit(p,
                          data.magn.curr,
                          data.magn.time,
                          )
error = np.sqrt(np.diag(covar))

m = ufloat(params[0], error[0])
b = ufloat(params[1], error[1])
print(m, b)
thet = 0.000134
T_m = ufloat(19.702, 0.012)  # - ufloat(18.059, 0.006)
k = 1 / (4 * np.pi ** 2 * thet)
m_mgn = 1 / k * m
b_mgn = 1 / k * b
b_anders = np.pi * G * R ** 4 / (2 * L)
print(m_mgn)
B_ = (1 / k) * ((1 / T_m ** 2) - b_mgn) / m_mgn
print(b_anders)
print(B_)
