# -*- coding: utf-8 -*-

# Standard library imports
import h5py
import os

# Third party imports
import matplotlib.pyplot as plt
import numpy as np
import pylab
import scipy as sp
from scipy.optimize import curve_fit
from scipy.stats import norm

# Local application imports
import Mock_data as mock
import radius_and_velocity_funcs as ravf
from RhoAndGaussianAndTsallis import func1, func2, func1Log

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

IC_R_middle = 0
Gamma = -1.5

# Mock data -------------------------------------------------------------------
x, y, z = mock.x, mock.y, mock.z
vx, vy, vz = mock.vx, mock.vy, mock.vz
VR, VTheta, VPhi, VT = mock.VR, mock.VTheta, mock.VPhi, mock.VT
vMin, vMax, nr_v_bins = mock.vMin, mock.vMax, mock.nr_v_bins
v_t_len = mock.v_t_len
Phi = mock.Phi
(VR_sigmaR, VTheta_sigmatheta, VPhi_sigmaphi, VT_sigmaT,
 VR_i_avg_in_bin_sigmaR, VTheta_i_avg_in_bin_sigmatheta,
 VPhi_i_avg_in_bin_sigmaphi,
 VT_i_avg_in_bin_sigmaT) = (mock.VR_sigmaR,
 mock.VTheta_sigmatheta, mock.VPhi_sigmaphi, mock.VT_sigmaT,
 mock.VR_i_avg_in_bin_sigmaR, mock.VTheta_i_avg_in_bin_sigmatheta,
 mock.VPhi_i_avg_in_bin_sigmaphi, mock.VT_i_avg_in_bin_sigmaT)
sigmaR2, sigmatheta2, sigmaphi2 = mock.sigmaR2, mock.sigmatheta2, mock.sigmaphi2
sigmaR, sigmatheta, sigmaphi = mock.sigmaR, mock.sigmatheta, mock.sigmaphi
Beta = mock.Beta
xcl2, ycl2, zcl2 = mock.xcl2, mock.ycl2, mock.zcl2
vxnew2, vynew2, vznew2 = mock.vxnew2, mock.vynew2, mock.vznew2
v_t_arr, v_r_arr, VR_sigmarad = mock.v_t_arr, mock.v_r_arr, mock.VR_sigmarad


def switch_R_middle_depending_on_Gamma(Gamma):
    """Switch case."""
    return {
        -1.5: lambda: 10 ** -.70,
        -2.0: lambda: 10 ** -.25,
        -2.5: lambda: 1.,
        -3.: lambda: 10 ** -.30
    }.get(Gamma, lambda: None)()


def get_xdata(bins):
    return bins[0:-1] + (bins[1] - bins[0]) * .5


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
    print(f'{VR[0]= } \n' # .0
          f'{VTheta[0]= } \n' # 1.0
          f'{VPhi[0]= } \n' # 1.0
          f'{VR[1]= } \n' # -4.37114e-08
          f'{VTheta[1]= } \n' # 1.91069e-15
          f'{VPhi[1]= } \n' # -1.0
          f'{VR[2]= } \n' # 1.0
          f'{VTheta[2]= } \n' # -4.37114e-08
          f'{VPhi[2]= } \n') # 0.0

if vsphericalold:
    Rvector = np.array([x, y, z])
    vvector = np.array([vx, vy, vz])
    v_r, v_t = np.zeros([len(x), 1]), np.zeros([len(x), 3])
    print(f'{Rvector.shape= } \n'
          f'{vvector.shape= }')
    for i in range(len(x)):
        v_r[i] = np.divide(np.dot(Rvector[:, i], vvector[:, i]),
                           np.linalg.norm(Rvector[:, i]))
        v_t[i] = np.divide(np.cross(Rvector[:, i], vvector[:, i], axis=0),
                           np.linalg.norm(Rvector[:, i]))

    print(f'{v_r= } \n'
          f'{v_r.shape= } \n'
          f'{v_t= } \n'
          f'{v_t.shape= } \n')

    v = ravf.modulus(vx, vy, vz)

    # v_theta and v_phi -------------------------------------------------------
    v_theta = v_phi = np.zeros([len(x), 1])
    for i in range(len(x)):
        xy = x[i] ** 2 + y[i] ** 2
        if (xy > 0.):
            v_theta[i] = (x[i] * vy[i] - y[i] * vx[i]) / xy
    for i in range(len(x)):
        r = ravf.modulus(x[i], y[i], z[i])
        if ((r > 0.) and (z[i] != r)):
            v_phi[i] = ((r * vz[i] - z[i] * v_r[i]) / (r ** 2)
                        * (1 - (z[i] / r) ** 2) ** .5)

        '''
        v_phi[i] = (z[i] * (x[i] * vx[i] + y[i] * vy[i])
                   - (x[i] ** 2 + y[i] ** 2) * vz[i])\
                   / ((x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
                   * (x[i] ** 2 + y[i] ** 2) ** .5)
        v_theta[i] = np.dot()
        v_phi[i] = np.cross()
        '''

    print(f'{v_r[0]= }'  # [0.]
          f'{v_theta[0]= }'  # [0.]
          f'{v_phi[0]= }')  # [0.]

if plotvelocitycheckold:  # Check old velocities are correct
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f'ax{i}.grid()')

    y1 = v_theta ** 2 + v_phi ** 2  # v_t^2
    y2 = v ** 2 - v_r ** 2  # v_t^2
    ax1.plot(y1, y2, 'o', ms=1.)
    ax1.xlabel(r'$v_{\theta}^2 + v_{\phi}^2$')
    ax1.ylabel(r'$v^2 - v_r^2$')
    ax1.title(r'check if $v_{\theta}^2 + v_{\phi}^2=v^2 - v_r^2$ ($N=%i$, $\gamma=%.2f$)'
              % (len(x), Gamma))

    ax2.ylim(-10, 10)
    ax2.plot(v_r, v_theta, 'o', ms=1.)
    ax2.xlabel(r'$v_r$')
    ax2.ylabel(r'$v_{\theta}$')
    ax2.title(r'check if $v_{\theta}=v_r$ ($N=%i$, $\gamma = %.2f$)'
              % (len(x), Gamma))

    ax3.plot(v_r, v_phi, 'o', ms=1.)
    ax3.xlabel(r'$v_r$')
    ax3.ylabel(r'$v_{\Phi}$')
    ax3.title(r'check if $v_{\Phi}=v_r$ ($N=%i$, $\gamma = %.2f$)'
              % (len(x), Gamma))

    ax4.xlim(-20, 20)
    ax4.plot(v_theta, v_phi, 'o', ms=1.)
    ax4.xlabel(r'$v_{\theta}$')
    ax4.ylabel(r'$v_{\phi}$')
    ax4.title(r'check if $v_{\phi} = v_{\theta}$ ($N=%i$, $\gamma = %.2f$)'
              % (len(x), Gamma))

if plotvelocitychecknew:  # Check new velocities are correct
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f'ax{i}.grid()')

    y1 = VTheta ** 2 + VPhi ** 2  # v_t ** 2
    y2 = v ** 2 - VR ** 2  # v_t ** 2

    ax1.plot(y1, y2, 'o', ms=1.)
    ax1.xlabel(r'$v_{\theta}^2 + v_{\phi}^2$')
    ax1.ylabel(r'$v^2 - v_r^2$')
    ax1.title(r'check if $ v_{\theta}^2 + v_{\phi}^2=\
              v^2 - v_r^2 $ ($N=%i$, $\gamma=%.2f$)' % (len(x), Gamma))

    ax2.plot(VR, VTheta, 'o', ms=1.)
    ax2.xlabel(r'$v_r$')
    ax2.ylabel(r'$v_{\theta}$')
    ax2.title(r'check if $ v_{\theta}=\
              v_r$ ($N=%i$, $\gamma=%.2f$)' % (len(x), Gamma))

    ax3.plot(VR, VPhi, 'o', ms=1.)
    ax3.xlabel(r'$v_r$')
    ax3.ylabel(r'$v_{\Phi}$')
    ax3.title(r'check if $v_{\Phi}=\
              v_r$ ($N=%i$, $\gamma=%.2f$)' % (len(x), Gamma))

    ax4.plot(VTheta, VPhi, 'o', ms=1.)
    ax4.xlabel(r'$v_{\Theta}$')
    ax4.ylabel(r'$v_{\Phi}$')
    ax4.title(r'check if $ v_{\Phi}=\
              v_{\Theta} $ ($N=%i$, $\gamma=%.2f$)' % (len(x), Gamma))

if Fig4_vspherical_hist_old:
    nr_binning_bins_v = 30
    v_arr = []
    # Renaming: v_limit_min = vMin, v_limit_max = vMax, nr_binning_bins_v = nr_v_bins
    v_binning_arr = np.linspace(vMin, vMax, nr_v_bins)
    f = plt.figure()
    plt.subplot(121)
    plt.xlabel(r'$v$, $v_r$, $v_t$, $v_{\theta}$ and $v_{\phi}$')
    plt.ylabel('Number of particles')
    plt.title(r'f(v) (HQ structure, $N=%i$, $\gamma=%.2f$' % (len(x), Gamma))
    plt.hist(v, bins=100, histtype='step', color='r',
             range=(vMin, vMax), label=r'$v$', lw=2)
    plt.hist(v_r, bins=100, histtype='step', color='b',
             range=(vMin, vMax), label=r'$v_r$', lw=2)
    plt.hist(v_t_len, bins=100, histtype='step', color='m',
             range=(vMin, vMax), label=r'$v_t$', lw=2)
    plt.hist(v_theta, bins=100, histtype='step', color='k',
             range=(vMin, vMax), label=r'$v_{\theta}$', lw=2)
    plt.hist(v_phi, bins=100, histtype='step', color='c',
             range=(vMin, vMax), label=r'$v_{\phi}$', lw=2)

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
             color='m', range=(-5, 0), label=r'$\log v_r$', lw=2)
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
    n, bins, patches = ax1.hist(VR, 100, histtype='step', color='r',
                                label=r'$v_r$', alpha=.75)
    # n, bins, patches = plt.hist(VR, 100, histtype='step', normed=1,
    #                             color='r', label=r'$v_r$', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n
    # popt, pcov = curve_fit(func_4, xdata, ydata)
    # y_fit = func_4(xdata, popt[0], popt[1], popt[2])
    # plt.plot(xdata, y_fit, 'r--', lw=3,
    #         label=r'$v_r-fit= a \cdot (1- (1 - q )\cdot b\
    #         \cdot x^2)^{(\frac{q}{1 - q})}$, $q = %.3f$' % popt[1])
    # popt, pcov = curve_fit(func_2, xdata, ydata)
    # y_fit = func_2(xdata, popt[0], popt[1])
    # plt.plot(xdata, y_fit, '--', lw=3, color='pink',
    #         label=r'$v_r-fit= a \cdot e^{-b \cdot x^2}$\
    #                ($\mu=%.3f$, $\sigma=%.3f$)' % (mu, sigma))

    (mu, sigma) = norm.fit(VTheta)
    n, bins, patches = ax1.hist(VTheta, 100, histtype='step', color='b',
                                label=r'$v_{\theta}$', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n

    (mu, sigma) = norm.fit(VPhi)
    n, bins, patches = ax1.hist(VPhi, 100, histtype='step', color='g',
                                label=r'$v_{\phi}$', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n

    ax1.xlabel(r'$v_r$, $v_{\theta}$ and $v_{\phi}$')
    ax1.ylabel(r'$\log$ number of particles')
    ax1.title(r'f(v) ($N=%i$, $\gamma=%.2f$, File=%s)' % (len(x), Gamma, F))
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    ax1.grid()
    ax1.set_yscale('log')

    ax2 = f.add_subplot(122)
    (mu, sigma) = norm.fit(np.log10(np.absolute(VR)))
    n, bins, patches = ax2.hist(np.log10(np.absolute(VR)), 100,
                                histtype='step', color='r',
                                label=r'$\log|v_r|$', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n

    (mu, sigma) = norm.fit(np.log10(np.absolute(VTheta)))
    n, bins, patches = ax2.hist(np.log10(np.absolute(VTheta)), 100,
                                histtype='step', color='b',
                                label=r'$\log |v_{\theta}|$', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n

    (mu, sigma) = norm.fit(np.log10(np.absolute(VPhi)))
    n, bins, patches = ax2.hist(np.log10(np.absolute(VPhi)), 100,
                                histtype='step', color='g',
                                label=r'$\log |v_{\phi}|$', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n

    ax2.xlabel(r'$\log |v_r|$, $\log |v_{\theta}|$, $\log |v_{\phi}|$')
    ax2.ylabel('number of particles')
    ax2.title(r'$f(\log|v|)$')
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
    ax2.grid()

if Fig6_v_hist_logfail:
    plt.figure()
    (mu, sigma) = norm.fit(np.log10(np.absolute(v)))
    n, bins, patches = plt.hist(np.log10(np.absolute(v)), 100,
                                histtype='step', normed=1, color='b',
                                label=r'$\log v$', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func1Log, xdata, ydata)
    y_fit = func1Log(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, 'r--', lw=3, label=r'Fit to $\log v$')
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
             range=(-.7, 1), label=r'$v_{\theta}$', lw=2)
    plt.hist(v_phi, bins=100, histtype='step', color='b',
             range=(-.7, 1), label=r'$v_{\phi}$', lw=2)
    plt.hist(v_r, bins=100, histtype='step', color='k',
             range=(-.7, 1), label=r'$v_r$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)

    plt.subplot(122)
    plt.xlabel(r'$\log v_r, \log v_{\theta}$ and $ \log v_{\phi}$')
    plt.hist(np.log10(np.absolute(v_theta)), bins=100, histtype='step',
             color='r', range=(-5, 1), label=r'$\log v_{\theta}$', lw=2)
    plt.hist(np.log10(np.absolute(v_phi)), bins=100, histtype='step',
             color='b', range=(-5, 1), label=r'$\log v_{\phi}$', lw=2)
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


def show_object_and_shape(object):
    print(f'{object= } \n {object.shape= }')


if print_vp_vn:
    show_object_and_shape(v_rp_arr)
    show_object_and_shape(v_rn_arr)
    show_object_and_shape(v_thetap_arr)
    show_object_and_shape(v_thetan_arr)
    show_object_and_shape(v_phip_arr)
    show_object_and_shape(v_phin_arr)
    show_object_and_shape(v_tp_arr)
    show_object_and_shape(v_tn_arr)

if Fig8_vspherical_hist_log_vpvn:
    f = plt.figure()
    plt.xlabel(r'$\log v_rp, \log v_{\theta}p$,\
                 $\log v_{\phi}p$, $\log v_rn, \log v_{\theta}n$\
                 and $\log v_{\phi}n$')
    plt.ylabel('Number of particles')
    plt.title(f'Positive and negative f(v)\
              ($N= {len(x) : %.3f$}, $\gamma={Gamma: .1f$},\
              File = {F: %s})')

    plt.hist(np.log10(v_thetap_arr), bins=100, histtype='step', color='r',
             range=(-5, 1), label=r'$\log v_{\theta}p$', lw=2)
    plt.hist(np.log10(v_phip_arr), bins=100, histtype='step', color='m',
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

    show_object_and_shape(x1)
    show_object_and_shape(x2)
    show_object_and_shape(x3)

    print(f'{x4.shape= }'
          f'{v_thetap_arr.shape= }'
          f'{v_thetan_arr.shape= }'
          f'{x5.shape= }'
          f'{x6.shape= }'
          f'{type(x1)= }')

if Fig9_VPhiminus:  # test VPhi and VPhiminus = -VPhi
    VPhiminus = sp.sin(Phi) * vx - sp.cos(Phi) * vy
    f = plt.figure()
    plt.subplot(121)
    plt.xlabel(r'$v_{\phi}$, $-v_{\phi}$, $\log |v_{\phi}|$ and $\log|-v_{\phi}|$')
    plt.ylabel('Number of particles')
    plt.title(r'f(v) comparison ($N=%.3f$, $\gamma=%.1f$, File=%s)' % (len(x), Gamma, F))
    plt.hist(VPhi, bins=100, histtype='step', color='r',
             range=(-5, 1), label=r'$v_{\phi}$', lw=2)
    plt.hist(VPhiminus, bins=100, histtype='step', color='c',
             range=(-5, 1), label=r'$-v_{\phi}$', lw=2)
    plt.hist(np.log10(np.absolute(VPhi)), bins=100, histtype='step',
             color='g', range=(-5, 1), label=r'$\log |v_{\phi}|$', lw=2)
    plt.hist(np.log10(np.absolute(VPhiminus)), bins=100, histtype='step',
             color='b', range=(-5, 1), label=r'$\log |-v_{\phi}|$', lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
    plt.subplot(122)
    plt.xlabel(r'$\log v_rp + \log |v_rn|$, $\log v_{\theta}p\
               + \log|v_{\theta}n|$ and $\log v_{\phi}p + \log |v_{\phi}n|$')
    plt.ylabel('Number of particles')
    plt.title('Positive and negative f(v) summed')
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
    (VR_sigmaR_p, VR_sigmaR_n, VTheta_sigmatheta_p, VTheta_sigmatheta_n,
     VPhi_sigmaphi_p, VPhi_sigmaphi_n, VT_sigmaT_p, VT_sigmaT_n) =\
        ([] for i in range(8))

    for i in range(len(k := VR_sigmaR)):
        VR_sigmaR_p.append(k[i]) if k[i] >= 0. else VR_sigmaR_n.append(k[i])
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
        VT_sigmaT_p.append(VT_sigmaT[i]) if VT_sigmaT[i] >= 0. else VT_sigmaT_n.append(VT_sigmaT[i])
    VT_sigmaT_p_arr = np.asarray(VT_sigmaT_p)
    VT_sigmaT_n_arr = np.asarray(VT_sigmaT_n)

    (VR_i_avg_in_bin_sigmaR_p, VR_i_avg_in_bin_sigmaR_n,
     VT_i_avg_in_bin_sigmaT_p, VT_i_avg_in_bin_sigmaT_n,
     VPhi_i_avg_in_bin_sigmaphi_p, VPhi_i_avg_in_bin_sigmaphi_n,
     VTheta_i_avg_in_bin_sigmatheta_p, VTheta_i_avg_in_bin_sigmatheta_n) =\
     ([] for i in range(8))

    for i in range(len(k := VR_i_avg_in_bin_sigmaR)):
        if k[i] >= 0.:
            VR_i_avg_in_bin_sigmaR_p.append(k[i])
        else:
            VR_i_avg_in_bin_sigmaR_n.append(k[i])
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
    show_object_and_shape(VR_sigmaR_p_arr)
    show_object_and_shape(VR_sigmaR_n_arr)
    show_object_and_shape(VTheta_sigmatheta_p_arr)
    show_object_and_shape(VTheta_sigmatheta_n_arr)
    show_object_and_shape(VPhi_sigmaphi_p_arr)
    show_object_and_shape(VPhi_sigmaphi_n_arr)
    show_object_and_shape(VT_sigmaT_p_arr)
    show_object_and_shape(VT_sigmaT_n_arr)
    # VTheta = np.array(VTheta)
    # VPhi = np.array(VPhi)
    # VR_sigmaR = np.array(VR_sigmaR)
    # VTheta_sigmatheta = np.array(VTheta_sigmatheta)
    # VPhi_sigmaphi = np.array(VPhi_sigmaphi)
    if print_sigma_binned_lin_radius:
        show_object_and_shape(sigmaR2)
        show_object_and_shape(sigmatheta2)
        show_object_and_shape(sigmaphi2)
        show_object_and_shape(sigmaR)
        show_object_and_shape(sigmatheta)
        show_object_and_shape(sigmaphi)
        show_object_and_shape(VR)
        show_object_and_shape(VTheta)
        show_object_and_shape(VPhi)
        print(f'{(VR / sigmaR).shape= }',
              f'{(VR / sigmaR)= }',
              f'{np.where(sigmaR == 0)= }',
              f'{np.where(sigmatheta == 0)= }',
              f'{np.where(sigmaphi == 0)= }')

if Fig10_concatenate_x789:
    # check new log, concatenate lists x1 and x4, x2 and x5, x3 and x6.
    x7 = np.asarray(x1 + list(np.absolute(v_thetan_arr)))
    x8 = np.asarray(x2 + list(np.absolute(v_phin_arr)))
    x9 = np.asarray(x3 + list(np.absolute(v_rn_arr)))

    f = plt.figure()
    ax = f.add_subplot(121)
    n, bins, patches = plt.hist(VR, 100, histtype='step', color='r',
                                label=r'$v_r$', alpha=.75)
    n, bins, patches = plt.hist(VTheta, 100, histtype='step', color='b',
                                label=r'$v_{\theta}$', alpha=.75)
    n, bins, patches = plt.hist(VPhi, 100, histtype='step', color='g',
                                label=r'$v_{\phi}$', alpha=.75)
    plt.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\beta = %.2f$, File = %s)' % (len(x), Beta, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.grid()
    ax.set_yscale('log')

    ax = f.add_subplot(122)
    n, bins, patches = plt.hist(np.log10(x7), bins=100, histtype='step',
                                color='r', range=(-5, 1),
                                label=r'$\log(|v_{\theta}n|,v_{\theta}p)$', lw=2)
    n, bins, patches = plt.hist(np.log10(x8), bins=100, histtype='step',
                                color='b', range=(-5, 1),
                                label=r'$\log (|v_{\phi}n|,v_{\phi}p)$', lw=2)
    n, bins, patches = plt.hist(np.log10(x9), bins=100, histtype='step',
                                color='g', range=(-5, 1),
                                label=r'$\log (|v_rn|,v_rp)$', lw=2)
    plt.xlabel(r'$\log (|v_rn|,v_rp)$, $\log (|v_{\theta}n|,v_{\theta}p)$\
               and $\log (|v_{\phi}n|,v_{\phi}p)$')
    plt.ylabel('Number of particles')
    plt.title(r'$f(\log (|v_n|,v_p)) $')
    plt.grid()
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

if Fig11_vspherical_hist_log_n123:
    f, (ax1, ax2) = plt.subplots(1, 2)
    # (mu, sigma) = norm.fit(VR)
    n, bins, patches = ax1.hist(VR, 100, histtype='step', color='r',
                                label=r'$v_r$', alpha=.75)
    # (mu, sigma) = norm.fit(VTheta)
    n, bins, patches = ax1.hist(VTheta, 100, histtype='step', color='b',
                                label=r'$v_{\theta}$', alpha=.75)
    # (mu, sigma) = norm.fit(VPhi)
    n, bins, patches = ax1.hist(VPhi, 100, histtype='step', color='g',
                                label=r'$v_{\phi}$', alpha=.75)
    ax1.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    ax1.ylabel(r'$\log$ number of particles')
    ax1.title(r'f(v) ($N=%i$, $\gamma=%.2f$, File=%s)' % (len(x), Gamma, F))
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    ax1.grid()
    ax1.set_yscale('log')

    n1 = np.absolute(x4) + x1
    n2 = np.absolute(x5) + x2
    n3 = np.absolute(x6) + x3
    # (mu, sigma) = norm.fit(np.log10(n3))
    n, bins, patches = ax2.hist(np.log10(n3), 100, histtype='step', color='r',
                                label=r'$\log (v_rp + |v_rn|)$', alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n1))
    n, bins, patches = ax2.hist(np.log10(n1), 100, histtype='step', color='b',
                                label=r'$\log (v_{\theta}p + |v_{\theta}n|)$',
                                alpha=.75)
    # (mu, sigma) = norm.fit(np.log10(n2))
    n, bins, patches = ax2.hist(np.log10(n2), 100, histtype='step', color='g',
                                label=r'$\log (v_{\phi}p + |v_{\phi}n|)$',
                                alpha=.75)
    ax2.xlabel(r'$\log (v_{\theta}p + |v_{\theta}n|)$, $\log (v_{\phi}p +\
               |v_{\phi}n|)$ and $\log (v_rp + |v_rn|)$')
    ax2.ylabel('number of particles')
    ax2.title('Positive and negative f(v) summed')
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
    ax2.grid()

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

    f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    n, bins, patches = ax1.hist(np.log10(n3) / np.linalg.norm(VR), 100,
                                histtype='step', color='r',
                                label=r'$\frac{f(\log (v_rp +\
                                |v_rn|))}{||v_r||}$', alpha=.75)
    n, bins, patches = ax1.hist(np.log10(n1) / np.linalg.norm(VTheta), 100,
                                histtype='step', color='b',
                                label=r'$\frac{f(\log (v_{\theta}p +\
                                |v_{\theta}n|))}{||v_{\theta}||}$', alpha=.75)
    n, bins, patches = ax1.hist(np.log10(n2) / np.linalg.norm(VPhi), 100,
                                histtype='step', color='g',
                                label=r'$\frac{f(\log (v_{\phi}p +\
                                |v_{\phi}n|))}{||v_{\phi}||}$', alpha=.75)
    ax1.xlabel(r'$\frac{\log (v_rp + |v_rn|)}{||v_r||}$,\
               $\frac{\log (v_{\theta}p + |v_{\theta}n|)}{||v_{\theta}||}$\
               and $\frac{\log (v_{\phi}p + |v_{\phi}n|)}{||v_{\phi}||}$')
    ax1.ylabel(r'$f \left( \frac{\log (v_p + |v_n|)}{||v||}\right)$')
    ax1.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax2.hist(VR / np.linalg.norm(normTXT_r_arr), 100,
                                histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = ax2.hist(VTheta / np.linalg.norm(normTXT_theta_arr), 100,
                                histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                      {\sigma_{\theta}}\right)$', alpha=.75)
    n, bins, patches = ax2.hist(VPhi / np.linalg.norm(normTXT_phi_arr), 100,
                                histtype='step', color='g',
                                label=r'$f\left(\frac{v_{\phi}}\
                                      {\sigma_{\phi}}\right)$', alpha=.75)
    ax2.xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$')
    ax2.ylabel(r'$f\left(u\right)$')
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax3.hist(np.log10(n3), 100, histtype='step', color='r',
                                label=r'$f(\log (v_rp + |v_rn|))$', alpha=.75)
    n, bins, patches = ax3.hist(np.log10(n1), 100, histtype='step', color='b',
                                label=r'$f(\log\
                                (v_{\theta}p + |v_{\theta}n|))$', alpha=.75)
    n, bins, patches = ax3.hist(np.log10(n2), 100, histtype='step', color='g',
                                label=r'$f(\log(v_{\phi}p+|v_{\phi}n|))$', alpha=.75)
    ax3.xlabel(r'$\log (v_rp + |v_rn|)$, $\log (v_{\theta}p +\
               |v_{\theta}n|)$ and $\log (v_{\phi}p + |v_{\phi}n|)$')
    ax3.ylabel(r'$f(\log (v_p + |v_n|))$')
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax4.hist(np.log10(n3 / np.linalg.norm(normTXT_r_arr)),
                                100, histtype='step', color='r',
                                label=r'$f\left(\log \left( \frac{v_rp +\
                                      |v_rn|}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = ax4.hist(np.log10(n1 / np.linalg.norm(normTXT_theta_arr)),
                                100, histtype='step', color='b',
                                label=r'$f\left(\log \left( \frac{v_{\theta}p \
                                      + |v_{\theta}n|}\
                                      {\sigma_{\theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = ax4.hist(np.log10(n2 / np.linalg.norm(normTXT_phi_arr)),
                                100, histtype='step', color='g',
                                label=r'$f\left(\log \left( \frac{v_{\phi}p +\
                                      |v_{\phi}n|}\
                                      {\sigma_{\phi}}\right)\right)$',
                                alpha=.75)
    ax4.xlabel(r'$\log \left( u_rp + |u_rn| \right)$,\
               $\log \left( u_{\theta}p + |u_{\theta}n| \right)$\
               and $\log \left( u_{\phi}p + |u_{\phi}n| \right)$')
    ax4.ylabel(r'$f\left(\log \left( u_p + |u_n| \right)\right)$')
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

if Fig12_x789_sigma:
    x7 = np.asarray(x1 + list(np.absolute(v_thetan_arr)))
    x8 = np.asarray(x2 + list(np.absolute(v_phin_arr)))
    x9 = np.asarray(x3 + list(np.absolute(v_rn_arr)))
    txt = Filename.strip('.hdf5') + 'Sigma.txt'
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

    f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    n, bins, patches = ax1.hist(np.log10(x9) / np.linalg.norm(VR), 100,
                                histtype='step', color='r', range=(-.1, .0),
                                label=r'$f\left(\frac{\log (|v_rn|,\
                                      v_rp))}{||v_r||} \right)$', alpha=.75)
    n, bins, patches = ax1.hist(np.log10(x7) / np.linalg.norm(VTheta), 100,
                                histtype='step', color='b', range=(-.1, .0),
                                label=r'$f\left(\frac{\log\
                                      (|v_{\theta}n|, v_{\theta}p))}\
                                      {||v_{\theta}||} \right)$', alpha=.75)
    n, bins, patches = ax1.hist(np.log10(x8) / np.linalg.norm(VPhi), 100,
                                histtype='step', color='g', range=(-.1, .0),
                                label=r'$f\left( \frac{\log\
                                      (|v_{\phi}n|, v_{\phi}p))}\
                                      {||v_{\phi}||} \right)$', alpha=.75)
    ax1.xlabel(r'$\frac{\log (|v_rn|, v_rp)}{||v_r||}$,\
               $\frac{\log(|v_{\theta}n|, v_{\theta}p)}{||v_{\theta}||}$\
               and $\frac{\log (|v_{\phi}n|, v_{\phi}p)}{||v_{\phi}||}$')
    ax1.ylabel(r'$f \left(\frac{\log (|v_n|, v_p)}{||v||}\right)$')
    ax1.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax2.hist(VR / np.linalg.norm(normTXT_r_arr), 100,
                                histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = ax2.hist(VTheta / np.linalg.norm(normTXT_theta_arr), 100,
                                histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                      {\sigma_{\theta}}\right)$', alpha=.75)
    n, bins, patches = ax2.hist(VPhi / np.linalg.norm(normTXT_phi_arr), 100,
                                histtype='step', color='g',
                                label=r'$f\left(\frac{v_{\phi}}\
                                      {\sigma_{\phi}}\right)$', alpha=.75)
    ax2.xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$')
    ax2.ylabel(r'$f\left(u\right)$')
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax3.hist(np.log10(x9), 100, histtype='step',
                                color='r', range=(-3, 0),
                                label=r'$f(\log (|v_rn|,v_rp))$', alpha=.75)
    n, bins, patches = ax3.hist(np.log10(x7), 100, histtype='step',
                                color='b', range=(-3, 0),
                                label=r'$f(\log (|v_{\theta}n|,v_{\theta}p))$',
                                alpha=.75)
    n, bins, patches = ax3.hist(np.log10(x8), 100, histtype='step',
                                color='g', range=(-3, 0),
                                label=r'$f(\log (|v_{\phi}n|,v_{\phi}p))$',
                                alpha=.75)
    ax3.xlabel(r'$\log (|v_rn|, v_rp)$, $\log (|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|, v_{\phi}p)$')
    ax3.ylabel(r'$f(\log (|v_n|, v_p))$')
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax4.hist(np.log10(x9 / np.linalg.norm(normTXT_r_arr)), 100,
                                histtype='step', color='r', range=(-3, 0),
                                label=r'$f\left(\log \left(\frac{|v_rn|,\
                                      v_rp}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = ax4.hist(np.log10(x7 / np.linalg.norm(normTXT_theta_arr)),
                                100, histtype='step', color='b',
                                range=(-3, 0),
                                label=r'$f\left(\log \left(\
                                      \frac{|v_{\theta}n|,v_{\theta}p}\
                                      {\sigma_{\theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = ax4.hist(np.log10(x8 / np.linalg.norm(normTXT_phi_arr)),
                                100, histtype='step', color='g',
                                range=(-3, 0),
                                label=r'$f\left(\log \left(\frac{|v_{\phi}n|,\
                                      v_{\phi}p}{\sigma_{\phi}}\
                                      \right)\right)$', alpha=.75)
    ax4.xlabel(r'$\log \left(|u_rn|,u_rp \right)$, $\log \left(|u_{\theta}n|\
               , u_{\theta}p\right)$ and $\log\left(|u_{\phi}n|,\
               u_{\phi}p \right)$')
    ax4.ylabel(r'$f\left(\log\left(|u_n|,u_p\right)\right)$')
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

if Fig12_vr_vtheta_vphi_vt_sigma:
    v_rpn = np.asarray(list(v_rp_arr) + list(np.absolute(v_rn_arr)))
    v_thetapn = np.asarray(list(v_thetap_arr)
                           + list(np.absolute(v_thetan_arr)))
    v_phipn = np.asarray(list(v_phip_arr) + list(np.absolute(v_phin_arr)))
    v_tpn = np.asarray(list(v_tp_arr) + list(np.absolute(v_tn_arr)))
    x7 = np.asarray(list(VTheta_sigmatheta_p_arr)
                    + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_sigmaphi_p_arr)
                    + list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_sigmaR_p_arr)
                    + list(np.absolute(VR_sigmaR_n_arr)))
    x10 = np.asarray(list(VT_sigmaT_p_arr)
                     + list(np.absolute(VT_sigmaT_n_arr)))

    f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    n, bins, patches = ax1.hist(np.log10(v_rpn) / np.linalg.norm(VR), 100,
                                histtype='step', color='r', range=(-.1, .0),
                                label=r'$f\left(\frac{\log (|v_rn|, v_rp)}\
                                      {||v_r||}\right)$', alpha=.75)
    n, bins, patches = ax1.hist(np.log10(v_thetapn) / np.linalg.norm(VTheta), 100,
                                histtype='step', color='b', range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_{\theta}n|,\
                                      v_{\theta}p))}{||v_{\theta}||} \right)$',
                                alpha=.75)
    n, bins, patches = ax1.hist(np.log10(v_phipn) / np.linalg.norm(VPhi), 100,
                                histtype='step', color='g',
                                range=(-.1, .0),
                                label=r'$f\left( \frac{\log (|v_{\phi}n|,\
                                      v_{\phi}p))}{||v_{\phi}||} \right)$',
                                alpha=.75)
    (mu, sigma) = norm.fit(np.log10(v_rpn) / np.linalg.norm(VR))
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func1Log, xdata, ydata)
    y_fit = func1Log(xdata, popt[0], popt[1])
    ax1.plot(xdata, y_fit, 'c--', lw=3, label=r'$\frac{\log(v_r)}{||v_r||}-fit\
             =a\cdot log(x)\cdot e^{-b\cdot log(x)^2}$')
    ax1.xlabel(r'$\frac{\log (|v_rn|,v_rp)}{||v_r||}$, $\frac{\log\
               (|v_{\theta}n|,v_{\theta}p)}{||v_{\theta}||}$ and $\frac{\log\
               (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    ax1.ylabel(r'$f \left( \frac{\log (|v_n|,v_p)}{||v||}\right)$')
    ax1.title(r'$N=%i$, $\gamma = %.2f$, File = %s' % (len(x), Gamma, F))
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax2.hist(VR_sigmaR, 100, histtype='step', color='r',
                                label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',
                                alpha=.75)
    n, bins, patches = ax2.hist(VTheta_sigmatheta, 100,
                                histtype='step', color='b',
                                label=r'$f\left(\frac{v_{\theta}}\
                                      {\sigma_{\theta}}\right)$', alpha=.75)
    n, bins, patches = ax2.hist(VPhi_sigmaphi, 100, histtype='step', color='g',
                                label=r'$f\left(\frac{v_{\phi}}\
                                      {\sigma_{\phi}}\right)$', alpha=.75)
    (mu, sigma) = norm.fit(VR_sigmarad)
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func2, xdata, ydata)
    y_fit = func2(xdata, popt[0], popt[1])
    ax2.plot(xdata, y_fit, 'm--', lw=3,
             label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')
    ax2.xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$')
    ax2.ylabel(r'$f\left(u\right)$')
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax3.hist(np.log10(v_rpn), 100, histtype='step',
                                color='r', range=(-3, 0),
                                label=r'$f(\log (|v_rn|,v_rp))$', alpha=.75)
    n, bins, patches = ax3.hist(np.log10(v_thetapn), 100, histtype='step',
                                color='b', range=(-3, 0),
                                label=r'$f(\log (|v_{\theta}n|,v_{\theta}p))$',
                                alpha=.75)
    n, bins, patches = ax3.hist(np.log10(v_phipn), 100, histtype='step',
                                color='g', range=(-3, 0),
                                label=r'$f(\log (|v_{\phi}n|,v_{\phi}p))$',
                                alpha=.75)
    (mu, sigma) = norm.fit(np.log10(v_rpn))
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func1Log, xdata, ydata)
    y_fit = func1Log(xdata, popt[0], popt[1])
    ax3.plot(xdata, y_fit, 'm--', lw=3,
             label=r'$\log(v_r)-fit = a\cdot log(x)\cdot\
                     e^{-b \cdot log(x)^2}$')
    ax3.xlabel(r'$\log (|v_rn|, v_rp)$, $\log(|v_{\theta}n|,\
               v_{\theta}p)$ and $\log (|v_{\phi}n|, v_{\phi}p)$')
    ax3.ylabel(r'$f(\log (|v_n|,v_p))$')
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

    n, bins, patches = ax4.hist(np.log10(x9), 100, histtype='step', color='r',
                                range=(-3, 1), label=r'$f\left(\log \left(\
                                \frac{|v_rn|, v_rp}{\sigma_r}\right)\right)$',
                                alpha=.75)
    n, bins, patches = ax4.hist(np.log10(x7), 100, histtype='step',
                                color='b', range=(-3, 1),
                                label=r'$f\left(\log \left(\
                                      \frac{|v_{\theta}n|, v_{\theta}p}\
                                      {\sigma_{\theta}}\right)\right)$',
                                alpha=.75)
    n, bins, patches = ax4.hist(np.log10(x8), 100, histtype='step',
                                color='g', range=(-3, 1),
                                label=r'$f\left(\log \left(\frac{|v_{\phi}n|,\
                                      v_{\phi}p}{\sigma_{\phi}}\
                                      \right)\right)$', alpha=.75)
    (mu, sigma) = norm.fit(np.log10(x9))
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func1Log, xdata, ydata)
    y_fit = func1Log(xdata, popt[0], popt[1])
    ax4.plot(xdata, y_fit, 'm--', lw=3,
             label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit=\
                   a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
    ax4.xlabel(r'$\log \left( |u_rn|,u_rp \right)$,\
               $\log \left(|u_{\theta}n|,u_{\theta}p \right)$\
               and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
    ax4.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
               frameon=True, loc=2, handlelength=2.5)

if Fig13_vspherical_hist_old:
    f = plt.figure()
    (mu, sigma) = norm.fit(v_t_arr[6])  # best fit of data
    n, bins, patches = plt.hist(v_t_arr[6], 100, normed=1, color='g', alpha=.75)
    xdata = get_xdata(bins)
    ydata = n
    popt, pcov = curve_fit(func1, xdata, ydata)
    y_fit = func1(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, 'b--', lw=3)
    plt.xlabel(r'$v_t$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    plt.grid()
    x = np.array((xdata, ydata))
    x = x.transpose()
    print('x.shape:', x.shape)
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFt.txt', x, delimiter=' ',
               header='\t bins \t\t n')

    f = plt.figure()
    (mu, sigma) = norm.fit(v_r_arr[6])
    n, bins, patches = plt.hist(v_r_arr[6], 100, normed=1, color='g', alpha=.75)
    # add a 'best fit' line
    # y = mlab.normpdf(bins, mu, sigma)
    # l = plt.plot(bins, y, 'r--', linewidth=2)
    xdata = get_xdata(bins)
    popt, pcov = curve_fit(func2, xdata, n)
    y_fit = func2(xdata, popt[0], popt[1], popt[2])
    plt.plot(xdata, y_fit, 'b--', lw=3)
    plt.xlabel(r'$v_r$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    plt.grid()
    x = np.array((xdata, n)).transpose()
    print(f'{x.shape= }')
    np.savetxt('HQ10000_G1.2_9_005_bin6_VDFr.txt', x, delimiter=' ',
               header='\t bins \t\t n')

if save_r_v_as_txt:
    x = np.array((xcl2, ycl2, zcl2, vxnew2, vynew2, vznew2)).transpose()
    print(f'{x.shape= }')
    np.savetxt('HQ10000_G1.2_9_005_bin0_05to0_25kpc_VDF.txt', x, delimiter=' ',
               header=' xcl2 \t ycl2 \t zcl2 \t vxnew2 \t vynew2 \t vznew2')

plt.show()
