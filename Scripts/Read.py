# -*- coding: utf-8 -*-

# import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
# from pylab import *
# import seaborn as sns
# from pathlib import Path
# import Gammas_and_R_middles
# import getSnapshotValues
# import snapshotFiles
# import NoOfParticlesAndParticleMass
# from definePaths import *

simulationsLst = ['A', 'B', 'Soft_B', 'CS1', 'CS2', 'CS3', 'CS4',
                  'CS5', 'CS6', 'DS1', 'D2', 'Soft_D2', 'E'
                  ]

R_hob_par = R[GoodIDs]

if Gamma == Gammas[1]:
    r_2 = R_middle
    # position of particles inside halo
    posR_par_inside_halo = np.where(R_hob_par < r_2)
    nr_par_inside_halo = len(posR_par_inside_halo[0])
    M_2 = nr_par_inside_halo * m
    G = 1.
    v_circ_2 = np.sqrt(G * M_2 / r_2)
    V_2 = 4 / 3 * np.pi * r_2 ** 3

(density_arr, Volume_arr, rho_arr, rho_2_arr) = ([] for i in range(4))

# Array, 0.00001-1.
binning_arr_lin_log10_unitRmax = 10 ** ((np.arange(nr_binning_bins)
                                 / (nr_binning_bins - 1))
                                 * abs(np.log10(max_binning_R_unitRmax)
                                 - np.log10(min_binning_R_unitRmax))
                                 + np.log10(min_binning_R_unitRmax))

# Array, 0-500
binning_arr_lin_log10 = R_limit * binning_arr_lin_log10_unitRmax
for i in range(0, int(nr_binning_bins - 2)):  # loop over 0-998
    min_R_bin_i = binning_arr_lin_log10[i]  # start of bin
    max_R_bin_i = binning_arr_lin_log10[i + 1]  # end of bin
    # position of particles inside a radial bin
    posR_par_inside_bin_i = np.where(min_R_bin_i < R < max_R_bin_i)[0]
    # number of particles inside a radial bin
    nr_par_inside_bin_i = len(posR_par_inside_bin_i)
    # Volume of cluster
    Volume_cl = (4. / 3.) * np.pi * (max_R_bin_i ** 3 - min_R_bin_i ** 3)
    den_cl = nr_par_inside_bin_i / Volume_cl  # Number density
    rho = den_cl * m
    rho_2 = rho * V_2 / M_2

    # save arrays
    density_arr.append(den_cl)
    Volume_arr.append(Volume_cl)
    rho_arr.append(rho)
    rho_2_arr.append(rho_2)

Invers_Volume_arr = np.log10(np.divide(np.ones(len(Volume_arr)),
                             Volume_arr))

print('len(density_arr) = ', len(density_arr),
      'len(rho_arr) = ', len(rho_arr),
      'len(x) = ', len(x),
      'len(y) = ', len(y),
      'len(z) = ', len(z),
      'len(R) = ', len(R),
      'x[0] = ', x[0],
      'y[0] = ', y[0],
      'z[0] = ', z[0],
      'R[0] = ', R[0],
      'x[100] = ', x[100],
      'y[100] = ', y[100],
      'z[100] = ', z[100],
      'R[100] = ', R[100],
      'x[99999] = ', x[99999],
      'y[99999] = ', y[99999],
      'z[99999] = ', z[99999],
      'R[99999] = ', R[99999]
      )


def savefigStr(simName, plotName):
    return f'{figurePath}{simName}{plotName}'


# Switches for figures -------------------------------------------------
Fig1_Density = 0
Fig1_Densityfit = 0
Fig2_Density_r_2 = 0
Fig3_Potential = 0
Fig4_xy_rectangular = 0
Fig5_cartesian_velocities = 0

if Fig1_Density:
    f = plt.figure(figsize=(16, 11))
    v = [-1, 1, -4, .5]
    plt.axis(v)
    x_plot = np.log10(binning_arr_lin_log10)
    # y_plot = density_arr
    plt.xlabel(r'$\log r$', fontsize=30)
    plt.ylabel(r'$\log \rho$', fontsize=30)
    plt.plot(x_plot[0:int(nr_binning_bins - 2)], np.log10(rho_arr),
             'g-o', ms=2, lw=2, mew=0, label=r'$\rho$')
    # plt.legend(prop=dict(size=12), numpoints=2, ncol=2,
    #            frameon=True, loc=1, handlelength=2.5)

    if Fig1_Densityfit:
        x = binning_arr_lin_log10
        y_plot = rho_Hernquist(1. / (2 * np.pi), 1., x)
        plt.plot(np.log10(x), np.log10(y_plot), 'k:o', ms=2, lw=2, mew=0,
                 label=r'$\frac{1}{2\pi r (1+r)^3}$')
        plt.title(r'Density profile (B IC with 998 radial bins)',
                  fontsize=30)

        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        plotName = '_Density_fit.png'
        f.savefig(savefigStr(simulationsLst[0], plotName))

    else:
        plt.title('Density profile', fontsize=30)
        plotName = '_Density.png'
        f.savefig(savefigStr(simulationsLst[0], plotName))

if Fig2_Density_r_2:
    f = plt.figure(figsize=(16, 11))
    v = [-1, 1, -4, .5]
    plt.axis(v)
    x_plot = np.log10(binning_arr_lin_log10 / r_2)
    plt.xlabel(r'$ \log (\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$ \log \rho $', fontsize=30)
    plt.plot(x_plot[0:int(nr_binning_bins - 2)], np.log10(rho_arr),
             'g-o', ms=2, lw=2, mew=0, label=r'$\rho$')

    plt.title(r'Density profile (B IC with 998 radial bins)',
              fontsize=30)
    plotName = '_Density_r_2.png'
    f.savefig(savefigStr(simulationsLst[0], plotName))

if Fig3_Potential:
    f = plt.figure()
    ax1 = plt.subplot(121)
    plt.xlabel('r')
    plt.ylabel(r'$\Phi$')
    plt.title('Potential')
    plt.plot(Rcl, Vcl, 'bo', ms=2, mew=0)
    plt.grid()

    ax2 = plt.subplot(122)
    plt.xlabel(r'$\log r$')
    plt.plot(np.log10(Rcl), Vcl, 'bo', ms=2, mew=0)
    plt.grid()
    setp(ax2.get_yticklabels(), visible=False)

    plotName = '_Potential.png'
    f.savefig(savefigStr(simulationsLst[0], plotName))


# plot rectangular slice through cluster:
if Fig4_xy_rectangular:
    f = plt.figure()
    plt.title('Rectangular slice through cluster')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.hist2d(xclrec, yclrec, bins=200, norm=LogNorm())
    plt.colorbar()

    plotName = '_xy_rectangular.png'
    f.savefig(savefigStr(simulationsLst[0], plotName))

# 3 plots of the velocities as function of x.
if Fig5_cartesian_velocities:
    f = plt.figure()
    ax1 = plt.subplot(131)
    plt.ylabel('vxnew')
    plt.plot(xclrec, vxnew, 'bo', ms=2, mew=0)
    plt.title('velocities')
    ax2 = plt.subplot(132)
    plt.xlabel('x')
    plt.ylabel('vynew')
    plt.plot(xclrec, vynew, 'bo', ms=2, mew=0)
    setp(ax2.get_yticklabels(), visible=False)
    ax3 = plt.subplot(133)
    plt.ylabel('vznew')
    plt.plot(xclrec, vznew, 'bo', ms=2, mew=0)
    setp(ax3.get_yticklabels(), visible=False)

    plotName = '_cartesian_velocities.png'
    f.savefig(savefigStr(simulationsLst[0], plotName))

plt.show()
