#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [500, 250, 200, 125, 62.5, 31.3, 15.6, 7.8]
ydata = [1.000000046, 0.823575113, 0.691950578, 0.634824117, 0.488234805, 0.354962446, 0.217080759,0.15088949]
plt.plot(xdata, ydata, '.')

def funcHyp(x, qi, exp, di):
    return qi*(1+exp*di*x)**(-1/exp)

trialX = np.linspace(xdata[0], xdata[-1], 1000)

# fit hyperbolic fxn
popt, pcov = curve_fit(funcHyp, xdata, ydata)
print 'popt'
yHYP = funcHyp(trialX, *popt)

plt.figure()
plt.plot(xdata, ydata, 'r+', label='Data', marker='o')
plt.plot(trialX, yHYP, 'r-',ls='--', label="Hyp Fit")
plt.legend()
plt.show()

#
#
#
#def func(x, a, b):
#     return (a * x) / (x + b)
#
#
#xdataf = np.linspace(0, 500, 25)
#y = func(xdataf, 1, 51)
#
#ydataf = y
#
#popt, pcov = curve_fit(func, xdata, ydata)
#
#plt.plot(xdataf, ydataf)
#plt.show()