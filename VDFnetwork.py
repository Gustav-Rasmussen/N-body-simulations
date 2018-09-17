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
import scipy
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D
import Gammas_and_R_middles
import os
import getSnapshotValues
import RhoAndGaussianAndTsallis
import velocityCheck
import snapshotFiles

# HQ1000000_150311_000.hdf5
# Gamma = -1.5, logr = -.75, r = 10 ** -.75
# Gamma = -2, logr = -.35, r = 10 ** -.35
# Gamma = -2.5, logr = .0 , r = 10 ** .0

# OM_150310_000.hdf5
# beta = .0, logr = -1.0, r = 10 ** -1.0
# beta = .87, logr = .5, r = 10 ** .5
# beta = .07, logr = -.5, r = 10 ** -.5
# beta = .4, logr = .0, r = 10 ** .0
# beta = 1.0, logr = 1.2, r = 10 ** 1.2

# Gamma = -1.5, logr = -.7, r = 10 ** -.7
# Gamma = -2, logr = -.28, r = 10 ** -.28
# Gamma = -2.5, logr = .0, r = 10 ** .0

# HQ10000_G0.8_2_000.hdf5
# Gamma = -1.5, logr = -.65, r = 10 ** -.65
# Gamma = -2, logr = -.35, r = 10 ** -.35
# Gamma = -2.5, logr = -.08, r = 10 ** -.08

# HQ10000_G1.2_9_005.hdf5
# Gamma = -1, logr = -.5, r = 10 ** -.5
# Gamma = -1.5, logr = -.4, r = 10 ** -.4
# Gamma = -2, logr = -.25, r = 10 ** -.25
# Gamma = -2.5, logr = -.15, r = 10 ** -.15
# Gamma = -3, logr = .5, r = 10 ** .5

# Make switches to control figures, print statements, binning etc. -----

Fig3_3D_xyz = 0

Fig8_vspherical_hist_log_vpvn = 0
Fig11_vspherical_hist_log_n123 = 0
calc_sigma_binned_lin_radius = 0
print_sigma = 0
Fig12_n123_sigma = 0
Fig12_x789_sigma = 0

Fig12_vr_vtheta_vphi_sigma = 0
Fig12_vr_vtheta_vphi_vt_sigma = 0

Fig13_vspherical_hist_old = 0
vbin = 0
x14_25_36_same_length = 0
print_vp_vn = 0
print_Vp_Vn = 0
print_x123456 = 0
print_sigma_binned_lin_radius = 0
print_sigma_unbinned = 0
save_r_v_as_txt = 0
Fig14_sigmas = 0


def randrange(n, vmin, vmax):  # 3D scatterplot of positions
    return (vmax - vmin) * np.random.rand(n) + vmin


# sigma_1 = .205
# sigma_2 = .335

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
        v_r_inside_bin_i = v_r[posv_par_inside_bin_i]
        v_t_inside_bin_i = v_t[posv_par_inside_bin_i]

        v_arr.append(v_inside_bin_i)
        v_r_arr.append(v_r_inside_bin_i)
        v_t_arr.append(v_t_inside_bin_i)
        nr_par_inside_bin.append(nr_par_inside_bin_i)

    plt.figure()  # plot structure over velocity bins.
    plt.subplot(121)
    plt.xlabel(r'$v, v_r$ and $v_t$')
    plt.ylabel('Number of particles')
    plt.title(r'VDF (HQ structure, $10^6$ particles)')
    plt.hist(v_arr[15], bins=100, histtype='step', color='red',
             range=(v_limit_min, v_limit_max), label=r'$v$', lw=2)
    plt.hist(v_r_arr[15], bins=100, histtype='step', color='blue',
             range=(v_limit_min, v_limit_max), label=r'$v_r$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.show()
    plt.hist(v_r, bins=100, histtype='step', color='skyblue',
             range=(v_limit_min, v_limit_max), label=r'$v_r$', lw=2)
    plt.hist(v_t, bins=100, histtype='step', color='black',
             range=(-4, 4), label=r'$v_t$', lw=2)

    plt.subplot(122)
    plt.xlabel(r'$\log v$, $ \log v_r$ and $ \log v_t$')
    plt.hist(np.log10(np.absolute(v_arr)), bins=100, histtype='step',
             color='red', range=(-5, 1), label=r'$\log v$', lw=2)
    plt.hist(np.log10(np.absolute(v_r)), bins=100, histtype='step',
             color='skyblue', range=(-5, 1), label=r'$\log v_r$', lw=2)
    plt.hist(np.log10(np.absolute(v_t)), bins=100, histtype='step',
             color='black', range=(-5, 1), label=r'$\log v_t$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

    plt.figure()
    plt.xlabel(r'$v_r$ and $v_t$')
    plt.ylabel('Number of particles')
    plt.title('velocity distributions')
    plt.hist(v_r_arr[5], bins=30, histtype='step',
             color='red', range=(-4, 1), label=r'$v_r$ (bin 5)',
             normed=True, lw=2)
    plt.hist(v_r_arr[8], bins=30, histtype='step',
             color='skyblue', range=(-4, 1), label=r'$v_r$ (bin 8)',
             normed=True, lw=2)
    plt.hist(v_r_arr[10], bins=300, histtype='step',
             color='black', range=(-1, 1), label=r'$v_r$ (bin 10)',
             lw=2)
    plt.hist(.5 * v_t_arr[5], bins=30, histtype='step',
             color='green', range=(-4, 1), label=r'$v_t$ (bin 5)',
             normed=True)
    plt.hist(.5 * v_t_arr[8], bins=30, histtype='step',
             color='blue', range=(-4, 1), label=r'$v_t$ (bin 8)',
             normed=True)
    plt.hist(v_t_arr[10], bins=300, histtype='step',
             color='orange', range=(-1, 1), label=r'$v_t$ (bin 10)')
    plt.hist(.25 * v_t_arr[10], bins=300, histtype='step',
             color='red', range=(-2, 1),
             label=r'$\frac{1}{4}\cdot v_t$ (bin 10)')
    plt.hist(v_t_arr[10] * v_t_arr[10], bins=300, histtype='step',
             color='green', range=(-2, 1),
             label=r'$v_t\cdot v_t$ (bin 10)')
    plt.hist(2 * v_t_arr[10], bins=300, histtype='step',
             color='blue', range=(-2, 1),
             label=r'$2 \cdot v_t$ (bin 10)')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if calc_sigma_binned_lin_radius:
    R_hob_par = R[GoodIDs]
    v2 = vx ** 2 + vy ** 2 + vz ** 2

    (sigma2, sigmarad2, sigmatheta2, sigmaphi2, sigmatan2, sigma,
    sigmarad, sigmatheta, sigmaphi, sigmatan, VR_sigmarad,
    VTheta_sigmatheta, VPhi_sigmaphi, VT_sigmatan, r, Phi, Theta, VR,
    VTheta, VPhi, VT, bin_radius_arr) = ([] for i in range(22))

    binning_arr = np.linspace(R_limit_min, R_limit_max, nr_binning_bins)

    for i in range(nr_binning_bins - 2):
        min_R_bin_i = binning_arr[i]  # start of bin
        max_R_bin_i = binning_arr[i + 1]  # end of bin
        # position of particles inside a radial bin
        posR_par_inside_bin_i = np.where((R_hob_par > min_R_bin_i)
                                         & (R_hob_par < max_R_bin_i))
        nr_par_inside_bin_i = len(posR_par_inside_bin_i[0])
        if nr_par_inside_bin_i == 0:
            continue

        r_i = np.sqrt(x[posR_par_inside_bin_i] ** 2
              + y[posR_par_inside_bin_i] ** 2
              + z[posR_par_inside_bin_i] ** 2)
        Phi_i = scipy.arctan2(y[posR_par_inside_bin_i],
                              x[posR_par_inside_bin_i])
        Theta_i = scipy.arccos(z[posR_par_inside_bin_i] / r_i)
        VR_i = scipy.sin(Theta_i) * scipy.cos(Phi_i)
               * vx[posR_par_inside_bin_i] + scipy.sin(Theta_i)
               * scipy.sin(Phi_i) * vy[posR_par_inside_bin_i]
               + scipy.cos(Theta_i) * vz[posR_par_inside_bin_i]
        VTheta_i = scipy.cos(Theta_i) * scipy.cos(Phi_i)
                   * vx[posR_par_inside_bin_i] + scipy.cos(Theta_i)
                   * scipy.sin(Phi_i) * vy[posR_par_inside_bin_i]
                   - scipy.sin(Theta_i) * vz[posR_par_inside_bin_i]
        VPhi_i = - scipy.sin(Phi_i) * vx[posR_par_inside_bin_i]
                 + scipy.cos(Phi_i) * vy[posR_par_inside_bin_i]

        VT_i = (VTheta_i ** 2 + VPhi_i ** 2) ** .5
        # VT_i = VTheta_i + VPhi_i

        # sigmatan2
        vtan2_inside_bin_i = VT_i ** 2
        sigmatan2_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                                 * np.sum(vtan2_inside_bin_i)
        sigmatan2.append(sigmatan2_inside_bin_i)
        # print(sigmatan2_inside_bin_i, np.std(VT_i) ** 2)
        # print(sigmatan2_inside_bin_i, np.mean(VT_i ** 2),
        #       nr_par_inside_bin_i)

        # sigma2 total
        v2_inside_bin_i = v2[posR_par_inside_bin_i]
        sigma2_inside_bin_i = (1. / (nr_par_inside_bin_i + 1.))
                              * np.sum(v2_inside_bin_i)
        sigma2.append(sigma2_inside_bin_i)
        bin_radius_arr.append((max_R_bin_i + min_R_bin_i) / 2)

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

        sigma_i = (sigma2[i]) ** .5
        sigmarad_i = (sigmarad2[i]) ** .5
        sigmatheta_i = (sigmatheta2[i]) ** .5
        sigmaphi_i = (sigmaphi2[i]) ** .5
        sigmatan_i = (sigmatan2[i]) ** .5

        sigma.append(sigma_i)
        sigmarad.append(sigmarad_i)
        sigmatheta.append(sigmatheta_i)
        sigmaphi.append(sigmaphi_i)
        sigmatan.append(sigmatan_i)

        r.append(r_i)  # save arrays
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

    # print(r'$\sigma_{tan} = $ ', linalg.norm(sigmatan))
    # print(r'$\sigma = $ ', linalg.norm(sigma))
    # print(r'$\sigma_{rad} = $ ', linalg.norm(sigmarad))
    # print(r'$\sigma_{\phi} = $ ', linalg.norm(sigmaphi))
    # print(r'$\sigma_{\theta} = $ ', linalg.norm(sigmatheta))

    # print('np.concatenate(np.array(VT_sigmatan), axis=0) = ',
    #       np.concatenate(np.array(VT_sigmatan), axis=0))
    # print(sigmatan2_inside_bin_i, np.mean(VT_i ** 2))

    # r = np.array(r)
    # Phi = np.array(Phi)
    # Theta = np.array(Theta)
    # VR = np.array(VR)
    # VTheta = np.array(VTheta)
    # VPhi = np.array(VPhi)
    # VT = np.array(VT)

    # print('VR = ', VR)

    r = np.concatenate(np.array(r), axis=0)
    Phi = np.concatenate(np.array(Phi), axis=0)
    Theta = np.concatenate(np.array(Theta), axis=0)
    VR = np.concatenate(np.array(VR), axis=0)
    VTheta = np.concatenate(np.array(VTheta), axis=0)
    VPhi = np.concatenate(np.array(VPhi), axis=0)
    VT = np.concatenate(np.array(VT), axis=0)
    VR_sigmarad = np.concatenate(np.array(VR_sigmarad), axis=0)
    VTheta_sigmatheta = np.concatenate(np.array(VTheta_sigmatheta),
                                       axis=0)
    VPhi_sigmaphi = np.concatenate(np.array(VPhi_sigmaphi), axis=0)
    VT_sigmatan = np.concatenate(np.array(VT_sigmatan), axis=0)

    # np.savetxt('v_sigma_Martin.txt', VT_sigmatan)
    # np.savetxt('vtan_Martin.txt', VT)

if Fig14_sigmas:
    plt.figure()
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

# divide into 6 graphs
(v_rp, v_rn, v_thetap, v_thetan, v_phip,
 v_phin, v_tp, v_tn) = ([] for i in range(8))

if vsphericalold:
    for i in range(len(x)):
        if v_r[i] >= 0.:
            v_rp.append(v_r[i])
        else:
            v_rn.append(v_r[i])
    v_rp_arr = np.asarray(v_rp)
    v_rn_arr = np.asarray(v_rn)
    for i in range(len(x)):
        if v_theta[i] >= 0.:
            v_thetap.append(v_theta[i])
        else:
            v_thetan.append(v_theta[i])
    v_thetap_arr = np.asarray(v_thetap)
    v_thetan_arr = np.asarray(v_thetan)
    for i in range(len(x)):
        if v_phi[i] >= 0.:
            v_phip.append(v_phi[i])
        else:
            v_phin.append(v_phi[i])
    v_phip_arr = np.asarray(v_phip)
    v_phin_arr = np.asarray(v_phin)

if vsphericalnew:
    for i in range(len(VR)):
        if VR[i] >= 0.:
            v_rp.append(VR[i])
        else:
            v_rn.append(VR[i])
    v_rp_arr = np.asarray(v_rp)
    v_rn_arr = np.asarray(v_rn)

    for i in range(len(VTheta)):
        if VTheta[i] >= 0.:
            v_thetap.append(VTheta[i])
        else:
            v_thetan.append(VTheta[i])
    v_thetap_arr = np.asarray(v_thetap)
    v_thetan_arr = np.asarray(v_thetan)

    for i in range(len(VPhi)):
        if VPhi[i] >= 0.:
            v_phip.append(VPhi[i])
        else:
            v_phin.append(VPhi[i])
    v_phip_arr = np.asarray(v_phip)
    v_phin_arr = np.asarray(v_phin)

    for i in range(len(VT)):
        if VT[i] >= 0.:
            v_tp.append(VT[i])
        else:
            v_tn.append(VT[i])
    v_tp_arr = np.asarray(v_tp)
    v_tn_arr = np.asarray(v_tn)

if print_vp_vn:
    print('v_rp_arr = ', v_rp_arr)
    print('v_rp_arr.shape = ', v_rp_arr.shape)
    print('v_rn_arr = ', v_rn_arr)
    print('v_rn_arr.shape = ', v_rn_arr.shape)
    print('v_thetap_arr = ', v_thetap_arr)
    print('v_thetap_arr.shape = ', v_thetap_arr.shape)
    print('v_thetan_arr = ', v_thetan_arr)
    print('v_thetan_arr.shape = ', v_thetan_arr.shape)
    print('v_phip_arr = ', v_phip_arr)
    print('v_phip_arr.shape = ', v_phip_arr.shape)
    print('v_phin_arr = ', v_phin_arr)
    print('v_phin_arr.shape = ', v_phin_arr.shape)
    print('v_tp_arr = ', v_tp_arr)
    print('v_tp_arr.shape = ', v_tp_arr.shape)
    print('v_tn_arr = ', v_tn_arr)
    print('v_tn_arr.shape = ', v_tn_arr.shape)

if Fig8_vspherical_hist_log_vpvn:
    plt.figure()
    plt.xlabel(r'$\log v_rp, \log v_{\theta}p$, $\log v_{\phi}p$,\
               $\log v_rn, \log v_{\theta}n$ and $ \log v_{\phi}n$')
    plt.ylabel('Number of particles')
    plt.title(r'Positive and negative f(v) ($N=%.3f$, $\gamma = %.1f$,\
              File = %s)' % (len(x), Gamma, F))
    plt.hist(np.log10(v_thetap_arr), bins=100, histtype='step',
             color='red', range=(-5, 1), label=r'$\log v_{\theta}p$',
             lw=2)
    plt.hist(np.log10(v_phip_arr), bins=100, histtype='step',
             color='skyblue', range=(-5, 1), label=r'$\log v_{\phi}p$',
             lw=2)
    plt.hist(np.log10(v_rp_arr), bins=100, histtype='step',
             color='black', range=(-5, 1), label=r'$\log v_rp$', lw=2)
    plt.hist(np.log10(np.absolute(v_thetan_arr)), bins=100,
             histtype='step', color='green', range=(-5, 1),
             label=r'$\log v_{\theta}n$', lw=2)
    plt.hist(np.log10(np.absolute(v_phin_arr)), bins=100,
             histtype='step', color='blue', range=(-5, 1),
             label=r'$\log v_{\phi}n$', lw=2)
    plt.hist(np.log10(np.absolute(v_rn_arr)), bins=100, histtype='step',
             color='cyan', range=(-5, 1), label=r'$\log v_rn$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if print_Vp_Vn:
    print('VR_sigmarad_p_arr = ', VR_sigmarad_p_arr)
    print('VR_sigmarad_p_arr.shape = ', VR_sigmarad_p_arr.shape)
    print('VR_sigmarad_n_arr = ', VR_sigmarad_n_arr)
    print('VR_sigmarad_n_arr.shape = ', VR_sigmarad_n_arr.shape)
    print('VTheta_sigmatheta_p_arr = ', VTheta_sigmatheta_p_arr)
    print('VTheta_sigmatheta_p_arr.shape = ', VTheta_sigmatheta_p_arr.shape)
    print('VTheta_sigmatheta_n_arr = ', VTheta_sigmatheta_n_arr)
    print('VTheta_sigmatheta_n_arr.shape = ', VTheta_sigmatheta_n_arr.shape)
    print('VPhi_sigmaphi_p_arr = ', VPhi_sigmaphi_p_arr)
    print('VPhi_sigmaphi_p_arr.shape = ', VPhi_sigmaphi_p_arr.shape)
    print('VPhi_sigmaphi_n_arr = ', VPhi_sigmaphi_n_arr)
    print('VPhi_sigmaphi_n_arr.shape = ', VPhi_sigmaphi_n_arr.shape)
    print('VT_sigmatan_p_arr = ', VT_sigmatan_p_arr)
    print('VT_sigmatan_p_arr.shape = ', VT_sigmatan_p_arr.shape)
    print('VT_sigmatan_n_arr = ', VT_sigmatan_n_arr)
    print('VT_sigmatan_n_arr.shape = ', VT_sigmatan_n_arr.shape)

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

if Fig11_vspherical_hist_log_n123:
    fig = plt.figure()
    ax = fig.add_subplot(121)
    # (mu, sigma) = norm.fit(VR)
    n, bins, patches = plt.hist(VR, 100, histtype='step', color='red',
                                label=r'$ v_r $', alpha=.75)
    # (mu, sigma) = norm.fit(VTheta)
    n, bins, patches = plt.hist(VTheta, 100, histtype='step',
                                color='blue', label=r'$v_{\theta}$',
                                alpha=.75)
    # (mu, sigma) = norm.fit(VPhi)
    n, bins, patches = plt.hist(VPhi, 100, histtype='step',
                                color='green', label=r'$ v_{\phi}$',
                                alpha=.75)
    plt.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\gamma = %.2f$,  File = %s )'
              % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.grid()
    ax.set_yscale('log')

    subplot(122)
    n1 = np.absolute(x4) + x1
    n2 = np.absolute(x5) + x2
    n3 = np.absolute(x6) + x3
    # (mu, sigma) = norm.fit(np.log10(n3))
    n, bins, patches = plt.hist(np.log10(n3), 100, histtype='step',
                                color='red',
                                label=r'$\log (v_rp + |v_rn|)$',
                                alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n1))
    n, bins, patches = plt.hist(np.log10(n1), 100, histtype='step',
                                color='blue',
                                label=r'$\log (v_{\theta}p +\
                                |v_{\theta}n|)$',
                                alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n2))
    n, bins, patches = plt.hist(np.log10(n2), 100, histtype='step',
                                color='green',
                                label=r'$\log (v_{\phi}p +\
                                |v_{\phi}n|)$',
                                alpha=.75)
    plt.xlabel(r'$\log (v_{\theta}p + |v_{\theta}n|)$,\
               $\log (v_{\phi}p + |v_{\phi}n|)$ and $\log\
               (v_rp + |v_rn|)$' )
    plt.ylabel('number of particles')
    plt.title(r'Positive and negative f(v) summed ')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

# All figures with log(v) can instead be plotted as log(v) vs. f(v)/v.
# the idea is, that a flat tail will appear towards small velocities.
# Next I will plot v/sigma along the x-axes instead
# (or maybe with log(v/sigma)).
# Plotting v/sigma makes it easier to compare different radial bins,
# because the x-axis will almost always be the same,
# even though they actually have very different sigma.

if Fig12_n123_sigma:
    # txt = open(Filename.strip('.hdf5') + '_sigma.txt', 'r')
    # print txt.read()
    txt = Filename.strip('.hdf5') + '_sigma.txt'
    TXT = pylab.loadtxt(txt)
    if print_sigma:
        print(r'$\sigma_{tot}^2$, TXT[:, 0] = ', TXT[:, 0])
        print(r'$\sigma_r^2$, TXT[:, 1] = ', TXT[:, 1])
        print(r'$\sigma_{\theta}^2$, TXT[:, 2] = ', TXT[:, 2])
        print(r'$\sigma_{\phi}^2$, TXT[:, 3] = ', TXT[:, 3])

    TXT_tot_arr = np.asarray(TXT[:, 0])
    TXT_r_arr = np.asarray(TXT[:, 1])
    TXT_theta_arr = np.asarray(TXT[:, 2])
    TXT_phi_arr = np.asarray(TXT[:, 3])
    normTXT_tot_arr = np.asarray(TXT[:, 0]) ** .5
    normTXT_r_arr = np.asarray(TXT[:, 1]) ** .5
    normTXT_theta_arr = np.asarray(TXT[:, 2]) ** .5
    normTXT_phi_arr = np.asarray(TXT[:, 3]) ** .5

    plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(n3) / linalg.norm(VR), 100,
                                histtype='step', color='red',
                                label=r'$\frac{f(\log (v_rp +\
                                |v_rn|))}{||v_r||}$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1) / linalg.norm(VTheta), 100,
                                histtype='step', color='blue',
                                label=r'$\frac{f(\log (v_{\theta}p +\
                                |v_{\theta}n|))}{||v_{\theta}||}$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2) / linalg.norm(VPhi), 100,
                                histtype='step', color='green',
                                label=r'$\frac{f(\log (v_{\phi}p +\
                                |v_{\phi}n|))}{||v_{\phi}||}$',
                                alpha=.75)
    plt.xlabel(r'$\frac{\log (v_rp + |v_rn|)}{||v_r||}$, $\frac{\log\
               (v_{\theta}p + |v_{\theta}n|)}{||v_{\theta}||}$ and\
               $\frac{\log (v_{\phi}p + |v_{\phi}n|)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (v_p + |v_n|)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s'
              % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR / linalg.norm(normTXT_r_arr), 100,
                                histtype='step', color='red',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\
                                \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta / linalg.norm(normTXT_theta_arr),
                                100, histtype='step', color='blue',
                                label=r'$f\left(\frac{v_{\theta}}\
                                {\sigma_{\theta}}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VPhi / linalg.norm(normTXT_phi_arr),
                                100, histtype='step', color='green',
                                label=r'$f\left(\frac{v_{\phi}}\
                                {\sigma_{\phi}}\right)$',
                                alpha=.75)
    plt.xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $')
    plt.ylabel(r'$f\left( u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(n3), 100, histtype='step',
                                color='red',
                                label=r'$f(\log (v_rp + |v_rn|))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1), 100, histtype='step',
                                color='blue',
                                label=r'$f(\log (v_{\theta}p +\
                                |v_{\theta}n|))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2), 100, histtype='step',
                                color='green',
                                label=r'$f(\log (v_{\phi}p +\
                                |v_{\phi}n|))$',
                                alpha=.75)
    plt.xlabel(r'$\log (v_rp + |v_rn|)$, $\log (v_{\theta}p +\
               |v_{\theta}n|)$ and $\log (v_{\phi}p + |v_{\phi}n|)$')
    plt.ylabel(r'$f(\log (v_p + |v_n|))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(n3
                                / linalg.norm(normTXT_r_arr)), 100,
                                histtype='step', color='red',
                                label=r'$f\left(\log \left( \frac{v_rp\
                                + |v_rn|}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1
                                / linalg.norm(normTXT_theta_arr)), 100,
                                histtype='step', color='blue',
                                label=r'$f\left(\log \left( \frac{v_{\
                                \theta}p + |v_{\theta}n|}{\sigma_{\
                                \theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2
                                / linalg.norm(normTXT_phi_arr)), 100,
                                histtype='step', color='green',
                                label=r'$f\left(\log \left( \frac{v_{\
                                \phi}p + |v_{\phi}n|}{\sigma_{\phi}}\
                                \right)\right)$',
                                alpha=.75)
    plt.xlabel(r'$\log \left( u_rp + |u_rn| \right)$, $\log \left(\
               u_{\theta}p + |u_{\theta}n| \right)$ and $\log \left(\
               u_{\phi}p + |u_{\phi}n| \right)$')
    plt.ylabel(r'$f\left(\log \left( u_p + |u_n| \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig12_x789_sigma:

    x7 = np.asarray(x1 + list(np.absolute(v_thetan_arr)))
    x8 = np.asarray(x2 + list(np.absolute(v_phin_arr)))
    x9 = np.asarray(x3 + list(np.absolute(v_rn_arr)))
    txt = Filename.strip('.hdf5') + '_sigma.txt'
    TXT = pylab.loadtxt(txt)

    if print_sigma:
        print(r'$\sigma_{tot}^2$, TXT[:, 0] = ', TXT[:, 0])
        print(r'$\sigma_r^2$, TXT[:, 1] = ', TXT[:, 1])
        print(r'$\sigma_{\theta}^2$, TXT[:, 2] = ', TXT[:, 2])
        print(r'$\sigma_{\phi}^2$, TXT[:, 3] = ', TXT[:, 3])

    TXT_tot_arr = np.asarray(TXT[:, 0])
    TXT_r_arr = np.asarray(TXT[:, 1])
    TXT_theta_arr = np.asarray(TXT[:, 2])
    TXT_phi_arr = np.asarray(TXT[:, 3])
    normTXT_tot_arr = np.asarray(TXT[:, 0]) ** .5
    normTXT_r_arr = np.asarray(TXT[:, 1]) ** .5
    normTXT_theta_arr = np.asarray(TXT[:, 2]) ** .5
    normTXT_phi_arr = np.asarray(TXT[:, 3]) ** .5

    plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(x9) / linalg.norm(VR), 100,
                                histtype='step', color='red',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_rn|,\
                                v_rp))}{||v_r||} \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7) / linalg.norm(VTheta), 100,
                                histtype='step', color='blue',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                (|v_{\theta}n|, v_{\theta}p))}\
                                {||v_{\theta}||} \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8) / linalg.norm(VPhi), 100,
                                histtype='step', color='green',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                (|v_{\phi}n|, v_{\phi}p))}\
                                {||v_{\phi}||} \right)$',
                                alpha=.75)
    plt.xlabel(r'$\frac{\log (|v_rn|, v_rp)}{||v_r||}$, $\frac{\log\
               (|v_{\theta}n|, v_{\theta}p)}{||v_{\theta}||}$ and\
               $\frac{\log (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (|v_n|, v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s'
              % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR / linalg.norm(normTXT_r_arr), 100,
                                histtype='step', color='red',
                                label=r'$f\left(\frac{v_r}\
                                {\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta / linalg.norm(normTXT_theta_arr),
                                100, histtype='step', color='blue',
                                label=r'$f\left(\frac{v_{\theta}}\
                                {\sigma_{\theta}}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VPhi / linalg.norm(normTXT_phi_arr),
                                100, histtype='step', color='green',
                                label=r'$f\left(\frac{v_{\phi}}\
                                {\sigma_{\phi}}\right)$',
                                alpha=.75)
    plt.xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $')
    plt.ylabel(r'$f\left( u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(x9), 100, histtype='step',
                                color='red', range=(-3, 0),
                                label=r'$f(\log (|v_rn|,v_rp))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7), 100, histtype='step',
                                color='blue', range=(-3, 0),
                                label=r'$f(\log (|v_{\theta}n|,\
                                v_{\theta}p))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8), 100, histtype='step',
                                color='green', range=(-3, 0),
                                label=r'$f(\log (|v_{\phi}n|,\
                                v_{\phi}p))$',
                                alpha=.75)
    plt.xlabel(r'$\log (|v_rn|, v_rp)$, $\log (|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|, v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|,v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9
                                / linalg.norm(normTXT_r_arr)), 100,
                                histtype='step', color='red',
                                range=(-3, 0),
                                label=r'$f\left(\log \left(\
                                \frac{|v_rn|,v_rp}{\sigma_r}\right)\
                                \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7
                                / linalg.norm(normTXT_theta_arr)), 100,
                                histtype='step', color='blue',
                                range=(-3, 0),
                                label=r'$f\left(\log \left( \frac{\
                                |v_{\theta}n|, v_{\theta}p}{\sigma_{\
                                \theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8
                                / linalg.norm(normTXT_phi_arr)), 100,
                                histtype='step', color='green',
                                range=(-3, 0),
                                label=r'$f\left(\log \left( \frac{\
                                |v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\
                                \right)\right)$',
                                alpha=.75)
    plt.xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
               |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left(\
               |u_{\phi}n|,u_{\phi}p \right)$')
    plt.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig12_vr_vtheta_vphi_sigma:
    v_rpn = np.asarray(list(v_rp_arr) + list(np.absolute(v_rn_arr)))
    v_thetapn = np.asarray(list(v_thetap_arr) + list(np.absolute(v_thetan_arr)))
    v_phipn = np.asarray(list(v_phip_arr) + list(np.absolute(v_phin_arr)))
    x7 = np.asarray(list(VTheta_sigmatheta_p_arr) + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_sigmaphi_p_arr) + list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_sigmarad_p_arr) + list(np.absolute(VR_sigmarad_n_arr)))

    plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(v_rpn) / linalg.norm(VR), 100,
                                histtype='step', color='red',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_rn|,\
                                v_rp)}{||v_r||}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn)
                                / linalg.norm(VTheta), 100,
                                histtype='step', color='blue',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                (|v_{\theta}n|,v_{\theta}p))}\
                                {||v_{\theta}||} \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_phipn) / linalg.norm(VPhi),
                                100, histtype='step', color='green',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                (|v_{\phi}n|,v_{\phi}p))}{||v_{\phi}||}\
                                \right)$',
                                alpha=.75)

    (mu, sigma) = norm.fit(np.log10(v_rpn)/linalg.norm(VR))
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata,popt[0],popt[1])
    plt.plot(xdata, y_fit, '--', lw=3, color='pink',
             label=r'$ \frac{ \log ( v_r )}{|| v_r ||} -fit=\
             a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\frac{\log (|v_rn|,v_rp)}{||v_r||}$, $\frac{\log\
               (|v_{\theta}n|,v_{\theta}p)}{||v_{\theta}||}$\
               and $\frac{\log (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (|v_n|,v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s'
              % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR_sigmarad, 100,
                                histtype='step', color='red',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\
                                \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta_sigmatheta, 100,
                                histtype='step', color='blue',
                                label=r'$f\left(\frac{v_{\theta}}\
                                {\sigma_{\theta}}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VPhi_sigmaphi, 100,
                                histtype='step', color='green',
                                label=r'$f\left(\frac{v_{\phi}}\
                                {\sigma_{\phi}}\right)$',
                                alpha=.75)

    (mu, sigma) = norm.fit(VR_sigmarad)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_2, xdata, ydata)
    y_fit = func_2(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, '--', lw=3, color='pink',
             label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')

    plt.xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $')
    plt.ylabel(r'$f\left( u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(v_rpn), 100, histtype='step',
                                color='red', range=(-3, 0),
                                label=r'$f(\log (|v_rn|,v_rp))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn), 100,
                                histtype='step', color='blue',
                                range=(-3, 0),
                                label=r'$f(\log (|v_{\theta}n|,\
                                v_{\theta}p))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_phipn), 100, histtype='step',
                                color='green', range=(-3, 0),
                                label=r'$f(\log (|v_{\phi}n|,\
                                v_{\phi}p))$',
                                alpha=.75)

    (mu, sigma) = norm.fit(np.log10(v_rpn))
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata,popt[0], popt[1])
    plt.plot(xdata, y_fit, '--', lw=3, color='pink',
             label=r'$\log ( v_r ) -fit= a \cdot log(x)\
             \cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\log (|v_rn|,v_rp)$, $\log (|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|,v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|,v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9), 100, histtype='step',
                                color='red', range=(-3, 1),
                                label=r'$f\left(\log \left( \frac{\
                                |v_rn|, v_rp}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7), 100, histtype='step',
                                color='blue', range=(-3, 1),
                                label=r'$f\left(\log \left( \frac{\
                                |v_{\theta}n|, v_{\theta}p}\
                                {\sigma_{\theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8), 100, histtype='step',
                                color='green', range=(-3, 1),
                                label=r'$f\left(\log \left( \frac{\
                                |v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\
                                \right)\right)$',
                                alpha=.75)

    (mu, sigma) = norm.fit(np.log10(x9))
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, '--', lw=3, color='pink',
             label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit=\
             a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
               |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left(\
               |u_{\phi}n|,u_{\phi}p \right)$')
    plt.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig12_vr_vtheta_vphi_vt_sigma:
    # v_rpn = np.asarray(list(v_rp_arr) + list(np.absolute(v_rn_arr)))
    # v_thetapn = np.asarray(list(v_thetap_arr) + list(np.absolute(v_thetan_arr)))
    # v_phipn = np.asarray(list(v_phip_arr) + list(np.absolute(v_phin_arr)))
    # v_tpn = np.asarray(list(v_tp_arr) + list(np.absolute(v_tn_arr)))
    # x7 = np.asarray(list(VTheta_sigmatheta_p_arr) + list(np.absolute(VTheta_sigmatheta_n_arr)))
    # x8 = np.asarray(list(VPhi_sigmaphi_p_arr) + list(np.absolute(VPhi_sigmaphi_n_arr)))
    # x9 = np.asarray(list(VR_sigmarad_p_arr) + list(np.absolute(VR_sigmarad_n_arr)))
    # x10 = np.asarray(list(VT_sigmatan_p_arr) + list(np.absolute(VT_sigmatan_n_arr)))

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    if keep_IC_R_middle:
        plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s'
                  % (len(VR), Gamma, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='Black',
                                    label=r'$f\left(\frac{v_t}\
                                    {\sigma_t}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_VT_sigmatan_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='red',
                                    label=r'$f\left(\frac{v_r}\
                                    {\sigma_r}\right)$',
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
                                    label=r'$f\left(\frac{v_{\theta}}\
                                    {\sigma_{\theta}}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_VTheta_sigmatheta_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='green',
                                    label=r'$f\left(\frac{v_{\phi}}\
                                    {\sigma_{\phi}}\right)$',
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

        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_tn|,v_tp}{\sigma_t}\
                                    \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_logx10_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_rn|,v_rp}{\sigma_r}\
                                    \right)\right)$',
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
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\theta}n|, v_{\theta}p}\
                                    {\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F + '_logx7_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\phi}n|,v_{\phi}p}\
                                    {\sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F + '_logx8_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left(\
                   |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,\
                   u_{\theta}p \right)$ and $\log \left(\
                   |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
                   u_p \right)\right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

    if new_R_middle:
        plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s , new R_middle'
                  % (len(VR), Gamma, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='Black',
                                    label=r'$f\left(\frac{v_t}\
                                    {\sigma_t}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_VT_sigmatan_gamma_%.2f.txt'
                   % Gamma, x, delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='red',
                                    label=r'$f\left(\frac{v_r}\
                                    {\sigma_r}\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_VR_sigmarad_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,
                                    histtype='step', color='blue',
                                    label=r'$f\left(\frac{v_{\theta}}\
                                    {\sigma_{\theta}}\right)$',
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
                                    label=r'$f\left(\frac{v_{\phi}}\
                                    {\sigma_{\phi}}\right)$',
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

        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='Black', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_tn|,v_tp}{\sigma_t}\
                                    \right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_logx10_gamma_%.2f.txt'
                   % Gamma, x, delimiter=' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='red', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_rn|,v_rp}{\sigma_r}\
                                    \right)\right)$',
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
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\theta}n|, v_{\theta}p}\
                                    {\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_logx7_gamma_%.2f.txt' % Gamma, x,
                   delimiter = ' ',
                   header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='green', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\phi}n|,v_{\phi}p}{\
                                    \sigma_{\phi}}\right)\right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
        x = x.transpose()
        np.savetxt(F + '_new_R_middle_logx8_gamma_%.2f.txt' % Gamma, x,
                   delimiter=' ',
                   header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log\
                   \left( |u_rn|,u_rp \right)$, $\log \left(\
                   |u_{\theta}n|,u_{\theta}p \right)$ and $\log\
                   \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|, u_p\
                   \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

    if large_R_middle:
        plt.title(r'$N=%i$, $R_{middle} = %.2f$, File = %s, new R_middle'
                  % (len(VR), R_middle, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='Black',
                                    label=r'$f\left( u_t \right)$',
                                    alpha=.75)
        xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
        ydata = n
        x = np.array((xdata, ydata))
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
        np.savetxt(F + '_large_R_middle_VTheta_sigmatheta_R_middle_%.2f.txt'
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
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log\
                   \left( |u_rn|,u_rp \right)$, $\log \left(\
                   |u_{\theta}n|,u_{\theta}p \right)$ and\
                    $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p\
                   \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

if Fig13_vspherical_hist_old:
    plt.figure()
    (mu, sigma) = norm.fit(v_t_arr[6]) # best fit of data
    n, bins, patches = plt.hist(v_t_arr[6], 100, normed=1,
                                color='green', alpha=.75)
    # add a 'best fit' line
    # y = mlab.normpdf( bins, mu, sigma)
    # l = plt.plot(bins, y, 'r--', linewidth=2)
    # plt.plot(v_t_arr[10], fit, 'b--', linewidth=2)
    # plot
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_1, xdata, ydata)
    y_fit = func_1(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, '--', lw=3, color='SkyBlue')
    plt.xlabel(r'$v_t$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$'
              % (mu, sigma))
    plt.grid()

    x = np.array((xdata, ydata))
    x = x.transpose()
    print 'x.shape:', x.shape
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFt.txt', x, delimiter = ' ',
        header='    bins                         n')

    plt.figure()
    (mu, sigma) = norm.fit(v_r_arr[6])
    # the histogram of the data
    n, bins, patches = plt.hist(v_r_arr[6], 100, normed=1, color='blue',
                                alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_2, xdata, ydata)
    y_fit = func_2(xdata,popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, '--', lw=3, color='SkyBlue')
    plt.xlabel(r'$v_r$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$'
              % (mu, sigma))
    plt.grid()

    x = np.array((xdata, ydata))
    x = x.transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFr.txt', x,
               delimiter=' ',
               header='    bins                         n')

plt.show()

if save_r_v_as_txt:
    x = np.array((xcl2, ycl2, zcl2, vxnew2, vynew2, vznew2))
    x = x.transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin0_05to0_25kpc_VDF.txt', x,
               delimiter=' ',
               header=' xcl2      ycl2      zcl2      vxnew2      vynew2      vznew2 ')
