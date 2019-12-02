# -*- coding: utf-8 -*-

# Standard library imports
import h5py
from pathlib import Path
import time

# Third party imports
import IPython
from matplotlib.colors import LogNorm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import scipy as sp
from scipy.optimize import curve_fit
from scipy.stats import norm
import seaborn as sns

# Local application imports
from Attractor.Sigma_calc_OOP import (get_volume_slice, vr_cartesian,
                                      vr_spherical, theta_velocity,
                                      phi_velocity, chi_2, beta, gamma, kappa)

User_path = Path.cwd()
Desktop_path = User_path + 'Desktop/'
GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/'
Stable_path = 'Energy_exchange/Stable_structures/'
figure_path = Desktop_path + Stable_path + 'figures/'
text_files_path = Desktop_path + Stable_path + 'text_files/'

Soft_B_path = 'E_HQ_1000000_B/output/'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_20_005.hdf5'
CS1_path = 'E_HQ_10000_CS1/output/'
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_20_005.hdf5'
CS4_path = 'E_HQ_100000_CS4/output/'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_20_005.hdf5'
CS5_path = 'E_HQ_100000_CS5/output/'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_20_005.hdf5'
CS6_path = 'E_HQ_100000_CS6/output/'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_20_005.hdf5'
DS1_path = 'E_0_5_100000_DS1/output/'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_20_005.hdf5'
D2_path = 'E_0_5_100000_D2/output/'
# Filename = GADGET_E_path + D2_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + D2_path + 'B_E_G2P_20_005.hdf5'
E_path = 'E_HQ_1000000_E/output/'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_20_005.hdf5'

# Control
con_Soft_B_path = 'E_HQ_1000000_B_control/output/'
con_Soft_B_snaps = ['0_000', '0_001', '20_005']
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_' + con_Soft_B_snaps[0]
#            + '.hdf5'
con_CS1_path = 'E_HQ_10000_CS1_control/output/'
# Filename = GADGET_E_path + con_CS1_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS1_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS1_path + 'B_E_20_005.hdf5'
con_CS4_path = 'E_HQ_100000_CS4_control/output/'
# Filename = GADGET_E_path + con_CS4_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS4_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS4_path + 'B_E_20_005.hdf5'
con_CS5_path = 'E_HQ_100000_CS5_control/output/'
# Filename = GADGET_E_path + con_CS5_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS5_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS5_path + 'B_E_20_005.hdf5'
con_CS6_path = 'E_HQ_100000_CS6_control/output/'
# Filename = GADGET_E_path + con_CS6_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS6_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS6_path + 'B_E_20_005.hdf5'
con_DS1_path = 'E_0_5_100000_DS1_control/output/'
# Filename = GADGET_E_path + con_DS1_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_DS1_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_DS1_path + 'B_E_20_005.hdf5'
con_D2_path = 'E_0_5_100000_D2_control/output/'
# Filename = GADGET_E_path + con_D2_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_D2_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_D2_path + 'B_E_20_005.hdf5'
con_E_path = 'E_HQ_1000000_E_control/output/'
# Filename = GADGET_E_path + con_E_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_E_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_E_path + 'B_E_20_005.hdf5'

SnapshotFile = h5py.File(Filename, 'r')

sims = ['B', 'CS1', 'CS4', 'CS5', 'CS6', 'DS1', 'D2', 'E']
paths = [Soft_B_path, con_Soft_B_path, CS1_path, con_CS1_path,
         CS4_path, con_CS4_path, CS5_path, con_CS5_path,
         CS6_path, con_CS6_path, DS1_path, con_DS1_path,
         D2_path, con_D2_path, E_path, con_E_path]
# F = sims[0] + Filename[len(GADGET_E_path + paths[0] + 'B'):-5]

Fig_beta = 0
Fig_betafit = 0
Fig_kappa = 0
Fig_gamma = 0
Fig_gammafit = 0
Fig_betagamma = 0
save_lnr_beta_gamma_kappa_VR_r_sigma_r = 0

B = 0
CS1 = 0
CS2 = 0
CS3 = 0
CS4 = 0
CS5 = 0
CS6 = 0
DS1 = 0
D2  = 0
E = 0

Pos = SnapshotFile['PartType1/Coordinates'].value
Vel = SnapshotFile['PartType1/Velocities'].value
V = SnapshotFile['PartType1/Potential'].value
x = Pos[:, 0]
y = Pos[:, 1]
z = Pos[:, 2]
vx = Vel[:, 0]
vy = Vel[:, 1]
vz = Vel[:, 2]
minV = np.argmin(V)  # Finds the particle with the lowest potential (which is in the center of the largest cluster)
xC = x[minV]  # Changes x, y and z so that the cluster is centered.
yC = y[minV]
zC = z[minV]
vxC = vx[minV]
vyC = vy[minV]
vzC = vz[minV]
R = modulus(x - xC, y - yC, z - zC)
vx -= np.median(vx)
vy -= np.median(vy)
vz -= np.median(vz)
IDs = np.argsort(R)
x_IDs = x[IDs]
y_IDs = y[IDs]
z_IDs = z[IDs]
vx_IDs = vx[IDs]
vy_IDs = vy[IDs]
vz_IDs = vz[IDs]
R_IDs = R[IDs]
V_IDs = V[IDs]

N_total = x.shape[0]
N_bins = N_total / N_particles_per_bin


def nr_par_bin_filter():
    if CS1 or CS2 or CS3:
        nr_par_bin = 500  # Number of particles per bin.
    elif CS4 or CS5 or CS6 or DS1 or D2:
        nr_par_bin = 5_000
    elif B or E:
        nr_par_bin = 50_000
    return nr_par_bin


nr_par_bin = nr_par_bin_filter()

(sigma2_arr, sigmarad2_arr, sigmatheta2_arr, sigmaphi2_arr,
 sigmatan2_arr, v2_arr, gamma_arr, kappa_arr, beta_arr,
 density_arr, Volume_arr, r, Phi, Theta, VR, VTheta, VPhi,
 VR_i_avg_in_bin, bin_radius_arr) = ([] for i in range(19))

# Divide structure into mass-bins. Favoured over radial bins, as outer region of structure has less particles.
for i in range(N_bins):
    GoodIDs = np.arange(i * nr_par_bin, (i + 1) * nr_par_bin)

    x = x_IDs[GoodIDs]
    y = y_IDs[GoodIDs]
    z = z_IDs[GoodIDs]
    vx = vx_IDs[GoodIDs]
    vy = vy_IDs[GoodIDs]
    vz = vz_IDs[GoodIDs]
    V = V_IDs[GoodIDs]  # Shape: 500

    R_min = R_IDs[GoodIDs][0]
    R_max = R_IDs[GoodIDs][-1]
    v = modulus(vx, vy, vz)
    v2_i = v ** 2  # sigma2 total
    sigma2_i = mean_velocity_slice(nr_par_bin, v2_i)
    v_r = vr_cartesian(x, y, z, vx, vy, vz)
    vrad2_i = v_r ** 2
    sigmarad2_i = mean_velocity_slice(nr_par_bin, vrad2_i)  # sigmarad2 radial
    Volume_cl = get_volume_slice(R_min, R_max)  # Volume of cluster
    den_cl = nr_par_bin / Volume_cl  # density
    r_i = modulus(x, y, z)
    Phi_i = sp.arctan2(y, x)
    Theta_i = sp.arccos(z / r_i)
    VR_i = vr_spherical(Theta_i, Phi_i, vx, vy, vz)
    VTheta_i = theta_velocity(Theta_i, Phi_i, vx, vy, vz)
    VPhi_i = phi_velocity(Phi_i, vx, vy)
    VR_i_avg_in_bin_i = mean_velocity_slice(nr_par_bin, VR_i)
    VTheta2_i = VTheta_i ** 2  # sigmatheta2
    sigmatheta2_i = mean_velocity_slice(nr_par_bin, VTheta2_i)
    VPhi2_i = VPhi_i ** 2  # sigmaphi2
    sigmaphi2_i = mean_velocity_slice(nr_par_bin, VPhi2_i)
    sigmatan = (sigmatheta2_i + sigmaphi2_i) ** .5  # sigmatan2
    sigmatan2 = sigmatan ** 2

    # save arrays
    sigma2_arr.append(sigma2_i)
    bin_radius_arr.append((R_max + R_min) / 2)
    sigmarad2_arr.append(sigmarad2_i)
    sigmatheta2_arr.append(sigmatheta2_i)
    sigmaphi2_arr.append(sigmaphi2_i)
    sigmatan2_arr.append(sigmatan2)
    density_arr.append(den_cl)
    Volume_arr.append(Volume_cl)
    r.append(r_i)
    Phi.append(Phi_i)
    Theta.append(Theta_i)
    VR.append(VR_i)
    VR_i_avg_in_bin.append(VR_i_avg_i)
    VTheta.append(VTheta_i)
    VPhi.append(VPhi_i)

# Change the nesessary lists into arrays
sigma2_arr = np.array(sigma2_arr)  # square of total velocity dispersion
sigmarad2_arr = np.array(sigmarad2_arr)
bin_radius_arr = np.array(bin_radius_arr)
r_arr = np.array(r)
Phi_arr = np.array(Phi)
Theta_arr = np.array(Theta)
VR_arr = np.array(VR)
VTheta_arr = np.array(VTheta)
VPhi_arr = np.array(VPhi)
VR_i_avg_arr = np.array(VR_i_avg_i)

# Set beta
sigmatheta2 = sigmatheta2_arr
sigmarad2 = sigmarad2_arr
beta_arr = beta()

# Set kappa
radii = bin_radius_arr
sigma_r2 = sigmarad2_arr
kappa_arr = kappa(sigma2_arr)

# Set gamma
density = density_arr
gamma_arr = gamma(sigma2_arr)

sims = ['B', 'CS1', 'CS4', 'CS5', 'CS6', 'DS1', 'D2', 'E']
mode = ['IC', 'Final', 'Final_control']

if Fig_beta:  # plot beta
    f = plt.figure()
    # plt.xlim(-1.7, 2.0)
    plt.ylim(-1.5, 1.5)
    x_plot = np.log10(bin_radius_arr)
    y_plot = beta_arr
    plt.xlabel(r'$\log$r (kpc)', fontsize=20)
    plt.ylabel(r'$\beta$', fontsize=20)
    # from this graph we see that beta is below zero. this means
    # sigmatheta2_arr/sigmarad2_arr > 1,
    # which in turn means that sigmatheta2_arr > sigmarad2_arr.
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0, label=r'$\beta$')
    plt.plot(x_plot, 0 * x_plot, '--', lw=2, color='grey')
    plt.grid()

    if Fig_betafit:  # fitting beta with two different profiles
        x = 10 ** x_plot
        y_plot = x ** 2 / (25 ** 2 + x ** 2)
        plt.plot(x_plot, y_plot, 'b-', ms=2, mew=0, label=r'$\frac{x^2}{25^2+x^2}$')

        Chi2 = chi_2(beta_arr)
        print('Chi2 for betafit: ', Chi2)

        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey', label= r'$\chi^2 = %.6f$' % Chi2)
        leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=2,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        plt.title(r'$\beta$ with fit. mass bins (%s)' % F, fontsize=18)

        f.savefig(figure_path + sims[0] + '_' + mode[0] + '_'
                  + 'beta_logr_fit_mass_bins.png')
    else:
        plt.title(r'$\beta$ with zero-line(%s)' % F, fontsize=18)
        f.savefig(figure_path + sims[0] + '_' + mode[0] + '_'
                  + 'beta_logr_mass_bins.png')

if Fig_kappa:
    f = plt.figure()
    x_plot = np.log10(bin_radius_arr)
    y_plot = kappa_arr
    plt.xlabel(r'$\log $r', fontsize=20)
    plt.ylabel(r'$\kappa$', fontsize=20)
    plt.title(r'$\kappa$ and zero-line. mass bins (%s)'% F, fontsize=18)
    plt.plot(x_plot, y_plot, 'k-o', ms=4, mew=0)
    plt.plot(x_plot, 0 * x_plot, '--', lw=2, color='grey')
    f.savefig(figure_path + sims[0] + '_kappa_mass_bins.png')

if Fig_gamma:
    f = plt.figure()
    x_plot = np.log10(bin_radius_arr)
    y_plot = gamma_arr
    plt.xlabel(r'$\log $r', fontsize=20)
    plt.ylabel(r'$\gamma$', fontsize=20)
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0, label=r'$\gamma$')
    plt.grid()
    plt.ylim(-6., 0.)

    if Fig_gammafit:
        x = 10 ** x_plot
        y_plot = -1 -3 * x / (1 + x)
        plt.plot(x_plot, y_plot, 'b-', ms=2, mew=0, label='Fit')
        # label=r'$\frac{x^2}{23^2+x^2}$'
        Chi2 = chi_2()
        # print('Chi2 for gammafit: ', Chi2)
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',label = r'$\chi^2 = %.6f$' % Chi2)
        leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=2,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        plt.title('Radial density slope with fit. mass bins (%s)' % F,
                  fontsize=18)
        f.savefig(figure_path + sims[0] + '_' + mode[0] + '_'
                  + 'gamma_logr_fit_mass_bins.png')
    else:
        plt.title(f'Radial density slope {F}', fontsize=18)
        f.savefig(figure_path + sims[0] + '_' + mode[0] + '_'
                  + 'gamma_logr_mass_bins.png')

if Fig_betagamma:
    f, (ax1, ax2) = plt.subplots(2, 1)
    ax1.xlabel(r'$\beta$', fontsize=20)
    ax1.ylabel(r'$\gamma$', fontsize=20)
    ax1.title(r'$\gamma$ vs $\beta$ (%s)' % F, fontsize=18)
    ax1.plot(beta_arr, gamma_arr, 'k-o', ms=2, mew=0)
    ax1.grid()
    ax2.xlabel(r'$\beta$', fontsize=20)
    ax2.ylabel(r'$\kappa$', fontsize=20)
    ax2.title(r'$\kappa$ vs $\beta$', fontsize=20)
    ax2.plot(beta_arr, kappa_arr, 'k-o', ms=2, mew=0)
    ax2.grid()
    f.savefig(figure_path + sims[0] + '_' + 'B_betagamma_mass_bins.png')

if save_lnr_beta_gamma_kappa_VR_r_sigma_r:
    logr_arr = np.array(np.log10(bin_radius_arr))
    beta_arr = np.array(beta_arr)
    gamma_arr = np.array(gamma_arr)
    kappa_arr = np.array(kappa_arr)
    r_arr = 10 ** (logr_arr)
    sigmarad2_arr = np.array(sigmarad2_arr)
    GoodIDs = np.where(gamma_arr == gamma_arr)
    logr_arr = logr_arr[GoodIDs]
    gamma_arr = gamma_arr[GoodIDs]
    beta_arr = beta_arr[GoodIDs]
    kappa_arr = kappa_arr[GoodIDs]
    r_arr = r_arr[GoodIDs]
    sigmarad2_arr = sigmarad2_arr[GoodIDs]
    VR_i_avg_in_bin_arr = VR_i_avg_in_bin_arr[GoodIDs]

    x = np.array((logr_arr, beta_arr, gamma_arr, kappa_arr,
                  VR_i_avg_in_bin_arr, r_arr, sigmarad2_arr))
    x = x.transpose()
    out_name = text_files_path + F + '_mass_bins.txt'
    np.savetxt(out_name, x, delimiter=' ')

plt.show()
