import matplotlib.pyplot as plot
import sys
import scipy.constants
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from cmath import sqrt


def f(nu, a_0, a_1, a_2, a_3):
    return (1.05 * (np.arctan(0.22 * (nu - 34)) + 1.45))


x, y, z, a = np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V354_ged-schwingungen/daten3.dat', unpack=True)

params, covar = curve_fit(f,
                          x,
                          z,

                          )
x_plot = np.linspace(0, 60, 2000)
print(params)

plot.plot(x, z, 'rx')

plot.semilogx()
plot.xlabel('$B \;in\; \mathrm{ mT }$')
plot.ylabel('$1/T^2\; in\; \mathrm{ 1/s^2 }$')
plot.xlim(0, 1e2)

plot.grid()
plot.legend(loc='best')
plot.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plot.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit', linewidth=1)

plot.show()
