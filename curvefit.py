#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [500, 250, 200, 125, 62.5, 31.3, 15.6, 7.8]
ydata = [1.000000046, 0.823575113, 0.691950578, 0.634824117, 0.488234805, 0.354962446, 0.217080759,0.15088949]
error = [1.76721E-07, 0.153325427, 0.011565495, 0.098371588, 0.097873602,
         0.074227226, 0.10134406, 0.103427488]

def funcHyp(x, a):
    return 1/((a/x)+1)

trialX = np.linspace(xdata[0], xdata[-1], 1000)

# fit hyperbolic fxn
popt, pcov = curve_fit(funcHyp, xdata, ydata)
print 'popt'
yHYP = funcHyp(trialX, *popt)

plt.figure()
plt.plot(xdata, ydata, 'r+', label='Data', marker='o')
plt.plot(trialX, yHYP, 'r-',ls='--', label="Hyp Fit")
plt.errorbar(xdata, ydata, yerr=error, linestyle = "none")
plt.legend()
plt.show()
