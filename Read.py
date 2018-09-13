# -*- coding: utf-8 -*-

# import h5py
import numpy as np
# import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
# from pylab import *
# import seaborn as sns
import os
# import Gammas_and_R_middles
# import getSnapshotValues
import snapshotFiles

UserPath = os.getcwd()
DesktopPath = UserPath + 'Desktop/'
GADGET_G_path = DesktopPath + 'RunGadget/G_perturbations/'
StablePath = 'G_perturbations/Stable_structures/'
figurePath = DesktopPath + StablePath + 'figures/'
text_files_path = DesktopPath + StablePath + 'text_files/'
MartinPath = 'Martin_IC_and_Final_Edd_and_OM/'
hdf5_path = DesktopPath + 'G_perturbations/hdf5_files/'
nosync_path = UserPath + 'nosync/RunGadget/'

# print(UserPath)
# print(DesktopPath)
# print(StablePath)
# print(figurePath)

simulationsLst = ['A', 'B', 'Soft_B', 'CS1', 'CS2', 'CS3', 'CS4',
                  'CS5', 'CS6', 'DS1', 'D2', 'Soft_D2', 'E']

# Switches for figures -------------------------------------------------

Fig2_Density = 0
Fig2_Densityfit = 0
Fig2_Density_r_2 = 0
Fig3_Potential = 0
Fig4_xy_rectangular = 0
Fig5_cartesian_velocities = 0

# Total number of particles:
if F.startswith(('A_', 'B_', 'E_')):
    N = 10 ** 6
elif F.startswith(('CS4_', 'CS5_', 'CS6_', 'DS1_', 'D2_')):
    N = 10 ** 5
elif F.startswith(('CS1_', 'CS2_', 'CS3_')):
    N = 10 ** 4

if F.startswith(('A_', 'B_', 'CS4_', 'CS5_', 'CS6_', 'E_')):
    M = 1.  # Total mass equals unity
elif F.startswith(('DS1_', 'D2_')):
    M = 1. / 6.

m = M / N  # Mass of each particle
# print('N = ', N)
# print('m = ', m)

R_hob_par = R[GoodIDs]

if Gamma == Gammas[1]:
    r_2 = R_middle
    # position of particles inside halo
    posR_par_inside_halo = np.where(R_hob_par < r_2)
    nr_par_inside_halo = len(posR_par_inside_halo[0])
    M_2 = nr_par_inside_halo*m
    G = 1.
    v_circ_2 = np.sqrt(G * M_2 / r_2)
    V_2 = 4 / 3 * np.pi * r_2 ** 3

(density_arr, Volume_arr, rho_arr, rho_2_arr) = ([] for i in range(4))

# Array, 0.00001-1.
binning_arr_lin_log10_unitRmax = 10 ** ((np.arange(nr_binning_bins) /
                                 (nr_binning_bins - 1)) *
                                 abs(np.log10(max_binning_R_unitRmax)
                                 - np.log10(min_binning_R_unitRmax))
                                 + np.log10(min_binning_R_unitRmax))
# Array, 0-500
binning_arr_lin_log10 = R_limit * binning_arr_lin_log10_unitRmax
for i in range(0, int(nr_binning_bins - 2)):  # loop over 0-998
    min_R_bin_i = binning_arr_lin_log10[i]  # start of bin
    max_R_bin_i = binning_arr_lin_log10[i + 1]  # end of bin
    # position of particles inside a radial bin
    posR_par_inside_bin_i = np.where((R > min_R_bin_i) & (R < max_R_bin_i))[0]
    # number of particles inside a radial bin
    nr_par_inside_bin_i = len(posR_par_inside_bin_i)
    Volume_cl = (4. / 3.) * np.pi * (max_R_bin_i ** 3 -
                            min_R_bin_i ** 3)  # Volume of cluster
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

'''
print('len(density_arr) = ', len(density_arr))
print('len(rho_arr) = ', len(rho_arr))
print('len(x) = ', len(x))
print('len(y) = ', len(y))
print('len(z) = ', len(z))
print('len(R) = ', len(R))

print('x[0] = ', x[0])
print('y[0] = ', y[0])
print('z[0] = ', z[0])
print('R[0] = ', R[0])

print('x[100] = ', x[100])
print('y[100] = ', y[100])
print('z[100] = ', z[100])
print('R[100] = ', R[100])

print('x[99999] = ', x[99999])
print('y[99999] = ', y[99999])
print('z[99999] = ', z[99999])
print('R[99999] = ', R[99999])
'''


def savefigStr(simName, plotName=plotName):
    return '{}{}{}'.format(figurePath, simName, plotName)


if Fig2_Density:
    f = plt.figure(figsize=(16, 11))
    v = [-1, 1, -4, .5]
    plt.axis(v)
    x_plot = np.log10(binning_arr_lin_log10)
    # y_plot = density_arr
    plt.xlabel(r'$ \log r $', fontsize=30)
    plt.ylabel(r'$ \log \rho $', fontsize=30)
    plt.plot(x_plot[0:int(nr_binning_bins - 2)], np.log10(rho_arr),
             '-o', ms=2, lw=2, mew=0, c='green', label=r'$\rho$')
    # plt.legend(prop=dict(size=12), numpoints=2, ncol=2,
    #            frameon=True, loc=1, handlelength=2.5)

    if Fig2_Densityfit:
        x = binning_arr_lin_log10
        y_plot = rho_Hernquist(1. / (2 * np.pi), 1., x)
        plt.plot(np.log10(x), np.log10(y_plot), ':o', ms=2, lw=2, mew=0,
                 c='black', label=r'$\frac{1}{2\pi r (1+r)^3}$')
        plt.title(r'Density profile (B IC with 998 radial bins)',
                  fontsize=30)
        '''
        Chi2 = 0
        i = 0
        print('rho_arr = ', rho_arr)
        # while (i < len(rho_arr)):  # returns chi2 = infinity.
        # while (300 < i < len(rho_arr) - 300):  # returns chi2 = .00000
        # while (1 < i < len(rho_arr) - 1):  # returns chi2 = .00000

            if isnan(rho_arr[i]):
                print('nan at index: ', i)
            else:
                Chi2 += ((rho_arr[i] - y_plot[i]) ** 2) / (rho_arr[i] *
                        .2) ** 2
                print('Chi2 for density-fit: ', Chi2)
            i += 1
        Chi2 = (1.0 / (len(rho_arr) - 1)) * Chi2

        print('Total Chi2 for density-fit: ', Chi2)
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',
                 label=r'$\chi^2 = %.6f$'%Chi2)
        '''
        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        plotName = '_Density_fit.png'
        # f.savefig(savefigStr(simulationsLst[0])
        # f.savefig(savefigStr(simulationsLst[1])
        # f.savefig(savefigStr(simulationsLst[2])
        # f.savefig(savefigStr(simulationsLst[3])
        # f.savefig(savefigStr(simulationsLst[4])
        # f.savefig(savefigStr(simulationsLst[5])
        # f.savefig(savefigStr(simulationsLst[6])
        # f.savefig(savefigStr(simulationsLst[7])
        # f.savefig(savefigStr(simulationsLst[8])
        # f.savefig(savefigStr(simulationsLst[9])
        # f.savefig(savefigStr(simulationsLst[10])
        # f.savefig(savefigStr(simulationsLst[11])
        # f.savefig(savefigStr(simulationsLst[12])
    else:
        plt.title('Density profile', fontsize=30)
        plotName = '_Density.png'
        # f.savefig(savefigStr(simulationsLst[0])
        # f.savefig(savefigStr(simulationsLst[1])
        # f.savefig(savefigStr(simulationsLst[2])
        # f.savefig(savefigStr(simulationsLst[3])
        # f.savefig(savefigStr(simulationsLst[4])
        # f.savefig(savefigStr(simulationsLst[5])
        # f.savefig(savefigStr(simulationsLst[6])
        # f.savefig(savefigStr(simulationsLst[7])
        # f.savefig(savefigStr(simulationsLst[8])
        # f.savefig(savefigStr(simulationsLst[9])
        # f.savefig(savefigStr(simulationsLst[10])
        # f.savefig(savefigStr(simulationsLst[11])
        # f.savefig(savefigStr(simulationsLst[12])

if Fig2_Density_r_2:
    f = plt.figure(figsize=(16, 11))
    v = [-1, 1, -4, .5]
    plt.axis(v)
    x_plot = np.log10(binning_arr_lin_log10 / r_2)
    plt.xlabel(r'$ \log (\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$ \log \rho $', fontsize=30)
    plt.plot(x_plot[0:int(nr_binning_bins - 2)], np.log10(rho_arr),
             '-o', ms=2, lw=2, mew=0, c='green', label=r'$\rho$')

    plt.title(r'Density profile (B IC with 998 radial bins)',
              fontsize=30)
    plotName = '_Density_r_2.png'
    # f.savefig(savefigStr(simulationsLst[0])
    # f.savefig(savefigStr(simulationsLst[1])
    # f.savefig(savefigStr(simulationsLst[2])
    # f.savefig(savefigStr(simulationsLst[3])
    # f.savefig(savefigStr(simulationsLst[4])
    # f.savefig(savefigStr(simulationsLst[5])
    # f.savefig(savefigStr(simulationsLst[6])
    # f.savefig(savefigStr(simulationsLst[7])
    # f.savefig(savefigStr(simulationsLst[8])
    # f.savefig(savefigStr(simulationsLst[9])
    # f.savefig(savefigStr(simulationsLst[10])
    # f.savefig(savefigStr(simulationsLst[11])
    # f.savefig(savefigStr(simulationsLst[12])

if Fig3_Potential:
    f = plt.figure()
    ax1 = plt.subplot(121)
    plt.xlabel('r')
    plt.ylabel(r'$\Phi$')
    plt.title('Potential')
    plt.plot(Rcl, Vcl, 'o', ms=2, mew=0, color='blue')
    plt.grid()

    ax2 = plt.subplot(122)
    plt.xlabel(r'$\log r$')
    plt.plot(np.log10(Rcl), Vcl, 'o', ms=2, mew=0, color='blue')
    plt.grid()
    setp(ax2.get_yticklabels(), visible=False)

    plotName = '_Potential.png'
    # f.savefig(savefigStr(simulationsLst[0])
    # f.savefig(savefigStr(simulationsLst[1])
    # f.savefig(savefigStr(simulationsLst[2])
    # f.savefig(savefigStr(simulationsLst[3])
    # f.savefig(savefigStr(simulationsLst[4])
    # f.savefig(savefigStr(simulationsLst[5])
    # f.savefig(savefigStr(simulationsLst[6])
    # f.savefig(savefigStr(simulationsLst[7])
    # f.savefig(savefigStr(simulationsLst[8])
    # f.savefig(savefigStr(simulationsLst[9])
    # f.savefig(savefigStr(simulationsLst[10])
    # f.savefig(savefigStr(simulationsLst[11])
    # f.savefig(savefigStr(simulationsLst[12])

# plot rectangular slice through cluster:
if Fig4_xy_rectangular:
    f = plt.figure()
    plt.title('Rectangular slice through cluster')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.hist2d(xclrec, yclrec, bins=200, norm=LogNorm())
    plt.colorbar()

    plotName = '_xy_rectangular.png'
    # f.savefig(savefigStr(simulationsLst[0])
    # f.savefig(savefigStr(simulationsLst[1])
    # f.savefig(savefigStr(simulationsLst[2])
    # f.savefig(savefigStr(simulationsLst[3])
    # f.savefig(savefigStr(simulationsLst[4])
    # f.savefig(savefigStr(simulationsLst[5])
    # f.savefig(savefigStr(simulationsLst[6])
    # f.savefig(savefigStr(simulationsLst[7])
    # f.savefig(savefigStr(simulationsLst[8])
    # f.savefig(savefigStr(simulationsLst[9])
    # f.savefig(savefigStr(simulationsLst[10])
    # f.savefig(savefigStr(simulationsLst[11])
    # f.savefig(savefigStr(simulationsLst[12])

# 3 plots of the velocities as function of x.
if Fig5_cartesian_velocities:
    f = plt.figure()
    ax1 = plt.subplot(131)
    plt.ylabel('vxnew')
    plt.plot(xclrec, vxnew, 'o', ms=2, mew=0, color='blue')
    plt.title('velocities')
    ax2 = plt.subplot(132)
    plt.xlabel('x')
    plt.ylabel('vynew')
    plt.plot(xclrec, vynew, 'o', ms=2, mew=0, color='blue')
    setp( ax2.get_yticklabels(), visible=False)
    ax3 = plt.subplot(133)
    plt.ylabel('vznew')
    plt.plot(xclrec, vznew, 'o', ms=2, mew=0, color='blue')
    setp(ax3.get_yticklabels(), visible=False)

    plotName = '_cartesian_velocities.png'
    # f.savefig(savefigStr(simulationsLst[0])
    # f.savefig(savefigStr(simulationsLst[1])
    # f.savefig(savefigStr(simulationsLst[2])
    # f.savefig(savefigStr(simulationsLst[3])
    # f.savefig(savefigStr(simulationsLst[4])
    # f.savefig(savefigStr(simulationsLst[5])
    # f.savefig(savefigStr(simulationsLst[6])
    # f.savefig(savefigStr(simulationsLst[7])
    # f.savefig(savefigStr(simulationsLst[8])
    # f.savefig(savefigStr(simulationsLst[9])
    # f.savefig(savefigStr(simulationsLst[10])
    # f.savefig(savefigStr(simulationsLst[11])
    # f.savefig(savefigStr(simulationsLst[12])

plt.show()
