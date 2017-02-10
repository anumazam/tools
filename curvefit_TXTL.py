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

# nanoBIT data from 2/9
xdata_nanoBIT= [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]
nano1 = [7396864.623, 7396864.623, 7397359.846, 7395874.179, 7399835.956, 7397855.068, 7399340.734, 7398845.512, 7400826.401, 7400826.401]
nano2 = [7403302.511, 7402312.067, 7404292.955, 7405778.622, 7406769.066, 7405283.4, 7407264.288, 7406769.066, 7408254.732, 7409740.399]
nano3 = [7407759.51, 7409740.399, 7410730.843, 7410235.621, 7411226.065, 7411226.065, 7412711.732, 7410730.843, 7411226.065, 7411226.065]
nano4 = [7349818.521, 7351304.187, 7353780.298, 7354275.52, 7354275.52, 7355761.187, 7356256.409, 7357742.075, 7359227.742, 7361208.63]
nano5 = [7361208.63, 7361208.63, 7363684.741, 7365170.407, 7366656.073, 7367151.296, 7370617.851, 7371113.073, 7371608.295, 7373589.183]
nano6 = [7374579.628, 7376560.516, 7377055.738, 7377550.96, 7380522.293, 7381512.737, 7383493.626, 7385474.514, 7385474.514, 7386464.959]
satpt = nano1[-1]
nano1_norm = [x / satpt for x in nano1]
satpt = nano2[-1]
nano2_norm = [x / satpt for x in nano2]
satpt = nano3[-1]
nano3_norm = [x / satpt for x in nano3]
satpt = nano4[-1]
nano4_norm = [x / satpt for x in nano4]
satpt = nano5[-1]
nano5_norm = [x / satpt for x in nano5]
satpt = nano6[-1]
nano6_norm = [x / satpt for x in nano6]

compiled_ydata = np.array([ydata1_norm, ydata2_norm, ydata3_norm, ydata4_norm, ydata5_norm, ydata6_norm])
compiled_Rydata = np.array([Rydata2_norm, Rydata5_norm, Rydata6_norm])
compiled_nanodata = np.array([nano4_norm, nano5_norm, nano6_norm])

ydata_avg = np.mean(compiled_ydata, axis = 0)
ydata_std = np.std(compiled_ydata, axis = 0)

Rydata_avg = np.mean(compiled_Rydata, axis = 0)
Rydata_std = np.std(compiled_Rydata, axis = 0)

nano_ydata_avg = np.mean(compiled_nanodata, axis = 0)
nano_ydata_std = np.std(compiled_nanodata, axis = 0)

#def funcHyp(x, a):
#    return 1*x/(a+x)

def funcHyp(x, b, a, c):
    return a + ( (b-a) / (1 + (c/x)) )

trialX = np.linspace(.1, 200, 1000)

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

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano1_norm)
nanoHYP1 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano2_norm)
nanoHYP2 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano3_norm)
nanoHYP3 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano4_norm)
nanoHYP4 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano5_norm)
nanoHYP5 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano6_norm)
nanoHYP6 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano_ydata_avg)
nanoHYPavg = funcHyp(trialX, *popt)
print 'average nanoBIT popt'
print popt
#print pcov
perr = np.sqrt(np.diag(pcov))
print perr

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
#
#plt.plot(RFPxdata, Rydata2_norm, 'pink', ls = 'none', marker='s', markersize=6)
#plt.plot(RFPxdata, Rydata4_norm, 'pink', ls = 'none', marker='s', markersize=6)
#plt.plot(RFPxdata, Rydata5_norm, 'pink', ls = 'none', marker='s', markersize=6)
#plt.plot(RFPxdata, Rydata6_norm, 'pink', ls = 'none', marker='s', markersize=6)
#plt.plot(RFPxdata, Rydata_avg, 'r+', label='data', marker='s', markersize=6)
#plt.plot(trialX, RyHYP2, 'pink',ls='--')
#plt.plot(trialX, RyHYP4, 'pink',ls='--')
#plt.plot(trialX, RyHYP5, 'pink',ls='--')
#plt.plot(trialX, RyHYP6, 'pink',ls='--')
#plt.plot(trialX, RyHYPavg, 'r-',ls='-', label='fit')

#plt.plot(xdata_nanoBIT, nano1_norm, 'lightgray', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata_nanoBIT, nano2_norm, 'lightgray', ls = 'none', marker='s', markersize=6)
#plt.plot(xdata_nanoBIT, nano3_norm, 'lightgray', ls = 'none', marker='s', markersize=6)
plt.plot(xdata_nanoBIT, nano4_norm, 'lightgray', ls = 'none', marker='s', markersize=6)
plt.plot(xdata_nanoBIT, nano5_norm, 'lightgray', ls = 'none', marker='s', markersize=6)
plt.plot(xdata_nanoBIT, nano6_norm, 'lightgray', ls = 'none', marker='s', markersize=6)
plt.plot(xdata_nanoBIT, nano_ydata_avg, 'k+', ls = 'none', marker='s', markersize=6)
#plt.plot(trialX, nanoHYP1, 'lightgray',ls='--')
#plt.plot(trialX, nanoHYP2, 'lightgray',ls='--')
#plt.plot(trialX, nanoHYP3, 'lightgray',ls='--')
plt.plot(trialX, nanoHYP4, 'lightgray',ls='--')
plt.plot(trialX, nanoHYP5, 'lightgray',ls='--')
plt.plot(trialX, nanoHYP6, 'lightgray',ls='--')
plt.plot(trialX, nanoHYPavg, 'black',ls='--')


plt.errorbar(xdata_nanoBIT, nano_ydata_avg, yerr=nano_ydata_std, linestyle = "none", color = "black")


plt.xlabel('FPP concentration (uM)')
plt.ylabel('Normalized response (AU)')
#plt.title('FPP titration')

#plt.errorbar(xdata, ydata_avg, yerr=ydata_std, linestyle = "none", color = "black")
#plt.errorbar(RFPxdata, Rydata_avg, yerr=Rydata_std, linestyle = "none", color = "black")
plt.xscale('linear', nonposy='clip')
#plt.ylim(0.6, 1.05)

plt.legend(loc=4)
plt.show()
