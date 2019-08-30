# -*- coding: utf-8 -*-

from __future__ import division
import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
# matplotlib.use('TkAgg')  # <-- THIS MAKES IT FAST!
import matplotlib.pyplot as plt
import IPython
# from matplotlib.colors import LogNorm
import time
import pylab
from scipy.stats import norm
# import matplotlib.mlab as mlab
import scipy as sp
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from pathlib import Path

User_path = Path.cwd() + '/Users/gustav.c.rasmussen/'
Desktop_path = User_path + 'Desktop/'
GADGET_G_path = Desktop_path + 'RunGadget/G_perturbations/'
Stable_path = 'LOS/Stable_structures/'
figure_path = Desktop_path + Stable_path + 'figures/'

sims = ['A', 'B', 'Soft_B', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'DS1', 'D2', 'Soft_D2', 'E']

# text_files_path = Desktop_path + Stable_path + 'text_files/' + sims[0] + '/'

Martin_path = 'Martin_IC_and_Final_Edd_and_OM/'
hdf5_path = Desktop_path + 'G_perturbations/hdf5_files/'
nosync_path = User_path + 'nosync/RunGadget/'

# Filename = hdf5_path + '0G00_IC_000.hdf5'
# Filename = hdf5_path + '0G20_Final_000.hdf5'
# Filename = hdf5_path + 'OMG00_001_IC_000.hdf5'
# Filename = hdf5_path + 'OMG20_Final_000.hdf5'

test_path = 'G_HQ_1000000_test/output/'

snaps = ['1.0_0_000', '1.2_1_005', '0.8_2_000', '0.8_2_005', '1.2_3_005', '1.2_5_005',
         '1.2_7_005', '1.2_9_005', '1.0_10_009']
# Filename = GADGET_G_path + test_path + 'Hernquist10000_G' + snaps[0] + '.hdf5'

A_path = 'G_HQ_1000000_A/output/'
# Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_5_005.hdf5'
# Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_10_005.hdf5'
# Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_40_005.hdf5'
# Filename = GADGET_G_path + A_path + 'Hernquist10000_G1.0_48_009.hdf5'
# Filename = nosync_path + A_path + 'Hernquist10000_G1.0_48_093.hdf5'   
B_path = 'G_HQ_1000000_B/output/'
# Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_5_005.hdf5'
# Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_10_005.hdf5'
# Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_198_000.hdf5'
# Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_198_093.hdf5'
# Filename = GADGET_G_path + B_path + 'Hernquist10000_G1.0_199_093.hdf5'
Soft_B_path = 'Soft_G_HQ_1000000_B/output/'
# Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_5_005.hdf5'
# Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_10_005.hdf5'
# Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_198_000.hdf5'
# Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_198_093.hdf5'
# Filename = GADGET_G_path + Soft_B_path + 'Hernquist10000_G1.0_199_093.hdf5'
CS1_path = 'G_HQ_10000_CS1/output/'
# Filename = GADGET_G_path + CS1_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS2_path = 'G_HQ_10000_CS2/output/'
# Filename = GADGET_G_path + CS2_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS3_path = 'G_HQ_10000_CS3/output/'
# Filename = GADGET_G_path + CS3_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS4_path = 'G_HQ_100000_CS4/output/'
# Filename = GADGET_G_path + CS4_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + CS4_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
CS5_path = 'G_HQ_100000_CS5/output/'
# Filename = GADGET_G_path + CS5_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + CS5_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
CS6_path = 'G_HQ_100000_CS6/output/'
# Filename = GADGET_G_path + CS6_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + CS6_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
DS1_path = 'G_0_5_100000_DS1/output/'
# Filename = GADGET_G_path + DS1_path + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + DS1_path + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
# Filename = GADGET_G_path + DS1_path + 'Osipkov_Merritt10000_G1.0_49_093.hdf5'
D2_path = 'G_0_5_100000_D2/output/'
# Filename = GADGET_G_path + D2_path + 'Hernquist10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + D2_path + 'Hernquist10000_G1.0_48_093.hdf5'
# Filename = GADGET_G_path + D2_path + 'Hernquist10000_G1.0_49_093.hdf5'
Soft_D2_path = 'Soft_G_0_5_100000_D2/output/'
# Filename = GADGET_G_path + Soft_D2_path + 'Hernquist10000_G1.0_0_000.hdf5'
# Filename = GADGET_G_path + Soft_D2_path + 'Hernquist10000_G1.0_48_093.hdf5'
# Filename = GADGET_G_path + Soft_D2_path + 'Hernquist10000_G1.0_49_093.hdf5'
E_path = 'Soft_G_HQ_1000000_E/output/'
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G1.0_0_000.hdf5' 
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G1.0_5_005.hdf5' 
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G1.0_10_005.hdf5' 
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G1.0_160_005.hdf5'
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G1.05_196_005.hdf5'
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G0.95_197_005.hdf5'
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G1.0_198_009.hdf5'
# Filename = GADGET_G_path + E_path + 'Hernquist10000_G1.0_198_093.hdf5'

# Bound particles only:
B_rfp_path = 'G_HQ_1000000_B/rfp_output/'
# Filename = GADGET_G_path + B_rfp_path + 'B_G1.0_200_rfp_011.hdf5'
# Filename = GADGET_G_path + B_rfp_path + 'B_G1.0_200_rfp_093.hdf5'
Soft_B_rfp_path = 'Soft_G_HQ_1000000_B/rfp_output/'
# Filename = GADGET_G_path + Soft_B_rfp_path + 'B_G1.0_200_rfp_011.hdf5'
# Filename = GADGET_G_path + Soft_B_rfp_path + 'B_G1.0_200_rfp_093.hdf5'
CS4_rfp_path = 'G_HQ_100000_CS4/rfp_output/'
# Filename = GADGET_G_path + CS4_rfp_path + 'CS4_G1.0_49_rfp_093.hdf5'
CS5_rfp_path = 'G_HQ_100000_CS5/rfp_output/'
# Filename = GADGET_G_path + CS5_rfp_path + 'CS5_G1.0_49_rfp_093.hdf5'
CS6_rfp_path = 'G_HQ_100000_CS6/rfp_output/'
# Filename = GADGET_G_path + CS6_rfp_path + 'CS6_G1.0_49_rfp_093.hdf5'
DS1_rfp_path = 'G_0_5_100000_DS1/rfp_output/'
# Filename = GADGET_G_path + DS1_rfp_path + 'DS1_G1.0_50_rfp_093.hdf5'
D2_rfp_path = 'G_0_5_100000_D2/rfp_output/'
# Filename = GADGET_G_path + D2_rfp_path + 'D2_G1.0_50_rfp_093.hdf5'
Soft_D2_rfp_path = 'Soft_G_0_5_100000_D2/rfp_output/'
# Filename = GADGET_G_path + Soft_D2_rfp_path + 'D2_G1.0_50_rfp_093.hdf5'
E_rfp_path = 'G_HQ_1000000_E/rfp_output/'
# Filename = GADGET_G_path + E_rfp_path + 'E_G1.0_50_rfp_093.hdf5'  # Fix filename here.

print(Filename)
SnapshotFile = h5py.File(Filename, 'r')

# F = 'test_' + Filename[len(GADGET_G_path + test_path):-5]
# F = 'A_' + Filename[len(GADGET_G_path + A_path):-5]
# F = 'A_' + Filename[len(nosync_path   + A_path):-5]
# F = 'B_' + Filename[len(GADGET_G_path + B_path):-5]
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
# F = 'E_' + Filename[len(GADGET_G_path + E_path):-5]

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

# Gamma = -1.5
# Beta = 1.0

keep_IC_R_middle = 0
new_R_middle = 0

zero_dict = {-1.5: .0, -2.0: .0, -2.5: .0, -3.0: .0}

if keep_IC_R_middle:
    if F.startswith('Hernquist10000_G'):
        if Gamma == -1.5:
            R_middle = 10 ** -.70 
        elif Gamma == -2.0:
            R_middle = 10**-.25
        elif Gamma == -2.5:
            R_middle = 10**-.0 
        elif Gamma == -3.0:
            R_middle = 10**-.30
    if F.startswith('OsipkovMerritt_'):
        zero_dict.get(Gamma, "No such gamma value")

if new_R_middle:
    [('Hernquist10000_G1.0_0_000', {-1.5: 10 ** -.70, -2.0: 10 ** -.25, -2.5: 10 ** -.0, -3.0: 10 ** -.30}),
     ('Hernquist10000_G1.2_1_005', {-1.5: 10**-0.55, -2.0: 10**-0.4, -2.5: 10**-0.1, -3.0: 10**0.2}),
     ('Hernquist10000_G0.8_2_005', zero_dict),
     ('Hernquist10000_G1.2_3_005', {-1.5: 10**-0.6, -2.0: 10**-0.4, -2.5: 10**0.0, -3.0: 10**0.4}),
     ('Hernquist10000_G1.2_5_005', {-1.5: 10**-0.45, -2.0: 10**-0.35, -2.5: 10**-0.1, -3.0: 10**0.45}),     
     ('Hernquist10000_G1.2_7_005', {-1.5: 10**-0.35, -2.0: 10**-0.25, -2.5: 10**-0.1, -3.0: 10**0.48}),
     ('Hernquist10000_G1.2_9_005', {-1.5: 10**-0.35, -2.0: 10**-0.3, -2.5: 10**-0.15, -3.0: 10**0.5}),
     ('Hernquist10000_G1.0_10_009', {-1.5: 10**-0.25, -2.0: 10**-0.15, -2.5: 10**0.0, -3.0: 10**0.5})
     ]

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
R = ravf.modulus(x - xC, y - yC, z - zC)

# R_limit_min = R_middle  # make R_limit_min and R_limit_max selection automatic
# R_limit_max = R_middle

'''
R_limit_min, R_limit_max = r_bin_automatic()

x = x[GoodIDs]
y = y[GoodIDs]
z = z[GoodIDs]
vx = vx[GoodIDs]
vy = vy[GoodIDs]
vz = vz[GoodIDs] 
vx -= np.median(vx)
vy -= np.median(vy)
vz -= np.median(vz)
'''
vx -= np.median(vx)
vy -= np.median(vy)
vz -= np.median(vz)

nr_binning_bins = 102

# Switches
Fig1_xy = 0
Fig2_xz = 0
Fig3_3D_xyz = 0

vsphericalnew = 0
vsphericalnew_sigma = 0

x14_25_36_same_length = 0
save_r_v_as_txt = 0

Fig13_LOS = 0
Fig14_LOS_log = 0
Fig15_LOS_radius10 = 0
Fig16_LOS_radius50 = 0
Fig17_LOS_radius200 = 0

if Fig1_xy:
    figure()
    plt.subplot(121)
    plt.plot(x, y)
    plt.xlabel(r'$x$', fontsize=30)
    plt.ylabel(r'$y$', fontsize=30)
    plt.title(r'Positions. $N=%i$, $\gamma = %.2f$ ,  File = %s' % (len(x), Gamma, F), fontsize=30)
    plt.subplot(122)
    plt.plot (x, z)
    plt.xlabel(r'$x$', fontsize=30)
    plt.ylabel(r'$z$',f ontsize=30)

if Fig2_xz:
    figure()
    plt.subplot(121)
    plt.plot(x,y,'o', ms=1)
    plt.xlabel(r'$x$',fontsize=30)
    plt.ylabel(r'$y$',fontsize=30)
    plt.title(r'Positions. $N=%i$, $\gamma = %.2f$ ,  File = %s' %(len(x), Gamma, F),fontsize=30)
    plt.subplot(122)
    plt.plot (x,z,'o', ms=1)
    plt.xlabel(r'$x$',fontsize=30)
    plt.ylabel(r'$z$',fontsize=30)

def randrange(n, vmin, vmax):  # 3D scatterplot of positions
    return (vmax - vmin) * np.random.rand(n) + vmin

if Fig3_3D_xyz:
    f = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    n = 100
    for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        ax.scatter(x, y, z, c=c, marker=m)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D view of halo positions')

if vsphericalnew: # radial and tangential velocities
    r = ravf.modulus(x, y, z)
    Phi = sp.arctan2(y, x)
    Theta = sp.arccos(z / r)
    VR = sp.sin(Theta)*sp.cos(Phi) * vx + sp.sin(Theta)*sp.sin(Phi) * vy + sp.cos(Theta) * vz
    VTheta = sp.cos(Theta)*sp.cos(Phi) * vx + sp.cos(Theta)*sp.sin(Phi) * vy - sp.sin(Theta) * vz
    VPhi = - sp.sin(Phi) * vx + sp.cos(Phi) * vy
    VT = VTheta + VPhi


def func_1(x, a, b):
    return a * x * np.exp(-b * x ** 2.)


def func_2(x, a, b):
    return a * np.exp(-b * x**2.)


def func_3(x, a, b):
    return a * x**2*np.exp(-b * x**2.)


def func_1_log(log10x, a, b):
    x=10.0**log10x
    return a * x * np.exp(-b * x**2.)


def func_2_log(log10x, a, b):
    x=10.0**log10x
    return a * np.exp(-b * x**2.)


def func_3_log(log10x, a, b):
    x=10.0**log10x
    return a * x**2 * np.exp(-b * x**2.)


def func_4(x, a, q, b):
    return a *(1.- (1. - q )*b*x**2.) **(q/( 1. - q))


def func_5(x, b, q):
    return (1.- (1. - q )*b*x**2.) **(q/( 1. - q))


def func_4_log(log10x, a, q, b):
    x=10.0**log10x
    return a * x *(1.- (1. - q )*b*x**2.) **(q/( 1. - q))


# R_hob_par = R[GoodIDs]
# v2 = vx**2+vy**2+vz**2

(sigma2, sigmarad2, sigmatheta2, sigmaphi2, sigmatan2, sigma, sigmarad,
 sigmatheta, sigmaphi, sigmatan, VR_sigmarad, VTheta_sigmatheta,
 VPhi_sigmaphi, VT_sigmatan, r, Phi, Theta, VR, VTheta, VPhi, VT,
 R_LOS_arr, vx_LOS_arr, bin_radius_arr) = ([] for i in range(24))

'''
binning_arr = np.linspace(R_limit_min, R_limit_max, nr_binning_bins) 

for i in range(nr_binning_bins - 2): 
    min_R_bin_i = binning_arr[i]  # start of bin
    max_R_bin_i = binning_arr[i + 1]  # end of bin
    posR_par_in_bin_i = np.where((R_hob_par > min_R_bin_i) & (R_hob_par < max_R_bin_i))  # position of particles inside a radial bin
    nr_par_in_bin_i = len(posR_par_in_bin_i[0])
    if nr_par_in_bin_i == 0:
        continue

    r_i = (x[posR_par_inside_bin_i]**2 + y[posR_par_inside_bin_i]**2+ z[posR_par_inside_bin_i]**2)**.5
    Phi_i = sp.arctan2(y[posR_par_inside_bin_i],x[posR_par_inside_bin_i])
    Theta_i = sp.arccos(z[posR_par_inside_bin_i]/r_i)
    VR_i = sp.sin(Theta_i)*sp.cos(Phi_i) * vx[posR_par_inside_bin_i] + sp.sin(Theta_i)*sp.sin(Phi_i) * vy[posR_par_inside_bin_i] + sp.cos(Theta_i) * vz[posR_par_inside_bin_i]
    VTheta_i = sp.cos(Theta_i)*sp.cos(Phi_i) * vx[posR_par_inside_bin_i] + sp.cos(Theta_i)*sp.sin(Phi_i) * vy[posR_par_inside_bin_i] - sp.sin(Theta_i) * vz[posR_par_inside_bin_i]
    VPhi_i = - sp.sin(Phi_i) * vx[posR_par_inside_bin_i] + sp.cos(Phi_i) * vy[posR_par_inside_bin_i]
    VT_i = (VTheta_i**2 + VPhi_i**2)**.5
    R_LOS_i = (y[posR_par_inside_bin_i]**2 + z[posR_par_inside_bin_i]**2)**.5
    vx_LOS_i = vx[posR_par_inside_bin_i]
    # v2 = vx[posR_par_inside_bin_i]**2+vy[posR_par_inside_bin_i]**2+vz[posR_par_inside_bin_i]**2
    v = (vx[posR_par_inside_bin_i]**2+vy[posR_par_inside_bin_i]**2+vz[posR_par_inside_bin_i]**2)**.5

    # sigmatan2
    vtan2_in_bin_i = VT_i ** 2
    sigmatan2_in_bin_i = (1. / (nr_par_in_bin_i + 1.)) * np.sum(vtan2_in_bin_i)
    sigmatan2.append(sigmatan2_in_bin_i)
    # print(sigmatan2_in_bin_i, np.std(VT_i) ** 2)
    # print(sigmatan2_in_bin_i, np.mean(VT_i ** 2), nr_par_in_bin_i)

    # sigma2 total
    # v2_in_bin_i = v2
    # sigma2_in_bin_i = (1./(nr_par_in_bin_i+1.))*np.sum(v2_in_bin_i)
    # sigma2_in_bin_i = (1./(nr_par_in_bin_i+1.))*np.sum(v2)
    # sigma2.append(sigma2_in_bin_i)
    bin_radius_arr.append((max_R_bin_i + min_R_bin_i) / 2)

    # sigmarad2 radial
    vrad2_in_bin_i = VR_i ** 2
    sigmarad2_in_bin_i = (1. / (nr_par_in_bin_i + 1.)) * np.sum(vrad2_in_bin_i)
    sigmarad2.append(sigmarad2_in_bin_i)

    # sigmatheta2
    VTheta2_in_bin_i = VTheta_i ** 2
    sigmatheta2_in_bin_i = (1. / (nr_par_in_bin_i + 1.)) * np.sum(VTheta2_in_bin_i)
    sigmatheta2.append(sigmatheta2_in_bin_i)

    # sigmaphi2
    VPhi2_in_bin_i = VPhi_i ** 2
    sigmaphi2_in_bin_i = (1. / (nr_par_in_bin_i + 1.)) * np.sum(VPhi2_in_bin_i)
    sigmaphi2.append(sigmaphi2_in_bin_i)

    # sigma_i = sigma2[i] ** .5
    sigma_i = ((1. / (nr_par_in_bin_i + 1.)) * np.sum(v**2)) ** .5  # total sigma
    # sigmarad_i = sigmarad2[i] ** .5
    sigmarad_i = ((1. / (nr_par_in_bin_i + 1.)) * np.sum(VR_i ** 2)) ** .5
    # sigmatheta_i = sigmatheta2[i] ** .5
    sigmatheta_i = ((1. / (nr_par_in_bin_i + 1.)) * np.sum(VTheta_i ** 2)) ** .5
    # sigmaphi_i = sigmaphi2[i] ** .5
    sigmaphi_i = ((1. / (nr_par_in_bin_i + 1.)) * np.sum(VPhi_i ** 2)) ** .5
    # sigmatan_i = sigmatan2[i] ** .5
    sigmatan_i = ((1. / (nr_par_in_bin_i + 1.)) * np.sum(VT_i ** 2)) ** .5 

    R_LOS_arr.append(R_LOS_i)
    vx_LOS_arr.append(vx_LOS_i)

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
    # np.array(VT)
    
    VR_sigmarad.append(VR_i / sigmarad_i)
    VTheta_sigmatheta.append(VTheta_i / sigmatheta_i)
    VPhi_sigmaphi.append(VPhi_i / sigmaphi_i)
    VT_sigmatan.append(VT_i / sigmatan_i)

# R_LOS = np.array(R_LOS_arr)
# vx_LOS = np.array(vx_LOS_arr)
R_LOS = np.concatenate(np.array(R_LOS_arr), axis = 0)
vx_LOS = np.concatenate(np.array(vx_LOS_arr), axis = 0)

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

'''

# divide into 6 graphs
(v_rp, v_rn, v_thetap, v_thetan, v_phip, v_phin, v_tp, v_tn) = ([] for i in range(8))

if vsphericalnew:
    for i in range(len(VR)):
        v_rp.append(VR[i]) if VR[i] >= 0. else v_rn.append(VR[i])

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
    x1 = np.asarray(x1)
    x4 = np.asarray(x4)                           

    if len(v_phin_arr) > len(v_phip_arr):
        for i in range(len(v_phin_arr) - len(v_phip_arr)):
            x2.append(0.)
    else:            
        for i in range(len(v_phip_arr) - len(v_phin_arr)):
            x5.append(0.)
    x2 = np.asarray(x2)
    x5 = np.asarray(x5)                           

    if len(v_rn_arr) > len(v_rp_arr):
        for i in range(len(v_rn_arr) - len(v_rp_arr)):
            x3.append(0.)
    else:
        for i in range(len(v_rp_arr) - len(v_rp_arr)):
            x6.append(0.)
    x3 = np.asarray(x3)
    x6 = np.asarray(x6)                           

if vsphericalnew_sigma:
    (VR_sigmarad_p, VR_sigmarad_n, VTheta_sigmatheta_p, VTheta_sigmatheta_n,
    VPhi_sigmaphi_p, VPhi_sigmaphi_n, VT_sigmatan_p, VT_sigmatan_n) = ([] for i in range(8))

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

r = ravf.modulus(x, y, z)
Phi = sp.arctan2(y, x)
Theta = sp.arccos(z / r)
VR = sp.sin(Theta) * sp.cos(Phi) * vx + sp.sin(Theta) * sp.sin(Phi) * vy + sp.cos(Theta) * vz
R = (y ** 2 + z ** 2) ** .5

if Fig13_LOS:
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(r, VR, 'bo', lw=2, ms=1)
    ax1.set_xlabel(r'Radius, $r$', fontsize=30)
    ax1.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    ax1.set_title(F, fontsize=30)
    ax2.plot(R, vx, 'bo', lw=2, ms=1)
    ax2.set_xlabel(r'Projected radius, $R$', fontsize=30)
    ax2.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)
    ax2.set_title('LOS (A)', fontsize=30)
    f.savefig(figure_path + sims[0] + '_v.png')

if Fig14_LOS_log:
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(np.log10(r), VR, 'bo', lw=2, ms=1)
    ax1.set_xlabel(r'$\log$ r', fontsize=30)
    ax1.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    ax1.set_title(F, fontsize=30)
    ax2.plot(np.log10(R), vx, 'bo', lw=2, ms=1)
    ax2.set_xlabel(r'$\log$ R', fontsize=30)
    ax2.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)
    ax2.set_title('LOS (A)', fontsize=30)
    f.savefig(figure_path + sims[0] + '_v.png')

if Fig15_LOS_radius10:
    f,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
    ax1.set_xlim(0,10)
    ax1.plot(r, VR,'bo',lw=2,ms=1 )
    ax1.set_xlabel(r'Radius, $r$', fontsize=30)
    ax1.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    ax1.set_title(F, fontsize=30)
    ax2.set_xlim(0, 10)
    ax2.plot(R, vx,'bo',lw=2,ms=1 )
    ax2.set_xlabel(r'Projected radius, $R$', fontsize=30)
    ax2.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)
    ax2.set_title('Line-of-sight', fontsize=30)
    ax3.set_xlim(np.log10(0),np.log10(10))
    ax3.plot(np.log10(r), VR,'bo',lw=2,ms=1 )
    ax3.set_xlabel(r'$\log$ r', fontsize=30)
    ax3.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    ax4.set_xlim(np.log10(0),np.log10(10))
    ax4.plot(np.log10(R), vx,'bo',lw=2,ms=1 )
    ax4.set_xlabel(r'$\log$ R', fontsize=30)
    ax4.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)

if Fig16_LOS_radius50:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)    
    # Only choose every thousand particle to plot.
    a = 0
    while a < len(r):
        # ax1.set_xlim(0, 50)
        ax1.plot(r[a], VR[a], 'bo', lw=2, ms=1)
        # ax2.set_xlim(0, 50)
        ax2.plot(R[a], vx[a],'bo', lw=2, ms=1)
        # ax3.set_xlim(np.log10(0),np.log10(50))
        ax3.plot(np.log10(r[a]), VR[a],'bo',lw=2,ms=1)
        # ax4.set_xlim(np.log10(0),np.log10(50))
        ax4.plot(np.log10(R[a]), vx[a],'bo',lw=2,ms=1)
        # print('a = ', a)
        a += 10 ** 3
    '''
    ax1.plot(r, VR,'bo',lw=2,ms=1 )
    ax2.plot(R, vx,'bo',lw=2,ms=1 )
    ax3.plot(np.log10(r), VR,'bo',lw=2,ms=1 )
    ax4.plot(np.log10(R), vx,'bo',lw=2,ms=1 )
    '''
    ax1.set_xlim(0,50)
    ax1.set_xlabel(r'Radius, $r$', fontsize=30)
    ax1.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    ax1.set_title(r' %s, $N = 10^3 $' % F, fontsize=30)
    #ax1.set_title(F, fontsize=30)
    ax2.set_xlim(0,50)
    ax2.set_xlabel(r'Projected radius, $R$', fontsize=30)
    ax2.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)
    ax2.set_title('Line-of-sight', fontsize=30)
    #ax3.set_xlim(np.log10(0),np.log10(50))
    ax3.set_xlim(0,np.log(50))
    ax3.set_xlabel(r'$\log$ r', fontsize=30)
    ax3.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    #ax4.set_xlim(np.log10(0),np.log10(50))
    ax4.set_xlim(0,np.log(50))
    ax4.set_xlabel(r'$\log$ R', fontsize=30)
    ax4.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)

if Fig17_LOS_radius200:
    f, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2) # Only choose every thousand particle to plot.
    a = 0
    while a < len(r):
        #ax1.set_xlim(0,50)
        ax1.plot(r[a], VR[a],'bo',lw=2,ms=1 )
        #ax2.set_xlim(0,50)
        ax2.plot(R[a], vx[a],'bo',lw=2,ms=1 )
        #ax3.set_xlim(np.log10(0),np.log10(50))
        ax3.plot(np.log10(r[a]), VR[a],'bo',lw=2,ms=1 )
        #ax4.set_xlim(np.log10(0),np.log10(50))
        ax4.plot(np.log10(R[a]), vx[a],'bo',lw=2,ms=1 )
        # print('a = ', a)
        a += 10 ** 3
    '''
    ax1.plot(r, VR,'bo',lw=2,ms=1 )
    ax2.plot(R, vx,'bo',lw=2,ms=1 )
    ax3.plot(np.log10(r), VR,'bo',lw=2,ms=1 )
    ax4.plot(np.log10(R), vx,'bo',lw=2,ms=1 )
    '''
    ax1.set_xlim(0,200)
    ax1.set_xlabel(r'Radius, $r$', fontsize=30)
    ax1.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    ax1.set_title(r' %s, $N = 10^3 $' %F, fontsize=30)
    #ax1.set_title(F, fontsize=30)
    ax2.set_xlim(0, 200)
    ax2.set_xlabel(r'Projected radius, $R$', fontsize=30)
    ax2.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)
    ax2.set_title('Line-of-sight', fontsize=30)
    ax3.set_xlim(0, np.log(200))
    ax3.set_xlabel(r'$\log$ r', fontsize=30)
    ax3.set_ylabel(r'Radial velocity, $v_r$', fontsize=30)
    ax4.set_xlim(0, np.log(200))
    ax4.set_xlabel(r'$\log$ R', fontsize=30)
    ax4.set_ylabel(r'Line-of-sight velocity, $v_x$', fontsize=30)
    
plt.show()
