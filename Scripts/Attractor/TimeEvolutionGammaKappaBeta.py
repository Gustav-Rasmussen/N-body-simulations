# -*- coding: utf-8 -*-

# Standard library imports
import h5py
import os
import time

# Third party imports
import IPython
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import pylab
import seaborn as sns

# Local application imports
import colorsAndSymbols
from definePaths import *
import fileLsts as lsts

# Datasets below are structured with the following columns (ordered):
# lnr, beta, gamma, kappa, VR, r, sigmarad2, r_r2, rho.

# Switches for figures -------------------------------------------------

logr_rho_IC_Final_R32 = 0
log_r_r2_rho_IC_Final_R32 = 0
logr_rho = 0
log_r_r2_rho = 0

A = 0
B = 0
CS1CS2CS3 = 0
CS4CS5CS6 = 0
DS1D2 = 0
BCS4CS5CS6DS1D2 = 0
DS1D2_final_evolution = 0
DS1 = 0
D2 = 0
rfp_B = 0
rfp_CS4CS5CS6 = 0
rfp_DS1D2 = 0
rfp_BCS4CS5CS6DS1D2 = 0

Overplot_IC_Final = 0
beta_vs_gamma_plus_kappa = 0
Attractor_3D = 0
Time_evolution_beta_gamma_kappa = 0
Overplot_logr_gamma = 0
Overplot_ln_rdividedbyd3_gamma = 0
lnr_VR_IC_Final_50bins_20bins = 0
lnr_sigmarad2_IC_Final_50bins_20bins = 0
lnr_sigmarad2_vr_Final_50bins = 0
R_limit_10000_logr_sigmarad2_vr_Final_20bins = 0
R_limit_5000_lnr_sigmarad2_vr_Final_50bins = 0
R_limit_10000_logr_r_vr_IC_Final_20bins_50bins = 0
R_limit_10000_logr_r_ur_Final_20bins_50bins = 0
R_limit_10000_logr_ur_Final_20bins_50bins = 0
Overplot_logr_gamma_4_different_bins = 0  # Panel created
R_limit_10000_logr_vr_Final_rfp_50bins = 0  # Panel created

if logr_rho_IC_Final_R32:

    def Plt(i, x, y, cls):
        exec(f"ax{i}.plot({x}, np.log10({y}), '{cls}', lw=2, ms=7)")

    def Plt_label(i, x, y, cls, label):
        exec(f"ax{i}.plot({x}, np.log10({y}), '{cls}',\
               label='{label}', lw=2, ms=7)")

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    d, _ = datalist_A_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'r-o', 'A')
    d, _ = datalist_B_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'b-s', 'B')
    d, _ = datalist_CS4_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'k-<', 'CS4')
    d, _ = datalist_CS5_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'y--v', 'CS5')
    d, _ = datalist_CS6_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'g--*', 'CS6')
    d, _ = datalist_DS1_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'm--s', 'DS1')
    d, _ = datalist_Soft_D2_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'c--d', 'Soft_D2')
    d, _ = datalist_E_R32[0]
    Plt_label(1, d[:, 0], d[:, 8], 'r--.', 'E')

    ax1.set_title(r'IC ($I: \Delta G, R_{limit}=32$)', fontsize=30)
    ax1.set_xlabel(r'$\log r$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    leg = ax1.legend(prop=dict(size=18), numpoints=1, ncol=1, loc=0,
                     fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    d, _ = datalist_A_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'r-o')
    d, _ = datalist_B_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'b-s')
    d, _ = datalist_CS4_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'k-<')
    d, _ = datalist_CS5_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'y--v')
    d, _ = datalist_CS6_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'g--*')
    d, _ = datalist_DS1_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'm--s')
    d, _ = datalist_Soft_D2_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'c--d')
    d, _ = datalist_E_R32[1]
    Plt(2, d[:, 0], d[:, 8], 'r--.')

    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'logr_rho_IC_Final_R32.png')

if log_r_r2_rho_IC_Final_R32:

    def Plt(i, x, y, cls):
        exec(f"ax{i}.plot(np.log10({x}), np.log10({y}), '{cls}', lw=2, ms=7)")

    def Plt_label(i, x, y, cls, label):
        exec(f"ax{i}.plot(np.log10({x}), np.log10({y}), '{cls}',\
               label='{label}', lw=2, ms=7)")

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    d, _ = datalist_A_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'r-o', 'A')
    d, _ = datalist_B_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'b-s', 'B')
    d, _ = datalist_CS4_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'k-<', 'CS4')
    d, _ = datalist_CS5_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'y--v', 'CS5')
    d, _ = datalist_CS6_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'g--*', 'CS6')
    d, _ = datalist_DS1_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'm--s', 'DS1')
    d, _ = datalist_Soft_D2_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'c--d', 'Soft_D2')
    d, _ = datalist_E_R32[0]
    Plt_label(1, d[:, 7], d[:, 8], 'r--.', 'E')

    ax1.set_title(r'IC ($I: \Delta G, R_{limit}=32$)', fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    leg = ax1.legend(prop=dict(size=18), numpoints=1, ncol=1, loc=0,
                     fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    d, _ = datalist_A_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'r-o')
    d, _ = datalist_B_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'b-s')
    d, _ = datalist_CS4_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'k-<')
    d, _ = datalist_CS5_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'y--v')
    d, _ = datalist_CS6_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'g--*')
    d, _ = datalist_DS1_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'm--s')
    d, _ = datalist_Soft_D2_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'c--d')
    d, _ = datalist_E_R32[1]
    Plt(2, d[:, 7], d[:, 8], 'r--.')

    ax2.set_xlabel(r'$\log(\frac{r}{r_{-2}})$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'log_r_r2_rho_IC_Final_R32.png')

if logr_rho:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(1, 3):
        exec(f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                                  loc=0, fancybox=True, handlelength=2.5)")
        exec(f"leg.get_frame().set_alpha(.5)")

    for i in range(len(datalist_A_R10000_20bins)):
        d, label = datalist_A_R10000_20bins[i]
        a = label[22:-29]
        ax1.plot(d[:, 0], np.log10(d[:, 8]), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)

    ax1.set_xlabel(r'$\log r$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    ax1.set_title(r'Sim. I of A ($R_{limit}=10^4, 20$ bins)', fontsize=30)

    for i in range(len(datalist_B_R10000_20bins)):
        d, label = datalist_B_R10000_20bins[i]
        a = label[22:-29]
        ax2.plot(d[:, 0], np.log10(d[:, 8]), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)

    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.set_title('Sim. I of B', fontsize=30)
    # ax2.tick_params(axis='both', which='both', bottom='on', top='off',
    #                 labelbottom='on', right='off', left='on',
    #                 labelleft='on')
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'logr_rho.png')

if log_r_r2_rho:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(1, 3):
        exec(f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                                  loc=0, fancybox=True, handlelength=2.5)")
        exec(f"leg.get_frame().set_alpha(.5)")

    for i in range(len(datalist_A_R10000_20bins)):
        d, label = datalist_A_R10000_20bins[i]
        a = label[22:-29]
        ax1.plot(np.log10(d[:, 7]), np.log10(d[:, 8]),
                 Symbols[i], color=Colors[i], label=a, lw=2, ms=7)
    ax1.set_xlabel(r'$\log(\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    ax1.set_title(r'Sim. I of A ($R_{limit}=10^4, 20$ bins)', fontsize=30)

    for i in range(len(datalist_B_R10000_20bins)):
        d, label = datalist_B_R10000_20bins[i]
        a = label[22:-29]
        ax2.plot(np.log10(d[:, 7]), np.log10(d[:, 8]),
                 Symbols[i], color=Colors[i], label=a, lw=2, ms=7)
    ax2.set_xlabel(r'$\log(\frac{r}{r_{-2}})$', fontsize=30)
    ax2.set_title('Sim. I of B', fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'log_r_r2_rho.png')

if Overplot_IC_Final:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    for i in range(len(datalist_Martin_IC)):
        d, label = datalist_Martin_IC[i]
        ax1.plot(d[:, 0], d[:, 1], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(len(datalist_Martin_Final) - 1):
        d, label = datalist_Martin_Final[i]
        ax1.plot(d[:, 4], d[:, 5], Symbols[i], color=Colors2[i],
                 label=label, lw=2, ms=7)
    d, label = datalist_Martin_Final[7]
    ax1.plot(d[:, 0], d[:, 1], 'r--.', label=label, lw=2, ms=7)
    ax1.title('IC and Final', fontsize=20)
    ax1.xlabel(r'$\beta$', fontsize=24)
    ax1.ylabel(r'$\gamma$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=4, handlelength=2.5)

    for i in range(len(datalist_Martin_IC)):
        d, label = datalist_Martin_IC[i]
        ax2.plot(d[:, 0], d[:, 2], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(len(datalist_Martin_Final) - 1):
        d, label = datalist_Martin_Final[i]
        ax2.plot(d[:, 4], d[:, 6], Symbols[i], color=Colors2[i], label=label,
                 lw=2, ms=7)
    d, label = datalist_Martin_Final[7]
    ax2.plot(d[:, 0], d[:, 2], 'r--.', label=label, lw=2, ms=7)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=4, handlelength=2.5)
    ax2.title('IC and Final', fontsize=20)
    ax2.xlabel(r'$\beta$', fontsize=24)
    ax2.ylabel(r'$\kappa$', fontsize=24)
    f.savefig(figurePath + 'Overplot_IC_Final.png')

if beta_vs_gamma_plus_kappa:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    for i in range(len(datalist_Martin_IC)):
        d, label = datalist_Martin_IC[i]
        ax1.plot(d[:, 0], d[:, 1] + d[:, 2], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    ax1.title('IC', fontsize=20)
    ax1.xlabel(r'$\beta$', fontsize=24)
    ax1.ylabel(r'$\gamma + \kappa$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(len(datalist_Martin_Final) - 1):
        d, label = datalist_Martin_Final[i]
        ax2.plot(d[:, 4], d[:, 5] + d[:, 6], Symbols[i], color=Colors2[i],
                 label=label, lw=2, ms=7)
    d, label = datalist_Martin_Final[7]
    ax2.plot(d[:, 0], d[:, 1] + d[:, 2], 'r--.', label=label, lw=2, ms=7)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)
    ax2.title('Final', fontsize=20)
    ax2.xlabel(r'$\beta$', fontsize=24)
    ax2.ylabel(r'$\gamma + \kappa$', fontsize=24)
    f.savefig(figurePath + 'beta_vs_gamma_plus_kappa.png')

if Attractor_3D:  # 3D plots of attractor, IC and Final.
    f = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    n = 100
    for i in range(len(datalist_Martin_IC)):
        d, label = datalist_Martin_IC[i]
        ax.scatter(d[:, 0], d[:, 1], d[:, 2], Symbols[i], color=Colors[i],
                   label=label, lw=2, ms=7)
    ax.set_xlabel(r'$2 \beta$')
    ax.set_ylabel(r'$\gamma$')
    ax.set_zlabel(r'$\kappa$')
    ax.set_title('3D view of attractor')
    f.savefig(figurePath + 'Attractor_3D.png')

if Time_evolution_beta_gamma_kappa:
    # Python 3.x: small greek letters are coded from 945 to 969,
    # so alpha is chr(945), omega is chr(969).

    def figure(sim):
        f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 11))
        f.subplots_adjust(hspace=0, wspace=0)
        exec(f"for i in range(len(datalist_{sim})):")
        exec(f"    d, label = datalist_{sim}[i]")
            ax1.plot(d[:, 0], d[:, 1], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        ax1.xlabel(r'$\log r$', fontsize=24)
        ax1.ylabel(f"{chr(946)}", fontsize=24)

        exec(f"for i in range(len(datalist_{sim})):")
        exec(f"    d, label = datalist_{sim}[i]")
            ax2.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        ax2.title(f"Time evolution of {chr(946)}, {chr(947)} and {chr(954)}\
                  for Simulation {sim}", fontsize=20)
        ax2.xlabel(r'$\log r$', fontsize=24)
        ax2.ylabel(f"{chr(947)}", fontsize=24)

        exec(f"for i in range(len(datalist_{sim})):")
        exec(f"    d, label = datalist_{sim}[i]")
            ax3.plot(d[:, 0], d[:, 3], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        ax3.xlabel(r'$\log r$', fontsize=24)
        ax3.ylabel(f"{chr(954)}", fontsize=24)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + f"{sim}_Time_evolution_beta_gamma_kappa.png")

    if A:
        figure('A')
    if B:
        figure('B')

if Overplot_logr_gamma:
    # Plot structures for R = 10000, except for CS1, CS2 and CS3
    f = plt.figure()
    if CS1CS2CS3:
        # Does the same as the line just above:
        # loop over 1.st to 5.th datafile and label.
        for i in range(6):
            d, label = datalist_C_IC[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.title(r'$\gamma$ for CS1, CS2 and CS3', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'$\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'CS1CS2CS3_Overplot_logr_gamma.png')

    if CS4CS5CS6:
        plt.subplot(121)
        for i in range(len(datalist_CS4CS5CS6_IC_R10000)):
            d, label = datalist_CS4CS5CS6_IC_R10000[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.title(r'Time evolution of $\gamma$ for CS4, CS5 and CS6', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Initial $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        plt.subplot(122)
        for i in range(len(datalist_CS4CS5CS6_Final)):
            d, label = datalist_CS4CS5CS6_Final[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'CS4CS5CS6_Overplot_logr_gamma.png')

    if DS1D2:
        plt.subplot(121)
        for i in range(len(datalist_DS1D2_IC_R10000)):
            d, label = datalist_DS1D2_IC_R10000[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.title(r'Time evolution of $\gamma$ for DS1 and D2', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Initial $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        plt.subplot(122)
        for i in range(len(datalist_DS1D2_Final_R10000)):
            d, label = datalist_DS1D2_Final_R10000[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'DS1D2_Overplot_logr_gamma.png')

    if BCS4CS5CS6DS1D2:

        plt.subplot(121)
        for i in range(len(datalist_CS4CS5CS6_IC_R10000)):
            d, label = datalist_CS4CS5CS6_IC_R10000[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i - 3],
                     color=Colors[i-3], label=label, lw=2, ms=7)
        for i in range(2):
            d, label = datalist_DS1D2_IC[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        data, label = FileLstB_IC_R10000[0]
        plt.plot(data[:, 0], data[:, 2], 'k-<', label=label, lw=2, ms=7)

        plt.title(r'Time evolution of $\gamma$\
                  for B, CS4, CS5, CS6, DS1 and D2', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Initial $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        plt.subplot(122)
        for i in range(3):
            d, label = datalist_C_Final[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(2):
            d, label = datalist_DS1D2_Final[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i + 3],
                     color=Colors[i + 3], label=label, lw=2, ms=7)
        data, label = FileLstB_Final_R10000[0]
        plt.plot(data[:, 0], data[:, 2], 'm--s', label=label, lw=2, ms=7)

        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)
        f.savefig(figurePath + 'BCS4CS5CS6DS1D2_Overplot_logr_gamma.png')

    if DS1D2_final_evolution:
        plt.subplot(221)
        d, _ = datalist_13[0]
        plt.plot(d[:, 0], d[:, 2], 'r-o', label='DS1, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[0]
        plt.plot(d[:, 0], d[:, 2], 'b-s', label='DS1, run 49_093', lw=2, ms=7)
        plt.title(r'Time evolution of $\gamma $ for DS1 and D2. 50 bins',
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        plt.subplot(222)
        d, _ = datalist_13[1]
        plt.plot(d[:, 0], d[:, 2], 'k-<', label='D2, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[1]
        plt.plot(d[:, 0], d[:, 2], 'y--v', label='D2, run 49_093', lw=2, ms=7)
        plt.title('50 bins', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        plt.subplot(223)
        d, _ = datalist_13[2]
        plt.plot(d[:, 0], d[:, 2], 'r-o', label='DS1, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[2]
        plt.plot(d[:, 0], d[:, 2], 'b-s', label='DS1, run 49_093', lw=2, ms=7)
        plt.title('20 bins', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        plt.subplot(224)
        d, _ = datalist_13[3]
        plt.plot(d[:, 0], d[:, 2], 'k-<', label='D2, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[3]
        plt.plot(d[:, 0], d[:, 2], 'y--v', label='D2, run 49_093', lw=2, ms=7)
        plt.title('20 bins', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)
        f.savefig(figurePath + 'DS1D2_final_evolution_Overplot_logr_gamma.png')

    if rfp_B:
        data, label = datalist_9b[0]
        plt.plot(data[:, 0], data[:, 2], 'r-o', label=label, lw=2, ms=7)
        data, label = datalist_17[0]
        plt.plot(data[:, 0], data[:, 2], 'b-s', label=label, lw=2, ms=7)
        plt.ylim(-4, 1)
        plt.title(r'$\gamma$ for B Final product,\
                  with bound structure (50 bins)', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'rfp_B_Overplot_logr_gamma.png')

    if rfp_CS4CS5CS6:
        for i in range(3):
            d, label = datalist_11[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(1, 4):
            d, label = datalist_17[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i + 2],
                     color=Colors[i + 2], label=label, lw=2, ms=7)
        plt.ylim(-4, 1)
        plt.title(r'$\gamma$ for CS4, CS5 and CS6 Final products,\
                  with bound structures (50 bins)', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'rfp_CS4CS5CS6_Overplot_logr_gamma.png')

    if rfp_DS1D2:
        for i in range(2):
            d, label = datalist_13b[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(4, 6):
            d, label = datalist_17[i]
            plt.plot(d[:, 0], d[:, 2], Symbols[i - 2],
                     color=Colors[i - 2], label=label, lw=2, ms=7)
        plt.ylim(-4, 1)
        plt.title(r'$\gamma$ for DS1 and D2 Final products,\
                  with bound structures (50 bins)', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'rfp_DS1D2_Overplot_logr_gamma.png')

    if rfp_BCS4CS5CS6DS1D2:
        f, (ax1, ax2, ax3) = plt.subplots(3, 1)

        for i in range(1, 4):
            exec(f"ax{i}.set_ylim(-4, 1)")
            exec(f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                                      loc=0, fancybox=True, handlelength=2.5)")
            exec(f"leg.get_frame().set_alpha(.5)")

        for i in range(1, 3):
            exec(f"ax{i}.axes.get_xaxis().set_visible(False)")

        data, label = datalist_9b[0]
        ax1.plot(data[:, 0], data[:, 2], 'r-o', label=label, lw=2, ms=7)
        data, label = datalist_17[0]
        ax1.plot(data[:, 0], data[:, 2], 'b-s', label=label, lw=2, ms=7)

        ax1.set_title(r'$\gamma$ for Final products,\
                      with bound structure (50 bins)', fontsize=20)
        ax1.set_ylabel('B', fontsize=24)

        for i in range(3):
            d, label = datalist_11[i]
            ax2.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(1, 4):
            d, label = datalist_17[i]
            ax2.plot(d[:, 0], d[:, 2], Symbols[i + 2],
                     color=Colors[i + 2], label=label, lw=2, ms=7)
        ax2.set_ylabel('CS4, CS5 and CS6', fontsize=24)

        for i in range(2):
            d, label = datalist_13b[i]
            ax3.plot(d[:, 0], d[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(4, 6):
            d, label = datalist_17[i]
            ax3.plot(d[:, 0], d[:, 2], Symbols[i - 2],
                     color=Colors[i - 2], label=label, lw=2, ms=7)
        ax3.set_xlabel(r'$\log r$', fontsize=24)
        ax3.set_ylabel('DS1 and D2', fontsize=24)
        f.savefig(figurePath + 'rfp_BCS4CS5CS6DS1D2_Overplot_logr_gamma.png')

if Overplot_ln_rdividedbyd3_gamma:
    f = plt.figure()

    # Below are only Final files with 50 radial bins.
    d_lst = [(0, 'd1'), (0, 'd2'), (0, 'd3')]
    p_lst = [(0, 'p1'), (0, 'p2'), (0, 'p3')]

    CS4_minima_lst = d_lst
    CS4_maxima_lst = p_lst
    CS5_minima_lst = d_lst
    CS5_maxima_lst = p_lst
    CS6_minima_lst = d_lst
    CS6_maxima_lst = p_lst
    DS1_minima_lst = d_lst
    DS1_maxima_lst = p_lst
    D2_minima_lst = [(0, 'd1'), (0, 'd2'), (-3.705065011901715444, 'd3')]
    D2_maxima_lst = p_lst

    d, label = datalist_6[0]
    v, _ = CS4_minima_lst[2]
    plt.plot(np.log(d[:, 5] / -v), d[:, 2], 'r-o', label=label, lw=2, ms=7)
    d, label = datalist_6[1]
    v, _ = CS5_minima_lst[2]
    plt.plot(np.log(d[:, 5] / -v), d[:, 2], 'b-s', label=label, lw=2, ms=7)
    d, label = datalist_6[2]
    v, _ = CS6_minima_lst[2]
    plt.plot(np.log(d[:, 5] / -v), d[:, 2], 'k-<', label=label, lw=2, ms=7)
    d, label = datalist_8[0]
    v, _ = DS1_minima_lst[2]
    plt.plot(np.log(d[:, 5] / -v), d[:, 2], 'y--v', label=label, lw=2, ms=7)
    d, label = datalist_8[1]
    v, _ = D2_minima_lst[2]
    plt.plot(np.log(d[:, 5] / -v), d[:, 2], 'g--*', label=label, lw=2, ms=7)

    plt.title(r'Final $\gamma$ for CS4, CS5, CS6, DS1 and D2', fontsize=20)
    plt.xlabel(r'$\log\frac{r}{|d_3|}$', fontsize=24)
    plt.ylabel(r'Final $\gamma$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'Overplot_ln_rdividedbyd3_gamma.png')

if lnr_VR_IC_Final_50bins_20bins:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    for i in range(6, 9):
        d, label = datalist_5[i]
        ax1.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2):
        d, label = datalist_7[i]
        ax1.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    ax1.title(r'Time evolution of $v_r$,\
              Sim CS4, CS5, CS6, DS1 and D2. 50 bins', fontsize=20)
    ax1.xlabel(r'$\log r$', fontsize=24)
    ax1.ylabel(r'Initial $v_r$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_6[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2):
        d, label = datalist_8[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    ax2.xlabel(r'$\log r$', fontsize=24)
    ax2.ylabel(r'Final $v_r$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(9, 12):
        d, label = datalist_5[i]
        ax3.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_7[i]
        ax3.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    ax3.title('20 bins', fontsize=20)
    ax3.xlabel(r'$\log r$', fontsize=24)
    ax3.ylabel(r'IC $v_r$', fontsize=24)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3, 6):
        d, label = datalist_6[i]
        ax4.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_8[i]
        ax4.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    ax4.xlabel(r'$\log r$', fontsize=24)
    ax4.ylabel(r'Final $v_r$', fontsize=24)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'lnr_VR_IC_Final_50bins_20bins.png')

if lnr_sigmarad2_IC_Final_50bins_20bins:

    title_str = f"Time evolution of {chr(946)}, {chr(947)} and {chr(954)}\
                for Simulation DS1 and D2"

    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    # 50 bins
    for i in range(6, 9):
        d, label = datalist_5[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2):
        d, label = datalist_7[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    ax1.title(r'Time evolution of $\sigma_r^2$\
              for Simulation CS4, CS5, CS6, DS1 and D2', fontsize=20)
    ax1.xlabel(r'$\log r$', fontsize=24)
    ax1.ylabel(r'IC $\sigma_r^2$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # 50 bins
    for i in range(3):
        d, label = datalist_6[i]
        ax2.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2):
        d, label = datalist_8[i]
        ax2.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    # ax2.title(title_str, fontsize=20)
    ax2.xlabel(r'$\log r$', fontsize=24)
    ax2.ylabel(r'Final $\sigma_r^2$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # 20 bins
    for i in range(9, 12):
        d, label = datalist_5[i]
        ax3.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_7[i]
        ax3.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    # ax3.title(title_str, fontsize=20)
    ax3.xlabel(r'$\log r$', fontsize=24)
    ax3.ylabel(r'IC $\sigma_r^2$', fontsize=24)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # 20 bins
    for i in range(3, 6):
        d, label = datalist_6[i]
        ax4.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_8[i]
        ax4.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    # ax4.title(title_str, fontsize=20)
    ax4.xlabel(r'$\log r$', fontsize=24)
    ax4.ylabel(r'Final $ \sigma_r^2 $', fontsize=24)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'lnr_sigmarad2_IC_Final_50bins_20bins.png')

if lnr_sigmarad2_vr_Final_50bins:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    for i in range(3):
        d, label = datalist_6[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2):
        d, label = datalist_8[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i + 3], color=Colors[i + 3],
                 label=label, lw=2, ms=7)
    d, label = datalist_4[4]
    ax1.plot(d[:, 0], d[:, 6], Symbols[5], color=Colors[5],
             label=label, lw=2, ms=7)
    ax1.title(r'Final $\sigma_r^2$\
              for Sim B, CS4, CS5, CS6, DS1 and D2', fontsize=20)
    ax1.xlabel(r'$\log r$', fontsize=24)
    ax1.ylabel(r'Final $\sigma_r^2$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_6[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i],
                 color=Colors[i], label=label, lw=2, ms=7)
    for i in range(2):
        d, label = datalist_8[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i + 3],
                 color=Colors[i + 3], label=label, lw=2, ms=7)
    d, label = datalist_4[4]
    ax2.plot(d[:, 0], d[:, 4], Symbols[5], color=Colors[5], label=label, lw=2,
             ms=7)
    ax2.title(r'Final $v_r$ for Simulation B, CS4, CS5, CS6, DS1 and D2',
              fontsize=20)
    ax2.xlabel(r'$\log r$', fontsize=24)
    ax2.ylabel(r'Final $v_r$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'lnr_sigmarad2_vr_Final_50bins.png')

if R_limit_10000_logr_sigmarad2_vr_Final_20bins:
    f, (ax1, ax2) = plt.subplots(2, 1)
    # CS4, CS5, CS6: datalist_10 (IC), datalist_11 (Final)
    for i in range(3, 6):
        d, label = datalist_11[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    # DS1, D2: datalist_12 (IC), datalist_13 (Final)
    for i in range(2, 4):
        d, label = datalist_13[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i - 2], color=Colors[i - 2],
                 label=label, lw=2, ms=7)
    # B: datalist_9 (Final)
    d, label = datalist_9[1]
    ax1.plot(d[:, 0], d[:, 6], Symbols[2], color=Colors[2], label=label, lw=2,
             ms=7)
    ax1.set_title(r'Final B, CS4, CS5, CS6, DS1 and D2.\
                  $R_{limit} = 10^4$. 20 bins', fontsize=20)
    ax1.set_ylabel(r'$\sigma_r^2$', fontsize=24)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(3, 6):
        d, label = datalist_11[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_13[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i - 2], color=Colors[i - 2],
                 label=label, lw=2, ms=7)
    d, label = datalist_9[1]
    ax2.plot(d[:, 0], d[:, 4], Symbols[2], color=Colors[2], label=label, lw=2,
             ms=7)
    ax2.set_xlabel(r'$\log r$', fontsize=24)
    ax2.set_ylabel(r'$v_r$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'R_limit_10000_logr_sigmarad2_vr_Final_20bins.png')

if R_limit_5000_lnr_sigmarad2_vr_Final_50bins:
    f, (ax1, ax2) = plt.subplots(2, 1)
    # CS4,CS5,CS6: datalist_15 (Final)
    for i in range(3):
        d, label = datalist_15[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # DS1,D2: datalist_16 (Final)
    for i in range(2):
        d, label = datalist_16[i]
        ax1.plot(d[:, 0], d[:, 6], Symbols[i + 3], color=Colors[i + 3],
                 label=label, lw=2, ms=7)
    # B: datalist_14 (Final)
    d, label = datalist_14[0]
    ax1.plot(d[:, 0], d[:, 6], 'm--s', label=label, lw=2, ms=7)
    ax1.title(r'Sim B, CS4, CS5, CS6, DS1 and D2.\
              $R_{limit} = 5 \cdot 10^3$. 50 bins', fontsize=20)
    ax1.xlabel(r'$\log r$', fontsize=24)
    ax1.ylabel(r'Final $\sigma_r^2$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_15[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=label,
                 lw=2, ms=7)
    for i in range(2):
        d, label = datalist_16[i]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i + 3], color=Colors[i + 3],
                 label=label, lw=2, ms=7)
    data, label = datalist_14[0]
    ax2.plot(data[:, 0], data[:, 4], 'm--s', label=label, lw=2, ms=7)
    # ax2.title(r'Final $v_r $ for Simulation B, CS4, CS5, CS6, DS1 and D2',
    #           fontsize=20)
    ax2.xlabel(r'$\log r$', fontsize=24)
    ax2.ylabel(r'Final $v_r$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'R_limit_5000_lnr_sigmarad2_vr_Final_50bins.png')

if R_limit_10000_logr_r_vr_IC_Final_20bins_50bins:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    for i in range(3, 6):
        d, label = datalist_11[i]
        a = label[:-62]
        ax1.plot(d[:, 5], d[:, 4], Symbols[i], color=Colors[i], label=a, lw=2,
                 ms=7)
    for i in range(2, 4):
        d, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        ax1.plot(d[:, 5], d[:, 4], Symbols[i - 1], color=Colors[i - 1],
                 label=a, lw=2, ms=7)
    d, label = datalist_9[1]
    a = label[:-57]
    ax1.plot(d[:, 5], d[:, 4], 'r-o', label=a, lw=2, ms=7)
    ax1.title(r'Final, $R_{limit} = 10^4$, 20 bins', fontsize=20)
    ax1.xlabel('r', fontsize=24)
    ax1.ylabel(r'$v_r$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3, 6):
        d, label = datalist_11[i]
        a = label[:-62]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=a, lw=2,
                 ms=7)
    for i in range(2, 4):
        d, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i - 1], color=Colors[i - 1],
                 label=a, lw=2, ms=7)
    d, label = datalist_9[1]
    a = label[:-57]
    ax2.plot(d[:, 0], d[:, 4], 'r-o', label=a, lw=2, ms=7)
    ax2.title('20 bins', fontsize=20)
    ax2.xlabel(r'$\log r$', fontsize=24)
    ax2.ylabel(r'$v_r$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_11[i]
        a = label[:-47]
        ax3.plot(d[:, 5], d[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(2):
        d, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        ax3.plot(d[:, 5], d[:, 4], Symbols[i + 3], color=Colors[i + 3],
                 label=a, lw=2, ms=7)
    d, label = datalist_9[0]
    a = label[:-42]
    ax3.plot(d[:, 5], d[:, 4], 'm--s', label=a, lw=2, ms=7)
    ax3.title('50 bins', fontsize=20)
    ax3.xlabel('r', fontsize=24)
    ax3.ylabel(r'$v_r$', fontsize=24)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_11[i]
        a = label[:-47]
        ax4.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=a, lw=2,
                 ms=7)
    for i in range(2):
        d, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        ax4.plot(d[:, 0], d[:, 4], Symbols[i + 3], color=Colors[i + 3],
                 label=a, lw=2, ms=7)
    d, label = datalist_9[0]
    a = label[:-42]
    ax4.plot(d[:, 0], d[:, 4], 'm--s', label=a, lw=2, ms=7)
    ax4.title('50 bins', fontsize=20)
    ax4.xlabel(r'$\log r$', fontsize=24)
    ax4.ylabel(r'$v_r$', fontsize=24)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath
              + 'R_limit_10000_logr_r_vr_IC_Final_20bins_50bins.png')

if R_limit_10000_logr_r_ur_Final_20bins_50bins:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    for i in range(3, 6):
        d, label = datalist_11[i]
        a = label[:-62]
        ax1.plot(d[:, 5], d[:, 4] / (d[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        ax1.plot(d[:, 5], d[:, 4] / (d[:, 6] ** .5), Symbols[i - 1],
                 color=Colors[i - 1], label=a, lw=2, ms=7)
    d, label = datalist_9[1]
    a = label[:-57]
    ax1.plot(d[:, 5], d[:, 4] / (d[:, 6] ** .5), 'r-o', label=a, lw=2, ms=7)
    ax1.title(r'Final, $R_{limit} = 10^4$, 20 bins', fontsize=20)
    ax1.xlabel('r', fontsize=24)
    ax1.ylabel(r'$u_r$', fontsize=24)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3, 6):
        d, label = datalist_11[i]
        a = label[:-62]
        ax2.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        ax2.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i - 1],
                 color=Colors[i - 1], label=a, lw=2, ms=7)
    d, label = datalist_9[1]
    a = label[:-57]
    ax2.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), 'r-o', label=a, lw=2, ms=7)
    ax2.title('20 bins', fontsize=20)
    ax2.xlabel(r'$\log r$', fontsize=24)
    ax2.ylabel(r'$u_r$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_11[i]
        a = label[:-47]
        ax3.plot(d[:, 5], d[:, 4] / (d[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2):
        d, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        ax3.plot(d[:, 5], d[:, 4] / (d[:, 6] ** .5), Symbols[i + 3],
                 color=Colors[i + 3], label=a, lw=2, ms=7)
    d, label = datalist_9[0]
    a = label[:-42]
    ax3.plot(d[:, 5], d[:, 4] / (d[:, 6] ** .5), 'm--s', label=a, lw=2, ms=7)
    ax3.title('50 bins', fontsize=20)
    ax3.xlabel('r', fontsize=24)
    ax3.ylabel(r'$u_r$', fontsize=24)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_11[i]
        a = label[:-47]
        ax4.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2):
        d, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        ax4.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i + 3],
                 color=Colors[i + 3], label=a, lw=2, ms=7)
    d, label = datalist_9[0]
    a = label[:-42]
    ax4.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), 'm--s', label=a, lw=2, ms=7)
    ax4.title('50 bins', fontsize=20)
    ax4.xlabel(r'$\log r$', fontsize=24)
    ax4.ylabel(r'$u_r$', fontsize=24)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'R_limit_10000_logr_r_ur_Final_20bins_50bins.png')

if R_limit_10000_logr_ur_Final_20bins_50bins:
    # subplot 2,4 are reused from previous figure.
    # changes:
    # datalist9 -> datalist9b,
    # datalist_11 -> ? datalist_11b ?,
    # datalist_13 -> datalist_13b.
    f, (ax1, ax2) = plt.subplots(2, 1)
    for i in range(3, 6):
        d, label = datalist_11[i]
        a = label[:-62]
        ax1.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2, 4):
        d, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        ax1.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i - 1],
                 color=Colors[i - 1], label=a, lw=2, ms=7)
    d, label = datalist_9b[1]
    a = label[:-57]
    ax1.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), 'r-o', label=a, lw=2, ms=7)
    ax1.title(r'Final, $R_{limit} = 10^4$, 20 bins', fontsize=20)
    ax1.xlabel(r'$\log r$', fontsize=24)
    ax1.ylabel(r'$u_r$', fontsize=24)
    ax1.xlim(-1, 2)
    ax1.ylim(-.2, .2)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_11[i]
        a = label[:-47]
        ax2.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2):
        d, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        ax2.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), Symbols[i + 3],
                 color=Colors[i + 3], label=a, lw=2, ms=7)
    d, label = datalist_9b[0]
    a = label[:-42]
    ax2.plot(d[:, 0], d[:, 4] / (d[:, 6] ** .5), 'm--s', label=a, lw=2, ms=7)
    ax2.title('50 bins', fontsize=20)
    ax2.xlabel(r'$\log r$', fontsize=24)
    ax2.ylabel(r'$u_r$', fontsize=24)
    ax2.xlim(-1, 2)
    ax2.ylim(-.2, .2)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'R_limit_10000_logr_ur_Final_20bins_50bins.png')

if Overplot_logr_gamma_4_different_bins:
    f, ((ax1, ax5), (ax2, ax6), (ax3, ax7), (ax4, ax8)) = plt.subplots(4, 2)
    if DS1D2:
        for i in [1, 2, 3, 5, 6, 7]:
            exec(f"ax{i}.axes.get_xaxis().set_visible(False)")
        for i in range(1, 9):
            exec(f"ax{i}.set_ylim(-5, 1)")
        for i in range(5, 9):
            exec(f"ax{i}.yaxis.tick_right()")
        d, _ = datalist_13[2]
        ax1.plot(d[:, 0], d[:, 2], 'r-o', label='DS1, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[2]
        ax1.plot(d[:, 0], d[:, 2], 'b-s', label='DS1, run 49_093', lw=2, ms=7)
        ax1.set_title(r'Time evolution of $\gamma$ for Sim DS1', fontsize=20)
        ax1.set_ylabel(r'20 bins', fontsize=24)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        d, _ = datalist_13[0]
        ax2.plot(d[:, 0], d[:, 2], 'r-o', label='DS1, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[0]
        ax2.plot(d[:, 0], d[:, 2], 'b-s', label='DS1, run 49_093', lw=2, ms=7)
        ax2.set_ylabel('50 bins', fontsize=24)

        d, _ = datalist_13[4]
        ax3.plot(d[:, 0], d[:, 2], 'r-o', label='DS1, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[4]
        ax3.plot(d[:, 0], d[:, 2], 'b-s', label='DS1, run 49_093', lw=2, ms=7)
        ax3.set_ylabel('100 bins', fontsize=24)

        d, _ = datalist_13[6]
        ax4.plot(d[:, 0], d[:, 2], 'r-o', label='DS1, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[6]
        ax4.plot(d[:, 0], d[:, 2], 'b-s', label='DS1, run 49_093', lw=2, ms=7)
        ax4.set_ylabel('200 bins', fontsize=24)

        d, _ = datalist_13[3]
        ax5.plot(d[:, 0], d[:, 2], 'r-o', label='D2, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[3]
        ax5.plot(d[:, 0], d[:, 2], 'b-s', label='D2, run 49_093', lw=2, ms=7)
        ax5.set_title('D2', fontsize=20)
        ax5.set_xlabel(r'$\log r$', fontsize=24)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        d, _ = datalist_13[1]
        ax6.plot(d[:, 0], d[:, 2], 'r-o', label='D2, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[1]
        ax6.plot(d[:, 0], d[:, 2], 'b-s', label='D2, run 49_093', lw=2, ms=7)
        ax6.set_xlabel(r'$\log r$', fontsize=24)

        d, _ = datalist_13[5]
        ax7.plot(d[:, 0], d[:, 2], 'r-o', label='D2, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[5]
        ax7.plot(d[:, 0], d[:, 2], 'b-s', label='D2, run 49_093', lw=2, ms=7)
        ax7.set_xlabel(r'$\log r$', fontsize=24)

        d, _ = datalist_13[7]
        ax8.plot(d[:, 0], d[:, 2], 'r-o', label='D2, run 48_093', lw=2, ms=7)
        d, _ = datalist_13b[7]
        ax8.plot(d[:, 0], d[:, 2], 'b-s', label='D2, run 49_093', lw=2, ms=7)
        ax8.set_xlabel(r'$\log r$', fontsize=24)
        f.savefig(figurePath + 'Overplot_logr_gamma_4_different_bins.png')

if R_limit_10000_logr_vr_Final_rfp_50bins:
    f, ((ax1, ax4), (ax2, ax5), (ax3, ax6)) = plt.subplots(3, 2)
    for i in range(1, 4):
        exec(f"ax{i}.set_xlim(-2, 4)")
        exec(f"ax{i}.set_ylim(-.1, .2)")
    for i in [1, 2, 4, 5]:
        exec(f"ax{i}.axes.get_xaxis().set_visible(False)")

    data, label = datalist_9b[0]
    a = label[:-14]
    ax1.plot(data[:, 0], data[:, 4], 'r-o', label=a, lw=2, ms=7)
    data, label = datalist_17[0]
    a = label[:-14]
    ax1.plot(data[:, 0], data[:, 4], 'b-s', label=a, lw=2, ms=7)
    ax1.set_ylabel('B', fontsize=24)
    ax1.set_title(r'Radial velocity, $v_r$. $R_{limit} = 10^4$, 50 bins',
                  fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(3):
        d, label = datalist_11[i]
        a = label[:-14]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=a, lw=2,
                 ms=7)
    for i in range(1, 4):
        d, label = datalist_17[i]
        a = label[:-14]
        ax2.plot(d[:, 0], d[:, 4], Symbols[i + 2], color=Colors[i + 2],
                 label=a, lw=2, ms=7)
    ax2.set_ylabel('CS', fontsize=24)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1, loc=0,
                     fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    for i in range(2):
        d, label = datalist_13b[i]
        if i == 0:
            a = label[:-14]
        else:
            a = label[:-14]
        ax3.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=a, lw=2,
                 ms=7)
    for i in range(4, 6):
        d, label = datalist_17[i]
        a = label[:-14]
        ax3.plot(d[:, 0], d[:, 4], Symbols[i - 2], color=Colors[i - 2],
                 label=a, lw=2, ms=7)
    ax3.set_ylabel('DS1 and D2', fontsize=24)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(4, 7):
        exec(f"ax{i}.set_xlim(-1.5, 3)")
        exec(f"ax{i}.set_ylim(-.005, .005)")
        exec(f"ax{i}.yaxis.tick_right()")

    data, label = datalist_9b[0]
    a = label[:-14]
    ax4.plot(data[:, 0], data[:, 4], 'r-o', label=a, lw=2, ms=7)
    data, label = datalist_17[0]
    a = label[:-14]
    ax4.plot(data[:, 0], data[:, 4], 'b-s', label=a, lw=2, ms=7)
    ax4.set_title('Zoom', fontsize=20)

    for i in range(3):
        d, label = datalist_11[i]
        a = label[:-14]
        ax5.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=a, lw=2,
                 ms=7)
    for i in range(1, 4):
        d, label = datalist_17[i]
        a = label[:-14]
        ax5.plot(d[:, 0], d[:, 4], Symbols[i + 2], color=Colors[i + 2],
                 label=a, lw=2, ms=7)

    for i in range(2):
        d, label = datalist_13b[i]
        if i == 0:
            a = label[:-14]
        else:
            a = label[:-14]
        ax6.plot(d[:, 0], d[:, 4], Symbols[i], color=Colors[i], label=a, lw=2,
                 ms=7)
    for i in range(4, 6):
        d, label = datalist_17[i]
        a = label[:-14]
        ax6.plot(d[:, 0], d[:, 4], Symbols[i - 2], color=Colors[i - 2],
                 label=a, lw=2, ms=7)
    ax6.set_xlabel(r'$\log r$', fontsize=24)
    f.savefig(figurePath + 'R_limit_10000_logr_vr_Final_rfp_50bins.png')

plt.show()
