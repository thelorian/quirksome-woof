import data
import calc
import matplotlib.pyplot as plot
import sys
import numpy as np

x = data.dyn.radius
y = data.dyn.time
x_plot = np.linspace(0, 80000, 500)
plot.plot(x, y, 'rx', label='Messwerte')

plot.xlabel('Radius $a^2 \:/\:\mathrm{mm^2}$')
plot.ylabel('Periodendauer $T^2\:/\:\mathrm{s^2}$')
# plot.ylim(5e3,2e5)

plot.grid()
plot.legend(loc='best')
plot.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plot.plot(x_plot, calc.f(x_plot, *calc.params),  label='linearer Fit', linewidth=1)
if len(sys.argv) > 1 and sys.argv[1] == "save":
    plot.savefig('plots/low_press.pdf')
else:
    plot.show()
