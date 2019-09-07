# -*- coding: utf-8 -*-

import h5py
import numpy as np
import IPython
import time
from pylab import *
from scipy.stats import norm
import scipy
import os.path
from pathlib import Path
import sys

pathname = Path.cwd() / 'RunGadget/Energy_Exchange/IIa/E_HQ_100000_D1/output/B_E_G2P_'
assert os.path.exists(Path.cwd() + '/RunGadget/Energy_Exchange/E_HQ_100000_D1/output/')


def find_latest_filenum():
    '''Return largest filenumber.'''
    hdf5_posix = list(pathname.glob('*.hdf5'))
    hdf5_filenum = [str(file).split('/')[-1][0] for file in hdf5_posix]
    return max(hdf5_filenum)


run_number = find_latest_filenum()

if ((type(run_number) != int) or (run_number < 0)):
    sys.exit('Filename or path error')

Filename_old = pathname / f'{run_number}_005.hdf5'  # D1. G2P (GADGET to Python).
Filename_new = f"B_E_{run_number}_005_P2G.hdf5"

OldSnapfile = h5py.File(Filename_old, 'r')      
NewSnapfile = h5py.File(Filename_new, 'w')  # Python to GADGET, or P2G.
F = Filename_old[len(Path.cwd() + '/RunGadget/Energy_Exchange/E_HQ_100000_D1/output/'):-5]

# Particle masses
Masses = OldSnapfile['PartType1/Masses'].value 
Pos = OldSnapfile['PartType1/Coordinates'].value
Vel = OldSnapfile['PartType1/Velocities'].value  
V = OldSnapfile['PartType1/Potential'].value     
M = Masses
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
vx -= np.median(vx)
vy -= np.median(vy)
vz -= np.median(vz)

# M_limit = np.sum(M)  # total mass
IDs = np.argsort(R)

x_IDs = x[IDs]
y_IDs = y[IDs]
z_IDs = z[IDs]
vx_IDs = vx[IDs]
vy_IDs = vy[IDs]
vz_IDs = vz[IDs]
R_IDs = R[IDs]
V_IDs = V[IDs]
M_IDs = M[IDs]

N_total = x.shape[0]
N_particles_per_bin = 500
N_bins = N_total / N_particles_per_bin

(bin_radius_arr, x_GoodIDs_arr, y_GoodIDs_arr, z_GoodIDs_arr,
 vx_GoodIDs_rand_arr, vy_GoodIDs_rand_arr, vz_GoodIDs_rand_arr,
 M_GoodIDs_arr, vx_GoodIDs_rand_norm_arr, vy_GoodIDs_rand_norm_arr,
 vz_GoodIDs_rand_norm_arr, vx_final_arr, vy_final_arr, vz_final_arr,
 K_init_mean_in_bin_arr, K_rand_mean_in_bin_arr,
 K_rand_norm_mean_in_bin_arr, K_final_mean_in_bin_arr,
 V_mean_in_bin_arr, Ratio_init_mean_in_bin_arr,
 Ratio_rand_mean_in_bin_arr, Ratio_norm_mean_in_bin_arr) = ([] for i in range(22))

# Divide structure into mass-bins. Favoured over radial bins, as outer region of structure has less particles.
for i in range(N_bins):
    (vx_unbound_norm_i_arr, vy_unbound_norm_i_arr, vz_unbound_norm_i_arr,
     vx_unbound_norm_i_rand_arr, vy_unbound_norm_i_rand_arr, vz_unbound_norm_i_rand_arr,
     vx_unbound_norm_i_zero_arr, vy_unbound_norm_i_zero_arr,
     vz_unbound_norm_i_zero_arr) = ([] for i in range(9))

    GoodIDs = np.arange(i * N_particles_per_bin, (i + 1) * N_particles_per_bin)
    x_GoodIDs = x_IDs[GoodIDs]
    y_GoodIDs = y_IDs[GoodIDs]
    z_GoodIDs = z_IDs[GoodIDs]
    vx_GoodIDs = vx_IDs[GoodIDs]
    vy_GoodIDs = vy_IDs[GoodIDs]
    vz_GoodIDs = vz_IDs[GoodIDs]
    M_GoodIDs = M_IDs[GoodIDs]
    V_GoodIDs = V_IDs[GoodIDs]  # Shape: 500
    R_min = R_IDs[GoodIDs][0]
    R_max = R_IDs[GoodIDs][-1] 
    # 1.st randomization
    a = np.random.uniform(low=0.5, high=1.5, size=(N_particles_per_bin,))  # Shape: 500
    b = np.random.uniform(low=0.5, high=1.5, size=(N_particles_per_bin,))  # Shape: 500
    c = np.random.uniform(low=0.5, high=1.5, size=(N_particles_per_bin,))  # Shape: 500
    vx_GoodIDs_rand = a * vx_GoodIDs  # Shape: 500
    vy_GoodIDs_rand = b * vy_GoodIDs  # Shape: 500
    vz_GoodIDs_rand = c * vz_GoodIDs  # Shape: 500
    v_GoodIDs_rand = ravf.modulus(vx_GoodIDs_rand, vy_GoodIDs_rand, vz_GoodIDs_rand)  # Shape: 500    
    v_GoodIDs = ravf.modulus(vx_GoodIDs, vy_GoodIDs, vz_GoodIDs)  # Shape: 500
    K_init = E_kin(v_GoodIDs)  # Kinetic energy before 1.st randomization
    K_rand = E_kin(v_GoodIDs_rand)  # -||- after -||-
    K_init_mean = np.mean(K_init)
    K_rand_mean = np.mean(K_rand)
    print('K_init_mean: ', K_init_mean)
    print('K_rand_mean: ', K_rand_mean)
    K_init_mean_in_bin_arr.append(K_init_mean)
    K_rand_mean_in_bin_arr.append(K_rand_mean) 
    E_tot_rand = V_GoodIDs + K_rand
    UnboundIDs_rand = np.where(E_tot_rand > 0.)  # Unbound particles. Tuple with 24 entries. (IDs of 19 unbound particles)
    BoundIDs_rand = np.where(E_tot_rand <= 0.)  # Bound particles.
    # Split particles into bound and unbound
    vx_unbound = vx_GoodIDs_rand[UnboundIDs_rand]
    vy_unbound = vy_GoodIDs_rand[UnboundIDs_rand]
    vz_unbound = vz_GoodIDs_rand[UnboundIDs_rand]
    # print('vx_unbound.shape: ', vx_unbound.shape)  # 23
    vx_bound = vx_GoodIDs_rand[BoundIDs_rand]
    vy_bound = vy_GoodIDs_rand[BoundIDs_rand]
    vz_bound = vz_GoodIDs_rand[BoundIDs_rand]
    Ratio_init = np.sqrt(np.abs(V_GoodIDs) / K_init)
    Ratio_rand = np.sqrt(np.abs(V_GoodIDs) / K_rand)  # Shape: 500
    # Ratio = Ratio[GoodIDs]
    Ratio_rand_unbound = Ratio_rand[UnboundIDs_rand]
    Ratio_init_mean = np.mean(Ratio_init)
    Ratio_rand_mean = np.mean(Ratio_rand)
    Ratio_init_mean_in_bin_arr.append(Ratio_init_mean)
    Ratio_rand_mean_in_bin_arr.append(Ratio_rand_mean)
    for i in range(len(UnboundIDs_rand[0])):
        vx_unbound_norm_i = vx_unbound[i] * np.random.uniform(low=.8, high=1.) * Ratio_rand_unbound[i]  # Multiplies velocities with random number between 0.8 and 1 (1 not included)
        vy_unbound_norm_i = vy_unbound[i] * np.random.uniform(low=.8, high=1.) * Ratio_rand_unbound[i]
        vz_unbound_norm_i = vz_unbound[i] * np.random.uniform(low=.8, high=1.) * Ratio_rand_unbound[i]
        vx_unbound_norm_i_arr.append(vx_unbound_norm_i)
        vy_unbound_norm_i_arr.append(vy_unbound_norm_i)
        vz_unbound_norm_i_arr.append(vz_unbound_norm_i)
    vx_unbound_norm = np.asarray(vx_unbound_norm_i_arr)
    vy_unbound_norm = np.asarray(vy_unbound_norm_i_arr)
    vz_unbound_norm = np.asarray(vz_unbound_norm_i_arr)
    v_GoodIDs_rand_norm = ravf.modulus(vx_unbound_norm, vy_unbound_norm, vz_unbound_norm)
    v_GoodIDs_bound = ravf.modulus(vx_bound, vy_bound, vz_bound)
    v_new = np.concatenate([v_GoodIDs_bound, v_GoodIDs_rand_norm])
    K_rand_norm = E_kin(v_new)  # Kinetic energy after 1.st randomization and subsequent normalization
    K_rand_norm_mean = np.mean(K_rand_norm)
    K_rand_norm_mean_in_bin_arr.append(K_rand_norm_mean)
    Ratio_norm = np.sqrt(np.abs(V_GoodIDs) / K_rand_norm)
    Ratio_norm_mean = np.mean(Ratio_norm)
    Ratio_norm_mean_in_bin_arr.append(Ratio_norm_mean)
    E_tot_new = V_GoodIDs + E_kin(v_new)

    # This does not give the right result. There should be zero unbound perticles here! Is the sorting wrong?
    for i in range(len(E_tot_new)):
        if E_tot_new[i] > 0.:
            print('E_tot_new check. This is an unbound particle!', i)

    UnboundIDs_new = np.where(E_tot_new > 0.)
    print('len(UnboundIDs_new[0]): ', len(UnboundIDs_new[0]))
    x_GoodIDs_arr.append(x_GoodIDs)
    y_GoodIDs_arr.append(y_GoodIDs)
    z_GoodIDs_arr.append(z_GoodIDs)
    M_GoodIDs_arr.append(M_GoodIDs)
    V_mean_in_bin = np.mean(V_GoodIDs)
    V_mean_in_bin_arr.append(V_mean_in_bin)
    K_Ratio = np.sqrt(K_init_mean / K_rand_norm)
    vx = np.concatenate([vx_bound, vx_unbound_norm])
    vx *= K_Ratio
    vy = np.concatenate([vy_bound, vy_unbound_norm])
    vy *= K_Ratio
    vz = np.concatenate([vz_bound, vz_unbound_norm])
    vz *= K_Ratio
    v_final = ravf.modulus(vx, vy, vz)
    K_final = E_kin(v_final)  # Kinetic energy after 1.st randomization and subsequent normalization
    K_final_mean = np.mean(K_final)
    K_final_mean_in_bin_arr.append(K_final_mean)
    vx_final_arr.append(vx)
    vy_final_arr.append(vy)
    vz_final_arr.append(vz)

# Save kinetic energies to textfile
'''
K_init_mean_in_bin_arr = np.asarray(K_init_mean_in_bin_arr)
K_rand_mean_in_bin_arr = np.asarray(K_rand_mean_in_bin_arr)
K_rand_norm_mean_in_bin_arr = np.asarray(K_rand_norm_mean_in_bin_arr)
K_final_mean_in_bin_arr = np.asarray(K_final_mean_in_bin_arr)
V_mean_in_bin_arr = np.asarray(V_mean_in_bin_arr)
Ratio_init_mean_in_bin_arr = np.asarray(Ratio_init_mean_in_bin_arr)
Ratio_rand_mean_in_bin_arr = np.asarray(Ratio_rand_mean_in_bin_arr)
Ratio_norm_mean_in_bin_arr = np.asarray(Ratio_norm_mean_in_bin_arr)

x = np.array((K_init_mean_in_bin_arr, K_rand_mean_in_bin_arr, K_rand_norm_mean_in_bin_arr,
              K_final_mean_in_bin_arr, V_mean_in_bin_arr, Ratio_init_mean_in_bin_arr,
              Ratio_rand_mean_in_bin_arr, Ratio_norm_mean_in_bin_arr))
x = x.transpose()
np.savetxt(F + '_Kinetic_energies.txt', x, delimiter=' ',
           header='\t <K_i> \t\t <K_rand> \t\t <K_rand_norm> \t\t <K_final> \t\t <V_mean> \t\t <Ratio_i>  \t\t <Ratio_rand> \t\t <Ratio_norm> \t')
'''

x = np.asarray(x_GoodIDs_arr)
y = np.asarray(y_GoodIDs_arr)
z = np.asarray(z_GoodIDs_arr)
vx = np.asarray(vx_final_arr)
vy = np.asarray(vy_final_arr)
vz = np.asarray(vz_final_arr)
Masses = np.asarray(M_GoodIDs_arr)
x = np.concatenate(x, axis=0)
y = np.concatenate(y, axis=0)
z = np.concatenate(z, axis=0)
vx = np.concatenate(vx, axis=0)
vy = np.concatenate(vy, axis=0)
vz = np.concatenate(vz, axis=0)
Masses = np.concatenate(Masses, axis=0)
OldSnapfile.copy('/Header', NewSnapfile, '/Header')  # copy header to new snapshot

Pos = np.array([x, y, z])
Pos = Pos.transpose() 
Vel = np.array([vx, vy, vz])
Vel = Vel.transpose() 

NewSnapfile['PartType1/Masses'] = Masses          
NewSnapfile['PartType1/Coordinates'] = Pos
NewSnapfile['PartType1/Velocities'] = Vel

# Set Ndm:
Ndm = NewSnapfile['PartType1/Coordinates'].shape[0]
Narray = np.array([0, Ndm, 0, 0, 0, 0], dtype=np.int32)
NewSnapfile['Header'].attrs.modify('NumPart_ThisFile', Narray)
NewSnapfile['Header'].attrs.modify('NumPart_Total', Narray)

NewSnapfile.close()       
OldSnapfile.close()
