# -*- coding: utf-8 -*-

import h5py
import numpy as np
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
from pylab import *
import seaborn as sns
import os

UserPath = os.getcwd()
DesktopPath = UserPath + 'Desktop/'
GADGET_G_path = DesktopPath + 'RunGadget/G_perturbations/'
Stable_path = 'G_perturbations/Stable_structures/'
figure_path = Desktop_path + Stable_path + 'figures/'
text_files_path = Desktop_path + Stable_path + 'text_files/'
Martin_path = 'Martin_IC_and_Final_Edd_and_OM/'
hdf5_path = Desktop_path + 'G_perturbations/hdf5_files/'
nosync_path = User_path + 'nosync/RunGadget/'

# Filename = hdf5_path + '0G00_IC_000.hdf5'
# Filename = hdf5_path + '0G20_Final_000.hdf5'
# Filename = hdf5_path + 'OMG00_001_IC_000.hdf5'
# Filename = hdf5_path + 'OMG20_Final_000.hdf5'

# Filename = 'Hq1000000_150311_000.hdf5'
test_path = 'G_HQ_1000000_test/output/'
# Filename = GADGET_G_path + test_path + 'Hernquist10000_G0.8_2_000.hdf5'
# Filename = 'OsipkovMerritt_150310_000.hdf5'
A_path = 'G_HQ_1000000_A/output/'
#Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_5_005.hdf5'
#Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_40_005.hdf5'
#Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_48_009.hdf5'
#Filename = nosync_path + A_path + 'Hernquist10000_G1.0_48_093.hdf5'
B_path = 'G_HQ_1000000_B/output/'
Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_5_005.hdf5'
#Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_198_000.hdf5'
#Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_198_093.hdf5'
#Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_199_093.hdf5'
Soft_B_path = 'Soft_G_HQ_1000000_B/output/'
#Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_5_005.hdf5'
#Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_198_000.hdf5'
#Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_198_093.hdf5'
#Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_199_093.hdf5'
CS1_path  = 'G_HQ_10000_CS1/output/'
#Filename = GADGET_G_path + CS1_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS2_path  = 'G_HQ_10000_CS2/output/'
#Filename = GADGET_G_path + CS2_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS3_path  = 'G_HQ_10000_CS3/output/'
#Filename = GADGET_G_path + CS2_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS4_path  = 'G_HQ_100000_CS4/output/'
#Filename = GADGET_G_path + CS4_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + CS4_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
CS5_path  = 'G_HQ_100000_CS5/output/'
#Filename = GADGET_G_path + CS5_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + CS5_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
CS6_path  = 'G_HQ_100000_CS6/output/'
#Filename = GADGET_G_path + CS6_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + CS6_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
DS1_path  = 'G_0_5_100000_DS1/output/'
#Filename = GADGET_G_path + DS1_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + DS1_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
#Filename = GADGET_G_path + DS1_path + 'Osipkov_Merritt10000_G1.0_49_093.hdf5'
D2_path   = 'G_0_5_100000_D2/output/'
#Filename = GADGET_G_path + D2_path + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + D2_path + 'Hernquist10000_G1.0_48_093.hdf5'
#Filename = GADGET_G_path + D2_path + 'Hernquist10000_G1.0_49_093.hdf5'
Soft_D2_path = 'Soft_G_0_5_100000_D2/output/'
#Filename = GADGET_G_path + Soft_D2_path + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename = GADGET_G_path + Soft_D2_path + 'Hernquist10000_G1.0_48_093.hdf5'
#Filename = GADGET_G_path + Soft_D2_path + 'Hernquist10000_G1.0_49_093.hdf5'

# Bound particles only:
B_rfp_path = 'G_HQ_1000000_B/rfp_output/'
#Filename = GADGET_G_path + B_rfp_path + 'B_G1.0_200_rfp_011.hdf5'
#Filename = GADGET_G_path + B_rfp_path + 'B_G1.0_200_rfp_093.hdf5'
Soft_B_rfp_path = 'Soft_G_HQ_1000000_B/rfp_output/'
#Filename = GADGET_G_path + Soft_B_rfp_path + 'B_G1.0_200_rfp_011.hdf5'
#Filename = GADGET_G_path + Soft_B_rfp_path + 'B_G1.0_200_rfp_093.hdf5'
CS4_rfp_path = 'G_HQ_100000_CS4/rfp_output/'
#Filename = GADGET_G_path + CS4_rfp_path + 'CS4_G1.0_49_rfp_093.hdf5'
CS5_rfp_path = 'G_HQ_100000_CS5/rfp_output/'
#Filename = GADGET_G_path + CS5_rfp_path + 'CS5_G1.0_49_rfp_093.hdf5'
CS6_rfp_path = 'G_HQ_100000_CS6/rfp_output/'
#Filename = GADGET_G_path + CS6_rfp_path + 'CS6_G1.0_49_rfp_093.hdf5'
DS1_rfp_path = 'G_0_5_100000_DS1/rfp_output/'
#Filename = GADGET_G_path + DS1_rfp_path + 'DS1_G1.0_50_rfp_093.hdf5'
D2_rfp_path  = 'G_0_5_100000_D2/rfp_output/'
#Filename = GADGET_G_path + D2_rfp_path  + 'D2_G1.0_50_rfp_093.hdf5'
Soft_D2_rfp_path = 'Soft_G_0_5_100000_D2/rfp_output/'
#Filename = GADGET_G_path + Soft_D2_rfp_path + 'D2_G1.0_50_rfp_093.hdf5'
E_rfp_path = 'G_HQ_1000000_E/rfp_output/'

SnapshotFile = h5py.File(Filename, 'r')
# F = 'test_' + Filename[len(GADGET_G_path + test_path):-5]
# F = 'A_' + Filename[len(GADGET_G_path + A_path):-5]
# F = 'A_' + Filename[len(nosync_path + A_path):-5]
F = 'B_' + Filename[len(GADGET_G_path + B_path):-5]
# F = 'Soft_B_' + Filename[len(GADGET_G_path + Soft_B_path):-5]
# F = 'CS1_' + Filename[len(GADGET_G_path + CS1_path):-5]
# F = 'CS2_' + Filename[len(GADGET_G_path + CS2_path):-5]
# F = 'CS3_' + Filename[len(GADGET_G_path + CS3_path):-5]
# F = 'CS4_' + Filename[len(GADGET_G_path + CS4_path):-5]
# F = 'CS5_' + Filename[len(GADGET_G_path + CS5_path):-5]
# F = 'CS6_' + Filename[len(GADGET_G_path + CS6_path):-5]
# F = 'DS1_' + Filename[len(GADGET_G_path + DS1_path):-5]
# F = 'D2_' + Filename[len(GADGET_G_path + D2_path):-5]
# F = 'Soft_D2_' + Filename[len(GADGET_G_path + Soft_D2_path):-5]

# Bound particles only:
# F = 'B_bound_particles_' + Filename[len(GADGET_G_path + B_rfp_path + 'B_'):-5]
# F = 'Soft_B_bound_particles_' + Filename[len(GADGET_G_path + Soft_B_rfp_path + 'B_'):-5]
# F = 'CS4_bound_particles_' + Filename[len(GADGET_G_path + CS4_rfp_path + 'CS4_'):-5]
# F = 'CS5_bound_particles_' + Filename[len(GADGET_G_path + CS5_rfp_path + 'CS5_'):-5]
# F = 'CS6_bound_particles_' + Filename[len(GADGET_G_path + CS6_rfp_path +  'CS6_'):-5]
# F = 'DS1_bound_particles_' + Filename[len(GADGET_G_path + DS1_rfp_path + 'DS1_'):-5]
# F = 'D2_bound_particles_' + Filename[len(GADGET_G_path + D2_rfp_path + 'D2_'):-5]
# F = 'Soft_D2_bound_particles_' + Filename[len(GADGET_G_path + Soft_D2_rfp_path + 'D2_'):-5]
# F = 'E_bound_particles_' + Filename[len(GADGET_G_path + E_rfp_path + 'E_'):-5]

Gammas = [-1.5, -2.0, -2.5, -3.0]
Gamma = Gammas[1]
Beta = 1.

keep_IC_R_middle = 0
new_R_middle = 1
R_bin_automatic = 0

# Switches for figures

Fig2_Density = 1
Fig2_Densityfit = 1
Fig2_Density_r_2 = 1
Fig3_Potential = 0
Fig4_xy_rectangular = 0
Fig5_cartesian_velocities = 0

bins_202 = 0
bins_102 = 0
# Reduce number of radial bins in analysis code.
# This makes them larger and they therefore contain more particles.
larger_fewer_bins = 1

largest_R_limit = 1  # Analyse larger volume of structure, sets R_limit to 10000.
large_R_limit = 0  # Analyse large volume of structure, sets R_limit to 5000.

if keep_IC_R_middle:  # For R_limit_10000 and 20 bins.
    if F.startswith('Hernquist10000_G'):
        R_middles = [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** -.30]
    if F.startswith('OsipkovMerritt_'):
        R_middles = [0, 0, 0, 0]
if new_R_middle:  # Choose new R_middle for each file.
    # B
    if F == 'B_Hernquist10000_G1.0_0_000':  # 0.th/IC file of B
        R_middles = [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** .3]
    if F == 'B_Hernquist10000_G1.0_5_005':  # 5.th file
        R_middles = [10 ** -.4, 10 ** -.15, 10 ** .1, 10 ** .25]
    if F == 'B_Hernquist10000_G1.0_10_005':  # 10.th file
        R_middles = [10 ** -.25, 10 ** -.14, 1., 10 ** .4]
    if F == 'B_Hernquist10000_G1.0_198_000':  # 198.th file
        R_middles = [10 ** .1, 10 ** .2, 10 ** .3, 10 ** .45]
    if F == 'B_Hernquist10000_G1.0_198_093':
        R_middles = [10 ** .1, 10 ** .15, 10 ** .25, 10 ** .5]
    # CS1
    if F == 'CS1_Osipkov_Merritt10000_G1.0_0_000':
        R_middles = [10 ** -.95, 10 ** -.25, 1., 10 ** .35]
    # CS2
    if F == 'CS2_Osipkov_Merritt10000_G1.0_0_000':
        R_middles = [10 ** -1.1, 10 ** -.4, 1., 10 ** .4]
    # CS3
    if F == 'CS3_Osipkov_Merritt10000_G1.0_0_000':
        R_middles = [10 ** -.7, 10 ** -.4, 1., 10 ** .4]
    # CS4
    if F == 'CS4_Osipkov_Merritt10000_G1.0_0_000':
        R_middles = [10 ** -.75, 10 ** -.4, 1., 10 ** .3]
    # CS5
    if F == 'CS5_Osipkov_Merritt10000_G1.0_0_000':
        R_middles = [10 ** -.75, 10 ** -.4, 1., 10 ** .3]
    # CS6
    if F == 'CS6_Osipkov_Merritt10000_G1.0_0_000':
        R_middles = [10 ** -.8, 10 ** -.25, 1., 10 ** .3]

if Gamma == Gammas[0]:
    R_middle = R_middles[0]
elif Gamma == Gammas[1]:
    R_middle = R_middles[1]
elif Gamma == Gammas[2]:
    R_middle = R_middles[2]
elif Gamma == Gammas[3]:
    R_middle = R_middles[3]

Pos = SnapshotFile['PartType1/Coordinates'].value
Vel = SnapshotFile['PartType1/Velocities'].value
V = SnapshotFile['PartType1/Potential'].value
x = Pos[:, 0]
y = Pos[:, 1]
z = Pos[:, 2]
vx = Vel[:, 0]
vy = Vel[:, 1]
vz = Vel[:, 2]
minV = np.argmin(V)
xC = x[minV]
yC = y[minV]
zC = z[minV]
vxC = vx[minV]
vyC = vy[minV]
vzC = vz[minV]
R = ((x - xC) ** 2 + (y - yC) ** 2 + (z - zC) ** 2) ** .5

if largest_R_limit:
    R_limit = 10000.
    F += '_R_limit_10000'
elif large_R_limit:
    R_limit = 5000.
    F += '_R_limit_5000'
else:
    R_limit = 500.
    # F += '_R_limit_500'

GoodIDs = np.where(R<R_limit)
xcl = x[GoodIDs]
ycl = y[GoodIDs]
zcl = z[GoodIDs]
Vcl = V[GoodIDs]
Rcl = R[GoodIDs]

# Now slice the cluster into a rectangular shape still 1000 kpc wide, but only 100 kpc tall
GoodIDs2 = np.where((R < R_limit) * (yC - 50.0 < y) * (y < yC + 50.0))
xclrec = x[GoodIDs2]
yclrec = y[GoodIDs2]
zclrec = z[GoodIDs2]
vxclrec = vx[GoodIDs2]
vyclrec = vy[GoodIDs2]
vzclrec = vz[GoodIDs2]
vxnew = vx[GoodIDs2] - np.median(vxclrec)
vynew = vy[GoodIDs2] - np.median(vyclrec)
vznew = vz[GoodIDs2] - np.median(vzclrec)
Vclrec = V[GoodIDs2]
Rclrec = R[GoodIDs2]


def rho_Hernquist(rho_0_HQ, rs, x):
    return rho_0_HQ / (x / rs * (1 + x / rs) ** 3)


def rho_NFW(rho_0_NFW, rs, x):
    return rho_0_NFW / (x / rs * (1 + x / rs) ** 2)


# Total number of particles:
if F.startswith(('A_', 'B_', 'E_')):
    N = 10 ** 6
elif F.startswith(('CS4_', 'CS5_', 'CS6_', 'DS1_', 'D2_')):
    N = 10 ** 5
elif F.startswith(('CS1_', 'CS2_', 'CS3_')):
    N = 10 ** 4

if F.startswith(('A_', 'B_', 'CS4_', 'CS5_', 'CS6_', 'E_')):
    M = 1.  # Total mass equals unity
elif F.startswith(('DS1_', 'D2_')):
    M = 1. / 6.

m = M / N  # Mass of each particle
# print('N = ', N)
# print('m = ', m)

R_hob_par = R[GoodIDs]

if Gamma == Gammas[1]:
    r_2 = R_middle
    # position of particles inside halo
    posR_par_inside_halo = np.where(R_hob_par < r_2)
    nr_par_inside_halo = len(posR_par_inside_halo[0])
    M_2 = nr_par_inside_halo*m
    G = 1.
    v_circ_2 = np.sqrt(G * M_2 / r_2)
    V_2 = 4 / 3 * np.pi * r_2 ** 3

min_binning_R_unitRmax = .00001  # end-value of first bin
max_binning_R_unitRmax = 1.0  # end-value of last bin
nr_binning_bins = 1000.0  # number of bins 1000.0

(density_arr, Volume_arr, rho_arr, rho_2_arr) = ([] for i in range(4))

# Array, 0.00001-1.
binning_arr_lin_log10_unitRmax = 10 ** ((np.arange(nr_binning_bins) /
                                 (nr_binning_bins - 1)) *
                                 abs(np.log10(max_binning_R_unitRmax)
                                 - np.log10(min_binning_R_unitRmax))
                                 + np.log10(min_binning_R_unitRmax))
# Array, 0-500
binning_arr_lin_log10 = R_limit * binning_arr_lin_log10_unitRmax
for i in range(0, int(nr_binning_bins - 2)):  # loop over 0-998
    min_R_bin_i = binning_arr_lin_log10[i]  # start of bin
    max_R_bin_i = binning_arr_lin_log10[i + 1]  # end of bin
    # position of particles inside a radial bin
    posR_par_inside_bin_i = np.where((R > min_R_bin_i) & (R < max_R_bin_i))[0]
    # number of particles inside a radial bin
    nr_par_inside_bin_i = len(posR_par_inside_bin_i)
    Volume_cl = (4. / 3.) * np.pi * (max_R_bin_i ** 3 -
                            min_R_bin_i ** 3)  # Volume of cluster
    den_cl = nr_par_inside_bin_i / Volume_cl  # Number density
    rho = den_cl * m
    rho_2 = rho * V_2 / M_2

    # save arrays
    density_arr.append(den_cl)
    Volume_arr.append(Volume_cl)
    rho_arr.append(rho)
    rho_2_arr.append(rho_2)

Invers_Volume_arr = np.log10(np.divide(np.ones(len(Volume_arr)),
                                               Volume_arr))

'''
print('len(density_arr) = ', len(density_arr))
print('len(rho_arr) = ', len(rho_arr))
print('len(x) = ', len(x))
print('len(y) = ', len(y))
print('len(z) = ', len(z))
print('len(R) = ', len(R))

print('x[0] = ', x[0])
print('y[0] = ', y[0])
print('z[0] = ', z[0])
print('R[0] = ', R[0])

print('x[100] = ', x[100])
print('y[100] = ', y[100])
print('z[100] = ', z[100])
print('R[100] = ', R[100])

print('x[99999] = ', x[99999])
print('y[99999] = ', y[99999])
print('z[99999] = ', z[99999])
print('R[99999] = ', R[99999])
'''

if Fig2_Density:
    f = plt.figure(figsize=(16, 11))
    v = [-1, 1, -4, .5]
    plt.axis(v)
    x_plot = np.log10(binning_arr_lin_log10)
    # y_plot = density_arr
    plt.xlabel(r'$ \log r $', fontsize=30)
    plt.ylabel(r'$ \log \rho $', fontsize=30)
    plt.plot(x_plot[0:int(nr_binning_bins - 2)], np.log10(rho_arr),
             '-o', ms=2, lw=2, mew=0, c='green', label=r'$\rho$')
    # plt.legend(prop=dict(size=12), numpoints=2, ncol=2,
    #            frameon=True, loc=1, handlelength=2.5)

    if Fig2_Densityfit:
        x = binning_arr_lin_log10
        y_plot = rho_Hernquist(1. / (2 * np.pi), 1., x)
        plt.plot(np.log10(x), np.log10(y_plot), ':o', ms=2, lw=2, mew=0,
                 c='black', label=r'$\frac{1}{2\pi r (1+r)^3}$')
        plt.title(r'Density profile (B IC with 998 radial bins)',
                  fontsize=30)
        '''
        Chi2 = 0
        i = 0
        # print('rho_arr = ', rho_arr)
        while (i < len(rho_arr)):  # returns chi2 = infinity.
        # while (300 < i < len(rho_arr) - 300):  # returns chi2 = .00000
        # while (1 < i < len(rho_arr) - 1):  # returns chi2 = .00000

            if isnan(rho_arr[i]):
                print('nan at index: ', i)
            else:
                Chi2 += ((rho_arr[i] - y_plot[i]) ** 2) / (rho_arr[i] *
                        .2) ** 2
                print('Chi2 for density-fit: ', Chi2)
            i += 1
        Chi2 = (1.0 / (len(rho_arr) - 1)) * Chi2

        print('Total Chi2 for density-fit: ', Chi2)
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',
                 label=r'$\chi^2 = %.6f$'%Chi2)
        '''
        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,
                         fancybox=True, loc=0, handlelength=2.5)
        leg.get_frame().set_alpha(.5)

        # f.savefig(figure_path + 'A_Density_fit.png')
        f.savefig(figure_path + 'B_Density_fit.png')
        # f.savefig(figure_path + 'Soft_B_Density_fit.png')
        # f.savefig(figure_path + 'CS1_Density_fit.png')
        # f.savefig(figure_path + 'CS2_Density_fit.png')
        # f.savefig(figure_path + 'CS3_Density_fit.png')
        # f.savefig(figure_path + 'CS4_Density_fit.png')
        # f.savefig(figure_path + 'CS5_Density_fit.png')
        # f.savefig(figure_path + 'CS6_Density_fit.png')
        # f.savefig(figure_path + 'DS1_Density_fit.png')
        # f.savefig(figure_path + 'D2_Density_fit.png')
        # f.savefig(figure_path + 'Soft_D2_Density_fit.png')
        # f.savefig(figure_path + 'E_Density_fit.png')

    else:
        plt.title('Density profile',fontsize=30)
        # f.savefig(figure_path + 'A_Density.png')
        # f.savefig(figure_path + 'B_Density.png')
        # f.savefig(figure_path + 'Soft_B_Density.png')
        # f.savefig(figure_path + 'CS1_Density.png')
        # f.savefig(figure_path + 'CS2_Density.png')
        # f.savefig(figure_path + 'CS3_Density.png')
        # f.savefig(figure_path + 'CS4_Density.png')
        # f.savefig(figure_path + 'CS5_Density.png')
        # f.savefig(figure_path + 'CS6_Density.png')
        # f.savefig(figure_path + 'DS1_Density.png')
        # f.savefig(figure_path + 'D2_Density.png')
        # f.savefig(figure_path + 'Soft_D2_Density.png')
        # f.savefig(figure_path + 'E_Density.png')

if Fig2_Density_r_2:
    f = plt.figure(figsize=(16, 11))
    v = [-1, 1, -4, .5]
    plt.axis(v)
    x_plot = np.log10(binning_arr_lin_log10 / r_2)
    plt.xlabel(r'$ \log (\frac{r}{r_{-2}})$', fontsize=30)
    plt.ylabel(r'$ \log \rho $', fontsize=30)
    plt.plot(x_plot[0:int(nr_binning_bins - 2)], np.log10(rho_arr),
             '-o', ms=2, lw=2, mew=0, c='green', label=r'$\rho$')
    # plt.legend(prop=dict(size=18), numpoints=2, ncol=2,
    #            frameon=True, loc=1, handlelength=2.5)

    plt.title(r'Density profile (B IC with 998 radial bins)',
              fontsize=30)

    # f.savefig(figure_path + 'A_Density_r_2.png')
    f.savefig(figure_path + 'B_Density_r_2.png')
    # f.savefig(figure_path + 'Soft_B_Density_r_2.png')
    # f.savefig(figure_path + 'CS1_Density_r_2.png')
    # f.savefig(figure_path + 'CS2_Density_r_2.png')
    # f.savefig(figure_path + 'CS3_Density_r_2.png')
    # f.savefig(figure_path + 'CS4_Density_r_2.png')
    # f.savefig(figure_path + 'CS5_Density_r_2.png')
    # f.savefig(figure_path + 'CS6_Density_r_2.png')
    # f.savefig(figure_path + 'DS1_Density_r_2.png')
    # f.savefig(figure_path + 'D2_Density_r_2.png')
    # f.savefig(figure_path + 'Soft_D2_Density_r_2.png')
    # f.savefig(figure_path + 'E_Density_r_2.png')

if Fig3_Potential:
    f = plt.figure()
    ax1 = plt.subplot(121)
    plt.xlabel('r')
    plt.ylabel(r'$\Phi$')
    plt.title('Potential')
    plt.plot(Rcl, Vcl, 'o', ms=2, mew=0, color='blue')
    plt.grid()

    ax2 = plt.subplot(122)
    plt.xlabel(r'$\log r$')
    plt.plot(np.log10(Rcl), Vcl, 'o', ms=2, mew=0, color='blue')
    plt.grid()
    setp(ax2.get_yticklabels(), visible=False)

    # f.savefig(figure_path + 'A_Potential.png')
    # f.savefig(figure_path + 'B_Potential.png')
    # f.savefig(figure_path + 'Soft_B_Potential.png')
    # f.savefig(figure_path + 'CS1_Potential.png')
    # f.savefig(figure_path + 'CS2_Potential.png')
    # f.savefig(figure_path + 'CS3_Potential.png')
    # f.savefig(figure_path + 'CS4_Potential.png')
    # f.savefig(figure_path + 'CS5_Potential.png')
    # f.savefig(figure_path + 'CS6_Potential.png')
    # f.savefig(figure_path + 'DS1_Potential.png')
    # f.savefig(figure_path + 'D2_Potential.png')
    # f.savefig(figure_path + 'Soft_D2_Potential.png')
    # f.savefig(figure_path + 'E_Potential.png')

# plot rectangular slice through cluster:
if Fig4_xy_rectangular:
    f = plt.figure()
    plt.title('Rectangular slice through cluster')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.hist2d(xclrec, yclrec, bins=200, norm=LogNorm())
    plt.colorbar()

    # f.savefig(figure_path + 'A_xy_rectangular.png')
    # f.savefig(figure_path + 'B_xy_rectangular.png')
    # f.savefig(figure_path + 'Soft_B_xy_rectangular.png')
    # f.savefig(figure_path + 'CS1_xy_rectangular.png')
    # f.savefig(figure_path + 'CS2_xy_rectangular.png')
    # f.savefig(figure_path + 'CS3_xy_rectangular.png')
    # f.savefig(figure_path + 'CS4_xy_rectangular.png')
    # f.savefig(figure_path + 'CS5_xy_rectangular.png')
    # f.savefig(figure_path + 'CS6_xy_rectangular.png')
    # f.savefig(figure_path + 'DS1_xy_rectangular.png')
    # f.savefig(figure_path + 'D2_xy_rectangular.png')
    # f.savefig(figure_path + 'Soft_D2_xy_rectangular.png')
    # f.savefig(figure_path + 'E_xy_rectangular.png')

# 3 plots of the velocities as function of x.
if Fig5_cartesian_velocities:
    f = plt.figure()
    ax1 = plt.subplot(131)
    plt.ylabel('vxnew')
    plt.plot(xclrec, vxnew, 'o', ms=2, mew=0, color='blue')
    plt.title('velocities')
    ax2 = plt.subplot(132)
    plt.xlabel('x')
    plt.ylabel('vynew')
    plt.plot(xclrec, vynew, 'o', ms=2, mew=0, color='blue')
    setp( ax2.get_yticklabels(), visible=False)
    ax3 = plt.subplot(133)
    plt.ylabel('vznew')
    plt.plot(xclrec, vznew, 'o', ms=2, mew=0, color='blue')
    setp(ax3.get_yticklabels(), visible=False)

    # f.savefig(figure_path + 'A_cartesian_velocities.png')
    # f.savefig(figure_path + 'B_cartesian_velocities.png')
    # f.savefig(figure_path + 'Soft_B_cartesian_velocities.png')
    # f.savefig(figure_path + 'CS1_cartesian_velocities.png')
    # f.savefig(figure_path + 'CS2_cartesian_velocities.png')
    # f.savefig(figure_path + 'CS3_cartesian_velocities.png')
    # f.savefig(figure_path + 'CS4_cartesian_velocities.png')
    # f.savefig(figure_path + 'CS5_cartesian_velocities.png')
    # f.savefig(figure_path + 'CS6_cartesian_velocities.png')
    # f.savefig(figure_path + 'DS1_cartesian_velocities.png')
    # f.savefig(figure_path + 'D2_cartesian_velocities.png')
    # f.savefig(figure_path + 'Soft_D2_cartesian_velocities.png')
    # f.savefig(figure_path + 'E_cartesian_velocities.png')

plt.show()  # show all plots
