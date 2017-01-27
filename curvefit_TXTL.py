#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [0.1, 0.5, 1, 2, 5, 10, 20]
ydata1 = [201196.00, 203955.00, 237793.33, 247993.33, 243903.33, 260283.33, 263960.00]
ydata2 = [28850.00, 33551.67, 35446.33, 38762.33, 39945.33, 42302.00, 43795.00]
satpt = ydata1[-1]
ydata1_norm = [x / satpt for x in ydata1]
satpt = ydata2[-1]
ydata2_norm = [y / satpt for y in ydata2]

compiled_ydata = np.array([ydata1_norm, ydata2_norm])

ydata_avg = np.mean(compiled_ydata, axis = 0)
ydata_std = np.std(compiled_ydata, axis = 0)

#error = [0.029748604,0.044241493,0.053897674,0.068093355,0.046003875,0]

#xdata = [0.001, 1, 10, 50, 200, 1000]
#ydata = [16175.00, 17520.00, 18150.67, 18259.33, 18535.33, 19254.00]
#error = [1340.16, 1172.84, 774.54, 1221.61, 408.08, 494.14]

#def funcHyp(x, a):
#    return 1*x/(a+x)

def funcHyp(x, b, a, c):
    return a + ( (b-a) / (1 + (c/x)) )

trialX = np.linspace(.1, 25, 100)

# fit hyperbolic fxn
popt, pcov = curve_fit(funcHyp, xdata, ydata1_norm)
yHYP1 = funcHyp(trialX, *popt)
print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata2_norm)
yHYP2 = funcHyp(trialX, *popt)
print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata_avg)
yHYPavg = funcHyp(trialX, *popt)
print popt

# plot
plt.figure()

plt.plot(xdata, ydata1_norm, 'lightgray', ls = 'none', label='data', marker='s', markersize=6)
plt.plot(xdata, ydata2_norm, 'lightgray', ls = 'none', label='data', marker='s', markersize=6)
plt.plot(xdata, ydata_avg, 'k+', label='data', marker='s', markersize=6)
plt.plot(trialX, yHYP1, 'lightgray',ls='--', label='fit')
plt.plot(trialX, yHYP2, 'lightgray',ls='--', label='fit')
plt.plot(trialX, yHYPavg, 'k-',ls='--', label='fit')

plt.errorbar(xdata, ydata_avg, yerr=ydata_std, linestyle = "none", color = "black")
plt.xscale('linear', nonposy='clip')
#plt.ylim(0.6, 1.05)

plt.legend(loc=4)
plt.show()
