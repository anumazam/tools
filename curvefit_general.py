#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [0.5, 1, 1.5, 3, 6, 12, 24]
Req = np.array([0.0059, 0.0084, 0.0048, 0.0218, 0.0256, 0.0352, 0.0568])
SSGRmax = 0.0842
norm_response = Req/SSGRmax

##### AVG DATA FROM CURVEFIT.py

xdata_FPP = [0.5, 1, 1.5, 2, 3, 6, 12, 24]
ydata_FPP = [0.225952162, 0.326625066, 0.371900122, 0.544879285, 0.598469869, 0.643102464, 0.848794955, 0.926004228]
error_FPP = [0.039232617, 0.120173924, 0.106431867, 0.092119897, 0.089798111, 0.082634764, 0.061454934, 0.061454934]
#####

#def funcHyp(x, b, a, c):
#    return a + ( (b-a) / (1 + (c/x)) )

def funcHyp(x, c):
    return ( 1 / (1 + (c/x)) )

trialX = np.linspace(.1, 150, 1000)

# fit hyperbolic fxn

#trialX_FPP = np.linspace(0.3, 10000, 1000)

popt, pcov = curve_fit(funcHyp, xdata, norm_response)
yHYP1 = funcHyp(trialX, *popt)
print popt

#####

popt, pcov = curve_fit(funcHyp, xdata_FPP, ydata_FPP)
yHYP_FPP = funcHyp(trialX, *popt)
print popt

#####

# plot
plt.figure()

plt.plot(xdata, norm_response, 'k', ls = 'none', label='+200uM FPP, +100mM maltose', marker='s', markersize=6)
plt.plot(trialX, yHYP1, 'lightgray',ls='--')

plt.plot(xdata_FPP, ydata_FPP, 'b+', label='+200uM FPP', marker='s', markersize=6)
plt.plot(trialX, yHYP_FPP, 'b-',ls='--')
plt.errorbar(xdata_FPP, ydata_FPP, yerr=error_FPP, linestyle = "none", color = "black")

plt.xscale('linear', nonposy='clip')
#plt.ylim(0, 1.25)
plt.xscale('log', nonposy='clip')
plt.xlabel('AR concentration (uM)')
plt.ylabel('Normalized response')
plt.title('Effect of maltose addition on S9G10 FPP biosensor')


plt.legend(loc=4)
plt.show()
