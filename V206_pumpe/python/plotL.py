import data
import matplotlib.pyplot as plot
import numpy as np
import calc


x_plot = np.linspace(0, 0.005)

plot.plot(data.verdampf.temp, data.verdampf.pres, 'rx', label='T1')


plot.plot(x_plot, calc.gerade(x_plot, *calc.paramsL), 'r-', linewidth=1)


plot.xlabel('$1/T$ in $\mathrm{1/K}$')
plot.ylabel('$log(p)$ in $ \mathrm{Pa}$')


plot.tight_layout(pad=1.08, h_pad=1.08, w_pad=1.08)
plot.grid()
plot.legend(loc='best')

plot.show()
