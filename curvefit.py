#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata_noFPP = [500, 250, 125, 62.5, 31.3, 15.6, 7.8]
ydata_noFPP = [0.607738308, 0.572979122, 0.394761845, 0.295375479, 0.180053687, 0.088909333, 0.055308416]
error_noFPP = [0.175614129, 0.162388403, 0.152732296, 0.104185172, 0.039427955, 0.018064735, 0.04112082]

xdata_FPP = [0.5, 1, 1.5, 2, 3, 6, 12, 24]
ydata_FPP = [0.225952162, 0.326625066, 0.371900122, 0.544879285, 0.598469869, 0.643102464, 0.848794955, 0.926004228]
error_FPP = [0.039232617, 0.120173924, 0.106431867, 0.092119897, 0.089798111, 0.082634764, 0.061454934, 0.061454934]

def funcHyp(x, a):
    return 1/((a/x)+1)

trialX_noFPP = np.linspace(0.3, 1000, 1000)
trialX_FPP = np.linspace(0.3, 1000, 1000)

# fit hyperbolic fxn
popt, pcov = curve_fit(funcHyp, xdata_noFPP, ydata_noFPP)
yHYP_noFPP = funcHyp(trialX_noFPP, *popt)
print popt

popt, pcov = curve_fit(funcHyp, xdata_FPP, ydata_FPP)
yHYP_FPP = funcHyp(trialX_FPP, *popt)
print popt

# plot
plt.figure()

plt.plot(xdata_noFPP, ydata_noFPP, 'g+', label='-FPP', marker='s', markersize=8)
plt.plot(trialX_noFPP, yHYP_noFPP, 'g-',ls='-')
plt.errorbar(xdata_noFPP, ydata_noFPP, yerr=error_noFPP, linestyle = "none", color = "black")

plt.xscale('log', nonposy='clip')
plt.xlabel('AR concentration (uM)')
plt.ylabel('Normalized response')
plt.title('Effect of FPP on biosensor dimerization')

plt.plot(xdata_FPP, ydata_FPP, 'b+', label='+200 uM FPP', marker='s', markersize=8)
plt.plot(trialX_FPP, yHYP_FPP, 'b-',ls='-')
plt.errorbar(xdata_FPP, ydata_FPP, yerr=error_FPP, linestyle = "none", color = "black")
plt.legend(loc=4)
plt.show()
