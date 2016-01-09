import data
import matplotlib.pyplot as plot
import numpy as np
import calc


x_plot = np.linspace(0, 20)

plot.plot(data.temp.time, data.temp.temp1, 'rx', label='T1')
plot.plot(data.temp.time, data.temp.temp2, 'bx', label='T2')

plot.plot(x_plot, calc.f(x_plot, *calc.params1), 'r-', linewidth=1)
plot.plot(x_plot, calc.f(x_plot, *calc.params2), 'b-', linewidth=0.8)

plot.xlabel('$t$ in $\mathrm{min}$')
plot.ylabel('$T$ in $\mathrm{K}$')


plot.tight_layout(pad=1.08, h_pad=1.08, w_pad=1.08)
plot.grid()
plot.legend(loc='best')

plot.show()
