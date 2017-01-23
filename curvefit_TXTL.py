#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [0.0001, 1, 10, 50, 200, 1000]
ydata = [0.841473664,0.909526975,0.94333909,0.949832164,0.963458835,1]
error = [0.029748604,0.044241493,0.053897674,0.068093355,0.046003875,0]

def funcHyp(x, a, b):
    return 1/((a/x)+1)

trialX = np.linspace(0.0001, 1000., 1000)

# fit hyperbolic fxn
popt, pcov = curve_fit(funcHyp, xdata, ydata)
yHYP = funcHyp(trialX, *popt)
print popt

# plot
plt.figure()

plt.plot(xdata, ydata, 'g+', label='data', marker='s', markersize=8)
plt.plot(trialX, yHYP, 'g-',ls='--', label='fit')
plt.errorbar(xdata, ydata, yerr=error, linestyle = "none", color = "black")
plt.xscale('linear', nonposy='clip')

plt.legend(loc=4)
plt.show()
