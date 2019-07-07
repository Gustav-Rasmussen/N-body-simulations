# -*- coding: utf-8 -*-

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
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D
import Gammas_and_R_middles
import os
import getSnapshotValues
import RhoAndGaussianAndTsallis
import velocityCheck
import snapshotFiles
import vSphericalAnd_vBins
import radius_and_velocity_funcs as ravf

# HQ1000000_150311_000.hdf5
# Gamma | logr | r
# -1.5  | -.75 | 10 ** -.75
# -2    | -.35 | 10 ** -.35
# -2.5  | .0   | 10 ** .0

# OM_150310_000.hdf5
# Beta | logr | r
# .0   | -1.0 | 10 ** -1.0
# .87  | .5   | 10 ** .5
# .07  | -.5  | 10 ** -.5
# .4   | .0   | 10 ** .0
# 1.0  | 1.2  | 10 ** 1.2

# Gamma | logr | r
# -1.5  | -.7  | 10 ** -.7
# -2    | -.28 | 10 ** -.28
# -2.5  | .0   | 10 ** .0

# HQ10000_G0.8_2_000.hdf5
# Gamma | logr | r
# -1.5  | -.65 | 10 ** -.65
# -2    | -.35 | 10 ** -.35
# -2.5  | -.08 | 10 ** -.08

# HQ10000_G1.2_9_005.hdf5
# Gamma | logr | r
# -1    | -.5  | 10 ** -.5
# -1.5  | -.4  | 10 ** -.4
# -2    | -.25 | 10 ** -.25
# -2.5  | -.15 | 10 ** -.15
# -3    | .5   | 10 ** .5

# Make switches to control figures, print statements, binning etc.

Fig8_vspherical_hist_log_vpvn = 0
Fig11_vspherical_hist_log_n123 = 0
calc_sigma_binned_lin_radius = 0
print_sigma = 0
Fig12_n123_sigma = 0
Fig12_x789_sigma = 0

Fig12_vr_vtheta_vphi_sigma = 0
Fig12_vr_vtheta_vphi_vt_sigma = 0

Fig13_vspherical_hist_old = 0
x14_25_36_same_length = 0
print_vp_vn = 0
print_Vp_Vn = 0
print_x123456 = 0
print_sigma_binned_lin_radius = 0
print_sigma_unbinned = 0
save_r_v_as_txt = 0
Fig14_sigmas = 0


def randrange(n, vmin, vmax):  # 3D scatterplot of positions
    """."""
    return (vmax - vmin) * np.random.rand(n) + vmin


# sigma_1 = .205
# sigma_2 = .335


def sigma2(num=nr_par_inside_bin_i, v2):
    """num: number of particles. v2: velocity squared"""
    return (1.0 / (num + 1.0)) * np.sum(v2)


def get_xdata(bins):
    """."""
    return bins[0:-1] + (bins[1] - bins[0]) * .5


def hist_data(n, bins):
    """."""
    xdata = get_xdata(bins)
    ydata = n
    x = np.array((xdata, ydata))
    return x.transpose()


def save_txt(title: str):
    """."""
    return np.savetxt(F + title.format(Gamma) + '.txt', x, delimiter=' ',
                      header='\t bins \t\t n')


if calc_sigma_binned_lin_radius:
    R_hob_par = R[GoodIDs]
    v2 = ravf.speed(vx, vy, vz) ** 2

    (sigma2, sigmarad2, sigmatheta2, sigmaphi2, sigmatan2, sigma,
     sigmarad, sigmatheta, sigmaphi, sigmatan, VR_sigmarad,
     VTheta_sigmatheta, VPhi_sigmaphi, VT_sigmatan, r, Phi, Theta, VR,
     VTheta, VPhi, VT, bin_radius_arr) = ([] for i in range(22))

    binning_arr = np.linspace(R_limit_min, R_limit_max, nr_bins)

    for i in range(nr_bins - 2):
        min_R_bin_i = binning_arr[i]  # start of bin
        max_R_bin_i = binning_arr[i + 1]  # end of bin
        # position of particles inside a radial bin
        posR_par_in_bin_i = np.where((R_hob_par > min_R_bin_i)
                                     & (R_hob_par < max_R_bin_i))
        nr_par_in_bin_i = len(posR_par_in_bin_i[0])
        if nr_par_in_bin_i == 0:
            continue

        x = x[posR_par_in_bin_i]
        y = y[posR_par_in_bin_i]
        z = z[posR_par_in_bin_i]
        vx = vx[posR_par_in_bin_i]
        vy = vy[posR_par_in_bin_i]
        vz = vz[posR_par_in_bin_i]

        r_i = ravf.modulus(x, y, z)
        Phi_i = ravf.phi(x, y)
        Theta_i = ravf.theta(r_i, z)
        VR_i = ravf.v_R(vx, vy, vz, Theta_i, Phi_i)
        VTheta_i = ravf.v_theta(vx, vy, vz, Theta, Phi)
        VPhi_i = ravf.v_phi(vx, vy, Phi_i)
        VT_i = ravf.v_tan(VTheta_i, VPhi_i)

        # sigmatan2
        vtan2_in_bin_i = VT_i ** 2
        sigmatan2_in_bin_i = sigma2(vtan2_in_bin_i)
        sigmatan2.append(sigmatan2_in_bin_i)
        # print(sigmatan2_in_bin_i, np.std(VT_i) ** 2)
        # print(sigmatan2_in_bin_i, np.mean(VT_i ** 2), nr_par_in_bin_i)

        # sigma2 total
        v2_in_bin_i = v2[posR_par_in_bin_i]
        sigma2_in_bin_i = sigma2(v2_in_bin_i)
        sigma2.append(sigma2_in_bin_i)
        bin_radius_arr.append((max_R_bin_i + min_R_bin_i) / 2)

        # sigmarad2 radial
        vrad2_in_bin_i = VR_i ** 2
        sigmarad2_in_bin_i = sigma2(vrad2_in_bin_i)
        sigmarad2.append(sigmarad2_in_bin_i)

        # sigmatheta2
        VTheta2_in_bin_i = VTheta_i ** 2
        sigmatheta2_in_bin_i = sigma2(VTheta2_in_bin_i)
        sigmatheta2.append(sigmatheta2_in_bin_i)

        # sigmaphi2
        VPhi2_in_bin_i = VPhi_i ** 2
        sigmaphi2_in_bin_i = sigma2(VPhi2_in_bin_i)
        sigmaphi2.append(sigmaphi2_in_bin_i)

        sigma_i = (sigma2[i]) ** .5
        sigmarad_i = (sigmarad2[i]) ** .5
        sigmatheta_i = (sigmatheta2[i]) ** .5
        sigmaphi_i = (sigmaphi2[i]) ** .5
        sigmatan_i = (sigmatan2[i]) ** .5

        # save arrays
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

    '''
    print(r'$\sigma_{tan} = $', linalg.norm(sigmatan),
          r'$\sigma = $', linalg.norm(sigma),
          r'$\sigma_{rad} = $', linalg.norm(sigmarad),
          r'$\sigma_{\phi} = $', linalg.norm(sigmaphi),
          r'$\sigma_{\theta} = $', linalg.norm(sigmatheta),
          'np.concatenate(np.array(VT_sigmatan), axis=0) = ',
          np.concatenate(np.array(VT_sigmatan), axis=0),
          sigmatan2_inside_bin_i, np.mean(VT_i ** 2),
          'VR = ', VR)
    '''

    r = np.concatenate(np.array(r), axis=0)
    Phi = np.concatenate(np.array(Phi), axis=0)
    Theta = np.concatenate(np.array(Theta), axis=0)
    VR = np.concatenate(np.array(VR), axis=0)
    VTheta = np.concatenate(np.array(VTheta), axis=0)
    VPhi = np.concatenate(np.array(VPhi), axis=0)
    VT = np.concatenate(np.array(VT), axis=0)
    VR_sigmarad = np.concatenate(np.array(VR_sigmarad), axis=0)
    VTheta_sigmatheta = np.concatenate(np.array(VTheta_sigmatheta), axis=0)
    VPhi_sigmaphi = np.concatenate(np.array(VPhi_sigmaphi), axis=0)
    VT_sigmatan = np.concatenate(np.array(VT_sigmatan), axis=0)

    # np.savetxt('v_sigma_Martin.txt', VT_sigmatan)
    # np.savetxt('vtan_Martin.txt', VT)

if Fig14_sigmas:
    plt.figure()
    plt.subplot(121)
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma2)
    plt.plot(x_plot, y_plot, 'r-o', ms=8, mew=0, label=r'$\log\sigma_{total}^2$')
    y_plot = np.log10(sigmarad2)
    plt.plot(x_plot, y_plot, 'b--s', ms=8, mew=0, label=r'$\log \sigma_{r}^2$')
    y_plot = np.log10(sigmatheta2)
    plt.plot(x_plot, y_plot, 'g--v', ms=8, mew=0, label=r'$\log \sigma_{\theta}^2$')
    y_plot = np.log10(sigmaphi2)
    plt.plot(x_plot, y_plot, 'k--^', ms=8, mew=0, label=r'$\log \sigma_{\phi}^2$')
    y_plot = np.log10(sigmatan2)
    plt.plot(x_plot, y_plot, 'c--^', ms=8, mew=0, label=r'$\log \sigma_{tan}^2$')
    plt.xlabel(r'$\log $r (kpc)', fontsize=20)
    plt.ylabel(r'$\log \sigma^2$', fontsize=20)
    plt.title(r'Velocity dispersions (File=%s, $\gamma=%.2f$)' % (F, Gamma), fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=3, handlelength=2.5)
    plt.grid()

    plt.subplot(122)
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma)
    plt.plot(x_plot, y_plot, 'r-o', ms=8, mew=0, label=r'$\log \sigma_{total}$')
    y_plot = np.log10(sigmarad)
    plt.plot(x_plot, y_plot, 'b--s', ms=8, mew=0, label=r'$\log \sigma_r$')
    y_plot = np.log10(sigmatheta)
    plt.plot(x_plot, y_plot, 'g--v', ms=8, mew=0, label=r'$\log \sigma_{\theta}$')
    y_plot = np.log10(sigmaphi)
    plt.plot(x_plot, y_plot, 'k--^', ms=8, mew=0, label=r'$\log \sigma_{\phi}$')
    y_plot = np.log10(sigmatan)
    plt.plot(x_plot, y_plot, 'c--^', ms=8, mew=0, label=r'$\log \sigma_{tan}$')
    plt.xlabel(r'$\log $r (kpc)', fontsize=20)
    plt.ylabel(r'$\log \sigma$', fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=3, handlelength=2.5)
    plt.grid()

# divide into 6 graphs
v_rp, v_rn, v_thetap, v_thetan, v_phip, v_phin, v_tp, v_tn = ([] for i in range(8))

if vsphericalold:
    for i in range(len(x)):
        v_rp.append(v_r[i]) if v_r[i] >= 0. else v_rn.append(v_r[i])
    v_rp_arr = np.asarray(v_rp)
    v_rn_arr = np.asarray(v_rn)
    for i in range(len(x)):
        v_thetap.append(v_theta[i]) if v_theta[i] >= 0. else v_thetan.append(v_theta[i])
    v_thetap_arr = np.asarray(v_thetap)
    v_thetan_arr = np.asarray(v_thetan)
    for i in range(len(x)):
        v_phip.append(v_phi[i]) if v_phi[i] >= 0. else v_phin.append(v_phi[i])
    v_phip_arr = np.asarray(v_phip)
    v_phin_arr = np.asarray(v_phin)

if vsphericalnew:
    for i in range(len(VR)):
        v_rp.append(VR[i]) if VR[i] >= 0. else v_rn.append(VR[i])
    v_rp_arr = np.asarray(v_rp)
    v_rn_arr = np.asarray(v_rn)
    for i in range(len(VTheta)):
        v_thetap.append(VTheta[i]) if VTheta[i] >= 0. else v_thetan.append(VTheta[i])
    v_thetap_arr = np.asarray(v_thetap)
    v_thetan_arr = np.asarray(v_thetan)
    for i in range(len(VPhi)):
        v_phip.append(VPhi[i]) if VPhi[i] >= 0. else v_phin.append(VPhi[i])
    v_phip_arr = np.asarray(v_phip)
    v_phin_arr = np.asarray(v_phin)
    for i in range(len(VT)):
        v_tp.append(VT[i]) if VT[i] >= 0. else v_tn.append(VT[i])
    v_tp_arr = np.asarray(v_tp)
    v_tn_arr = np.asarray(v_tn)

if print_vp_vn:
    print(f'v_rp_arr = {v_rp_arr}',
          f'v_rp_arr.shape = {v_rp_arr.shape}',
          f'v_rn_arr = {v_rn_arr}',
          f'v_rn_arr.shape = {v_rn_arr.shape}',
          f'v_thetap_arr = {v_thetap_arr}',
          f'v_thetap_arr.shape = {v_thetap_arr.shape}',
          f'v_thetan_arr = {v_thetan_arr}',
          f'v_thetan_arr.shape = {v_thetan_arr.shape}',
          f'v_phip_arr = {v_phip_arr}',
          f'v_phip_arr.shape = {v_phip_arr.shape}',
          f'v_phin_arr = {v_phin_arr}',
          f'v_phin_arr.shape = {v_phin_arr.shape}',
          f'v_tp_arr = {v_tp_arr}',
          f'v_tp_arr.shape = {v_tp_arr.shape}',
          f'v_tn_arr = {v_tn_arr}',
          f'v_tn_arr.shape = {v_tn_arr.shape}')

if Fig8_vspherical_hist_log_vpvn:
    plt.figure()
    plt.xlabel(r'$\log v_rp, \log v_{\theta}p$, $\log v_{\phi}p$,\
               $\log v_rn, \log v_{\theta}n$ and $ \log v_{\phi}n$')
    plt.ylabel('Number of particles')
    plt.title(r'Positive and negative f(v) ($N=%.3f$, $\gamma = %.1f$,\
              File = %s)' % (len(x), Gamma, F))
    plt.hist(np.log10(v_thetap_arr), bins=100, histtype='step',
             color='r', range=(-5, 1), label=r'$\log v_{\theta}p$', lw=2)
    plt.hist(np.log10(v_phip_arr), bins=100, histtype='step',
             color='m', range=(-5, 1), label=r'$\log v_{\phi}p$', lw=2)
    plt.hist(np.log10(v_rp_arr), bins=100, histtype='step',
             color='k', range=(-5, 1), label=r'$\log v_rp$', lw=2)
    plt.hist(np.log10(np.absolute(v_thetan_arr)), bins=100, histtype='step',
             color='g', range=(-5, 1), label=r'$\log v_{\theta}n$', lw=2)
    plt.hist(np.log10(np.absolute(v_phin_arr)), bins=100,
             histtype='step', color='b', range=(-5, 1),
             label=r'$\log v_{\phi}n$', lw=2)
    plt.hist(np.log10(np.absolute(v_rn_arr)), bins=100, histtype='step',
             color='c', range=(-5, 1), label=r'$\log v_rn$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if print_Vp_Vn:
    print(f'VR_sigmarad_p_arr = {VR_sigmarad_p_arr}',
          f'VR_sigmarad_p_arr.shape = {VR_sigmarad_p_arr.shape}',
          f'VR_sigmarad_n_arr = {VR_sigmarad_n_arr}',
          f'VR_sigmarad_n_arr.shape = {VR_sigmarad_n_arr.shape}',
          f'VTheta_sigmatheta_p_arr = {VTheta_sigmatheta_p_arr}',
          f'VTheta_sigmatheta_p_arr.shape = {VTheta_sigmatheta_p_arr.shape}',
          f'VTheta_sigmatheta_n_arr = {VTheta_sigmatheta_n_arr}',
          f'VTheta_sigmatheta_n_arr.shape = {VTheta_sigmatheta_n_arr.shape}',
          f'VPhi_sigmaphi_p_arr = {VPhi_sigmaphi_p_arr}',
          f'VPhi_sigmaphi_p_arr.shape = {VPhi_sigmaphi_p_arr.shape}',
          f'VPhi_sigmaphi_n_arr = {VPhi_sigmaphi_n_arr}',
          f'VPhi_sigmaphi_n_arr.shape = {VPhi_sigmaphi_n_arr.shape}',
          f'VT_sigmatan_p_arr = {VT_sigmatan_p_arr}',
          f'VT_sigmatan_p_arr.shape = {VT_sigmatan_p_arr.shape}',
          f'VT_sigmatan_n_arr = {VT_sigmatan_n_arr}',
          f'VT_sigmatan_n_arr.shape = {VT_sigmatan_n_arr.shape}')

    VTheta = np.array(VTheta)
    VPhi = np.array(VPhi)
    VR_sigmarad = np.array(VR_sigmarad)
    VTheta_sigmatheta = np.array(VTheta_sigmatheta)
    VPhi_sigmaphi = np.array(VPhi_sigmaphi)

    if print_sigma_binned_lin_radius:
        print(f'sigmarad2 = {sigmarad2}',
              f'sigmarad2.shape = {sigmarad2.shape}',
              f'sigmatheta2 = {sigmatheta2}',
              f'sigmatheta2.shape = {sigmatheta2.shape}',
              f'sigmaphi2 = {sigmaphi2}',
              f'sigmaphi2.shape = {sigmaphi2.shape}',
              f'sigmarad = {sigmarad}',
              f'sigmarad.shape = {sigmarad.shape}',
              f'sigmatheta = {sigmatheta}',
              f'sigmatheta.shape = {sigmatheta.shape}',
              f'sigmaphi = {sigmaphi}',
              f'sigmaphi.shape = {sigmaphi.shape}',
              f'VR = {VR}',
              f'VR.shape = {VR.shape}',
              f'VTheta = {VTheta}',
              f'VTheta.shape = {VTheta.shape}',
              f'VPhi = {VPhi}',
              f'VPhi.shape = {VPhi.shape}',
              f'VR_sigmarad.shape = {(VR / sigmarad).shape}',
              f'VR_sigmarad = {VR / sigmarad}',
              f'np.where(sigmarad == 0) = {np.where(sigmarad == 0)}',
              f'np.where(sigmatheta == 0) = {np.where(sigmatheta == 0)}',
              f'np.where(sigmaphi == 0) = {np.where(sigmaphi == 0)}')

if Fig11_vspherical_hist_log_n123:
    fig = plt.figure()
    ax = fig.add_subplot(121)
    # (mu, sigma) = norm.fit(VR)
    n, bins, patches = plt.hist(VR, 100, histtype='step', color='r',
                                label=r'$v_r$', alpha=.75)
    # (mu, sigma) = norm.fit(VTheta)
    n, bins, patches = plt.hist(VTheta, 100, histtype='step',
                                color='b', label=r'$v_{\theta}$', alpha=.75)
    # (mu, sigma) = norm.fit(VPhi)
    n, bins, patches = plt.hist(VPhi, 100, histtype='step',
                                color='g', label=r'$v_{\phi}$', alpha=.75)
    plt.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\gamma=%.2f$,  File=%s)' % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.grid()
    ax.set_yscale('log')

    subplot(122)
    n1 = np.absolute(x4) + x1
    n2 = np.absolute(x5) + x2
    n3 = np.absolute(x6) + x3
    # (mu, sigma) = norm.fit(np.log10(n3))
    n, bins, patches = plt.hist(np.log10(n3), 100, histtype='step', color='r',
                                label=r'$\log (v_rp + |v_rn|)$', alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n1))
    n, bins, patches = plt.hist(np.log10(n1), 100, histtype='step', color='b',
                                label=r'$\log (v_{\theta}p + |v_{\theta}n|)$',
                                alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n2))
    n, bins, patches = plt.hist(np.log10(n2), 100, histtype='step', color='g',
                                label=r'$\log (v_{\phi}p + |v_{\phi}n|)$',
                                alpha=.75)
    plt.xlabel(r'$\log (v_{\theta}p + |v_{\theta}n|)$, $\log (v_{\phi}p +\
               |v_{\phi}n|)$ and $\log (v_rp + |v_rn|)$')
    plt.ylabel('number of particles')
    plt.title(r'Positive and negative f(v) summed')
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
        print(r'$\sigma_{tot}^2$, TXT[:, 0] = ', TXT[:, 0],
              r'$\sigma_r^2$, TXT[:, 1] = ', TXT[:, 1],
              r'$\sigma_{\theta}^2$, TXT[:, 2] = ', TXT[:, 2],
              r'$\sigma_{\phi}^2$, TXT[:, 3] = ', TXT[:, 3])

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
                                histtype='step', color='r', label=r'$\frac{f(\
                                \log (v_rp + |v_rn|))}{||v_r||}$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1) / linalg.norm(VTheta), 100,
                                histtype='step', color='b', label=r'$\frac{f(\
                                \log (v_{\theta}p + |v_{\theta}n|))}{\
                                ||v_{\theta}||}$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2) / linalg.norm(VPhi), 100,
                                histtype='step', color='g', label=r'$\frac{f(\
                                \log (v_{\phi}p + |v_{\phi}n|))}\
                                {||v_{\phi}||}$', alpha=.75)
    plt.xlabel(r'$\frac{\log (v_rp + |v_rn|)}{||v_r||}$, $\frac{\log\
               (v_{\theta}p + |v_{\theta}n|)}{||v_{\theta}||}$ and\
               $\frac{\log (v_{\phi}p + |v_{\phi}n|)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (v_p + |v_n|)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR / linalg.norm(normTXT_r_arr), 100,
                                histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta / linalg.norm(normTXT_theta_arr),
                                100, histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                {\sigma_{\theta}}\right)$', alpha=.75)
    n, bins, patches = plt.hist(VPhi / linalg.norm(normTXT_phi_arr),
                                100, histtype='step', color='g',
                                label=r'$f\left(\frac{v_{\phi}}\
                                {\sigma_{\phi}}\right)$', alpha=.75)
    plt.xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$')
    plt.ylabel(r'$f\left(u\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(n3), 100, histtype='step', color='r',
                                label=r'$f(\log(v_rp + |v_rn|))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1), 100, histtype='step', color='b',
                                label=r'$f(\log(v_{\theta}p +\
                                |v_{\theta}n|))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2), 100, histtype='step', color='g',
                                label=r'$f(\log(v_{\phi}p +\
                                |v_{\phi}n|))$', alpha=.75)
    plt.xlabel(r'$\log (v_rp + |v_rn|)$, $\log (v_{\theta}p +\
               |v_{\theta}n|)$ and $\log (v_{\phi}p + |v_{\phi}n|)$')
    plt.ylabel(r'$f(\log (v_p + |v_n|))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(n3 / linalg.norm(normTXT_r_arr)), 100,
                                histtype='step', color='r',
                                label=r'$f\left(\log \left( \frac{v_rp\
                                + |v_rn|}{\sigma_r}\right)\right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1 / linalg.norm(normTXT_theta_arr)),
                                100, histtype='step', color='b',
                                label=r'$f\left(\log \left( \frac{v_{\
                                \theta}p + |v_{\theta}n|}{\sigma_{\
                                \theta}}\right)\right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2
                                / linalg.norm(normTXT_phi_arr)), 100,
                                histtype='step', color='g',
                                label=r'$f\left(\log \left( \frac{v_{\
                                \phi}p + |v_{\phi}n|}{\sigma_{\phi}}\
                                \right)\right)$', alpha=.75)
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
        print(r'$\sigma_{tot}^2$, TXT[:, 0] = ', TXT[:, 0],
              r'$\sigma_r^2$, TXT[:, 1] = ', TXT[:, 1],
              r'$\sigma_{\theta}^2$, TXT[:, 2] = ', TXT[:, 2],
              r'$\sigma_{\phi}^2$, TXT[:, 3] = ', TXT[:, 3])

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
                                histtype='step', color='r', range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_rn|,\
                                v_rp))}{||v_r||} \right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7) / linalg.norm(VTheta), 100,
                                histtype='step', color='b', range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                (|v_{\theta}n|, v_{\theta}p))}\
                                {||v_{\theta}||} \right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8) / linalg.norm(VPhi), 100,
                                histtype='step', color='g', range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                (|v_{\phi}n|, v_{\phi}p))}\
                                {||v_{\phi}||} \right)$', alpha=.75)
    plt.xlabel(r'$\frac{\log (|v_rn|, v_rp)}{||v_r||}$, $\frac{\log\
               (|v_{\theta}n|, v_{\theta}p)}{||v_{\theta}||}$ and\
               $\frac{\log (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (|v_n|, v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR / linalg.norm(normTXT_r_arr), 100,
                                histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta / linalg.norm(normTXT_theta_arr),
                                100, histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                {\sigma_{\theta}}\right)$', alpha=.75)
    n, bins, patches = plt.hist(VPhi / linalg.norm(normTXT_phi_arr),
                                100, histtype='step', color='g',
                                label=r'$f\left(\frac{v_{\phi}}\
                                {\sigma_{\phi}}\right)$', alpha=.75)
    plt.xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$')
    plt.ylabel(r'$f\left(u\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(x9), 100, histtype='step',
                                color='r', range=(-3, 0),
                                label=r'$f(\log (|v_rn|,v_rp))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7), 100, histtype='step', color='b',
                                range=(-3, 0), label=r'$f(\log (|v_{\theta}n|,\
                                v_{\theta}p))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8), 100, histtype='step', color='g',
                                range=(-3, 0), label=r'$f(\log (|v_{\phi}n|,\
                                v_{\phi}p))$', alpha=.75)
    plt.xlabel(r'$\log (|v_rn|, v_rp)$, $\log (|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|, v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|,v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9 / linalg.norm(normTXT_r_arr)), 100,
                                histtype='step', color='r', range=(-3, 0),
                                label=r'$f\left(\log \left(\
                                \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7 / linalg.norm(normTXT_theta_arr)),
                                100, histtype='step', color='b', range=(-3, 0),
                                label=r'$f\left(\log \left( \frac{\
                                |v_{\theta}n|, v_{\theta}p}{\sigma_{\
                                \theta}}\right)\right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8 / linalg.norm(normTXT_phi_arr)),
                                100, histtype='step', color='g', range=(-3, 0),
                                label=r'$f\left(\log \left( \frac{\
                                |v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\
                                \right)\right)$', alpha=.75)
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
    x7 = np.asarray(list(VTheta_sigmatheta_p_arr) +
                    list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_sigmaphi_p_arr) +
                    list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_sigmarad_p_arr) +
                    list(np.absolute(VR_sigmarad_n_arr)))

    plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(v_rpn) / linalg.norm(VR), 100,
                                histtype='step', color='r', range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_rn|,\
                                v_rp)}{||v_r||}\right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn)
                                / linalg.norm(VTheta), 100,
                                histtype='step', color='b', range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                (|v_{\theta}n|,v_{\theta}p))}\
                                {||v_{\theta}||} \right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_phipn) / linalg.norm(VPhi),
                                100, histtype='step', color='g',
                                range=(-.1, .0), label=r'$f\left(\frac{\log\
                                (|v_{\phi}n|,v_{\phi}p))}{||v_{\phi}||}\
                                \right)$', alpha=.75)

    (mu, sigma) = norm.fit(np.log10(v_rpn) / linalg.norm(VR))
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, 'k--', lw=3, label=r'$\frac{\log(v_r)}{||v_r||}-fit\
             =a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\frac{\log (|v_rn|,v_rp)}{||v_r||}$, $\frac{\log\
               (|v_{\theta}n|,v_{\theta}p)}{||v_{\theta}||}$\
               and $\frac{\log (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (|v_n|,v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma=%.2f$, File=%s' % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR_sigmarad, 100, histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta_sigmatheta, 100, histtype='step',
                                color='b', label=r'$f\left(\frac{v_{\theta}}\
                                {\sigma_{\theta}}\right)$', alpha=.75)
    n, bins, patches = plt.hist(VPhi_sigmaphi, 100, histtype='step', color='g',
                                label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\
                                \right)$', alpha=.75)

    (mu, sigma) = norm.fit(VR_sigmarad)
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func_2, xdata, ydata)
    y_fit = func_2(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, 'k--', lw=3,
             label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')

    plt.xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$')
    plt.ylabel(r'$f\left(u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1, frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(v_rpn), 100, histtype='step',
                                color='r', range=(-3, 0),
                                label=r'$f(\log(|v_rn|,v_rp))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn), 100, histtype='step',
                                color='b', range=(-3, 0),
                                label=r'$f(\log(|v_{\theta}n|, v_{\theta}p))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_phipn), 100, histtype='step',
                                color='g', range=(-3, 0),
                                label=r'$f(\log(|v_{\phi}n|, v_{\phi}p))$',
                                alpha=.75)

    (mu, sigma) = norm.fit(np.log10(v_rpn))
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, 'k--', lw=3, label=r'$\log(v_r)-fit=a \cdot\
             log(x)\cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\log (|v_rn|,v_rp)$, $\log (|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|,v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|,v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9), 100, histtype='step', color='r',
                                range=(-3, 1), label=r'$f\left(\log\left(\
                                \frac{|v_rn|, v_rp}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7), 100, histtype='step', color='b',
                                range=(-3, 1), label=r'$f\left(\log\left(\
                                \frac{|v_{\theta}n|, v_{\theta}p}\
                                {\sigma_{\theta}}\right)\right)$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8), 100, histtype='step', color='g',
                                range=(-3, 1), label=r'$f\left(\log\left(\
                                \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\
                                \right)\right)$', alpha=.75)

    (mu, sigma) = norm.fit(np.log10(x9))
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, 'k--', lw=3, label=r'$\log\left(\frac{v_r}\
             {\sigma_r}\right)-fit=a\cdot log(x)\cdot e^{-b\cdot log(x)^2}$')

    plt.xlabel(r'$\log \left(|u_rn|,u_rp \right)$, $\log \left(\
               |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left(\
               |u_{\phi}n|,u_{\phi}p \right)$')
    plt.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig12_vr_vtheta_vphi_vt_sigma:
    # v_rpn = np.asarray(list(v_rp_arr) + list(np.absolute(v_rn_arr)))
    # v_thetapn = np.asarray(list(v_thetap_arr) +
    #                        list(np.absolute(v_thetan_arr)))
    # v_phipn = np.asarray(list(v_phip_arr) + list(np.absolute(v_phin_arr)))
    # v_tpn = np.asarray(list(v_tp_arr) + list(np.absolute(v_tn_arr)))
    # x7 = np.asarray(list(VTheta_sigmatheta_p_arr) +
    #                 list(np.absolute(VTheta_sigmatheta_n_arr)))
    # x8 = np.asarray(list(VPhi_sigmaphi_p_arr) +
    #                 list(np.absolute(VPhi_sigmaphi_n_arr)))
    # x9 = np.asarray(list(VR_sigmarad_p_arr) +
    #                 list(np.absolute(VR_sigmarad_n_arr)))
    # x10 = np.asarray(list(VT_sigmatan_p_arr) +
    #                  list(np.absolute(VT_sigmatan_n_arr)))

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    if keep_IC_R_middle:
        plt.title(r'$N=%i$, $\gamma=%.2f$, File=%s' % (len(VR), Gamma, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='k', label=r'$f\left(\frac{v_t}\
                                    {\sigma_t}\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_VT_sigmatan_gamma_{}')

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='r', label=r'$f\left(\frac{v_r}\
                                    {\sigma_r}\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_VR_sigmarad_gamma_{}')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50, histtype='step',
                                    color='b', label=r'$f\left(\frac{v_{\
                                    \theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        x = hist_data(n, bins)
        save_txt('_VTheta_sigmatheta_gamma_{}')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='g', label=r'$f\left(\frac{v_{\phi}}\
                                    {\sigma_{\phi}}\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_VPhi_sigmaphi_gamma_{}')

        plt.xlabel(r'$u_t$, $u_r$, $u_{\theta}$ and $u_{\phi}$')
        plt.ylabel(r'$f\left(u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='k', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_tn|,v_tp}{\sigma_t}\
                                    \right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_logx10_gamma_{}')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='r', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_rn|,v_rp}{\sigma_r}\
                                    \right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_logx9_gamma_{}')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='b', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\theta}n|, v_{\theta}p}\
                                    {\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        x = hist_data(n, bins)
        save_txt('_logx7_gamma_{}')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='g', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\phi}n|,v_{\phi}p}\
                                    {\sigma_{\phi}}\right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_logx8_gamma_{}')

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
        plt.title(r'$N=%i$, $\gamma=%.2f$, File=%s, new R_middle'
                  % (len(VR), Gamma, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step',
                                    color='k', label=r'$f\left(\frac{v_t}\
                                    {\sigma_t}\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_VT_sigmatan_gamma_{}')

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step',
                                    color='r', label=r'$f\left(\frac{v_r}\
                                    {\sigma_r}\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_VR_sigmarad_gamma_{}')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50, histtype='step',
                                    color='b', label=r'$f\left(\frac{v_{\
                                    \theta}}{\sigma_{\theta}}\right)$',
                                    alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_VTheta_sigmatheta_gamma_{}')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step',
                                    color='g', label=r'$f\left(\frac{v_{\phi}}\
                                    {\sigma_{\phi}}\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_VPhi_sigmaphi_gamma_{}')

        plt.xlabel(r'$u_t$, $u_r$, $u_{\theta}$ and $u_{\phi}$')
        plt.ylabel(r'$f\left(u\right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='k', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_tn|,v_tp}{\sigma_t}\
                                    \right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_logx10_gamma_{}')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='r', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_rn|,v_rp}{\sigma_r}\
                                    \right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_logx9_gamma_{}')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='b', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\theta}n|, v_{\theta}p}\
                                    {\sigma_{\theta}}\right)\right)$',
                                    alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_logx7_gamma_{}')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='g', range=(-3, 1),
                                    label=r'$f\left(\log \left(\
                                    \frac{|v_{\phi}n|,v_{\phi}p}{\
                                    \sigma_{\phi}}\right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_new_R_middle_logx8_gamma_{}')

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

        n, bins, patches = plt.hist(VT_sigmatan, 50, histtype='step', color='k',
                                    label=r'$f\left(u_t\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_VT_sigmatan_R_middle_{}')

        n, bins, patches = plt.hist(VR_sigmarad, 50, histtype='step', color='r',
                                    label=r'$f\left( u_r \right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_VR_sigmarad_R_middle_{}')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50, histtype='step',
                                    color='b', label=r'$f\left(u_{\theta}\
                                    \right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_VTheta_sigmatheta_R_middle_{}')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50, histtype='step', color='g',
                                    label=r'$f\left(u_{\phi}\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_VPhi_sigmaphi_R_middle_{}')

        plt.xlabel(r'$u_t$, $u_r$, $u_{\theta}$ and $u_{\phi}$')
        plt.ylabel(r'$f\left(u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=1, handlelength=2.5)
        plt.grid()

        n, bins, patches = plt.hist(np.log10(x10), 50, histtype='step',
                                    color='k', range=(-3, 1),
                                    label=r'$f\left(\log \left( |u_tn|,\
                                    u_tp \right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_logx10_R_middle_{}')

        n, bins, patches = plt.hist(np.log10(x9), 50, histtype='step',
                                    color='r', range=(-3, 1),
                                    label=r'$f\left(\log\left(|u_rn|,\
                                    u_rp\right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_logx9_R_middle_{}')

        n, bins, patches = plt.hist(np.log10(x7), 50, histtype='step',
                                    color='b', range=(-3, 1),
                                    label=r'$f\left(\log \left(|u_{\theta}n|,\
                                    u_{\theta}p\right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_logx7_R_middle_{}')

        n, bins, patches = plt.hist(np.log10(x8), 50, histtype='step',
                                    color='g', range=(-3, 1),
                                    label=r'$f\left(\log\left(|u_{\phi}n|,\
                                    u_{\phi}p\right)\right)$', alpha=.75)
        x = hist_data(n, bins)
        save_txt('_large_R_middle_logx8_R_middle_{}')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log\left(|u_tn|,u_tp \right)$, $\log\left(|u_rn|,u_rp\
                   \right)$, $\log\left(|u_{\theta}n|,u_{\theta}p\right)$ and\
                    $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p\
                   \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=2, handlelength=2.5)
        plt.grid()

if Fig13_vspherical_hist_old:
    plt.figure()
    (mu, sigma) = norm.fit(v_t_arr[6])  # best fit of data
    n, bins, patches = plt.hist(v_t_arr[6], 100, normed=1, color='g', alpha=.75)
    # add a 'best fit' line
    # y = mlab.normpdf( bins, mu, sigma)
    # l = plt.plot(bins, y, 'r--', linewidth=2)
    # plt.plot(v_t_arr[10], fit, 'b--', linewidth=2)
    # plot
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func_1, xdata, ydata)
    y_fit = func_1(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, 'r--', lw=3)
    plt.xlabel(r'$v_t$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    plt.grid()

    x = np.array((xdata, ydata)).transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFt.txt', x, delimiter=' ',
               header='\t bins \t\t n')

    plt.figure()
    (mu, sigma) = norm.fit(v_r_arr[6])
    # the histogram of the data
    n, bins, patches = plt.hist(v_r_arr[6], 100, normed=1, color='b', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func_2, xdata, ydata)
    y_fit = func_2(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, 'r--', lw=3)
    plt.xlabel(r'$v_r$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    plt.grid()

    x = np.array((xdata, ydata)).transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFr.txt', x, delimiter=' ',
               header='\t bins \t\t n')

plt.show()

if save_r_v_as_txt:
    x = np.array((xcl2, ycl2, zcl2, vxnew2, vynew2, vznew2))
    x = x.transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin0_05to0_25kpc_VDF.txt', x, delimiter=' ',
               header=' xcl2 \t ycl2 \t zcl2 \t vxnew2 \t vynew2 \t vznew2')
