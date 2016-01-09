import numpy as np
from scipy.optimize import curve_fit
import scipy.constants
import data
from uncertainties import ufloat


def f(t, a_0, a_1, a_2, a_3):
    return a_0 + a_1 * t + a_2 * t ** 2 + a_3 * t ** 3


def df(t, a_0, a_1, a_2, a_3):
    return a_1 + 2 * a_2 * t + 3 * a_3 * t ** 2

params1, covar1 = curve_fit(f,
                            data.temp.time,
                            data.temp.temp1,
                            )
error1 = np.sqrt(np.diag(covar1))

params2, covar2 = curve_fit(f,
                            data.temp.time,
                            data.temp.temp2,
                            )
error2 = np.sqrt(np.diag(covar2))

print(params1)
print(params2)

print(df(4, *params1), df(6, *params1), df(10, *params1), df(13, *params1))

print(df(4, *params2), df(6, *params2), df(10, *params2), df(13, *params2))

N = sum(data.temp.power) / 20
print(N)


def nu(m_1, m_2, dT, P):
    return (m1 + m2) * dT / P

m1 = 12600
m2 = 660

print(nu(m1, m2, df(4, *params1), N), nu(m1, m2, df(6, *params1), N), nu(m1, m2, df(10, *params1), N), nu(m1, m2, df(13, *params1), N))


def gerade(T, m, b):
    return m * T + b

paramsL, covarL = curve_fit(gerade,
                            data.verdampf.temp,
                            data.verdampf.pres,
                            )
errorL = np.sqrt(np.diag(covarL))
print(paramsL)

L = scipy.constants.R * paramsL[0]

print('L', L)

print(nu(m1, m2, df(4, *params2),  L), nu(m1, m2, df(6, *params2),  L), nu(m1, m2, df(10, *params2),  L), nu(m1, m2, df(13, *params2),  L))


def N_mech(p_a, p_b, T2, t):
    return (p_b * (p_a / p_b) ** 1.14 - p_a) / (1.14 - 1) * T2 / (273.15 * 5.514e-3) * nu(m1, m2, df(t, *params2), L)

print(N_mech(data.temp.pres1, data.temp.pres2, data.temp.temp2, data.temp.time))


print(data.temp.temp1[4] / (data.temp.temp1[4] - data.temp.temp2[4]), data.temp.temp1[6] / (data.temp.temp1[6] - data.temp.temp2[6]), data.temp.temp1[10] / (data.temp.temp1[10] - data.temp.temp2[10]), data.temp.temp1[13] / (data.temp.temp1[13] - data.temp.temp2[13]))
