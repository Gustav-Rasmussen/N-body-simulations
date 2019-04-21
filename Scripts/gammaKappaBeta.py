# -*- coding: utf-8 -*-

# import pylab
# from pathlib import Path
import matplotlib.lines as lines
import matplotlib.pyplot as plt
import numpy as np
# import fileLsts as lsts
# import snapshotFiles
# import colorsAndSymbols
# import dataLsts
# from definePaths import *
# import sigma_calc

# Functions -------------------------------------------------------------------


def rhoHQ(r, rho0, rS):
    """Return Hernquist density profile."""
    return rho0 / ((r / rS) * (1 + r / rS) ** 3.)


def betaOM(r, rA=1.20):
    """Return Osipkov-Merritt beta profile."""
    return 1. / (1. + (rA / r) ** 2)


def sigmaRad2():
    """Return the square of the radial velocity dispersion."""
    x, y, z, vx, vy, vz = np.linspace(.01, 1.2)
    binningArrLinLog10 = np.logspace(minBinningR, maxBinningR,
                                     nrBinningBins)
    for i in range(nrBinningBins - 2):
        minRBinI = binningArrLinLog10[i]  # start of bin
        maxRBinI = binningArrLinLog10[i + 1]  # end of bin
        vR[i] = ((vx[i] * x[i] + vy[i] * y[i] + vz[i] * z[i])
                 / ((x[i] ** 2 + y[i] ** 2 + z[i] ** 2) ** .5))
        vR2[i] = vR[i] ** 2
        sigmaR2 = (1. / (len(vR2) + 1.)) * np.sum(vR2[i])
    return sigmaR2


# Switches for figures --------------------------------------------------------

logrR2BetaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
logrR2KappaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
logrR2GammaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
logrBetaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
logrKappaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
logrGammaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
betaGammaKappaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
betaGammaABCS4CS5CS6DS1D2E_ICFinalRLimit32 = 0
betaGammaKappaABCS4CS5CS6DS1D2E_ICFinal20BinsRLimit10000 = 0
betaGammaABCS4CS5CS6DS1D2E_ICFinal20BinsRLimit10000 = 0
betaGammaKappaCS1CS2CS3_20_50Bins = 0
betaGammaKappaCS4CS5CS6_20_50Bins = 0
betaGammaKappaCS4CS5CS6_Final20_50Bins = 0
betaGammaKappaDS1D2_20_50Bins = 0
betaGammaKappaDS1D2_Final20_50Bins = 0
betaGammaKappaBCS4CS5CS6DS1D2_ICFinal20_50Bins = 0
betaGammaKappaRfpBCS4CS5CS6DS1D2_Final50BinsRLimit10000 = 0
overplotICFinal = 0
ICFinal4Subplots = 0
finalGammaBetaFit = 0
betaVsGammaPlusKappa = 0
attractor3D = 0
attractor3DSparre = 0
betaGammaFunctions = 0

# Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$'
# by An & Evans 2006. Ciotto et Al.


def Plt(data_list, i, x, y, cls, l, r, mode=None):
    """."""
    exec(f"data, label = {data_list}")
    if mode == 'log':
        exec(f"ax{i}.plot(np.log10(x), y, cls, label=label[{l}:{r}], lw=2, ms=7)")
    else:
        exec(f"ax{i}.plot(x, y, cls, label=label[{l}:{r}], lw=2, ms=7)")


if logrR2BetaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ---------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 7], data[:, 1], 'r-o', 0, -52, 'log')
    Plt(datalistB_R32[0], 1, data[:, 7], data[:, 1], 'b-s', 0, -52, 'log')
    Plt(datalistCS4_R32[0], 1, data[:, 7], data[:, 1], 'k-<', 0, -58, 'log')
    Plt(datalistCS5_R32[0], 1, data[:, 7], data[:, 1], 'y--v', 0, -58, 'log')
    Plt(datalistCS6_R32[0], 1, data[:, 7], data[:, 1], 'g--*', 0, -58, 'log')
    Plt(datalistDS1_R32[0], 1, data[:, 7], data[:, 1], 'm--s', 0, -58, 'log')
    Plt(datalistE_R32[0], 1, data[:, 7], data[:, 1], 'r--.', 0, -52, 'log')
    # Soft D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(np.log10(data[:, 7]), data[:, 1],
             'c--d', label='Soft_' + label[5:-52], lw=2, ms=7)

    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\beta$', fontsize=30)
    ax1.set_ylim(-.4, 1.)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[:, 7], data[:, 1], 'r-o', 0, -53, 'log')
    Plt(datalistB_R32[1], 2, data[:, 7], data[:, 1], 'b-s', 0, -54, 'log')
    Plt(datalistCS4_R32[1], 2, data[:, 7], data[:, 1], 'k-<', 0, -59, 'log')
    Plt(datalistCS5_R32[1], 2, data[:, 7], data[:, 1], 'y--v', 0, -59, 'log')
    Plt(datalistCS6_R32[1], 2, data[:, 7], data[:, 1], 'g--*', 0, -63, 'log')
    Plt(datalistDS1_R32[1], 2, data[:, 7], data[:, 1], 'm--s', 0, -59, 'log')
    Plt(datalistE_R32[1], 2, data[:, 7], data[:, 1], 'r--.', 0, -54, 'log')
    # Soft_D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(np.log10(data[:, 7]), data[:, 1],
             'c--d', label='Soft_' + label[5:-53], lw=2, ms=7)

    ax2.yaxis.tick_right()
    ax2.set_ylim(-.4, 1.)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=1, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'logrR2BetaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if logrR2KappaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 7], data[:, 3], 'r-o', 0, -52, 'log')
    Plt(datalistB_R32[0], 1, data[:, 7], data[:, 3], 'b-s', 0, -52, 'log')
    Plt(datalistCS4_R32[0], 1, data[:, 7], data[:, 3], 'k-<', 0, -58, 'log')
    Plt(datalistCS5_R32[0], 1, data[:, 7], data[:, 3], 'y--v', 0, -58, 'log')
    Plt(datalistCS6_R32[0], 1, data[:, 7], data[:, 3], 'g--*', 0, -58, 'log')
    Plt(datalistDS1_R32[0], 1, data[:, 7], data[:, 3], 'm--s', 0, -58, 'log')
    Plt(datalistE_R32[0], 1, data[:, 7], data[:, 3], 'r--.', 0, -52, 'log')
    # Soft_D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(np.log10(data[:, 7]), data[:, 3],
             'c--d', label='Soft_' + label[5:-52],
             lw=2, ms=7)

    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\kappa$', fontsize=30)
    ax1.set_ylim(-2., 2.)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[:, 7], data[:, 3], 'r-o', 0, -53, 'log')
    Plt(datalistB_R32[1], 2, data[:, 7], data[:, 3], 'b-s', 0, -54, 'log')
    Plt(datalistCS4_R32[1], 2, data[:, 7], data[:, 3], 'k-<', 0, -59, 'log')
    Plt(datalistCS5_R32[1], 2, data[:, 7], data[:, 3], 'y--v', 0, -59, 'log')
    Plt(datalistCS6_R32[1], 2, data[:, 7], data[:, 3], 'g--*', 0, -63, 'log')
    Plt(datalistDS1_R32[1], 2, data[:, 7], data[:, 3], 'm--s', 0, -59, 'log')
    Plt(datalistE_R32[1], 2, data[:, 7], data[:, 3], 'r--.', 0, -54, 'log')
    # Soft_D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(np.log10(data[:, 7]), data[:, 3],
             'c--d', label='Soft_' + label[5:-53], lw=2, ms=7)

    ax2.yaxis.tick_right()
    ax2.set_ylim(-1.5, .5)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=1, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'logrR2KappaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if logrR2GammaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 7], data[:, 2], 'r-o', 0, -52, 'log')
    Plt(datalistB_R32[0], 1, data[:, 7], data[:, 2], 'b-s', 0, -52, 'log')
    Plt(datalistCS4_R32[0], 1, data[:, 7], data[:, 2], 'k-<', 0, -58, 'log')
    Plt(datalistCS5_R32[0], 1, data[:, 7], data[:, 2], 'y--v', 0, -58, 'log')
    Plt(datalistCS6_R32[0], 1, data[:, 7], data[:, 2], 'g--*', 0, -58, 'log')
    Plt(datalistDS1_R32[0], 1, data[:, 7], data[:, 2], 'm--s', 0, -58, 'log')
    Plt(datalistE_R32[0], 1, data[:, 7], data[:, 2], 'r--.', 0, -52, 'log')

    # Soft_D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(np.log10(data[:, 7]), data[:, 2],
             'c--d', label='Soft_' + label[5:-52], lw=2, ms=7)

    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\gamma$', fontsize=30)
    ax1.set_ylim(-5., 0.)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[:, 7], data[:, 2], 'r-o', 0, -53, 'log')
    Plt(datalistB_R32[1], 2, data[:, 7], data[:, 2], 'b-s', 0, -54, 'log')
    Plt(datalistCS4_R32[1], 2, data[:, 7], data[:, 2], 'k-<', 0, -59, 'log')
    Plt(datalistCS5_R32[1], 2, data[:, 7], data[:, 2], 'y--v', 0, -59, 'log')
    Plt(datalistCS6_R32[1], 2, data[:, 7], data[:, 2], 'g--*', 0, -63, 'log')
    Plt(datalistDS1_R32[1], 2, data[:, 7], data[:, 2], 'm--s', 0, -59, 'log')
    Plt(datalistE_R32[1], 2, data[:, 7], data[:, 2], 'r--.', 0, -54, 'log')

    # Soft_D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(np.log10(data[:, 7]), data[:, 2],
             'c--d', label='Soft_' + label[5:-53], lw=2, ms=7)

    ax2.yaxis.tick_right()
    ax2.set_ylim(-4., 1.)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=1, ncol=1, fancybox=True,
                     loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'logrR2GammaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if logrBetaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 0], data[:, 1], 'r-o', 0, -52)
    Plt(datalistB_R32[0], 1, data[:, 0], data[:, 1], 'b-s', 0, -52)
    Plt(datalistCS4_R32[0], 1, data[:, 0], data[:, 1], 'k-<', 0, -58)
    Plt(datalistCS5_R32[0], 1, data[:, 0], data[:, 1], 'y--v', 0, -58)
    Plt(datalistCS6_R32[0], 1, data[:, 0], data[:, 1], 'g--*', 0, -58)
    Plt(datalistDS1_R32[0], 1, data[:, 0], data[:, 1], 'm--s', 0, -58)
    Plt(datalistE_R32[0], 1, data[:, 0], data[:, 1], 'r--.', 0, -52)

    # Soft_D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(data[:, 0], data[:, 1],
             'c--d', label='Soft_' + label[5:-52], lw=2, ms=7)

    ax1.set_xlabel(r'$\log r$', fontsize=30)
    ax1.set_ylabel(r'$\beta$', fontsize=30)
    ax1.set_ylim(-.4, 1.)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[:, 0], data[:, 1], 'r-o', 0, -53)
    Plt(datalistB_R32[1], 2, data[:, 0], data[:, 1], 'b-s', 0, -54)
    Plt(datalistCS4_R32[1], 2, data[:, 0], data[:, 1], 'k-<', 0, -59)
    Plt(datalistCS5_R32[1], 2, data[:, 0], data[:, 1], 'y--v', 0, -59)
    Plt(datalistCS6_R32[1], 2, data[:, 0], data[:, 1], 'g--*', 0, -63)
    Plt(datalistDS1_R32[1], 2, data[:, 0], data[:, 1], 'm--s', 0, -59)
    Plt(datalistE_R32[1], 2, data[:, 0], data[:, 1], 'r--.', 0, -54)

    # Soft_D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(data[:, 0], data[:, 1],
             'c--d', label='Soft_' + label[5:-53], lw=2, ms=7)

    ax2.yaxis.tick_right()
    ax2.set_ylim(-.4, 1.)
    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'logrBetaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if logrKappaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 0], data[:, 3], 'r-o', 0, -52)
    Plt(datalistB_R32[0], 1, data[:, 0], data[:, 3], 'b-s', 0, -52)
    Plt(datalistCS4_R32[0], 1, data[:, 0], data[:, 3], 'k-<', 0, -58)
    Plt(datalistCS5_R32[0], 1, data[:, 0], data[:, 3], 'y--v', 0, -58)
    Plt(datalistCS6_R32[0], 1, data[:, 0], data[:, 3], 'g--*', 0, -58)
    Plt(datalistDS1_R32[0], 1, data[:, 0], data[:, 3], 'm--s', 0, -58)
    Plt(datalistE_R32[0], 1, data[:, 0], data[:, 3], 'r--.', 0, -52)

    # Soft_D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(data[:, 0], data[:, 3],
             'c--d', label='Soft_' + label[5:-52], lw=2, ms=7)

    ax1.set_xlabel(r'$\log r$', fontsize=30)
    ax1.set_ylabel(r'$\kappa$', fontsize=30)
    ax1.set_ylim(-2., 2.)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[:, 0], data[:, 3], 'r-o', 0, -53)
    Plt(datalistB_R32[1], 2, data[:, 0], data[:, 3], 'b-s', 0, -54)
    Plt(datalistCS4_R32[1], 2, data[:, 0], data[:, 3], 'k-<', 0, -59)
    Plt(datalistCS5_R32[1], 2, data[:, 0], data[:, 3], 'y--v', 0, -59)
    Plt(datalistCS6_R32[1], 2, data[:, 0], data[:, 3], 'g--*', 0, -63)
    Plt(datalistDS1_R32[1], 2, data[:, 0], data[:, 3], 'm--s', 0, -59)
    Plt(datalistE_R32[1], 2, data[:, 0], data[:, 3], 'r--.', 0, -54)

    # Soft_D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(data[:, 0], data[:, 3],
             'c--d', label='Soft_' + label[5:-53], lw=2, ms=7)

    ax2.yaxis.tick_right()
    ax2.set_ylim(-2., 2.)
    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'logrKappaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if logrGammaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 0], data[:, 2], 'r-o', 0, -52)
    Plt(datalistB_R32[0], 1, data[:, 0], data[:, 2], 'b-s', 0, -52)
    Plt(datalistCS4_R32[0], 1, data[:, 0], data[:, 2], 'k-<', 0, -58)
    Plt(datalistCS5_R32[0], 1, data[:, 0], data[:, 2], 'y--v', 0, -58)
    Plt(datalistCS6_R32[0], 1, data[:, 0], data[:, 2], 'g--*', 0, -58)
    Plt(datalistDS1_R32[0], 1, data[:, 0], data[:, 2], 'm--s', 0, -58)
    Plt(datalistE_R32[0], 1, data[:, 0], data[:, 2], 'r--.', 0, -52)

    # Soft_D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(data[:, 0], data[:, 2],
             'c--d', label='Soft_' + label[5:-52], lw=2, ms=7)

    ax1.set_xlabel(r'$\log r$', fontsize=30)
    ax1.set_ylabel(r'$\gamma$', fontsize=30)
    ax1.set_ylim(-5., 0.)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[:, 0], data[:, 2], 'r-o', 0, -53)
    Plt(datalistB_R32[1], 2, data[:, 0], data[:, 2], 'b-s', 0, -54)
    Plt(datalistCS4_R32[1], 2, data[:, 0], data[:, 2], 'k-<', 0, -59)
    Plt(datalistCS5_R32[1], 2, data[:, 0], data[:, 2], 'y--v', 0, -59)
    Plt(datalistCS6_R32[1], 2, data[:, 0], data[:, 2], 'g--*', 0, -63)
    Plt(datalistDS1_R32[1], 2, data[:, 0], data[:, 2], 'm--s', 0, -59)
    Plt(datalistE_R32[1], 2, data[:, 0], data[:, 2], 'r--.', 0, -54)

    # Soft D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(data[:, 0], data[:, 2],
             'c--d', label='Soft_' + label[5:-53], lw=2, ms=7)

    ax2.yaxis.tick_right()
    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.set_title('Final', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'logrGammaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if betaGammaKappaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'r-o', 0, -52)
    Plt(datalistB_R32[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'b-s', 0, -52)
    Plt(datalistCS4_R32[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'k-<', 0, -58)
    Plt(datalistCS5_R32[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'y--v', 0, -58)
    Plt(datalistCS6_R32[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'g--*', 0, -58)
    Plt(datalistDS1_R32[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'm--s', 0, -58)
    Plt(datalistE_R32[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'r--.', 0, -52)

    # Soft_D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(data[:, 1], data[:, 2] + data[:, 3],
             'c--d', label='Soft_' + label[5:-52], lw=2, ms=7)

    # Annotation
    ax1.annotate('Inner region', xy=(0., -.5), xytext=(.4, -.5),
                 arrowprops=dict(facecolor='k', shrink=.05))
    ax1.annotate('Outer region', xy=(.9, -3.5), xytext=(.5, -3.),
                 arrowprops=dict(facecolor='k', shrink=.05))
    # Restriction
    x = np.linspace(-.3, 1.1)
    y = -2 * x
    ax1.plot(x, y, 'm', lw=2, ms=7)
    ax1.fill_between(x, 10, y, color='Violet')
    ax1.set_xlim(-.3, 1.1)
    ax1.set_ylim(-4., 0.)
    ax1.set_ylabel(r'$\gamma + \kappa$', fontsize=30)
    ax1.set_xlabel(r'$\beta$', fontsize=30)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[9:, 1], data[9:, 2] + data[9:, 3],
        'r-o', 0, -53)
    Plt(datalistB_R32[1], 2, data[6:, 1], data[6:, 2] + data[6:, 3],
        'b-s', 0, -54)
    Plt(datalistCS4_R32[1], 2, data[5:, 1], data[5:, 2] + data[5:, 3],
        'k-<', 0, -59)
    Plt(datalistCS5_R32[1], 2, data[5:, 1], data[5:, 2] + data[5:, 3],
        'y--v', 0, -59)
    Plt(datalistCS6_R32[1], 2, data[4:, 1], data[4:, 2] + data[4:, 3],
        'g--*', 0, -63)
    Plt(datalistDS1_R32[1], 2, data[3:, 1], data[3:, 2] + data[3:, 3],
        'm--s', 0, -59)
    Plt(datalistE_R32[1], 2, data[13:, 1], data[13:, 2] + data[13:, 3],
        'r--.', 0, -54)

    # Soft_D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(data[6:, 1], data[6:, 2] + data[6:, 3],
             'c--d', label='Soft_' + label[5:-53], lw=2, ms=7)

    # Martin Final
    data, label = datalistMartinFinal[0]
    ax2.plot(data[:, 4], data[:, 5] + data[:, 6],
             'b.', label=label[:] + '_Sparre', lw=2, ms=7)

    # Restriction
    x = np.linspace(-10., 2.)
    y = -2 * x
    ax2.plot(x, y, 'm', lw=2, ms=7)
    ax2.fill_between(x, 10, y, color='Violet')
    y = -5 * x - .8
    ax2.plot(x, y, 'k', label=r'$\beta=-0.2(\gamma + 0.8)$', lw=2, ms=7)
    ax2.yaxis.tick_right()
    ax2.set_xlim(-.2, 1.)
    ax2.set_ylim(-4., 0.)
    ax2.set_xlabel(r'$\beta$', fontsize=30)
    ax2.set_title('Final (with cuts)', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'betaGammaKappaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if betaGammaABCS4CS5CS6DS1D2E_ICFinalRLimit32:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R32[0], 1, data[:, 1], data[:, 2], 'r-o', 0, -52)
    Plt(datalistB_R32[0], 1, data[:, 1], data[:, 2], 'b-s', 0, -52)
    Plt(datalistCS4_R32[0], 1, data[:, 1], data[:, 2], 'k-<', 0, -58)
    Plt(datalistCS5_R32[0], 1, data[:, 1], data[:, 2], 'y--v', 0, -58)
    Plt(datalistCS6_R32[0], 1, data[:, 1], data[:, 2], 'g--*', 0, -58)
    Plt(datalistDS1_R32[0], 1, data[:, 1], data[:, 2], 'm--s', 0, -58)
    Plt(datalistE_R32[0], 1, data[:, 1], data[:, 2], 'b-<', 0, -52)

    # Soft_D2
    data, label = datalistSoftD2_R32[0]
    ax1.plot(data[:, 1], data[:, 2], 'r--.', label='Soft_' + label[5:-52],
             lw=2, ms=7)

    # Annotation
    ax1.annotate('Inner region', xy=(0., -.5), xytext=(.4, -.5),
                 arrowprops=dict(facecolor='k', shrink=.05))
    ax1.annotate('Outer region', xy=(.9, -3.), xytext=(.5, -2.5),
                 arrowprops=dict(facecolor='k', shrink=.05))
    # Restriction
    x = np.linspace(-.3, 1.1)
    y = -2 * x
    ax1.plot(x, y, 'm', lw=2, ms=7)
    ax1.fill_between(x, 10, y, color='Violet')
    ax1.set_xlim(-.2, 1.)
    ax1.set_ylim(-4., 0.)
    ax1.set_ylabel(r'$\gamma$', fontsize=30)
    ax1.set_xlabel(r'$\beta$', fontsize=30)
    ax1.set_title(r'IC ($R_{limit} = 32$)', fontsize=30)

    # Final ------------------------------------------------------------
    Plt(datalistA_R32[1], 2, data[9:, 1], data[9:, 2], 'r-o', 0, -53)
    Plt(datalistB_R32[1], 2, data[6:, 1], data[6:, 2], 'b-s', 0, -54)
    Plt(datalistCS4_R32[1], 2, data[5:, 1], data[5:, 2], 'k-<', 0, -59)
    Plt(datalistCS5_R32[1], 2, data[5:, 1], data[5:, 2], 'y--v', 0, -59)
    Plt(datalistCS6_R32[1], 2, data[4:, 1], data[4:, 2], 'g--*', 0, -63)
    Plt(datalistDS1_R32[1], 2, data[3:, 1], data[3:, 2], 'm--s', 0, -59)
    Plt(datalistE_R32[1], 2, data[13:, 1], data[13:, 2], 'b-<', 0, -54)

    # Soft D2
    data, label = datalistSoftD2_R32[1]
    ax2.plot(data[6:, 1], data[6:, 2], 'r--.', label='Soft_' + label[5:-53],
             lw=2, ms=7)

    # Martin Final
    data, label = datalistMartinFinal[0]
    ax2.plot(data[:, 4], data[:, 5], 'k--v', label=label[:] + '_Sparre',
             lw=2, ms=7)

    # Restriction
    x = np.linspace(-10., 2.)
    y = -2 * x
    ax2.plot(x, y, 'm', lw=2, ms=7)
    ax2.fill_between(x, 10, y, color='Violet')
    y = -5 * x - .8
    ax2.plot(x, y, 'k', label=r'$\beta=-0.2(\gamma + 0.8)$', lw=2,ms=7)
    ax2.yaxis.tick_right()
    ax2.set_xlim(-.2, 1.)
    ax2.set_ylim(-4., 0.)
    ax2.set_xlabel(r'$\beta$', fontsize=30)
    ax2.set_title('Final (with cuts)', fontsize=30)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath +
              'betaGammaABCS4CS5CS6DS1D2E_ICFinalRLimit32.png')

if betaGammaKappaABCS4CS5CS6DS1D2E_ICFinal20BinsRLimit10000:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R10000[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'r-o', 0, -55)
    Plt(datalistB_R10000[2], 1, data[:, 1], data[:, 2] + data[:, 3],
        'b-s', 0, -55)
    Plt(datalistDS1_SoftD2_R10000[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'k-<', 0, -61)
    Plt(datalistE_R10000[0], 1, data[:, 1], data[:, 2] + data[:, 3],
        'g--*', 0, -55)

    # CS4, CS5 and CS6
    for i in range(3):
        data, label = datalistCS4CS5CS6_R10000[i]
        ax1.plot(data[:, 1], data[:, 2] + data[:, 3],
                 Symbols[i + 2], color=Colors[i + 2], label=label[:-61],
                 lw=2, ms=7)

    # Soft_D2
    data, label = datalistDS1_SoftD2_R10000[1]
    ax1.plot(data[:, 1], data[:, 2] + data[:, 3], 'r--.',
             label='Soft_' + label[:-55], lw=2, ms=7)

    # Restriction
    x = np.linspace(-.3, 1.1)
    y = -2 * x
    ax1.plot(x, y, 'm', lw=2, ms=7)
    ax1.fill_between(x, 10, y, color='Violet')
    ax1.set_ylabel(r'$\gamma + \kappa$', fontsize=30)
    ax1.set_xlabel(r'$\beta$', fontsize=30)
    ax1.set_xlim(-.3, 1.1)
    ax1.set_ylim(-9., 0.)
    ax1.set_title(r'IC ($R_{limit} = 10^4, 20$ bins)', fontsize=30)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    # Final ------------------------------------------------------------
    Plt(datalistA_R10000[1], 2, data[3:-2, 1], data[3:-2, 2] + data[3:-2, 3],
        'r-o', 0, -55)
    Plt(datalistB_R10000[3], 2, data[4:-2, 1], data[4:-2, 2] + data[4:-2, 3],
        'b-s', 0, -55)
    Plt(datalistDS1_SoftD2_R10000[2], 2, data[3:-2, 1],
        data[3:-2, 2] + data[3:-2, 3], 'k-<', 0, -61)
    Plt(datalistE_R10000[1], 2, data[3:-2, 1], data[3:-2, 2] + data[3:-2, 3],
        'y--v', 0, -55)
    Plt(datalistA_R10000[1], 2, data[:, 1], data[:, 2] + data[:, 3],
        'g--*', 0, -55)
    Plt(datalistB_R10000[3], 2, data[:, 1], data[:, 2] + data[:, 3],
        'm--s', 0, -55)
    Plt(datalistE_R10000[1], 2, data[:, 1], data[:, 2] + data[:, 3],
        'r--.', 0, -55)

    # CS4, CS5 and CS6
    for i in range(3, 6):
        data, label = datalistCS4CS5CS6_R10000[i]
        ax2.plot(data[:, 1], data[:, 2] + data[:, 3],
                 Symbols[i - 1], color=Colors[i - 1], label=label[:-61],
                 lw=2, ms=7)

    # CS4, CS5 and CS6
    for i in range(3, 6):
        data, label = datalistCS4CS5CS6_R10000[i]
        ax2.plot(data[3:-2, 1], data[3:-2, 2] + data[3:-2, 3],
                 Symbols[i - 1], color=Colors[i - 1], label=label[:-61],
                 lw=2, ms=7)

    data, label = datalistDS1_SoftD2_R10000[3]
    ax2.plot(data[3:-2, 1], data[3:-2, 2] + data[3:-2, 3],
             'r--.', label='Soft_' + label[:-55], lw=2, ms=7)

    # Restriction
    x = np.linspace(-10., 2.)
    ax2.plot(x, y, 'm', lw=2, ms=7)
    ax2.fill_between(x, 10, y, color='Violet')
    ax2.yaxis.tick_right()
    ax2.set_xlim(-.3, 1.)
    ax2.set_ylim(-5.2, 1.2)
    ax2.set_title('Final', fontsize=30)
    f.savefig(figurePath +
              'betaGammaKappaABCS4CS5CS6DS1D2E_ICFinal20BinsRLimit10000.png')

if betaGammaABCS4CS5CS6DS1D2E_ICFinal20BinsRLimit10000:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    Plt(datalistA_R10000[0], 1, data[:, 1], data[:, 2], 'r-o', 0, -55)
    Plt(datalistB_R10000[2], 1, data[:, 1], data[:, 2], 'b-s', 0, -55)
    Plt(datalistDS1_SoftD2_R10000[0], 1, data[:, 1], data[:, 2],
        'm--s', 0, -61)
    Plt(datalistE_R10000[0], 1, data[:, 1], data[:, 2], 'r--.', 0, -55)

    # CS4, CS5 and CS6
    for i in range(3):
        data, label = datalistCS4CS5CS6_R10000[i]
        ax1.plot(data[:, 1], data[:, 2],
                 Symbols[i + 2], color=Colors[i + 2], label=label[:-61],
                 lw=2, ms=7)

    # Soft D2
    data, label = datalistDS1_SoftD2_R10000[1]
    ax1.plot(data[:, 1], data[:, 2], 'c--d',
             label='Soft_' + label[:-55], lw=2, ms=7)

    # Restriction
    x = np.linspace(-.3, 1.1)
    y = -2 * x
    ax1.plot(x, y, 'm', lw=2, ms=7)
    ax1.fill_between(x, 10, y, color='Violet')
    ax1.set_ylabel(r'$\gamma$', fontsize=30)
    ax1.set_xlabel(r'$\beta$', fontsize=30)
    ax1.set_xlim(-.2, 1.)
    ax1.set_ylim(-5., 0.)
    ax1.set_title(r'IC ($R_{limit} = 10^4, 20$ bins)', fontsize=30)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    # Final ------------------------------------------------------------
    Plt(datalistA_R10000[1], 2, data[1:-9, 1], data[1:-9, 2], 'r-o', 0, -55)
    Plt(datalistB_R10000[3], 2, data[3:-5, 1], data[3:-5, 2], 'b-s', 0, -55)
    Plt(datalistCS4CS5CS6_R10000[3], 2, data[5:-7, 1], data[5:-7, 2],
        'k-<', 0, -61)
    Plt(datalistCS4CS5CS6_R10000[4], 2, data[4:-6, 1], data[4:-6, 2],
        'y--v', 0, -61)
    Plt(datalistCS4CS5CS6_R10000[5], 2, data[3:-7, 1], data[3:-7, 2],
        'g--*', 0, -61)
    Plt(datalistDS1_SoftD2_R10000[2], 2, data[2:-8, 1], data[2:-8, 2],
        'm--s', 0, -61)
    Plt(datalistE_R10000[1], 2, data[2:-6, 1], data[2:-6, 2], 'r--.', 0, -55)

    # Soft_D2
    data, label = datalistDS1_SoftD2_R10000[3]
    ax2.plot(data[4:-9, 1], data[4:-9, 2], 'c--d',
             label='Soft_' + label[:-55], lw=2, ms=7)

    # Restriction
    x = np.linspace(-10., 2.)
    ax2.plot(x, y, 'm', lw=2, ms=7)
    ax2.fill_between(x, 10, y, color='Violet')
    ax2.yaxis.tick_right()
    ax2.set_xlim(-.1, .25)
    ax2.set_ylim(-4., .1)
    ax2.set_title('Final', fontsize=30)
    f.savefig(figurePath +
              'betaGammaABCS4CS5CS6DS1D2E_ICFinal20BinsRLimit10000.png')

if betaGammaKappaCS1CS2CS3_20_50Bins:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    data, _ = datalistC_IC[0]  # IC 50 bins
    ax1.plot(data[:, 1], data[:, 2], 'r-o', label='CS1', lw=2, ms=7)
    data, _ = datalistC_IC[1]
    ax1.plot(data[:, 1], data[:, 2], 'b-s', label='CS2', lw=2, ms=7)
    data, _ = datalistC_IC[2]
    ax1.plot(data[:, 1], data[:, 2], 'k-<', label='CS3', lw=2, ms=7)
    x = np.linspace(-2., 2.)
    y = -2 * x
    ax1.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    ax1.fill_between(x, 4, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma}{2}$')
    # Unstable region.
    ax1.set_title(r'IC. 50 bins', fontsize=30)
    ax1.set_ylabel(r'$\gamma$', fontsize=30)
    ax1.set_xlim(-2.5, 1.1)
    ax1.set_ylim(-8., 2.)
    ax1.axes.get_xaxis().set_visible(False)
    ax1.tick_params(axis='both', which='both', bottom='on', top='off',
                    labelbottom='on', right='off', left='on', labelleft='on')

    data, _ = datalistC_IC[3]  # IC 20 bins
    ax2.plot(data[:, 1], data[:, 2], 'r-o', label='CS1', lw=2, ms=7)
    data, _ = datalistC_IC[4]
    ax2.plot(data[:, 1], data[:, 2], 'b-s', label='CS2', lw=2, ms=7)
    data, _ = datalistC_IC[5]
    ax2.plot(data[:, 1], data[:, 2], 'k-<', label='CS3', lw=2, ms=7)
    x = np.linspace(-2., 2.)
    y = -2 * x
    ax2.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma}{2}$', lw=2, ms=7)
    ax2.fill_between(x, 4, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma}{2}$')
    # Unstable region.
    ax2.set_title('20 bins', fontsize=30)
    ax2.set_xlim(-.7, 1.1)
    ax2.set_ylim(-5., -.8)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.yaxis.tick_right()

    data, _ = datalistC_IC[0]  # IC 50 bins
    ax3.plot(data[:, 1], data[:, 3], 'r-o', label='CS1', lw=2, ms=7)
    data, _ = datalistC_IC[1]
    ax3.plot(data[:, 1], data[:, 3], 'b-s', label='CS2', lw=2, ms=7)
    data, _ = datalistC_IC[2]
    ax3.plot(data[:, 1], data[:, 3], 'k-<', label='CS3', lw=2, ms=7)
    ax3.set_xlabel(r'$\beta$', fontsize=30)
    ax3.set_ylabel(r'$\kappa$', fontsize=30)
    ax3.set_xlim(-2.5, 1.1)
    ax3.set_ylim(-10., 7.)

    data, _ = datalistC_IC[3]  # IC 20 bins
    ax4.plot(data[:, 1], data[:, 3], 'r-o', label='CS1', lw=2, ms=7)
    data, _ = datalistC_IC[4]
    ax4.plot(data[:, 1], data[:, 3], 'b-s', label='CS2', lw=2, ms=7)
    data, _ = datalistC_IC[5]
    ax4.plot(data[:, 1], data[:, 3], 'k-<', label='CS3', lw=2, ms=7)
    ax4.set_xlim(-.7, 1.1)
    ax4.set_ylim(-2.3, .8)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax4.yaxis.tick_right()
    f.savefig(figurePath +
              'betaGammaKappaCS1CS2CS3_20_50Bins.png')

if betaGammaKappaCS4CS5CS6_20_50Bins:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    data, _ = datalistC_IC[6]
    ax1.plot(data[:, 1], data[:, 2], 'r-o', label='CS4', lw=2, ms=7)
    data, _ = datalistC_IC[7]
    ax1.plot(data[:, 1], data[:, 2], 'b-s', label='CS5', lw=2, ms=7)
    data, _ = datalistC_IC[8]
    ax1.plot(data[:, 1], data[:, 2], 'k-<', label='CS6', lw=2, ms=7)
    x = np.linspace(-2., 2.)
    y = -2 * x
    ax1.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    ax1.fill_between(x, 4, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    # Unstable region
    ax1.set_title(r'Initial conditions. 50 bins', fontsize=20)
    ax1.set_ylabel(r'$\gamma$', fontsize=24)
    ax1.set_xlim(-.3, 1.1)
    ax1.set_ylim(-4.7, -1.)
    ax1.axes.get_xaxis().set_visible(False)

    data, _ = datalistC_IC[9]
    ax2.plot(data[:, 1], data[:, 2], 'r-o', label='CS4', lw=2, ms=7)
    data, _ = datalistC_IC[10]
    ax2.plot(data[:, 1], data[:, 2], 'b-s', label='CS5', lw=2, ms=7)
    data, _ = datalistC_IC[11]
    ax2.plot(data[:, 1], data[:, 2], 'k-<', label='CS6', lw=2, ms=7)
    x = np.linspace(-2., 2.)
    y = -2 * x
    ax2.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    # Unstable region
    ax2.fill_between(x, 4, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.set_title('20 bins', fontsize=20)
    ax2.set_xlim(-.2, 1.1)
    ax2.set_ylim(-4.7, -1.)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    data, _ = datalistC_IC[6]
    ax3.plot(data[:, 1], data[:, 3], 'r-o', label='CS4', lw=2, ms=7)
    data, _ = datalistC_IC[7]
    ax3.plot(data[:, 1], data[:, 3], 'b-s', label='CS5', lw=2, ms=7)
    data, _ = datalistC_IC[8]
    ax3.plot(data[:, 1], data[:, 3], 'k-<', label='CS6', lw=2, ms=7)
    ax3.set_xlabel(r'$\beta$', fontsize=24)
    ax3.set_ylabel(r'$\kappa$', fontsize=24)
    ax3.set_xlim(-.3, 1.1)
    ax3.set_ylim(-6., 3.)

    data, label = datalistC_IC[9]
    ax4.plot(data[:, 1], data[:, 3], 'r-o', label=label[:-15], lw=2, ms=7)
    data, label = datalistC_IC[10]
    ax4.plot(data[:, 1], data[:, 3], 'b-s', label=label[:-15], lw=2, ms=7)
    data, label = datalistC_IC[11]
    ax4.plot(data[:, 1], data[:, 3], 'k-<', label=label[:-15], lw=2, ms=7)
    ax4.set_xlim(-.2, 1.1)
    ax4.set_ylim(-6., 3.)
    ax4.axes.get_yaxis().set_visible(False)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath + 'betaGammaKappaCS4CS5CS6_20_50Bins.png')

# betaGammaKappaCS4CS5CS6_Final20_50Bins
# betaGammaKappaDS1D2_20_50Bins
# betaGammaKappaDS1D2_Final20_50Bins
# betaGammaKappaRfpBCS4CS5CS6DS1D2_Final50BinsRLimit10000

if betaGammaKappaBCS4CS5CS6DS1D2_ICFinal20_50Bins:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6),
        (ax7, ax8)) = plt.subplots(4, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    # IC ------------------------------------------------------------
    # B
    data, label = datalistB[0]
    ax1.plot(data[:, 1], data[:, 2] + data[:, 3], 'r-o',
             label=label, lw=2, ms=7)
    # CS4, CS5 and CS6
    for i in range(6, 9):
        data, label = datalistC_IC[i]
        ax1.plot(data[:, 1], data[:, 2] + data[:, 3],
                 Symbols[i - 5], color=Colors[i - 5], label=label, lw=2, ms=7)

    # Restriction
    x = np.linspace(-.3, 1.1)
    y = -2 * x
    ax1.plot(x, y, 'm', lw=2, ms=7)
    ax1.fill_between(x, 10, y, color='Violet')
    ax1.set_title(r'IC $\gamma + \kappa$', fontsize=20)
    ax1.set_ylabel(r'50 bins', fontsize=18)
    ax1.set_xlim(-.3, 1.1)
    ax1.set_ylim(-10., 10.)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     frameon=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.axes.get_xaxis().set_visible(False)

    # Final ------------------------------------------------------------
    # B
    data, label = datalistB[5]
    ax2.plot(data[:, 1], data[:, 2] + data[:, 3], 'r-o',
             label=label, lw=2, ms=7)
    # Restriction
    x = np.linspace(-10., 2.)
    ax2.plot(x, y, 'm', lw=2, ms=7)
    ax2.fill_between(x, 10, y, color='Violet')
    ax2.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='off', right='off', left='off',
                    labelleft='off')
    ax2.set_title(r'Final $\gamma + \kappa$', fontsize=20)
    ax2.set_xlim(-1., 1.5)
    ax2.set_ylim(-10., 10.)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_ylabel(r'$R_{limit} = 5 \cdot 10^2$', fontsize=18)
    ax2.yaxis.set_label_position("right")

    # IC ------------------------------------------------------------
    # B
    data, label = datalistB20[0]
    ax3.plot(data[:, 1], data[:, 2] + data[:, 3],
             Symbols[0], color=Colors[0], label=label[:-15], lw=2, ms=7)
    # CS4, CS5 and CS6
    for i in range(9, 12):
        data, label = datalistC_IC[i]
        ax3.plot(data[:, 1], data[:, 2] + data[:, 3],
                 Symbols[i - 8], color=Colors[i - 8], label=label[:-15],
                 lw=2, ms=7)
    # Restriction
    x = np.linspace(-.3, 1.1)
    ax3.plot(x, y, 'm', lw=2, ms=7)
    ax3.fill_between(x, 10, y, color='Violet')
    ax3.set_ylabel(r'20 bins', fontsize=18)
    ax3.set_xlim(-.3, 1.1)
    ax3.set_ylim(-10., 10.)
    ax3.axes.get_xaxis().set_visible(False)

    # Final ------------------------------------------------------------
    # B
    data, label = datalistB20[1]
    ax4.plot(data[:, 1], data[:, 2] + data[:, 3], 'r-o',
             label=label[:-15], lw=2, ms=7)

    # Restriction
    x = np.linspace(-10., 2.)
    ax4.plot(x, y, 'm', lw=2, ms=7)
    ax4.fill_between(x, 10, y, color='Violet')
    ax4.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='off', right='off', left='off',
                    labelleft='off')
    ax4.set_xlim(-1., 1.5)
    ax4.set_ylim(-10., 10.)
    ax4.set_ylabel(r'$R_{limit} = 5 \cdot 10^2$', fontsize=18)
    ax4.yaxis.set_label_position("right")

    # IC ------------------------------------------------------------

    # Restriction
    x = np.linspace(-.3, 1.1)
    y = -2 * x
    ax5.plot(x, y, 'm', lw=2, ms=7)
    ax5.fill_between(x, 10, y, color='Violet')
    ax5.set_ylabel(r'50 bins', fontsize=18)
    ax5.set_xlim(-.3, 1.1)
    ax5.set_ylim(-10., 10.)
    ax5.axes.get_xaxis().set_visible(False)

    # Final ------------------------------------------------------------

    # Restriction
    x = np.linspace(-10., 2.)
    ax6.plot(x, y, 'm', lw=2, ms=7)
    ax6.fill_between(x, 10, y, color='Violet')
    ax6.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='off', right='off', left='off',
                    labelleft='off')
    ax6.set_xlim(-1., 1.5)
    ax6.set_ylim(-10., 10.)
    ax6.set_ylabel(r'$R_{limit} = 10^4$', fontsize=18)
    ax6.yaxis.set_label_position("right")
    # IC

    f.savefig(figurePath +
              'betaGammaKappaBCS4CS5CS6DS1D2_ICFinal20_50Bins.png')

if overplotICFinal:
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(len(datalistMartinIC)):
        data, label = datalistMartinIC[i]
        ax1.plot(data[:, 0], data[:, 1],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    for i in range(len(datalistMartinFinal)):
        data, label = datalistMartinFinal[i]
        ax1.plot(data[:, 4], data[:, 5],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    x = np.linspace(0, 1.1)
    y = -2 * x
    ax1.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    ax1.fill_between(x, 0, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.set_title(r'IC and Final', fontsize=20)
    ax1.set_ylabel(r'$\gamma$', fontsize=24)
    ax1.set_xlim(-0.1, 1.1)
    ax1.set_ylim(-4., 0.)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(len(datalistMartinIC)):
        data, label = datalistMartinIC[i]
        ax2.plot(data[:, 0], data[:, 2],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    for i in range(len(datalistMartinFinal)):
        data, label = datalistMartinFinal[i]
        ax2.plot(data[:, 4], data[:, 6],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)

    ax2.set_xlabel(r'$\beta$', fontsize=24)
    ax2.set_ylabel(r'$\kappa$', fontsize=24)
    ax2.set_xlim(-0.1, 1.1)
    ax2.set_ylim(-2., 2.)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath + 'overplotICFinal.png')

if ICFinal4Subplots:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(len(datalistMartinIC)):
        data, label = datalistMartinIC[i]
        ax1.plot(data[:, 0], data[:, 1],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    x = np.linspace(0, 1.1)
    y = -2 * x
    ax1.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    ax1.fill_between(x, 0, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.set_title('IC', fontsize=30)
    ax1.set_ylabel(r'$\gamma$', fontsize=30)
    ax1.set_xlim(-.1, 1.1)
    ax1.set_ylim(-6., 0.)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(len(datalistMartinFinal)):
        data, label = datalistMartinFinal[i]
        ax2.plot(data[:, 4], data[:, 5],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    ax2.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    ax2.fill_between(x, 0, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.set_title(r'Final', fontsize=30)
    ax2.set_xlim(-.1, 1.1)
    ax2.set_ylim(-6., 0.)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    for i in range(len(datalistMartinIC)):
        data, label = datalistMartinIC[i]
        ax3.plot(data[:, 0], data[:, 2],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    ax3.set_xlabel(r'$\beta$', fontsize=30)
    ax3.set_ylabel(r'$\kappa$', fontsize=30)
    ax3.set_xlim(-.1, 1.1)
    ax3.set_ylim(-5., 2.)
    leg = ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     frameon=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    for i in range(len(datalistMartinFinal)):
        data, label = datalistMartinFinal[i]
        ax4.plot(data[:, 4], data[:, 6],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    ax4.set_xlim(-.1, 1.1)
    ax4.set_ylim(-5., 2.)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=2,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax4.axes.get_yaxis().set_visible(False)
    f.savefig(figurePath + 'ICFinal4Subplots.png')

if finalGammaBetaFit:
    f = plt.figure()
    for i in range(len(datalistMartinFinal)):
        data, label = datalistMartinFinal[i]
        plt.plot(data[:, 4], data[:, 5],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    x = np.linspace(0, 1.1)
    y1 = -2 * x
    y2 = -5 * x - .8
    y3 = -.5 * np.exp(1. * np.exp(1. * x))  # Gompertz function
    y4 = -1. / (1. + .01 * .1 ** (-x))  # Logistic function
    y5 = -5 * np.sin(x) / np.cos(x)
    # y6 = 1 * np.exp(-2 * x)
    # y7 = a / (1 + bc ** (-x))
    # y8 = ae^-be^-ct
    plt.plot(x, y1, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    plt.plot(x, y2, 'k', label=r'$\beta=-0.2(\gamma + 0.8)$', lw=2, ms=7)
    # plt.plot(x, y3, color='k', label=r'Gompertz function', lw=2, ms=7)
    # plt.plot(x, y4, color='k', label=r'Logistic function', lw=2, ms=7)
    # plt.plot(x, y5, color='k', label=r'arccot fit', lw=2, ms=7)
    # plt.plot(x, y6, color='k', label=r'Exponential fit', lw=2, ms=7)
    plt.fill_between(x, 0, y, color='c',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    plt.title(r'Final', fontsize=20)
    plt.xlim(-.1, 1.1)
    plt.ylim(-6., 0.)
    plt.ylabel(r'$\gamma$', fontsize=24)
    plt.xlabel(r'$\beta$', fontsize=24)
    leg = plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    f.savefig(figurePath + 'finalGammaBetaFit.png')

if betaVsGammaPlusKappa:
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    for i in range(len(datalistMartinIC)):
        data, label = datalistMartinIC[i]
        ax1.plot(data[:, 0], data[:, 1] + data[:, 2],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    x = np.linspace(0, 1.2)
    y = -2 * x
    ax1.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    ax1.fill_between(x, 0, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.set_title(r'$\gamma + \kappa$', fontsize=30)
    ax1.set_xlabel(r'$\beta$', fontsize=30)
    ax1.set_ylabel(r'IC', fontsize=30)
    ax1.set_xlim(-.1, 1.)
    ax1.set_ylim(-6., 0.)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(len(datalistMartinFinal)):
        data, label = datalistMartinFinal[i]
        ax2.plot(data[:, 4], data[:, 5] + data[:, 6],
                 Symbols[i], color=Colors[i], label=label, lw=2, ms=7)
    ax2.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma }{2}$', lw=2, ms=7)
    ax2.fill_between(x, 0, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma }{2}$')
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$', fontsize=30)
    ax2.set_ylabel(r'Final', fontsize=30)
    ax2.set_xlim(-.1, 1.)
    ax2.set_ylim(-4.5, 0.)
    f.savefig(figurePath + 'betaVsGammaPlusKappa.png')

if attractor3D:  # 3D plots of attractor, IC and Final.
    f = plt.figure(figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax = f.add_subplot(121, projection='3d')
    n = 100

    # IC ------------------------------------------------------------
    # A
    data, label = datalistA_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'r-o', label=label, lw=2)
    # B
    data, label = datalistB_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'b-s', label=label, lw=2)
    # CS4
    data, label = datalistCS4_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'g-<', label=label, lw=2)
    # CS5
    data, label = datalistCS5_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'k--v', label=label, lw=2)
    # CS6
    data, label = datalistCS6_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'c--*', label=label, lw=2)
    # DS1
    data, label = datalistDS1_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'm--s', label=label, lw=2)
    # Soft D2
    data, label = datalistSoftD2_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'y--d', label=label, lw=2)
    # E
    data, label = datalistE_R32[0]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'r--.', label=label, lw=2)

    handles = []
    scatter1_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='r', marker='-o')
    scatter2_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='b', marker='-s')
    scatter3_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='g', marker='-<')
    scatter4_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='k', marker='--v')
    scatter5_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='c', marker='--*')
    scatter6_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='m', marker='--s')
    scatter7_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='y', marker='--d')
    scatter8_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='r', marker='--.')
    leg = ax.legend([scatter1_proxy, scatter2_proxy, scatter3_proxy,
                     scatter4_proxy, scatter5_proxy, scatter6_proxy,
                     scatter7_proxy, scatter8_proxy],
                    ['A', 'B', 'CS4', 'CS5', 'CS6', 'DS1', 'Soft D2', 'E'],
                    loc=0, numpoints=1, fancybox=True)
    leg.get_frame().set_alpha(.5)
    ax.set_xlabel(r'$2 \beta$', fontsize=30)
    ax.set_ylabel(r'$\gamma$', fontsize=30)
    ax.set_zlabel(r'$\kappa$', fontsize=30)
    ax.set_title('IC', fontsize=30)

    ax = f.add_subplot(122, projection='3d')
    n = 100

    # Final ------------------------------------------------------------
    # A
    data, label = datalistA_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'r-o', label=label, lw=2)
    # B
    data, label = datalistB_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'b-s', label=label, lw=2)
    # CS4
    data, label = datalistCS4_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'g-<', label=label, lw=2)
    # CS5
    data, label = datalistCS5_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'k--v', label=label, lw=2)
    # CS6
    data, label = datalistCS6_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'c--*', label=label, lw=2)
    # DS1
    data, label = datalistDS1_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'm--s', label=label, lw=2)
    # Soft D2
    data, label = datalistSoftD2_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'y--d', label=label, lw=2)
    # E
    data, label = datalistE_R32[1]
    ax.plot(2 * data[:, 1], data[:, 2], data[:, 3], 'r--.', label=label, lw=2)

    handles = []
    scatter1_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='r', marker='-o')
    scatter2_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='b', marker='-s')
    scatter3_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='g', marker='-<')
    scatter4_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='k', marker='--v')
    scatter5_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='c', marker='--*')
    scatter6_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='m', marker='--s')
    scatter7_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='y', marker='--d')
    scatter8_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='r', marker='--.')
    # leg = ax.legend([scatter1_proxy, scatter2_proxy, scatter3_proxy,
    #                  scatter4_proxy, scatter5_proxy, scatter6_proxy,
    #                  scatter7_proxy, scatter8_proxy],
    #                 ['A', 'B', 'CS4', 'CS5', 'CS6', 'DS1', 'Soft D2', 'E'],
    #                 loc=0, numpoints=1, fancybox=True)
    # leg.get_frame().set_alpha(.5)
    ax.set_xlabel(r'$2 \beta$', fontsize=30)
    ax.set_ylabel(r'$\gamma$', fontsize=30)
    ax.set_zlabel(r'$\kappa$', fontsize=30)
    ax.set_title('Final', fontsize=30)
    ax.set_xlim(-2., 2.)
    ax.set_ylim(-4., 0.)
    ax.set_zlim(-2., 1.)
    f.savefig(figurePath + 'Attractor3D.png')

if attractor3DSparre:  # 3D plots of attractor, IC and Final.
    f = plt.figure(figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax = f.add_subplot(121, projection='3d')
    n = 100
    for i in range(len(datalistMartinIC)):
        data, label = datalistMartinIC[i]
        ax.plot(2 * data[:, 0], data[:, 1], data[:, 2],
                marker=Symbols[i], color=Colors[i], label=label, lw=2)
    handles = []
    scatter1_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='r', marker='-o')
    scatter2_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='b', marker='-s')
    scatter3_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='g', marker='-<')
    leg = ax.legend([scatter1_proxy, scatter2_proxy, scatter3_proxy],
                    ['OMG00_001_IC_000', '0G00_IC_000', 'OMG20_IC_000'],
                    loc=0, numpoints=1, fancybox=True)
    leg.get_frame().set_alpha(.5)
    ax.set_xlabel(r'$2 \beta$', fontsize=30)
    ax.set_ylabel(r'$\gamma$', fontsize=30)
    ax.set_zlabel(r'$\kappa$', fontsize=30)
    ax.set_title('IC', fontsize=30)
    ax = f.add_subplot(122, projection='3d')
    n = 100
    for i in range(len(datalistMartinFinal)):
        data, label = datalistMartinFinal[i]
        ax.plot(2 * data[:, 0], data[:, 1], data[:, 2],
                marker=Symbols[i], color=Colors[i], label=label, lw=2)
    handles = []

    scatter1_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='r', marker='-o')
    scatter2_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='b', marker='-s')
    scatter3_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='g', marker='-<')
    scatter4_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='k', marker='--v')
    scatter5_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='c', marker='--*')
    scatter6_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='m', marker='--s')
    scatter7_proxy = lines.Line2D([0], [0], linestyle="none",
                                  c='y', marker='--d')

    leg = ax.legend([scatter1_proxy, scatter2_proxy, scatter3_proxy,
                     scatter4_proxy, scatter5_proxy, scatter6_proxy,
                     scatter7_proxy],
                    ['0G20_001', '00-5G20_001', 'om0-3.5G20_001',
                     's1G20_001', 's2G20_001', 's3G20_001',
                     's4G20_001'],
                    loc=0, numpoints=1, fancybox=True)
    leg.get_frame().set_alpha(.5)
    ax.set_xlabel(r'$2 \beta$', fontsize=30)
    ax.set_ylabel(r'$\gamma$', fontsize=30)
    ax.set_zlabel(r'$\kappa$', fontsize=30)
    ax.set_title('Final', fontsize=30)
    ax.set_xlim(-2., 2.)
    f.savefig(figurePath + 'attractor3DSparre.png')

if betaGammaFunctions:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    r = np.linspace(.1, 1.2)
    # restriction
    x = np.linspace(0., 1.2)
    y = -2 * x
    ax1.plot(x, y, 'm', label=r'$\beta=-\frac{\gamma}{2}$', lw=2, ms=7)
    ax1.fill_between(x, 0, y, color='Violet',
                     label=r'$\beta > -\frac{\gamma}{2}$')

    # print(f'betaOM(r, 1.20) = {betaOM(r)}')
    # print(r'rhoHQ(r, $ \frac{1}{2\pi}$, 1.)) = ',
    #         rhoHQ(r, 1. / (2. * np.pi), 1.))
    # print(r'gammaHQ(r, $ \frac{1}{2\pi}$, 1. ) = ',
    # gammaHQ(r))

    gamma_arr = []
    # r, rho0, rS
    gammaHQ = Sigma_calc.gamma_func(radii=r,
                                    density=rhoHQ(r, 1. / (2. * np.pi), 1.),
                                    len_obj_1=r, len_obj_2=r)

    ax1.plot(betaOM(r, 1.40), gammaHQ, 'r-o', mew=0, label=r'$rA = 1.4$',
             lw=2, ms=7)
    ax1.plot(betaOM(r, 1.00), gammaHQ, 'b-o', mew=0, label=r'$rA = 1$',
             lw=2, ms=7)
    ax1.plot(betaOM(r, .20), gammaHQ, 'g-o', mew=0, label=r'$rA = 0.2$',
             lw=2, ms=7)
    ax1.plot(betaOM(r, .15), gammaHQ, 'k-o', mew=0, label=r'$rA = 0.15$',
             lw=2, ms=7)

    ax1.set_xlabel(r'$\beta$', fontsize=20)
    ax1.set_ylabel(r'$\gamma$', fontsize=20)
    ax1.set_title(r'Anisotropy radius variation. \
                  ($\rho0 = \frac{1}{2\pi}$, $rS = 1$)', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1, frameon=True,
               loc=0, handlelength=2.5)
    ax1.set_xlim(0., 1.05)

    ax2.plot(betaOM(r), gammaHQ(r, x=5.), 'r-o', mew=0, label=r'$rS = 5$',
             lw=2, ms=7)
    ax2.plot(betaOM(r), gammaHQ(r, x=2.), 'b-o', mew=0, label=r'$rS = 2$',
             lw=2, ms=7)
    ax2.plot(betaOM(r), gammaHQ(r, x=1.2), 'g-o', mew=0, label=r'$rS = 1.2$',
             lw=2, ms=7)
    ax2.plot(betaOM(r), gammaHQ(r), 'k-o', mew=0, label=r'$rS = 1$',
             lw=2, ms=7)
    ax2.plot(x, y, 'm', lw=2, ms=7)

    ax2.fill_between(x, 0, y, color='Violet')
    ax2.set_xlim(0., .5)
    ax2.set_xlabel(r'$\beta$', fontsize=20)
    ax2.set_ylabel(r'$\gamma$', fontsize=20)
    ax2.set_title(r'Scale radius variation. \
                  ($\rho0 = \frac{1}{2\pi}$, $rA = 1.2$)',
                  fontsize=20)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1, frameon=True,
               loc=0, handlelength=2.5)

    g = gammaHQ(r)
    k = Sigma_calc.kappa_func(len_obj=r, radii=r, sigma_r2=sigmaRad2())
    Fit = ((-.15 * g - .85 * k)
           / ((1 + (-.15 * g - .85 * k) ** 3) ** .333333))
    b = betaOM(r)
    ax3.plot(b, Fit, 'r-o', mew=0, label=r'$Fit$', lw=2, ms=7)
    ax3.set_xlim(0., .5)
    ax3.set_xlabel(r'$\beta$', fontsize=20)
    ax3.set_ylabel('Fit', fontsize=20)
    ax3.set_title(r'Fit ($rA = 1.2$, $rS = 1$)', fontsize=20)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)

    ax4.plot(x, y, 'm', lw=2, ms=7)
    ax4.fill_between(x, 0, y, color='Violet')
    ax4.plot(betaOM(r, .2), gammaHQ(r, x=1.5), 'r-o', mew=0,
             label=r'$rA = 0.2, rS = 1.5$', lw=2, ms=7)
    ax4.plot(betaOM(r, .3), gammaHQ(r, x=2.), 'b-o', mew=0,
             label=r'$rA = 0.3, rS = 2$', lw=2, ms=7)
    ax4.plot(betaOM(r, .5), gammaHQ(r), 'g-o', mew=0,
             label=r'$rA = 0.5, rS = 1$', lw=2, ms=7)

    ax4.set_xlim(0., 1.)
    ax4.set_xlabel(r'', fontsize=20)
    ax4.set_ylabel(r'', fontsize=20)
    ax4.set_title(r'$rS$ and $rA$ tuning ($\rho0=\frac{1}{2\pi}$)',
                  fontsize=20)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1, frameon=True,
               loc=0, handlelength=2.5)

    f.savefig(figurePath + 'betaGammaFunctions.png')

plt.show()
