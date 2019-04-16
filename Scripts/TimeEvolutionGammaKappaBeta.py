# -*- coding: utf-8 -*-

import h5py
import numpy as np
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
import pylab
import seaborn as sns
import os
import fileLsts as lsts
import colorsAndSymbols
from definePaths import *

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
      exec(f"ax{i}.plot({x}, np.log10({y}), '{cls}', label='{label}', lw=2, ms=7)")


    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC
    # A
    data, _ = datalist_A_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'r-o', 'A')
    # B
    data, _ = datalist_B_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'b-s', 'B')
    # CS4
    data, _ = datalist_CS4_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'k-<', 'CS4')
    # CS5
    data, _ = datalist_CS5_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'y--v', 'CS5')
    # CS6
    data, _ = datalist_CS6_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'g--*', 'CS6')
    # DS1
    data, _ = datalist_DS1_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'm--s', 'DS1')
    # Soft_D2
    data, _ = datalist_Soft_D2_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'c--d', 'Soft_D2')
    # E
    data, _ = datalist_E_R32[0]
    Plt_label(1, data[:, 0], data[:, 8], 'r--.', 'E')

    ax1.set_title(r'IC ($I: \Delta G, R_{limit}=32$)', fontsize=30)
    ax1.set_xlabel(r'$\log r$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    leg = ax1.legend(prop=dict(size=18), numpoints=1, ncol=1, loc=0,
                     fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    # Final
    # A
    data, _ = datalist_A_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'r-o')
    # B
    data, _ = datalist_B_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'b-s')
    # CS4
    data, _ = datalist_CS4_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'k-<')
    # CS5
    data, _ = datalist_CS5_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'y--v')
    # CS6
    data, _ = datalist_CS6_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'g--*')
    # DS1
    data, _ = datalist_DS1_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'm--s')
    # Soft_D2
    data, _ = datalist_Soft_D2_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'c--d')
    # E
    data, _ = datalist_E_R32[1]
    Plt(2, data[:, 0], data[:, 8], 'r--.')

    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.set_title(r'Final', fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'logr_rho_IC_Final_R32.png')

if log_r_r2_rho_IC_Final_R32:


  def Plt(i, x, y, cls):
      exec(f"ax{i}.plot(np.log10({x}), np.log10({y}), '{cls}', lw=2, ms=7)")


  def Plt_label(i, x, y, cls, label):
      exec(f"ax{i}.plot(np.log10({x}), np.log10({y}), '{cls}', label='{label}', lw=2, ms=7)")


    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC
    # A
    data, _ = datalist_A_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'r-o', 'A')
    # B
    data, _ = datalist_B_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'b-s', 'B')
    # CS4
    data, _ = datalist_CS4_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'k-<', 'CS4')
    # CS5
    data, _ = datalist_CS5_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'y--v', 'CS5')
    # CS6
    data, _ = datalist_CS6_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'g--*', 'CS6')
    # DS1
    data, _ = datalist_DS1_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'm--s', 'DS1')
    # Soft_D2
    data, _ = datalist_Soft_D2_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'c--d', 'Soft_D2')
    # E
    data, _ = datalist_E_R32[0]
    Plt_label(1, data[:, 7], data[:, 8], 'r--.', 'E')

    ax1.set_title(r'IC ($I: \Delta G, R_{limit}=32$)', fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    leg = ax1.legend(prop=dict(size=18), numpoints=1, ncol=1, loc=0,
                     fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    # Final
    # A
    data, _ = datalist_A_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'r-o')
    # B
    data, _ = datalist_B_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'b-s')
    # CS4
    data, _ = datalist_CS4_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'k-<')
    # CS5
    data, _ = datalist_CS5_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'y--v')
    # CS6
    data, _ = datalist_CS6_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'g--*')
    # DS1
    data, _ = datalist_DS1_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'm--s')
    # Soft_D2
    data, _ = datalist_Soft_D2_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'c--d')
    # E
    data, _ = datalist_E_R32[1]
    Plt(2, data[:, 7], data[:, 8], 'r--.')

    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax2.set_title(r'Final', fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'log_r_r2_rho_IC_Final_R32.png')

if logr_rho:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(1, 3):
        exec(f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1, loc=0,
                                  fancybox=True, handlelength=2.5)")
        exec(f"leg.get_frame().set_alpha(.5)")

    for i in range(len(datalist_A_R10000_20bins)):
        data, label = datalist_A_R10000_20bins[i]
        a = label[22:-29]
        ax1.plot(data[:, 0], np.log10(data[:, 8]), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)

    ax1.set_xlabel(r'$\log r$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    ax1.set_title(r'Sim. I of A ($R_{limit}=10^4, 20$ bins)',
                  fontsize=30)

    for i in range(len(datalist_B_R10000_20bins)):
        data, label = datalist_B_R10000_20bins[i]
        a = label[22:-29]
        ax2.plot(data[:, 0], np.log10(data[:, 8]), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)

    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.set_title(r'Sim. I of B', fontsize=30)
    # ax2.tick_params(axis='both', which='both', bottom='on', top='off',
    #                 labelbottom='on', right='off', left='on',
    #                 labelleft='on')
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'logr_rho.png')

if log_r_r2_rho:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(1, 3):
        exec(f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1, loc=0,
                                  fancybox=True, handlelength=2.5)")
        exec(f"leg.get_frame().set_alpha(.5)")

    for i in range(len(datalist_A_R10000_20bins)):
        data, label = datalist_A_R10000_20bins[i]
        a = label[22:-29]
        ax1.plot(np.log10(data[:, 7]), np.log10(data[:, 8]),
                 Symbols[i], color=Colors[i], label=a, lw=2, ms=7)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\log \rho$', fontsize=30)
    ax1.set_title(r'Sim. I of A ($R_{limit}=10^4, 20$ bins)',
                  fontsize=30)

    for i in range(len(datalist_B_R10000_20bins)):
        data, label = datalist_B_R10000_20bins[i]
        a = label[22:-29]
        ax2.plot(np.log10(data[:, 7]), np.log10(data[:, 8]),
                 Symbols[i], color=Colors[i], label=a, lw=2, ms=7)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax2.set_title(r'Sim. I of B', fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figurePath + 'log_r_r2_rho.png')

if Overplot_IC_Final:
    f = plt.figure()
    plt.subplot(121)
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        plt.plot(data[:, 0], data[:, 1], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(len(datalist_Martin_Final) - 1):
        data, label = datalist_Martin_Final[i]
        plt.plot(data[:, 4], data[:, 5], Symbols[i], color=Colors2[i],
                 label=label, lw=2, ms=7)
    data, label = datalist_Martin_Final[7]
    plt.plot(data[:, 0], data[:, 1], 'r--.',
             label=label, lw=2, ms=7)
    plt.title(r'IC and Final', fontsize=20)
    plt.xlabel(r'$\beta$', fontsize=24)
    plt.ylabel(r'$\gamma$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=4, handlelength=2.5)

    plt.subplot(122)
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        plt.plot(data[:, 0], data[:, 2], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(len(datalist_Martin_Final) - 1):
        data, label = datalist_Martin_Final[i]
        plt.plot(data[:, 4], data[:, 6], Symbols[i], color=Colors2[i],
                 label=label, lw=2, ms=7)
    data, label = datalist_Martin_Final[7]
    plt.plot(data[:, 0], data[:, 2], 'r--.',
             label=label, lw=2, ms=7)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=4, handlelength=2.5)
    plt.title(r'IC and Final', fontsize=20)
    plt.xlabel(r'$\beta$', fontsize=24)
    plt.ylabel(r'$\kappa$', fontsize=24)
    f.savefig(figurePath + 'Overplot_IC_Final.png')

if beta_vs_gamma_plus_kappa:
    f = plt.figure()
    plt.subplot(121)
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        plt.plot(data[:, 0], data[:, 1] + data[:, 2], Symbols[i],
                 color=Colors[i], label=label, lw=2, ms=7)
    plt.title(r'IC', fontsize=20)
    plt.xlabel(r'$\beta$', fontsize=24)
    plt.ylabel(r'$\gamma + \kappa$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(122)
    for i in range(len(datalist_Martin_Final) - 1):
        data, label = datalist_Martin_Final[i]
        plt.plot(data[:, 4], data[:, 5] + data[:, 6], Symbols[i],
                 color=Colors2[i], label=label, lw=2, ms=7)
    data, label = datalist_Martin_Final[7]
    plt.plot(data[:, 0], data[:, 1] + data[:, 2], 'r--.', label=label, lw=2, ms=7)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)
    plt.title(r'Final', fontsize=20)
    plt.xlabel(r'$\beta$', fontsize=24)
    plt.ylabel(r'$\gamma + \kappa$', fontsize=24)
    f.savefig(figurePath + 'beta_vs_gamma_plus_kappa.png')

# 3D plots of attractor, IC and Final.
if Attractor_3D:
    f = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    n = 100
    # for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], Symbols[i],
                   color=Colors[i], label=label, lw=2, ms=7)
        # plt.plot(data[:, 0], data[:, 1] + data[:, 2], Symbols[i],
        #          color=Colors[i], label=label, lw=2, ms=7)
        # ax.scatter(x, y, z, c=c, marker=m)
    ax.set_xlabel(r'$2 \beta$')
    ax.set_ylabel(r'$\gamma$')
    ax.set_zlabel(r'$\kappa$')
    ax.set_title('3D view of attractor')
    f.savefig(figurePath + 'Attractor_3D.png')

if Time_evolution_beta_gamma_kappa:

  # Python 3.x: small greek letters are coded from 945 to 969 , so alpha is chr(945), omega is chr(969).


    def figure(sim):
        f = plt.figure()
        plt.subplot(131)
        exec(f"for i in range(len(datalist_{sim})):")
            exec(f"data, label = datalist_{sim}[i]")
            plt.plot(data[:, 0], data[:, 1], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(f"{chr(946)}", fontsize=24)

        plt.subplot(132)
        exec(f"for i in range(len(datalist_{sim})):")
            exec(f"data, label = datalist_{sim}[i]")
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.title(f"Time evolution of {chr(946)}, {chr(947)} and {chr(954)}\
                  for Simulation {sim}",
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(f"{chr(947)}", fontsize=24)

        plt.subplot(133)
        exec(f"for i in range(len(datalist_{sim})):")
            exec(f"data, label = datalist_{sim}[i]")
            plt.plot(data[:, 0], data[:, 3], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(f"{chr(954)}", fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
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
            data, label = datalist_C_IC[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.title(r'$\gamma $ for CS1, CS2 and CS3', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'$\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'CS1CS2CS3_Overplot_logr_gamma.png')

    if CS4CS5CS6:
        plt.subplot(121)
        # IC
        for i in range(len(datalist_CS4CS5CS6_IC_R10000)):
            data, label = datalist_CS4CS5CS6_IC_R10000[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.title(r'Time evolution of $\gamma $ for CS4, CS5 and CS6',
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Initial $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        plt.subplot(122)
        # Final
        for i in range(len(datalist_CS4CS5CS6_Final)):
            data, label = datalist_CS4CS5CS6_Final[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        # plt.title(r'Time evolution of $\beta$, $\gamma$ and $\kappa$\
        #           for CS4, CS5 and CS6', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'CS4CS5CS6_Overplot_logr_gamma.png')

    if DS1D2:
        plt.subplot(121)
        # IC
        for i in range(len(datalist_DS1D2_IC_R10000)):
            data, label = datalist_DS1D2_IC_R10000[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        plt.title(r'Time evolution of $\gamma $ for DS1 and D2', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Initial $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        plt.subplot(122)
        # Final
        for i in range(len(datalist_DS1D2_Final_R10000)):
            data, label = datalist_DS1D2_Final_R10000[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        # plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$\
        #           for DS1 and D2',
        #           fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'DS1D2_Overplot_logr_gamma.png')

    if BCS4CS5CS6DS1D2:

        plt.subplot(121)
        # IC
        for i in range(len(datalist_CS4CS5CS6_IC_R10000)):
            data, label = datalist_CS4CS5CS6_IC_R10000[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i - 3],
                     color=Colors[i-3], label=label, lw=2, ms=7)
        for i in range(2):
            data, label = datalist_DS1D2_IC[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        data, label = FileLstB_IC_R10000[0]
        plt.plot(data[:, 0], data[:, 2], 'k-<', label=label, lw=2, ms=7)

        plt.title(r'Time evolution of $\gamma$\
                  for B, CS4, CS5, CS6, DS1 and D2',
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Initial $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        # Final
        plt.subplot(122)
        # C
        for i in range(3):
            data, label = datalist_C_Final[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        # D
        for i in range(2):
            data, label = datalist_DS1D2_Final[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i + 3],
                     color=Colors[i + 3], label=label, lw=2, ms=7)
        # B
        data, label = FileLstB_Final_R10000[0]
        plt.plot(data[:, 0], data[:, 2], 'm--s', label=label, lw=2, ms=7)

        # plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$\
        #           for DS1 and D2',fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)
        f.savefig(figurePath + 'BCS4CS5CS6DS1D2_Overplot_logr_gamma.png')

    if DS1D2_final_evolution:
        # DS1, Run 48 and 49, 50 bins
        plt.subplot(221)
        data, _ = datalist_13[0]
        plt.plot(data[:, 0], data[:, 2], 'r-o',
                 label='DS1, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[0]
        plt.plot(data[:, 0], data[:, 2], 'b-s',
                 label='DS1, run 49_093', lw=2, ms=7)
        plt.title(r'Time evolution of $\gamma $ for DS1 and D2. 50 bins',
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        # D2, Run 48 and 49, 50 bins
        plt.subplot(222)
        data, _ = datalist_13[1]
        plt.plot(data[:, 0], data[:, 2], 'k-<', label='D2, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[1]
        plt.plot(data[:, 0], data[:, 2], 'y--v', label='D2, run 49_093', lw=2, ms=7)
        plt.title(r'50 bins', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        # DS1, Run 48 and 49, 20 bins
        plt.subplot(223)
        data, _ = datalist_13[2]
        plt.plot(data[:, 0], data[:, 2], 'r-o', label='DS1, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[2]
        plt.plot(data[:, 0], data[:, 2], 'b-s', label='DS1, run 49_093', lw=2, ms=7)
        plt.title(r'20 bins', fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        plt.ylim(-5, 1)

        # D2, Run 48 and 49, 20 bins
        plt.subplot(224)
        data, _ = datalist_13[3]
        plt.plot(data[:, 0], data[:, 2], 'k-<', label='D2, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[3]
        plt.plot(data[:, 0], data[:, 2], 'y--v', label='D2, run 49_093', lw=2, ms=7)
        plt.title(r'20 bins', fontsize=20)
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
                  with bound structure (50 bins)',
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'rfp_B_Overplot_logr_gamma.png')

    if rfp_CS4CS5CS6:
        for i in range(3):
            data, label = datalist_11[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(1, 4):
            data, label = datalist_17[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i + 2],
                     color=Colors[i + 2], label=label, lw=2, ms=7)
        plt.ylim(-4, 1)
        plt.title(r'$\gamma$ for CS4, CS5 and CS6 Final products,\
                  with bound structures (50 bins)',
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'rfp_CS4CS5CS6_Overplot_logr_gamma.png')

    if rfp_DS1D2:
        for i in range(2):
            data, label = datalist_13b[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(4, 6):
            data, label = datalist_17[i]
            plt.plot(data[:, 0], data[:, 2], Symbols[i - 2],
                     color=Colors[i - 2], label=label, lw=2, ms=7)
        plt.ylim(-4, 1)
        plt.title(r'$\gamma$ for DS1 and D2 Final products,\
                  with bound structures (50 bins)',
                  fontsize=20)
        plt.xlabel(r'$\log r$', fontsize=24)
        plt.ylabel(r'Final $\gamma$', fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        f.savefig(figurePath + 'rfp_DS1D2_Overplot_logr_gamma.png')

    if rfp_BCS4CS5CS6DS1D2:
        f, (ax1, ax2, ax3) = plt.subplots(3, 1)

        for i in range(1, 4):
            exec(f"ax{i}.set_ylim(-4, 1)")
            exec(f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1, loc=0,
                                      fancybox=True, handlelength=2.5)")
            exec(f"leg.get_frame().set_alpha(.5)")

        for i in range(1, 3):
            exec(f"ax{i}.axes.get_xaxis().set_visible(False)")

        data, label = datalist_9b[0]
        ax1.plot(data[:, 0], data[:, 2], 'r-o',
                 label=label, lw=2, ms=7)
        data, label = datalist_17[0]
        ax1.plot(data[:, 0], data[:, 2], 'b-s',
                 label=label, lw=2, ms=7)

        ax1.set_title(r'$\gamma$ for Final products,\
                      with bound structure (50 bins)',
                      fontsize=20)
        ax1.set_ylabel('B', fontsize=24)

        for i in range(3):
            data, label = datalist_11[i]
            ax2.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(1, 4):
            data, label = datalist_17[i]
            ax2.plot(data[:, 0], data[:, 2], Symbols[i + 2],
                     color=Colors[i + 2], label=label, lw=2, ms=7)
        ax2.set_ylabel('CS4, CS5 and CS6', fontsize=24)

        for i in range(2):
            data, label = datalist_13b[i]
            ax3.plot(data[:, 0], data[:, 2], Symbols[i],
                     color=Colors[i], label=label, lw=2, ms=7)
        for i in range(4, 6):
            data, label = datalist_17[i]
            ax3.plot(data[:, 0], data[:, 2], Symbols[i - 2],
                     color=Colors[i - 2], label=label, lw=2, ms=7)
        ax3.set_xlabel(r'$\log r$', fontsize=24)
        ax3.set_ylabel('DS1 and D2', fontsize=24)
        f.savefig(figurePath + 'rfp_BCS4CS5CS6DS1D2_Overplot_logr_gamma.png')

if Overplot_ln_rdividedbyd3_gamma:
    f = plt.figure()

    # Below are only Final files with 50 radial bins.
    list_of_minima_CS4 = [(0, 'd1'), (0, 'd2'), (0, 'd3')]
    list_of_maxima_CS4 = [(0, 'p1'), (0, 'p2'), (0, 'p3')]
    list_of_minima_CS5 = [(0, 'd1'), (0, 'd2'), (0, 'd3')]
    list_of_maxima_CS5 = [(0, 'p1'), (0, 'p2'), (0, 'p3')]
    list_of_minima_CS6 = [(0, 'd1'), (0, 'd2'), (0, 'd3')]
    list_of_maxima_CS6 = [(0, 'p1'), (0, 'p2'), (0, 'p3')]
    list_of_minima_DS1 = [(0, 'd1'), (0, 'd2'), (0, 'd3')]
    list_of_maxima_DS1 = [(0, 'p1'), (0, 'p2'), (0, 'p3')]
    list_of_minima_D2 = [(0, 'd1'), (0, 'd2'), (-3.705065011901715444, 'd3')]
    list_of_maxima_D2 = [(0, 'p1'), (0, 'p2'), (0, 'p3')]

    d_data_CS4 = [(value, label_d) for value, label_d in list_of_minima_CS4]
    d_data_CS5 = [(value, label_d) for value, label_d in list_of_minima_CS5]
    d_data_CS6 = [(value, label_d) for value, label_d in list_of_minima_CS6]
    d_data_DS1 = [(value, label_d) for value, label_d in list_of_minima_DS1]
    d_data_D2 = [(value, label_d) for value, label_d in list_of_minima_D2]

    p_data_CS4 = [(value, label_p) for value, label_p in list_of_maxima_CS4]
    p_data_CS5 = [(value, label_p) for value, label_p in list_of_maxima_CS5]
    p_data_CS6 = [(value, label_p) for value, label_p in list_of_maxima_CS6]
    p_data_DS1 = [(value, label_p) for value, label_p in list_of_maxima_DS1]
    p_data_D2 = [(value, label_p) for value, label_p in list_of_maxima_D2]

    data, label = datalist_6[0]
    value, label_d = d_data_C4[2]
    plt.plot(np.log(data[:, 5] / -value), data[:, 2], 'r-o', label=label, lw=2, ms=7)
    data, label = datalist_6[1]
    value, label_d = d_data_C5[2]
    plt.plot(np.log(data[:, 5] / -value), data[:, 2], 'b-s', label=label, lw=2, ms=7)
    data, label = datalist_6[2]
    value, label_d = d_data_C6[2]
    plt.plot(np.log(data[:, 5] / -value), data[:, 2], 'k-<', label=label, lw=2, ms=7)
    data, label = datalist_8[0]
    value, label_d = d_data_D1[2]
    plt.plot(np.log(data[:, 5] / -value), data[:, 2], 'y--v', label=label, lw=2, ms=7)
    data, label = datalist_8[1]
    value, label_d = d_data_D2[2]
    plt.plot(np.log(data[:, 5] / -value), data[:, 2], 'g--*', label=label, lw=2, ms=7)

    plt.title(r'Final $\gamma $ for CS4, CS5, CS6, DS1 and D2',
              fontsize=20)
    plt.xlabel(r'$ \log \frac{r}{|d_3|}$', fontsize=24)
    plt.ylabel(r'Final $\gamma$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'Overplot_ln_rdividedbyd3_gamma.png')

if lnr_VR_IC_Final_50bins_20bins:

    title_str = f"Time evolution of {chr(946)}, {chr(947)} and {chr(954)}\
                  for Simulation DS1 and D2"

    f = plt.figure()
    # Initial, 50 bins
    plt.subplot(221)
    for i in range(6, 9):
        data, label = datalist_5[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_7[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    plt.title(r'Time evolution of $v_r $\
              for Simulation CS4, CS5, CS6, DS1 and D2',
              fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Initial $v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # Final, 50 bins
    plt.subplot(222)
    for i in range(3):
        data, label = datalist_6[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_8[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # plt.title(title_str, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # Initial, 20 bins
    plt.subplot(223)
    for i in range(9, 12):
        data, label = datalist_5[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_7[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # plt.title(title_str, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Initial $v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # Final, 20 bins
    plt.subplot(224)
    for i in range(3, 6):
        data, label = datalist_6[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_8[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # plt.title(title_str, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'lnr_VR_IC_Final_50bins_20bins.png')

if lnr_sigmarad2_IC_Final_50bins_20bins:

    title_str = f"Time evolution of {chr(946)}, {chr(947)} and {chr(954)}\
                  for Simulation DS1 and D2"

    f = plt.figure()
    # Initial, 50 bins
    plt.subplot(221)
    for i in range(6, 9):
        data, label = datalist_5[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_7[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    plt.title(r'Time evolution of $\sigma_r^2$\
              for Simulation CS4, CS5, CS6, DS1 and D2',
              fontsize=20)  # Include Sim B as well.
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Initial $\sigma_r^2$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # Final, 50 bins
    plt.subplot(222)
    for i in range(3):
        data, label = datalist_6[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_8[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # plt.title(title_str, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $\sigma_r^2$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # Initial, 20 bins
    plt.subplot(223)
    for i in range(9, 12):
        data, label = datalist_5[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_7[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # plt.title(title_str, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Initial $\sigma_r^2$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    # Final, 20 bins
    plt.subplot(224)
    for i in range(3, 6):
        data, label = datalist_6[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_8[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # plt.title(title_str, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $ \sigma_r^2 $', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'lnr_sigmarad2_IC_Final_50bins_20bins.png')

if lnr_sigmarad2_vr_Final_50bins:
    f = plt.figure()
    plt.subplot(121)
    for i in range(3):
        data, label = datalist_6[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_8[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i + 3], color=Colors[i + 3],
                 label=label, lw=2, ms=7)
    data, label = datalist_4[4]
    plt.plot(data[:, 0], data[:, 6], Symbols[5], color=Colors[5],
             label=label, lw=2, ms=7)
    plt.title(r'Final $\sigma_r^2$\
              for Simulation B, CS4, CS5, CS6, DS1 and D2',
              fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $\sigma_r^2$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(122)
    for i in range(3):
        data, label = datalist_6[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i],
                 color=Colors[i], label=label, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_8[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i + 3],
                 color=Colors[i + 3], label=label, lw=2, ms=7)
    data, label = datalist_4[4]
    plt.plot(data[:, 0], data[:, 4], Symbols[5], color=Colors[5],
             label=label, lw=2, ms=7)
    plt.title(r'Final $v_r$ for Simulation B, CS4, CS5, CS6, DS1 and D2',
              fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'lnr_sigmarad2_vr_Final_50bins.png')

if R_limit_10000_logr_sigmarad2_vr_Final_20bins:
    f, (ax1, ax2) = plt.subplots(2, 1)
    # CS4, CS5, CS6: datalist_10 (IC), datalist_11 (Final)
    for i in range(3, 6):
        data, label = datalist_11[i]
        ax1.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # DS1, D2: datalist_12 (IC), datalist_13 (Final)
    for i in range(2, 4):
        data, label = datalist_13[i]
        ax1.plot(data[:, 0], data[:, 6], Symbols[i - 2], color=Colors[i - 2],
                 label=label, lw=2, ms=7)
    # B: datalist_9 (Final)
    data, label = datalist_9[1]
    ax1.plot(data[:, 0], data[:, 6], Symbols[2], color=Colors[2],
             label=label, lw=2, ms=7)
    ax1.set_title(r'Final B, CS4, CS5, CS6, DS1 and D2.\
                  $R_{limit} = 10^4$. 20 bins',
                  fontsize=20)
    ax1.set_ylabel(r'$\sigma_r^2$', fontsize=24)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(3, 6):
        data, label = datalist_11[i]
        ax2.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_13[i]
        ax2.plot(data[:, 0], data[:, 4], Symbols[i - 2], color=Colors[i - 2],
                 label=label, lw=2, ms=7)
    data, label = datalist_9[1]
    ax2.plot(data[:, 0], data[:, 4], Symbols[2], color=Colors[2],
             label=label, lw=2, ms=7)
    ax2.set_xlabel(r'$\log r$', fontsize=24)
    ax2.set_ylabel(r'$v_r$', fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'R_limit_10000_logr_sigmarad2_vr_Final_20bins.png')

if R_limit_5000_lnr_sigmarad2_vr_Final_50bins:
    f = plt.figure()
    plt.subplot(121)
    # CS4,CS5,CS6: datalist_15 (Final)
    for i in range(3):
        data, label = datalist_15[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    # DS1,D2: datalist_16 (Final)
    for i in range(2):
        data, label = datalist_16[i]
        plt.plot(data[:, 0], data[:, 6], Symbols[i + 3], color=Colors[i + 3],
                 label=label, lw=2, ms=7)
    # B: datalist_14 (Final)
    data, label = datalist_14[0]
    plt.plot(data[:, 0], data[:, 6], 'm--s',
             label=label, lw=2, ms=7)
    plt.title(r'Simulation B, CS4, CS5, CS6, DS1 and D2.\
              $R_{limit} = 5 \cdot 10^3$. 50 bins',
              fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $\sigma_r^2$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(122)
    for i in range(3):
        data, label = datalist_15[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=label, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_16[i]
        plt.plot(data[:, 0], data[:, 4], Symbols[i + 3], color=Colors[i + 3],
                 label=label, lw=2, ms=7)
    data, label = datalist_14[0]
    plt.plot(data[:, 0], data[:, 4], 'm--s',
             label=label, lw=2, ms=7)
    # plt.title(r'Final $v_r $ for Simulation B, CS4, CS5, CS6, DS1 and D2',
    #           fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'Final $v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'R_limit_5000_lnr_sigmarad2_vr_Final_50bins.png')

if R_limit_10000_logr_r_vr_IC_Final_20bins_50bins:
    f = plt.figure()
    plt.subplot(221)
    for i in range(3, 6):
        data, label = datalist_11[i]
        a = label[:-62]
        plt.plot(data[:, 5], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot(data[:, 5], data[:, 4], Symbols[i - 1], color=Colors[i - 1],
                 label=a, lw=2, ms=7)
    data, label = datalist_9[1]
    a = label[:-57]
    plt.plot(data[:, 5], data[:, 4], 'r-o', label=a, lw=2, ms=7)

    plt.title(r'Final products, $R_{limit} = 10^4$, 20 bins', fontsize=20)
    plt.xlabel('r', fontsize=24)
    plt.ylabel(r'$v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(222)
    for i in range(3, 6):
        data, label = datalist_11[i]
        a = label[:-62]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot(data[:, 0], data[:, 4], Symbols[i - 1], color=Colors[i - 1],
                 label=a, lw=2, ms=7)
    data, label = datalist_9[1]
    a = label[:-57]
    plt.plot(data[:, 0], data[:, 4], 'r-o', label=a, lw=2, ms=7)

    plt.title(r'20 bins', fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'$v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(223)
    for i in range(3):
        data, label = datalist_11[i]
        a = label[:-47]
        plt.plot(data[:, 5], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot(data[:, 5], data[:, 4], Symbols[i + 3], color=Colors[i+3],
                 label=a, lw=2, ms=7)
    data, label = datalist_9[0]
    a = label[:-42]
    plt.plot(data[:, 5], data[:, 4], 'm--s',
             label=a, lw=2, ms=7)
    plt.title(r'50 bins', fontsize=20)
    plt.xlabel('r', fontsize=24)
    plt.ylabel(r'$v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(224)
    for i in range(3):
        data, label = datalist_11[i]
        a = label[:-47]
        plt.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot(data[:, 0], data[:, 4], Symbols[i + 3], color=Colors[i + 3],
                 label=a, lw=2, ms=7)

    data, label = datalist_9[0]
    a = label[:-42]
    plt.plot(data[:, 0], data[:, 4], 'm--s',
             label=a, lw=2, ms=7)
    plt.title(r'50 bins', fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'$v_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath
              + 'R_limit_10000_logr_r_vr_IC_Final_20bins_50bins.png')

if R_limit_10000_logr_r_ur_Final_20bins_50bins:
    f = plt.figure()
    plt.subplot(221)
    for i in range(3, 6):
        data, label = datalist_11[i]
        a = label[:-62]
        plt.plot(data[:, 5], data[:, 4] / (data[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot(data[:, 5], data[:, 4] / (data[:, 6] ** .5),
                 Symbols[i - 1],
                 color=Colors[i - 1], label=a, lw=2, ms=7)
    data, label = datalist_9[1]
    a = label[:-57]
    plt.plot(data[:, 5], data[:, 4] / (data[:, 6] ** .5), 'r-o', label=a, lw=2, ms=7)
    plt.title(r'Final products, $R_{limit} = 10^4$, 20 bins',
              fontsize=20)
    plt.xlabel('r', fontsize=24)
    plt.ylabel(r'$u_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(222)
    for i in range(3, 6):
        data, label = datalist_11[i]
        a = label[:-62]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i - 1],
                 color=Colors[i - 1], label=a, lw=2, ms=7)
    data, label = datalist_9[1]
    a = label[:-57]
    plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), 'r-o', label=a, lw=2, ms=7)
    plt.title(r'20 bins', fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'$u_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(223)
    for i in range(3):
        data, label = datalist_11[i]
        a = label[:-47]
        plt.plot(data[:, 5], data[:, 4] / (data[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot(data[:, 5], data[:, 4] / (data[:, 6] ** .5), Symbols[i + 3],
                 color=Colors[i + 3], label=a, lw=2, ms=7)
    data, label = datalist_9[0]
    a = label[:-42]
    plt.plot(data[:, 5], data[:, 4] / (data[:, 6] ** .5), 'm--s', label=a, lw=2, ms=7)
    plt.title(r'50 bins', fontsize=20)
    plt.xlabel('r', fontsize=24)
    plt.ylabel(r'$u_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(224)
    for i in range(3):
        data, label = datalist_11[i]
        a = label[:-47]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i + 3],
                 color=Colors[i + 3], label=a, lw=2, ms=7)
    data, label = datalist_9[0]
    a = label[:-42]
    plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), 'm--s', label=a, lw=2, ms=7)
    plt.title(r'50 bins', fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'$u_r$', fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)
    f.savefig(figurePath + 'R_limit_10000_logr_r_ur_Final_20bins_50bins.png')

if R_limit_10000_logr_ur_Final_20bins_50bins:
    # subplot 2,4 are reused from previous figure.
    # changes:
    # datalist9 -> datalist9b,
    # datalist_11 -> ? datalist_11b ?,
    # datalist_13 -> datalist_13b.
    f = plt.figure()
    plt.subplot(121)
    for i in range(3, 6):
        data, label = datalist_11[i]
        a = label[:-62]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2, 4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i - 1],
                 color=Colors[i - 1], label=a, lw=2, ms=7)
    data, label = datalist_9b[1]
    a = label[:-57]
    plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), 'r-o', label=a, lw=2, ms=7)

    plt.title(r'Final products, $R_{limit} = 10^4$, 20 bins',
              fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r' $u_r$',  fontsize=24)
    plt.xlim(-1, 2)
    plt.ylim(-.2, .2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=0, handlelength=2.5)

    plt.subplot(122)
    for i in range(3):
        data, label = datalist_11[i]
        a = label[:-47]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i],
                 color=Colors[i], label=a, lw=2, ms=7)
    for i in range(2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), Symbols[i + 3],
                 color=Colors[i + 3], label=a, lw=2, ms=7)
    data, label = datalist_9b[0]
    a = label[:-42]
    plt.plot(data[:, 0], data[:, 4] / (data[:, 6] ** .5), 'm--s', label=a, lw=2, ms=7)
    plt.title(r'50 bins', fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=24)
    plt.ylabel(r'$u_r$', fontsize=24)
    plt.xlim(-1, 2)
    plt.ylim(-.2, .2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
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

        data, _ = datalist_13[2]
        ax1.plot(data[:, 0], data[:, 2], 'r-o',
                 label='DS1, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[2]
        ax1.plot(data[:, 0], data[:, 2], 'b-s',
                 label='DS1, run 49_093', lw=2, ms=7)

        ax1.set_title(r'Time evolution of $\gamma$ for Simulation DS1',
                      fontsize=20)
        ax1.set_ylabel(r'20 bins', fontsize=24)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, _ = datalist_13[0]
        ax2.plot(data[:, 0], data[:, 2], 'r-o',
                 label='DS1, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[0]
        ax2.plot(data[:, 0], data[:, 2], 'b-s',
                 label='DS1, run 49_093', lw=2, ms=7)
        ax2.set_ylabel(r'50 bins', fontsize=24)

        data, _ = datalist_13[4]
        ax3.plot(data[:, 0], data[:, 2], 'r-o',
                 label='DS1, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[4]
        ax3.plot(data[:, 0], data[:, 2], 'b-s',
                 label='DS1, run 49_093', lw=2, ms=7)
        ax3.set_ylabel(r'100 bins', fontsize=24)

        data, _ = datalist_13[6]
        ax4.plot(data[:, 0], data[:, 2], 'r-o',
                 label='DS1, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[6]
        ax4.plot(data[:, 0], data[:, 2], 'b-s',
                 label='DS1, run 49_093', lw=2, ms=7)
        ax4.set_ylabel(r'200 bins', fontsize=24)

        data, _ = datalist_13[3]
        ax5.plot(data[:, 0], data[:, 2], 'r-o',
                 label='D2, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[3]
        ax5.plot(data[:, 0], data[:, 2], 'b-s',
                 label='D2, run 49_093', lw=2, ms=7)
        ax5.set_title(r'D2', fontsize=20)
        ax5.set_xlabel(r'$\log r$', fontsize=24)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, _ = datalist_13[1]
        ax6.plot(data[:, 0], data[:, 2], 'r-o',
                 label='D2, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[1]
        ax6.plot(data[:, 0], data[:, 2], 'b-s',
                 label='D2, run 49_093', lw=2, ms=7)
        ax6.set_xlabel(r'$\log r$', fontsize=24)

        data, _ = datalist_13[5]
        ax7.plot(data[:, 0], data[:, 2], 'r-o',
                 label='D2, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[5]
        ax7.plot(data[:, 0], data[:, 2], 'b-s',
                 label='D2, run 49_093', lw=2, ms=7)
        ax7.set_xlabel(r'$\log r$', fontsize=24)

        data, _ = datalist_13[7]
        ax8.plot(data[:, 0], data[:, 2], 'r-o',
                 label='D2, run 48_093', lw=2, ms=7)
        data, _ = datalist_13b[7]
        ax8.plot(data[:, 0], data[:, 2], 'b-s',
                 label='D2, run 49_093', lw=2, ms=7)

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
        data, label = datalist_11[i]
        a = label[:-14]
        ax2.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(1, 4):
        data, label = datalist_17[i]
        a = label[:-14]
        ax2.plot(data[:, 0], data[:, 4], Symbols[i + 2], color=Colors[i + 2],
                 label=a, lw=2, ms=7)
    ax2.set_ylabel('CS', fontsize=24)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1, loc=0,
                     fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    for i in range(2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-14]
        else:
            a = label[:-14]
        ax3.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(4, 6):
        data, label = datalist_17[i]
        a = label[:-14]
        ax3.plot(data[:, 0], data[:, 4], Symbols[i - 2],
                 color=Colors[i - 2], label=a, lw=2, ms=7)
    ax3.set_ylabel('DS1 and D2', fontsize=24)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    for i in range(4, 7):
        exec(f"ax{i}.set_xlim(-1.5, 3)")
        exec(f"ax{i}.set_ylim(-.005, .005)")
        exec(f"ax{i}.yaxis.tick_right()")

    data, label = datalist_9b[0]
    a = label[:-14]
    ax4.plot(data[:, 0], data[:, 4], 'r-o',
             label=a, lw=2, ms=7)
    data, label = datalist_17[0]
    a = label[:-14]
    ax4.plot(data[:, 0], data[:, 4], 'b-s',
             label=a, lw=2, ms=7)
    ax4.set_title(r'Zoom', fontsize=20)

    for i in range(3):
        data, label = datalist_11[i]
        a = label[:-14]
        ax5.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(1, 4):
        data, label = datalist_17[i]
        a = label[:-14]
        ax5.plot(data[:, 0], data[:, 4], Symbols[i + 2], color=Colors[i + 2],
                 label=a, lw=2, ms=7)

    for i in range(2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-14]
        else:
            a = label[:-14]
        ax6.plot(data[:, 0], data[:, 4], Symbols[i], color=Colors[i],
                 label=a, lw=2, ms=7)
    for i in range(4, 6):
        data, label = datalist_17[i]
        a = label[:-14]
        ax6.plot(data[:, 0], data[:, 4], Symbols[i - 2], color=Colors[i - 2],
                 label=a, lw=2, ms=7)
    ax6.set_xlabel(r'$\log r$', fontsize=24)
    f.savefig(figurePath + 'R_limit_10000_logr_vr_Final_rfp_50bins.png')

plt.show()
