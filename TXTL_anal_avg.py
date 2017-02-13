#!/usr/bin/python

# analyze ddRFP binding data from TxTl rxns.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


# raw ddRFP data

xdata = [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]

RFP1 = [197676.67, 207636.67, 237793.33, 247993.33, 243903.33, 260283.33, 263960.00, 264170.00, 268793.33, 262210.00] #1/23
RFP2 = [73811.33, 76708.33, 77805.00, 74427.67, 73278.67, 80947.67, 83713.00, 85375.33, 86835.00, 92648.67] #2/4
RFP3 = [160946.33, 174836.67, 182423.33, 235703.33, 293670.00, 276890.00, 289036.67, 298386.67, 283650.00, 258313.33] #2/10

#RFP1_error = [46125.72, 14889.63, 15154.07, 32813.19, 13235.25, 35282.29, 5273.22, 3761.06, 20505.62, 15042.22]
#RFP2_error = [9627.77, 5127.72, 2108.81, 3841.39, 9958.73, 3714.66, 4850.61, 8994.54, 12911.58, 10184.63]
#RFP3_error = [95514.86, 42732.11, 15790.41, 7064.17, 23302.13, 18997.38, 34851.05, 24503.38, 22805.06, 58030.00]

# normalization to saturation point

satpt = RFP1[-1]
ydata1_norm = [x / satpt for x in RFP1]
satpt = RFP2[-1]
ydata2_norm = [x / satpt for x in RFP2]
satpt = RFP3[-1]
ydata3_norm = [x / satpt for x in RFP3]

#satpt = RFP1_error[-1]
#ydata1_norm_error = [x / satpt for x in RFP1_error]
#satpt = RFP2_error[-1]
#ydata2_norm_error = [x / satpt for x in RFP2_error]
#satpt = RFP3_error[-1]
#ydata3_norm_error = [x / satpt for x in RFP3_error]

# compute statistics

compiled_ydata = np.array([ydata1_norm, ydata2_norm, ydata3_norm])

ydata_avg = np.mean(compiled_ydata, axis = 0)
ydata_std = np.std(compiled_ydata, axis = 0)

# define and fit modified Hill equation to find EC50 / determine expected bound species

    # a = min asymptote (response when x = 0)
    # b = max asymptote or stabilized response for infinite dosage
    # c = EC50, or x value when 50% of species is bound, equal to KD for noncooperative ligand binding
    # assume Hill slope = 1 (otherwise use: a + ( (b-a) / (1 + (c/x)^d) ) where d = Hill slope.

def funcHyp(x, b, a, c):
    return a + ( (b-a) / (1 + (c/x)) )

trialX = np.linspace(.1, 200, 1000)

popt, pcov = curve_fit(funcHyp, xdata, ydata1_norm)
yHYP1 = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, ydata2_norm)
yHYP2 = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, ydata3_norm)
yHYP3 = funcHyp(trialX, *popt)

popt, pcov = curve_fit(funcHyp, xdata, ydata_avg)
yHYPavg = funcHyp(trialX, *popt)
print 'Calculated parameters from curve-fitting, [max, min, EC50]: '
print popt
perr = np.sqrt(np.diag(pcov))
print 'Error: '
print perr

# plot raw data and curves

plt.figure()

plt.plot(xdata, ydata1_norm, '#FFA07A', ls = 'none', marker='s', markersize=5)
plt.plot(xdata, ydata2_norm, '#FA8072', ls = 'none', marker='s', markersize=5)
plt.plot(xdata, ydata3_norm, '#E9967A', ls = 'none', marker='s', markersize=5)

plt.plot(xdata, ydata_avg, 'k+', label='data', marker='s', markersize=5)

plt.plot(trialX, yHYP1, '#FFA07A',ls='dotted')
plt.plot(trialX, yHYP2, '#FA8072',ls='dotted')
plt.plot(trialX, yHYP3, '#E9967A',ls='dotted')

plt.plot(trialX, yHYPavg, 'k-',ls='-', lw='3', label='fit')

plt.xscale('log', nonposy='clip')

#plt.errorbar(xdata, ydata1_norm, yerr=ydata1_norm_error, linestyle = "none", color = "#FFA07A")
plt.errorbar(xdata, ydata_avg, yerr=ydata_std, linestyle = "none", color = "black")


plt.xlabel('FPP concentration (uM)')
plt.ylabel('Normalized response (AU)')
plt.title('FPP titration')

plt.legend(loc=4)
plt.show()

