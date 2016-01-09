import numpy as np
from scipy.optimize import curve_fit
import scipy.constants
import data
from uncertainties import ufloat

# Niedrigdruck


def f(T, L, p0):
    return p0 * np.exp(-L / (T * scipy.constants.R))

params, covar = curve_fit(f,
                          data.low_pres.temp,
                          data.low_pres.pres,
                          )
error = np.sqrt(np.diag(covar))

L = ufloat(params[0], error[0])
print(L)


def f_lin(T, L, p0):
    return -L * T / scipy.constants.R + p0

paramsnew, covarnew = curve_fit(f_lin,
                                data.low_presnew.temp,
                                data.low_presnew.pres,
                                )

errornew = np.sqrt(np.diag(covarnew))
Lnew = ufloat(paramsnew[0], errornew[0])

print(Lnew)
L_a = 373 * scipy.constants.R
print(L_a)
L_i = L - L_a
print(L_i)

L_imol = L_i / scipy.constants.N_A
print(L_imol)
L_imol = L_imol / 1.602176565e-19
print(L_imol)

# Hochdruck


def p(T, p0, p1, p2, p3):
    return p0 + p1 * T + p2 * T ** 2 + p3 * T ** 3


def all(T, p0, p1, p2, p3):
    return(scipy.constants.R * T / 2 - np.sqrt((scipy.constants.R * T / 2) ** 2 - 0.9 * p(T, p0, p1, p2, p3))) * (3 * p3 * T ** 3 + 2 * p2 * T ** 2 + p1 * T) / p(T, p0, p1, p2, p3)

params_high, covar_high = curve_fit(p,
                                    data.high_pres.temp,
                                    data.high_pres.pres,
                                    )
error_high = np.sqrt(np.diag(covar_high))
p0 = ufloat(params_high[0], error_high[0])
p1 = ufloat(params_high[1], error_high[1])
p2 = ufloat(params_high[2], error_high[2])
p3 = ufloat(params_high[3], error_high[3])

print(p0)
print(p1)
print(p2)
print(p3)
