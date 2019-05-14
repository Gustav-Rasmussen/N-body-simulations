# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import VDF
# from mpl_toolkits.mplot3d import Axes3D
# import GaussianAndTsallis
# import Gammas_and_R_middles
# import getSnapshotValues
# import vSphericalAnd_vBins

# readline will not be well behaved unless this is installed:
# pip install gnureadline

# Make switches to control figures, print statements, binning etc.

Fig_sigmas = 0
vspherical_sigma = 0
print_Vp_Vn = 0
print_sigma_binned_lin_radius = 0
Fig_vr_vtheta_vphi_vt_sigma = 0
Fig_vr_vtheta_vphi_vt_sigma_bin_avg = 0


def plot_xy(ax, y_plot, Ms, Color, Label):
    """Return plot."""
    return ax.plot(x_plot, y_plot, Ms, ms=8, mew=0, color=Color, label=Label)


if Fig_sigmas:
    x_plot = np.log10(bin_radius_arr)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))

    plot_xy(ax1, np.log10(sigma2), 'r-o', r'$\log \sigma_{total}^2$')
    plot_xy(ax1, np.log10(sigmarad2), 'b--s', r'$\log \sigma_{r}^2$')
    plot_xy(ax1, np.log10(sigmatheta2), 'g--v', r'$\log \sigma_{\theta}^2$')
    plot_xy(ax1, np.log10(sigmaphi2), 'k--^', r'$\log \sigma_{\phi}^2$')
    plot_xy(ax1, np.log10(sigmatan2), 'y--^', r'$\log \sigma_{tan}^2$')

    ax1.set_xlabel(r'$\log $r (kpc)', fontsize=20)
    ax1.set_ylabel(r'$\log \sigma^2$', fontsize=20)
    ax1.set_title(r'Velocity dispersions (File = %s, $\gamma=%.2f$)'
                  % (F, Gamma), fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=3, handlelength=2.5)
    ax1.grid()

    plot_xy(ax2, np.log10(sigma), 'r-o', r'$\log \sigma_{total}$')
    plot_xy(ax2, np.log10(sigmarad), 'b--s', r'$\log \sigma_r$')
    plot_xy(ax2, np.log10(sigmatheta), 'g--v', r'$\log \sigma_{\theta}$')
    plot_xy(ax2, np.log10(sigmaphi), 'k--^', r'$\log \sigma_{\phi}$')
    plot_xy(ax2, np.log10(sigmatan), 'y--^', r'$\log \sigma_{tan}$')

    ax2.set_xlabel(r'$\log $r (kpc)', fontsize=20)
    ax2.set_ylabel(r'$\log \sigma$', fontsize=20)
    ax2.set_legend(prop=dict(size=13), numpoints=2, ncol=2,
                   frameon=True, loc=3, handlelength=2.5)
    ax2.grid()

if vspherical_sigma:
    (VR_sigmaR_p, VR_sigmaR_n, VTheta_sigmatheta_p,
     VTheta_sigmatheta_n, VPhi_sigmaphi_p, VPhi_sigmaphi_n,
     VT_sigmaT_p, VT_sigmaT_n) = ([] for i in range(8))

    for i in range(len(VR_sigmaR)):
        if VR_sigmaR[i] >= 0.:
            VR_sigmaR_p.append(VR_sigmaR[i])
        else:
            VR_sigmaR_n.append(VR_sigmaR[i])
    VR_sigmaR_p_arr = np.asarray(VR_sigmaR_p)
    VR_sigmaR_n_arr = np.asarray(VR_sigmaR_n)
    for i in range(len(VR_sigmaR)):
        if VTheta_sigmatheta[i] >= 0.:
            VTheta_sigmatheta_p.append(VTheta_sigmatheta[i])
        else:
            VTheta_sigmatheta_n.append(VTheta_sigmatheta[i])
    VTheta_sigmatheta_p_arr = np.asarray(VTheta_sigmatheta_p)
    VTheta_sigmatheta_n_arr = np.asarray(VTheta_sigmatheta_n)
    for i in range(len(VR_sigmaR)):
        if VPhi_sigmaphi[i] >= 0.:
            VPhi_sigmaphi_p.append(VPhi_sigmaphi[i])
        else:
            VPhi_sigmaphi_n.append(VPhi_sigmaphi[i])
    VPhi_sigmaphi_p_arr = np.asarray(VPhi_sigmaphi_p)
    VPhi_sigmaphi_n_arr = np.asarray(VPhi_sigmaphi_n)
    for i in range(len(VR_sigmaR)):
        if VT_sigmaT[i] >= 0.:
            VT_sigmaT_p.append(VT_sigmaT[i])
        else:
            VT_sigmaT_n.append(VT_sigmaT[i])
    VT_sigmaT_p_arr = np.asarray(VT_sigmaT_p)
    VT_sigmaT_n_arr = np.asarray(VT_sigmaT_n)

    (VR_i_avg_in_bin_sigmaR_p, VR_i_avg_in_bin_sigmaR_n,
     VT_i_avg_in_bin_sigmaT_p, VT_i_avg_in_bin_sigmaT_n,
     VPhi_i_avg_in_bin_sigmaphi_p, VPhi_i_avg_in_bin_sigmaphi_n,
     VTheta_i_avg_in_bin_sigmatheta_p,
     VTheta_i_avg_in_bin_sigmatheta_n) = ([] for i in range(8))

    for i in range(len(VR_i_avg_in_bin_sigmaR)):
        if VR_i_avg_in_bin_sigmaR[i] >= 0.:
            VR_i_avg_in_bin_sigmaR_p.append(VR_i_avg_in_bin_sigmaR[i])
        else:
            VR_i_avg_in_bin_sigmaR_n.append(VR_i_avg_in_bin_sigmaR[i])
    VR_i_avg_in_bin_sigmaR_p_arr = np.asarray(VR_i_avg_in_bin_sigmaR_p)
    VR_i_avg_in_bin_sigmaR_n_arr = np.asarray(VR_i_avg_in_bin_sigmaR_n)
    for i in range(len(VR_i_avg_in_bin_sigmaR)):
        if VTheta_i_avg_in_bin_sigmatheta[i] >= 0.:
            VTheta_i_avg_in_bin_sigmatheta_p.append(VTheta_i_avg_in_bin_sigmatheta[i])
        else:
            VTheta_i_avg_in_bin_sigmatheta_n.append(VTheta_i_avg_in_bin_sigmatheta[i])
    VTheta_i_avg_in_bin_sigmatheta_p_arr = np.asarray(VTheta_i_avg_in_bin_sigmatheta_p)
    VTheta_i_avg_in_bin_sigmatheta_n_arr = np.asarray(VTheta_i_avg_in_bin_sigmatheta_n)
    for i in range(len(VR_i_avg_in_bin_sigmaR)):
        if VPhi_i_avg_in_bin_sigmaphi[i] >= 0.:
            VPhi_i_avg_in_bin_sigmaphi_p.append(VPhi_i_avg_in_bin_sigmaphi[i])
        else:
            VPhi_i_avg_in_bin_sigmaphi_n.append(VPhi_i_avg_in_bin_sigmaphi[i])
    VPhi_i_avg_in_bin_sigmaphi_p_arr = np.asarray(VPhi_i_avg_in_bin_sigmaphi_p)
    VPhi_i_avg_in_bin_sigmaphi_n_arr = np.asarray(VPhi_i_avg_in_bin_sigmaphi_n)
    for i in range(len(VR_i_avg_in_bin_sigmaR)):
        if VT_i_avg_in_bin_sigmaT[i] >= 0.:
            VT_i_avg_in_bin_sigmaT_p.append(VT_i_avg_in_bin_sigmaT[i])
        else:
            VT_i_avg_in_bin_sigmaT_n.append(VT_i_avg_in_bin_sigmaT[i])
    VT_i_avg_in_bin_sigmaT_p_arr = np.asarray(VT_i_avg_in_bin_sigmaT_p)
    VT_i_avg_in_bin_sigmaT_n_arr = np.asarray(VT_i_avg_in_bin_sigmaT_n)

if print_Vp_Vn:
    VTheta = np.array(VTheta)
    VPhi = np.array(VPhi)
    VR_sigmaR = np.array(VR_sigmaR)
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
              f'VPhi ={VPhi}',
              f'VPhi.shape = {VPhi.shape}',
              f'VR_sigmarad.shape = {(VR / sigmarad).shape}',
              f'VR_sigmarad = {VR / sigmarad}',
              f'np.where(sigmarad == 0) = {np.where(sigmarad == 0)}',
              f'np.where(sigmatheta == 0) = {np.where(sigmatheta == 0)}',
              f'np.where(sigmaphi == 0) = {np.where(sigmaphi == 0)}'
              )

# All figures with log(v) can instead be plotted as log(v) vs. f(v)/v.
# the idea is, that a flat tail will appear towards small velocities.
# Next I will plot v/sigma along the x-axes instead
# (or maybe with log(v/sigma)).
# Plotting v/sigma makes it easier to compare different radial bins,
# because the x-axis will almost always be the same,
# even though they actually have very different sigma.


# def hist_func(data, ax=None, **kwargs):
def hist_func(data, label, color, ax=None, **kwargs):
    # ax = ax or plt.gca()
    n, bins, patches = plt.hist(data, 50, histtype='step', color=color,
                                label=label, alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    # (mu, sigma) = norm.fit(np.log10(x9))
    # popt, pcov = curve_fit(func_1_log, xdata, ydata)
    # y_fit = func_1_log(xdata, popt[0], popt[1])
    # plt.plot(xdata, y_fit, '--', lw=3, color='pink',
    #          label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit=\
    #                a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
    x = np.array((xdata, ydata))
    x = x.transpose()
    return x


def hist_to_txt(x, txtNameSuffix, param=Gamma):
    return np.savetxt(F + txtNameSuffix.format(param), x,
                      delimiter=' ', header='\t bins \t \t \t \t n')


RmiddleStatesLst = ['keep_IC_R_middle', 'new_R_middle', 'large_R_middle']

# Choose Rmiddle
State = RmiddleStatesLst[1]


def getRmiddleState(state):
    RmiddleStates = {'keep_IC_R_middle': '',
                     'new_R_middle': 'new_R_middle',
                     'large_R_middle': 'large_R_middle'}
    return RmiddleStates.get(state, 'That state does not exist!')


if Fig_vr_vtheta_vphi_vt_sigma:
    x7 = np.asarray(list(VTheta_sigmatheta_p_arr)
                    + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_sigmaphi_p_arr)
                    + list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_sigmaR_p_arr)
                    + list(np.absolute(VR_sigmaR_n_arr)))
    x10 = np.asarray(list(VT_sigmaT_p_arr)
                     + list(np.absolute(VT_sigmaT_n_arr)))

    f, (ax1, ax2) = plt.subplots(2)

    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))

    x = hist_func(VT_sigmaT, label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',
                  color='k')
    # print 'x.shape:', x.shape
    hist_to_txt(x, f'{getRmiddleState(State)}_VT_sigmaT_gamma_{}.txt')
    # print 'F + _VT_sigmatan_gamma_%.2f.txt % Gamma = ',
    #        F + '_VT_sigmatan_gamma_%.2f.txt' % Gamma

    x = hist_func(VR_sigmaR, label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                  color='r')
    hist_to_txt(x, f'{getRmiddleState(State)}_VR_sigmaR_gamma_{}.txt')

    x = hist_func(VTheta_sigmatheta, label=r'$f\left(\frac{v_{\theta}}\
                  {\sigma_{\theta}}\right)$', color='b')
    hist_to_txt(x, f'{getRmiddleState(State)}_VTheta_sigmatheta_gamma_{}.txt')

    x = hist_func(VPhi_sigmaphi, label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}\
                  }\right)$', color='g')
    hist_to_txt(x, f'{getRmiddleState(State)}_VPhi_sigmaphi_gamma_{}.txt')

    plt.xlabel(r'$u_t$, $u_r$, $u_{\theta}$ and $u_{\phi}$')
    plt.ylabel(r'$f\left(u \right)$')
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=1, handlelength=2.5)
    plt.grid()

    x = hist_func(np.log10(x10), label=r'$f\left(\log \left(\frac{|v_tn|,\
                  v_tp}{\sigma_t}\right)\right)$', color='k')
    hist_to_txt(x, f'{getRmiddleState(State)}_logx10_gamma_{}.txt')

    x = hist_func(np.log10(x9), label=r'$f\left(\log \left( \frac{|v_rn|,\
                  v_rp}{\sigma_r}\right)\right)$', color='r')
    hist_to_txt(x, f'{getRmiddleState(State)}_logx9_gamma_{}.txt')

    x = hist_func(np.log10(x7), label=r'$f\left(\log \left(\frac{\
                  |v_{\theta}n|, v_{\theta}p}{\sigma_{\theta}}\right)\right)$',
                  color='b')
    hist_to_txt(x, f'{getRmiddleState(State)}_logx7_gamma_{}.txt')

    x = hist_func(np.log10(x8), label=r'$f\left(\log\left(\frac{|v_{\phi}\
                  n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', color='g')
    hist_to_txt(x, f'{getRmiddleState(State)}_logx8_gamma_{}.txt')

    ax2.set_yscale('log')
    # plt.ylim(10 ** -1, 10 ** 3)
    # plt.xlim(-3.5, 0)
    plt.xlabel(r'$\log \left(|u_tn|,u_tp \right)$, $\log \left( |u_rn|,\
               u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p\
               \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
    plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
               u_p \right)\right) \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig_vr_vtheta_vphi_vt_sigma_bin_avg:
    x7 = np.asarray(list(VTheta_i_avg_in_bin_sigmatheta_p_arr)
                    + list(np.absolute(VTheta_i_avg_in_bin_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_i_avg_in_bin_sigmaphi_p_arr)
                    + list(np.absolute(VPhi_i_avg_in_bin_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_i_avg_in_bin_sigmaR_p_arr)
                    + list(np.absolute(VR_i_avg_in_bin_sigmaR_n_arr)))
    x10 = np.asarray(list(VT_i_avg_in_bin_sigmatan_p_arr)
                     + list(np.absolute(VT_i_avg_in_bin_sigmatan_n_arr)))

    f, (ax1, ax2) = plt.subplots(2)

    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s'
              % (len(x), Gamma, F) + ', ' + getRmiddleState(State))

    x = hist_func(VT_i_avg_in_bin_sigmaT,
                  label=r'$f\left(\frac{v_t}{\sigma_t}\right)$', color='k')
    hist_to_txt(x, f'{getRmiddleState(State)}_VT_i_avg_in_bin_sigmaT_gamma_{}.txt')

    x = hist_func(VR_i_avg_in_bin_sigmaR,
                  label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', color='r')
    hist_to_txt(x, f'{getRmiddleState(State)}_VR_i_avg_in_bin_sigmaR_gamma_{}.txt')

    x = hist_func(VTheta_i_avg_in_bin_sigmatheta,
                  label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',
                  color='b')
    hist_to_txt(x, f'{getRmiddleState(State)}_VTheta_i_avg_in_bin_sigmatheta_gamma_{}.txt')

    x = hist_func(VPhi_i_avg_in_bin_sigmaphi,
                  label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',
                  color='g')
    hist_to_txt(x, f'{getRmiddleState(State)}_VPhi_i_avg_in_bin_sigmaphi_gamma_{}.txt')

    plt.xlabel(r'$u_t$, $u_r$, $u_{\theta}$ and $u_{\phi}$')
    plt.ylabel(r'$f\left(u \right)$')
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=1, handlelength=2.5)
    plt.grid()

    x = hist_func(np.log10(x10), label=r'$f\left(\log \left(\frac{\
                  |v_tn|,v_tp}{\sigma_t}\right)\right)$', color='k')
    hist_to_txt(x, f'{getRmiddleState(State)}_avg_logx10_gamma_{}.txt')

    x = hist_func(np.log10(x9),
                  label=r'$f\left(\log\left(\frac{|v_rn|,v_rp}{\sigma_r}\
                        \right)\right)$', color='r')
    hist_to_txt(x, f'{getRmiddleState(State)}_avg_logx9_gamma_{}.txt')

    x = hist_func(np.log10(x7), label=r'$f\left(\log \left(\frac{\
                  |v_{\theta}n|, v_{\theta}p}\
                  {\sigma_{\theta}}\right)\right)$', color='b')
    hist_to_txt(x, f'{getRmiddleState(State)}_avg_logx7_gamma_{}.txt')

    x = hist_func(np.log10(x8), label=r'$f\left(\log \left( \frac{\
                  |v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\
                  \right)$', color='g')
    hist_to_txt(x, f'{getRmiddleState(State)}_avg_logx8_gamma_{}.txt')

    ax2.set_yscale('log')
    plt.xlabel(r'$\log \left(|u_tn|,u_tp \right)$, $\log \left(\
               |u_rn|,u_rp \right)$, $\log \left(|u_{\theta}n|,\
               u_{\theta}p \right)$ and $\log \left(|u_{\phi}n|,\
               u_{\phi}p \right)$')
    plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
               u_p \right)\right) \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

plt.show()
