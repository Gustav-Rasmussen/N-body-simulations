# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pylab
from scipy.optimize import curve_fit

import RhoAndGaussianAndTsallis as ragat

Lst1 = ['HQ10000_G0.8_2_000_bin3_VDFr', 'HQ10000_G0.8_2_000_bin3_VDFt',
        'HQ10000_G1.2_3_005_bin4_VDFr', 'HQ10000_G1.2_3_005_bin4_VDFt',
        'HQ10000_G1.2_9_005_bin5_VDFr', 'HQ10000_G1.2_9_005_bin5_VDFt']

FileLstbin1 = [(Lst1[0] + '.txt', Lst1[0]), (Lst1[1] + '.txt', Lst1[1]),
               (Lst1[2] + '.txt', Lst1[2]), (Lst1[3] + '.txt', Lst1[3]),
               (Lst1[4] + '.txt', Lst1[4]), (Lst1[5] + '.txt', Lst1[5])]

Lst2 = ['HQ10000_G0.8_2_000_bin6_VDFr', 'HQ10000_G0.8_2_000_bin6_VDFt',
        'HQ10000_G1.2_3_005_bin10_VDFr', 'HQ10000_G1.2_3_005_bin10_VDFt',
        'HQ10000_G1.2_9_005_bin6_VDFr', 'HQ10000_G1.2_9_005_bin6_VDFt']

FileLstbin2 = [(Lst2[0] + '.txt', Lst2[0]), (Lst2[1] + '.txt', Lst2[1]),
               (Lst2[2] + '.txt', Lst2[2]), (Lst2[3] + '.txt', Lst2[3]),
               (Lst2[4] + '.txt', Lst2[4]), (Lst2[5] + '.txt', Lst2[5])]

Lst3 = ['HQ10000_G0.8_2_000_bin10_VDFr', 'HQ10000_G0.8_2_000_bin10_VDFt',
        'HQ10000_G1.2_3_005_bin13_VDFr', 'HQ10000_G1.2_3_005_bin13_VDFt',
        'HQ10000_G1.2_9_005_bin10_VDFr', 'HQ10000_G1.2_9_005_bin10_VDFt']

FileLstbin3 = [(Lst3[0] + '.txt', Lst3[0]), (Lst3[1] + '.txt', Lst3[1]),
               (Lst3[2] + '.txt', Lst3[2]), (Lst3[3] + '.txt', Lst3[3]),
               (Lst3[4] + '.txt', Lst3[4]), (Lst3[5] + '.txt', Lst3[5])]

bin1 = [(pylab.loadtxt(f), l) for f, l in FileLstbin1]
bin2 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2]
bin3 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3]


def plot_binData_with_fit(figNum, binIndex1, binIndex2, title3, binNum, Gamma,
                          Bin):
    plt.figure(figNum)
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,
                                               sharex='col', sharey='row')

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    data, label = Bin[binIndex1]
    popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
    ax1.plot(data[:, 0], data[:, 1], 'b', label=label, lw=2, ms=7)
    ax1.plot(data[:, 0], y_fit, 'r--', lw=3)
    ax1.set_title(r'f($v_r$)')

    data, label = Bin[binIndex2]
    popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
    ax2.plot(data[:, 0], data[:, 1], 'b', label=label, lw=2, ms=7)
    ax2.plot(data[:, 0], y_fit, 'r--', lw=3)
    ax2.set_title(r'f($v_t$)')

    data, label = Bin[binIndex1]
    popt, pcov = curve_fit(ragat.func_2_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_2_add(data[:, 0], popt[0], popt[1], popt[2])
    ax3.plot(data[:, 0], np.log10(data[:, 1]), 'k',
             label=label, lw=2, ms=7)
    ax3.plot(data[:, 0], np.log10(y_fit), 'g--', lw=3)
    ax3.set_title(f'HQ10000_G{title3}')

    data, label = Bin[binIndex2]
    popt, pcov = curve_fit(ragat.func_1_add, data[:, 0], data[:, 1])
    y_fit = ragat.func_1_add(data[:, 0], popt[0], popt[1], popt[2])
    ax4.plot(data[:, 0], np.log10(data[:, 1]), 'k',
             label=label, lw=2, ms=7)
    ax4.plot(data[:, 0], np.log10(y_fit), 'g--', lw=3)
    ax4.set_title(r'bin {0}, $\gamma = {1}$'.format(binNum, Gamma))
    # return


def main():
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


if __name__ == '__main__':
    main()
