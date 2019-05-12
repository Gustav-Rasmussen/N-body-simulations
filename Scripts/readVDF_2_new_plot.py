# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pylab
from readVDF_2_new_files import *
from readVDF2 import Plt

# import RhoAndGaussianAndTsallis
# import snapshotFiles

# Switches ---------------------------------------------------------
Gamma_on = 1
Beta_on = 0

# Figures ---------------------------------------------------------------------
# WF: Works For
Fig2a_vr_vPhi_vTheta_divided_by_gauss = 0  # WF: test, test2
Fig2b_vt_divided_by_gauss = 0  # WF: test, test2
Fig3a_GPerts_same_gammas_as_IC_vr = 0  # WF: test. test2?
Fig3b_GPerts_G1_2_same_gammas_as_IC_vt = 0  # Not yet created
Fig4_GPerts_different_gammas_vt = 0  # WF: test, test2, B
# Next 4 figures works for test, test2, B:
Fig5a_GPerts_gammas_1_5_vt_divided_by_gauss_and_Tsallis = 0
Fig5b_GPerts_gammas_2_0_vt_divided_by_gauss_and_Tsallis = 0
Fig5c_GPerts_gammas_2_5_vt_divided_by_gauss_and_Tsallis = 0
Fig5d_GPerts_gammas_3_0_vt_divided_by_gauss_and_Tsallis = 0
# Next 2 figures works for A, B:
Fig6a_GPerts_R_middle_19_95_vt_divided_by_gauss_and_Tsallis = 0
Fig6b_GPerts_R_middle_31_62_vt_divided_by_gauss_and_Tsallis = 0

if Fig2a_vr_vPhi_vTheta_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        data, _ = bin2_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1] / (478.006 * np.exp(-.456
                 * data[:, 0] ** 2)),
                 "g:", label=r"$r, a=478.006, b=0.456$", lw=4, ms=7)
        data, _ = bin2_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0], data[:, 1] / (482.605 * np.exp(-.473
                 * data[:, 0] ** 2)),
                 "r:", label=r"$\Theta, a=482.605, b=0.473$", lw=4, ms=7)
        data, _ = bin2_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0], data[:, 1] / (502.652 * np.exp(-.477
                 * data[:, 0] ** 2)),
                 "k:", label=r"$\Phi, a=502.652, b=0.477$", lw=2, ms=7)

        ax1.set_xlabel(r"$u_r$, $u_{\Theta}$ and $u_{\Phi}$", fontsize=20)
        ax1.set_ylabel(r"$\frac{f\left(u \right)}{ae^{-bx^2}}$", fontsize=20)
        ax1.set_title(r"File = %s, $\gamma = -2.0$" % HQ12, fontsize=20)

        data, _ = bin2_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:, 0], data[:, 1] / (1433.228 * 10 ** data[:, 0]
                 * np.exp(-.472 * (10 ** data[:, 0]) ** 2)),
                 "g:", label=r"$a=1433.228, b=0.472$", lw=2, ms=7)
        data, _ = bin2_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:, 0], data[:, 1] / (1416.346 * 10 ** data[:, 0]
                 * np.exp(-.473 * (10 ** data[:, 0]) ** 2)),
                 "r:", label=r"$ a=1416.346, b=0.473 $", lw=2, ms=7)
        data, _ = bin2_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:, 0], data[:, 1] / (1405.914 * 10 ** data[:, 0]
                 * np.exp(-.470 * (10 ** data[:, 0]) ** 2)),
                 "k:", label=r"$a=1405.914, b=0.470$", lw=2, ms=7)

        ax2.set_xlabel(r"$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                        |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                        |u_{\Phi}n|,u_{\Phi}p \right)$", fontsize=20)
        ax2.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,\
                         u_p \right)\right)}{axe^{-b\log (x)^2}}$",
                         fontsize=20)
        # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}

    if test2:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:, 0], data[:, 1] / (478.006 * np.exp(-.456
                 * data[:, 0] ** 2)),
                 "g:", label=r"$r, a=478.006, b=0.456$", lw=4, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:, 0],
            data[:, 1] / (482.605 * np.exp(-.473 * data[:, 0] ** 2)),
            "r:", label=r"$\Theta, a=482.605, b=0.473$", lw=4, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:, 0],
            data[:, 1] / (502.652 * np.exp(-.477 * data[:, 0] ** 2)),
            "k:", label=r"$\Phi, a=502.652, b=0.477$", lw=2, ms=7)

        ax1.set_xlabel(r"$u_r$, $u_{\Theta}$ and $u_{\Phi}$", fontsize=20)
        ax1.set_ylabel(r"$\frac{f\left(u \right)}{ae^{-bx^2}}$", fontsize=20)
        ax1.set_title(r"File = %s, $\gamma = -2.0$" % test2_HQ0, fontsize=20)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:, 0], data[:, 1] / (1433.228 * 10 ** data[:, 0]
                 * np.exp(-.472 * (10 ** data[:, 0]) ** 2)),
                 "g:", label=r"$a=1433.228, b=0.472$", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:, 0], data[:, 1] / (1416.346 * 10 ** data[:, 0]
                 * np.exp(-.473 * (10 ** data[:, 0]) ** 2)),
                 "r:", label=r"$a=1416.346, b=0.473$", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:, 0], data[:, 1] / (1405.914 * 10 ** data[:, 0]
                 * np.exp(-.470 * (10 ** data[:, 0]) ** 2)),
                 "k:", label=r"$ a=1405.914, b=0.470$", lw=2, ms=7)

        ax2.set_xlabel(r"$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                       |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                       |u_{\Phi}n|,u_{\Phi}p \right)$", fontsize=20)
        ax2.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {axe^{-b\log (x)^2}}$", fontsize=20)

if Fig2b_vt_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        def denom_ax1(a):
            return 918.083 * a * np.exp(-.922 * a ** 2)

        data, _ = bin1_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b--", label=r"$ \gamma = -1.5$", lw=3)
        data, _ = bin2_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b:", label=r"$ \gamma = -2.0$", lw=4, ms=7)
        data, _ = bin3_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b-.", label=r"$ \gamma = -2.5$", lw=4, ms=7)
        data, _ = bin4_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b", label=r"$ \gamma = -3.0$", lw=2, ms=7)

        ax1.set_ylim(0, 2)
        ax1.set_xlabel(r"$u_t$", fontsize=20)
        ax1.set_ylabel(r"$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$",
                       fontsize=20)
        ax1.set_title(r"File = %s" % HQ12, fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0,  handlelength=2.5)

        def denom_ax2(a):
            return 3400.442 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin1_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b--", label=r"$ \gamma = -1.5 $", lw=2, ms=7)
        data, _ = bin2_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b:", label=r"$ \gamma = -2.0 $", lw=2, ms=7)
        data, _ = bin3_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b-.", label=r"$ \gamma = -2.5 $", lw=2, ms=7)
        data, _ = bin4_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b", label=r"$ \gamma = -3.0 $", lw=2, ms=7)

        ax2.set_xlabel(r"$\log \left(|u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(r"$\frac{f\left(\log \left(|u_tn|,u_tp \right)\
                         \right)}{3400.442x^2e^{-0.930x^2}}$", fontsize=20)
        # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}

    if test2:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        def denom_ax1(a):
            return 918.083 * a * np.exp(-.922 * a ** 2)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b--", label=r"$ \gamma = -1.5 $", lw=3)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b:", label=r"$ \gamma = -2.0 $", lw=4, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b-.", label=r"$ \gamma = -2.5 $", lw=4, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1] / denom_ax1(data[:, 0]),
                 "b", label=r"$ \gamma = -3.0 $", lw=2, ms=7)

        ax1.set_ylim(0, 2)
        ax1.set_xlabel(r"$u_t$", fontsize=20)
        ax1.set_ylabel(r"$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$",
                       fontsize=20)
        ax1.set_title(r"File = %s" % test2_HQ0, fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        def denom_ax2(a):
            return 3400.442 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b--", label=r"$ \gamma = -1.5 $", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b:", label=r"$ \gamma = -2.0 $", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b-.", label=r"$ \gamma = -2.5 $", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1] / denom_ax2(data[:, 0]),
                 "b", label=r"$ \gamma = -3.0 $", lw=2, ms=7)

        ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {3400.442x^2e^{-0.930x^2}}$", fontsize=20)

if Fig3a_GPerts_same_gammas_as_IC_vr:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
               frameon=True, loc=0, handlelength=2.5)")

    Plt(1, bin1_HQ10000_G1_0_0_000[0], "b--", r"%s" % HQ0[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(1, bin1_HQ10000_G1_2_1_005[0], "r--", r"%s" % HQ12[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(1, bin1_HQ10000_G0_8_2_005[0], "g--", r"%s" % HQ18[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(1, bin1_HQ10000_G1_2_5_005[0], "k--", r"%s" % HQ36[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange",
             ls="--", label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
    Plt(1, bin1_HQ10000_G1_2_9_005[1], "y--")
    Plt(1, bin1_HQ10000_G1_0_10_009[0], "m--", r"%s" % HQ70[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], "Violet", ls="--", lw=2, ms=7)
    Plt(1, bin2_HQ10000_G1_0_0_000[0], "b:")  # label=r'$\gamma = -2.0$'
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
    Plt(1, bin3_HQ10000_G1_0_0_000[0], "b-.")  # label=r'$\gamma = -2.5$'
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
    Plt(1, bin4_HQ10000_G1_0_0_000[0], "b")  # label=r'$\gamma = -3.0$'
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

    ax1.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
    ax1.set_title(r"Time evolution of files = %s" % HQ0[:-9], fontsize=20)

    # label=r'$\gamma = -1.5$'
    Plt(2, bin1_HQ10000_G1_0_0_000[4], "b--", HQ0[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(2, bin1_HQ10000_G1_2_1_005[4], "r--", r"%s" % HQ12[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(2, bin1_HQ10000_G0_8_2_005[4], "g--", r"%s" % HQ18[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(2, bin1_HQ10000_G1_2_5_005[4], "k--", r"%s" % HQ36[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange",
             ls="--", label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
    Plt(2, bin1_HQ10000_G1_2_9_005[5], "y--")
    Plt(2, bin1_HQ10000_G1_0_10_009[4], "m--", HQ70[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], "Violet", ls="--", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G1_0_0_000[4], "b:")  # label=r'$\gamma = -2.0$'
    data, _ = bin2_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G1_2_1_005[4], "r:")
    data, _ = bin2_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G0_8_2_005[4], "g:")
    data, _ = bin2_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G1_2_5_005[4], "k:")
    data = bin2_HQ10000_G1_2_5_005[5][0]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
    data = bin2_HQ10000_G1_2_9_005[4][0]
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
    data = bin3_HQ10000_G1_2_5_005[5][0]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
    data = bin3_HQ10000_G1_2_9_005[4][0]
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

    ax2.set_xlabel(r"$\log \left(|u_tn|,u_tp \right)$ and $\log \left(|u_rn|\
                     ,u_rp \right)$", fontsize=20)
    ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                   fontsize=20)

    # label=r'$\gamma = -1.5$'
    Plt(3, bin1_HQ10000_G1_0_0_000[0], "b--", r"%s" % HQ0[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(3, bin1_HQ10000_G1_2_1_005[0], "r--", r"%s" % HQ12[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(3, bin1_HQ10000_G0_8_2_005[0], "g--", r"%s" % HQ18[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(3, bin1_HQ10000_G1_2_5_005[0], "k--", r"%s" % HQ36[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange",
             ls="--", label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
    Plt(3, bin1_HQ10000_G1_2_9_005[1], "y--")
    Plt(3, bin1_HQ10000_G1_0_10_009[0], "m--", r"%s" % HQ70[len("HQ10000_G"):])
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

    ax3.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")

    # label=r'$\gamma = -1.5$'
    Plt(4, bin1_HQ10000_G1_0_0_000[4], "b--", r"%s" % HQ0[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(4, bin1_HQ10000_G1_2_1_005[4], "r--", r"%s" % HQ12[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(4, bin1_HQ10000_G0_8_2_005[4], "g--", r"%s" % HQ18[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(4, bin1_HQ10000_G1_2_5_005[4], "k--", r"%s" % HQ36[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange",
             ls="--", label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
    Plt(4, bin1_HQ10000_G1_2_9_005[5], "y--")
    Plt(4, bin1_HQ10000_G1_0_10_009[4], "m--", r"%s" % HQ70[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], "Violet", ls="--", lw=2, ms=7)
    Plt(4, bin2_HQ10000_G1_0_0_000[4], "b:")  # label=r'$\gamma = -2.0$'
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
    Plt(4, bin3_HQ10000_G1_0_0_000[4], "b-.")  # label=r'$\gamma = -2.5$'
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

    ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left(\
                     |u_rn|,u_rp \right)$", fontsize=20)
    ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right)\
                     \right)$", fontsize=20)
    ax4.set_yscale("log")

if Fig3b_GPerts_G1_2_same_gammas_as_IC_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
               frameon=True, loc=0, handlelength=2.5)")

    data, _ = bin1_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], "b--",
             label=r"%s" % HQ12[len("HQ10000_G"):], lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:, 0], data[:, 1], "r--",
             label=r"%s" % HQ24[len("HQ10000_G"):], lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], "g--",
             label=r"%s" % HQ36[len("HQ10000_G"):], lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], "k--",
             label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", ls="--",
             label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
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

    ax1.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
    ax1.set_title(r"Time evolution of files = %s" % HQ0[:-9], fontsize=20)

    Plt(2, bin1_HQ10000_G1_2_1_005[4], "r--", r"%s" % HQ12[len("HQ10000_G"):])
    Plt(2, bin1_HQ10000_G1_2_3_005[4], "g--", r"%s" % HQ24[len("HQ10000_G"):])
    Plt(2, bin1_HQ10000_G1_2_5_005[4], "k--", r"%s" % HQ36[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="--",
             label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", ls="--",
             label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
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

    ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left(\
                     |u_rn|,u_rp \right)$", fontsize=20)
    ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                   fontsize=20)

    Plt(3, bin1_HQ10000_G1_2_1_005[0], "r--", r"%s" % HQ12[len("HQ10000_G"):])
    Plt(3, bin1_HQ10000_G1_2_3_005[0], "g--", r"%s" % HQ24[len("HQ10000_G"):])
    Plt(3, bin1_HQ10000_G1_2_5_005[0], "k--", r"%s" % HQ36[len("HQ10000_G"):])
    data, _ = bin1_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls="--",
             label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", ls="--",
             label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
    Plt(3, bin2_HQ10000_G1_2_1_005[0], "r:")
    Plt(3, bin2_HQ10000_G1_2_3_005[0], "g:")
    Plt(3, bin2_HQ10000_G1_2_5_005[0], "k:")
    data = bin2_HQ10000_G1_2_7_005[0][0]
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

    ax3.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")

    Plt(4, bin1_HQ10000_G1_2_1_005[4], "r--", r"%s" % HQ12[len("HQ10000_G"):])
    Plt(4, bin1_HQ10000_G1_2_3_005[4], "g--", r"%s" % HQ24[len("HQ10000_G"):])
    Plt(4, bin1_HQ10000_G1_2_5_005[4], "k--", r"%s" % HQ36[len("HQ10000_G"):])
    data = bin1_HQ10000_G1_2_7_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="--",
             label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
    data = bin1_HQ10000_G1_2_9_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls="--",
             label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
    Plt(4, bin2_HQ10000_G1_2_1_005[4], "r:")
    Plt(4, bin2_HQ10000_G1_2_3_005[4], "g:")
    Plt(4, bin2_HQ10000_G1_2_5_005[4], "k:")
    data = bin2_HQ10000_G1_2_7_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
    data = bin2_HQ10000_G1_2_9_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)
    Plt(4, bin3_HQ10000_G1_2_1_005[4], "r-.")
    Plt(4, bin3_HQ10000_G1_2_3_005[4], "g-.")
    Plt(4, bin3_HQ10000_G1_2_5_005[4], "k-.")
    data = bin3_HQ10000_G1_2_7_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
    data = bin3_HQ10000_G1_2_9_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)
    Plt(4, bin4_HQ10000_G1_2_1_005[4], "r")
    Plt(4, bin4_HQ10000_G1_2_3_005[4], "g")
    Plt(4, bin4_HQ10000_G1_2_5_005[4], "k")
    data = bin4_HQ10000_G1_2_7_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
    data = bin4_HQ10000_G1_2_9_005[4][0]
    ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

    ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left(|u_rn|\
                     ,u_rp \right)$", fontsize=20)
    ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right)\
                     \right)$", fontsize=20)
    ax4.set_yscale("log")

if Fig4_GPerts_different_gammas_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    if test:
        for i in range(1, 5):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        Plt(1, bin1_different_gammas_HQ10000_G1_2_1_005[0],
            "b--", r"%s" % HQ12[len("HQ10000_G"):])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_3_005[0],
            "r--", r"%s" % HQ24[len("HQ10000_G"):])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_5_005[0],
            "g--", r"%s" % HQ36[len("HQ10000_G"):])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_7_005[0],
            "k--", r"%s" % HQ48[len("HQ10000_G"):])
        data = bin1_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls="--",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
        Plt(1, bin2_different_gammas_HQ10000_G1_2_1_005[0], "r:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_3_005[0], "g:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_5_005[0], "k:")
        data = bin2_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data = bin2_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)
        Plt(1, bin3_different_gammas_HQ10000_G1_2_1_005[0], "r-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_3_005[0], "g-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_5_005[0], "k-.")
        data = bin3_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data = bin3_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)
        Plt(1, bin4_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_5_005[0], "k")
        data = bin4_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data = bin4_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax1.set_xlabel(r"$u_t$", fontsize=20)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files=%s, different r bins"
                        % HQ0[:-9], fontsize=20)

        Plt(2, bin1_different_gammas_HQ10000_G1_2_1_005[4],
            "r--", r"%s" % HQ12[len("HQ10000_G"):])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_3_005[4],
            "g--", r"%s" % HQ24[len("HQ10000_G"):])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_5_005[4],
            "k--", r"%s" % HQ36[len("HQ10000_G"):])
        data = bin1_different_gammas_HQ10000_G1_2_7_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls="--",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_9_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls="--",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
        Plt(2, bin2_different_gammas_HQ10000_G1_2_1_005[4], "r:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_3_005[4], "g:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_5_005[4], "k:")
        data = bin2_different_gammas_HQ10000_G1_2_7_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
        data = bin2_different_gammas_HQ10000_G1_2_9_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)
        Plt(2, bin3_different_gammas_HQ10000_G1_2_1_005[4], "r-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_3_005[4], "g-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_5_005[4], "k-.")
        data = bin3_different_gammas_HQ10000_G1_2_7_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
        data = bin3_different_gammas_HQ10000_G1_2_9_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)
        Plt(2, bin4_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_5_005[4], "k")
        data = bin4_different_gammas_HQ10000_G1_2_7_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data = bin4_different_gammas_HQ10000_G1_2_9_005[4][0]
        ax2.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        # ax2.set_xlim(-3, 0)
        ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$",
                       fontsize=20)

        Plt(3, bin1_different_gammas_HQ10000_G1_2_1_005[0],
            "r--", r"%s" % HQ12[len("HQ10000_G"):])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_3_005[0],
            "g--", r"%s" % HQ24[len("HQ10000_G"):])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_5_005[0],
            "k--", r"%s" % HQ36[len("HQ10000_G"):])
        data = bin1_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Brown",
                 ls="--", label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Orange",
                 ls="--", label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
        Plt(3, bin2_different_gammas_HQ10000_G1_2_1_005[0], "r:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_3_005[0], "g:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_5_005[0], "k:")
        data = bin2_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
        data = bin2_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)
        Plt(3, bin3_different_gammas_HQ10000_G1_2_1_005[0], "r-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_3_005[0], "g-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_5_005[0], "k-.")
        data = bin3_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
        data = bin3_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)
        Plt(3, bin4_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_5_005[0], "k")
        data = bin4_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data = bin4_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax3.set_xlabel(r"$u_t$", fontsize=20)
        ax3.set_ylabel(r"$\log \left( f\left( u_t \right) \right)$",
                       fontsize=20)
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_HQ10000_G1_2_1_005[4],
            "r--", r"%s" % HQ12[len("HQ10000_G"):])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_3_005[4],
            "g--", r"%s" % HQ24[len("HQ10000_G"):])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_5_005[4],
            "k--", r"%s" % HQ36[len("HQ10000_G"):])
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", ls="--",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", ls="--",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)
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
        ax4.set_ylabel(r"$\log \left(f\left(\log\left(|u_tn|,u_tp\right)\
                         \right)\right)$", fontsize=20)
        ax4.set_yscale("log")

    if test2:
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0],
            "b--", r"%s" % test2_HQ0[len("test2_HQ10000_G"):])
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0],
            "r--", r"%s" % test2_HQ36[len("test2_HQ10000_G"):])
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0],
            "g--", r"%s" % test2_HQ66[len("test2_HQ10000_G"):])
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_15_005[0],
            "k--", r"%s" % test2_HQ96[len("test2_HQ10000_G"):])
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls="--",
                 label=r"%s" % test2_HQ126[len("test2_HQ10000_G"):],
                 lw=2, ms=7)
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0],
            "b--", r"%s" % test2_HQ159[len("test2_HQ10000_G"):])
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

        ax1.set_xlabel(r"$u_t$", fontsize=20)
        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins"
                        % test2_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

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
        ax2.set_ylabel(r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$",
                       fontsize=20)

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

        ax3.set_xlabel(r"$u_t$", fontsize=20)
        ax3.set_ylabel(r"$\log \left( f\left( u_t \right) \right)$",
                       fontsize=20)
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
        ax4.set_ylabel(r"$\log \left( f\left(\log\left(|u_tn|,u_tp\right)\
                         \right)\right)$", fontsize=20)
        ax4.set_yscale("log")

    if B:
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_0_000[0],
            "r--", r"%s" % B_HQ0[len("B_HQ10000_G"):])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_5_005[0],
            "g--", r"%s" % B_HQ36[len("B_HQ10000_G"):])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_10_005[0],
            "k--", r"%s" % B_HQ66[len("B_HQ10000_G"):])
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", ls="--",
                 label=r"%s" % B_HQ294[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", ls="--",
                 label=r"%s" % B_HQ382[len("B_HQ10000_G"):], lw=2, ms=7)
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

        ax1.set_xlabel(r"$u_t$", fontsize=20)
        ax1.set_ylabel(r"$f\left(u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins"
                      % B_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

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

        ax2.set_xlabel(r"$\log \left(|u_tn|,u_tp \right)$", fontsize=20)
        ax2.set_ylabel(r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$",
                       fontsize=20)

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

        ax3.set_xlabel(r"$u_t$", fontsize=20)
        ax3.set_ylabel(r"$\log \left( f\left( u_t \right) \right)$",
                       fontsize=20)
        ax3.set_yscale("log")

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

        ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax4.set_ylabel(r"$\log\left(f\left(\log\left(|u_tn|,u_tp\right)\right)\
                         \right)$", fontsize=20)
        ax4.set_yscale("log")

if Fig5a_GPerts_gammas_1_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

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

        ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -1.5$" % HQ0[:-9], fontsize=20)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % HQ12[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % HQ24[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % HQ36[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_7_005[4][0]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_9_005[4][0]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax4.set_ylabel(r"$\log \left( f\left(\log \left(|u_n|,u_p\right)\
                         \right)\right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-.5 * a ** 2)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$",
                       fontsize=20)

        def denom_ax6(a):
            return np.exp(-.5 * a ** 2)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_7_005[4][0]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data = bin1_different_gammas_HQ10000_G1_2_9_005[4][0]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {e^{-0.5x^2}}$", fontsize=20)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -1.5$" % test2_HQ0[:-9], fontsize=20)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s" % test2_HQ0[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % test2_HQ36[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % test2_HQ66[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % test2_HQ96[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % test2_HQ126[len("test2_HQ10000_G"):],
                 lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % test2_HQ159[len("test2_HQ10000_G"):],
                 lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left(|u_n|,u_p \right)\right)$",
                       fontsize=20)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax4.set_ylabel(r"$\log\left(f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2} }$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left(|u_tn|,u_tp \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                       fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                         \right)}{Tsallis}$", fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of %s, different r bins,\
                        $\gamma = -1.5$" % A_HQ0[:-9], fontsize=20)

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % A_HQ0[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % A_HQ36[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % A_HQ66[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % A_HQ246[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % A_HQ298[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % A_HQ382[len("A_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax4.set_ylabel(r"$\log \left( f\left(\log\left( |u_n|,u_p \right)\
                         \right)\right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of %s, different r bins,\
                        $\gamma = -1.5$" % B_HQ0[:-9], fontsize=20)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % B_HQ0[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % B_HQ36[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % B_HQ66[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % B_HQ294[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % B_HQ382[len("B_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-.930 * a ** 2)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                         e^{-0.930 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3452.955 * (10 ** a) ** 2 * np.exp(-.936 * (10 ** a) ** 2)

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (894.292 * a * (1 - (1 - .955) * .918 * a ** 2)
                    ** (.955 / (1 - .955)))

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        def denom_ax8(a):
            return (3418.569 * 10 ** a * (1 - (1 - .987) * .929
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left(|u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

if Fig5b_GPerts_gammas_2_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -2.0$" % HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % HQ12[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % HQ24[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % HQ36[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-.5 * a ** 2)

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$",
                       fontsize=20)

        def denom_ax6(a):
            return np.exp(-.5 * a ** 2)

        data, _ = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {e^{-0.5x^2}}$", fontsize=20)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -2.0$" % test2_HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % test2_HQ0[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % test2_HQ36[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % test2_HQ66[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % test2_HQ96[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % test2_HQ126[len("test2_HQ10000_G"):],
                 lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % test2_HQ159[len("test2_HQ10000_G"):],
                 lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                       fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of %s, different r bins,\
                        $\gamma = -2.0$" % A_HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % A_HQ0[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % A_HQ36[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % A_HQ66[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % A_HQ246[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % A_HQ298[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % A_HQ382[len("A_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                       fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of %s, different r bins,\
                        $\gamma = -2.0$" % B_HQ0[:-9], fontsize=20)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % B_HQ0[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % B_HQ36[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % B_HQ66[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % B_HQ294[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % B_HQ382[len("B_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-.930 * a ** 2)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                         e^{-0.930 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3452.955 * (10 ** a) ** 2 * np.exp(-.936 * (10 ** a) ** 2)

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (894.292 * a * (1 - (1 - .955) * .918 * a ** 2)
                    ** (.955 / (1 - .955)))

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3418.569 * 10 ** a * (1 - (1 - .987) * .929
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

if Fig5c_GPerts_gammas_2_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -2.5$" % HQ0[:-9], fontsize=20)

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % HQ12[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % HQ24[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % HQ36[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left(|u_n|, u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,\
                         u_p \right)\right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-.5 * a ** 2)

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$",
                         fontsize=20)

        def denom_ax6(a):
            return np.exp(-.5 * a ** 2)

        data, _ = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylabel(r"$\frac{f\left(\log \left(|u_n|,u_p \right)\right)}\
                         {e^{-0.5x^2}}$", fontsize=20)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -2.5$" % test2_HQ0[:-9], fontsize=20)

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % test2_HQ0[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % test2_HQ36[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % test2_HQ66[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % test2_HQ96[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % test2_HQ126[len("test2_HQ10000_G"):],
                 lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % test2_HQ159[len("test2_HQ10000_G"):],
                 lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                         fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left(|u_n|,\
                         u_p \right)\right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left(u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                         \right)}{3424.993 \cdot x^2 \cdot e^{-0.930\
                         \cdot x^2}}$", fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left(|u_tn|,u_tp\
                         \right)\right)}{Tsallis}$", fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of %s, different r bins,\
                        $\gamma = -2.5$" % A_HQ0[:-9], fontsize=20)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s" % A_HQ0[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % A_HQ36[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % A_HQ66[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % A_HQ246[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % A_HQ298[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % A_HQ382[len("A_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left(|u_n|,\
                         u_p \right)\right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\
                         \right)}{3424.993 \cdot x^2 \cdot e^{-0.930\
                         \cdot x^2 }}$", fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,\
                         u_tp \right)\right)}{Tsallis}$", fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of %s, different r bins,\
                        $\gamma = -2.5$" % B_HQ0[:-9], fontsize=20)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % B_HQ0[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % B_HQ36[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % B_HQ66[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % B_HQ294[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % B_HQ382[len("B_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,\
                         u_p \right)\right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-.930 * a ** 2)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                         e^{-0.930 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3452.955 * (10 ** a) ** 2 * np.exp(-.936 * (10 ** a) ** 2)

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,\
                         u_p \right)\right)}{3452.955 \cdot x^2\
                         \cdot e^{-0.936 \cdot x^2 }}$", fontsize=20)

        def denom_ax7(a):
            return (894.292 * a * (1 - (1 - .955) * .918 * a ** 2)
                    ** (.955 / (1 - .955)))

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3418.569 * 10 ** a * (1 - (1 - .987) * .929
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

if Fig5d_GPerts_gammas_3_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -3.0$" % HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % HQ12[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % HQ24[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % HQ36[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left(|u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log\left( f\left(\log \left(|u_n|,u_p\right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-.5 * a ** 2)

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$",
                       fontsize=20)

        def denom_ax6(a):
            return np.exp(-.5 * a ** 2)

        data, _ = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {e^{-0.5x^2}}$", fontsize=20)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -3.0$" % test2_HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % test2_HQ0[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % test2_HQ36[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % test2_HQ66[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % test2_HQ96[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % test2_HQ126[len("test2_HQ10000_G"):],
                 lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % test2_HQ159[len("test2_HQ10000_G"):],
                 lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left(|u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r"Time evolution of %s, different r bins, $\gamma = -3.0$"
            % A_HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % A_HQ0[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % A_HQ36[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % A_HQ66[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % A_HQ246[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % A_HQ298[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % A_HQ382[len("A_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left(|u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax3.set_ylabel(r"$\log \left( f\left(u \right) \right)$", fontsize=20)
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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)


        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                       fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)
        data, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of %s, different r bins,\
                        $\gamma=-3.0$" % B_HQ0[:-9], fontsize=20)

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % B_HQ0[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % B_HQ36[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % B_HQ66[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % B_HQ294[len("B_HQ10000_G"):], lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % B_HQ382[len("B_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-.930 * a ** 2)

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                         e^{-0.930 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3452.955 * (10 ** a) ** 2 * np.exp(-.936 * (10 ** a) ** 2)


        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (894.292 * a * (1 - (1 - .955) * .918
                    * a ** 2) ** (.955 / (1 - .955)))

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3418.569 * 10 ** a * (1 - (1 - .987) * .929
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                         \right)}{Tsallis}$", fontsize=20)

# datalist_bin5different_gammas_test2_HQ10000_G1_0_25_005

if Fig6a_GPerts_R_middle_19_95_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

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

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -1.5$" % HQ0[:-9], fontsize=20)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % HQ12[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % HQ24[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % HQ36[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left(|u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-.5 * a ** 2)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$",
                       fontsize=20)

        def denom_ax6(a):
            return np.exp(-.5 * a ** 2)

        data, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        data, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {e^{-0.5x^2}}$", fontsize=20)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, $R_{middle} = 19.95$"
                      % test2_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % test2_HQ0[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % test2_HQ66[len("test2_HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % test2_HQ166[len("test2_HQ10000_G"):],
                 lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                       fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                         \right)}{3424.993 \cdot x^2 \cdot\
                         e^{-0.930 \cdot x^2 }}$", fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u \right)}{Tsallis} $", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left(u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, $R_{middle} = 19.95$"
                      % A_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % A_HQ0[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % A_HQ66[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % A_HQ382[len("A_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                         fontsize=20)

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

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left(u_t \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)

        data, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                         \right)}{Tsallis}$", fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left(u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, $R_{middle} = 19.95$"\
                        % B_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % B_HQ0[len("B_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left(|u_n|,u_p \right)\right)$",
                         fontsize=20)

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2}}$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {Tsallis}$", fontsize=20)

if Fig6b_GPerts_R_middle_31_62_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, different r bins,\
                        $\gamma = -2.0$" % HQ0[:-9], fontsize=20)

        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % HQ12[len("HQ10000_G"):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "g",
                 label=r"%s" % HQ24[len("HQ10000_G"):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % HQ36[len("HQ10000_G"):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "Brown",
                 label=r"%s" % HQ48[len("HQ10000_G"):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "Orange",
                 label=r"%s" % HQ60[len("HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$",
                         fontsize=20)

        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)

        ax4.set_ylabel(r"$\log \left(f\left(\log \left(|u_n|,u_p \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-.5 * a ** 2)

        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "g", lw=2, ms=7)
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Brown", lw=2, ms=7)
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$",
                         fontsize=20)

        def denom_ax6(a):
            return np.exp(-.5 * a ** 2)

        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "g", lw=2, ms=7)
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Brown", lw=2, ms=7)
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "Orange", lw=2, ms=7)

        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                         {e^{-0.5x^2}}$", fontsize=20)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, $ R_{middle} = 31.62$"
                        % test2_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % test2_HQ0[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % test2_HQ66[len("HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % test2_HQ166[len("HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$",
                       fontsize=20)

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left( f\left( u_t \right) \right)$",
                       fontsize=20)
        ax3.set_yscale("log")

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax4.set_ylabel(r"$\log \left( f\left(\log \left(|u_tn|, u_tp\
                         \right)\right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u_t \right)}{887.569 \cdot x\
                         \cdot e^{-0.922 \cdot x^2} }$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                         {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
                         fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                         \right)}{Tsallis}$", fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left(u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, $R_{middle} = 31.62$"
                        % A_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s " % A_HQ0[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], "k",
                 label=r"%s" % A_HQ66[len("A_HQ10000_G"):], lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:, 0], data[:, 1], "b",
                 label=r"%s" % A_HQ382[len("A_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left(|u_tn|, u_tp \right)\right)$",
                         fontsize=20)

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left(f\left(u_t \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)

        ax4.set_ylabel(r"$\log \left(f\left(\log \left(|u_tn|, u_tp \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "b", lw=2, ms=7)

        ax5.set_ylabel(r"$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2} }$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "b", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left(|u_tn|, u_tp\
                         \right)\right)}\{3424.993 \cdot x^2 \cdot e^{-0.930\
                         \cdot x^2 }}$", fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7 )
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u_t \right)}{Tsallis}$", fontsize=20)

        def denom_ax7(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "k", lw=2, ms=7)
        data, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "b", lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|, u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                         \right)}{Tsallis}$", fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)")

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)

        ax1.set_ylabel(r"$f\left( u_t \right)$", fontsize=20)
        ax1.set_title(r"Time evolution of files = %s, $R_{middle} = 31.62$"\
                        % B_HQ0[:-9], fontsize=20)

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], "r",
                 label=r"%s" % B_HQ0[len("B_HQ10000_G"):], lw=2, ms=7)

        ax2.set_ylabel(r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$",
                       fontsize=20)

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)

        ax3.set_ylabel(r"$\log \left( f\left( u_t \right) \right)$",
                       fontsize=20)
        ax3.set_yscale("log")

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)

        ax4.set_ylabel(r"$\log \left( f\left(\log \left( |u_tn|, u_tp \right)\
                         \right) \right)$", fontsize=20)
        ax4.set_yscale("log")

        data, _ = datalist_largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_0_000[
            0
        ]

        def denom_ax5(a):
            return 887.569 * a * np.exp(-.922 * a ** 2)

        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]),
                 "r", lw=2, ms=7)
        ax5.set_ylabel(r"$\frac{f\left( u_t \right)}{887.569 \cdot x\
                         \cdot e^{-0.922 \cdot x^2} }$", fontsize=20)

        def denom_ax6(a):
            return 3424.993 * (10 ** a) ** 2 * np.exp(-.930 * (10 ** a) ** 2)

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / denom_ax6(data[:, 0]),
                 "r", lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                         \right)}{3424.993 \cdot x^2\cdot e^{-0.930\
                         \cdot x^2}}$", fontsize=20)

        def denom_ax7(a):
            return (864.543 * a * (1 - (1 - .946) * .908 * a ** 2)
                    ** (.946 / (1 - .946)))

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / denom_ax7(data[:, 0]),
                 "r", lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left( u_t \right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (3391.113 * 10 ** a * (1 - (1 - .987) * .924
                    * 10 ** (a ** 2)) ** (.987 / (1.0 - .987)))

        data, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / denom_ax8(data[:, 0]),
                 "r", lw=2, ms=7)
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(r"$\frac{f\left(\log \left( |u_tn|, u_tp\
                         \right)\right)}{Tsallis}$", fontsize=20)

plt.show()
