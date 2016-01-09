import data
import matplotlib.pyplot as plot
import numpy as np
from scipy.optimize import curve_fit
import calc

x = 1 / data.low_pres.temp
y = np.log(data.low_pres.pres)


def p(T, m, a):
    return m * T + a
params, covar = curve_fit(p,
                          x,
                          y,
                          )
error = np.sqrt(np.diag(covar))

x_plot = np.linspace(365, 410)

plot.plot(data.high_pres.temp, calc.all(data.high_pres.temp, *calc.params_high), 'r.')

plot.xlabel('$T$ in $\mathrm{K }$')
plot.ylabel('$p$ in $10^5 \mathrm{Pa}$')


plot.grid()
plot.legend(loc='best')
plot.tight_layout(pad=1, h_pad=1.08, w_pad=1.08)
plot.plot(x_plot, calc.all(x_plot, *calc.params_high), 'b-', linewidth=1)

plot.show()
