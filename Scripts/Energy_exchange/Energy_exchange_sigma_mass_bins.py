# -*- coding: utf-8 -*-

import h5py
import numpy as np
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
from pylab import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import scipy as sp
import seaborn as sns
import matplotlib.patches as mpatches
from pathlib import Path
from Attractor.Sigma_calc_OOP import get_volume_slice

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
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_20_005.hdf5'
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
# F = 'B' + Filename[len(GADGET_E_path + Soft_B_path + 'B'):-5]
# F = 'B' + Filename[len(GADGET_E_path + con_Soft_B_path + 'B'):-5]
# F = 'CS1' + Filename[len(GADGET_E_path + CS1_path + 'B'):-5]
# F = 'CS1' + Filename[len(GADGET_E_path + con_CS1_path + 'B'):-5]
# F = 'CS4' + Filename[len(GADGET_E_path + CS4_path + 'B'):-5]
# F = 'CS4' + Filename[len(GADGET_E_path + con_CS4_path + 'B'):-5]
# F = 'CS5' + Filename[len(GADGET_E_path + CS5_path + 'B'):-5]
# F = 'CS5' + Filename[len(GADGET_E_path + con_CS5_path + 'B'):-5]
# F = 'CS6' + Filename[len(GADGET_E_path + CS6_path + 'B'):-5]
# F = 'CS6' + Filename[len(GADGET_E_path + con_CS6_path + 'B'):-5]
# F = 'DS1' + Filename[len(GADGET_E_path + DS1_path + 'B'):-5]
# F = 'DS1' + Filename[len(GADGET_E_path + con_DS1_path + 'B'):-5]
# F = 'D2' + Filename[len(GADGET_E_path + D2_path + 'B'):-5]
# F = 'D2' + Filename[len(GADGET_E_path + con_D2_path + 'B'):-5]
# F = 'E' + Filename[len(GADGET_E_path + E_path + 'B'):-5]
# F = 'E' + Filename[len(GADGET_E_path + con_E_path + 'B'):-5]

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
R = ravf.modulus(x - xC, y - yC, z - zC)
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

if CS1 or CS2 or CS3:
    N_particles_per_bin = 500
elif CS4 or CS5 or CS6 or DS1 or D2:
    N_particles_per_bin = 5000
elif B or E: 
    N_particles_per_bin = 50000

N_bins = N_total / N_particles_per_bin

(sigma2_arr, sigmarad2_arr, sigmatheta2_arr, sigmaphi2_arr,
 sigmatan2_arr, v2_arr, gamma_arr, kappa_arr, beta_arr,
 density_arr, Volume_arr, r, Phi, Theta, VR, VTheta, VPhi,
 VR_i_avg_in_bin, bin_radius_arr) = ([] for i in range(19))

# Divide structure into mass-bins. Favoured over radial bins, as outer region of structure has less particles.
for i in range(N_bins):
    GoodIDs = np.arange(i * N_particles_per_bin, (i + 1) * N_particles_per_bin)
    x_GoodIDs = x_IDs[GoodIDs]
    y_GoodIDs = y_IDs[GoodIDs]
    z_GoodIDs = z_IDs[GoodIDs]
    vx_GoodIDs = vx_IDs[GoodIDs]
    vy_GoodIDs = vy_IDs[GoodIDs]
    vz_GoodIDs = vz_IDs[GoodIDs]
    V_GoodIDs = V_IDs[GoodIDs]  # Shape: 500
    R_min = R_IDs[GoodIDs][0]
    R_max = R_IDs[GoodIDs][-1]
    v = ravf.modulus(vx_GoodIDs, vy_GoodIDs, vz_GoodIDs)
    
    # sigma2 total
    v2_in_bin_i = v ** 2
    sigma2_in_bin_i = (1. / (N_particles_per_bin + 1.)) * np.sum(v2_in_bin_i)
    sigma2_arr.append(sigma2_in_bin_i)
    bin_radius_arr.append((R_max + R_min) / 2)

    # sigmarad2 radial
    v_r = (vx_GoodIDs * x_GoodIDs + vy_GoodIDs * y_GoodIDs + vz_GoodIDs * z_GoodIDs)
           / ravf.modulus(x_GoodIDs, y_GoodIDs, z_GoodIDs)
    vrad2_in_bin_i = v_r ** 2
    sigmarad2_in_bin_i = (1. / (N_particles_per_bin + 1.)) * np.sum(vrad2_in_bin_i)
    sigmarad2_arr.append(sigmarad2_in_bin_i)

    # calculate volume of cluster:
    Volume_cl = get_volume_slice(R_min, R_max)
    # density
    den_cl = N_particles_per_bin / Volume_cl
 
    r_i = ravf.modulus(x_GoodIDs, y_GoodIDs, z_GoodIDs)
    Phi_i = sp.arctan2(y_GoodIDs, x_GoodIDs)
    Theta_i = sp.arccos(z_GoodIDs / r_i)
    VR_i = sp.sin(Theta_i) * sp.cos(Phi_i) * vx_GoodIDs + sp.sin(Theta_i)
           * sp.sin(Phi_i) * vy_GoodIDs + sp.cos(Theta_i) * vz_GoodIDs
    VTheta_i = sp.cos(Theta_i) * sp.cos(Phi_i) * vx_GoodIDs + sp.cos(Theta_i)
               * sp.sin(Phi_i) * vy_GoodIDs - sp.sin(Theta_i) * vz_GoodIDs
    VPhi_i = -sp.sin(Phi_i) * vx_GoodIDs + sp.cos(Phi_i) * vy_GoodIDs
    VR_i_avg_in_bin_i = (1. / (N_particles_per_bin + 1.)) * np.sum(VR_i)

    # sigmatheta2
    VTheta2_in_bin_i = VTheta_i ** 2
    sigmatheta2_in_bin_i = (1. / (N_particles_per_bin + 1.)) * np.sum(VTheta2_in_bin_i)
    sigmatheta2_arr.append(sigmatheta2_in_bin_i)

    # sigmaphi2
    VPhi2_in_bin_i = VPhi_i ** 2
    sigmaphi2_in_bin_i = (1. / (N_particles_per_bin + 1.)) * np.sum(VPhi2_in_bin_i)
    sigmaphi2_arr.append(sigmaphi2_in_bin_i)

    # sigmatan2
    sigmatan = (sigmatheta2_in_bin_i + sigmaphi2_in_bin_i) ** .5
    sigmatan2 = sigmatan ** 2
    sigmatan2_arr.append(sigmatan2)

    # save arrays
    density_arr.append(den_cl)
    Volume_arr.append(Volume_cl)
    r.append(r_i)
    Phi.append(Phi_i)
    Theta.append(Theta_i)
    VR.append(VR_i)
    VR_i_avg_in_bin.append(VR_i_avg_in_bin_i)
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
VR_i_avg_in_bin_arr = np.array(VR_i_avg_in_bin)

for i in range(len(sigma2_arr)):  # kappa
    if i == 0 or i == len(sigma2_arr) - 1:
        kappa_arr.append(np.nan)
        continue
    dlogr = np.log10(bin_radius_arr[i + 1]) - np.log10(bin_radius_arr[i - 1])
    dlogsigmarad2 = np.log10(sigmarad2_arr[i + 1]) - np.log10(sigmarad2_arr[i - 1])
    kappa_arr.append(dlogsigmarad2 / dlogr)

for i in range(len(density_arr)):  # gamma
    if i == 0 or i == len(sigma2_arr) - 1:
        gamma_arr.append(np.nan)
        continue
    dlogr = np.log10(bin_radius_arr[i + 1]) - np.log10(bin_radius_arr[i - 1])
    dlogrho = np.log10(density_arr[i + 1]) - np.log10(density_arr[i - 1])
    gamma_arr.append(dlogrho / dlogr)

beta_arr = 1. - sigmatheta2_arr / sigmarad2_arr  # Calculate beta

if Fig_beta:  # plot beta
    f = plt.figure()
    # plt.xlim(-1.7, 2.0)
    plt.ylim(-1.5, 1.5)
    x_plot = np.log10(bin_radius_arr)
    y_plot = beta_arr
    plt.xlabel(r'$\log$r (kpc)', fontsize=20)
    plt.ylabel(r'$\beta$', fontsize=20)
    # from this graph we see that beta is below zero. this means sigmatheta2_arr/sigmarad2_arr > 1,
    # which in turn means that sigmatheta2_arr > sigmarad2_arr. 
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0, label=r'$\beta$')
    plt.plot(x_plot, 0 * x_plot, '--', lw=2, color='grey')
    plt.grid()

    if Fig_betafit:  # fitting beta with two different profiles
        x = 10 ** x_plot
        y_plot = x ** 2 / (25 ** 2 + x ** 2)
        plt.plot(x_plot, y_plot, 'b-', ms=2, mew=0, label=r'$\frac{x^2}{25^2+x^2}$') 

        Chi2 = 0
        i = 0 
        while (i < len(beta_arr)):
          Chi2 += ((beta_arr[i] - y_plot[i]) ** 2) / (beta_arr[i] * .2) ** 2
          i += 1         
        Chi2 = (1.0 / (len(beta_arr) - 1)) * Chi2
        print('Chi2 for betafit: ', Chi2)

        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey', label= r'$\chi^2 = %.6f$' % Chi2)
        leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=2,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        plt.title(r'$\beta$ with fit. mass bins (%s)' % F, fontsize=18)
        # f.savefig(figure_path + 'B_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_control_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS1_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_control_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS4_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_control_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS5_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_control_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS6_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_control_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'DS1_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_control_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'D2_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_control_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'E_IC_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_beta_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_control_beta_logr_fit_mass_bins.png')
    else:
        plt.title(r'$\beta$ with zero-line(%s)' % F, fontsize=18)
        # f.savefig(figure_path + 'B_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_control_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS1_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_control_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS4_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_control_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS5_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_control_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS6_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_control_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'DS1_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_control_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'D2_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_control_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'E_IC_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_beta_logr_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_control_beta_logr_mass_bins.png')

if Fig_kappa:
    f = plt.figure()
    x_plot = np.log10(bin_radius_arr)
    y_plot = kappa_arr
    plt.xlabel(r'$\log $r', fontsize=20)
    plt.ylabel(r'$\kappa$', fontsize=20)
    plt.title(r'$\kappa$ and zero-line. mass bins (%s)'% F, fontsize=18)
    plt.plot(x_plot, y_plot, 'k-o', ms=4, mew=0)
    plt.plot(x_plot, 0 * x_plot, '--', lw=2, color='grey')
    # f.savefig(figure_path + 'B_kappa_mass_bins.png')
    # f.savefig(figure_path + 'CS1_kappa_mass_bins.png')
    # f.savefig(figure_path + 'CS4_kappa_mass_bins.png')
    # f.savefig(figure_path + 'CS5_kappa_mass_bins.png')
    # f.savefig(figure_path + 'CS6_kappa_mass_bins.png')
    # f.savefig(figure_path + 'DS1_kappa_mass_bins.png')
    # f.savefig(figure_path + 'D2_kappa_mass_bins.png')
    # f.savefig(figure_path + 'E_kappa_mass_bins.png')

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
        plt.plot(x_plot, y_plot, 'b-', ms=2, mew=0, label='Fit')  # label=r'$\frac{x^2}{23^2+x^2}$'

        Chi2 = 0
        i = 0
        while (i < len(gamma_arr)):
            # if gamma_arr[i] == nan :
            if isnan(gamma_arr[i]):
                # continue
                print('nan at index: ', i)
            else:
                Chi2 += ((gamma_arr[i] - y_plot[i]) ** 2) / (gamma_arr[i] * .2) ** 2
            i += 1
        Chi2 = (1.0 / (len(gamma_arr) - 1)) * Chi2
        # print('Chi2 for gammafit: ', Chi2)

        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',label = r'$\chi^2 = %.6f$' % Chi2)
        leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=2,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        plt.title('Radial density slope with fit. mass bins (%s)' % F, fontsize=18)
        # f.savefig(figure_path + 'B_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_control_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS1_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_control_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS4_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_control_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS5_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_control_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS6_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_control_gamma_logr_fit_mass_bins.png')             
        # f.savefig(figure_path + 'DS1_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_control_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'D2_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_control_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'E_IC_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_gamma_logr_fit_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_control_gamma_logr_fit_mass_bins.png')
    else:
        plt.title(f'Radial density slope {F}', fontsize=18)
        # f.savefig(figure_path + 'B_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'B_Final_control_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS1_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS1_Final_control_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS4_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS4_Final_control_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS5_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS5_Final_control_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS6_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'CS6_Final_control_gamma_logr_mass_bins.png')             
        # f.savefig(figure_path + 'DS1_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'DS1_Final_control_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'D2_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'D2_Final_control_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'E_IC_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_gamma_logr_mass_bins.png')
        # f.savefig(figure_path + 'E_Final_control_gamma_logr_mass_bins.png')

if Fig_betagamma:
    f = plt.figure()
    subplot(121)
    plt.xlabel(r'$\beta$', fontsize=20)
    plt.ylabel(r'$\gamma$', fontsize=20)
    plt.title(r'$\gamma$ vs $\beta$ (%s)' % F, fontsize=18)
    plt.plot(beta_arr, gamma_arr, 'k-o', ms=2, mew=0)
    plt.grid()
    subplot(122)
    plt.xlabel(r'$\beta$', fontsize=20)
    plt.ylabel(r'$\kappa$', fontsize=20)
    plt.title(r'$\kappa$ vs $\beta$', fontsize=20)
    plt.plot(beta_arr, kappa_arr, 'k-o', ms=2, mew=0)
    plt.grid()
    
    # f.savefig(figure_path + 'B_betagamma_mass_bins.png')
    # f.savefig(figure_path + 'CS1_betagamma_mass_bins.png')
    # f.savefig(figure_path + 'CS4_betagamma_mass_bins.png')
    # f.savefig(figure_path + 'CS5_betagamma_mass_bins.png')
    # f.savefig(figure_path + 'CS6_betagamma_mass_bins.png')
    # f.savefig(figure_path + 'DS1_betagamma_mass_bins.png')
    # f.savefig(figure_path + 'D2_betagamma_mass_bins.png')
    # f.savefig(figure_path + 'E_betagamma_mass_bins.png')

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

    x = np.array((logr_arr, beta_arr, gamma_arr, kappa_arr, VR_i_avg_in_bin_arr, r_arr, sigmarad2_arr))
    x = x.transpose()
    out_name = text_files_path + F + '_mass_bins.txt'
    np.savetxt(out_name, x, delimiter=' ')

plt.show()
