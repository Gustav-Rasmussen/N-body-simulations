# -*- coding: utf-8 -*-

# import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# from matplotlib.colors import LogNorm
# import time
import pylab
# from scipy.stats import norm
# import matplotlib.mlab as mlab
# import seaborn as sns
import RhoAndGaussianAndTsallis as ragat

FileLstbin1 = [('HQ10000_G0.8_2_000_bin3_VDFr.txt',
                'HQ10000_G0.8_2_000_bin3_VDFr'),
               ('HQ10000_G0.8_2_000_bin3_VDFt.txt',
                'HQ10000_G0.8_2_000_bin3_VDFt'),
               ('HQ10000_G1.2_3_005_bin4_VDFr.txt',
                'HQ10000_G1.2_3_005_bin4_VDFr'),
               ('HQ10000_G1.2_3_005_bin4_VDFt.txt',
                'HQ10000_G1.2_3_005_bin4_VDFt'),
               ('HQ10000_G1.2_9_005_bin5_VDFr.txt',
                'HQ10000_G1.2_9_005_bin5_VDFr'),
               ('HQ10000_G1.2_9_005_bin5_VDFt.txt',
                'HQ10000_G1.2_9_005_bin5_VDFt.txt')]

FileLstbin2 = [('HQ10000_G0.8_2_000_bin6_VDFr.txt',
                'HQ10000_G0.8_2_000_bin6_VDFr'),
               ('HQ10000_G0.8_2_000_bin6_VDFt.txt',
                'HQ10000_G0.8_2_000_bin6_VDFt'),
               ('HQ10000_G1.2_3_005_bin10_VDFr.txt',
                'HQ10000_G1.2_3_005_bin10_VDFr'),
               ('HQ10000_G1.2_3_005_bin10_VDFt.txt',
                'HQ10000_G1.2_3_005_bin10_VDFt'),
               ('HQ10000_G1.2_9_005_bin6_VDFr.txt',
                'HQ10000_G1.2_9_005_bin6_VDFr'),
               ('HQ10000_G1.2_9_005_bin6_VDFt.txt',
                'HQ10000_G1.2_9_005_bin6_VDFt.txt')]

FileLstbin3 = [('HQ10000_G0.8_2_000_bin10_VDFr.txt',
                'HQ10000_G0.8_2_000_bin10_VDFr'),
               ('HQ10000_G0.8_2_000_bin10_VDFt.txt',
                'HQ10000_G0.8_2_000_bin10_VDFt'),
               ('HQ10000_G1.2_3_005_bin13_VDFr.txt',
                'HQ10000_G1.2_3_005_bin13_VDFr'),
               ('HQ10000_G1.2_3_005_bin13_VDFt.txt',
                'HQ10000_G1.2_3_005_bin13_VDFt'),
               ('HQ10000_G1.2_9_005_bin10_VDFr.txt',
                'HQ10000_G1.2_9_005_bin10_VDFr'),
               ('HQ10000_G1.2_9_005_bin10_VDFt.txt',
                'HQ10000_G1.2_9_005_bin10_VDFt.txt')]

bin1 = [(pylab.loadtxt(f), l) for f, l in FileLstbin1]
bin2 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2]
bin3 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3]

# innerbin
plt.figure(1)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = bin1[0]
popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = bin1[1]
popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = bin1[0]
popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G0.8_2_000')
ax3.grid()

data, label = bin1[1]
popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 3, $\gamma = -0.5$')
ax4.grid()

plt.figure(2)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = bin1[2]
popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = bin1[3]
popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = bin1[2]
popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black', label=label,
         lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G1.2_3_005')
ax3.grid()

data, label = bin1[3]
popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black', label=label,
         lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 4, $\gamma = -0.5$')
ax4.grid()

plt.figure(3)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = bin1[4]
popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = bin1[5]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = bin1[4]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black', label=label, lw=2,
         ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G1.2_9_005')
ax3.grid()

data, label = bin1[5]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black', label=label, lw=2,
         ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 5, $\gamma = -0.5$')
ax4.grid()

# middlebin
plt.figure(4)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_middlebin[0]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue',
         label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_middlebin[1]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue',
         label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_middlebin[0]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G0.8_2_000')
ax3.grid()

data, label = datalist_middlebin[1]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 6, $\gamma = -1.5$')
ax4.grid()

plt.figure(5)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_middlebin[2]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_middlebin[3]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue',
         label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_middlebin[2]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G1.2_3_005')
ax3.grid()

data, label = datalist_middlebin[3]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 10, $\gamma = -2.5$')
ax4.grid()

plt.figure(6)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_middlebin[4]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue',
         label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_middlebin[5]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue',
         label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_middlebin[4]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G1.2_9_005')
ax3.grid()

data, label = datalist_middlebin[5]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 6, $\gamma = -1$')
ax4.grid()

# outerbin
plt.figure(7)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = bin4[0]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = bin4[1]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = bin4[0]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G0.8_2_000')
ax3.grid()

data, label = bin4[1]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 10, $\gamma = -2.5$')
ax4.grid()

plt.figure(8)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = bin4[2]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = bin4[3]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = bin4[2]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G1.2_3_005')
ax3.grid()

data, label = bin4[3]
popt, pcov = curve_fit(func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 13, $\gamma = -3$')
ax4.grid()

plt.figure(9)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = bin4[4]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax1.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax1.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = bin4[5]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax2.plot(data[:, 0], data[:, 1], color='Blue', label=label, lw=2, ms=7)
ax2.plot(data[:, 0], y_fit, '--', lw=3, color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = bin4[4]
popt, pcov = curve_fit(ragat.func_2, data[:, 0], data[:, 1])
y_fit = ragat.func_2(data[:, 0], popt[0], popt[1], popt[2])
ax3.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax3.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax3.set_title('HQ10000_G1.2_9_005')
ax3.grid()

data, label = bin4[5]
popt, pcov = curve_fit(ragat.func_1, data[:, 0], data[:, 1])
y_fit = ragat.func_1(data[:, 0], popt[0], popt[1], popt[2])
ax4.plot(data[:, 0], np.log10(data[:, 1]), color='Black',
         label=label, lw=2, ms=7)
ax4.plot(data[:, 0], np.log10(y_fit), '--', lw=3, color='green')
ax4.set_title(r'bin 10, $\gamma = -2.5$')
ax4.grid()

plt.show()
