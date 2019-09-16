# -*- coding: utf-8 -*-

import h5py
from pathlib import Path
import time

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

from Attractor.Sigma_calc_OOP import chi_2, get_volume_slice, beta, gamma, kappa
from Gammas_and_R_middles import R_bin_automatic

User_path = Path.cwd()
Stable_path = 'Energy_exchange/Stable_structures/'
Desktop_path = User_path + 'Desktop/'

sims_II = ['a', 'b', 'c', 'd']
# GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/II' + sims_II[0] + '/'
# figure_path = Desktop_path + Stable_path + 'figures/II' + sims_II[0] + '/'

# IIa
sims = ['Soft_B', 'CS1', 'CS4', 'CS5', 'CS6', 'DS1', 'Soft_D2', 'E',
        'Test_CS4', 'Test_D2', 'Test_CS4_10tdyn']
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/' + sims[0]
#                   + '/'  # All sims

# IIb
# text_files_path = Desktop_path + Stable_path + 'text_files/IIb/' + sims[2]
#                   + '/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIb/Soft_D2/'

# IIc
# text_files_path = Desktop_path + Stable_path + 'text_files/IIc/' + sims[2]
#                   + '/'  # sims[3], sims[4], sims[5], sims[6]

# IId
# text_files_path = Desktop_path + Stable_path + 'text_files/IId/CS4/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IId/Soft_D2/'

Soft_B_path = 'E_HQ_1000000_B/output/'
Soft_B_snaps = ['0_000', '0_005', '1_000', '2_005', '4_005', '6_005', '8_005',
                '10_005', '20_005']
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_' + Soft_B_snaps[0]
#            + '.hdf5'

CS1_path = 'E_HQ_10000_CS1/output/'
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_20_005.hdf5'

CS4_path = 'E_HQ_100000_CS4/output/'
CS4_snaps = ['0_005', '10_005', '20_013', '20_021', '30_005', '40_021']
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_' + CS4_snaps[0] + '.hdf5'

CS5_path = 'E_HQ_100000_CS5/output/'
CS5_snaps = ['0_005', '2_005', '4_005', '6_005', '8_005', '10_005', '20_021',
             '30_005', '40_021']
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_' + CS5_snaps[0] + '.hdf5'

CS6_path = 'E_HQ_100000_CS6/output/'
CS6_snaps = ['0_005', '2_005', '4_005', '6_005', '8_005', '10_005', '20_021',
             '30_005', '40_021']
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_' + CS6_snaps[0] + '.hdf5'

DS1_path = 'E_0_5_100000_DS1/output/'
DS1_snaps = ['0_005', '2_005', '4_005', '6_005', '8_005', '10_005', '20_005',
             '30_005', '40_021', '60_021']
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_' + DS1_snaps[0] + '.hdf5'

Soft_D2_path = 'E_0_5_100000_D2/output/'
Soft_D2_snaps = ['0_005', '10_005', '20_013', '20_021', '30_021', '40_021',
                 '60_021']
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_' + Soft_D2_snaps[0]
#            + '.hdf5'

E_path = 'E_HQ_1000000_E/output/'
E_snaps = ['0_005', '2_005', '4_005', '6_005', '8_005', '10_005', '20_005',
           '30_005', '40_021']
# Filename = GADGET_E_path + E_path + 'B_E_G2P_' + E_snaps[0] + '.hdf5'

Test_CS4_path = 'Test_CS4/output/'
# Filename = GADGET_E_path + Test_CS4_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + 'Test_CS4/' + 'B_E_0_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_CS4_path + 'B_E_G2P_1_005.hdf5'
# Filename = GADGET_E_path + 'Test_CS4/' + 'B_E_1_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_CS4_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + 'Test_CS4/' + 'B_E_2_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_CS4_path + 'B_E_G2P_3_005.hdf5'
# Filename = GADGET_E_path + 'Test_CS4/' + 'B_E_3_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_CS4_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + 'Test_CS4/' + 'B_E_4_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_CS4_path + 'B_E_G2P_5_005.hdf5'
# Filename = GADGET_E_path + 'Test_CS4/' + 'B_E_5_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_CS4_path + 'B_E_G2P_6_005.hdf5'

Test_D2_path = 'Test_D2/output/'
# Filename = GADGET_E_path + Test_D2_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + 'Test_D2/' + 'B_E_0_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_D2_path + 'B_E_G2P_1_005.hdf5'
# Filename = GADGET_E_path + 'Test_D2/' + 'B_E_1_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_D2_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + 'Test_D2/' + 'B_E_2_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_D2_path + 'B_E_G2P_3_005.hdf5'
# Filename = GADGET_E_path + 'Test_D2/' + 'B_E_3_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_D2_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + 'Test_D2/' + 'B_E_4_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_D2_path + 'B_E_G2P_5_005.hdf5'
# Filename = GADGET_E_path + 'Test_D2/' + 'B_E_5_005_P2G.hdf5'
# Filename = GADGET_E_path + Test_D2_path + 'B_E_G2P_6_005.hdf5'

Test_CS4_10tdyn_path = 'Test_CS4_10tdyn/output/'
Test_CS4_10tdyn_snaps = ['0_005', '1_041', '2_041', '3_041']
# Filename = GADGET_E_path + Test_CS4_10tdyn_path + 'B_E_G2P_' + Test_CS4_10tdyn_snaps[0] + '.hdf5'

# Control
con_Soft_B_path = 'E_HQ_1000000_B_control/output/'
con_Soft_B_snaps = ['0_000', '0_001', '10_005', '20_005']
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_' + con_Soft_B_snaps[0] + '.hdf5'

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
con_Soft_D2_path = 'E_0_5_100000_D2_control/output/'
# Filename = GADGET_E_path + con_Soft_D2_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_Soft_D2_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_Soft_D2_path + 'B_E_20_005.hdf5'
con_E_path = 'E_HQ_1000000_E_control/output/'
# Filename = GADGET_E_path + con_E_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_E_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_E_path + 'B_E_20_005.hdf5'

SnapshotFile = h5py.File(Filename, 'r')

# IIa
# F = 'Soft_B' + Filename[len(GADGET_E_path + Soft_B_path + 'B'):-5]
# F = 'Soft_B' + Filename[len(GADGET_E_path + con_Soft_B_path + 'B'):-5]
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
# F = 'Soft_D2' + Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5]
# F = 'Soft_D2' + Filename[len(GADGET_E_path + con_Soft_D2_path + 'B'):-5]
# F = 'E' + Filename[len(GADGET_E_path + E_path + 'B'):-5]
# F = 'E' + Filename[len(GADGET_E_path + con_E_path + 'B'):-5]
# F = 'Test_CS4' + Filename[len(GADGET_E_path + Test_CS4_path + 'B'):-5]
# F = 'Test_CS4' + Filename[len(GADGET_E_path + 'Test_CS4/' + 'B'):-5]
# F = 'Test_D2' + Filename[len(GADGET_E_path + Test_D2_path + 'B'):-5]
# F = 'Test_D2' + Filename[len(GADGET_E_path + 'Test_D2/' + 'B'):-5]
# F = 'Test_CS4_10tdyn' + Filename[len(GADGET_E_path + Test_CS4_10tdyn_path + 'B'):-5]

# IIb
# F = 'IIb_CS4' + Filename[len(GADGET_E_path + CS4_path + 'B'):-5]
# F = 'IIb_Soft_D2' + Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5]

# IIc
# F = 'IIc_CS4' + Filename[len(GADGET_E_path + CS4_path + 'B'):-5]
# F = 'IIc_CS4_no_K_ratio' + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F = 'IIc_CS4_unbound' + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F = 'IIc_CS4_no_rand' + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F = 'IIc_CS4_car_sph_car' + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F = 'IIc_Test_CS4' + Filename[len(GADGET_E_path + 'Test_CS4_path/' + 'B'):-5]
# F = 'IIc_Test_CS4' + Filename[len(GADGET_E_path + 'Test_CS4/' + 'B'):-5]
# F = 'IIc_CS5' + Filename[len(GADGET_E_path + CS5_path + 'B'):-5]
# F = 'IIc_CS6' + Filename[len(GADGET_E_path + CS6_path + 'B'):-5]
# F = 'IIc_DS1' + Filename[len(GADGET_E_path + DS1_path + 'B'):-5]
# F = 'IIc_Soft_D2' + Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5]
# F = 'IIc_Soft_D2' + Filename[len(GADGET_E_path + 'E_0_5_100000_D2/' + 'B'):-5]

# IId
# F = 'IId_CS4' + Filename[len(GADGET_E_path + CS4_path + 'B'):-5]
# F = 'IId_Soft_D2'+ Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5]

Gamma = -2.0
Beta = 1.0

keep_IC_R_middle = 0
new_R_middle = 0
R_bin_automatic = 0

bins_202 = 0
bins_102 = 0
bins_52 = 0
# Reduce number of radial bins in analysis code.
# This makes them larger and they therefore contain more particles.
bins_22 = 0

R_limit_10000 = 0  # Analyse larger volume of structure, sets R_limit to 10000.
R_limit_5000 = 0
R_limit_50 = 0
R_limit_32 = 0

Fig_vx_x = 0
Fig_v_logr = 0
Fig_x_hist = 0
Fig_x_hist2d = 0
Fig4_beta = 0
Fig4_betafit = 0
Fig5_kappa = 0
Fig6_gamma = 0
Fig6_gammafit = 0
Fig7_betagamma = 0
save_lnr_beta_gamma_kappa_VR_r_sigma_r_r2_rho = 0

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
# xC = np.median(x[V.argsort()[0:100]])  # Changes x, y and z so that the cluster is centered.
# yC = np.median(y[V.argsort()[0:100]])
# zC = np.median(z[V.argsort()[0:100]])
# R = ravf.modulus(x - xC, y - yC, z - zC)
# R = ravf.modulus(x, y, z)

if R_limit_10000:
    R_limit = 10000.
    F += '_R_limit_10000'
elif R_limit_5000:
    R_limit = 5000.
    F +='_R_limit_5000'
elif R_limit_50:
    R_limit = 50.
    F += '_R_limit_50'
elif R_limit_32:
    R_limit = 32.
    F += '_R_limit_32'
else:
    R_limit = 10.
    F += '_R_limit_10'

# GoodIDs = np.where(R < R_limit)  # Removes all particles that is far away from the cluster.

if R_bin_automatic:  # make R_limit_min and R_limit_max selection automatic
    R_limit_min, R_limit_max = R_bin_automatic(R_middle, x, R)

if Fig_x_hist:
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.set_xlabel(r'$x-x_c$', fontsize=30)
    n, bins, patches = ax1.hist(x - xC, 500, normed=1, histtype='stepfilled')
    plt.setp(patches, 'facecolor', 'g', 'alpha', .75)
    ax1.set_xlim(-40, 40)
    ax1.set_ylim(.0, .4)
    ax2.set_xlabel(r'$y-y_c$', fontsize=30)
    n, bins, patches = ax2.hist(y - yC, 500, normed=1, histtype='stepfilled')
    plt.setp(patches, 'facecolor', 'g', 'alpha', .75)
    ax2.set_title('Histograms of centralized positions', fontsize=30)
    ax2.set_xlim(-40, 40)
    ax2.set_ylim(.0, .4)
    ax2.tick_params(axis='both', which='both', bottom='on', top='off',
                    labelbottom='on', right='off', left='off', labelleft='off')
    ax3.set_xlabel(r'$z-z_c$', fontsize=30)
    n, bins, patches = ax3.hist(z - zC, 500, normed=1, histtype='stepfilled')
    plt.setp(patches, 'facecolor', 'g', 'alpha', .75)
    ax3.set_xlim(-40, 40)
    ax3.set_ylim(.0, .4)
    # ax3.axes.get_yaxis().set_visible(False)
    ax3.tick_params(axis='both', which='both', bottom='on', top='off',
                    labelbottom='on', right='off', left='off', labelleft='off')
    f.savefig(figure_path + 'Fig_CS4_Final_x_hist.png')  # 'Fig_x_hist.png'

if Fig_x_hist2d:
    f = plt.figure(figsize=(13, 11))
    plt.xlabel(r'$x-x_c$', fontsize=30 )
    plt.ylabel(r'$y-y_c$', fontsize=30 )
    plt.hexbin(x - xC, y - yC, gridsize=500)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    sims = ['B', 'CS4', 'CS5', 'CS6', 'DS1', 'D2', 'E']
    plt.title(f'Centralized positions x and y ({sims[0]}, gridsize = 500)', fontsize=30)
    f.savefig(f'{figure_path}Fig_{sims[0]}_Final_x_hist2d.png')

x -= np.median(x)
y -= np.median(y)
z -= np.median(z)
R = ravf.modulus(x, y, z)
GoodIDs = np.where(R < R_limit)  # Removes all particles that is far away from the cluster.
x = x[GoodIDs]
y = y[GoodIDs]
z = z[GoodIDs]
vx = vx[GoodIDs]
vy = vy[GoodIDs]
vz = vz[GoodIDs]
vx -= np.median(vx)
vy -= np.median(vy)
vz -= np.median(vz)

R_hob_par = R[GoodIDs]

# Declare number of particles
if F.startswith(('Soft_B_', 'E_')):
    N = 10 ** 6
elif F.startswith(('CS4_', 'CS5_', 'CS6_', 'DS1_', 'Soft_D2_', 'IIc', 'IId', 'IId', 'Test_')):
    N = 10 ** 5
elif F.startswith('CS1_'):
    N = 10 ** 4
# Declare total mass
if F.startswith(('Soft_B_', 'CS1_', 'CS4_', 'CS5_', 'CS6_', 'E_', 'Test_', 'IIc_CS4_', 'IIc_CS5_', 'IIc_CS6_', 'IIc_Test_CS4', 'IId_CS4')):
    M = 1.
elif F.startswith(('DS1_', 'D2_', 'Soft_D2_', 'IIc_Soft_D2_', 'IIc_DS1_', 'IId_Soft_D2_')):
    M = 1. / 6.
# Define particle mass
m = M / N

if Gamma == -2.0:
    r_2 = R_middle
    posR_par_in_halo = np.where(R_hob_par < r_2)  # position of particles inside halo
    nr_par_in_halo = len(posR_par_in_halo[0])
    M_2 = nr_par_in_halo * m
    G = 1.
    v_circ_2 = (G * M_2 / r_2) ** .5
    # print('r_2 = ', r_2)
    # print('nr_par_in_halo = ', nr_par_in_halo)
    # print('M_2 = ', M_2)
    # print('v_circ_2 = ', v_circ_2)

if bins_202:
    nr_of_bins = 202
    F += '_200_radial_bins'
elif bins_102:
    nr_of_bins = 102
    F += '_100_radial_bins'
elif bins_52:
    nr_of_bins = 52
    F += '_50_radial_bins'
elif bins_22:
    nr_of_bins = 22
    F += '_20_radial_bins'
# print(F)

# GoodIDs = np.where(R < R_limit)  # Removes all particles that is far away from the cluster.
# R_hob_par = R[GoodIDs]

(bin_radius_arr, sigma2_arr, sigmarad2_arr, sigmatheta2_arr, sigmaphi2_arr, sigmatan2_arr,
 v2_arr, gamma_arr, kappa_arr, beta_arr, density_arr, rho_arr, Volume_arr,
 r, Phi, Theta, VR, VTheta, VPhi, VR_i_avg_in_bin) = ([] for i in range(20))

v_r = vr_cartesian(x, y, z, vx, vy, vz)
min_binning_R = -1.5
max_binning_R = np.log10(R_limit)
binning_arr_lin_log10 = np.logspace(min_binning_R, max_binning_R, nr_binning_bins)  # Array, -5-1000

for i in range(nr_binning_bins - 2):
    min_R_i = binning_arr_lin_log10[i]  # start of bin
    max_R_i = binning_arr_lin_log10[i + 1]  # end of bin
    posR_par_i = np.where((R_hob_par > min_R_i) & (R_hob_par < max_R_i))  # position of particles inside a radial bin
    nr_par_i = len(posR_par_i[0])  # number of particles inside a radial bin
    if nr_par_i == 0:
        continue

    x = x[posR_par_i]
    y = y[posR_par_i]
    z = z[posR_par_i]
    vx = vx[posR_par_i]
    vy = vy[posR_par_i]
    vz = vz[posR_par_i]

    v = ravf.modulus(vx, vy, vz)
    v2_i = v ** 2
    sigma2_i = mean_velocity_slice(nr_par_i, v2_i)  # sigma2 total
    vrad2_i = v_r[posR_par_in_bin_i] ** 2
    sigmarad2_i = mean_velocity_slice(nr_par_i, vrad2_i)  # sigmarad2 radial
    Volume_cl = get_volume_slice(min_R_i, max_R_i)  # Volume of cluster
    den_cl = nr_par_i / Volume_cl  # number density
    rho = den_cl * m  # density
    r_i = ravf.modulus(x, y, z)
    Phi_i = phi(x, y)
    Theta_i = theta(z, r_i)
    VR_i = vr_spherical(Theta_i, Phi_i, vx, vy, vz)
    VTheta_i = theta_velocity(Theta_i, Phi_i, vx, vy, vz)
    VPhi_i = phi_velocity(Phi_i, vx, vy)
    VR_i_avg_i = mean_velocity_slice(nr_par_i, VR_i)
    VTheta2_i = VTheta_i ** 2
    sigmatheta2_i = mean_velocity_slice(nr_par_i, VTheta2_i)  # sigmatheta2
    VPhi2_i = VPhi_i ** 2
    sigmaphi2_i = mean_velocity_slice(nr_par_i, VPhi2_i)  # sigmaphi2
    sigmatan = (sigmatheta2_i + sigmaphi2_i) ** .5
    sigmatan2 = sigmatan ** 2  # sigmatan2

    # save arrays
    sigma2_arr.append(sigma2_i)
    bin_radius_arr.append((max_R_i + min_R_i) / 2)
    sigmarad2_arr.append(sigmarad2_i)
    sigmatheta2_arr.append(sigmatheta2_i)
    sigmaphi2_arr.append(sigmaphi2_i)
    sigmatan2_arr.append(sigmatan2)
    density_arr.append(den_cl)
    rho_arr.append(rho)
    Volume_arr.append(Volume_cl)
    r.append(r_i)
    Phi.append(Phi_i)
    Theta.append(Theta_i)
    VR.append(VR_i)
    VR_i_avg_i.append(VR_i_avg_i)
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
rho_arr = np.array(rho_arr)

# Set kappa
radii = bin_radius_arr
sigma_r2 = sigmarad2_arr
kappa_arr = kappa(sigma2_arr)

# Set gamma
density = density_arr
gamma_arr = gamma(sigma2_arr)

# Set beta
sigmatheta2 = sigmatheta2_arr
sigmarad2 = sigmarad2_arr
beta_arr = beta()

if Fig_vx_x:
    f, (ax1) = plt.subplots(1, 1, figsize=(13, 11))
    ax1.set_xlabel(r'$\log x$', fontsize=30)
    ax1.set_ylabel(r'$\log v_x$', fontsize=30)
    ax1.plot(np.log10(x), np.log10(vx), 'bo', label='Soft B 0_005', lw=3, ms=2)  # label='Soft B 1_000'
    leg = ax1.legend(prop=dict(size=18), numpoints=1, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'II: $\Delta E,R_{lim}=10^4$', fontsize=30)
    f.savefig(figure_path + 'Soft_B_0_005_logvx_logx_II.png')  # 'Soft_B_1_000_logvx_logx_II'

if Fig_v_logr:
    r = ravf.modulus(x, y, z)
    v = ravf.modulus(vx, vy, vz)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.set_xlabel('r', fontsize=30)
    ax1.set_ylabel(r'total velocity, $v=\sqrt{v_x^2+v_y^2+v_z^2}$', fontsize=30)
    labels = ['Soft B IC', 'Soft B 10_005', 'Soft B 20_005', 'Soft B control IC',
              'Soft B control 10_005', 'Soft B control 20_005',
              r'$CS_4$ 2_005', r'$CS_4$ 2_005 perturbation', r'$CS_4$ 2_005 P2G (no K_ratio)',
              r'$CS_4$ 2_005 P2G (unbound)', r'$CS_4$ 2_005 P2G (no rand)',
              r'$CS_4$ 2_005 P2G (car sph car)']
    ax1.plot(r, v, 'bo', label=labels[-1], lw=3, ms=2)
    leg = ax1.legend(prop=dict(size=18), numpoints=1, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'IIc: $R_{lim}=32, 20$ bins', fontsize=30)
    ax2.plot(np.log10(r), v, 'bo', lw=3, ms=2)
    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.yaxis.tick_right()
    figtitles = ['Soft_B_IC_v_logr_II',
                 'Soft_B_10_005_v_logr_II',
                 'Soft_B_20_005_v_logr_II',
                 'Soft_B_control_IC_v_logr_II',
                 'Soft_B_control_10_005_v_logr_II',
                 'Soft_B_control_20_005_v_logr_II',
                 'CS4_2_005_v_logr_IIc',
                 'CS4_2_005_P2G_v_logr_IIc',
                 'CS4_2_005_P2G_no_K_ratio_v_logr_IIc',
                 'CS4_2_005_P2G_unbound_v_logr_IIc',
                 'CS4_2_005_P2G_no_rand_v_logr_IIc'
                 ]
    f.savefig(figure_path + figtitles[-1] + '.png')

if Fig4_beta:  # plot beta
    f = plt.figure(figsize=(13, 11))
    # plt.xlim(-1.7, 2.0)
    # plt.ylim(-1., 1.)
    x_plot = np.log10(bin_radius_arr)
    y_plot = beta_arr
    plt.xlabel(r'$\log$r', fontsize=30)
    plt.ylabel(r'$\beta$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0, label=r'$\beta$')  # from this graph we see that beta is below zero. this means sigmatheta2_arr/sigmarad2_arr > 1, which in turn means that sigmatheta2_arr > sigmarad2_arr.
    plt.plot(x_plot, 0 * x_plot, '--', lw=2, color='grey')

    if Fig4_betafit:  # fitting beta with two different profiles
        x = 10 ** x_plot
        y_plot = x ** 2 / (23. ** 2 + x ** 2)
        plt.plot(x_plot, y_plot, 'b-', ms=2, mew=0, label=r'$\frac{x^2}{23^2+x^2}$')
        Chi2 = Sigma_calc_OOP.chi_2(beta_arr)
        # print('Chi2 for betafit: ', Chi2)
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey', label=r'$\chi^2 = %.6f$' % Chi2)
        leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=2,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        plt.title(r'$\beta$ with fit (%s)' % F, fontsize=30)
        figtitles = ['B_IC', 'B_Final', 'B_Final_control', 'CS1_IC',
                     'CS1_Final', 'CS1_Final_control', 'CS4_IC',
                     'CS4_Final', 'CS4_Final_control', 'CS5_IC',
                     'CS5_Final', 'CS5_Final_control', 'CS6_IC',
                     'CS6_Final', 'CS6_Final_control', 'DS1_IC',
                     'DS1_Final', 'DS1_Final_control', 'D2_IC',
                     'D2_Final', 'D2_Final_control', 'E_IC',
                     'E_Final', 'E_Final_control'
                     ]
                     f.savefig(figure_path + figtitles[-1] + '_beta_logr_fit.png']
    else:
        # plt.title(r'$\beta$ with zero-line(%s)' % F, fontsize=30)
        sims = ['Soft_B', 'CS4', 'CS5', 'CS6', 'DS1', 'Soft_D2', 'E']
        # plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, (%s) final, $R_{limit}=10^4$, 20 bins)' % sims[-1], fontsize=30)  # all sims
        # plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, (%s) final, $R_{limit}=50$, 50 bins)', % sims[-1], fontsize=30)  # all sims
        # plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_B final, $R_{limit}=32$, 50 bins)', fontsize=30)
        # plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, (%s) final, $R_{limit}=32$, 20 bins)', % sims[1], fontsize=30)  # sims[1] to sims[-2]
        # plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, E final, $R_{limit}=32$, 50 bins)', fontsize=30)
        # plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, (%s) final, $R_{limit}=10$, 20 bins)', % sims[-1], fontsize=30)

        titles = ['Soft_B', 'CS1', 'CS4', 'CS5', 'CS6', 'DS1', 'Soft_D2', 'E']
        ext = ['IC', 'Final', 'Final_control']
        radii = ['10000', '50', '32', '10']
        f.savefig(figure_path + titles[0] + '_' + ext[0] + '_beta_logr_II_R' + radii[0] + '.png')

if Fig5_kappa:
    f = plt.figure(figsize=(13, 11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = kappa_arr
    plt.xlabel(r'$\log $r', fontsize=30)
    plt.ylabel(r'$\kappa$', fontsize=30)

    # plt.title(r'$\kappa$ and zero-line (%s)' % F, fontsize=30)

    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=10^4$, 20 bins)',fontsize=30)

    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=50$, 50 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=50$, 50 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=50$, 50 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=50$, 50 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=50$, 50 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=50$, 50 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=50$, 50 bins)',fontsize=30)

    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=32$, 50 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=32$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=32$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=32$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=32$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=32$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=32$, 50 bins)',fontsize=30)

    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=10$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=10$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=10$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=10$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10$, 20 bins)',fontsize=30)
    # plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=10$, 20 bins)',fontsize=30)

    plt.plot(x_plot, y_plot, 'k-o', ms=4, mew=0)
    plt.plot(x_plot, 0 * x_plot, '--', lw=2, color='grey')
    # f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R10000.png')
    # f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R10000.png')
    # f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R10000.png')
    # f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R10000.png')
    # f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R10000.png')
    # f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R10000.png')
    # f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R10000.png')
    # f.savefig(figure_path + 'E_Final_kappa_logr_II_R10000.png')

    # f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R50.png')
    # f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R50.png')
    # f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R50.png')
    # f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R50.png')
    # f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R50.png')
    # f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R50.png')
    # f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R50.png')
    # f.savefig(figure_path + 'E_Final_kappa_logr_II_R50.png')

    # f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R32.png')
    # f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R32.png')
    # f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R32.png')
    # f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R32.png')
    # f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R32.png')
    # f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R32.png')
    # f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R32.png')
    # f.savefig(figure_path + 'E_Final_kappa_logr_II_R32.png')

    # f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R10.png')
    # f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R10.png')
    # f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R10.png')
    # f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R10.png')
    # f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R10.png')
    # f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R10.png')
    # f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R10.png')
    # f.savefig(figure_path + 'E_Final_kappa_logr_II_R10.png')

if Fig6_gamma:
    f = plt.figure(figsize=(13, 11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = gamma_arr
    # plt.xlim(0., 1.6)
    plt.ylim(-3., -1.5)
    plt.xlabel(r'$\log $r', fontsize=30)
    plt.ylabel(r'$\gamma$', fontsize=30)
    plt.plot(x_plot, y_plot, 'k-o', ms=7, lw=2, mew=0, label=r'$\gamma$')

    if Fig6_gammafit:
        x = 10 ** x_plot
        y_plot = -1 - 3 * x / (1 + x)
        plt.plot(x_plot, y_plot, 'b-', ms=2, mew=0, label='Fit')  # label=r'$\frac{x^2}{23^2+x^2}$'

        Chi2 = Sigma_calc_OOP.chi_2()
        # print('Chi2 for gammafit: ', Chi2)

        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey', label=r'$\chi^2 = %.6f$' % Chi2)
        leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=2,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        plt.title('Radial density slope with fit (%s)' % F, fontsize=18)
        # f.savefig(figure_path + 'B_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'B_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'B_Final_control_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS1_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS1_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS1_Final_control_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS4_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS4_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS4_Final_control_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS5_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS5_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS5_Final_control_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS6_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS6_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'CS6_Final_control_gamma_logr_fit.png')
        # f.savefig(figure_path + 'DS1_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'DS1_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'DS1_Final_control_gamma_logr_fit.png')
        # f.savefig(figure_path + 'D2_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'D2_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'D2_Final_control_gamma_logr_fit.png')
        # f.savefig(figure_path + 'E_IC_gamma_logr_fit.png')
        # f.savefig(figure_path + 'E_Final_gamma_logr_fit.png')
        # f.savefig(figure_path + 'E_Final_control_gamma_logr_fit.png')
    else:
        # plt.title('Radial density slope (%s)' % F, fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=10^4$, 20 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, Soft_B final, $R_{limit}=50$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 final, $R_{limit}=50$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=50$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=50$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=50$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=50$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=50$, 50 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, B IC, $R_{limit}=32$, 50 bins)', fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, B 2_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, B 4_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, B 6_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, B 8_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, B 10_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, B final, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, B control final, $R_{limit}=32$, 50 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 IC, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 2_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 4_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 6_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 8_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 10_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim IIc, CS4 40_021, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 control final, $R_{limit}=32$, 20 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 IC, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 2_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 4_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 6_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 8_005, $R_{limit}=32$, 20 bins)', fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 10_005, $R_{limit}=32$, 20 bins)', fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=32$, 20 bins)', fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 control final, $R_{limit}=32$, 20 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 IC, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 2_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 4_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 6_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 8_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 10_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 control final, $R_{limit}=32$, 20 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 IC, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 2_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 4_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 6_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 8_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 10_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 control final, $R_{limit}=32$, 20 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 IC, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 2_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 4_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 6_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 8_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 10_005, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 final, $R_{limit}=32$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, D2 control final, $R_{limit}=32$, 20 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, E IC, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E 2_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E 4_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E 6_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E 8_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E 10_005, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=32$, 50 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E control final, $R_{limit}=32$, 50 bins)',fontsize=30)

        # plt.title('Radial density slope (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS4 final, $R_{limit}=10$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=10$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=10$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=10$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10$, 20 bins)',fontsize=30)
        # plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=10$, 20 bins)',fontsize=30)

        # f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS4_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'E_IC_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'E_Final_gamma_logr_II_R10000.png')
        # f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R10000.png')

        # f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS4_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'E_IC_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'E_Final_gamma_logr_II_R50.png')
        # f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R50.png')

        # f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R32.png')

        # f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS4_2_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS4_4_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS4_6_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS4_8_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS4_10_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS4_40_gamma_logr_IIc_R32.png')
        # f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R32.png')

        # f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS5_2_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS5_4_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS5_6_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS5_8_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS5_10_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R32.png')

        # f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS6_2_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS6_4_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS6_6_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS6_8_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS6_10_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R32.png')

        # f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'DS1_2_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'DS1_4_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'DS1_6_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'DS1_8_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'DS1_10_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R32.png')

        # f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_D2_2_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_D2_4_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_D2_6_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_D2_8_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_D2_10_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R32.png')

        # f.savefig(figure_path + 'E_IC_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'E_2_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'E_4_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'E_6_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'E_8_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'E_10_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'E_Final_gamma_logr_II_R32.png')
        # f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R32.png')

        # f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS4_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'E_IC_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'E_Final_gamma_logr_II_R10.png')
        # f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R10.png')

if Fig7_betagamma:
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

    sims = ['B', 'CS1', 'CS4', 'CS5', 'CS6', 'DS1', 'D2', 'E']

    f.savefig(figure_path + sims[-1] + '_betagamma.png')

if save_lnr_beta_gamma_kappa_VR_r_sigma_r_r2_rho:
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

    if Gamma == -2.0:
        r_r2_arr = r_arr / r_2
        # print('r_r2_arr = ', r_r2_arr)
        rho_arr = rho_arr[GoodIDs]
        x = np.array((logr_arr, beta_arr, gamma_arr, kappa_arr,
                      VR_i_avg_in_bin_arr, r_arr, sigmarad2_arr, r_r2_arr, rho_arr))
        x = x.transpose()
        out_name = text_files_path + F + '.txt'
        np.savetxt(out_name, x, delimiter=' ',
                   header='\t logr \t beta \t gamma \t kappa \t VR_avg \t r \t sigmarad2 \t r_r2 \t rho')
    else:
        rho_arr = rho_arr[GoodIDs]
        x = np.array((logr_arr, beta_arr, gamma_arr, kappa_arr,
                      VR_i_avg_in_bin_arr, r_arr, sigmarad2_arr, rho_arr))
        x = x.transpose()
        out_name = text_files_path + F + '.txt'
        np.savetxt(out_name, x, delimiter=' ',
                   header='\t logr \t beta \t gamma \t kappa \t VR_avg \t r \t sigmarad2 \t rho')
        # print('out_name = ', out_name)

plt.show()
