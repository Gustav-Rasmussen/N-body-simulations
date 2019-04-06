#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 21:36:43 2018
@author: gustavcollinrasmussen
"""

import pylab
import readVDF2FileLst as fls

# import snapshotFiles
# from definePaths import *
# from pathlib import Path
# from terminal_code import *

# print(Path.cwd())

# Switches --------------------------------------------------------------------
Gamma_on = 1
Beta_on = 0

Fig_vRvPhivTheta = 0
Fig_vr_vPhi_vTheta_with_fit = 0
Fig_vt = 0
Fig_vT_with_fit = 0

vRvPhivThetaDividedByGauss = 0
vTdividedByGauss = 0
GpertSameGammasAsICvR = 0
GpertDifferentGammasvT = 0
GpertGammas_1_5_vTdividedByGaussAndTsallis = 0
GpertGammas_2_0_vTdividedByGaussAndTsallis = 0
GpertGammas_2_5_vTdividedByGaussAndTsallis = 0
GpertGammas_3_0_vTdividedByGaussAndTsallis = 0
GpertRmiddle_19_95_vTdividedByGaussAndTsallis = 0
GpertRmiddle_31_62_vTdividedByGaussAndTsallis = 0

# fls.Bin1differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l)
#                                              for f, l in bins3A[0]]

"""
def plot_test():
    return fls.Bin1differentGammasTest2HQ10000_G1_0_0_000
    # f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,
    #                                            sharex='col', sharey='row')
    # data, _ = fls.Bin1differentGammasTest2HQ10000_G1_0_0_000[0]
    # ax1.plot(data[:, 0], data[:, 1],\
    #          '{colours[fileNum]}--', lw=2, ms=7)")
# plot_test()
"""


def Plt(i, data, cls, Label=False):
    if Label:
        return eval(
            f"ax{i}.plot({data}[0][:, 0], {data}[0][:, 1], {cls}, label={Label}, lw=2, ms=7)"
        )
    return eval(
        f"ax{i}.plot({data}[0][:, 0],\
                  {data}[0][:, 1], {cls}, lw=2, ms=7)"
    )


def plot_binData(fileLst):
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
        2, 2, sharex="col", sharey="row"
    )
    for axNum in range(1, 5):
        for binNum in range(1, 5):
            for fileNum in range(1, 4):
                exec(f"data, _ = fls.Bin{binNum}{fileLst}[{fileNum}]")
                exec(
                    f"ax{axNum}.plot(data[:, 0], data[:, 1],\
                     {colours[fileNum - 1]}, ls='--', lw=2, ms=7)"
                )
        exec(f"ax{axNum}.grid()")

    ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
    ax1.set_title(r"File = %s" % HQ12, fontsize=20)

    ax2.set_ylabel(
        r"$f\left(\log\left(|u_n|, u_p \right)\right)$", fontsize=20
    )

    ax1_labels = [r"$v_r$", r"$v_{\Theta}$", r"$v_{\Phi}$"]
    ax2_labels = [
        r"$\gamma = -1.5$",
        r"$\gamma = -2.0$",
        r"$\gamma = -2.5$",
        r"$\gamma = -3.0 $",
    ]

    for i in range(len(ax1_labels)):
        ax1.plot([], [], label=ax1_labels[i], ls="--", lw=2, ms=7)

    for i in range(len(ax2_labels)):
        ax2.plot([], [], label=ax2_labels[i], ls="--", lw=2, ms=7)

    for binNum in range(1, 3):
        exec(
            f"ax{binNum}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
             frameon=True, loc=0, handlelength=2.5"
        )

    ax3.set_xlabel(r"$u_r$, $u_{\Theta}$ and $u_{\Phi}$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f(u) \right)$", fontsize=20)

    ax4.set_xlabel(
        r"$\log \left( |u_rn|,u_rp \right)$, $\log\
                   \left( |u_{\Theta}n|,u_{\Theta}p \right)$ and\
                   $\log \left( |u_{\Phi}n|,u_{\Phi}p \right)$",
        fontsize=20,
    )
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,\
                   u_p \right)\right) \right)$",
        fontsize=20,
    )

    ax3.set_yscale("log")
    ax4.set_yscale("log")


colours = ["g", "r", "k"]
if Fig_vRvPhivTheta:
    if test:
        plot_binData("HQ10000_G1_2_1_005")
    if test2:
        plot_binData("different_gammas_test2_HQ10000_G1_0_0_000")

if Fig_vr_vPhi_vTheta_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(
                f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)"
            )

        data, _ = bin2_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f$"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "Pink",
            ".-",
            lw=3,
            label=r"$ \Theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "Brown",
            ".-",
            lw=3,
            label=r"$ \Phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r"Fits to file = %s, $\gamma = -2.0$" % HQ12, fontsize=20
        )

        data, _ = bin2_HQ10000_G1_2_1_005[5]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"$ \frac{v_r}{\sigma_r} $",
            lw=2,
            ms=7,
        )
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$radial: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f$"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_HQ10000_G1_2_1_005[6]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"$ \frac{v_{\Theta}}{\sigma_{\Theta}} $",
            lw=2,
            ms=7,
        )
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "Pink",
            ".-",
            lw=3,
            label=r"$\Theta: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f$"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_HQ10000_G1_2_1_005[7]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"$ \frac{v_{\Phi}}{\sigma_{\Phi}} $",
            lw=2,
            ms=7,
        )
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "Brown",
            ".-",
            lw=3,
            label=r"$ \Phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        data, _ = bin2_HQ10000_G1_2_1_005[1]
        ax3.plot(
            data[:, 0], data[:, 1], "g", label=r"$\gamma = -2.0$", lw=4, ms=7
        )
        data, _ = bin2_HQ10000_G1_2_1_005[2]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=4, ms=7)
        data, _ = bin2_HQ10000_G1_2_1_005[3]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax3.set_xlabel(r"$ u_r $, $u_{\Theta}$ and $u_{\Phi}$", fontsize=20)
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin2_HQ10000_G1_2_1_005[5]
        ax4.plot(
            data[:, 0], data[:, 1], "g", label=r"$\gamma = -2.0 $", lw=2, ms=7
        )
        data, _ = bin2_HQ10000_G1_2_1_005[6]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_HQ10000_G1_2_1_005[7]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax4.set_xlabel(
            r"$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\Theta}n|,\
                       u_{\Theta}p \right)$ and $\log \left( |u_{\Phi}n|,u_{\Phi}p \right)$",
            fontsize=20,
        )
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

    if test2:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "Pink",
            ".-",
            lw=3,
            label=r"$\Theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f$"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "Brown",
            ".-",
            lw=3,
            label=r"$ \Phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r"Fits to file = %s, $\gamma = -2.0 $" % test2_HQ0, fontsize=20
        )
        ax1.legend(
            prop=dict(size=13),
            numpoints=2,
            ncol=1,
            frameon=True,
            loc=0,
            handlelength=2.5,
        )

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"$ \frac{v_r}{\sigma_r} $",
            lw=2,
            ms=7,
        )
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$radial: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"$ \frac{v_{\Theta}}{\sigma_{\Theta}} $",
            lw=2,
            ms=7,
        )
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "Pink",
            ".-",
            lw=3,
            label=r"$ \Theta: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"$ \frac{v_{\Phi}}{\sigma_{\Phi}} $",
            lw=2,
            ms=7,
        )
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "Brown",
            ".-",
            lw=3,
            label=r"$ \Phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )
        ax2.legend(
            prop=dict(size=13),
            numpoints=2,
            ncol=1,
            frameon=True,
            loc=0,
            handlelength=2.5,
        )

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(
            data[:, 0], data[:, 1], "g", label=r"$\gamma = -2.0 $", lw=4, ms=7
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=4, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax3.set_xlabel(r"$ u_r $, $u_{\Theta}$ and $u_{\Phi}$", fontsize=20)
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(
            data[:, 0], data[:, 1], "g", label=r"$\gamma = -2.0$", lw=2, ms=7
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax4.set_xlabel(
            r"$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left( |u_{\Phi}n|,u_{\Phi}p \right)$",
            fontsize=20,
        )
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

if Fig_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        Plt(
            1,
            bin1_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b--",
            r"$\gamma = -1.5$",
        )
        Plt(1, bin2_HQ10000_G1_2_1_005[0], "b:", r"$\gamma = -2.0$")
        Plt(1, bin3_HQ10000_G1_2_1_005[0], "b-.", r"$\gamma = -2.5$")
        Plt(1, bin4_HQ10000_G1_2_1_005[0], "b", r"$\gamma = -3.0$")

        ax1.set_ylabel(r"$f\left(u_t \right)$", fontsize=20)
        ax1.set_title(r" File = %s" % HQ12, fontsize=20)
        ax1.legend(
            prop=dict(size=13),
            numpoints=2,
            ncol=1,
            frameon=True,
            loc=0,
            handlelength=2.5,
        )

        Plt(2, bin1_HQ10000_G1_2_1_005[4], "b--", r"$\gamma = -1.5$")
        Plt(2, bin2_HQ10000_G1_2_1_005[4], "b:", r"$\gamma = -2.0$")
        Plt(2, bin3_HQ10000_G1_2_1_005[4], "b-.", r"$\gamma = -2.5$")
        Plt(2, bin4_HQ10000_G1_2_1_005[4], "b", r"$\gamma = -3.0$")

        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        Plt(3, bin1_HQ10000_G1_2_1_005[0], "b--", r"$\gamma = -1.5$")
        Plt(3, bin2_HQ10000_G1_2_1_005[0], "b:", r"$\gamma = -2.0$")
        Plt(3, bin3_HQ10000_G1_2_1_005[0], "b-.", r"$\gamma = -2.5$")
        Plt(3, bin4_HQ10000_G1_2_1_005[0], "b", r"$\gamma = -3.0$")

        ax3.set_xlabel(r"$ u_t $", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left(u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        Plt(4, bin1_HQ10000_G1_2_1_005[4], "b--", r"$\gamma = -1.5$")
        Plt(4, bin2_HQ10000_G1_2_1_005[4], "b:", r"$\gamma = -2.0$")
        Plt(4, bin3_HQ10000_G1_2_1_005[4], "b-.", r"$\gamma = -2.5$")
        Plt(4, bin4_HQ10000_G1_2_1_005[4], "b", r"$\gamma = -3.0$")

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left(\
                       |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

    if test2:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        Plt(
            1,
            bin1_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b--",
            r"$\gamma = -1.5$",
        )
        Plt(
            1,
            bin2_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b:",
            r"$\gamma = -2.0$",
        )
        Plt(
            1,
            bin3_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b-.",
            r"$\gamma = -2.5$",
        )
        Plt(
            1,
            bin4_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b",
            r"$\gamma = -3.0$",
        )

        ax1.set_ylabel(r"$f\left(u_t \right)$", fontsize=20)
        ax1.set_title(r"File = %s" % test2_HQ0, fontsize=20)
        ax1.legend(
            prop=dict(size=13),
            numpoints=2,
            ncol=1,
            frameon=True,
            loc=0,
            handlelength=2.5,
        )

        Plt(
            2,
            bin1_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b--",
            r"$\gamma = -1.5$",
        )
        Plt(
            2,
            bin2_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b:",
            r"$\gamma = -2.0$",
        )
        Plt(
            2,
            bin3_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b-.",
            r"$\gamma = -2.5$",
        )
        Plt(
            2,
            bin4_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b",
            r"$\gamma = -3.0$",
        )

        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        Plt(
            3,
            bin1_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b--",
            r"$\gamma = -1.5$",
        )
        Plt(
            3,
            bin2_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b:",
            r"$\gamma = -2.0$",
        )
        Plt(
            3,
            bin3_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b-.",
            r"$\gamma = -2.5$",
        )
        Plt(
            3,
            bin4_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b",
            r"$\gamma = -3.0$",
        )

        ax3.set_xlabel(r"$ u_t $", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left(u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        Plt(
            4,
            bin1_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b--",
            r"$\gamma = -1.5$",
        )
        Plt(
            4,
            bin2_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b:",
            r"$\gamma = -2.0$",
        )
        Plt(
            4,
            bin3_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b-.",
            r"$\gamma = -2.5$",
        )
        Plt(
            4,
            bin4_different_gammas_test2_HQ10000_G1_0_0_000[4],
            "b",
            r"$\gamma = -3.0$",
        )

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left(\
                       |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

special_fit = 0

if Fig_vT_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(17, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 3):
        exec(
            f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                                  fancybox=True, loc=0, handlelength=2.5)"
        )
        exec(f"leg.get_frame().set_alpha(.5)")

    if test:
        data, _ = bin2_HQ10000_G1_2_1_005[0]
        ax1.plot(
            data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0$", lw=4, ms=7
        )
        popt, pcov = curve_fit(func_1, data[:, 0], data[:, 1])
        y_fit = func_1(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, "c.-", lw=3,
            label=r"$axe^{-bx^2}$, $ a,b = %.3f,%.3f $" % (popt[0], popt[1]))
        popt, pcov = curve_fit(func_6, data[:, 0], data[:, 1])
        y_fit = func_6(data[:, 0], popt[0], popt[1], popt[2])
        ax1.plot(data[:, 0], y_fit, "g:", lw=3,
            label=r"$ax(1- (1 - q)bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
            % (popt[0], popt[1], popt[2]))
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Fit to VDF, File = %s" % HQ12, fontsize=20)

        data, _ = bin2_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0 $", lw=2, ms=7
        )
        popt, pcov = curve_fit(func_3_log, data[:, 0], data[:, 1])
        y_fit = func_3_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, "c.-", lw=3,
            label=r"$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f$"
            % (popt[0], popt[1]))
        popt, pcov = curve_fit(func_7_log, data[:, 0], data[:, 1])
        y_fit = func_7_log(data[:, 0], popt[0], popt[1], popt[2])
        ax2.plot(
            data[:, 0],
            y_fit,
            "g:",
            lw=3,
            label=r"$a\cdot \log(x)^2(1- (1 - q)b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
            % (popt[0], popt[1], popt[2]),
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        Plt(3, bin1_HQ10000_G1_2_1_005[0], "b--", r"$\gamma = -1.5$")
        Plt(3, bin2_HQ10000_G1_2_1_005[0], "b:", r"$\gamma = -2.0$")
        Plt(3, bin3_HQ10000_G1_2_1_005[0], "b-.", r"$\gamma = -2.5$")
        Plt(3, bin4_HQ10000_G1_2_1_005[0], "b", r"$\gamma = -3.0$")

        ax3.set_xlabel(r"$ u_t $", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        Plt(4, bin1_HQ10000_G1_2_1_005[4], "b--", r"$\gamma = -1.5$")
        Plt(4, bin2_HQ10000_G1_2_1_005[4], "b:", r"$\gamma = -2.0$")
        Plt(4, bin3_HQ10000_G1_2_1_005[4], "b-.", r"$\gamma = -2.5$")
        Plt(4, bin4_HQ10000_G1_2_1_005[4], "b", r"$\gamma = -3.0$")

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

    if test2:
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0$", lw=4, ms=7
        )
        popt, pcov = curve_fit(func_1, data[:, 0], data[:, 1])
        y_fit = func_1(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$axe^{-bx^2}$, $ a,b = %.3f,%.3f $" % (popt[0], popt[1]),
        )
        popt, pcov = curve_fit(func_6, data[:, 0], data[:, 1])
        y_fit = func_6(data[:, 0], popt[0], popt[1], popt[2])
        ax1.plot(
            data[:, 0],
            y_fit,
            "g:",
            lw=3,
            label=r"$ax(1- (1 - q)bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
            % (popt[0], popt[1], popt[2]),
        )
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Fit to VDF, File = %s" % test2_HQ0, fontsize=20)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0 $", lw=2, ms=7
        )
        popt, pcov = curve_fit(func_3_log, data[:, 0], data[:, 1])
        y_fit = func_3_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        popt, pcov = curve_fit(func_7_log, data[:, 0], data[:, 1])
        y_fit = func_7_log(data[:, 0], popt[0], popt[1], popt[2])
        ax2.plot(
            data[:, 0],
            y_fit,
            "g:",
            lw=3,
            label=r"$a\cdot \log(x)^2(1- (1 - q)b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
            % (popt[0], popt[1], popt[2]),
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "b--",
            r"$\gamma = -1.5$")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_0_000[0], "b:",
            r"$\gamma = -2.0$")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_0_000[0], "b-.",
            r"$\gamma = -2.5$")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_0_000[0], "b",
            r"$\gamma = -3.0$")

        ax3.set_xlabel(r"$u_t$", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "b--",
            r"$\gamma = -1.5$")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_0_000[4], "b:",
            r"$\gamma = -2.0$")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_0_000[4], "b-.",
            r"$\gamma = -2.5$")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_0_000[4], "b",
            r"$\gamma = -3.0$")

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

    if A:
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(
            data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0 $", lw=4, ms=7
        )
        popt, pcov = curve_fit(func_1, data[:, 0], data[:, 1])
        y_fit = func_1(data[:, 0], popt[0], popt[1])
        ax1.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$axe^{-bx^2}$, $ a,b = %.3f,%.3f $" % (popt[0], popt[1]),
        )
        popt, pcov = curve_fit(func_6, data[:, 0], data[:, 1])
        y_fit = func_6(data[:, 0], popt[0], popt[1], popt[2])
        ax1.plot(
            data[:, 0],
            y_fit,
            "g:",
            lw=3,
            label=r"$ax(1- (1 - q)bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
            % (popt[0], popt[1], popt[2]),
        )
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Fit to %s" % A_HQ0, fontsize=20)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0 $", lw=2, ms=7
        )
        popt, pcov = curve_fit(func_3_log, data[:, 0], data[:, 1])
        y_fit = func_3_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        popt, pcov = curve_fit(func_7_log, data[:, 0], data[:, 1])
        y_fit = func_7_log(data[:, 0], popt[0], popt[1], popt[2])
        ax2.plot(
            data[:, 0],
            y_fit,
            "g:",
            lw=3,
            label=r"$a\cdot \log(x)^2(1- (1 - q)b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
            % (popt[0], popt[1], popt[2])
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_0_000[0], "b--",
            r"$\gamma = -1.5$")
        Plt(3, bin2_different_gammas_A_HQ10000_G1_0_0_000[0], "b:",
            r"$\gamma = -2.0$")
        Plt(3, bin3_different_gammas_A_HQ10000_G1_0_0_000[0], "b-.",
            r"$\gamma = -2.5$")
        Plt(3, bin4_different_gammas_A_HQ10000_G1_0_0_000[0], "b",
            r"$\gamma = -3.0$")

        ax3.set_xlabel(r"$ u_t $", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_0_000[4], "b--",
            r"$\gamma = -1.5$")
        Plt(4, bin2_different_gammas_A_HQ10000_G1_0_0_000[4], "b:",
            r"$\gamma = -2.0$")
        Plt(4, bin3_different_gammas_A_HQ10000_G1_0_0_000[4], "b-.",
            r"$\gamma = -2.5$")
        Plt(4, bin4_different_gammas_A_HQ10000_G1_0_0_000[4], "b",
            r"$\gamma = -3.0$")

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

    if B:
        if special_fit:
            data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
            ax1.plot(
                data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0 $", lw=4, ms=7
            )
            popt, pcov = curve_fit(func_3, data[:, 0], data[:, 1])
            y_fit = func_3(data[:, 0], popt[0], popt[1])
            ax1.plot(data[:, 0], y_fit, "c.-", lw=3,
                     label=r"$axe^{-bx^2}$, $ a,b = %.3f,%.3f $" % (popt[0],
                                                                    popt[1]))
            popt, pcov = curve_fit(func_4, data[:, 0], data[:, 1])
            y_fit = func_4(data[:, 0], popt[0], popt[1], popt[2])
            ax1.plot(data[:, 0], y_fit, "g:", lw=3,
                     label=r"$ax(1- (1 - q)bx^2)^{(\frac{q}{1-q})}$,\
                           $ a,b,q = %.3f,%.3f,%.3f $"
                           % (popt[0], popt[1], popt[2]))
            ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=26)
            ax1.set_title(r"Fit to %s" % B_HQ0, fontsize=20)

        else:
            data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
            ax1.plot(
                data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0 $", lw=4, ms=7)
            popt, pcov = curve_fit(func_1, data[:, 0], data[:, 1])
            y_fit = func_1(data[:, 0], popt[0], popt[1])
            ax1.plot(data[:, 0], y_fit, "c.-", lw=3,
                label=r"$axe^{-bx^2}$, $ a,b = %.3f,%.3f $"
                      % (popt[0], popt[1]))
            popt, pcov = curve_fit(func_6, data[:, 0], data[:, 1])
            y_fit = func_6(data[:, 0], popt[0], popt[1], popt[2])
            ax1.plot(
                data[:, 0],
                y_fit,
                "g:",
                lw=3,
                label=r"$ax(1- (1 - q)bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
                % (popt[0], popt[1], popt[2]),
            )
            ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
            ax1.set_title(r"Fit to %s" % B_HQ0, fontsize=20)
            ax1.axes.get_xaxis().set_visible(False)
            ax1.set_xlim(0.0, 3.0)
            ax1.set_ylim(0.0, 450.0)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0], data[:, 1], "b:", label=r"$\gamma = -2.0$", lw=2, ms=7
        )
        popt, pcov = curve_fit(func_3_log, data[:, 0], data[:, 1])
        y_fit = func_3_log(data[:, 0], popt[0], popt[1])
        ax2.plot(
            data[:, 0],
            y_fit,
            "c.-",
            lw=3,
            label=r"$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $"
            % (popt[0], popt[1]),
        )
        popt, pcov = curve_fit(func_7_log, data[:, 0], data[:, 1])
        y_fit = func_7_log(data[:, 0], popt[0], popt[1], popt[2])
        ax2.plot(
            data[:, 0],
            y_fit,
            "g:",
            lw=3,
            label=r"$a\cdot \log(x)^2(1- (1 - q)b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $"
            % (popt[0], popt[1], popt[2]),
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )
        ax2.yaxis.tick_right()
        ax2.tick_params(
            axis="both",
            which="both",
            bottom="off",
            top="off",
            labelbottom="off",
            right="on",
            left="off",
            labelleft="off",
        )
        ax2.yaxis.set_label_position("right")
        ax2.set_xlim(-3.0, 1.0)
        ax2.set_ylim(0.0, 1500.0)

        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_0_000[0], "b--",
            r"$\gamma = -1.5$")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_0_000[0], "b:",
            r"$\gamma = -2.0$")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_0_000[0], "b-.",
            r"$\gamma = -2.5$")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_0_000[0], "b",
            r"$\gamma = -3.0$")

        ax3.set_xlabel(r"$u_t$", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")
        ax3.set_xlim(0.0, 3.0)
        ax3.set_ylim(10 ** 0.0, 10 ** 3.0)

        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_0_000[4], "b--",
            r"$\gamma = -1.5$")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_0_000[4], "b:",
            r"$\gamma = -2.0$")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_0_000[4], "b-.",
            r"$\gamma = -2.5$")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_0_000[4], "b",
            r"$\gamma = -3.0$")

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")
        ax4.yaxis.tick_right()
        ax4.tick_params(
            axis="both",
            which="both",
            bottom="on",
            top="off",
            labelbottom="on",
            right="on",
            left="off",
            labelleft="off",
        )
        ax4.yaxis.set_label_position("right")
        ax4.set_xlim(-3.0, 1.0)
        ax4.set_ylim(10 ** 0.0, 2 * 10 ** 3.0)
        f.savefig("vt_fit_show_abq.png")

if Fig_vr_vPhi_vTheta_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)

    ax1.grid()
    ax2.grid()

    for i in range(1, 3):
        exec(f"legend(
                      prop=dict(size=13),
                      numpoints=2,
                      ncol=1,
                      frameon=True,
                      loc=0,
                      handlelength=2.5)")

    if test:
        data, _ = bin2_HQ10000_G1_2_1_005[1]
        ax1.plot(
            data[:, 0],
            data[:, 1] / (478.006 * np.exp(-0.456 * data[:, 0] ** 2)),
            "g:",
            label=r"$r, a=478.006, b=0.456$",
            lw=4,
            ms=7,
        )
        data, _ = bin2_HQ10000_G1_2_1_005[2]
        ax1.plot(
            data[:, 0],
            data[:, 1] / (482.605 * np.exp(-0.473 * data[:, 0] ** 2)),
            "r:",
            label=r"$\Theta, a=482.605, b=0.473$",
            lw=4,
            ms=7,
        )
        data, _ = bin2_HQ10000_G1_2_1_005[3]
        ax1.plot(
            data[:, 0],
            data[:, 1] / (502.652 * np.exp(-0.477 * data[:, 0] ** 2)),
            "k:",
            label=r"$\Phi, a=502.652, b=0.477$",
            lw=2,
            ms=7,
        )
        ax1.set_xlabel(
            r"$ u_r $, $ u_{\Theta} $ and $ u_{\Phi} $", fontsize=20
        )
        ax1.set_ylabel(r"$\frac{f\left(u \right)}{ae^{-bx^2}}$", fontsize=20)
        ax1.set_title(r" File = %s, $\gamma = -2.0 $" % HQ12, fontsize=20)

        data, _ = bin2_HQ10000_G1_2_1_005[5]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                1433.228
                * 10 ** data[:, 0]
                * np.exp(-0.472 * (10 ** data[:, 0]) ** 2)
            ),
            "g:",
            label=r"$a=1433.228, b=0.472$",
            lw=2,
            ms=7,
        )
        data, _ = bin2_HQ10000_G1_2_1_005[6]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                1416.346
                * 10 ** data[:, 0]
                * np.exp(-0.473 * (10 ** data[:, 0]) ** 2)
            ),
            "r:",
            label=r"$ a=1416.346, b=0.473 $",
            lw=2,
            ms=7,
        )
        data, _ = bin2_HQ10000_G1_2_1_005[7]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                1405.914
                * 10 ** data[:, 0]
                * np.exp(-0.470 * (10 ** data[:, 0]) ** 2)
            ),
            "k:",
            label=r"$ a=1405.914, b=0.470$",
            lw=2,
            ms=7,
        )
        ax2.set_xlabel(
            r"$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left( |u_{\Phi}n|,u_{\Phi}p \right)$",
            fontsize=20,
        )
        ax2.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{axe^{-b\log (x)^2}}$",
            fontsize=20,
        )  # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}

    if test2:
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(
            data[:, 0],
            data[:, 1] / (478.006 * np.exp(-0.456 * data[:, 0] ** 2)),
            "g:",
            label=r"$r, a=478.006, b=0.456$",
            lw=4,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(
            data[:, 0],
            data[:, 1] / (482.605 * np.exp(-0.473 * data[:, 0] ** 2)),
            "r:",
            label=r"$\Theta, a=482.605, b=0.473$",
            lw=4,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(
            data[:, 0],
            data[:, 1] / (502.652 * np.exp(-0.477 * data[:, 0] ** 2)),
            "k:",
            label=r"$\Phi, a=502.652, b=0.477$",
            lw=2,
            ms=7,
        )
        ax1.set_xlabel(
            r"$ u_r $, $ u_{\Theta} $ and $ u_{\Phi} $", fontsize=20
        )
        ax1.set_ylabel(r"$\frac{f\left(u \right)}{ae^{-bx^2}}$", fontsize=20)
        ax1.set_title(r" File = %s, $\gamma = -2.0$" % test2_HQ0, fontsize=20)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                1433.228
                * 10 ** data[:, 0]
                * np.exp(-0.472 * (10 ** data[:, 0]) ** 2)
            ),
            "g:",
            label=r"$a=1433.228, b=0.472$",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                1416.346
                * 10 ** data[:, 0]
                * np.exp(-0.473 * (10 ** data[:, 0]) ** 2)
            ),
            "r:",
            label=r"$ a=1416.346, b=0.473 $",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                1405.914
                * 10 ** data[:, 0]
                * np.exp(-0.470 * (10 ** data[:, 0]) ** 2)
            ),
            "k:",
            label=r"$ a=1405.914, b=0.470$",
            lw=2,
            ms=7,
        )
        ax2.set_xlabel(
            r"$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left( |u_{\Phi}n|,u_{\Phi}p \right)$",
            fontsize=20,
        )
        ax2.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{axe^{-b\log (x)^2}}$",
            fontsize=20,
        )

if Fig_vt_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)

    ax1.grid()
    ax2.grid()

    ax1.legend(
        prop=dict(size=13),
        numpoints=2,
        ncol=1,
        frameon=True,
        loc=0,
        handlelength=2.5,
    )

    if test:
        data, _ = bin1_HQ10000_G1_2_1_005[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b--",
            label=r"$ \gamma = -1.5 $",
            lw=3,
        )
        data, _ = bin2_HQ10000_G1_2_1_005[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b:",
            label=r"$ \gamma = -2.0$",
            lw=4,
            ms=7,
        )
        data, _ = bin3_HQ10000_G1_2_1_005[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b-.",
            label=r"$ \gamma = -2.5$",
            lw=4,
            ms=7,
        )
        data, _ = bin4_HQ10000_G1_2_1_005[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            label=r"$ \gamma = -3.0$",
            lw=2,
            ms=7,
        )
        ax1.set_ylim(0, 2)
        ax1.set_xlabel(r"$u_t$", fontsize=20)
        ax1.set_ylabel(
            r"$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$", fontsize=20
        )
        ax1.set_title(r" File = %s" % HQ12, fontsize=20)

        data, _ = bin1_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b--",
            label=r"$ \gamma = -1.5$",
            lw=2,
            ms=7,
        )
        data, _ = bin2_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b:",
            label=r"$ \gamma = -2.0 $",
            lw=2,
            ms=7,
        )
        data, _ = bin3_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b-.",
            label=r"$ \gamma = -2.5 $",
            lw=2,
            ms=7,
        )
        data, _ = bin4_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            label=r"$ \gamma = -3.0$",
            lw=2,
            ms=7,
        )
        ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3400.442x^2e^{-0.930x^2}}$",
            fontsize=20,
        )  # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}

    if test2:
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b--",
            label=r"$ \gamma = -1.5$",
            lw=3,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b:",
            label=r"$ \gamma = -2.0$",
            lw=4,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b-.",
            label=r"$\gamma = -2.5$",
            lw=4,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            data[:, 0],
            data[:, 1]
            / (918.083 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            label=r"$ \gamma = -3.0$",
            lw=2,
            ms=7,
        )
        ax1.set_ylim(0, 2)
        ax1.set_xlabel(r"$ u_t $", fontsize=20)
        ax1.set_ylabel(
            r"$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$", fontsize=20
        )
        ax1.set_title(r" File = %s" % test2_HQ0, fontsize=20)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b--",
            label=r"$ \gamma = -1.5$",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b:",
            label=r"$ \gamma = -2.0$",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b-.",
            label=r"$ \gamma = -2.5$",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1]
            / (
                3400.442
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            label=r"$ \gamma = -3.0$",
            lw=2,
            ms=7,
        )
        ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3400.442x^2e^{-0.930x^2}}$",
            fontsize=20,
        )

if Fig3_vr_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(f"ax{i}.legend(
                            prop=dict(size=18),
                            numpoints=2,
                            ncol=1,
                            frameon=True,
                            loc=0,
                            handlelength=2.5)")

    Plt(1, bin1_HQ10000_G1_0_0_000[0], "b--",
        r"$\gamma = -1.5$")
    Plt(1, bin1_HQ10000_G1_0_0_000[1], "g--")
    Plt(1, bin2_HQ10000_G1_0_0_000[0], "b:",
        r"$\gamma = -2.0$")
    Plt(1, bin2_HQ10000_G1_0_0_000[1], "g:")
    Plt(1, bin3_HQ10000_G1_0_0_000[0], "b-.",
        r"$\gamma = -2.5$")
    Plt(1, bin3_HQ10000_G1_0_0_000[1], "g-.")
    Plt(1, bin4_HQ10000_G1_0_0_000[0], "b",
        r"$\gamma = -3.0$")
    Plt(1, bin4_HQ10000_G1_0_0_000[1], "g")

    ax1.set_xlabel(r"$ u_t $ and $ u_r $", fontsize=20)
    ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
    ax1.set_title(r" File = %s" % HQ0, fontsize=20)

    Plt(2, bin1_HQ10000_G1_0_0_000[4], "b--", label=r"$\gamma = -1.5$")
    Plt(2, bin1_HQ10000_G1_0_0_000[5], "g--")
    Plt(2, bin2_HQ10000_G1_0_0_000[4], "b:", label=r"$\gamma = -2.0$")
    Plt(2, bin2_HQ10000_G1_0_0_000[5], "g:")
    Plt(2, bin3_HQ10000_G1_0_0_000[4], "b-.", label=r"$\gamma = -2.5$")
    Plt(2, bin3_HQ10000_G1_0_0_000[5], "g-.")
    Plt(2, bin4_HQ10000_G1_0_0_000[4], "b", label=r"$\gamma = -3.0$")
    Plt(2, bin4_HQ10000_G1_0_0_000[5], "g")

    ax2.set_xlim(-3, 0)
    ax2.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax2.set_ylabel(
        r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
    )

    Plt(3, bin1_HQ10000_G1_0_0_000[0], "b--", label=r"$\gamma = -1.5$")
    Plt(3, bin1_HQ10000_G1_0_0_000[1], "g--")
    Plt(3, bin2_HQ10000_G1_0_0_000[0], "b:", r"$\gamma = -2.0$")
    Plt(3, bin2_HQ10000_G1_0_0_000[1], "g:")
    Plt(3, bin3_HQ10000_G1_0_0_000[0], "b-.", r"$\gamma = -2.5$")
    Plt(3, bin3_HQ10000_G1_0_0_000[1], "g-.")
    Plt(3, bin4_HQ10000_G1_0_0_000[0], "b", r"$\gamma = -3.0$")
    Plt(3, bin4_HQ10000_G1_0_0_000[1], "g")

    ax3.set_xlabel(r"$ u_t $ and $ u_r $", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")

    Plt(4, bin1_HQ10000_G1_0_0_000[4], "b--", label=r"$\gamma = -1.5$")
    Plt(4, bin1_HQ10000_G1_0_0_000[5], "g--")
    Plt(4, bin2_HQ10000_G1_0_0_000[4], "b:", label=r"$\gamma = -2.0$")
    Plt(4, bin2_HQ10000_G1_0_0_000[5], "g:")
    Plt(4, bin3_HQ10000_G1_0_0_000[4], "b-.", label=r"$\gamma = -2.5$")
    Plt(4, bin3_HQ10000_G1_0_0_000[5], "g-.")
    Plt(4, bin4_HQ10000_G1_0_0_000[4], "b", label=r"$\gamma = -3.0 $")
    Plt(4, bin4_HQ10000_G1_0_0_000[5], "g")

    ax4.set_xlim(-3, 0)
    ax4.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

if Fig_GPerts_same_gammas_as_IC_vr:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(f"ax{i}.legend(
                            prop=dict(size=18),
                            numpoints=2,
                            ncol=1,
                            frameon=True,
                            loc=0,
                            handlelength=2.5)")

    Plt(1, bin1_HQ10000_G1_0_0_000[0], "b--", label=r"%s" % HQ0[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)

    Plt(1, bin1_HQ10000_G1_2_1_005[0], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)

    Plt(1, bin1_HQ10000_G0_8_2_005[0], "g--", label=r"%s" % HQ18[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)

    Plt(1, bin1_HQ10000_G1_2_5_005[0], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)

    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax1.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(1, bin1_HQ10000_G1_2_9_005[1], "y--")
    Plt(1, bin1_HQ10000_G1_0_10_009[0], "m--", label=r"%s" % HQ70[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], "Violet", ls="--", lw=2, ms=7)

    Plt(1, bin2_HQ10000_G1_0_0_000[0], "b:")  # , label=r"$\gamma = -2.0$")

    data, _ = bin2_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=4, ms=7)

    Plt(1, bin2_HQ10000_G1_2_1_005[0], "r:")

    data, _ = bin2_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=4, ms=7)

    Plt(1, bin2_HQ10000_G0_8_2_005[0], "g:")

    data, _ = bin2_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=4, ms=7)

    Plt(1, bin2_HQ10000_G1_2_5_005[0], "k:")

    data, _ = bin2_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)

    data, _ = bin2_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

    Plt(1, bin2_HQ10000_G1_2_9_005[1], "y:")
    Plt(1, bin2_HQ10000_G1_0_10_009[0], "m:")

    data, _ = bin2_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], "Violet", ls=":", lw=4, ms=7)

    Plt(1, bin3_HQ10000_G1_0_0_000[0], "b-.")  # , label=r'$\gamma = -2.5$')

    data, _ = bin3_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=4, ms=7)

    Plt(1, bin3_HQ10000_G1_2_1_005[0], "r-.")

    data, _ = bin3_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=4, ms=7)

    Plt(1, bin3_HQ10000_G0_8_2_005[0], "g-.")

    data, _ = bin3_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=4, ms=7)

    Plt(1, bin3_HQ10000_G1_2_5_005[0], "k-.")

    data, _ = bin3_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)

    data, _ = bin3_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

    Plt(1, bin3_HQ10000_G1_2_9_005[1], "y-.")
    Plt(1, bin3_HQ10000_G1_0_10_009[0], "m-.")

    data, _ = bin3_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], "Violet", ls="-.", lw=4, ms=7)

    Plt(1, bin4_HQ10000_G1_0_0_000[0], "b")  # , label=r'$\gamma = -3.0$'

    data, _ = bin4_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)

    Plt(1, bin4_HQ10000_G1_2_1_005[0], "r")

    data, _ = bin4_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)

    Plt(1, bin4_HQ10000_G0_8_2_005[0], "g")

    data, _ = bin4_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)

    Plt(1, bin4_HQ10000_G1_2_5_005[0], "k")

    data, _ = bin4_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)

    data, _ = bin4_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    Plt(1, bin4_HQ10000_G1_2_9_005[1], "y")
    Plt(1, bin4_HQ10000_G1_0_10_009[0], "m")

    data, _ = bin4_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], "Violet", lw=2, ms=7)

    ax1.set_xlabel(r"$ u_t $ and $ u_r$", fontsize=20)
    ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
    ax1.set_title(r" Time evolution of files = %s" % HQ0[:-9], fontsize=20)

    Plt(2, bin1_HQ10000_G1_0_0_000[4], "b--"), label=r"%s" % HQ0[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)

    Plt(2, bin1_HQ10000_G1_2_1_005[4], "r--"), label=r"%s" % HQ12[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)

    Plt(2, bin1_HQ10000_G0_8_2_005[4], "g--", label=r"%s" % HQ18[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)

    Plt(2, bin1_HQ10000_G1_2_5_005[4], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)

    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax2.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(2, bin1_HQ10000_G1_2_9_005[5], "m--", label=r"%s" % HQ70[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], "Violet", ls="--", lw=2, ms=7)

    Plt(2, bin2_HQ10000_G1_0_0_000[4], "b:")  # , label=r'$\gamma = -2.0$'

    data, _ = bin2_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=2, ms=7)

    Plt(2, bin2_HQ10000_G1_2_1_005[4], "r:")

    data, _ = bin2_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=2, ms=7)

    Plt(2, bin2_HQ10000_G0_8_2_005[4], "g:")

    data, _ = bin2_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=2, ms=7)

    Plt(2, bin2_HQ10000_G1_2_5_005[4], "k:")

    data, _ = bin2_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
    data, _ = bin2_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

    Plt(2, bin2_HQ10000_G1_2_9_005[5], "y:")
    Plt(2, bin2_HQ10000_G1_0_10_009[4], "m:")

    data, _ = bin2_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], "Violet", ls=":", lw=2, ms=7)

    Plt(2, bin3_HQ10000_G1_0_0_000[4], "b-.")  # label=r'$\gamma = -2.5$'

    data, _ = bin3_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=2, ms=7)

    Plt(2, bin3_HQ10000_G1_2_1_005[4], "r-.")

    data, _ = bin3_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=2, ms=7)

    Plt(2, bin3_HQ10000_G0_8_2_005[4], "g-.")

    data, _ = bin3_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=2, ms=7)

    Plt(2, bin3_HQ10000_G1_2_5_005[4], "k-.")

    data, _ = bin3_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
    data, _ = bin3_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

    Plt(2, bin3_HQ10000_G1_2_9_005[5], "y-.")
    Plt(2, bin3_HQ10000_G1_0_10_009[4], "m-.")

    data, _ = bin3_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], "Violet", ls="-.", lw=2, ms=7)

    Plt(2, bin4_HQ10000_G1_0_0_000[4], "b")  # label=r'$\gamma = -3.0$'

    data, _ = bin4_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)

    Plt(2, bin4_HQ10000_G1_2_1_005[4], "r")

    data, _ = bin4_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)

    Plt(2, bin4_HQ10000_G0_8_2_005[4], "g")

    data, _ = bin4_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)

    Plt(2, bin4_HQ10000_G1_2_5_005[4], "k")

    data, _ = bin4_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
    data, _ = bin4_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    Plt(2, bin4_HQ10000_G1_2_9_005[5], "y")
    Plt(2, bin4_HQ10000_G1_0_10_009[4], "m")

    data, _ = bin4_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], "Violet", lw=2, ms=7)

    ax2.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax2.set_ylabel(
        r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
    )

    Plt(3, bin1_HQ10000_G1_0_0_000[0], "b--", label=r"%s" % HQ0[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)

    Plt(3, bin1_HQ10000_G1_2_1_005[0], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)

    Plt(3, bin1_HQ10000_G0_8_2_005[0], "g--", label=r"%s" % HQ18[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)

    Plt(3, bin1_HQ10000_G1_2_5_005[0], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax3.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(3, bin1_HQ10000_G1_2_9_005[1], "y--")
    Plt(3, bin1_HQ10000_G1_0_10_009[0], "m--")

    data, _ = bin1_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], "Violet", ls="--", lw=2, ms=7)

    Plt(3, bin2_HQ10000_G1_0_0_000[0], "b:")  # label=r'$\gamma = -2.0$'

    data, _ = bin2_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=4, ms=7)

    Plt(3, bin2_HQ10000_G1_2_1_005[0], "r:")

    data, _ = bin2_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=4, ms=7)

    Plt(3, bin2_HQ10000_G0_8_2_005[0], "g:")

    data, _ = bin2_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=4, ms=7)

    Plt(3, bin2_HQ10000_G1_2_5_005[0], "k:")

    data, _ = bin2_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
    data, _ = bin2_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

    Plt(3, bin2_HQ10000_G1_2_9_005[1], "y:")
    Plt(3, bin2_HQ10000_G1_0_10_009[0], "m:")

    data, _ = bin2_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], "Violet", ls=":", lw=4, ms=7)

    Plt(3, bin3_HQ10000_G1_0_0_000[0], "b-.")  # label=r'$\gamma = -2.5$'

    data, _ = bin3_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=4, ms=7)

    Plt(3, bin3_HQ10000_G1_2_1_005[0], "r-.")

    data, _ = bin3_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=4, ms=7)

    Plt(3, bin3_HQ10000_G0_8_2_005[0], "g-.")

    data, _ = bin3_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=4, ms=7)

    Plt(3, bin3_HQ10000_G1_2_5_005[0], "k-.")

    data, _ = bin3_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
    data, _ = bin3_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

    Plt(3, bin3_HQ10000_G1_2_9_005[1], "y-.")
    Plt(3, bin3_HQ10000_G1_0_10_009[0], "m-.")

    data, _ = bin3_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], "Violet", ls="-.", lw=4, ms=7)

    Plt(3, bin4_HQ10000_G1_0_0_000[0], "b")  # label=r'$\gamma = -3.0$'

    data, _ = bin4_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)

    Plt(3, bin4_HQ10000_G1_2_1_005[0], "r")

    data, _ = bin4_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)

    Plt(3, bin4_HQ10000_G0_8_2_005[0], "g")

    data, _ = bin4_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)

    Plt(3, bin4_HQ10000_G1_2_5_005[0], "k")

    data, _ = bin4_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
    data, _ = bin4_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    Plt(3, bin4_HQ10000_G1_2_9_005[1], "y")
    Plt(3, bin4_HQ10000_G1_0_10_009[0], "m")

    data, _ = bin4_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], "Violet", lw=2, ms=7)

    ax3.set_xlabel(r"$ u_t $ and $ u_r $", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")

    Plt(4, bin1_HQ10000_G1_0_0_000[4], "b--", label=r"%s" % HQ0[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)

    Plt(4, bin1_HQ10000_G1_2_1_005[4], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)

    Plt(4, bin1_HQ10000_G0_8_2_005[4], "g--", label=r"%s" % HQ18[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)

    Plt(4, bin1_HQ10000_G1_2_5_005[4], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)

    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax4.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(4, bin1_HQ10000_G1_2_9_005[5], "y--")
    Plt(4, bin1_HQ10000_G1_0_10_009[4], "m--", label=r"%s" % HQ70[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], "Violet", ls="--", lw=2, ms=7)

    Plt(4, bin2_HQ10000_G1_0_0_000[4], "b:")

    data, _ = bin2_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=2, ms=7)

    Plt(4, bin2_HQ10000_G1_2_1_005[4], "r:")

    data, _ = bin2_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=2, ms=7)

    Plt(4, bin2_HQ10000_G0_8_2_005[4], "g:")

    data, _ = bin2_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=2, ms=7)

    Plt(4, bin2_HQ10000_G1_2_5_005[4], "k:")

    data, _ = bin2_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)

    data, _ = bin2_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

    Plt(4, bin2_HQ10000_G1_2_9_005[5], "y:")
    Plt(4, bin2_HQ10000_G1_0_10_009[4], "m:")

    data, _ = bin2_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], "Violet", ls=":", lw=2, ms=7)

    Plt(4, bin3_HQ10000_G1_0_0_000[4], "b-.")  # , label=r'$\gamma = -2.5$'

    data, _ = bin3_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=2, ms=7)

    Plt(4, bin3_HQ10000_G1_2_1_005[4], "r-.")

    data, _ = bin3_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=2, ms=7)

    Plt(4, bin3_HQ10000_G0_8_2_005[4], "g-.")

    data, _ = bin3_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=2, ms=7)

    Plt(4, bin3_HQ10000_G1_2_5_005[4], "k-.")

    data, _ = bin3_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)

    data, _ = bin3_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

    Plt(4, bin3_HQ10000_G1_2_9_005[5], "y-.")
    Plt(4, bin3_HQ10000_G1_0_10_009[4], "m-.")

    data, _ = bin3_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], "Violet", ls="-.", lw=2, ms=7)

    Plt(4, bin4_HQ10000_G1_0_0_000[4], "b")  # label=r'$\gamma = -3.0$'

    data, _ = bin4_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)

    Plt(4, bin4_HQ10000_G1_2_1_005[4], "r")

    data, _ = bin4_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)

    Plt(4, bin4_HQ10000_G0_8_2_005[4], "g")

    data, _ = bin4_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)

    Plt(4, bin4_HQ10000_G1_2_5_005[4], "k")

    data, _ = bin4_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)

    data, _ = bin4_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    Plt(4, bin4_HQ10000_G1_2_9_005[5], "y")
    Plt(4, bin4_HQ10000_G1_0_10_009[4], "m")

    data, _ = bin4_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], "Violet", lw=2, ms=7)

    ax4.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

if Fig_GPerts_G1_2_same_gammas_as_IC_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(f"ax{i}.legend(
                            prop=dict(size=18),
                            numpoints=2,
                            ncol=1,
                            frameon=True,
                            loc=0,
                            handlelength=2.5)")

    Plt(1, bin1_HQ10000_G1_2_1_005[0], "b--", label=r"%s" % HQ12[len("HQ10000_G") :])
    Plt(1, bin1_HQ10000_G1_2_3_005[0], "r--", label=r"%s" % HQ24[len("HQ10000_G") :])
    Plt(1, bin1_HQ10000_G1_2_5_005[0], "g--", label=r"%s" % HQ36[len("HQ10000_G") :])
    Plt(1, bin1_HQ10000_G1_2_7_005[0], "k--", label=r"%s" % HQ48[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax1.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(1, bin2_HQ10000_G1_2_1_005[0], "r:")
    Plt(1, bin2_HQ10000_G1_2_3_005[0], "g:")
    Plt(1, bin2_HQ10000_G1_2_5_005[0], "k:")

    data, _ = bin2_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)

    data, _ = bin2_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

    Plt(1, bin3_HQ10000_G1_2_1_005[0], "r-.")
    Plt(1, bin3_HQ10000_G1_2_3_005[0], "g-.")
    Plt(1, bin3_HQ10000_G1_2_5_005[0], "k-.")

    data, _ = bin3_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)

    data, _ = bin3_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

    Plt(1, bin4_HQ10000_G1_2_1_005[0], "r")
    Plt(1, bin4_HQ10000_G1_2_3_005[0], "g")
    Plt(1, bin4_HQ10000_G1_2_5_005[0], "k")

    data, _ = bin4_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)

    data, _ = bin4_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    ax1.set_xlabel(r"$ u_t $ and $ u_r $", fontsize=20)
    ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
    ax1.set_title(r" Time evolution of files = %s" % HQ0[:-9], fontsize=20)

    Plt(2, bin1_HQ10000_G1_2_1_005[4], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])
    Plt(2, bin1_HQ10000_G1_2_3_005[4], "g--", label=r"%s" % HQ24[len("HQ10000_G") :])
    Plt(2, bin1_HQ10000_G1_2_5_005[4], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_7_005[4]
    ax2.plot(
        data[:, 0],
        data[:, 1],
        "Brown",
        ls="--",
        label=r"%s" % HQ48[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax2.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(2, bin2_HQ10000_G1_2_1_005[4], "r:")
    Plt(2, bin2_HQ10000_G1_2_3_005[4], "g:")
    Plt(2, bin2_HQ10000_G1_2_5_005[4], "k:")

    data, _ = bin2_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)

    data, _ = bin2_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

    Plt(2, bin3_HQ10000_G1_2_1_005[4], "r-.")
    Plt(2, bin3_HQ10000_G1_2_3_005[4], "g-.")
    Plt(2, bin3_HQ10000_G1_2_5_005[4], "k-.")

    data, _ = bin3_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)

    data, _ = bin3_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

    Plt(2, bin4_HQ10000_G1_2_1_005[4], "r")
    Plt(2, bin4_HQ10000_G1_2_3_005[4], "g")
    Plt(2, bin4_HQ10000_G1_2_5_005[4], "k")

    data, _ = bin4_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)

    data, _ = bin4_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    ax2.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax2.set_ylabel(
        r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
    )

    Plt(3, bin1_HQ10000_G1_2_1_005[0], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])
    Plt(3, bin1_HQ10000_G1_2_3_005[0], "g--", label=r"%s" % HQ24[len("HQ10000_G") :])
    Plt(3, bin1_HQ10000_G1_2_5_005[0], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_7_005[0]
    ax3.plot(
        data[:, 0],
        data[:, 1],
        "Brown",
        ls="--",
        label=r"%s" % HQ48[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax3.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(3, bin2_HQ10000_G1_2_1_005[0], "r:")
    Plt(3, bin2_HQ10000_G1_2_3_005[0], "g:")
    Plt(3, bin2_HQ10000_G1_2_5_005[0], "k:")

    data, _ = bin2_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)

    data, _ = bin2_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

    Plt(3, bin3_HQ10000_G1_2_1_005[0], "r-.")
    Plt(3, bin3_HQ10000_G1_2_3_005[0], "g-.")
    Plt(3, bin3_HQ10000_G1_2_5_005[0], "k-.")

    data, _ = bin3_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)

    data, _ = bin3_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

    Plt(3, bin4_HQ10000_G1_2_1_005[0], "r")
    Plt(3, bin4_HQ10000_G1_2_3_005[0], "g")
    Plt(3, bin4_HQ10000_G1_2_5_005[0], "k")

    data, _ = bin4_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)

    data, _ = bin4_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    ax3.set_xlabel(r"$u_t $ and $ u_r$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")

    Plt(4, bin1_HQ10000_G1_2_1_005[4], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])
    Plt(4, bin1_HQ10000_G1_2_3_005[4], "g--", label=r"%s" % HQ24[len("HQ10000_G") :])
    Plt(4, bin1_HQ10000_G1_2_5_005[4], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

    data, _ = bin1_HQ10000_G1_2_7_005[4]
    ax4.plot(
        data[:, 0],
        data[:, 1],
        "Brown",
        ls="--",
        label=r"%s" % HQ48[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax4.plot(
        data[:, 0],
        data[:, 1],
        "Orange",
        ls="--",
        label=r"%s" % HQ60[len("HQ10000_G") :],
        lw=2,
        ms=7,
    )

    Plt(4, bin2_HQ10000_G1_2_1_005[4], "r:")
    Plt(4, bin2_HQ10000_G1_2_3_005[4], "g:")
    Plt(4, bin2_HQ10000_G1_2_5_005[4], "k:")

    data, _ = bin2_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)

    data, _ = bin2_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

    Plt(4, bin3_HQ10000_G1_2_1_005[4], "r-.")
    Plt(4, bin3_HQ10000_G1_2_3_005[4], "g-.")
    Plt(4, bin3_HQ10000_G1_2_5_005[4], "k-.")

    data, _ = bin3_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)

    data, _ = bin3_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

    Plt(4, bin4_HQ10000_G1_2_1_005[4], "r")
    Plt(4, bin4_HQ10000_G1_2_3_005[4], "g")
    Plt(4, bin4_HQ10000_G1_2_5_005[4], "k")

    data, _ = bin4_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)

    data, _ = bin4_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    ax4.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

if Fig_GPerts_different_gammas_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    if test:

        for i in range(1, 5):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        Plt(1, bin1_different_gammas_HQ10000_G1_2_1_005[0], "b--", label=r"%s" % HQ12[len("HQ10000_G") :])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_3_005[0], "r--", label=r"%s" % HQ24[len("HQ10000_G") :])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_5_005[0], "g--", label=r"%s" % HQ36[len("HQ10000_G") :])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_7_005[0], "k--", label=r"%s" % HQ48[len("HQ10000_G") :])

        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            ls="--",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(1, bin2_different_gammas_HQ10000_G1_2_1_005[0], "r:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_3_005[0], "g:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_5_005[0], "k:")

        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(1, bin3_different_gammas_HQ10000_G1_2_1_005[0], "r-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_3_005[0], "g-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_5_005[0], "k-.")

        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(1, bin4_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_5_005[0], "k")

        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax1.set_xlabel(r"$ u_t $", fontsize=20)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins" % HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g--", label=r"%s" % HQ24[len("HQ10000_G") :])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            ls="--",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            ls="--",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(2, bin2_different_gammas_HQ10000_G1_2_1_005[4], "r:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_3_005[4], "g:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_5_005[4], "k:")

        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

        Plt(2, bin3_different_gammas_HQ10000_G1_2_1_005[4], "r-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_3_005[4], "g-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_5_005[4], "k-.")

        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

        Plt(2, bin4_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_5_005[4], "k")

        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        Plt(3, bin1_different_gammas_HQ10000_G1_2_1_005[0], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_3_005[0], "g--", label=r"%s" % HQ24[len("HQ10000_G") :])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_5_005[0], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            ls="--",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            ls="--",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(3, bin2_different_gammas_HQ10000_G1_2_1_005[0], "r:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_3_005[0], "g:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_5_005[0], "k:")

        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(3, bin3_different_gammas_HQ10000_G1_2_1_005[0], "r-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_3_005[0], "g-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_5_005[0], "k-.")

        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(3, bin4_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_5_005[0], "k")

        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax3.set_xlabel(r"$ u_t $", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r--", label=r"%s" % HQ12[len("HQ10000_G") :])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g--", label=r"%s" % HQ24[len("HQ10000_G") :])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k--", label=r"%s" % HQ36[len("HQ10000_G") :])

        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            ls="--",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            ls="--",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(4, bin2_different_gammas_HQ10000_G1_2_1_005[4], "r:")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_3_005[4], "g:")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_5_005[4], "k:")

        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

        Plt(4, bin3_different_gammas_HQ10000_G1_2_1_005[4], "r-.")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_3_005[4], "g-.")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_5_005[4], "k-.")

        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

        Plt(4, bin4_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_5_005[4], "k")

        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

    if test2:
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "b--", label=r"%s" % test2_HQ0[len("test2_HQ10000_G") :])
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "r--", label=r"%s" % test2_HQ36[len("test2_HQ10000_G") :])
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0], "g--", label=r"%s" % test2_HQ66[len("test2_HQ10000_G") :])
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_15_005[0], "k--", label=r"%s" % test2_HQ96[len("test2_HQ10000_G") :])

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            ls="--",
            label=r"%s" % test2_HQ126[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0], "b--", label=r"%s" % test2_HQ159[len("test2_HQ10000_G") :])
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_0_000[0], "r:")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_5_005[0], "g:")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_10_005[0], "k:")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_25_005[0], "b:")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_0_000[0], "r-.")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_5_005[0], "g-.")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_10_005[0], "k-.")

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_25_005[0], "b-.")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        ax1.set_xlabel(r"$ u_t $", fontsize=20)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins"
            % test2_HQ0[:-9],
            fontsize=20,
        )
        ax1.legend(
            prop=dict(size=18),
            numpoints=2,
            ncol=1,
            frameon=True,
            loc=0,
            handlelength=2.5,
        )

        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "b--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "r--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "g--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_15_005[4], "k--")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls="--", lw=2, ms=7)

        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b--")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_0_000[4], "r:")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_5_005[4], "g:")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_10_005[4], "k:")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_25_005[4], "b:")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_0_000[4], "r-.")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_5_005[4], "g-.")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_10_005[4], "k-.")

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_25_005[4], "b-.")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "b--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "r--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0], "g--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_15_005[0], "k--")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls="--", lw=2, ms=7)

        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0], "b--")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_0_000[0], "r:")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_5_005[0], "g:")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_10_005[0], "k:")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_25_005[0], "b:")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_0_000[0], "r-.")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_5_005[0], "g-.")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_10_005[0], "k-.")

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_25_005[0], "b-.")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        ax3.set_xlabel(r"$ u_t $", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "b--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "r--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "g--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_15_005[4], "k--")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls="--", lw=2, ms=7)

        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b--")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_0_000[4], "r:")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_5_005[4], "g:")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_10_005[4], "k:")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_25_005[4], "b:")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_0_000[4], "r-.")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_5_005[4], "g-.")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_10_005[4], "k-.")

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_25_005[4], "b-.")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

    if B:
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_0_000[0], "r--", label=r"%s" % B_HQ0[len("B_HQ10000_G") :])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_5_005[0], "g--", label=r"%s" % B_HQ36[len("B_HQ10000_G") :])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_10_005[0], "k--", label=r"%s" % B_HQ66[len("B_HQ10000_G") :])

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            ls="--",
            label=r"%s" % B_HQ294[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            ls="--",
            label=r"%s" % B_HQ382[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_0_000[0], "r:")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_5_005[0], "g:")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_10_005[0], "k:")

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_0_000[0], "r-.")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_5_005[0], "g-.")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_10_005[0], "k-.")

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax1.set_xlabel(r"$ u_t $", fontsize=20)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins" % B_HQ0[:-9],
            fontsize=20,
        )
        ax1.legend(
            prop=dict(size=18),
            numpoints=2,
            ncol=1,
            frameon=True,
            loc=0,
            handlelength=2.5,
        )
        ax1.set_xlim(0, 3)
        ax1.axes.get_xaxis().set_visible(False)
        ax1.tick_params(
            axis="both",
            which="both",
            bottom="off",
            top="off",
            labelbottom="off",
            right="off",
            left="on",
            labelleft="on",
        )

        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_0_000[4], "r--")
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_5_005[4], "g--")
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_10_005[4], "k--")

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls="--", lw=2, ms=7)

        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_0_000[4], "r:")
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_5_005[4], "g:")
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_10_005[4], "k:")

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_0_000[4], "r-.")
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_5_005[4], "g-.")
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_10_005[4], "k-.")

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_10_005[4], "k")

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax2.set_xlim(-3, 1)
        ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )
        ax2.axes.get_xaxis().set_visible(False)
        ax2.yaxis.tick_right()
        ax2.yaxis.set_label_position("right")

        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_0_000[0], "r--")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_5_005[0], "g--")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_10_005[0], "k--")

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls="--", lw=2, ms=7)

        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_0_000[0], "r:")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_5_005[0], "g:")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_10_005[0], "k:")

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)

        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_0_000[0], "r-.")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_5_005[0], "g-.")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_10_005[0], "k-.")

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)

        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax3.set_xlabel(r"$ u_t $", fontsize=20)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")
        ax3.tick_params(
            axis="both",
            which="both",
            bottom="on",
            top="off",
            labelbottom="on",
            right="off",
            left="on",
            labelleft="on",
        )
        ax3.set_xlim(0, 3)

        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_0_000[4], "r--")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_5_005[4], "g--")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_10_005[4], "k--")

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls="--", lw=2, ms=7)

        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_0_000[4], "r:")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_5_005[4], "g:")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_10_005[4], "k:")

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)

        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_0_000[4], "r-.")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_5_005[4], "g-.")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_10_005[4], "k-.")

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)

        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_10_005[4], "k")

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax4.set_xlim(-3, 1)
        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")
        ax4.yaxis.tick_right()
        ax4.yaxis.set_label_position("right")
        ax4.tick_params(
            axis="both",
            which="both",
            bottom="on",
            top="off",
            labelbottom="on",
            right="on",
            left="off",
            labelleft="off",
        )
        f.savefig("Time_evolution_B_vt_different_rbins.png")

if Fig_GPerts_gammas_1_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        Plt(1, bin1_different_gammas_HQ10000_G1_2_1_005[0], "b")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_3_005[0], "r")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_5_005[0], "g")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_7_005[0], "k")

        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -1.5$"
            % HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r", label=r"%s " % HQ12[len("HQ10000_G") :])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g", label=r"%s" % HQ24[len("HQ10000_G") :])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k", label=r"%s" % HQ36[len("HQ10000_G") :])

        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )

        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        Plt(3, bin1_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_5_005[0], "k")

        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k")

        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20
        )

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$",
            fontsize=20)

    if test2:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -1.5$"
            % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "r", label=r"%s " % test2_HQ0[len("test2_HQ10000_G") :])
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "g", label=r"%s" % test2_HQ36[len("test2_HQ10000_G") :])
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "k", label=r"%s" % test2_HQ66[len("test2_HQ10000_G") :])

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % test2_HQ96[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % test2_HQ126[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b", label=r"%s" % test2_HQ159[len("test2_HQ10000_G") :])

        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if A:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

    for i in range(1, 7):
        exec(f"ax{i}.legend(
                            prop=dict(size=18),
                            numpoints=2,
                            ncol=1,
                            frameon=True,
                            loc=0,
                            handlelength=2.5)")

        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -1.5$"
            % A_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_0_000[4], "r", label=r"%s " % A_HQ0[len("A_HQ10000_G") :])
        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_5_005[4], "g", label=r"%s" % A_HQ36[len("A_HQ10000_G") :])
        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_10_005[4], "k", label=r"%s" % A_HQ66[len("A_HQ10000_G") :])

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % A_HQ246[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % A_HQ298[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )

        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_48_093[4], "b", label=r"%s" % A_HQ382[len("A_HQ10000_G") :])

        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_10_005[0], "k")

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_10_005[4], "k")

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_48_093[4], "b")

        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20)

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if B:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

    for i in range(1, 7):
        exec(f"ax{i}.legend(
                            prop=dict(size=18),
                            numpoints=2,
                            ncol=1,
                            frameon=True,
                            loc=0,
                            handlelength=2.5)")

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -1.5$"
            % B_HQ0[:-9],
            fontsize=20)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % B_HQ0[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % B_HQ36[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % B_HQ66[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % B_HQ294[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % B_HQ382[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$",
            fontsize=20)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

if Fig_GPerts_gammas_2_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

    for i in range(1, 7):
        exec(f"ax{i}.legend(
                            prop=dict(size=18),
                            numpoints=2,
                            ncol=1,
                            frameon=True,
                            loc=0,
                            handlelength=2.5)")

        data, _ = bin2__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -2.0$"
            % HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % HQ12[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % HQ24[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % HQ36[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20
        )

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$",
            fontsize=20)

    if test2:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

    for i in range(1, 3):
        exec(f"ax{i}.legend(
                            prop=dict(size=18),
                            numpoints=2,
                            ncol=1,
                            frameon=True,
                            loc=0,
                            handlelength=2.5)")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -2.0$"
            % test2_HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % test2_HQ0[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % test2_HQ36[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % test2_HQ66[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % test2_HQ96[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % test2_HQ126[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % test2_HQ159[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if A:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -2.0$"
            % A_HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % A_HQ0[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % A_HQ36[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % A_HQ66[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % A_HQ246[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % A_HQ298[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % A_HQ382[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20)

    if B:
        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -2.0$"
            % B_HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % B_HQ0[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % B_HQ36[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % B_HQ66[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % B_HQ294[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % B_HQ382[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$",
            fontsize=20)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

if Fig_GPerts_gammas_2_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin3__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -2.5$"
            % HQ0[:-9],
            fontsize=20,
        )

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % HQ12[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % HQ24[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % HQ36[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20
        )

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$",
            fontsize=20)

    if test2:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -2.5 $"
            % test2_HQ0[:-9],
            fontsize=20,
        )

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % test2_HQ0[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % test2_HQ36[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % test2_HQ66[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % test2_HQ96[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % test2_HQ126[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % test2_HQ159[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if A:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -2.5$"
            % A_HQ0[:-9],
            fontsize=20)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % A_HQ0[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % A_HQ36[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % A_HQ66[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % A_HQ246[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % A_HQ298[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % A_HQ382[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if B:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -2.5$"
            % B_HQ0[:-9], fontsize=20)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % B_HQ0[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % B_HQ36[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % B_HQ66[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % B_HQ294[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % B_HQ382[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$",
            fontsize=20)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

if Fig_GPerts_gammas_3_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin4__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -3.0$"
            % HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % HQ12[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % HQ24[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % HQ36[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$",
            fontsize=20)

    if test2:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -3.0 $"
            % test2_HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % test2_HQ0[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % test2_HQ36[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % test2_HQ66[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % test2_HQ96[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % test2_HQ126[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % test2_HQ159[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if A:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -3.0$"
            % A_HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % A_HQ0[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % A_HQ36[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % A_HQ66[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % A_HQ246[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % A_HQ298[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % A_HQ382[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20)

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if B:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of %s , different r bins, $\gamma = -3.0$"
            % B_HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % B_HQ0[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % B_HQ36[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % B_HQ66[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % B_HQ294[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % B_HQ382[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (914.415 * data[:, 0] * np.exp(-0.930 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$", fontsize=20)

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3452.955
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.936 * (10 ** data[:, 0]) ** 2)
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
            fontsize=20)

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                894.292
                * data[:, 0]
                * (1 - (1 - 0.955) * 0.918 * data[:, 0] ** 2)
                ** (0.955 / (1 - 0.955))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3418.569
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.929 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "Orange",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

if Fig_GPerts_R_middle_19_95_vt_divided_by_gauss_and_Tsallis:
    # f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -1.5$"
            % HQ0[:-9], fontsize=20)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % HQ12[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % HQ24[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % HQ36[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20)
        ax4.set_yscale("log")

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "g",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Brown",
            lw=2,
            ms=7,
        )
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$",
            fontsize=20)

    if test2:

        f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(
            4, 2
        )

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s ,  $ R_{middle} = 19.95 $"
            % test2_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % test2_HQ0[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % test2_HQ66[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % test2_HQ166[len("test2_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if A:

        f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(
            4, 2
        )

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s ,  $ R_{middle} = 19.95 $"
            % A_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % A_HQ0[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % A_HQ66[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % A_HQ382[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_ylabel(
            r"$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis} $", fontsize=20)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if B:

        f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(
            4, 2
        )

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s ,  $ R_{middle} = 19.95 $"
            % B_HQ0[:-9],
            fontsize=20,
        )

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % B_HQ0[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % B_HQ66[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % B_HQ294[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % B_HQ382[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        ax5.set_ylabel(
            r"$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis} $", fontsize=20)

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

if Fig16_GPerts_R_middle_31_62_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , different r bins, $\gamma = -2.0$"
            % HQ0[:-9],
            fontsize=20,
        )

        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % HQ12[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % HQ24[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % HQ36[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Brown",
            label=r"%s" % HQ48[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "Orange",
            label=r"%s" % HQ60[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_xticklabels([])
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20
        )

        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Brown",
            lw=2,
            ms=7,
        )
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (np.log10(data[:, 0]) * np.exp(-0.5 * data[:, 0] ** 2)),
            "Orange",
            lw=2,
            ms=7,
        )
        ax5.set_xticklabels([])
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20
        )

        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "r",
            lw=2,
            ms=7,
        )
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "g",
            lw=2,
            ms=7,
        )
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "k",
            lw=2,
            ms=7,
        )
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Brown",
            lw=2,
            ms=7,
        )
        ax6.plot(
            data[:, 0],
            data[:, 1] / np.exp(-0.5 * data[:, 0] ** 2),
            "Orange",
            lw=2,
            ms=7,
        )
        ax6.set_xticklabels([])
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$",
            fontsize=20,
        )

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , $ R_{middle} = 31.62 $"
            % test2_HQ0[:-9],
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % test2_HQ0[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % test2_HQ66[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % test2_HQ166[len("HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_ylabel(
            r"$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis} $", fontsize=20)

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if A:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , $ R_{middle} = 31.62 $"
            % A_HQ0[:-9],
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % A_HQ0[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % A_HQ66[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % A_HQ382[len("A_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        ax5.set_ylabel(
            r"$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis} $", fontsize=20)

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

    if B:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(
                                prop=dict(size=18),
                                numpoints=2,
                                ncol=1,
                                frameon=True,
                                loc=0,
                                handlelength=2.5)")

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(
            r" Time evolution of files = %s , $ R_{middle} = 31.62 $"
            % B_HQ0[:-9],
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "r",
            label=r"%s " % B_HQ0[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "k",
            label=r"%s" % B_HQ66[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "b",
            label=r"%s" % B_HQ294[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(
            data[:, 0],
            data[:, 1],
            "g",
            label=r"%s" % B_HQ382[len("B_HQ10000_G") :],
            lw=2,
            ms=7,
        )
        ax2.set_ylabel(
            r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20
        )

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax3.set_ylabel(
            r"$\log \left( f\left( u_t \right) \right)$", fontsize=20
        )
        ax3.set_yscale("log")

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(
            data[:, 0],
            data[:, 1]
            / (887.569 * data[:, 0] * np.exp(-0.922 * data[:, 0] ** 2)),
            "g",
            lw=2,
            ms=7,
        )
        ax5.set_ylabel(
            r"$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(
            data[:, 0],
            data[:, 1]
            / (
                3424.993
                * (10 ** data[:, 0]) ** 2
                * np.exp(-0.930 * (10 ** data[:, 0]) ** 2)
            ),
            "g",
            lw=2,
            ms=7,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(
            data[:, 0],
            data[:, 1]
            / (
                864.543
                * data[:, 0]
                * (1 - (1 - 0.946) * 0.908 * data[:, 0] ** 2)
                ** (0.946 / (1 - 0.946))
            ),
            "g",
            lw=2,
            ms=7,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis} $", fontsize=20)

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "r",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "k",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "b",
            lw=2,
            ms=7,
        )
        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(
            data[:, 0],
            data[:, 1]
            / (
                3391.113
                * 10 ** data[:, 0]
                * (1 - (1 - 0.987) * 0.924 * 10 ** (data[:, 0] ** 2))
                ** (0.987 / (1.0 - 0.987))
            ),
            "g",
            lw=2,
            ms=7,
        )
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$",
            fontsize=20,
        )

plt.show()
