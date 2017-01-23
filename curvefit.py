#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata_noFPP = [500, 250, 200, 125, 62.5, 31.3, 15.6, 7.8]
ydata_noFPP = [1.000000046, 0.823575113, 0.691950578, 0.634824117, 0.488234805, 0.354962446, 0.217080759,0.15088949]
error_noFPP = [1.76721E-07, 0.153325427, 0.011565495, 0.098371588, 0.097873602,
         0.074227226, 0.10134406, 0.103427488]

xdata_FPP = [0.5, 1, 1.5, 2, 3, 6, 12]
ydata_FPP = [0.226945521, 0.38802961, 0.392258075, 0.603923118, 0.64817188, 0.731730787, 0.999999856]
error_FPP = [0.093410724, 0.102987031, 0.125067467, 0.097100952, 0.147154242, 0.056740852, 5.41186E-07]

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

plt.plot(xdata_noFPP, ydata_noFPP, 'g+', label='noFPP', marker='s', markersize=8)
plt.plot(trialX_noFPP, yHYP_noFPP, 'g-',ls='--', label="noFPP fit")
plt.errorbar(xdata_noFPP, ydata_noFPP, yerr=error_noFPP, linestyle = "none", color = "black")
plt.xscale('log', nonposy='clip')

plt.plot(xdata_FPP, ydata_FPP, 'b+', label='FPP', marker='s', markersize=8)
plt.plot(trialX_FPP, yHYP_FPP, 'b-',ls='--', label="FPP fit")
plt.errorbar(xdata_FPP, ydata_FPP, yerr=error_FPP, linestyle = "none", color = "black")
plt.legend(loc=4)
plt.show()
