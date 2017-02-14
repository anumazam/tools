#!/usr/bin/python

# analyze ddRFP binding data from TxTl rxns.
from __future__ import division
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


# raw ddRFP data

xdata = [0.1, 0.5, 1, 2, 5, 10, 20, 50]

RFP1 = [1.89E+05, 2.15E+05, 2.52E+05, 2.17E+05, 2.29E+05, 2.31E+05, 2.70E+05, 2.65E+05] #1/23
RFP2 = [1.83E+05, 2.17E+05, 2.40E+05, 2.44E+05, 2.53E+05, 2.50E+05, 2.59E+05, 2.60E+05] #1/23
RFP3 = [1.61E+05, 1.91E+05, 2.22E+05, 2.83E+05, 2.50E+05, 2.99E+05, 2.63E+05, 2.67E+05] #1/23
#RFP4 = [82092.67, 80245.33, 80172.33, 78625.33, 82553.67, 75538.33, 79585.67, 86038.67] #2/4
#RFP5 = [73811.33, 76708.33, 77805.00, 74427.67, 73278.67, 80947.67, 83713.00, 85375.33] #2/4
#RFP6 = [87338.67, 86318.00, 85106.00, 80333.00, 83650.33, 79777.33, 91419.67, 91898.33 #2/4
#RFP7 = [2.67E+05, 1.80E+05, 1.81E+05, 2.30E+05, 2.77E+05, 2.98E+05, 3.10E+05, 2.94E+05] #2/10
#RFP8 = [1.34E+05, 2.15E+05, 1.99E+05, 2.33E+05, 3.20E+05, 2.70E+05, 3.09E+05, 2.77E+05] #2/10
#RFP9 = [81749, 1.30E+05, 1.67E+05, 2.44E+05, 2.83E+05, 2.62E+05, 2.49E+05, 3.25E+05] #2/10

# raw maltose data

maltose1 = [64035, 69398, 61733, 70428, 74670, 78389, 71429, 77258]
maltose2 = [60203, 72891, 70473, 73610, 77491, 88195, 82548, 82058]
maltose3 = [69013, 67783, 68653, 64318, 74765, 83659, 77139, 83226]

# raw sucrose data

#xdata_sucrose = [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]
#
#sucrose1 = [68968, 69215, 62083, 61647, 72320, 65709, 59757, 62582, 68133, 62821]
#sucrose2 = [80612, 62266, 62777, 66024, 67902, 68392, 66960, 62209, 74057, 71927]
#sucrose3 = [76006, 62603, 70811, 6.63E+04, 69720, 71805, 65234, 78308, 69058, 1.28E+05]

# normalization to saturation point

satpt = RFP1[-1]
ydata1_norm = [x / satpt for x in RFP1]
satpt = RFP2[-1]
ydata2_norm = [x / satpt for x in RFP2]
satpt = RFP3[-1]
ydata3_norm = [x / satpt for x in RFP3]
#satpt = RFP4[-1]
#ydata4_norm = [x / satpt for x in RFP4]
#satpt = RFP5[-1]
#ydata5_norm = [x / satpt for x in RFP5]
#satpt = RFP6[-1]
#ydata6_norm = [x / satpt for x in RFP6]
#satpt = RFP7[-1]
#ydata7_norm = [x / satpt for x in RFP7]
#satpt = RFP8[-1]
#ydata8_norm = [x / satpt for x in RFP8]
#satpt = RFP9[-1]
#ydata9_norm = [x / satpt for x in RFP9]

satpt = maltose1[-1]
maltose_ydata1_norm = [y / satpt for y in maltose1]
satpt = maltose2[-1]
maltose_ydata2_norm = [y / satpt for y in maltose2]
satpt = maltose3[-1]
maltose_ydata3_norm = [y / satpt for y in maltose3]

#satpt = sucrose1[-1]
#sucrose_ydata1_norm = [y / satpt for y in sucrose1]
#satpt = sucrose2[-1]
#sucrose_ydata2_norm = [y / satpt for y in sucrose2]
#satpt = sucrose3[-1]
#sucrose_ydata3_norm = [y / satpt for y in sucrose3]


compiled_ydata = np.array([ydata1_norm, ydata2_norm, ydata3_norm])
compiled_ydata_maltose = np.array([maltose_ydata1_norm, maltose_ydata2_norm, maltose_ydata3_norm])
#compiled_ydata_sucrose = np.array([sucrose_ydata1_norm, sucrose_ydata2_norm, sucrose_ydata3_norm])

ydata_avg = np.mean(compiled_ydata, axis = 0)
ydata_std = np.std(compiled_ydata, axis = 0)

maltose_ydata_avg = np.mean(compiled_ydata_maltose, axis = 0)
maltose_ydata_std = np.std(compiled_ydata_maltose, axis = 0)
#
#sucrose_ydata_avg = np.mean(compiled_ydata_sucrose, axis = 0)
#sucrose_ydata_std = np.std(compiled_ydata_sucrose, axis = 0)

# define and fit modified Hill equation to find EC50 / determine expected bound species

    # a = min asymptote (response when x = 0)
    # b = max asymptote or stabilized response for infinite dosage
    # c = EC50, or x value when 50% of species is bound, equal to KD for noncooperative ligand binding
    # assume Hill slope = 1 (otherwise use: a + ( (b-a) / (1 + (c/x)^d) ) where d = Hill slope.

def funcHyp(x, b, a, c):
    return a + ( (b-a) / (1 + (c/x)) )

trialX = np.linspace(.1, 50, 1000)

popt, pcov = curve_fit(funcHyp, xdata, ydata1_norm)
yHYP1 = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, ydata2_norm)
yHYP2 = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, ydata3_norm)
yHYP3 = funcHyp(trialX, *popt)

#popt, pcov = curve_fit(funcHyp, xdata, ydata4_norm)
#yHYP4 = funcHyp(trialX, *popt)
#
#popt, pcov = curve_fit(funcHyp, xdata, ydata5_norm)
#yHYP5 = funcHyp(trialX, *popt)
#
#popt, pcov = curve_fit(funcHyp, xdata, ydata6_norm)
#yHYP6 = funcHyp(trialX, *popt)
#
#popt, pcov = curve_fit(funcHyp, xdata, ydata7_norm)
#yHYP7 = funcHyp(trialX, *popt)
#
#popt, pcov = curve_fit(funcHyp, xdata, ydata8_norm)
#yHYP8 = funcHyp(trialX, *popt)
#
#popt, pcov = curve_fit(funcHyp, xdata, ydata9_norm)
#yHYP9 = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, ydata_avg)
yHYPavg = funcHyp(trialX, *popt)
print 'Calculated parameters from curve-fitting, [max, min, EC50]: '
print popt
perr = np.sqrt(np.diag(pcov))
print 'Error: '
print perr

popt, pcov = curve_fit(funcHyp, xdata, maltose_ydata1_norm)
yHYP1_maltose = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, maltose_ydata2_norm)
yHYP2_maltose = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, maltose_ydata3_norm)
yHYP3_maltose = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, maltose_ydata_avg)
yHYPavg_maltose = funcHyp(trialX, *popt)
print 'Calculated parameters from curve-fitting for maltose, [max, min, EC50]: '
print popt
perr = np.sqrt(np.diag(pcov))
print 'Error: '
print perr

#popt, pcov = curve_fit(funcHyp, xdata_sucrose, sucrose_ydata_avg)
#yHYPavg_sucrose = funcHyp(trialX, *popt)
#print 'Calculated parameters from curve-fitting for sucrose, [max, min, EC50]: '
#print popt
#perr = np.sqrt(np.diag(pcov))
#print 'Error: '
#print perr

# plot raw data and curves

plt.figure()

plt.plot(xdata, ydata1_norm, '#FFA07A', ls = 'none', marker='s', markersize=5)
plt.plot(xdata, ydata2_norm, '#FA8072', ls = 'none', marker='s', markersize=5)
plt.plot(xdata, ydata3_norm, '#E9967A', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, ydata4_norm, '#F08080', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, ydata5_norm, '#CD5C5C', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, ydata6_norm, '#DC143C', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, ydata7_norm, '#FF0000', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, ydata8_norm, '#B22222', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, ydata9_norm, '#8B0000', ls = 'none', marker='s', markersize=5)
plt.plot(xdata, ydata_avg, 'k+', marker='s', markersize=5, label='data')

#plt.plot(xdata, maltose_ydata1_norm, '#FF0000', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, maltose_ydata2_norm, '#B22222', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, maltose_ydata3_norm, '#8B0000', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata, maltose_ydata_avg, 'gray', ls = 'none', marker = 's', markersize = 5)

#plt.plot(xdata_sucrose, sucrose_ydata_avg, 'lightgray', ls = 'none', marker = 's', markersize = 5)

plt.plot(trialX, yHYP1, '#FFA07A',ls='dotted')
plt.plot(trialX, yHYP2, '#FA8072',ls='dotted')
plt.plot(trialX, yHYP3, '#E9967A',ls='dotted')
#plt.plot(trialX, yHYP4, '#F08080',ls='dotted')
#plt.plot(trialX, yHYP5, '#CD5C5C',ls='dotted')
#plt.plot(trialX, yHYP6, '#DC143C',ls='dotted')
#plt.plot(trialX, yHYP7, '#FF0000',ls='dotted')
#plt.plot(trialX, yHYP8, '#B22222',ls='dotted')
#plt.plot(trialX, yHYP9, '#8B0000',ls='dotted')
plt.plot(trialX, yHYPavg, 'k-',ls='-', lw='3', label='fit')

#plt.plot(trialX, yHYP1_maltose, '#FF0000',ls='dotted')
#plt.plot(trialX, yHYP2_maltose, '#B22222',ls='dotted')
#plt.plot(trialX, yHYP3_maltose, '#8B0000',ls='dotted')
#plt.plot(trialX, yHYPavg_maltose, 'gray', ls = '-', lw='3',label = '+ 1 mM maltose')

#plt.plot(trialX, yHYPavg_sucrose, 'lightgray', ls = '-', lw='3',label = '+ 1 mM sucrose')

plt.errorbar(xdata, ydata_avg, yerr=ydata_std, ls = "none", color="black")
#plt.errorbar(xdata, maltose_ydata_avg, yerr=maltose_ydata_std, linestyle = "none", color = "gray")
#plt.errorbar(xdata_sucrose, sucrose_ydata_avg, yerr=sucrose_ydata_std, linestyle = "none", color = "lightgray")

plt.xlabel('FPP concentration (uM)')
plt.xscale('linear', nonposy='clip')
plt.ylabel('Normalized response (AU)')
plt.title('FPP titration')

plt.legend(loc=4)
plt.show()

