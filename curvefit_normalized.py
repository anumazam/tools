#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

### raw data, - FPP

xdata_noFPP = [500, 200, 125, 62.5, 31.3, 15.6, 7.8]
xdata_noFPP_blue = [500, 250, 125, 62.5, 31.3, 15.6, 7.8]
xdata_noFPP_green = [500, 250, 125, 62.5]

# yellow data
ydata_noFPP1 = [0.60235321, 0.458304775, 0.445167923, 0.392049349]
# green data
ydata_noFPP2 = [0.70526939, 0.501835406, 0.394671403, 0.307045589]
# blue data
ydata_noFPP3 = [0.760076775, 0.758797185, 0.551503519, 0.333973129, 0.207933461, 0.076135637, 0.026231606]
# orange data
ydata_noFPP4 = [0.230425056, 0.157558325, 0.145893257, 0.116810483, 0.085810163, 0.062480026, 0.042825184]
# purple data
ydata_noFPP5 = [0.363253857, 0.254324451, 0.187704535, 0.148433848, 0.152173913, 0.101683029, 0.084385227]

### raw data, + FPP

xdata_FPP = [0.5, 1, 1.5, 2, 3, 6, 12]
xdata_FPP_blue = [0.5, 1, 1.5, 3, 6, 12]
xdata_FPP_yellow = [0.5, 1.5, 3, 12, 24]

# yellow data
ydata_FPP1 = [0.22832981, 0.312896406, 0.54756871, 0.78858351, 0.926004228]
# green data
ydata_FPP2 = [0.179916318, 0.188284519, 0.267782427, 0.581589958, 0.581589958, 0.80334728]
#blue data
ydata_FPP3 = [0.042513863, 0.262476895, 0.134935305, 0.251386322, 0.423290203, 0.597042514]
#orange data
ydata_FPP4 = [0.275526742, 0.405186386, 0.397082658, 0.479740681, 0.534846029, 0.610687023, 0.896272285]
# purple data
ydata_FPP5 = [0.220035778, 0.386404293, 0.509838998, 0.610017889, 0.729874776, 0.737030411, 0.906976744]


# define function
def funcHyp(x, a, b):
    return 1/((a/x)+1)

trialX_noFPP = np.linspace(0.1, 1000, 1000)
trialX_FPP = np.linspace(0.1, 1000, 1000)

popt, pcov = curve_fit(funcHyp, xdata_noFPP_green, ydata_noFPP1)
yHYP_noFPP1 = funcHyp(trialX_noFPP, *popt)
print "popt 1 no FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_noFPP_green, ydata_noFPP2)
yHYP_noFPP2 = funcHyp(trialX_noFPP, *popt)
print "popt 2 no FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_noFPP_blue, ydata_noFPP3)
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

popt, pcov = curve_fit(funcHyp, xdata_FPP_yellow, ydata_FPP1)
yHYP_FPP1 = funcHyp(trialX_FPP, *popt)
print "popt 1 FPP "
print popt

popt, pcov = curve_fit(funcHyp, xdata_FPP_blue, ydata_FPP2)
yHYP_FPP2 = funcHyp(trialX_FPP, *popt)
print "popt 2 FPP "
print popt

#popt, pcov = curve_fit(funcHyp, xdata_FPP_blue, ydata_FPP3)
#yHYP_FPP3 = funcHyp(trialX_FPP, *popt)
#print "popt 3 FPP "
#print popt

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

#plt.plot(xdata_noFPP_green, ydata_noFPP1, 'pink', ls='none', label='-FPP', marker='s', markersize=8)
#plt.plot(trialX_noFPP, yHYP_noFPP1, 'pink',ls='-')
#plt.plot(xdata_noFPP_green, ydata_noFPP2, 'chartreuse', ls='none', label='-FPP', marker='s', markersize=8)
#plt.plot(trialX_noFPP, yHYP_noFPP2, 'chartreuse',ls='-')
plt.plot(xdata_noFPP_blue, ydata_noFPP3, 'r+', label='-FPP', marker='s', markersize=8)
plt.plot(trialX_noFPP, yHYP_noFPP3, 'r-',ls='-')
plt.plot(xdata_noFPP, ydata_noFPP4, 'g+', label='-FPP', marker='s', markersize=8)
plt.plot(trialX_noFPP, yHYP_noFPP4, 'g-',ls='-')
plt.plot(xdata_noFPP, ydata_noFPP5, 'y+', label='-FPP', marker='s', markersize=8)
plt.plot(trialX_noFPP, yHYP_noFPP5, 'y-',ls='-')


plt.xscale('log', nonposy='clip')
plt.xlabel('AR concentration (uM)')
plt.ylabel('Normalized response')
plt.title('Effect of FPP on biosensor dimerization')

plt.plot(xdata_FPP_yellow, ydata_FPP1, 'maroon', ls='none', label='+200 uM FPP', marker='s', markersize=8)
plt.plot(trialX_FPP, yHYP_FPP1, 'maroon',ls='-')
plt.plot(xdata_FPP_blue, ydata_FPP2, 'm+', label='+200 uM FPP', marker='s', markersize=8)
plt.plot(trialX_FPP, yHYP_FPP2, 'm-',ls='-')
#plt.plot(xdata_FPP_blue, ydata_FPP3, 'k+', label='+200 uM FPP', marker='s', markersize=8)
#plt.plot(trialX_FPP, yHYP_FPP3, 'k-',ls='-')
plt.plot(xdata_FPP, ydata_FPP4, 'c+', label='+200 uM FPP', marker='s', markersize=8)
plt.plot(trialX_FPP, yHYP_FPP4, 'c-',ls='-')
plt.plot(xdata_FPP, ydata_FPP5, 'b+', label='+200 uM FPP', marker='s', markersize=8)
plt.plot(trialX_FPP, yHYP_FPP5, 'b-',ls='-')


#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.show()
