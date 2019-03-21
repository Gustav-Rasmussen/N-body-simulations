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


def plot_binData_with_fit(figNum, binIndex1, binIndex2, title3, binNum, Gamma,
                          Bin):
    plt.figure(figNum)
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,
                                               sharex='col', sharey='row')
    data, label = Bin[binIndex1]
    popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
    ax1.plot(data[:, 0], data[:, 1], 'b', label=label, lw=2, ms=7)
    ax1.plot(data[:, 0], y_fit, 'r--', lw=3)
    ax1.set_title(r'f($v_r$)')
    ax1.grid()

    data, label = Bin[binIndex2]
    popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
    ax2.plot(data[:, 0], data[:, 1], 'b', label=label, lw=2, ms=7)
    ax2.plot(data[:, 0], y_fit, 'r--', lw=3)
    ax2.set_title(r'f($v_t$)')
    ax2.grid()

    data, label = Bin[binIndex1]
    popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
    ax3.plot(data[:, 0], np.log10(data[:, 1]), 'k',
             label=label, lw=2, ms=7)
    ax3.plot(data[:, 0], np.log10(y_fit), 'g--', lw=3)
    ax3.set_title(f'HQ10000_G{title3}')
    ax3.grid()

    data, label = Bin[binIndex2]
    popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
    ax4.plot(data[:, 0], np.log10(data[:, 1]), 'k',
             label=label, lw=2, ms=7)
    ax4.plot(data[:, 0], np.log10(y_fit), 'g--', lw=3)
    ax4.set_title(r'bin {0}, $\gamma = {1}$'.format(binNum, Gamma))
    ax4.grid()
    # return


# innerbin
plot_binData_with_fit(1, 0, 1, '0.8_2_000', 3, -0.5, bin1)
plot_binData_with_fit(2, 2, 3, '1.2_3_005', 4, -0.5, bin1)
plot_binData_with_fit(3, 4, 5, '1.2_9_005', 5, -0.5, bin1)

# middlebin
plot_binData_with_fit(4, 0, 1, '0.8_2_000', 6, -1.5, bin2)
plot_binData_with_fit(5, 2, 3, '1.2_3_005', 10, -2.5, bin2)
plot_binData_with_fit(6, 4, 5, '1.2_9_005', 6, -1, bin2)

# outerbin
plot_binData_with_fit(7, 0, 1, '0.8_2_000', 10, -2.5, bin3)
plot_binData_with_fit(8, 2, 3, '1.2_3_005', 13, -3, bin3)
plot_binData_with_fit(9, 4, 5, '1.2_9_005', 10, -2.5, bin3)

plt.show()
