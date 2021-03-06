# -*- coding: utf-8 -*-

from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np

import Mock_data as mock
from RhoAndGaussianAndTsallis import rho_HQ
import Sigma_calc_OOP as scoop

figurePath = mock.figurePath
Gamma = mock.Gamma
Gammas = mock.Gammas
x, y, z = mock.x, mock.y, mock.z
R = mock.R
R_middle = mock.R_middle
R_limit = mock.R_limit
R_hob_par = R[mock.GoodIDs]
m = mock.m
nr_bins = mock.nr_bins
max_binning_R_unitRmax = mock.max_binning_R_unitRmax
min_binning_R_unitRmax = mock.min_binning_R_unitRmax
Rcl, Vcl, xclrec, yclrec = mock.Rcl, mock.Vcl, mock.xclrec, mock.yclrec
vxnew, vynew, vznew = mock.vxnew, mock.vynew, mock.vznew

simulationsLst = ['A', 'B', 'Soft_B', 'CS1', 'CS2', 'CS3', 'CS4',
                  'CS5', 'CS6', 'DS1', 'D2', 'Soft_D2', 'E']


def get_sphere_volume(radius: np.ndarray) -> np.ndarray:
    return 4 / 3 * np.pi * radius ** 3


def get_bin_number_density(number, volume):
    """Get the number density of particles inside a radial bin of a cluster."""
    return number / volume


def get_bin_density(mass, number_density):
    """Get the density of particles inside a radial bin of a cluster."""
    return mass * number_density


def get_volume_ratio(bin_density, cluster_volume, bin_mass):
    """Get the ratio between volume of bin and total cluster
    volume."""
    return bin_density * cluster_volume / bin_mass


def savefigStr(simName, plotName):
    return f'{figurePath}{simName}{plotName}'


if Gamma == Gammas[1]:
    r_2 = R_middle
    # position of particles in halo
    posR_par_in_halo = np.where(R_hob_par < r_2)
    nr_par_in_halo = len(posR_par_in_halo[0])
    M_2 = nr_par_in_halo * m
    G = 1.
    v_circ_2 = scoop.get_circular_velocity(M_2, r_2)
    V_2 = get_sphere_volume(r_2)

(density_arr, Volume_arr, rho_arr, rho_2_arr) = ([] for i in range(4))

# Array, 0.00001-1.
binning_arr_lin_log10_unitRmax = 10 ** ((np.arange(nr_bins) / (nr_bins - 1))
                                        * abs(np.log10(max_binning_R_unitRmax)
                                        - np.log10(min_binning_R_unitRmax))
                                        + np.log10(min_binning_R_unitRmax))

# Array, 0-500
binning_arr_lin_log10 = R_limit * binning_arr_lin_log10_unitRmax
for i in range(0, int(nr_bins - 2)):  # loop over 0-998
    min_R_bin_i = binning_arr_lin_log10[i]  # start of bin
    max_R_bin_i = binning_arr_lin_log10[i + 1]  # end of bin
    # position of particles inside a radial bin
    posR_par_in_bin_i = np.where(min_R_bin_i < R < max_R_bin_i)[0]
    # number of particles inside a radial bin
    nr_par_in_bin_i = len(posR_par_in_bin_i)
    # Volume of cluster
    Volume_cl = scoop.get_volume_slice(min_R_bin_i, max_R_bin_i)
    den_cl = get_bin_number_density(nr_par_in_bin_i, Volume_cl)
    rho = get_bin_density(mock.m, den_cl)
    rho_2 = get_volume_ratio(rho, V_2, M_2)

    # save arrays
    density_arr.append(den_cl)
    Volume_arr.append(Volume_cl)
    rho_arr.append(rho)
    rho_2_arr.append(rho_2)

Invers_Volume_arr = np.log10(np.divide(np.ones(len(Volume_arr)), Volume_arr))

print(f'{len(density_arr)= }',
      f'{len(rho_arr)= }',
      f'{len(x)= }',
      f'{len(y)= }',
      f'{len(z)= }',
      f'{len(R)= }'
      )

for i in [0, 100, 99999]:
    print(f'{x[i]= }',
          f'{y[i]= }',
          f'{z[i]= }',
          f'{R[i]= }'
          )

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
    plt.plot(x_plot[0:int(nr_bins - 2)], np.log10(rho_arr), 'g-o', ms=2,
             lw=2, mew=0, label=r'$\rho$')
    if Fig1_Densityfit:
        x = binning_arr_lin_log10
        y_plot = rho_HQ(1. / (2 * np.pi), 1., x)
        plt.plot(np.log10(x), np.log10(y_plot), 'k:o', ms=2, lw=2, mew=0,
                 label=r'$\frac{1}{2\pi r (1+r)^3}$')
        plt.title('Density profile (B IC with 998 radial bins)', fontsize=30)
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
    plt.xlabel(r'$\log(\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$\log\rho$', fontsize=30)
    plt.plot(x_plot[0:int(nr_bins - 2)], np.log10(rho_arr), 'g-o', ms=2,
             lw=2, mew=0, label=r'$\rho$')
    plt.title('Density profile (B IC with 998 radial bins)', fontsize=30)
    plotName = '_Density_r_2.png'
    f.savefig(savefigStr(simulationsLst[0], plotName))

if Fig3_Potential:
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.xlabel('r')
    ax1.ylabel(r'$\Phi$')
    ax1.title('Potential')
    ax1.plot(Rcl, Vcl, 'bo', ms=2, mew=0)
    ax1.grid()
    ax2.xlabel(r'$\log r$')
    ax2.plot(np.log10(Rcl), Vcl, 'bo', ms=2, mew=0)
    ax2.grid()
    f.setp(ax2.get_yticklabels(), visible=False)
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
    f, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.ylabel('vxnew')
    ax1.plot(xclrec, vxnew, 'bo', ms=2, mew=0)
    ax1.title('velocities')
    ax2.xlabel('x')
    ax2.ylabel('vynew')
    ax2.plot(xclrec, vynew, 'bo', ms=2, mew=0)
    f.setp(ax2.get_yticklabels(), visible=False)
    ax3.ylabel('vznew')
    ax3.plot(xclrec, vznew, 'bo', ms=2, mew=0)
    f.setp(ax3.get_yticklabels(), visible=False)
    plotName = '_cartesian_velocities.png'
    f.savefig(savefigStr(simulationsLst[0], plotName))

plt.show()
