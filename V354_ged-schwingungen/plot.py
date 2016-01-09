import matplotlib.pyplot as plot
import sys
import scipy.constants
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from cmath import sqrt


def f(nu,  a_0, a_1):
    return (1 / np.sqrt((1 - a_0 * nu ** 2) ** 2 + (nu ** 2) * a_1))

x, y, z, a = np.genfromtxt('/home/sirleonard/Documents/Praktikum_01/quirksome-woof/V354_ged-schwingungen/Daten2.dat', unpack=True)

print(x)
print(y)
print(z)
print(a)


params, covar = curve_fit(f,
                          x,
                          z,
                          )

print(params)
x_plot = np.linspace(0, 60)
x_plot1 = np.linspace(0, 60, 1000)
plot.errorbar(x, z + (a / 10), xerr=None, yerr=(a / 10), fmt='rx')

plot.xscale('log')
plot.xlabel(' v$ \;in\; \mathrm{ kHz }$')
plot.ylabel('$U_c/U_0$')
plot.xlim(0, 1e2)

plot.grid()
plot.legend(loc='best')
plot.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plot.plot(x_plot, f(x_plot, *params), 'b-', linewidth=1)
plot.plot(x_plot1, f(x_plot1, *params), 'b-', linewidth=1)


plot.show()
