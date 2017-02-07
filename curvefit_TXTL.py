#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

xdata = [0.1, 0.5, 1, 2, 5, 10, 20]

# ddGFP data
ydata1 = [30610.33, 33610.33, 36984.00, 39845.33, 41518.67, 41808.00, 45431.00] # 1/23
ydata2 = [28850.00, 33551.67, 35446.33, 38762.33, 39945.33, 42302.00, 43795.00] # 1/25
ydata3 = [38232.33, 37612.33, 40004.67, 41669.33, 43156.33, 42927.00, 46783.67] # 1/23
ydata4 = [44704.67, 42012.67, 46372.00, 47514.00, 50669.33, 50366.00, 49915.33] # 2/4
ydata5 = [44130.33, 42466.33, 45767.33, 47000.00, 49649.33, 49393.00, 49245.00] # 2/4
ydata6 = [44873.67, 42439.33, 47272.00, 47111.00, 50168.33, 49650.33, 49846.33] # 2/4
satpt = ydata1[-1]
ydata1_norm = [x / satpt for x in ydata1]
satpt = ydata2[-1]
ydata2_norm = [y / satpt for y in ydata2]
satpt = ydata3[-1]
ydata3_norm = [z / satpt for z in ydata3]
satpt = ydata4[-1]
ydata4_norm = [l / satpt for l in ydata4]
satpt = ydata5[-1]
ydata5_norm = [m / satpt for m in ydata5]
satpt = ydata6[-1]
ydata6_norm = [n / satpt for n in ydata6]

# ddRFP data
#RFPxdata = [0.1, 1, 10, 50, 200]
RFPxdata = [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]
#RFP1 = [16175.00, 17520.00, 18150.67, 18259.33, 18535.33] #1/20
RFP2 = [202950.33, 203955.00, 237793.33, 247993.33, 243903.33, 260283.33, 263960.00, 264170.00, 268793.33, 262210.00] #1/23
#RFP3 = [33927.00, 37075.67, 41038.67, 41134.00, 41730.67] #1/17
RFP4 = [82092.67, 80245.33, 80172.33, 78625.33, 82553.67, 75538.33, 79585.67, 86038.67, 86300.67, 92251.33] #2/4
RFP5 = [73811.33, 76708.33, 77805.00, 74427.67, 73278.67, 80947.67, 83713.00, 85375.33, 86835.00, 92648.67] #2/4
RFP6 = [87338.67, 86318.00, 85106.00, 80333.00, 83650.33, 79777.33, 91419.67, 91898.33, 87393.67, 94828.00] #2/4
satpt = RFP2[-1]
Rydata2_norm = [x / satpt for x in RFP2]
satpt = RFP4[-1]
Rydata4_norm = [y / satpt for y in RFP4]
satpt = RFP5[-1]
Rydata5_norm = [z / satpt for z in RFP5]
satpt = RFP6[-1]
Rydata6_norm = [z / satpt for z in RFP6]

# nanoBIT data
#xdata_nanoBIT= [0.1, 1, 10, 50, 100, 200, 500, 1000]
#nano1 = [1765.00, 1804.67, 1884.33, 1896.33, 1900.33, 1946.67, 1913.67, 1951.33]
#satpt = nano1[-1]
#nano1_norm = [x / satpt for x in nano1]

compiled_ydata = np.array([ydata4_norm, ydata5_norm, ydata6_norm])
compiled_Rydata = np.array([Rydata2_norm, Rydata5_norm, Rydata6_norm])

ydata_avg = np.mean(compiled_ydata, axis = 0)
ydata_std = np.std(compiled_ydata, axis = 0)

Rydata_avg = np.mean(compiled_Rydata, axis = 0)
Rydata_std = np.std(compiled_Rydata, axis = 0)

#def funcHyp(x, a):
#    return 1*x/(a+x)

def funcHyp(x, b, a, c):
    return a + ( (b-a) / (1 + (c/x)) )

trialX = np.linspace(.1, 1000, 1000)

# fit hyperbolic fxn
popt, pcov = curve_fit(funcHyp, xdata, ydata1_norm)
yHYP1 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata2_norm)
yHYP2 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata3_norm)
yHYP3 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata4_norm)
yHYP4 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata5_norm)
yHYP5 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata6_norm)
yHYP6 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata, ydata_avg)
yHYPavg = funcHyp(trialX, *popt)
print 'average ddGFP popt'
print popt
#print pcov
perr = np.sqrt(np.diag(pcov))
print perr

popt, pcov = curve_fit(funcHyp, RFPxdata, Rydata2_norm)
RyHYP2 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, RFPxdata, Rydata4_norm)
RyHYP4 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, RFPxdata, Rydata5_norm)
RyHYP5 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, RFPxdata, Rydata6_norm)
RyHYP6 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, RFPxdata, Rydata_avg)
RyHYPavg = funcHyp(trialX, *popt)
print 'average ddRFP popt'
print popt
#print pcov
perr = np.sqrt(np.diag(pcov))
print perr


#popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano1_norm)
#RyHYPavg = funcHyp(trialX, *popt)
#print 'nanoBIT popt'
#print popt

# plot
plt.figure()

#plt.plot(xdata, ydata1_norm, 'lightgreen', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata, ydata2_norm, 'lightgreen', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata, ydata3_norm, 'lightgreen', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata, ydata4_norm, 'lightgreen', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata, ydata5_norm, 'lightgreen', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata, ydata6_norm, 'lightgreen', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata, ydata_avg, 'g+', label='data', marker='s', markersize=6)
#plt.plot(trialX, yHYP1, 'lightgreen',ls='--')
#plt.plot(trialX, yHYP2, 'lightgreen',ls='--')
#plt.plot(trialX, yHYP3, 'lightgreen',ls='--')
#plt.plot(trialX, yHYP4, 'lightgreen',ls='--')
#plt.plot(trialX, yHYP5, 'lightgreen',ls='--')
#plt.plot(trialX, yHYP6, 'lightgreen',ls='--')
#plt.plot(trialX, yHYPavg, 'g-',ls='-', label='fit')

plt.plot(RFPxdata, Rydata2_norm, 'pink', ls = 'none', marker='s', markersize=6)
plt.plot(RFPxdata, Rydata4_norm, 'pink', ls = 'none', marker='s', markersize=6)
plt.plot(RFPxdata, Rydata5_norm, 'pink', ls = 'none', marker='s', markersize=6)
plt.plot(RFPxdata, Rydata6_norm, 'pink', ls = 'none', marker='s', markersize=6)
plt.plot(RFPxdata, Rydata_avg, 'r+', label='data', marker='s', markersize=6)
plt.plot(trialX, RyHYP2, 'pink',ls='--')
plt.plot(trialX, RyHYP4, 'pink',ls='--')
plt.plot(trialX, RyHYP5, 'pink',ls='--')
plt.plot(trialX, RyHYP6, 'pink',ls='--')
plt.plot(trialX, RyHYPavg, 'r-',ls='-', label='fit')

#plt.plot(xdata_nanoBIT, nano1_norm, 'k+', ls = 'none', marker='s', markersize=6)
#error_nano = [30.81, 66.16, 27.57, 50.21, 37.23, 40.20, 38.80, 69.29]
#plt.errorbar(xdata_nanoBIT, nano1_norm, yerr=error_nano, linestyle = "none", color = "black")


plt.xlabel('FPP concentration (uM)')
plt.ylabel('Normalized fluorescence (AU)')
#plt.title('FPP titration')

#plt.errorbar(xdata, ydata_avg, yerr=ydata_std, linestyle = "none", color = "black")
plt.errorbar(RFPxdata, Rydata_avg, yerr=Rydata_std, linestyle = "none", color = "black")
plt.xscale('log', nonposy='clip')
#plt.ylim(0.6, 1.05)

plt.legend(loc=4)
plt.show()
