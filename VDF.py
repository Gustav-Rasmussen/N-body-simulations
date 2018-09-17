# -*- coding: utf-8 -*-

from __future__ import division
import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
from pylab import *
import pylab
from scipy.stats import norm
import matplotlib.mlab as mlab
import scipy as sp
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import os
import Gammas_and_R_middles
import RhoAndGaussianAndTsallis
import getSnapshotValues
import snapshotFiles

# Run 3D plots with this command from terminal:
# ~/python/3dplot/bin/python VDF.py

# readline will not be well behaved unless this is installed:
# pip install gnureadline

UserPath = os.getcwd()
DesktopPath = UserPath + 'Desktop/'
GADGET_G_path = DesktopPath + 'RunGadget/G_perturbations/'
StablePath = 'G_perturbations/StableStructures/'
figurePath = DesktopPath + StablePath + 'figures/'
textFilesPath = DesktopPath + StablePath + 'textFiles/'
MartinPath = 'Martin_IC_and_Final_Edd_and_OM/'
hdf5Path = DesktopPath + 'G_perturbations/hdf5_files/'
nosyncPath = UserPath + 'nosync/RunGadget/'

# Make switches to control figures, print statements, binning etc.
Fig_xz = 0
Fig_3D_xyz = 0
vspherical = 0
calc_sigma_binned_lin_radius = 0
Fig_sigmas = 0
vsphericalnew_sigma = 0
print_Vp_Vn = 0
print_sigma_binned_lin_radius = 0
Fig_vr_vtheta_vphi_vt_sigma = 0
Fig_vr_vtheta_vphi_vt_sigma_bin_average = 0

if Fig_xz:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    ax1.plot(x, y, 'o', ms=1)
    ax1.set_xlabel(r'$x$', fontsize=30)
    ax1.set_ylabel(r'$y$', fontsize=30)
    ax1.set_title(r'positions ($N = %i$)' % len(x), fontsize=30)

    ax2.plot (x,z,'o', ms=1)
    ax2.set_xlabel(r'$x$', fontsize=30)
    ax2.set_ylabel(r'$z$', fontsize=30)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")

    f.savefig(figurePath + 'Fig_xz.png')


def randrange(n, vmin, vmax):  # 3D scatterplot of positions
   return (vmax - vmin) * np.random.rand(n) + vmin


if Fig_3D_xyz:
    f = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    n = 100
    for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        ax.scatter(x, y, z, c=c, marker=m)
    ax.set_xlabel('x', fontsize=20)
    ax.set_ylabel('y', fontsize=20)
    ax.set_zlabel('z', fontsize=20)
    ax.set_title('3D view of halo structure.($N = %i$, $\gamma = %.2f $)'
                 % (len(x), Gamma), fontsize=20)

# radial and tangential velocities
if vspherical:
    r = (x ** 2 + y ** 2 + z ** 2) ** .5
    Phi = sp.arctan2(y, x)
    Theta = sp.arccos(z / r)
    VR = sp.sin(Theta) * sp.cos(Phi) * vx + sp.sin(Theta) * sp.sin(Phi)
         * vy + sp.cos(Theta) * vz
    VTheta = sp.cos(Theta) * sp.cos(Phi) * vx + sp.cos(Theta)
         * sp.sin(Phi) * vy - sp.sin(Theta) * vz
    VPhi = - sp.sin(Phi) * vx + sp.cos(Phi) * vy
    VT = VTheta + VPhi

if calc_sigma_binned_lin_radius:
    R_hob_par = R[GoodIDs]
    v2 = vx ** 2 + vy ** 2 + vz ** 2

    (sigma2, sigmarad2, sigmatheta2, sigmaphi2, sigmatan2, sigma,
    sigmarad, sigmatheta, sigmaphi, sigmatan, VR_sigmarad,
    VTheta_sigmatheta, VPhi_sigmaphi, VT_sigmatan, r, Phi, Theta, VR,
    VTheta, VPhi, VT, VR_i_average_inside_bin, VT_i_average_inside_bin,
    VTheta_i_average_inside_bin, VPhi_i_average_inside_bin,
    VR_i_average_inside_bin_sigmarad, VT_i_average_inside_bin_sigmatan,
    VTheta_i_average_inside_bin_sigmatheta,
    VPhi_i_average_inside_bin_sigmaphi, bin_radius_arr) =
    ([] for i in range(30))

    min_binning_R = -1.5
    max_binning_R = np.log10(R_limit)
    # min_binning_R = R_limit_min
    # max_binning_R = R_limit_max

    binning_arr = np.logspace(min_binning_R, max_binning_R, nr_binning_bins)
    # binning_arr = np.linspace(R_limit_min, R_limit_max, nr_binning_bins)

    j = 0
    for i in range(nr_binning_bins - 2):
        min_R_bin_i = binning_arr[j]  # start of bin
        max_R_bin_i = binning_arr[j+1]  # end of bin
        # position of particles inside a radial bin
        posR_par_inside_bin_i = np.where((R_hob_par > min_R_bin_i)
                                          & (R_hob_par < max_R_bin_i))
        nr_par_inside_bin_i = len(posR_par_inside_bin_i[0])
        if nr_par_inside_bin_i == 0:
            print('-', i)
            continue
        print('+', i)

        r_i = (x[posR_par_inside_bin_i] ** 2 + y[posR_par_inside_bin_i]
              ** 2 + z[posR_par_inside_bin_i] ** 2) ** .5
        Phi_i = sp.arctan2(y[posR_par_inside_bin_i],
                           x[posR_par_inside_bin_i])
        Theta_i = sp.arccos(z[posR_par_inside_bin_i] / r_i)
        VR_i = sp.sin(Theta_i) * sp.cos(Phi_i)
               * vx[posR_par_inside_bin_i] + sp.sin(Theta_i)
               * sp.sin(Phi_i) * vy[posR_par_inside_bin_i]
               + sp.cos(Theta_i) * vz[posR_par_inside_bin_i]
        VTheta_i = sp.cos(Theta_i) * sp.cos(Phi_i)
                   * vx[posR_par_inside_bin_i] + sp.cos(Theta_i)
                   * sp.sin(Phi_i) * vy[posR_par_inside_bin_i]
                   - sp.sin(Theta_i) * vz[posR_par_inside_bin_i]
        VPhi_i = - sp.sin(Phi_i) * vx[posR_par_inside_bin_i]
                 + sp.cos(Phi_i) * vy[posR_par_inside_bin_i]
        VT_i = (VTheta_i ** 2 + VPhi_i ** 2) ** .5

        # sigma2 total
        v2_inside_bin_i = v2[posR_par_inside_bin_i]
        sigma2_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                              * np.sum(v2_inside_bin_i)
        sigma2.append(sigma2_inside_bin_i)
        bin_radius_arr.append((max_R_bin_i + min_R_bin_i) / 2)

        # sigmatan2
        vtan2_inside_bin_i = VT_i ** 2
        sigmatan2_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                 * np.sum(vtan2_inside_bin_i)
        sigmatan2.append(sigmatan2_inside_bin_i)

        # sigmarad2 radial
        vrad2_inside_bin_i = VR_i ** 2
        sigmarad2_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                 * np.sum(vrad2_inside_bin_i)
        sigmarad2.append(sigmarad2_inside_bin_i)

        # sigmatheta2
        VTheta2_inside_bin_i = VTheta_i ** 2
        sigmatheta2_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                   * np.sum(VTheta2_inside_bin_i)
        sigmatheta2.append(sigmatheta2_inside_bin_i)

        # sigmaphi2
        VPhi2_inside_bin_i = VPhi_i ** 2
        sigmaphi2_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                 * np.sum(VPhi2_inside_bin_i)
        sigmaphi2.append(sigmaphi2_inside_bin_i)

        VR_i_average_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                    * np.sum(VR_i)
        VT_i_average_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                    * np.sum(VT_i)
        VTheta_i_average_inside_bin_i = (1. /
                                        (nr_par_inside_bin_i + 1.))
                                        * np.sum(VTheta_i)
        VPhi_i_average_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                      * np.sum(VPhi_i)

        VR_i_average_inside_bin.append(VR_i_average_inside_bin_i)
        VT_i_average_inside_bin.append(VT_i_average_inside_bin_i)
        VTheta_i_average_inside_bin.append(VTheta_i_average_inside_bin_i)
        VPhi_i_average_inside_bin.append(VPhi_i_average_inside_bin_i)

        sigma_i = (sigma2[j]) ** .5
        sigmarad_i = (sigmarad2[j]) ** .5
        sigmatheta_i = (sigmatheta2[j]) ** .5
        sigmaphi_i = (sigmaphi2[j]) ** .5
        sigmatan_i = (sigmatan2[j]) ** .5

        sigma.append(sigma_i)
        sigmarad.append(sigmarad_i)
        sigmatheta.append(sigmatheta_i)
        sigmaphi.append(sigmaphi_i)
        sigmatan.append(sigmatan_i)
        r.append(r_i)
        Phi.append(Phi_i)
        Theta.append(Theta_i)
        VR.append(VR_i)
        VTheta.append(VTheta_i)
        VPhi.append(VPhi_i)
        VT.append(VT_i)
        VR_sigmarad.append(VR_i / sigmarad_i)
        VTheta_sigmatheta.append(VTheta_i / sigmatheta_i)
        VPhi_sigmaphi.append(VPhi_i / sigmaphi_i)
        VT_sigmatan.append(VT_i / sigmatan_i)
        VR_i_average_inside_bin_sigmarad.append(VR_i_average_inside_bin_i
                                                / sigmarad_i)
        VT_i_average_inside_bin_sigmatan.append(VT_i_average_inside_bin_i
                                                / sigmatan_i)
        VTheta_i_average_inside_bin_sigmatheta.append(VTheta_i_average_inside_bin_i
                                                      / sigmatheta_i)
        VPhi_i_average_inside_bin_sigmaphi.append(VPhi_i_average_inside_bin_i
                                                  / sigmaphi_i)

        j += 1

    sigma2 = np.array(sigma2)
    sigmarad2 = np.array(sigmarad2)
    sigmatheta2 = np.array(sigmatheta2)
    sigmaphi2 = np.array(sigmaphi2)
    sigmatan2 = np.array(sigmatan2)
    sigma = np.array(sigma)
    sigmarad = np.array(sigmarad)
    sigmatheta = np.array(sigmatheta)
    sigmaphi = np.array(sigmaphi)
    sigmatan = np.array(sigmatan)

if Fig_sigmas:
    f = plt.figure()
    plt.subplot(121)
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma2)
    plt.plot(x_plot, y_plot, '-o', ms=8, mew=0, color='red',
             label=r'$\log \sigma_{total}^2$')
    y_plot = np.log10(sigmarad2)
    plt.plot(x_plot, y_plot, '--s', ms=8, mew=0, color='blue',
             label=r'$\log \sigma_{r}^2$')
    y_plot = np.log10(sigmatheta2)
    plt.plot(x_plot, y_plot, '--v', ms=8, mew=0, color='green',
             label=r'$\log \sigma_{\theta}^2$')
    y_plot = np.log10(sigmaphi2)
    plt.plot(x_plot, y_plot, '--^', ms=8, mew=0, color='black',
             label=r'$\log \sigma_{\phi}^2$')
    y_plot = np.log10(sigmatan2)
    plt.plot(x_plot, y_plot, '--^', ms=8, mew=0, color='Violet',
             label=r'$\log \sigma_{tan}^2$')
    plt.xlabel(r'$\log $r (kpc)', fontsize=20)
    plt.ylabel(r'$\log \sigma^2$', fontsize=20)
    plt.title(r'Velocity dispersions (File = %s, $\gamma=%.2f$)'
              % (F, Gamma), fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=3, handlelength=2.5)
    plt.grid()

    plt.subplot(122)
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma)
    plt.plot(x_plot, y_plot, '-o', ms=8, mew=0, color='red',
             label=r'$\log \sigma_{total}$')
    y_plot = np.log10(sigmarad)
    plt.plot(x_plot, y_plot, '--s', ms=8, mew=0, color='blue',
             label=r'$\log \sigma_r$')
    y_plot = np.log10(sigmatheta)
    plt.plot(x_plot, y_plot, '--v', ms=8, mew=0, color='green',
             label=r'$\log \sigma_{\theta}$')
    y_plot = np.log10(sigmaphi)
    plt.plot(x_plot, y_plot, '--^', ms=8, mew=0, color='black',
             label=r'$\log \sigma_{\phi}$')
    y_plot = np.log10(sigmatan)
    plt.plot(x_plot, y_plot, '--^', ms=8, mew=0, color='Violet',
             label=r'$\log \sigma_{tan}$')
    plt.xlabel(r'$\log $r (kpc)', fontsize=20)
    plt.ylabel(r'$\log \sigma$', fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=3, handlelength=2.5)
    plt.grid()

if vsphericalnew_sigma:
    (VR_sigmarad_p, VR_sigmarad_n, VTheta_sigmatheta_p,
    VTheta_sigmatheta_n, VPhi_sigmaphi_p, VPhi_sigmaphi_n,
    VT_sigmatan_p, VT_sigmatan_n) = ([] for i in range(8))

    for i in range(len(VR_sigmarad)):
        if VR_sigmarad[i] >= 0.:
            VR_sigmarad_p.append(VR_sigmarad[i])
        else:
            VR_sigmarad_n.append(VR_sigmarad[i])
    VR_sigmarad_p_arr = np.asarray(VR_sigmarad_p)
    VR_sigmarad_n_arr = np.asarray(VR_sigmarad_n)

    for i in range(len(VR_sigmarad)):
        if VTheta_sigmatheta[i] >= 0.:
            VTheta_sigmatheta_p.append(VTheta_sigmatheta[i])
        else:
            VTheta_sigmatheta_n.append(VTheta_sigmatheta[i])
    VTheta_sigmatheta_p_arr = np.asarray(VTheta_sigmatheta_p)
    VTheta_sigmatheta_n_arr = np.asarray(VTheta_sigmatheta_n)

    for i in range(len(VR_sigmarad)):
        if VPhi_sigmaphi[i] >= 0.:
            VPhi_sigmaphi_p.append(VPhi_sigmaphi[i])
        else:
            VPhi_sigmaphi_n.append(VPhi_sigmaphi[i])
    VPhi_sigmaphi_p_arr = np.asarray(VPhi_sigmaphi_p)
    VPhi_sigmaphi_n_arr = np.asarray(VPhi_sigmaphi_n)

    for i in range(len(VR_sigmarad)):
        if VT_sigmatan[i] >= 0.:
            VT_sigmatan_p.append(VT_sigmatan[i])
        else:
            VT_sigmatan_n.append(VT_sigmatan[i])
    VT_sigmatan_p_arr = np.asarray(VT_sigmatan_p)
    VT_sigmatan_n_arr = np.asarray(VT_sigmatan_n)

    (VR_i_average_inside_bin_sigmarad_p,
     VR_i_average_inside_bin_sigmarad_n,
     VT_i_average_inside_bin_sigmatan_p,
     VT_i_average_inside_bin_sigmatan_n,
     VPhi_i_average_inside_bin_sigmaphi_p,
     VPhi_i_average_inside_bin_sigmaphi_n,
     VTheta_i_average_inside_bin_sigmatheta_p,
     VTheta_i_average_inside_bin_sigmatheta_n) = ([] for i in range(8))

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VR_i_average_inside_bin_sigmarad[i] >= 0.:
            VR_i_average_inside_bin_sigmarad_p.append(VR_i_average_inside_bin_sigmarad[i])
        else:
            VR_i_average_inside_bin_sigmarad_n.append(VR_i_average_inside_bin_sigmarad[i])
    VR_i_average_inside_bin_sigmarad_p_arr = np.asarray(VR_i_average_inside_bin_sigmarad_p)
    VR_i_average_inside_bin_sigmarad_n_arr = np.asarray(VR_i_average_inside_bin_sigmarad_n)

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VTheta_i_average_inside_bin_sigmatheta[i] >= 0.:
            VTheta_i_average_inside_bin_sigmatheta_p.append(VTheta_i_average_inside_bin_sigmatheta[i])
        else:
            VTheta_i_average_inside_bin_sigmatheta_n.append(VTheta_i_average_inside_bin_sigmatheta[i])
    VTheta_i_average_inside_bin_sigmatheta_p_arr = np.asarray(VTheta_i_average_inside_bin_sigmatheta_p)
    VTheta_i_average_inside_bin_sigmatheta_n_arr = np.asarray(VTheta_i_average_inside_bin_sigmatheta_n)

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VPhi_i_average_inside_bin_sigmaphi[i] >= 0.:
            VPhi_i_average_inside_bin_sigmaphi_p.append(VPhi_i_average_inside_bin_sigmaphi[i])
        else:
            VPhi_i_average_inside_bin_sigmaphi_n.append(VPhi_i_average_inside_bin_sigmaphi[i])
    VPhi_i_average_inside_bin_sigmaphi_p_arr = np.asarray(VPhi_i_average_inside_bin_sigmaphi_p)
    VPhi_i_average_inside_bin_sigmaphi_n_arr = np.asarray(VPhi_i_average_inside_bin_sigmaphi_n)

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VT_i_average_inside_bin_sigmatan[i] >= 0.:
            VT_i_average_inside_bin_sigmatan_p.append(VT_i_average_inside_bin_sigmatan[i])
        else:
            VT_i_average_inside_bin_sigmatan_n.append(VT_i_average_inside_bin_sigmatan[i])
    VT_i_average_inside_bin_sigmatan_p_arr = np.asarray(VT_i_average_inside_bin_sigmatan_p)
    VT_i_average_inside_bin_sigmatan_n_arr = np.asarray(VT_i_average_inside_bin_sigmatan_n)

if print_Vp_Vn:
    if print_sigma_binned_lin_radius:
        print('sigmarad2 = ', sigmarad2)
        print('sigmarad2.shape = ', sigmarad2.shape)
        print('sigmatheta2 = ', sigmatheta2)
        print('sigmatheta2.shape = ', sigmatheta2.shape)
        print('sigmaphi2 = ', sigmaphi2)
        print('sigmaphi2.shape = ', sigmaphi2.shape)
        print('sigmarad = ', sigmarad)
        print('sigmarad.shape = ', sigmarad.shape)
        print('sigmatheta = ', sigmatheta)
        print('sigmatheta.shape = ', sigmatheta.shape)
        print('sigmaphi = ', sigmaphi)
        print('sigmaphi.shape = ', sigmaphi.shape)
        print('VR = ', VR)
        print('VR.shape = ', VR.shape)
        print('VTheta = ', VTheta)
        print('VTheta.shape = ', VTheta.shape)
        print('VPhi = ', VPhi)
        print('VPhi.shape = ', VPhi.shape)
        print('VR_sigmarad.shape = ', (VR / sigmarad).shape)
        print('VR_sigmarad = ', VR / sigmarad)
        print('np.where(sigmarad == 0) = ', np.where(sigmarad == 0))
        print('np.where(sigmatheta == 0) = ', np.where(sigmatheta == 0))
        print('np.where(sigmaphi == 0) = ', np.where(sigmaphi == 0))

# All figures with log(v) can instead be plotted as log(v) vs. f(v)/v.
# the idea is, that a flat tail will appear towards small velocities.
# Next I will plot v/sigma along the x-axes instead of v
# (and with log(v/sigma) as well).
# Plotting v/sigma makes it easier to compare different radial bins,
# because the x-axis will almost always be the same,
# even though they actually have very different sigma.

if Fig_vr_vtheta_vphi_vt_sigma:
    x7 = np.asarray(list(VTheta_sigmatheta_p_arr)
         + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_sigmaphi_p_arr)
         + list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_sigmarad_p_arr)
         + list(np.absolute(VR_sigmarad_n_arr)))
    x10 = np.asarray(list(VT_sigmatan_p_arr)
         + list(np.absolute(VT_sigmatan_n_arr)))
    if keep_IC_R_middle:
        f = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$ , File = %s'
                  % (len(x), Gamma, F))
        n, bins, patches = plt.hist(VT_sigmatan, 50,histtype='step',
                                    color='Black',
                                    label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_VT_sigmatan_gamma_%.2f.txt' % Gamma, x,
                   delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='red',
                                    label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_VR_sigmarad_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,
                                    histtype='step', color='blue',
                                    label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F+'_VTheta_sigmatheta_gamma_%.2f.txt' % Gamma, x,
                   delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='green',
                                    label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_VPhi_sigmaphi_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta}$ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        ax2   = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F+'_logx10_gamma_%.2f.txt' %Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',
                                    color='red', range=(-3,1),
                                    label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F+'_logx9_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50,histtype='step',
                                    color='blue', range=(-3,1),
                                    label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F+'_logx7_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green',range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F+'_logx8_gamma_%.2f.txt' %Gamma, x, delimiter = ' ',
                   header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=2,handlelength=2.5)
        plt.grid()

    if new_R_middle:
        f   = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$,File=%s,new R_middle' % (len(x),Gamma,F))
        n, bins, patches = plt.hist(VT_sigmatan,50,histtype='step',color='Black',label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F+'_new_R_middle_VT_sigmatan_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VR_sigmarad, 50,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F+'_new_R_middle_VR_sigmarad_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F+'_new_R_middle_VTheta_sigmatheta_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x     = np.array((xdata , ydata))
        x     = x.transpose()
        np.savetxt(F + '_new_R_middle_VPhi_sigmaphi_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   0header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        ax2 = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_logx10_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_logx9_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_logx7_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_logx8_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

    if large_R_middle:
        f = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $R_{middle} = %.2f$, File = %s, new R_middle'
                  % (len(x), R_middle, F))
        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='Black',
                                    label=r'$f\left( u_t \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_VT_sigmatan_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='red',
                                    label=r'$f\left( u_r \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_VR_sigmarad_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,
                                    histtype='step', color='blue',
                                    label=r'$f\left( u_{\theta} \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_VTheta_sigmatheta_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='green',
                                    label=r'$f\left( u_{\phi} \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_VPhi_sigmaphi_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        ax2   = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_logx10_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_rn|,u_rp \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_logx9_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_{\theta}n|,u_{\theta}p \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_logx7_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_{\phi}n|,u_{\phi}p \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_logx8_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

if Fig_vr_vtheta_vphi_vt_sigma_bin_average:
    x7 = np.asarray(list(VTheta_i_average_inside_bin_sigmatheta_p_arr)
                    + list(np.absolute(VTheta_i_average_inside_bin_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_i_average_inside_bin_sigmaphi_p_arr)
                    + list(np.absolute(VPhi_i_average_inside_bin_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_i_average_inside_bin_sigmarad_p_arr)
                    + list(np.absolute(VR_i_average_inside_bin_sigmarad_n_arr)))
    x10 = np.asarray(list(VT_i_average_inside_bin_sigmatan_p_arr)
                    + list(np.absolute(VT_i_average_inside_bin_sigmatan_n_arr)))

    if keep_IC_R_middle:
        f = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s'
                  % (len(x), Gamma, F))
        n, bins, patches = plt.hist(VT_i_average_inside_bin_sigmatan,
                                    50, histtype='step', color='Black',
                                    label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_VT_i_average_inside_bin_sigmatan_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VR_i_average_inside_bin_sigmarad,
                                    50, histtype='step', color='red',
                                    label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_VR_i_average_inside_bin_sigmarad_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_i_average_inside_bin_sigmatheta,
                                    50, histtype='step', color='blue',
                                    label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_VTheta_i_average_inside_bin_sigmatheta_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_i_average_inside_bin_sigmaphi,
                                    50, histtype='step', color='green',
                                    label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_VPhi_i_average_inside_bin_sigmaphi_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta}$ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        ax2 = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left(\frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_average_logx10_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_average_logx9_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left(\frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_average_logx7_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_average_logx8_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left(\
                   |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,\
                   u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,\
                   u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                   \right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

    if new_R_middle:
        f = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s , new R_middle'
                  % (len(x), Gamma, F))
        n, bins, patches = plt.hist(VT_i_average_inside_bin_sigmatan,
                                    50, histtype='step', color='Black',
                                    label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VR_i_average_inside_bin_sigmarad,
                                    50, histtype='step', color='red',
                                    label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_i_average_inside_bin_sigmatheta,
                                    50, histtype='step', color='blue',
                                    label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_i_average_inside_bin_sigmaphi,
                                    50, histtype='step', color='green',
                                    label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        ax2   = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_tn|, v_tp}{\sigma_t}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_average_logx10_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_rn|, v_rp}{\sigma_r}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_average_logx9_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\theta}n|, v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_average_logx7_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_average_logx8_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

    if large_R_middle:
        f = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $R_{middle} = %.2f$ , File = %s, new R_middle'
                  % (len(x), R_middle, F))
        n, bins, patches = plt.hist(VT_i_average_inside_bin_sigmatan,
                                    50, histtype='step', color='Black',
                                    label=r'$f\left(u_t \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VR_i_average_inside_bin_sigmarad,
                                    50, histtype='step', color='red',
                                    label=r'$f\left(u_r \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_i_average_inside_bin_sigmatheta,
                                    50, histtype='step', color='blue',
                                    label=r'$f\left( u_{\theta} \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_i_average_inside_bin_sigmaphi,
                                    50, histtype='step', color='green',
                                    label=r'$f\left( u_{\phi} \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        ax2 = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_average_logx10_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_rn|,u_rp \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_average_logx9_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_{\theta}n|,u_{\theta}p \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_average_logx7_R_middle_%.2f.txt'
                   % R_middle, x,
                   delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left(|u_{\phi}n|,u_{\phi}p \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_large_R_middle_average_logx8_R_middle_%.2f.txt'
                   % R_middle, x, delimiter=' ',
                   header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$,\
                     $\log \left( |u_rn|,u_rp \right)$,\
                     $\log \left( |u_{\theta}n|,u_{\theta}p \right)$\
                     and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
                   u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

plt.show()
