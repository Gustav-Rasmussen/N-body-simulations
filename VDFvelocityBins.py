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
import GaussianAndTsallis
import Gammas_and_R_middles
import getSnapshotValues

# Run 3D plots with this command from terminal:
# ~/python/3dplot/bin/python VDF.py

# readline will not be well behaved unless this is installed:
# pip install gnureadline

# Make switches to control figures, print statements, binning etc.
vspherical = 0
vbin = 0
Fig_sigmas = 0
vspherical_sigma = 0
print_Vp_Vn = 0
print_sigma_binned_lin_radius = 0
Fig_vr_vtheta_vphi_vt_sigma = 0
Fig_vr_vtheta_vphi_vt_sigma_bin_average = 0

# radial and tangential velocities
if vspherical:
    r = (x ** 2 + y ** 2 + z ** 2) ** .5
    Phi = sp.arctan2(y, x)
    Theta = sp.arccos(z / r)
    VR = sp.sin(Theta) * sp.cos(Phi) * vx + sp.sin(Theta)
         * sp.sin(Phi) * vy + sp.cos(Theta) * vz
    VTheta = sp.cos(Theta) * sp.cos(Phi) * vx + sp.cos(Theta)
             * sp.sin(Phi) * vy - sp.sin(Theta) * vz
    VPhi = - sp.sin(Phi) * vx + sp.cos(Phi) * vy
    VT = VTheta + VPhi

if vbin:
    for i in range(nr_binning_bins_v - 2):  # loop over 0-998
        min_v_bin_i = v_binning_arr[i]  # start of bin
        max_v_bin_i = v_binning_arr[i + 1]  # end of bin
        # position of particles inside a radial bin
        posv_par_inside_bin_i = np.where((v_hob_par > min_v_bin_i)
                                         * (v_hob_par < max_v_bin_i))
        # number of particles inside a radial bin
        nr_par_inside_bin_i = len(posv_par_inside_bin_i)
        if nr_par_inside_bin_i == 0:
            continue

        v_inside_bin_i = v[posv_par_inside_bin_i]
        V_R_inside_bin_i = VR[posv_par_inside_bin_i]
        V_T_inside_bin_i = VT[posv_par_inside_bin_i]

        v_arr.append(v_inside_bin_i)
        v_r_arr.append(v_r_inside_bin_i)
        v_t_arr.append(v_t_inside_bin_i)
        nr_par_inside_bin.append(nr_par_inside_bin_i)

    f = plt.figure()  # plot structure over velocity bins.
    plt.subplot(121)
    plt.xlabel(r'$v, v_r$ and $v_t$')
    plt.ylabel('Number of particles')
    plt.title(r'VDF (Hernquist structure, $10^6$ particles)')
    plt.hist(v_arr[15], bins=100, histtype='step', color='red',
             range=(v_limit_min, v_limit_max), label=r'$v$', lw=2)
    plt.hist(v_r_arr[15], bins=100, histtype='step', color='blue',
             range=(v_limit_min,v_limit_max), label=r'$v_r$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.show()
    plt.hist(v_r, bins=100, histtype='step', color='skyblue',
             range=(v_limit_min, v_limit_max), label=r'$v_r$', lw=2)
    plt.hist(v_t, bins=100, histtype='step', color='black',
             range=(-4, 4), label=r'$v_t$', lw=2)

    plt.subplot(122)
    plt.xlabel(r'$\log v$, $\log v_r$ and $\log v_t$')
    plt.hist(np.log10(np.absolute(v_arr)), bins=100, histtype='step',
                      color='red', range=(-5, 1), label=r'$\log v$',
                      lw=2)
    plt.hist(np.log10(np.absolute(v_r)), bins=100, histtype='step',
             color='skyblue', range=(-5, 1), label=r'$\log v_r$', lw=2)
    plt.hist(np.log10(np.absolute(v_t)), bins=100, histtype='step',
             color='black', range=(-5, 1), label=r'$\log v_t$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

    f = plt.figure()
    plt.xlabel(r'$v_r$ and $v_t$')
    plt.ylabel('Number of particles')
    plt.title('velocity distributions')
    plt.hist(v_r_arr[5], bins=30, histtype='step', color='red',
             range=(-4, 1), label=r'$v_r$ (bin 5)', normed=True, lw=2)
    plt.hist(v_r_arr[8], bins=30, histtype='step', color='skyblue',
             range=(-4, 1), label=r'$v_r$ (bin 8)', normed=True, lw=2)
    plt.hist(v_r_arr[10], bins=300, histtype='step', color='black',
             range=(-1, 1), label=r'$v_r$ (bin 10)', lw=2)
    plt.hist(.5 * v_t_arr[5], bins=30, histtype='step', color='green',
             range=(-4, 1), label=r'$v_t$ (bin 5)', normed=True, lw=2)
    plt.hist(.5 * v_t_arr[8], bins=30, histtype='step', color='blue',
             range=(-4, 1), label=r'$v_t$ (bin 8)', normed=True, lw=2)
    plt.hist(v_t_arr[10], bins=300, histtype='step', color='orange',
             range=(-1, 1), label=r'$v_t$ (bin 10)', lw=2)
    plt.hist(.25 * v_t_arr[10], bins=300, histtype='step', color='red',
             range=(-2, 1), label=r'$\frac{1}{4}\cdot v_t$ (bin 10)',
             lw=2)
    plt.hist(v_t_arr[10] * v_t_arr[10], bins=300, histtype='step',
             color='green',  range=(-2, 1),
             label=r'$v_t\cdot v_t$ (bin 10)', lw=2)
    plt.hist(2 * v_t_arr[10], bins=300, histtype='step', color='blue',
             range=(-2, 1), label=r'$2 \cdot v_t$ (bin 10)', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

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
    plt.plot(x_plot,y_plot,'-o', ms=8, mew=0, color='red',
             label=r'$\log \sigma_{total}$')
    y_plot = np.log10(sigmarad)
    plt.plot(x_plot,y_plot,'--s', ms=8, mew=0, color='blue',
             label=r'$\log \sigma_r$')
    y_plot = np.log10(sigmatheta)
    plt.plot(x_plot,y_plot,'--v', ms=8, mew=0, color='green',
             label=r'$\log \sigma_{\theta}$')
    y_plot = np.log10(sigmaphi)
    plt.plot(x_plot,y_plot,'--^', ms=8, mew=0, color='black',
             label=r'$\log \sigma_{\phi}$')
    y_plot = np.log10(sigmatan)
    plt.plot(x_plot,y_plot,'--^', ms=8, mew=0, color='Violet',
             label=r'$\log \sigma_{tan}$')
    plt.xlabel(r'$\log $r (kpc)', fontsize=20)
    plt.ylabel(r'$\log \sigma$', fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=3, handlelength=2.5)
    plt.grid()

if vspherical_sigma:
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
    VTheta = np.array(VTheta)
    VPhi = np.array(VPhi)
    VR_sigmarad = np.array(VR_sigmarad)
    VTheta_sigmatheta = np.array(VTheta_sigmatheta)
    VPhi_sigmaphi = np.array(VPhi_sigmaphi)

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
# Next I will plot v/sigma along the x-axes instead
# (or maybe with log(v/sigma)).
# Plotting v/sigma makes it easier to compare different radial bins,
# because the x-axis will almost always be the same,
# even though they actually have very different sigma.

if Fig12_vr_vtheta_vphi_vt_sigma:
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
        plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s'
                  % (len(x), Gamma, F))
        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='Black',
                                    label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F + '_VT_sigmatan_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')
        # print 'F + _VT_sigmatan_gamma_%.2f.txt % Gamma = ',
        #        F + '_VT_sigmatan_gamma_%.2f.txt' % Gamma

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='red',
                                    label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_VR_sigmarad_gamma_%.2f.txt' % Gamma, x,
                   delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,
                                    histtype='step', color='blue',
                                    label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_VTheta_sigmatheta_gamma_%.2f.txt' % Gamma, x,
                   delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='green',
                                    label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_VPhi_sigmaphi_gamma_%.2f.txt' % Gamma, x,
                   delimiter = ' ',
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
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F + '_logx10_gamma_%.2f.txt' % Gamma, x,
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
        np.savetxt(F + '_logx9_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\theta}n|, v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_logx7_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        # (mu, sigma) = norm.fit(np.log10(x9))
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        # popt, pcov = curve_fit(func_1_log, xdata, ydata)
        # y_fit = func_1_log(xdata, popt[0], popt[1])
        # plt.plot(xdata, y_fit, '--', lw=3, color='pink',
        #          label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_logx8_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')
        ax2.set_yscale('log')
        # plt.ylim(10 ** -1, 10 ** 3)
        # plt.xlim(-3.5, 0)
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

    if new_R_middle:
        f = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$,File=%s,new R_middle'
                  % (len(x), Gamma, F))
        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='Black',
                                    label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_VT_sigmatan_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')
        # print('F + _VT_sigmatan_gamma_%.2f.txt %Gamma = ', F + '_VT_sigmatan_gamma_%.2f.txt' % Gamma)

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='red',
                                    label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_VR_sigmarad_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,
                                    histtype='step', color='blue',
                                    label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_VTheta_sigmatheta_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='green',
                                    label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_VPhi_sigmaphi_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')
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
        np.savetxt(F + '_new_R_middle_logx8_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
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
        plt.title(r'$N=%i$, $R_{middle} = %.2f$, File = %s , new R_middle'
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
        x = np.array((xdata, ydata))
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
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_VTheta_sigmatheta_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='green',
                                    label=r'$f\left( u_{\phi} \right)$',
                                    alpha=.75)
        xdata            = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata            = n
        x                = np.array((xdata, ydata))
        x                = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_VPhi_sigmaphi_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                                    alpha=.75)
        xdata            = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata            = n
        x                = np.array((xdata, ydata))
        x                = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_logx10_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',
                                    color='red',range=(-3,1),
                                    label=r'$f\left(\log \left( |u_rn|,u_rp \right)\right)$',
                                    alpha=.75)
        xdata            = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata            = n
        x                = np.array((xdata, ydata))
        x                = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_logx9_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_{\theta}n|,u_{\theta}p \right)\right)$',
                                    alpha=.75)
        xdata            = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata            = n
        x                = np.array((xdata, ydata))
        x                = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_logx7_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_{\phi}n|,u_{\phi}p \right)\right)$',
                                    alpha=.75)
        xdata            = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata            = n
        x                = np.array((xdata, ydata))
        x                = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_logx8_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

if Fig18_vr_vtheta_vphi_vt_sigma_bin_average:
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
        ax1              = f.add_subplot(121)
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
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
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
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_average_logx10_gamma_%.2f.txt' % Gamma, x,
                   delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_average_logx9_gamma_%.2f.txt'%Gamma,x,delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left(\frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
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
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_average_logx8_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

    if new_R_middle:
        f = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$,File = %s, new R_middle'
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

        ax2 = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$',
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
                                    label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_new_R_middle_average_logx9_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_new_R_middle_average_logx7_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( \frac{|v_{\phi}n|, v_{\phi}p}{\sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_new_R_middle_average_logx8_gamma_%.2f.txt'
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
        plt.title(r'$N=%i$, $R_{middle} = %.2f$,File = %s, new R_middle'
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

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_tn|, u_tp \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata , ydata))
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
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='blue', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_{\theta}n|, u_{\theta}p \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_average_logx7_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_{\phi}n|,u_{\phi}p \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F
                   + '_large_R_middle_average_logx8_R_middle_%.2f.txt'
                   % R_middle, x, delimiter = ' ',
                   header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|, u_tp \right)$, $\log\
                   \left( |u_rn|, u_rp \right)$, $\log \left(\
                   |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

plt.show()
