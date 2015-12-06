import data
import matplotlib.pyplot as plot
import sys

x = 1 / data.low_pres.temp
y = data.low_pres.pres

plot.plot(x, y, 'r.', label='Dampfdruckkurve')

plot.yscale('log')
plot.xlabel('$T\;/\mathrm{{}^\circ C}$')
plot.ylabel('Dampfdruck $p/\mathrm{Pa}$')
# plot.ylim(5e3,2e5)

plot.grid()
plot.legend(loc='best')
plot.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

if len(sys.argv) > 1 and sys.argv[1] == "save":
    plot.savefig('plots/low_press.pdf')
else:
    plot.show()
