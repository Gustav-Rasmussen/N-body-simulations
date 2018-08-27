# -*- coding: utf-8 -*-

import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
import pylab
from scipy.stats import norm
import matplotlib.mlab as mlab
import seaborn as sns


def func_1(x, a, b, c):
    return a * x*np.exp(-b * x**2) + c


def func_2(x, a, b, c):
    return a * np.exp(-b * x ** 2) + c


list_of_files_innerbin = [('Hernquist10000_G0.8_2_000_bin3_VDFr.txt',
                           'Hernquist10000_G0.8_2_000_bin3_VDFr'),
                          ('Hernquist10000_G0.8_2_000_bin3_VDFt.txt',
                           'Hernquist10000_G0.8_2_000_bin3_VDFt'),
                          ('Hernquist10000_G1.2_3_005_bin4_VDFr.txt',
                           'Hernquist10000_G1.2_3_005_bin4_VDFr'),
                          ('Hernquist10000_G1.2_3_005_bin4_VDFt.txt',
                           'Hernquist10000_G1.2_3_005_bin4_VDFt'),
                          ('Hernquist10000_G1.2_9_005_bin5_VDFr.txt',
                           'Hernquist10000_G1.2_9_005_bin5_VDFr'),
                          ('Hernquist10000_G1.2_9_005_bin5_VDFt.txt',
                           'Hernquist10000_G1.2_9_005_bin5_VDFt.txt')]

list_of_files_middlebin = [('Hernquist10000_G0.8_2_000_bin6_VDFr.txt',
                            'Hernquist10000_G0.8_2_000_bin6_VDFr'),
                           ('Hernquist10000_G0.8_2_000_bin6_VDFt.txt',
                            'Hernquist10000_G0.8_2_000_bin6_VDFt'),
                           ('Hernquist10000_G1.2_3_005_bin10_VDFr.txt',
                            'Hernquist10000_G1.2_3_005_bin10_VDFr'),
                           ('Hernquist10000_G1.2_3_005_bin10_VDFt.txt',
                            'Hernquist10000_G1.2_3_005_bin10_VDFt'),
                           ('Hernquist10000_G1.2_9_005_bin6_VDFr.txt',
                            'Hernquist10000_G1.2_9_005_bin6_VDFr'),
                           ('Hernquist10000_G1.2_9_005_bin6_VDFt.txt',
                            'Hernquist10000_G1.2_9_005_bin6_VDFt.txt')]

list_of_files_outerbin = [('Hernquist10000_G0.8_2_000_bin10_VDFr.txt',
                           'Hernquist10000_G0.8_2_000_bin10_VDFr'),
                          ('Hernquist10000_G0.8_2_000_bin10_VDFt.txt',
                           'Hernquist10000_G0.8_2_000_bin10_VDFt'),
                          ('Hernquist10000_G1.2_3_005_bin13_VDFr.txt',
                           'Hernquist10000_G1.2_3_005_bin13_VDFr'),
                          ('Hernquist10000_G1.2_3_005_bin13_VDFt.txt',
                           'Hernquist10000_G1.2_3_005_bin13_VDFt'),
                          ('Hernquist10000_G1.2_9_005_bin10_VDFr.txt',
                           'Hernquist10000_G1.2_9_005_bin10_VDFr'),
                          ('Hernquist10000_G1.2_9_005_bin10_VDFt.txt',
                           'Hernquist10000_G1.2_9_005_bin10_VDFt.txt')]

datalist_innerbin = [(pylab.loadtxt(f), l) for f, l in list_of_files_innerbin]
datalist_middlebin = [(pylab.loadtxt(f), l) for f, l in list_of_files_middlebin]
datalist_outerbin = [(pylab.loadtxt(f), l) for f, l in list_of_files_outerbin]

#innerbin
plt.figure(1)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_innerbin[0]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_innerbin[1]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_innerbin[0]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black', label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G0.8_2_000')
ax3.grid()

data, label = datalist_innerbin[1]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black', label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 3, $\gamma = -0.5$')
ax4.grid()


plt.figure(2)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_innerbin[2]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_innerbin[3]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_innerbin[2]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black', label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G1.2_3_005')
ax3.grid()

data, label = datalist_innerbin[3]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black', label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 4, $\gamma = -0.5$')
ax4.grid()


plt.figure(3)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_innerbin[4]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_innerbin[5]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_innerbin[4]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black', label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G1.2_9_005')
ax3.grid()

data, label = datalist_innerbin[5]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black', label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 5, $\gamma = -0.5$')
ax4.grid()

#middlebin
plt.figure(4)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_middlebin[0]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue',
    label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_middlebin[1]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue',
    label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_middlebin[0]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G0.8_2_000')
ax3.grid()

data, label = datalist_middlebin[1]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 6, $\gamma = -1.5$')
ax4.grid()


plt.figure(5)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_middlebin[2]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_middlebin[3]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue',
    label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_middlebin[2]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G1.2_3_005')
ax3.grid()

data, label = datalist_middlebin[3]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]), color = 'Black',
    label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 10, $\gamma = -2.5$')
ax4.grid()


plt.figure(6)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_middlebin[4]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue',
    label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_middlebin[5]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue',
    label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_middlebin[4]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G1.2_9_005')
ax3.grid()

data, label = datalist_middlebin[5]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 6, $\gamma = -1$')
ax4.grid()


#outerbin
plt.figure(7)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_outerbin[0]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_outerbin[1]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_outerbin[0]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G0.8_2_000')
ax3.grid()

data, label = datalist_outerbin[1]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 10, $\gamma = -2.5$')
ax4.grid()


plt.figure(8)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_outerbin[2]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_outerbin[3]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_outerbin[2]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G1.2_3_005')
ax3.grid()

data, label = datalist_outerbin[3]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 13, $\gamma = -3$')
ax4.grid()


plt.figure(9)
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
data, label = datalist_outerbin[4]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax1.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax1.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax1.set_title(r'f($v_r$)')
ax1.grid()

data, label = datalist_outerbin[5]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax2.plot(data[:,0], data[:,1],color = 'Blue', label=label,lw=2,ms=7 )
ax2.plot(data[:,0],y_fit,'--',lw=3,color='red')
ax2.set_title(r'f($v_t$)')
ax2.grid()

data, label = datalist_outerbin[4]
popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
y_fit = func_2(data[:,0],popt[0],popt[1],popt[2])
ax3.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax3.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax3.set_title('Hernquist10000_G1.2_9_005')
ax3.grid()

data, label = datalist_outerbin[5]
popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
y_fit = func_1(data[:,0],popt[0],popt[1],popt[2])
ax4.plot(data[:,0], np.log10(data[:,1]),color = 'Black',
    label=label,lw=2,ms=7 )
ax4.plot(data[:,0],np.log10(y_fit),'--',lw=3,color='green')
ax4.set_title(r'bin 10, $\gamma = -2.5$')
ax4.grid()

plt.show()
