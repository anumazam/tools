#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

# raw data, - FPP

xdata_noFPP = [500, 200, 125, 62.5, 31.3, 15.6, 7.8]

# orange data norm
ydata_noFPP3 = [1, 0.683772538, 0.633148405, 0.506934813, 0.372399445, 0.271151179, 0.185852982]
# purple data norm
ydata_noFPP4 = [0.999999881, 0.700128617, 0.516730955, 0.40862286, 0.418918869, 0.279922747, 0.232303705]
# purple data
ydata_noFPP5 = [0.783777466, 0.444834035, 0.384291725, 0.270453483, 0.210378682, 0.164329126, 0.103786816]

# raw data, + FPP

xdata_FPP = [0.5, 1, 1.5, 2, 3, 6, 12]

# orange data norm
ydata_FPP3 = [0.307414203, 0.45207971, 0.443038116, 0.535262377, 0.596745217, 0.681363496, 1.000000318]
# purple data norm
ydata_FPP4 = [0.242603562, 0.426035524, 0.562130205, 0.672583859, 0.804733767, 0.812623314, 1.000000049]
# purple data
ydata_FPP5 = [0.220035778, 0.386404293, 0.509838998, 0.610017889, 0.729874776, 0.737030411, 0.906976744]


# define function
def funcHyp(x, a, b):
    return 1/((a/x)+1)

trialX_noFPP = np.linspace(.1, 1000, 1000)
trialX_FPP = np.linspace(0.1, 1000, 1000)


popt, pcov = curve_fit(funcHyp, xdata_noFPP, ydata_noFPP3)
yHYP_noFPP3 = funcHyp(trialX_noFPP, *popt)
print "popt 3 no FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_noFPP, ydata_noFPP4)
yHYP_noFPP4 = funcHyp(trialX_noFPP, *popt)
print "popt 4 no FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_noFPP, ydata_noFPP5)
yHYP_noFPP5 = funcHyp(trialX_noFPP, *popt)
print "popt 5 no FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_FPP, ydata_FPP3)
yHYP_FPP3 = funcHyp(trialX_FPP, *popt)
print "popt 3 FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_FPP, ydata_FPP4)
yHYP_FPP4 = funcHyp(trialX_FPP, *popt)
print "popt 4 FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_FPP, ydata_FPP5)
yHYP_FPP5 = funcHyp(trialX_FPP, *popt)
print "popt 5 FPP "
print popt

# plot
plt.figure()

#plt.plot(xdata_noFPP, ydata_noFPP1, 'r+', label='-FPP', marker='s', markersize=8)
#plt.plot(trialX_noFPP, yHYP_noFPP1, 'r-',ls='-')
#plt.plot(xdata_noFPP, ydata_noFPP2, 'g+', label='-FPP', marker='s', markersize=8)
#plt.plot(trialX_noFPP, yHYP_noFPP2, 'g-',ls='-')
#plt.plot(xdata_noFPP, ydata_noFPP3, 'y+', label='-FPP', marker='s', markersize=8)
#plt.plot(trialX_noFPP, yHYP_noFPP3, 'y-',ls='-')
#plt.plot(xdata_noFPP, ydata_noFPP4, 'b+', label='-FPP', marker='s', markersize=8)
#plt.plot(trialX_noFPP, yHYP_noFPP4, 'b-',ls='-')
plt.plot(xdata_noFPP, ydata_noFPP5, 'b+', label='-FPP', marker='s', markersize=8)
plt.plot(trialX_noFPP, yHYP_noFPP5, 'b-',ls='-')


plt.xscale('log', nonposy='clip')
plt.xlabel('AR concentration (uM)')
plt.ylabel('Normalized response')
plt.title('Effect of FPP on biosensor dimerization')

#plt.plot(xdata_FPP, ydata_FPP1, 'y+', label='+200 uM FPP', marker='s', markersize=8)
#plt.plot(trialX_FPP, yHYP_FPP1, 'y-',ls='-')
#plt.plot(xdata_FPP, ydata_FPP2, 'b+', label='+200 uM FPP', marker='s', markersize=8)
#plt.plot(trialX_FPP, yHYP_FPP2, 'b-',ls='-')
#plt.plot(xdata_FPP, ydata_FPP3, 'y+', label='+200 uM FPP', marker='s', markersize=8)
#plt.plot(trialX_FPP, yHYP_FPP3, 'y-',ls='-')
#plt.plot(xdata_FPP, ydata_FPP4, 'b+', label='+200 uM FPP', marker='s', markersize=8)
#plt.plot(trialX_FPP, yHYP_FPP4, 'b-',ls='-')
plt.plot(xdata_FPP, ydata_FPP5, 'b+', label='+200 uM FPP', marker='s', markersize=8)
plt.plot(trialX_FPP, yHYP_FPP5, 'b-',ls='-')


plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
