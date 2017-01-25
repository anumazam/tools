#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [0.5, 1, 2, 5, 10, 20, 50, 100, 200]
ydata = [203955.00, 237793.33, 247993.33, 243903.33, 260283.33, 263960.00, 264170.00, 268793.33, 262210.00]
satpt = ydata[-1]
ydata_norm = [x / satpt for x in ydata]
#error = [0.029748604,0.044241493,0.053897674,0.068093355,0.046003875,0]

#xdata = [0.001, 1, 10, 50, 200, 1000]
#ydata = [16175.00, 17520.00, 18150.67, 18259.33, 18535.33, 19254.00]
#error = [1340.16, 1172.84, 774.54, 1221.61, 408.08, 494.14]

def funcHyp(x, a):
    return x/(a+x)

trialX = np.linspace(.5, 1000, 1000)

# fit hyperbolic fxn
popt, pcov = curve_fit(funcHyp, xdata, ydata_norm)
yHYP = funcHyp(trialX, *popt)
print popt

# plot
plt.figure()

plt.plot(xdata, ydata_norm, 'g+', label='data', marker='s', markersize=8)
plt.plot(trialX, yHYP, 'k-',ls='--', label='fit')
#plt.errorbar(xdata, ydata, yerr=error, linestyle = "none", color = "black")
plt.xscale('log', nonposy='clip')
#plt.ylim(0.6, 1.05)

plt.legend(loc=4)
plt.show()
