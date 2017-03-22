#!/usr/bin/python

# this is a tool for fitting binding curves.

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import matplotlib
import matplotlib as mpl

xdata = [0, 0.1, 0.5, 1, 2, 5, 10, 20]


# ddGFP data
ydata1 = [0, 610.33, 3610.33, 6984.00, 9845.33, 11518.67, 11808.00, 15431.00] # 1/23
ydata2 = [0, 8850.00, 13551.67, 15446.33, 18762.33, 19945.33, 22302.00, 23795.00] # 1/25
ydata3 = [0, 8232.33, 7612.33, 10004.67, 11669.33, 13156.33, 12927.00, 16783.67] # 1/23
ydata4 = [0, 4704.67, 2012.67, 6372.00, 7514.00, 10669.33, 17366.00, 19915.33] # 2/4
ydata5 = [0, 3130.33, 3466.33, 5767.33, 7000.00, 9649.33, 9293.00, 9245.00] # 2/4
ydata6 = [0, 3873.67, 3439.33, 7272.00, 7111.00, 10168.33, 9650.33, 9846.33] # 2/4
satpt = ydata1[-1]
ydata1_norm = [x / 14000 for x in ydata1]
satpt = ydata2[-1]
ydata2_norm = [y / 23000 for y in ydata2]
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
xdata_nanoBIT= [0, 0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]
nano1 = [0.01, 7396864.623, 7396864.623, 7397359.846, 7395874.179, 7399835.956, 7397855.068, 7399340.734, 7398845.512, 7400826.401, 7400826.401]
nano2 = [0.01, 7403302.511, 7402312.067, 7404292.955, 7405778.622, 7406769.066, 7405283.4, 7407264.288, 7406769.066, 7408254.732, 7409740.399]
nano3 = [0.01, 7407759.51, 7409740.399, 7410730.843, 7410235.621, 7411226.065, 7411226.065, 7412711.732, 7410730.843, 7411226.065, 7411226.065]
nano4 = [0, 9818.521, 11304.187, 13780.298, 14275.52, 14275.52, 15761.187, 16256.409, 17742.075, 19227.742, 21208.63]
nano5 = [0, 1208.63, 1208.63, 3684.741, 5170.407, 6656.073, 7151.296, 10617.851, 11113.073, 11608.295, 13589.183]
nano6 = [0, 4579.628, 6560.516, 7055.738, 7550.96, 10522.293, 11512.737, 13493.626, 15474.514, 15474.514, 16464.959]
nano7 = [0, 5839.31, 7324.98, 9801.09, 10791.53, 13267.64, 18219.86, 17229.42, 18219.86, 22676.86, 22676.86]
nano8 = [0, 7133.86, 8124.30, 8124.30, 12581.30, 12581.30, 11590.86, 16047.86, 18523.97, 19514.41, 19019.19]
nano9 = [0, 7437.97, 9418.86, 9418.86, 11894.97, 13875.86, 15361.52, 19818.52, 19818.52, 25761.19, 29227.74]
nano10 = [0, 6751.630852, 7742.075114, 9227.741508, 17151.29561, 14179.96282, 17151.29561, 19132.18413, 18141.73987, 19132.18413, 23589.18331]
nano11 = [0, 5570.071837, 6065.293968, 10027.07102, 11512.73741, 12503.18167, 13493.62594, 15474.51446, 15969.73659, 16960.18085, 18445.84725]
nano12 = [0, 921.957903, 4883.734953, 3893.29069, 5378.957084, 8350.289871, 11321.62266, 8845.512002, 10826.40053, 12312.06692, 15283.39971]
satpt = nano1[-2]
nano1_norm = [x / satpt for x in nano1]
satpt = nano2[-2]
nano2_norm = [x / satpt for x in nano2]
satpt = nano3[-2]
nano3_norm = [x / satpt for x in nano3]
satpt = nano4[-2]
nano4_norm = [x / 17000 for x in nano4]
satpt = nano5[-2]
nano5_norm = [x / 10000 for x in nano5]
satpt = nano6[-2]
nano6_norm = [x / satpt for x in nano6]
satpt = nano7[-2]
nano7_norm = [x / satpt for x in nano7]
satpt = nano8[-2]
nano8_norm = [x / satpt for x in nano8]
satpt = nano9[-2]
nano9_norm = [x / satpt for x in nano9]
satpt = nano10[-2]
nano10_norm = [x / satpt for x in nano10]
satpt = nano11[-2]
nano11_norm = [x / satpt for x in nano11]
satpt = nano12[-2]
nano12_norm = [x / satpt for x in nano12]


# nanoBIT data WITH MALTOSE 2/15
# xdata_nanoBIT= [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]
maltose1 = [522.293149, 522.293149, 2007.959542, 2503.181673, 5969.736592, 7455.402985, 8941.069379, 9436.29151, 10426.73577, 14388.51282]
maltose2 = [4883.734953, 4883.734953, 7855.06774, 9340.734133, 9340.734133, 11816.84479, 13302.51118, 13302.51118, 17759.51036, 18749.95463]
maltose3 = [1721.287413, 4692.6202, 7168.730856, 5187.842331, 5187.842331, 9644.841512, 13111.39643, 9149.619381, 12120.95217, 15092.28495]
satpt = maltose1[-1]
maltose1_norm = [x / satpt for x in maltose1]
satpt = maltose2[-1]
maltose2_norm = [x / satpt for x in maltose2]
satpt = maltose3[-1]
maltose3_norm = [x / satpt for x in maltose3]

compiled_ydata = np.array([ydata1_norm, ydata2_norm, ydata3_norm, ydata4_norm, ydata5_norm])
compiled_Rydata = np.array([Rydata2_norm, Rydata5_norm, Rydata6_norm])
compiled_nanodata = np.array([nano4_norm, nano5_norm, nano6_norm, nano7_norm, nano8_norm, nano9_norm, nano10_norm, nano11_norm, nano12_norm])
compiled_maltosedata = np.array([maltose1_norm, maltose2_norm, maltose3_norm])

ydata_avg = np.mean(compiled_ydata, axis = 0)
ydata_std = np.std(compiled_ydata, axis = 0)

Rydata_avg = np.mean(compiled_Rydata, axis = 0)
Rydata_std = np.std(compiled_Rydata, axis = 0)

nano_ydata_avg = np.mean(compiled_nanodata, axis = 0)
nano_ydata_std = np.std(compiled_nanodata, axis = 0)

maltose_ydata_avg = np.mean(compiled_maltosedata, axis = 0)
maltose_ydata_std = np.std(compiled_maltosedata, axis = 0)

#def funcHyp(x, a):
#    return 1*x/(a+x)

def funcHyp(x, b, a, c):
    return a + ( (b-a) / (1 + (c/x)) )

trialX = np.linspace(-.35, 50, 1000)

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
#nanoHYP1 = funcHyp(trialX, *popt)
##print popt
#
#popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano2_norm)
#nanoHYP2 = funcHyp(trialX, *popt)
##print popt
#
#popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano3_norm)
#nanoHYP3 = funcHyp(trialX, *popt)
##print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano4_norm)
nanoHYP4 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano5_norm)
nanoHYP5 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano6_norm)
nanoHYP6 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano7_norm)
nanoHYP7 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano8_norm)
nanoHYP8 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano9_norm)
nanoHYP9 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano10_norm)
nanoHYP10 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano11_norm)
nanoHYP11 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano12_norm)
nanoHYP12 = funcHyp(trialX, *popt)
#print popt

popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, nano_ydata_avg)
nanoHYPavg = funcHyp(trialX, *popt)
print 'average nanoBIT popt'
print popt
#print pcov
perr = np.sqrt(np.diag(pcov))
print perr

#popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, maltose1_norm)
#maltoseHYP1 = funcHyp(trialX, *popt)
##print popt
#
#popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, maltose2_norm)
#maltoseHYP2 = funcHyp(trialX, *popt)
##print popt
#
#popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, maltose3_norm)
#maltoseHYP3 = funcHyp(trialX, *popt)
##print popt
#
#popt, pcov = curve_fit(funcHyp, xdata_nanoBIT, maltose_ydata_avg)
#maltoseHYPavg = funcHyp(trialX, *popt)
#print 'average maltose popt'
#print popt
##print pcov
#perr = np.sqrt(np.diag(pcov))
#print perr

# plot
#plt.figure()

plt.figure(num=None, figsize=(6, 5), dpi=80, facecolor='w', edgecolor='k')
font = {'family' : 'arial',
    'weight' : 'regular',
        'size'   : 18}
matplotlib.rc('font', **font)


#plt.plot(xdata, ydata1_norm, '#d5f4e6', ls = 'none', marker='s', markersize=5, mec='k')
#plt.plot(xdata, ydata2_norm, '#80ced6', ls = 'none', marker='s', markersize=5, mec='k')
#plt.plot(xdata, ydata3_norm, '#fefbd8', ls = 'none', marker='s', markersize=5, mec='k')
##plt.plot(xdata, ydata4_norm, 'lightgreen', ls = 'none', marker='s', markersize=5, mec='k')
##plt.plot(xdata, ydata5_norm, 'lightgreen', ls = 'none', marker='s', markersize=5, mec='k')
##plt.plot(xdata, ydata6_norm, 'lightgreen', ls = 'none', marker='s', markersize=5, mec='k')
#plt.plot(xdata, ydata_avg, 'k+', ls = 'none', marker='s', markersize=7, mec='k')
#plt.plot(trialX, yHYP1, '#d5f4e6',ls='dotted')
#plt.plot(trialX, yHYP2, '#80ced6',ls='dotted')
#plt.plot(trialX, yHYP3, '#fefbd8',ls='dotted')
##plt.plot(trialX, yHYP4, 'lightgreen',ls='--')
##plt.plot(trialX, yHYP5, 'lightgreen',ls='--')
##plt.plot(trialX, yHYP6, 'lightgreen',ls='--')
#plt.plot(trialX, yHYPavg, 'black',ls='-', lw='3')
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
#plt.plot(xdata_nanoBIT, nano10_norm, 'lightblue', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata_nanoBIT, nano11_norm, 'lightblue', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata_nanoBIT, nano12_norm, 'lightblue', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata_nanoBIT, nano7_norm, '#f1e3dd', ls = 'none', marker='s', markersize=5, mec='k')
#plt.plot(xdata_nanoBIT, nano8_norm, '#cfe0e8', ls = 'none', marker='s', markersize=5, mec='k')
#plt.plot(xdata_nanoBIT, nano9_norm, 'lightgray', ls = 'none', marker='s', markersize=5, mec='k')
plt.plot(xdata_nanoBIT, nano_ydata_avg, 'k', ls = 'none', marker='s', markersize=7)
#plt.plot(trialX, nanoHYP1, 'lightgray',ls='--')
#plt.plot(trialX, nanoHYP2, 'lightgray',ls='--')
#plt.plot(trialX, nanoHYP3, 'lightgray',ls='--')
#plt.plot(trialX, nanoHYP4, '#bccad6',ls='dotted')
#plt.plot(trialX, nanoHYP5, '#8d9db6',ls='dotted')
#plt.plot(trialX, nanoHYP6, '#667292',ls='dotted')
#plt.plot(trialX, nanoHYP10, 'lightblue',ls='--')
#plt.plot(trialX, nanoHYP11, 'lightblue',ls='--')
#plt.plot(trialX, nanoHYP12, 'lightblue',ls='--')
plt.plot(trialX, nanoHYPavg, 'k',ls='-', lw='3')


#plt.plot(xdata_nanoBIT, maltose1_norm, 'lightgray', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata_nanoBIT, maltose2_norm, 'lightgray', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata_nanoBIT, maltose3_norm, 'lightgray', ls = 'none', marker='s', markersize=5)
#plt.plot(xdata_nanoBIT, maltose_ydata_avg, 'k+', ls = 'none', marker='s', markersize=5, mec='k')
#plt.plot(trialX, maltoseHYP1, 'lightgray',ls='--')
#plt.plot(trialX, maltoseHYP2, 'lightgray',ls='--')
#plt.plot(trialX, maltoseHYP3, 'lightgray',ls='--')
#plt.plot(trialX, maltoseHYPavg, 'black',ls='-', lw='4', label='+maltose')
#
#
plt.errorbar(xdata_nanoBIT, nano_ydata_avg, yerr=nano_ydata_std, linestyle = "none", color = "black")
#plt.errorbar(xdata_nanoBIT, maltose_ydata_avg, yerr=maltose_ydata_std, linestyle = "none", color = "black")


plt.xlabel(r'FPP concentration ($\mu$M)')
plt.ylabel('Normalized response (AU)')
plt.title('LgBIT-AR/MBP-SmBIT')

#plt.errorbar(xdata, ydata_avg, yerr=ydata_std, linestyle = "none", color = "black")
#plt.errorbar(RFPxdata, Rydata_avg, yerr=Rydata_std, linestyle = "none", color = "black")
plt.xscale('linear', nonposy='clip')
plt.ylim(-.05, 1.1)
plt.xlim(-1, 51)


#plt.legend(loc=4)
plt.show()
