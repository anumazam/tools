#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [0.5, 1, 1.5, 3, 6, 12, 24]

Req1 = np.array([0.0059, 0.0084, 0.0048, 0.0218, 0.0256, 0.0352, 0.0568])
SSGRmax1 = 0.0842
norm_response1 = Req1/SSGRmax1

Req2 = np.array([0, 0.0038, 0.0037, 0.0037, 0.0048, 0.0142, 0.0202])
SSGRmax2 = 0.0567
norm_response2 = Req2/SSGRmax2

Req3 = np.array([0, 0, 0.0058, 0.0011, 0.0038, 0.0121, 0.0159])
SSGRmax3 = 0.0426
norm_response3 = Req3/SSGRmax3

compiled_response = np.array([norm_response1, norm_response2, norm_response3])

ydata_avg = np.mean(compiled_response, axis = 0)
ydata_std = np.std(compiled_response, axis = 0)

##### AVG DATA FROM CURVEFIT.py

xdata_FPP = [0.5, 1, 1.5, 2, 3, 6, 12, 24]
ydata_FPP = [0.225952162, 0.326625066, 0.371900122, 0.544879285, 0.598469869, 0.643102464, 0.848794955, 0.926004228]
error_FPP = [0.039232617, 0.120173924, 0.106431867, 0.092119897, 0.089798111, 0.082634764, 0.061454934, 0.061454934]
#####

def funcHyp(x, a):
    return 1*x/(a+x)

#def funcHyp(x, b, a, c):
#    return a + ( (b-a) / (1 + (c/x)) )

#def funcHyp(x, c):
#    return ( 1 / (1 + (c/x)) )

trialX = np.linspace(.1, 25, 1000)

# fit hyperbolic fxn

popt, pcov = curve_fit(funcHyp, xdata, ydata_avg)
yHYP1 = funcHyp(trialX, *popt)
print 'average +maltose data'
print popt

perr = np.sqrt(np.diag(pcov))
print 'stdv +maltose data'
print perr

popt, pcov = curve_fit(funcHyp, xdata_FPP, ydata_FPP)
yHYP_FPP = funcHyp(trialX, *popt)
print 'average FPP data'
print popt

perr = np.sqrt(np.diag(pcov))
print 'stdv +maltose data'
print perr

#####

# plot
plt.figure()

plt.plot(xdata, ydata_avg, 'k', ls = 'none', label='+200uM FPP, +100mM maltose', marker='s', markersize=6)
plt.plot(trialX, yHYP1, 'lightgray',ls='--')
plt.errorbar(xdata, ydata_avg, yerr=ydata_std, linestyle = "none", color = "black")

plt.plot(xdata_FPP, ydata_FPP, 'b+', label='+200uM FPP', marker='s', markersize=6)
plt.plot(trialX, yHYP_FPP, 'b-',ls='--')
plt.errorbar(xdata_FPP, ydata_FPP, yerr=error_FPP, linestyle = "none", color = "black")

#plt.ylim(0, 1.25)
plt.xscale('linear', nonposy='clip')
plt.xlabel('AR concentration (uM)')
plt.ylabel('Normalized response')
plt.title('Effect of maltose addition on S9G10 FPP biosensor')


plt.legend(loc=4)
plt.show()
