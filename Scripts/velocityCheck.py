# -*- coding: utf-8 -*-

from __future__ import division
import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
import pylab
from scipy.stats import norm
import matplotlib.mlab as mlab
import scipy as sp
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import os
import Gammas_and_R_middles
import getSnapshotValues
import radius_and_velocity_funcs as ravf

User_path = os.getcwd()
Desktop_path = User_path + '/Desktop/'
GADGET_G_path = Desktop_path + 'RunGadget/G_perturbations/'
Stable_path = 'G_perturbations/Stable_structures/'
figure_path = Desktop_path + Stable_path + 'figures/'
text_files_path = Desktop_path + Stable_path + 'text_files/'
Martin_path = 'Martin_IC_and_Final_Edd_and_OM/'
hdf5_path = Desktop_path + 'G_perturbations/hdf5_files/'
nosync_path = User_path + 'nosync/RunGadget/'
test_path = 'G_HQ_1000000_test/output/'

Filename = GADGET_G_path + test_path + 'HQ10000_G1.0_0_000.hdf5'
SnapshotFile = h5py.File(Filename, 'r')
F = 'test' + Filename[len(GADGET_G_path + test_path):-5]

def switch_R_middle_depending_on_Gamma(Gamma):
    return {
        -1.5: lambda: 10 ** -.70,
        -2.0: lambda: 10 ** -.25,
        -2.5: lambda: 1.,
        -3.: lambda: 10 ** -.30
    }.get(Gamma, lambda: None)()


# print(switch_R_middle_depending_on_Gamma(Gamma))

if IC_R_middle:
    R_middle = switch_R_middle_depending_on_Gamma(Gamma)

# Make switches to control figures, print statements, binning etc.
Fig4_vspherical_hist_old = 0
Fig5_vspherical_hist_logfail_new = 0
Fig6_v_hist_logfail = 0
Fig7_vspherical_hist_logfail_old = 0
Fig8_vspherical_hist_log_vpvn = 0
Fig9_VPhiminus = 0
Fig10_concatenate_x789 = 0
Fig11_vspherical_hist_log_n123 = 0
calc_sigma_binned_lin_radius = 0
print_sigma = 0
Fig12_n123_sigma = 0
Fig12_x789_sigma = 0
Fig12_vr_vtheta_vphi_sigma = 0
Fig12_vr_vtheta_vphi_vt_sigma = 0
Fig13_vspherical_hist_old = 0
velocitycheck = 0
vsphericalold = 0
vsphericalnew = 0
vsphericalnew_sigma = 0
plotvelocitycheckold = 0
plotvelocitychecknew = 0

x14_25_36_same_length = 0
print_vp_vn = 0
print_Vp_Vn = 0
print_x123456 = 0
print_sigma_binned_lin_radius = 0
print_sigma_unbinned = 0
save_r_v_as_txt = 0
Fig14_sigmas = 0

if velocitycheck:  # Use 3 simple particles to check vr and vtheta
    x[0], y[0], z[0] = 0., 0., 1.
    vx[0], vy[0], vz[0] = 1., 1., 0.

    x[1], y[1], z[1] = 0., 1., 0.
    vx[1], vy[1], vz[1] = 1., 0., 0.

    x[2], y[2], z[2] = 1., 0., 0.
    vx[2], vy[2], vz[2] = 1., 0., 0.

if vsphericalnew:  # radial and tangential velocities
    ravf.spherical_coords_and_velocities()


if velocitycheck:  # Use 3 simple particles to check vr and vtheta (continued)
    print(f'VR[0] = {VR[0]} \n'  # .0
          f'VTheta[0] = {VTheta[0]} \n'  # 1.0
          f'VPhi[0] = {VPhi[0]} \n'  # 1.0
          f'VR[1] = {VR[1]} \n'  # -4.37114e-08
          f'VTheta[1] = {VTheta[1]} \n'  # 1.91069e-15
          f'VPhi[1] = {VPhi[1]} \n'  # -1.0
          f'VR[2] = {VR[2]} \n'  # 1.0
          f'VTheta[2] = {VTheta[2]} \n'  # -4.37114e-08
          f'VPhi[2] = {VPhi[2]} \n')  # 0.0

if vsphericalold:
    Rvector, vvector = np.array([x, y, z]), np.array([vx, vy, vz])
    v_r, v_t = zeros([len(x), 1]), zeros([len(x), 3])
    print(f'Rvector.shape = {Rvector.shape} \n'
          f'vvector.shape = {vvector.shape}')
    for i in range(len(x)):
        v_r[i] = np.divide(np.dot(Rvector[:, i], vvector[:, i]),
                           linalg.norm(Rvector[:, i]))
        v_t[i] = np.divide(np.cross(Rvector[:, i], vvector[:, i], axis=0),
                           linalg.norm(Rvector[:, i]))

    print(f'v_r = {v_r} \n'
          f'v_r.shape = {v_r.shape} \n'
          f'v_t = {v_t} \n'
          f'v_t.shape = {v_t.shape} \n')

    v = ravf.speed(vx, vy, vz)

    # v_theta and v_phi -------------------------------------------------------
    v_theta, v_phi = zeros([len(x), 1]), zeros([len(x), 1])
    for i in range(len(x)):
        if (x[i] ** 2 + y[i] ** 2 > 0.):
            v_theta[i] = (x[i] * vy[i] - y[i] * vx[i]) \
                        / (x[i] ** 2 + y[i] ** 2)
    for i in range(len(x)):
        if ((x[i] ** 2 + y[i] ** 2 + z[i] ** 2) ** .5 > 0.) * (z[i]
           != (x[i] ** 2 + y[i] ** 2 + z[i] ** 2) ** .5):
            v_phi[i] = ((x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
                        ** .5 * vz[i] - z[i] * v_r[i])\
                        / ((x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
                            * (1 - (z[i] / ((x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
                                            ** .5)) ** 2) ** .5)

        #  v_phi[i] = (z[i] * (x[i] * vx[i] + y[i] * vy[i])
        #             - (x[i] ** 2 + y[i] ** 2) * vz[i])\
        #             / ((x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
        #             * (x[i] ** 2 + y[i] ** 2) ** .5)
        #  v_theta[i] = np.dot()
        #  v_phi[i] = np.cross()

    print(f'v_r[0] = {v_r[0]}'  # [0.]
          f'v_theta[0] = {v_theta[0]}'  # [0.]
          f'v_phi[0] = {v_phi[0]}')  # [0.]

if plotvelocitycheckold:  # Check old velocities are correct
    y1 = v_theta ** 2 + v_phi ** 2  # v_t^2
    y2 = v ** 2 - v_r ** 2  # v_t^2
    figure()
    plt.plot(y1, y2, 'o', ms=1.)
    plt.xlabel(r'$ v_{\theta}^2 + v_{\phi}^2 $')
    plt.ylabel(r'$  v^2 - v_r^2$')
    plt.title(r'check if $ v_{\theta}^2 + v_{\phi}^2 =\
              v^2 - v_r^2 $ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()

    figure()
    plt.ylim(-10, 10)
    plt.plot(v_r, v_theta, 'o', ms=1.)
    plt.xlabel(r'$v_r$')
    plt.ylabel(r'$v_{\theta}$')
    plt.title(r'check if $ v_{\theta} =\
              v_r$ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()

    figure()
    plt.plot(v_r, v_phi, 'o', ms=1.)
    plt.xlabel(r'$ v_r $')
    plt.ylabel(r'$  v_{\Phi}$')
    plt.title(r'check if $ v_{\Phi} =\
              v_r$ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()

    figure()
    plt.xlim(-20, 20)
    plt.plot(v_theta, v_phi, 'o', ms=1.)
    plt.xlabel(r'$ v_{\theta} $')
    plt.ylabel(r'$ v_{\phi}$')
    plt.title(r'check if $ v_{\phi} =\
              v_{\theta} $ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()


if plotvelocitychecknew:  # Check new velocities are correct
    y1 = VTheta ** 2 + VPhi ** 2  # v_t ** 2
    y2 = v ** 2 - VR ** 2  # v_t ** 2
    figure()
    plt.plot(y1, y2, 'o', ms=1.)
    plt.xlabel(r'$ v_{\theta}^2 + v_{\phi}^2 $')
    plt.ylabel(r'$  v^2 - v_r^2$')
    plt.title(r'check if $ v_{\theta}^2 + v_{\phi}^2 =\
              v^2 - v_r^2 $ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()

    figure()
    plt.plot(VR, VTheta, 'o', ms=1.)
    plt.xlabel(r'$ v_r $')
    plt.ylabel(r'$  v_{\theta}$')
    plt.title(r'check if $ v_{\theta} =\
              v_r$ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()

    figure()
    plt.plot(VR, VPhi, 'o', ms=1.)
    plt.xlabel(r'$ v_r $')
    plt.ylabel(r'$  v_{\Phi}$')
    plt.title(r'check if $ v_{\Phi} =\
              v_r$ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()

    figure()
    plt.plot(VTheta, VPhi, 'o', ms=1.)
    plt.xlabel(r'$ v_{\Theta} $')
    plt.ylabel(r'$  v_{\Phi}$')
    plt.title(r'check if $ v_{\Phi} =\
              v_{\Theta} $ ($N=%i$, $\gamma = %.2f$)' % (len(x), Gamma))
    plt.grid()

if Fig4_vspherical_hist_old:
    nr_binning_bins_v = 30
    v_arr = []
    v_binning_arr = np.linspace(v_limit_min, v_limit_max, nr_binning_bins_v)
    f = plt.figure()
    plt.subplot(121)
    plt.xlabel(r'$v$, $v_r$, $v_t$, $ v_{\theta}$ and $ v_{\phi}$')
    plt.ylabel('Number of particles')
    plt.title(r'f(v) (Hernquist structure,\
              $N=%i$, $\gamma = %.2f$' % (len(x), Gamma))
    plt.hist(v, bins=100, histtype='step', color='r',
             range=(v_limit_min, v_limit_max), label=r'$v$', lw=2)
    plt.hist(v_r, bins=100, histtype='step', color='b',
             range=(v_limit_min, v_limit_max), label=r'$v_r$', lw=2)
    plt.hist(v_t_len, bins=100, histtype='step', color='Indigo',
             range=(v_limit_min, v_limit_max), label=r'$v_t$', lw=2)
    plt.hist(v_theta, bins=100, histtype='step', color='k',
             range=(v_limit_min, v_limit_max), label=r'$v_{\theta}$', lw=2)
    plt.hist(v_phi, bins=100, histtype='step', color='c',
             range=(v_limit_min, v_limit_max), label=r'$v_{\phi}$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)

    plt.subplot(122)
    plt.xlabel(r'$\log v$, $\log v_r$, $\log v_t$,\
               $\log v_{\theta}$ and $ \log v_{\phi}$')
    plt.hist(np.log10(np.absolute(v)), bins=100, histtype='step',
             color='r', range=(-5, 0), label=r'$\log v$', lw=2)
    plt.hist(np.log10(np.absolute(v_r)), bins=100, histtype='step',
             color='b', range=(-5, 0), label=r'$\log v_r$', lw=2)
    plt.hist(np.log10(np.absolute(v_t_len)), bins=100, histtype='step',
             color='Indigo', range=(-5, 0), label=r'$\log v_r$', lw=2)
    plt.hist(np.log10(np.absolute(v_theta)), bins=100, histtype='step',
             color='k', range=(-5, 0), label=r'$\log v_{\theta}$', lw=2)
    plt.hist(np.log10(np.absolute(v_phi)),  bins=100, histtype='step',
             color='c', range=(-5, 0), label=r'$\log v_{\phi}$', lw=2)
    plt.legend(prop=dict(size=11), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if Fig5_vspherical_hist_logfail_new:
    f = plt.figure()
    ax1 = f.add_subplot(121)
    (mu, sigma) = norm.fit(VR)
    n, bins, patches = plt.hist(VR, 100, histtype='step', color='r',
                                label=r'$v_r$', alpha=.75)
    # n, bins, patches = plt.hist(VR, 100, histtype='step',
    #                             normed=1, color='red',
    #                             label=r'$v_r$', alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    # popt, pcov = curve_fit(func_4, xdata, ydata)
    # y_fit = func_4(xdata, popt[0], popt[1], popt[2])
    # plt.plot(xdata, y_fit, '--', lw=3, color='red',
    #         label=r'$v_r-fit= a \cdot (1- (1 - q )\cdot b\
    #         \cdot x^2)^{(\frac{q}{1 - q})}$, $q = %.3f$' % popt[1])
    # popt, pcov = curve_fit(func_2, xdata, ydata)
    # y_fit = func_2(xdata, popt[0], popt[1])
    # plt.plot(xdata, y_fit, '--', lw=3, color='pink',
    #         label=r'$v_r-fit= a \cdot e^{-b \cdot x^2}$\
    #                ($\mu=%.3f$, $\sigma=%.3f$)' % (mu, sigma))

    (mu, sigma) = norm.fit(VTheta)
    n, bins, patches = plt.hist(VTheta, 100, histtype='step', color='b',
                                label=r'$v_{\theta}$', alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n

    (mu, sigma) = norm.fit(VPhi)
    n, bins, patches = plt.hist(VPhi, 100, histtype='step', color='g',
                                label=r'$ v_{\phi}$', alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n

    plt.xlabel(r'$v_r$, $v_{\theta}$ and $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\gamma = %.2f$, File = %s)'
              % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.grid()
    ax1.set_yscale('log')

    ax2 = f.add_subplot(122)
    (mu, sigma) = norm.fit(np.log10(np.absolute(VR)))
    n, bins, patches = plt.hist(np.log10(np.absolute(VR)), 100,
                                histtype='step', color='r',
                                label=r'$ \log |v_r| $', alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n

    (mu, sigma) = norm.fit(np.log10(np.absolute(VTheta)))
    n, bins, patches = plt.hist(np.log10(np.absolute(VTheta)), 100,
                                histtype='step', color='b',
                                label=r'$ \log |v_{\theta}|$', alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n

    (mu, sigma) = norm.fit(np.log10(np.absolute(VPhi)))
    n, bins, patches = plt.hist(np.log10(np.absolute(VPhi)), 100,
                                histtype='step', color='g',
                                label=r'$ \log |v_{\phi}|$', alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n

    plt.xlabel(r'$\log |v_r|$, $\log |v_{\theta}|$, $\log |v_{\phi}|$')
    plt.ylabel('number of particles')
    plt.title(r'$f(\log |v|)$ ')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig6_v_hist_logfail:
    plt.figure()
    (mu, sigma) = norm.fit(np.log10(np.absolute(v)))
    n, bins, patches = plt.hist(np.log10(np.absolute(v)), 100,
                                histtype='step', normed=1, color='b',
                                label=r'$\log v$', alpha=.75)
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, '--', lw=3, color='SkyBlue',
             label=r'Fit to $\log v$')
    plt.xlabel(r'$\log v$')
    plt.ylabel('number of particles')
    plt.title(r'VDF ($\mu=%.2f$, $\sigma=%.2f$)' % (mu, sigma))
    plt.grid()
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if Fig7_vspherical_hist_logfail_old:
    f = plt.figure()  # plot structure over radial bins.
    plt.subplot(121)
    plt.xlabel(r'$v_r, v_{\theta}$ and $v_{\phi}$')
    plt.ylabel('Number of particles')
    plt.title(r'VDF (HQ structure, $10^6$ particles).\
                distance: 0.5 to 0.25 kpc from center')
    plt.hist(v_theta, bins=100, histtype='step', color='r',
             range=(-.7, 1),
             label=r'$v_{\theta}$', lw=2)
    plt.hist(v_phi, bins=100, histtype='step', color='skyblue',
             range=(-.7, 1),
             label=r'$v_{\phi}$', lw=2)
    plt.hist(v_r, bins=100, histtype='step', color='k',
             range=(-.7, 1),
             label=r'$v_r$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)

    plt.subplot(122)
    plt.xlabel(r'$\log v_r, \log v_{\theta}$ and $ \log v_{\phi}$')
    plt.hist(np.log10(np.absolute(v_theta)), bins=100, histtype='step',
             color='r', range=(-5, 1), label=r'$\log v_{\theta}$',
             lw=2)
    plt.hist(np.log10(np.absolute(v_phi)), bins=100, histtype='step',
             color='skyblue', range=(-5, 1), label=r'$\log v_{\phi}$',
             lw=2)
    plt.hist(np.log10(np.absolute(v_r)), bins=100, histtype='step',
             color='k', range=(-5, 1), label=r'$\log v_r$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

# divide into 6 graphs
v_rp, v_rn, v_thetap, v_thetan, v_phip, v_phin, v_tp, v_tn =\
    ([] for i in range(8))

if vsphericalold:
    for i in range(len(x)):
        v_rp.append(v_r[i]) if (v_r[i] >= 0.) else v_rn.append(v_r[i])
        v_thetap.append(v_theta[i]) if (v_theta[i] >= 0.) else v_thetan.append(v_theta[i])
        v_phip.append(v_phi[i]) if (v_phi[i] >= 0.) else v_phin.append(v_phi[i])

    v_rp_arr, v_rn_arr = np.asarray(v_rp), np.asarray(v_rn)
    v_thetap_arr, v_thetan_arr = np.asarray(v_thetap), np.asarray(v_thetan)
    v_phip_arr, v_phin_arr = np.asarray(v_phip), np.asarray(v_phin)


if vsphericalnew:
    for i in range(len(VR)):
        v_rp.append(VR[i]) if (VR[i] >= 0.) else v_rn.append(VR[i])
    v_rp_arr, v_rn_arr = np.asarray(v_rp), np.asarray(v_rn)

    for i in range(len(VTheta)):
        v_thetap.append(VTheta[i]) if (VTheta[i] >= 0.) else v_thetan.append(VTheta[i])
    v_thetap_arr, v_thetan_arr = np.asarray(v_thetap), np.asarray(v_thetan)

    for i in range(len(VPhi)):
        v_phip.append(VPhi[i]) if (VPhi[i] >= 0.) else v_phin.append(VPhi[i])
    v_phip_arr, v_phin_arr = np.asarray(v_phip), np.asarray(v_phin)

    for i in range(len(VT)):
        v_tp.append(VT[i]) if (VT[i] >= 0.) else v_tn.append(VT[i])
    v_tp_arr, v_tn_arr = np.asarray(v_tp), np.asarray(v_tn)


if print_vp_vn:
    print(f'v_rp_arr = {v_rp_arr}'
          f'v_rp_arr.shape = {v_rp_arr.shape}'
          f'v_rn_arr = {v_rn_arr}'
          f'v_rn_arr.shape = {v_rn_arr.shape}'
          f'v_thetap_arr = {v_thetap_arr}'
          f'v_thetap_arr.shape = {v_thetap_arr.shape}'
          f'v_thetan_arr = {v_thetan_arr}'
          f'v_thetan_arr.shape = {v_thetan_arr.shape}'
          f'v_phip_arr = {v_phip_arr}'
          f'v_phip_arr.shape = {v_phip_arr.shape}'
          f'v_phin_arr = {v_phin_arr}'
          f'v_phin_arr.shape = {v_phin_arr.shape}')

    print(f'v_tp_arr = {v_tp_arr} \n'
          f'v_tp_arr.shape = {v_tp_arr.shape} \n'
          f'v_tn_arr = {v_tn_arr} \n'
          f'v_tn_arr.shape = {v_tn_arr.shape} \n')

if Fig8_vspherical_hist_log_vpvn:
    f = plt.figure()
    plt.xlabel(r'$\log v_rp, \log v_{\theta}p$,\
                 $\log v_{\phi}p$, $\log v_rn, \log v_{\theta}n$\
                 and $ \log v_{\phi}n$')
    plt.ylabel('Number of particles')
    plt.title(f'Positive and negative f(v)\
                ($N= {len(x) : %.3f$}, $\gamma = {Gamma : .1f$},\
                File = {F : %s})')

    plt.hist(np.log10(v_thetap_arr), bins=100, histtype='step', color='r',
             range=(-5, 1), label=r'$\log v_{\theta}p$', lw=2)
    plt.hist(np.log10(v_phip_arr), bins=100, histtype='step', color='skyblue',
             range=(-5, 1), label=r'$\log v_{\phi}p$', lw=2)
    plt.hist(np.log10(v_rp_arr), bins=100, histtype='step', color='k',
             range=(-5, 1), label=r'$\log v_rp$', lw=2)
    plt.hist(np.log10(np.absolute(v_thetan_arr)), bins=100, histtype='step',
             color='g', range=(-5, 1), label=r'$\log v_{\theta}n$', lw=2)
    plt.hist(np.log10(np.absolute(v_phin_arr)), bins=100, histtype='step',
             color='b', range=(-5, 1), label=r'$\log v_{\phi}n$', lw=2)
    plt.hist(np.log10(np.absolute(v_rn_arr)), bins=100, histtype='step',
             color='c', range=(-5, 1), label=r'$\log v_rn$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)


x1 = list(v_thetap_arr)
x2 = list(v_phip_arr)
x3 = list(v_rp_arr)
x4 = list(v_thetan_arr)
x5 = list(v_phin_arr)
x6 = list(v_rn_arr)

if x14_25_36_same_length:
    if len(v_thetan_arr) > len(v_thetap_arr):
        for i in range(len(v_thetan_arr) - len(v_thetap_arr)):
            x1.append(0.)
    else:
        for i in range(len(v_thetap_arr) - len(v_thetan_arr)):
            x4.append(0.)
    x1, x4 = np.asarray(x1), np.asarray(x4)

    if len(v_phin_arr) > len(v_phip_arr):
        for i in range(len(v_phin_arr) - len(v_phip_arr)):
            x2.append(0.)
    else:
        for i in range(len(v_phip_arr) - len(v_phin_arr)):
            x5.append(0.)
    x2, x5 = np.asarray(x2), np.asarray(x5)

    if len(v_rn_arr) > len(v_rp_arr):
        for i in range(len(v_rn_arr) - len(v_rp_arr)):
            x3.append(0.)
    else:
        for i in range(len(v_rp_arr) - len(v_rp_arr)):
            x6.append(0.)
    x3, x6 = np.asarray(x3), np.asarray(x6)


if print_x123456:
    print(f'x1 = {x1}'
          f'x1.shape = {x1.shape}'
          f'x4.shape = {x4.shape}'
          f'v_thetap_arr.shape = {v_thetap_arr.shape}'
          f'v_thetan_arr.shape = {v_thetan_arr.shape}'
          f'x2 = {x2}'
          f'x2.shape = {x2.shape}'
          f'x5.shape = {x5.shape}'
          f'x3 = {x3}'
          f'x3.shape = {x3.shape}'
          f'x6.shape = {x6.shape}'
          f'type(x1) = {type(x1)}')

if Fig9_VPhiminus:  # test VPhi and VPhiminus = -VPhi
    VPhiminus = sp.sin(Phi) * vx - sp.cos(Phi) * vy
    f = plt.figure()
    plt.subplot(121)
    plt.xlabel(r'$v_{\phi}$, $-v_{\phi}$,\
               $\log |v_{\phi}|$ and $\log |-v_{\phi}|$')
    plt.ylabel('Number of particles')
    plt.title(r'f(v) comparison ($N=%.3f$, $\gamma = %.1f$, File = %s )'
              % (len(x), Gamma, F))
    plt.hist(VPhi, bins=100, histtype='step', color='r',
             range=(-5, 1), label=r'$ v_{\phi}$', lw=2)
    plt.hist(VPhiminus, bins=100, histtype='step', color='skyblue',
             range=(-5, 1), label=r'$-v_{\phi}$', lw=2)
    plt.hist(np.log10(np.absolute(VPhi)), bins=100, histtype='step',
             color='g', range=(-5, 1), label=r'$\log |v_{\phi}|$', lw=2)
    plt.hist(np.log10(np.absolute(VPhiminus)), bins=100, histtype='step',
             color='b', range=(-5, 1), label=r'$\log |-v_{\phi}|$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
    plt.subplot(122)
    plt.xlabel(r'$\log v_rp + \log |v_rn|$, $\log v_{\theta}p\
               + \log |v_{\theta}n|$ and $\log v_{\phi}p + \log |v_{\phi}n|$')
    plt.ylabel('Number of particles')
    plt.title(r'Positive and negative f(v) summed')
    plt.hist(np.log10(x1) + np.log10(np.absolute(x4)), bins=100,
             histtype='step', color='r', range=(-5, 1),
             label=r'$\log v_{\theta}p + \log |v_{\theta}n|$', lw=2)
    plt.hist(np.log10(x2) + np.log10(np.absolute(x5)), bins=100,
             histtype='step', color='b', range=(-5, 1),
             label=r'$\log v_{\phi}p + \log |v_{\phi}n|$', lw=2)
    plt.hist(np.log10(x3) + np.log10(np.absolute(x6)), bins=100,
             histtype='step', color='g', range=(-5, 1),
             label=r'$\log v_rp + \log |v_rn|$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if vsphericalnew_sigma:
    VR_sigmarad_p, VR_sigmarad_n, VTheta_sigmatheta_p, VTheta_sigmatheta_n,
    VPhi_sigmaphi_p, VPhi_sigmaphi_n, VT_sigmatan_p, VT_sigmatan_n =\
        ([] for i in range(8))

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

    VR_i_average_inside_bin_sigmarad_p, VR_i_average_inside_bin_sigmarad_n,
    VT_i_average_inside_bin_sigmatan_p, VT_i_average_inside_bin_sigmatan_n,
    VPhi_i_average_inside_bin_sigmaphi_p, VPhi_i_average_inside_bin_sigmaphi_n,
    VTheta_i_average_inside_bin_sigmatheta_p,
    VTheta_i_average_inside_bin_sigmatheta_n =\
        ([] for i in range(8))

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
    print(f'VR_sigmarad_p_arr = {VR_sigmarad_p_arr}'
          f'VR_sigmarad_p_arr.shape = {VR_sigmarad_p_arr.shape}'
          f'VR_sigmarad_n_arr = {VR_sigmarad_n_arr}'
          f'VR_sigmarad_n_arr.shape = {VR_sigmarad_n_arr.shape}'
          f'VTheta_sigmatheta_p_arr = {VTheta_sigmatheta_p_arr}'
          f'VTheta_sigmatheta_p_arr.shape = {VTheta_sigmatheta_p_arr.shape}'
          f'VTheta_sigmatheta_n_arr = {VTheta_sigmatheta_n_arr}'
          f'VTheta_sigmatheta_n_arr.shape = {VTheta_sigmatheta_n_arr.shape}'
          f'VPhi_sigmaphi_p_arr = {VPhi_sigmaphi_p_arr}'
          f'VPhi_sigmaphi_p_arr.shape = {VPhi_sigmaphi_p_arr.shape}'
          f'VPhi_sigmaphi_n_arr = {VPhi_sigmaphi_n_arr}'
          f'VPhi_sigmaphi_n_arr.shape = {VPhi_sigmaphi_n_arr.shape}'
          f'VT_sigmatan_p_arr = {VT_sigmatan_p_arr}'
          f'VT_sigmatan_p_arr.shape = {VT_sigmatan_p_arr.shape}'
          f'VT_sigmatan_n_arr = {VT_sigmatan_n_arr}'
          f'VT_sigmatan_n_arr.shape = {VT_sigmatan_n_arr.shape}')

    # VTheta = np.array(VTheta)
    # VPhi = np.array(VPhi)
    # VR_sigmarad = np.array(VR_sigmarad)
    # VTheta_sigmatheta = np.array(VTheta_sigmatheta)
    # VPhi_sigmaphi = np.array(VPhi_sigmaphi)

    if print_sigma_binned_lin_radius:
        print(f'sigmarad2 = {sigmarad2}'
              f'sigmarad2.shape = {sigmarad2.shape}'
              f'sigmatheta2 = {sigmatheta2}'
              f'sigmatheta2.shape = {sigmatheta2.shape}'
              f'sigmaphi2 = {sigmaphi2}'
              f'sigmaphi2.shape = {sigmaphi2.shape}'
              f'sigmarad = {sigmarad}'
              f'sigmarad.shape = {sigmarad.shape}'
              f'sigmatheta = {sigmatheta}'
              f'sigmatheta.shape = {sigmatheta.shape}'
              f'sigmaphi = {sigmaphi}'
              f'sigmaphi.shape = {sigmaphi.shape}'
              f'VR = {VR}'
              f'VR.shape = {VR.shape}'
              f'VTheta = {VTheta}'
              f'VTheta.shape = {VTheta.shape}'
              f'VPhi = {VPhi}'
              f'VPhi.shape = {VPhi.shape}'
              f'VR_sigmarad.shape = {(VR / sigmarad).shape}'
              f'VR_sigmarad = {VR / sigmarad}'
              f'np.where(sigmarad == 0) = {np.where(sigmarad == 0)}'
              f'np.where(sigmatheta == 0) = {np.where(sigmatheta == 0)}'
              f'np.where(sigmaphi == 0) = {np.where(sigmaphi == 0)}')

        # pass

if Fig10_concatenate_x789:  # check new log, concatenate lists x1 and x4, x2 and x5, x3 and x6.
    x7 = np.asarray(x1 + list(np.absolute(v_thetan_arr)))
    x8 = np.asarray(x2 + list(np.absolute(v_phin_arr)))
    x9 = np.asarray(x3 + list(np.absolute(v_rn_arr)))

    f = plt.figure()
    ax = f.add_subplot(121)
    n, bins, patches = plt.hist(VR, 100, histtype='step', color='r',
                                label=r'$v_r$', alpha=.75)
    n, bins, patches = plt.hist(VTheta, 100, histtype='step', color='b',
                                label=r'$v_{\theta}$', alpha=.75)
    n, bins, patches = plt.hist(VPhi, 100, histtype='step', color='g'
                                label=r'$ v_{\phi}$', alpha=.75)
    plt.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\beta = %.2f$, File = %s )' % (len(x), Beta, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.grid()
    ax.set_yscale('log')

    ax = f.add_subplot(122)
    n, bins, patches = plt.hist(np.log10(x7), bins=100, histtype='step',
                                color='r', range=(-5, 1),
                                label=r'$\log (|v_{\theta}n|,v_{\theta}p)$',
                                lw=2)
    n, bins, patches = plt.hist(np.log10(x8), bins=100, histtype='step',
                                color='b', range=(-5, 1),
                                label=r'$\log (|v_{\phi}n|,v_{\phi}p)$', lw=2)
    n, bins, patches = plt.hist(np.log10(x9), bins=100, histtype='step',
                                color='g', range=(-5, 1),
                                label=r'$\log (|v_rn|,v_rp)$', lw=2)
    plt.xlabel(r'$\log (|v_rn|,v_rp)$, $\log (|v_{\theta}n|,v_{\theta}p)$\
               and $\log (|v_{\phi}n|,v_{\phi}p)$')
    plt.ylabel('Number of particles')
    plt.title(r'$ f(\log (|v_n|,v_p)) $')
    plt.grid()
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if Fig11_vspherical_hist_log_n123:
    f  = plt.figure()
    ax = f.add_subplot(121)
    # (mu, sigma) = norm.fit(VR)
    n, bins, patches = plt.hist(VR, 100, histtype='step', color='r',
                                label=r'$v_r$', alpha=.75)
    # (mu, sigma) = norm.fit(VTheta)
    n, bins, patches = plt.hist(VTheta, 100, histtype='step', color='b',
                                label=r'$v_{\theta}$', alpha=.75)
    # (mu, sigma) = norm.fit(VPhi)
    n, bins, patches = plt.hist(VPhi, 100, histtype='step', color='g',
                                label=r'$v_{\phi}$', alpha=.75)
    plt.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\gamma = %.2f$, File = %s )'
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
                                color='r', label=r'$\log (v_rp + |v_rn|)$',
                                alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n1))
    n, bins, patches = plt.hist(np.log10(n1), 100, histtype='step',
                                color='b',
                                label=r'$\log (v_{\theta}p + |v_{\theta}n|)$',
                                alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n2))
    n, bins, patches = plt.hist(np.log10(n2), 100, histtype='step',
                                color='g',
                                label=r'$\log (v_{\phi}p + |v_{\phi}n|)$',
                                alpha=.75)
    plt.xlabel(r'$\log (v_{\theta}p + |v_{\theta}n|)$, $\log (v_{\phi}p +\
               |v_{\phi}n|)$ and $\log (v_rp + |v_rn|)$')
    plt.ylabel('number of particles')
    plt.title(r'Positive and negative f(v) summed ')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

# All figures with log(v) can instead be plotted as log(v) vs. f(v) / v.
# The idea is, that a flat tail will appear towards small velocities.
# Next I will plot v / sigma along the x-axes instead of v
# (and with log(v / sigma) as well).
# Plotting v / sigma makes it easier to compare different radial bins,
# because the x-axis will almost always be the same,
# even though they actually have very different sigma.

if Fig12_n123_sigma:
    # txt = open(Filename.strip('.hdf5') + 'Sigma.txt', 'r')
    # print txt.read()
    txt = Filename.strip('.hdf5') + 'Sigma.txt'
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

    f = plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(n3) / linalg.norm(VR), 100,
                                histtype='step', color='r',
                                label=r'$\frac{f(\log (v_rp +\
                                |v_rn|))}{||v_r||}$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1) / linalg.norm(VTheta), 100,
                                histtype='step', color='b',
                                label=r'$\frac{f(\log (v_{\theta}p +\
                                |v_{\theta}n|))}{||v_{\theta}||}$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2) / linalg.norm(VPhi), 100,
                                histtype='step', color='g',
                                label=r'$\frac{f(\log (v_{\phi}p +\
                                |v_{\phi}n|))}{||v_{\phi}||}$',
                                alpha=.75)
    plt.xlabel(r'$\frac{\log (v_rp + |v_rn|)}{||v_r||}$,\
               $\frac{\log (v_{\theta}p +\
               |v_{\theta}n|)}{||v_{\theta}||}$\
               and $\frac{\log (v_{\phi}p + |v_{\phi}n|)}{||v_{\phi}||}$')
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
    n, bins, patches = plt.hist(VTheta / linalg.norm(normTXT_theta_arr), 100,
                                histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                {\sigma_{\theta}}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VPhi / linalg.norm(normTXT_phi_arr), 100,
                                histtype='step', color='g',
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
                                color='r',
                                label=r'$f(\log (v_rp + |v_rn|))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1), 100, histtype='step',
                                color='b',
                                label=r'$f(\log\
                                (v_{\theta}p + |v_{\theta}n|))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2), 100, histtype='step',
                                color='g',
                                label=r'$f(\log (v_{\phi}p + |v_{\phi}n|))$',
                                alpha=.75)
    plt.xlabel(r'$\log (v_rp + |v_rn|)$, $\log (v_{\theta}p +\
               |v_{\theta}n|)$ and $\log (v_{\phi}p + |v_{\phi}n|)$')
    plt.ylabel(r'$f(\log (v_p + |v_n|))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(n3 / linalg.norm(normTXT_r_arr)),
                                100, histtype='step', color='r',
                                label=r'$f\left(\log \left( \frac{v_rp +\
                                |v_rn|}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n1 / linalg.norm(normTXT_theta_arr)),
                                100, histtype='step', color='b',
                                label=r'$f\left(\log \left( \frac{v_{\theta}p \
                                      + |v_{\theta}n|}\
                                      {\sigma_{\theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(n2 / linalg.norm(normTXT_phi_arr)),
                                100, histtype='step', color='g',
                                label=r'$f\left(\log \left( \frac{v_{\phi}p +\
                                      |v_{\phi}n|}\
                                      {\sigma_{\phi}}\right)\right)$',
                                alpha=.75)
    plt.xlabel(r'$\log \left( u_rp + |u_rn| \right)$,\
               $\log \left( u_{\theta}p + |u_{\theta}n| \right)$\
               and $\log \left( u_{\phi}p + |u_{\phi}n| \right)$')
    plt.ylabel(r'$f\left(\log \left( u_p + |u_n| \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig12_x789_sigma:
    x7 = np.asarray(x1 + list(np.absolute(v_thetan_arr)))
    x8 = np.asarray(x2 + list(np.absolute(v_phin_arr)))
    x9 = np.asarray(x3 + list(np.absolute(v_rn_arr)))
    txt = Filename.strip('.hdf5') + 'Sigma.txt'
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

    f = plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(x9) / linalg.norm(VR), 100,
                                histtype='step', color='r', range=(-.1, .0),
                                label=r'$f\left(\frac{\log (|v_rn|,\
                                v_rp))}{||v_r||} \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7) / linalg.norm(VTheta), 100,
                                histtype='step', color='b', range=(-.1, .0),
                                label=r'$f\left(\frac{\log\
                                      (|v_{\theta}n|, v_{\theta}p))}\
                                      {||v_{\theta}||} \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8) / linalg.norm(VPhi), 100,
                                histtype='step', color='g',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                      (|v_{\phi}n|, v_{\phi}p))}\
                                      {||v_{\phi}||} \right)$',
                                alpha=.75)
    plt.xlabel(r'$\frac{\log (|v_rn|, v_rp)}{||v_r||}$,\
               $\frac{\log(|v_{\theta}n|, v_{\theta}p)}{||v_{\theta}||}$\
               and $\frac{\log (|v_{\phi}n|, v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left(\frac{\log (|v_n|, v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR / linalg.norm(normTXT_r_arr), 100,
                                histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta / linalg.norm(normTXT_theta_arr), 100,
                                histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                      {\sigma_{\theta}}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VPhi / linalg.norm(normTXT_phi_arr), 100,
                                histtype='step', color='g',
                                label=r'$f\left(\frac{v_{\phi}}\
                                      {\sigma_{\phi}}\right)$',
                                alpha=.75)
    plt.xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$')
    plt.ylabel(r'$f\left( u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(x9), 100, histtype='step',
                                color='r', range=(-3, 0),
                                label=r'$f(\log (|v_rn|,v_rp))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7), 100, histtype='step',
                                color='blue', range=(-3, 0),
                                label=r'$f(\log (|v_{\theta}n|,v_{\theta}p))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8), 100, histtype='step',
                                color='g', range=(-3, 0),
                                label=r'$f(\log (|v_{\phi}n|,v_{\phi}p))$',
                                alpha=.75)
    plt.xlabel(r'$\log (|v_rn|, v_rp)$, $\log (|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|, v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|, v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9 / linalg.norm(normTXT_r_arr)), 100,
                                histtype='step', color='r', range=(-3, 0),
                                label=r'$f\left(\log \left( \frac{|v_rn|,\
                                      v_rp}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7 / linalg.norm(normTXT_theta_arr)),
                                100, histtype='step', color='b',
                                range=(-3, 0),
                                label=r'$f\left(\log \left(\
                                      \frac{|v_{\theta}n|,v_{\theta}p}\
                                      {\sigma_{\theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8 / linalg.norm(normTXT_phi_arr)),
                                100, histtype='step', color='g',
                                range=(-3, 0),
                                label=r'$f\left(\log \left( \frac{|v_{\phi}n|,\
                                      v_{\phi}p}{\sigma_{\phi}}\
                                      \right)\right)$',
                                alpha=.75)
    plt.xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|\
               , u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,\
               u_{\phi}p \right)$')
    plt.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig12_vr_vtheta_vphi_vt_sigma:
    v_rpn = np.asarray(list(v_rp_arr) + list(np.absolute(v_rn_arr)))
    v_thetapn = np.asarray(list(v_thetap_arr) + list(np.absolute(v_thetan_arr)))
    v_phipn = np.asarray(list(v_phip_arr) + list(np.absolute(v_phin_arr)))
    v_tpn = np.asarray(list(v_tp_arr) + list(np.absolute(v_tn_arr)))
    x7  = np.asarray(list(VTheta_sigmatheta_p_arr) + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8  = np.asarray(list(VPhi_sigmaphi_p_arr) + list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9  = np.asarray(list(VR_sigmarad_p_arr) + list(np.absolute(VR_sigmarad_n_arr)))
    x10 = np.asarray(list(VT_sigmatan_p_arr) + list(np.absolute(VT_sigmatan_n_arr)))

    f = plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(v_rpn) / linalg.norm(VR), 100,
                                histtype='step', color='r', range=(-.1, .0),
                                label=r'$f\left(\frac{\log (|v_rn|, v_rp)}\
                                      {||v_r||}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn) / linalg.norm(VTheta), 100,
                                histtype='step', color='b', range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_{\theta}n|,\
                                      v_{\theta}p))}{||v_{\theta}||} \right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_phipn) / linalg.norm(VPhi), 100,
                                histtype='step', color='g',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_{\phi}n|,\
                                      v_{\phi}p))}{||v_{\phi}||} \right)$',
                                alpha=.75)
    (mu, sigma) = norm.fit(np.log10(v_rpn) / linalg.norm(VR))
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, '--', lw=3, color='pink',
             label=r'$\frac{\log(v_r)}{|| v_r ||} -fit =\
                   a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
    plt.xlabel(r'$\frac{\log (|v_rn|,v_rp)}{||v_r||}$, $\frac{\log\
               (|v_{\theta}n|,v_{\theta}p)}{||v_{\theta}||}$ and $\frac{\log\
               (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (|v_n|,v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR_sigmarad, 100, histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VTheta_sigmatheta, 100,
                                histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                      {\sigma_{\theta}}\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(VPhi_sigmaphi, 100, histtype='step',
                                color='g',
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
                                color='r', range=(-3, 0),
                                label=r'$f(\log (|v_rn|,v_rp))$', alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn), 100, histtype='step',
                                color='b', range=(-3, 0),
                                label=r'$f(\log (|v_{\theta}n|,v_{\theta}p))$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(v_phipn), 100, histtype='step',
                                color='g', range=(-3, 0),
                                label=r'$f(\log (|v_{\phi}n|,v_{\phi}p))$',
                                alpha=.75)
    (mu, sigma) = norm.fit(np.log10(v_rpn))
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata, popt[0], popt[1])
    plt.plot(xdata, y_fit, '--', lw=3, color='pink',
             label=r'$\log(v_r)-fit = a \cdot log(x) \cdot\
                   e^{-b \cdot log(x)^2}$')
    plt.xlabel(r'$\log (|v_rn|, v_rp)$, $\log(|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|, v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|,v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9), 100, histtype='step',
                                color='r', range=(-3, 1),
                                label=r'$f\left(\log \left(\frac{|v_rn|,\
                                      v_rp}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x7), 100, histtype='step',
                                color='b', range=(-3, 1),
                                label=r'$f\left(\log \left(\
                                      \frac{|v_{\theta}n|, v_{\theta}p}\
                                      {\sigma_{\theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = plt.hist(np.log10(x8), 100, histtype='step',
                                color='g', range=(-3, 1),
                                label=r'$f\left(\log \left(\frac{|v_{\phi}n|,\
                                      v_{\phi}p}{\sigma_{\phi}}\
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
    plt.xlabel(r'$\log \left( |u_rn|,u_rp \right)$,\
               $\log \left(|u_{\theta}n|,u_{\theta}p \right)$\
               and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
    plt.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)
    plt.grid()

if Fig13_vspherical_hist_old:
    f = plt.figure()
    (mu, sigma) = norm.fit(v_t_arr[6])  # best fit of data
    n, bins, patches = plt.hist(v_t_arr[6], 100, normed=1, color='g',
                                alpha=.75)
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
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFt.txt', x, delimiter=' ',
               header='    bins                         n')

    f = plt.figure()
    (mu, sigma) = norm.fit(v_r_arr[6])
    n, bins, patches = plt.hist(v_r_arr[6], 100, normed=1,
                                color='b', alpha=.75)
    # add a 'best fit' line
    # y = mlab.normpdf(bins, mu, sigma)
    # l = plt.plot(bins, y, 'r--', linewidth=2)
    # plot
    xdata = bins[0:-1] + (bins[1] - bins[0]) * .5
    ydata = n
    popt, pcov = curve_fit(func_2, xdata, ydata)
    y_fit = func_2(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, '--', lw=3, color='SkyBlue')
    plt.xlabel(r'$v_r$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$'
              % (mu, sigma))
    plt.grid()
    x = np.array((xdata, ydata))
    x = x.transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFr.txt', x, delimiter=' ',
               header='    bins                         n')

if save_r_v_as_txt:
    x = np.array((xcl2, ycl2, zcl2, vxnew2, vynew2, vznew2)).transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin0_05to0_25kpc_VDF.txt', x,
               delimiter=' ',
               header=' xcl2      ycl2      zcl2      vxnew2 \
               vynew2      vznew2 ')

plt.show()
