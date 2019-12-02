# -*- coding: utf-8 -*-

# Standard library imports
import h5py
import os.path
from pathlib import Path
import sys
import time

# Third party imports
import IPython
import numpy as np
from pylab import *
import scipy
from scipy.stats import norm

# Local application
from bin_halo import bin_halo_by_mass

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
R = modulus(x - xC, y - yC, z - zC)
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

x, y, z, vx, vy, vz, Masses = bin_halo_by_mass()

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
x = np.array((K_init_mean_in_bin_arr, K_rand_mean_in_bin_arr,
              K_rand_norm_mean_in_bin_arr,
              K_final_mean_in_bin_arr, V_mean_in_bin_arr, Ratio_init_mean_in_bin_arr,
              Ratio_rand_mean_in_bin_arr, Ratio_norm_mean_in_bin_arr))
x = x.transpose()
np.savetxt(F + '_Kinetic_energies.txt', x, delimiter=' ',
           header='\t <K_i> \t\t <K_rand> \t\t <K_rand_norm> \t\t <K_final> \t\t <V_mean> \t\t <Ratio_i>  \t\t <Ratio_rand> \t\t <Ratio_norm> \t')
'''


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
