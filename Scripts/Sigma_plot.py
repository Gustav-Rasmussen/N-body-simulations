# -*- coding: utf-8 -*-

import h5py
import numpy as np
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
import pylab
from scipy.stats import norm
from scipy.optimize import curve_fit
import scipy as sp
import seaborn as sns
from pathlib import Path
import Gammas_and_R_middles
import getSnapshotValues
import snapshotFiles
import NoOfParticlesAndParticleMass
from definePaths import *
from collections import namedtuple
import Sigma_calc

# Paths -----------------------------------------------------------------------

simulations = ['A/', 'B/', 'Soft_B/', 'CS4/', 'CS5/', 'CS6/', 'DS1/',
               'Soft_D2/', 'E/'
               ]

text_files_path = textFilesPath / simulations[0]

# Choose number of bins -------------------------------------------------------

bins_list = [202, 102, 52, 22]

bins = bins_list[0]

# Figure switches -------------------------------------------------------------

Fig_x_hist = 0
Fig_x_hist2d = 0
Fig_v_logr = 0
Fig_v_logr_r2 = 0
Fig2_v = 0
Fig3_sigma = 0
Fig3_sigma_r_2 = 0
Fig3_sigma_over_v_circ_r_2 = 0
Fig4_beta = 0
Fig4_beta_r_2 = 0
Fig5_kappa = 0
Fig5_kappa_r_2 = 0
Fig6_gamma = 0
Fig6_gamma_r_2 = 0
Fig7_betagamma = 0

Fig_combine_ASCII = 0
# save_sigma = 0
V_vr_r_logr_panel = 0

snapshot_num = ['IC', '10_005', '48_009', '198_093']
sim = ['A', 'B', 'CS4', 'CS5', 'CS6', 'DS1', 'D2', 'Soft_D2', 'E']
snap = ['48_009', '48_093', '49_093', '198_093', '199_093']

# rlimit, bins
sim_snap = [sim[0] + snap[0],  # 10^4, 20
            sim[1] + snap[4],  # 10^4, 20
            sim[2] + snap[1],  # 10^4, 20
            sim[3] + snap[1],  # 10^4, 20
            sim[4] + snap[1],  # 10^4, 20
            sim[5] + snap[2],  # 10^4, 20
            sim[6] + snap[2],  # 10^4, 20
            sim[7] + snap[2],  # 10^4, 20
            sim[8] + snap[3],  # 10^4, 20
            sim[0] + snap[0],  # 32, 50
            sim[1] + snap[4],  # 32, 50
            sim[2] + snap[1],  # 32, 20
            sim[3] + snap[1],  # 32, 20
            sim[4] + snap[1],  # 32, 20
            sim[5] + snap[2],  # 32, 20
            sim[6] + snap[2],  # 32, 20
            sim[7] + snap[2],  # 32, 20
            sim[8] + snap[3]  # 32, 50
            ]

# Figures ---------------------------------------------------------------------

if Fig_x_hist:
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 11))

    f.subplots_adjust(hspace=0, wspace=0)
    ax1.set_xlabel(r'$x - x_c$', fontsize=30)
    n, bins, patches = ax1.hist(x - xC, 500, normed=1,
                                histtype='stepfilled')
    plt.setp(patches, 'facecolor', 'g', 'alpha', .75)
    ax1.set_xlim(-40, 40)
    ax1.set_ylim(.0, .4)

    ax2.set_xlabel(r'$y-y_c$', fontsize=30)
    n, bins, patches = ax2.hist(y - yC, 500, normed=1,
                                histtype='stepfilled')
    plt.setp(patches, 'facecolor', 'g', 'alpha', .75)
    ax2.set_title(r'Histograms of centralized positions', fontsize=30)
    ax2.set_xlim(-40, 40)
    ax2.set_ylim(.0, .4)
    ax2.tick_params(axis='both', which='both', bottom='on', top='off',
                    labelbottom='on', right='off', left='off',
                    labelleft='off')

    ax3.set_xlabel(r'$z - z_c$', fontsize=30)
    n, bins, patches = ax3.hist(z - zC, 500, normed=1,
                                histtype='stepfilled')
    plt.setp(patches, 'facecolor', 'g', 'alpha', .75)
    ax3.set_xlim(-40, 40)
    ax3.set_ylim(.0, .4)
    ax3.tick_params(axis='both', which='both', bottom='on', top='off',
                    labelbottom='on', right='off', left='off',
                    labelleft='off')

    fig_titles = ['x_hist', 'CS4_Final_x_hist_I']
    f.savefig(f"{figurePath}Fig_{fig_titles[0]}.png")

if Fig_x_hist2d:
    f = plt.figure(figsize=(13, 11))
    plt.xlabel(r'$x - x_c$', fontsize=30)
    plt.ylabel(r'$y - y_c$', fontsize=30)
    plt.hexbin(x - xC, y - yC, gridsize=200)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.title(r'Histogram of centralized positions x and y (200 hexbins)',
              fontsize=30)

    fig_titles = ['x_hist2d', 'CS4_Final_x_hist2d_I']
    f.savefig(f"{figurePath}Fig_{fig_titles[0]}.png")

if Fig_v_logr:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.plot(r, v, 'bo', lw=3, ms=2)
    ax1.set_xlabel('r', fontsize=30)
    ax1.set_ylabel(r'velocity, $v = \sqrt{v_x^2 + v_y^2 + v_z^2}$',
                   fontsize=30)

    ax1.set_title(r'A {0}(I: $\Delta G,\
                  R_{lim}=10^4$)'.format(snapshot_num[0]),
                  fontsize=30)
    # ax1.set_title(r'%s' % F, fontsize=30)

    ax2.plot(np.log10(r), v, 'bo', lw=3, ms=2)
    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.yaxis.tick_right()

    fig_names = ['A_IC_v_logr', 'A_10_005_v_logr', 'A_48_009_v_logr',
                 'B_v_logr', 'Soft_B_v_logr', 'CS1_v_logr', 'CS2_v_logr',
                 'CS3_v_logr', 'CS4_v_logr', 'CS5_v_logr', 'CS6_v_logr',
                 'DS1_v_logr', 'D2_v_logr', 'Soft_D2_v_logr', 'E_v_logr'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig_v_logr_r2:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.plot(r_r2, v, 'bo', lw=3, ms=2)
    ax1.set_xlabel(r'$\frac{r}{r_{-2}}$', fontsize=30)
    ax1.set_ylabel(r'velocity, $v = \sqrt{v_x^2+v_y^2+v_z^2}$',
                   fontsize=30)

    ax1.set_title(r'A {0}(I: $\Delta G,\
                  R_{lim}=10^4$)'.format(snapshot_num[0]),
                  fontsize=30)

    # ax1.set_title(r'%s' % F, fontsize=30)

    ax2.plot(np.log10(r_r2), v, 'bo', lw=3, ms=2)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax2.yaxis.tick_right()

    fig_names = ['A_IC_v_logr_r2', 'A_10_005_v_logr_r2', 'A_48_009_v_logr_r2',
                 'B_v_logr_r2', 'Soft_B_v_logr_r2', 'CS1_v_logr_r2',
                 'CS2_v_logr_r2', 'CS3_v_logr_r2', 'CS4_v_logr_r2',
                 'CS5_v_logr_r2', 'CS6_v_logr_r2', 'DS1_v_logr_r2',
                 'D2_v_logr_r2', 'Soft_D2_v_logr_r2', 'E_v_logr_r2'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig2_v:  # 3 plots of the velocities as function of x.
    f = plt.figure()
    ax1 = plt.subplot(131)
    plt.ylabel('vx', fontsize=30)
    plt.plot(x, vx, 'bo', ms=2, mew=0)

    ax2 = plt.subplot(132)
    plt.xlabel('x', fontsize=30)
    plt.ylabel('vy', fontsize=30)
    plt.title('Velocities (File = %s)' % F, fontsize=30)
    plt.plot(x, vy, 'bo', ms=2, mew=0)
    setp(ax2.get_yticklabels(), visible=False)

    ax3 = plt.subplot(133)
    plt.ylabel('vz', fontsize=30)
    plt.plot(x, vz, 'bo', ms=2, mew=0)
    setp(ax3.get_yticklabels(), visible=False)

    fig_names = ['A_v', 'B_v', 'Soft_B_v', 'CS1_v', 'CS2_v', 'CS3_v', 'CS4_v',
                 'CS5_v', 'CS6_v', 'DS1_v', 'D2_v', 'Soft_D2_v', 'E_v'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig3_sigma:  # Dispersions
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma2_arr)

    plt.plot(x_plot, y_plot, 'r-o', ms=8, mew=0,
             label=r'$\log (\sigma_{total}^2)$')
    y_plot = np.log10(sigmarad2_arr)
    plt.plot(x_plot, y_plot, 'b--s', ms=8, mew=0,
             label=r'$\log (\sigma_{r}^2)$')
    y_plot = np.log10(sigmatheta2_arr)
    plt.plot(x_plot, y_plot, 'g--v', ms=8, mew=0,
             label=r'$\log (\sigma_{\theta}^2)$')
    y_plot = np.log10(sigmaphi2_arr)
    plt.plot(x_plot, y_plot, 'k--^', ms=8, mew=0,
             label=r'$\log (\sigma_{\phi}^2)$')
    y_plot = np.log10(sigmatan2_arr)  # plot sigma_tan
    plt.plot(x_plot, y_plot, 'c--^', ms=8, mew=0,
             label=r'$\log (\sigma_{tan}^2)$')

    plt.xlabel(r'$\log $r', fontsize=30)
    plt.ylabel(r'$\log (\sigma^2)$', fontsize=30)

    plt.title(r'Velocity dispersions (B {}, $R_{limit} = 10^4$,\
              20 radial bins)'.format(snapshot_num[0]),
              fontsize=30)

    # plt.title(r'Velocity dispersions (File = %s)' % F, fontsize=30)

    leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    fig_names = ['A_sigma', 'B_IC_sigma', 'B_198_093_sigma', 'Soft_B_sigma',
                 'CS1_sigma', 'CS2_sigma', 'CS3_sigma', 'CS4_sigma',
                 'CS5_sigma', 'CS6_sigma', 'DS1_sigma', 'D2_sigma',
                 'Soft_D2_sigma', 'E_sigma'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig3_sigma_r_2:  # Dispersions
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr / r_2)
    y_plot = np.log10(sigma2_arr)
    plt.plot(x_plot, y_plot, 'r-o', ms=8, mew=0,
             label=r'$\log (\sigma_{total}^2)$')
    y_plot = np.log10(sigmarad2_arr)
    plt.plot(x_plot, y_plot, 'b--s', ms=8, mew=0,
             label=r'$\log (\sigma_{r}^2)$')
    y_plot = np.log10(sigmatheta2_arr)
    plt.plot(x_plot, y_plot, 'g--v', ms=8, mew=0,
             label=r'$\log (\sigma_{\theta}^2)$')
    y_plot = np.log10(sigmaphi2_arr)
    plt.plot(x_plot, y_plot, 'k--^', ms=8, mew=0,
             label=r'$\log (\sigma_{\phi}^2)$')
    y_plot = np.log10(sigmatan2_arr)  # plot sigma_tan
    plt.plot(x_plot, y_plot, 'c--^', ms=8, mew=0,
             label=r'$\log (\sigma_{\tan}^2)$')
    leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$\log (\sigma^2) $', fontsize=30)

    plt.title(r'Velocity dispersions (B {}, $R_{limit} = 10^4$,\
              20 radial bins)'.format(snapshot_num[0]),
              fontsize=30)

    # plt.title(r'Velocity dispersions (File = %s)' % F, fontsize=30)

    fig_names = ['A_sigma_r_2', 'B_IC_sigma_r_2', 'B_198_093_sigma_r_2',
                 'Soft_B_sigma_r_2', 'CS1_sigma_r_2', 'CS2_sigma_r_2',
                 'CS3_sigma_r_2', 'CS4_sigma_r_2', 'CS5_sigma_r_2',
                 'CS6_sigma_r_2', 'DS1_sigma_r_2', 'D2_sigma_r_2',
                 'Soft_D2_sigma_r_2', 'E_sigma_r_2'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig3_sigma_over_v_circ_r_2:  # Dispersions
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr / r_2)
    y_plot = np.log10(sigma2_arr / v_circ_2 ** 2)
    # label=r'$\log ((\frac{\sigma_{total}}{v_{circ,2}})^2)$'
    plt.plot(x_plot, y_plot, 'r-o', ms=8, mew=0,
             label=r'$\log (\bar{\sigma_{total}}^2)$')
    y_plot = np.log10(sigmarad2_arr / v_circ_2 ** 2)
    plt.plot(x_plot, y_plot, 'b--s', ms=8, mew=0,
             label=r'$\log (\bar{\sigma_{r}}^2)$')
    y_plot = np.log10(sigmatheta2_arr / v_circ_2 ** 2)
    plt.plot(x_plot, y_plot, 'g--v', ms=8, mew=0,
             label=r'$\log (\bar{\sigma_{\theta}}^2)$')
    y_plot = np.log10(sigmaphi2_arr / v_circ_2 ** 2)
    plt.plot(x_plot, y_plot, 'k--^', ms=8, mew=0,
             label=r'$\log (\bar{\sigma_{\phi}}^2)$')
    y_plot = np.log10(sigmatan2_arr / v_circ_2 ** 2)  # plot sigma_tan
    plt.plot(x_plot, y_plot, 'c--^', ms=8, mew=0,
             label=r'$\log (\bar{\sigma_{\tan}}^2)$')

    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    # plt.ylabel(r'$\log (\frac{\sigma^2}{v_{circ,2}})$', fontsize=26)
    plt.ylabel(r'$\log (\bar{\sigma}^2)$', fontsize=30)

    plt.title(r'Velocity dispersions (B {}, $R_{limit} = 10^4$,\
              20 radial bins)'.format(snapshot_num[0]),
              fontsize=30)

    # plt.title(r'Velocity dispersions (File = %s)' % F, fontsize=26)

    leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    fig_names = ['A_sigma_divided_by_v_circ_r_2',
                 'B_sigma_divided_by_v_circ_r_2',
                 'Soft_B_sigma_divided_by_v_circ_r_2',
                 'CS1_sigma_divided_by_v_circ_r_2',
                 'CS2_sigma_divided_by_v_circ_r_2',
                 'CS3_sigma_divided_by_v_circ_r_2',
                 'CS4_sigma_divided_by_v_circ_r_2',
                 'CS5_sigma_divided_by_v_circ_r_2',
                 'CS6_sigma_divided_by_v_circ_r_2',
                 'DS1_sigma_divided_by_v_circ_r_2',
                 'D2_sigma_divided_by_v_circ_r_2',
                 'Soft_D2_sigma_divided_by_v_circ_r_2',
                 'E_sigma_divided_by_v_circ_r_2'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig4_beta:  # plot beta
    f = plt.figure(figsize=(16, 11))
    plt.ylim(-1., 1.)
    x_plot = np.log10(bin_radius_arr)
    y_plot = beta_arr
    plt.xlabel(r'$\log$r', fontsize=30)
    plt.ylabel(r'$\beta$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0)
    # from this graph we see that beta is below zero.
    # this means sigmatheta2_arr/sigmarad2_arr > 1,
    # which in turn means that sigmatheta2_arr > sigmarad2_arr.
    plt.plot(x_plot, 0 * x_plot, 'c--', lw=2)
    plt.plot((-.5, -.5), (-1., 1.), 'r-', label=r'inner cut')
    # plt.plot((1., 1.), (-1., 1.), 'b-', label=r'outer cut')

    if Fig4_betafit:  # fitting beta with two different profiles
        x = 10 ** x_plot
        y_plot = x ** 2 / (4 ** 2 + x ** 2)
        plt.plot(x_plot, y_plot, 'b-', ms=2, mew=0,
                 label=r'$\frac{r^2}{4^2+r^2}$')
        # plt.title(r'$\beta$ with fit (%s)' % F, fontsize=26)
        plt.title(r'$\beta$ with analytical expression\
                  (CS6 IC with 20 radial bins)', fontsize=30)

        # Dummy plot to add label to legend for chi2
        plt.plot([], [], 'm.',
                 label=r'$\chi^2 = %.6f$' % chi_2(beta_arr))

        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        fig_names = ['A_IC_beta_logr_fit', 'B_IC_beta_logr_fit',
                     'Soft_B_IC_beta_logr_fit', 'CS1_IC_beta_logr_fit',
                     'CS4_IC_beta_logr_fit', 'CS5_IC_beta_logr_fit',
                     'CS6_IC_beta_logr_fit', 'DS1_IC_beta_logr_fit',
                     'D2_beta_logr_fit', 'Soft_D2_beta_logr_fit',
                     'Soft_D2_Final_beta_logr_fit', 'E_beta_logr_fit'
                     ]

        f.savefig(f"{figurePath}{fig_names[0]}.png")

    else:
        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        # rlimits = ['10^4', '32']
        # bins = ['20', '50']

        plt.title(r'$\beta$ with zero-line\
                  ({0}, $R_{limit}$=10^4, 20 bins)'.format(sim_snap[0]),
                  fontsize=30)

        # plt.title(r'$\beta$ with zero-line(%s)' % F, fontsize=30)

        fig_names_I_R32 = ['A_IC_beta_logr_I_R32',
                           'A_48_009_beta_logr_I_R32',
                           'A_48_009_beta_logr_I_R32_cuts',
                           'B_IC_beta_logr_I_R32',
                           'B_199_093_beta_logr_I_R32',
                           'Soft_B_IC_beta_logr_I_R32',
                           'Soft_B_Final_beta_logr_I_R32',
                           'CS1_IC_beta_logr_I_R32',
                           'CS4_IC_beta_logr_I_R32',
                           'CS4_48_093_beta_logr_I_R32',
                           'CS5_IC_beta_logr_I_R32',
                           'CS5_48_093_beta_logr_I_R32',
                           'CS6_IC_beta_logr_I_R32',
                           'CS6_48_093_beta_logr_I_R32',
                           'DS1_IC_beta_logr_I_R32',
                           'DS1_49_093_beta_logr_I_R32',
                           'D2_beta_logr_I_R32',
                           'D2_49_093_beta_logr_I_R32',
                           'Soft_D2_beta_logr_I_R32',
                           'Soft_D2_49_093_beta_logr_I_R32',
                           'E_beta_logr_I_R32',
                           'E_198_093_beta_logr_I_R32'
                           ]

        f.savefig(f"{figurePath}{fig_names_I_R32[0]}.png")

        fig_names = ['A_IC_beta_logr',
                     'A_48_009_beta_logr',
                     'B_IC_beta_logr',
                     'B_199_093_beta_logr',
                     'Soft_B_IC_beta_logr',
                     'Soft_B_Final_beta_logr',
                     'CS1_IC_beta_logr',
                     'CS4_IC_beta_logr',
                     'CS4_48_093_beta_logr',
                     'CS5_IC_beta_logr',
                     'CS5_48_093_beta_logr',
                     'CS6_IC_beta_logr',
                     'CS6_48_093_beta_logr',
                     'DS1_IC_beta_logr',
                     'DS1_49_093_beta_logr',
                     'D2_beta_logr',
                     'D2_49_093_beta_logr',
                     'Soft_D2_beta_logr',
                     'Soft_D2_49_093_beta_logr',
                     'E_beta_logr',
                     'E_198_093_beta_logr'
                     ]

        # f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig4_beta_r_2:  # plot beta
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr / r_2)
    y_plot = beta_arr
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$\beta$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0, label=r'$\beta$')
    # from this graph we see that beta is below zero.
    # this means sigmatheta2_arr/sigmarad2_arr > 1,
    # which in turn means that sigmatheta2_arr > sigmarad2_arr.
    plt.plot(x_plot, 0 * x_plot, 'b--', lw=2)
    # plt.title(r'$\beta$ with zero-line(%s)' % F , fontsize=30)
    # plt.title(r'Velocity anisotropy (CS6 IC with 20 radial bins)',
    #           fontsize=30)

    fig_names = ['A_IC_beta_r_2_logr', 'A_Final_beta_r_2_logr',
                 'B_IC_beta_r_2_logr', 'B_Final_beta_r_2_logr',
                 'Soft_B_IC_beta_r_2_logr', 'Soft_B_Final_beta_r_2_logr',
                 'CS1_IC_beta_r_2_logr', 'CS4_IC_beta_r_2_logr',
                 'CS4_Final_beta_r_2_logr', 'CS5_IC_beta_r_2_logr',
                 'CS5_Final_beta_r_2_logr', 'CS6_IC_beta_r_2_logr',
                 'CS6_Final_beta_r_2_logr', 'DS1_IC_beta_r_2_logr',
                 'DS1_Final_beta_r_2_logr', 'D2_beta_r_2_logr',
                 'D2_Final_beta_r_2_logr', 'Soft_D2_beta_r_2_logr',
                 'Soft_D2_Final_beta_r_2_logr', 'E_beta_r_2_logr',
                 'E_Final_beta_r_2_logr'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig5_kappa:
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = kappa_arr
    plt.xlabel(r'$\log $r', fontsize=30)
    plt.ylabel(r'$\kappa$', fontsize=30)
    plt.ylim(-4., .4)
    plt.plot(x_plot, y_plot, 'k-o', ms=4, mew=0)
    # plt.plot(x_plot, y_plot, 'k-o', ms=4, mew=0, label=r'$\kappa$')
    # plt.plot(x_plot, 0 * x_plot, '--', lw=2, color='grey')
    plt.plot((-.92, -.92), (-5., 25.), 'r-', label=r'inner cut')
    # plt.plot((1., 1.), (-4., 4.), 'b-', label=r'outer cut')

    if Fig5_kappafit:  # fitting beta with two different profiles
        x = bin_radius_arr
        # x = 10 ** x_plot
        l = np.log(x)
        ll = np.log(x + 1)

        num1 = -151.9999999 * x + 12 * ll - 12 * l - 250 * x ** 2 - 37 +
               48 * ll * x ** 5 - 48 * l * x ** 5 + 204 * ll * x ** 4 -
               204 * l * x ** 4 + 336 * ll * x ** 3 - 336 * l * x ** 3

        num2 = 264 * ll * x ** 2 - 264 * l * x ** 2 + 96 * ll * x - 96 *
               l * x + 2 * 10 ** (-8) * x ** 5 - 47.99999992 * x ** 4 -
               179.9999999 * x ** 3

        denom = (12 * ll * x ** 4 - 12 * l * x ** 4 + 4.049710908 * 10
                ** (-9) * x ** 4 + 48 * ll * x ** 3 - 48 * l * x ** 3 -
                11.99999998 * x ** 3 + 72 * ll * x ** 2 - 72 * l * x **
                2 - 41.99999998 * x ** 2 + 48 * ll * x - 48 * l * x -
                51.99999998 * x + 12 * ll - 12 * l - 25) * (x + 1)

        y_plot = (num1 + num2) / denom

        print('y_plot.shape = ', y_plot.shape,
              'len(y_plot) = ', len(y_plot),
              'y_plot[1.] = ', y_plot[1.])

        plt.plot(x_plot[0:len(y_plot) - 3], y_plot[0:len(y_plot) - 3],
                 'b-', ms=2, mew=0, label=r'Analytical shape')

        # plt.title(r'$\kappa$ with fit (%s)' % F , fontsize=30)
        plt.title(r'$\kappa$ with analytical expression\
                  (B IC with 20 radial bins)', fontsize=30)
        plt.ylim(-2., .5)

        # Dummy plot to add label to legend for chi2
        plt.plot([], [], 'g.',
                 label=r'$\chi^2 = %.6f$' % chi_2(kappa_arr))

        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        fig_names = ['A_IC_kappa_logr_fit', 'B_IC_kappa_logr_fit',
                     'Soft_B_IC_kappa_logr_fit', 'CS1_IC_kappa_logr_fit',
                     'CS2_IC_kappa_logr_fit', 'CS3_IC_kappa_logr_fit',
                     'CS4_IC_kappa_logr_fit', 'CS5_IC_kappa_logr_fit',
                     'CS6_IC_kappa_logr_fit', 'DS1_IC_kappa_logr_fit',
                     'D2_kappa_logr_fit', 'Soft_D2_kappa_logr_fit',
                     'Soft_D2_Final_kappa_logr_fit', 'E_kappa_logr_fit'
                     ]

        f.savefig(f"{figurePath}{fig_names[0]}.png")

    else:
        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        plt.title(r'$\kappa$ and zero-line\
                  ({0}, $R_{limit}$=10^4, 20 bins)'.format(sim_snap[0]),
                  fontsize=30)

        # plt.title(r'$\kappa$ and zero-line (%s)' % F, fontsize=30)

        fig_names_I_32 = ['A_IC_kappa_logr_I_R32', 'A_48_009_kappa_logr_I_R32',
                          'A_48_009_kappa_logr_I_R32_cuts',
                          'B_IC_kappa_logr_I_R32',
                          'B_199_093_kappa_logr_I_R32',
                          'Soft_B_IC_kappa_logr_I_R32',
                          'Soft_B_Final_kappa_logr_I_R32',
                          'CS1_IC_kappa_logr_I_R32', 'CS4_IC_kappa_logr_I_R32',
                          'CS4_48_093_kappa_logr_I_R32',
                          'CS5_IC_kappa_logr_I_R32',
                          'CS5_48_093_kappa_logr_I_R32',
                          'CS6_IC_kappa_logr_I_R32',
                          'CS6_48_093_kappa_logr_I_R32',
                          'DS1_IC_kappa_logr_I_R32',
                          'DS1_49_093_kappa_logr_I_R32', 'D2_kappa_logr_I_R32',
                          'D2_49_093_kappa_logr_I_R32',
                          'Soft_D2_kappa_logr_I_R32',
                          'Soft_D2_49_093_kappa_logr_I_R32',
                          'E_kappa_logr_I_R32', 'E_198_093_kappa_logr_I_R32'
                          ]

        f.savefig(f"{figurePath}{fig_names_I_32[0]}.png")

        fig_names = ['A_IC_kappa_logr', 'A_48_009_kappa_logr',
                     'B_IC_kappa_logr', 'B_199_093_kappa_logr',
                     'Soft_B_IC_kappa_logr', 'Soft_B_Final_kappa_logr',
                     'CS1_IC_kappa_logr', 'CS4_IC_kappa_logr',
                     'CS4_48_093_kappa_logr', 'CS5_IC_kappa_logr',
                     'CS5_48_093_kappa_logr', 'CS6_IC_kappa_logr',
                     'CS6_48_093_kappa_logr', 'DS1_IC_kappa_logr',
                     'DS1_49_093_kappa_logr', 'D2_kappa_logr',
                     'D2_49_093_kappa_logr', 'Soft_D2_kappa_logr',
                     'Soft_D2_49_093_kappa_logr', 'E_kappa_logr',
                     'E_198_093_kappa_logr'
                     ]

        f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig5_kappa_r_2:
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr / r_2)
    y_plot = kappa_arr
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$\kappa$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=4, mew=0, label=r'$\kappa$')

    # plt.title(r'$\kappa$ and zero-line (%s)' % F, fontsize=30)
    # plt.title(r'$\kappa$ (B IC with 20 radial bins)', fontsize=30)

    fig_names = ['A_IC_kappa_r_2_logr', 'A_Final_kappa_r_2_logr',
                 'B_IC_kappa_r_2_logr', 'B_Final_kappa_r_2_logr',
                 'Soft_B_IC_kappa_r_2_logr', 'Soft_B_Final_kappa_r_2_logr',
                 'CS1_IC_kappa_r_2_logr', 'CS4_IC_kappa_r_2_logr',
                 'CS4_Final_kappa_r_2_logr', 'CS5_IC_kappa_r_2_logr',
                 'CS5_Final_kappa_r_2_logr', 'CS6_IC_kappa_r_2_logr',
                 'CS6_Final_kappa_r_2_logr', 'DS1_IC_kappa_r_2_logr',
                 'DS1_Final_kappa_r_2_logr', 'D2_kappa_r_2_logr',
                 'D2_Final_kappa_r_2_logr',  'Soft_D2_kappa_r_2_logr',
                 'Soft_D2_Final_kappa_r_2_logr', 'E_kappa_r_2_logr',
                 'E_Final_kappa_r_2_logr'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig6_gamma:
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr)
    plt.ylim(-4., 1.5)
    y_plot = gamma_arr
    plt.xlabel(r'$\log $r', fontsize=30)
    plt.ylabel(r'$\gamma$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0)
    plt.plot((-.5, -.5), (-4., 4.), 'r-', label=r'inner cut')
    plt.plot((1., 1.), (-4., 4.), 'b-', label=r'outer cut')

    if Fig6_gammafit:
        x = 10 ** x_plot
        y_plot = -1 - 3 * x / (1 + x)
        plt.plot(x_plot, y_plot, 'c-', ms=2, mew=0,
                 label=r'$-1 -\frac{3r}{1 + r}$')

        # Dummy plot to add label to legend for chi2
        plt.plot([], [], 'm.', label=r'$\chi^2 = %.6f$' % chi_2)

        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        plt.title(f'Radial density slope with analytical expression\
                  ({sim[1]} {snapshot_num[0]} with 20 radial bins)',
                  fontsize=30)  # 'B IC', 'CS4 IC', 'CS5 IC', 'CS6 IC'

        # plt.title('Radial density slope with analytical expression (%s)' % F,
        #           fontsize=18)

        fig_names = ['A_IC_gamma_logr_fit', 'A_Final_gamma_logr_fit',
                     'B_IC_gamma_logr_fit', 'B_Final_gamma_logr_fit',
                     'Soft_B_IC_gamma_logr_fit', 'Soft_B_Final_gamma_logr_fit',
                     'CS1_IC_gamma_logr_fit', 'CS2_IC_gamma_logr_fit',
                     'CS3_IC_gamma_logr_fit', 'CS4_IC_gamma_logr_fit',
                     'CS4_Final_gamma_logr_fit', 'CS5_IC_gamma_logr_fit',
                     'CS5_Final_gamma_logr_fit', 'CS6_IC_gamma_logr_fit',
                     'CS6_Final_gamma_logr_fit', 'DS1_IC_gamma_logr_fit',
                     'DS1_Final_gamma_logr_fit', 'D2_IC_gamma_logr_fit',
                     'D2_Final_gamma_logr_fit', 'Soft_D2_IC_gamma_logr_fit',
                     'Soft_D2_Final_gamma_logr_fit', 'E_IC_gamma_logr_fit',
                     'E_Final_gamma_logr_fit'
                     ]

        f.savefig(f"{figurePath}{fig_names[0]}.png")

    else:
        # leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
        #                  fancybox=True, loc=0, handlelength=2.5)
        # leg.get_frame().set_alpha(.5)

        title_params = namedtuple('title_params',
                                  ['sim', 'snapshot', 'Rlimit', 'bins'])

        A_48_009 = title_params('A', '48_009', '10^4', '20')
        B_199_093 = title_params('B', '199_093', '10^4', '20')
        CS4_Final = title_params('CS4', 'Final', '10^4', '20')
        CS5_Final = title_params('CS5', 'Final', '10^4', '20')
        CS6_Final = title_params('CS6', 'Final', '10^4', '20')
        DS1_IC = title_params('DS1', 'IC', '10^4', '20')
        DS1_49_093 = title_params('DS1', '49_093', '10^4', '20')
        Soft_D2_IC = title_params('Soft_D2', 'IC', '10^4', '20')
        Soft_D2_49_093 = title_params('Soft_D2', '49_093', '10^4', '20')
        E_IC = title_params('E', 'IC', '10^4', '20')
        E_198_093 = title_params('E', '198_093', '10^4', '20')
        A_IC = title_params('A', 'IC', '32', '50')
        A_48_009 = title_params('A', '48_009', '32', '50')
        B_IC = title_params('B', 'IC', '32', '50')
        B_199_093 = title_params('B', '199_093', '32', '50')
        CS4_IC = title_params('CS4', 'IC', '32', '20')
        CS4_48_093 = title_params('CS4', '48_093', '32', '20')
        CS5_IC = title_params('CS5', 'IC', '32', '20')
        CS5_48_093 = title_params('CS5', '48_093', '32', '20')
        CS6_IC = title_params('CS6', 'IC', '32', '20')
        CS6_48_093 = title_params('CS6', '48_093', '32', '20')
        DS1_IC = title_params('DS1', 'IC', '32', '20')
        DS1_49_093 = title_params('DS1', '49_093', '32', '20')
        Soft_D2_IC = title_params('Soft_D2', 'IC', '32', '20')
        Soft_D2_49_093 = title_params('Soft_D2', '49_093', '32', '20')
        E_IC = title_params('E', 'IC', '32', '50')
        E_198_093 = title_params('E', '198_093', '32', '50')

        plt.title(f'Radial density slope\
                  ({A_48_009.sim} {A_48_009.snapshot},\
                  $R_{limit}$=A_48_009.Rlimit, {A_48_009.bins} bins)',
                  fontsize=30)

        '''
        plt.title(f'Radial density slope\
                  ({sim[0]} {snapshot_num[0]}, $R_{limit}$=10^4, 20 bins)',
                  fontsize=30)
        '''

        # plt.title('Radial density slope (%s)' % F, fontsize=30)

        fig_names_I_32 = ['A_IC_gamma_logr_I_R32',
                          'A_48_009_gamma_logr_I_R32',
                          'A_48_009_gamma_logr_I_R32_cuts',
                          'A_48_009_gamma_r_I_R32',
                          'B_IC_gamma_logr_I_R32',
                          'B_199_093_gamma_logr_I_R32',
                          'Soft_B_IC_gamma_logr_I_R32',
                          'Soft_B_Final_gamma_logr_I_R32',
                          'CS1_IC_gamma_logr_I_R32',
                          'CS2_IC_gamma_logr_I_R32',
                          'CS3_IC_gamma_logr_I_R32',
                          'CS4_IC_gamma_logr_I_R32',
                          'CS4_48_093_gamma_logr_I_R32',
                          'CS5_IC_gamma_logr_I_R32',
                          'CS5_48_093_gamma_logr_I_R32',
                          'CS6_IC_gamma_logr_I_R32',
                          'CS6_48_093_gamma_logr_I_R32',
                          'DS1_IC_gamma_logr_I_R32',
                          'DS1_49_093_gamma_logr_I_R32',
                          'D2_IC_gamma_logr_I_R32',
                          'D2_Final_gamma_logr_I_R32',
                          'Soft_D2_IC_gamma_logr_I_R32',
                          'Soft_D2_49_093_gamma_logr_I_R32',
                          'E_IC_gamma_logr_I_R32',
                          'E_198_093_gamma_logr_I_R32'
                          ]

        f.savefig(f"{figurePath}{fig_names_I_32[0]}.png")

        fig_names = ['A_IC_gamma_logr', 'A_48_009_gamma_logr',
                     'B_IC_gamma_logr', 'B_199_093_gamma_logr',
                     'Soft_B_IC_gamma_logr', 'Soft_B_Final_gamma_logr',
                     'CS1_IC_gamma_logr', 'CS2_IC_gamma_logr',
                     'CS3_IC_gamma_logr', 'CS4_IC_gamma_logr',
                     'CS4_Final_gamma_logr', 'CS5_IC_gamma_logr',
                     'CS5_Final_gamma_logr', 'CS6_IC_gamma_logr',
                     'CS6_Final_gamma_logr', 'DS1_IC_gamma_logr',
                     'DS1_49_093_gamma_logr', 'D2_IC_gamma_logr',
                     'D2_Final_gamma_logr', 'Soft_D2_IC_gamma_logr',
                     'Soft_D2_49_093_gamma_logr', 'E_IC_gamma_logr',
                     'E_198_093_gamma_logr'
                     ]

        # f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig6_gamma_r_2:
    f = plt.figure(figsize=(16, 11))
    x_plot = np.log10(bin_radius_arr / r_2)
    y_plot = gamma_arr
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$\gamma$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0, label=r'$\gamma$')

    plt.title(f'Radial density slope\
              ({sim[1]} {snapshot_num[0]} with 20 radial bins)',
               fontsize=30)
    # sim, snapshot_num
    # B, IC
    # CS6, IC
    # CS5, IC
    # CS4, IC
    # CS4, Final

    # plt.title('Radial density slope (%s)' % F, fontsize=30)

    fig_names = ['A_IC_gamma_r_2_logr', 'A_Final_gamma_r_2_logr',
                 'B_IC_gamma_r_2_logr', 'B_Final_gamma_r_2_logr',
                 'Soft_B_IC_gamma_r_2_logr', 'Soft_B_Final_gamma_r_2_logr',
                 'CS1_IC_gamma_r_2_logr', 'CS2_IC_gamma_r_2_logr',
                 'CS3_IC_gamma_r_2_logr', 'CS4_IC_gamma_r_2_logr',
                 'CS4_Final_gamma_r_2_logr', 'CS5_IC_gamma_r_2_logr',
                 'CS5_Final_gamma_r_2_logr', 'CS6_IC_gamma_r_2_logr',
                 'CS6_Final_gamma_r_2_logr', 'DS1_IC_gamma_r_2_logr',
                 'DS1_Final_gamma_r_2_logr', 'D2_IC_gamma_r_2_logr',
                 'D2_Final_gamma_r_2_logr', 'Soft_D2_IC_gamma_r_2_logr',
                 'Soft_D2_Final_gamma_r_2_logr', 'E_IC_gamma_r_2_logr',
                 'E_Final_gamma_r_2_logr'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig7_betagamma:
    f = plt.figure()
    subplot(121)
    x_plot = beta_arr
    y_plot = gamma_arr
    plt.xlabel(r'$\beta$', fontsize=30)
    plt.ylabel(r'$\gamma$', fontsize=30)
    plt.title(r'$\gamma$ vs $\beta$ (%s)' % F, fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=2, mew=0)

    subplot(122)
    x_plot = beta_arr
    y_plot = kappa_arr
    plt.xlabel(r'$\beta$', fontsize=30)
    plt.ylabel(r'$\kappa$', fontsize=30)
    plt.title(r'$\kappa$ vs $\beta$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=2, mew=0)

    fig_names = ['A_betagamma', 'B_betagamma', 'Soft_B_betagamma',
                 'CS1_betagamma', 'CS2_betagamma', 'CS3_betagamma',
                 'CS4_betagamma', 'CS5_betagamma', 'CS6_betagamma',
                 'DS1_betagamma', 'D2_betagamma', 'Soft_D2_betagamma',
                 'E_betagamma'
                 ]

    f.savefig(f"{figurePath}{fig_names[0]}.png")

if Fig_combine_ASCII:

    sim_names = ['A', 'B']

    read_txt = pylab.loadtxt(text_files_path +
                             f'{sim_names[1]}_particle_tracking.txt')

    f, (ax1) = plt.subplots(1, 1, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.plot(read_txt[:, 0], read_txt[:, 4], 'r-o',
             label='Particle 100000', lw=2, ms=7)
    ax1.plot(read_txt[:, 0], read_txt[:, 8], 'b-s',
             label='Particle 200000', lw=2, ms=7)
    ax1.plot(read_txt[:, 0], read_txt[:, 12], 'k-<',
             label='Particle 300000', lw=2, ms=7)
    ax1.plot(read_txt[:, 0], read_txt[:, 16], 'c--v',
             label='Particle 400000', lw=2, ms=7)

    ax1.set_ylabel('Radius', fontsize=30)
    ax1.set_xlabel('Simulation time', fontsize=30)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    # ax1.set_title(r'A (I: $\Delta $G)', fontsize=30)
    ax1.set_title(r'B (I: $\Delta $G)', fontsize=30)

    s = 'Fig_combine_ASCII_{}.png'
    # f.savefig(figurePath + s.format('A'))
    f.savefig(figurePath + s.format('B'))

if V_vr_r_logr_panel:
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 8))
    f.subplots_adjust(hspace=0, wspace=0)

    r = Sigma_calc.radii(x, y, z)
    Phi = Sigma_calc.phi(x, y)
    Theta = Sigma_calc.theta(z, r)
    VR = Sigma_calc.radial_velocity(Theta, Phi, vx, vy, vz)

    ax1.plot(r, VR, 'bo', lw=2, ms=1)
    a = F[:-14]
    ax1.set_title(r'$v_r$', fontsize=20)
    ax1.set_xlabel('r', fontsize=20)

    ax2.plot(np.log10(r), VR, 'bo', lw=2, ms=1)
    ax2.set_title(r'%s' % a, fontsize=20)
    ax2.set_xlabel(r'$\log r$', fontsize=20)
    ax2.axes.get_yaxis().set_visible(False)

    ax3.plot(np.log10(r), V, 'bo', lw=2, ms=1)
    ax3.set_title('Potential', fontsize=20)
    ax3.set_xlabel(r'$\log r$', fontsize=20)
    ax3.yaxis.tick_right()

    s = '{}_final_V_vr_r_logr_panel.png'
    if F.startswith('B_HQ10000_G1.0_199_093'):
        f.savefig(figurePath + 'B_final_vr_V_panel.png')
    elif F.startswith('B_bound_particles_G1.0_200_rfp_093'):
        f.savefig(figurePath + 'B_rfp_vr_V_panel.png')
    elif F.startswith('CS4_OM10000_G1.0_48_093'):
        f.savefig(figurePath + s.format('CS4'))
    elif F.startswith('CS5_OM10000_G1.0_48_093'):
        f.savefig(figurePath + s.format('CS5'))
    elif F.startswith('CS6_OM10000_G1.0_48_093'):
        f.savefig(figurePath + s.format('CS6'))
    elif F.startswith('DS1_OM10000_G1.0_48_093'):
        f.savefig(figurePath + s.format('DS1'))

plt.show()
