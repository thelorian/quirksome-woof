import numpy as np
from scipy.optimize import curve_fit
from scipy.constants import R
import scipy
import data
from uncertainties import ufloat


def f(T, L, p0):
    return p0 * np.exp(-L / (T * R))

params, covar = curve_fit(f,
                          data.low_pres.temp,
                          data.low_pres.pres,
                          )
error = np.sqrt(np.diag(covar))

L = ufloat(params[0], error[0])
print(L)

a = ufloat(20, 1)
b = ufloat(20, 1)
print(a ** 2, a + a, a - b)
