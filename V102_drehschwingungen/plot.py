import data
import matplotlib.pyplot as plot
import sys
import numpy as np
from scipy.optimize import curve_fit
import scipy.constants
import data
from uncertainties import ufloat

import numpy as np
from scipy.optimize import curve_fit
import scipy.constants
import data
from uncertainties import ufloat


def f(T, m, a):
    return m * T + a
params, covar = curve_fit(f,
                          data.magn.curr,
                          data.magn.time,
                          )
error = np.sqrt(np.diag(covar))

m = ufloat(params[0], error[0])
b = ufloat(params[1], error[1])
print(m, b)
thet = 1.34e-4
T_m = ufloat(19.702, 0.012)
k = 1 / (4 * np.pi * thet)
m_mgn = k * m
b_mgn = k * b
B_ = 1 / (T_m ** 2 * m) - (b / m)
print(B_)


x = data.magn.curr
y = data.magn.time
x_plot = np.linspace(0, 0.005)
plot.plot(x, y, 'rx')


plot.xlabel('$B \;in\; \mathrm{ mT }$')
plot.ylabel('$1/T^2\; in\; \mathrm{ 1/s^2 }$')
plot.xlim(0, 0.005)
plot.ylim(0, 0.0055)
plot.grid()
plot.legend(loc='best')
plot.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plot.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit', linewidth=1)


plot.show()
