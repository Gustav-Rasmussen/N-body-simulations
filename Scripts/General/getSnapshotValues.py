# -*- coding: utf-8 -*-

from dataclasses import dataclass
import h5py
import numpy as np
from pathlib import Path
from typing import IO

# import definePaths as dp
# import radius_and_velocity_funcs as ravf

# data_folder = Path.home() / 'Documents/Hdf5/'
# filename: IO = data_folder / '0G00_IC_000.hdf5'
# print((Path.home() / 'Documents/Hdf5/0G00_IC_000.hdf5').is_file())
# print(f"filename: {filename}")

data_folder = Path.home() / 'Documents/Hdf5/'


@dataclass
class LoadHalo:
    '''Class for loading a halo.'''
    filename: str = '0G00_IC_000.hdf5'

    def __post_init__(self):
        self.read_arepo_snapshot()
        # self.centralized_coords()
        # self.radial_cut()
        # self.centralized_velocities()

    def read_arepo_snapshot(self):
        filepath = data_folder / self.filename
        with h5py.File(filepath, 'r') as snapshotfile:
            pos = snapshotfile['PartType1/Coordinates']
            vel = snapshotfile['PartType1/Velocities']
            V = snapshotfile['PartType1/Potential']
            x = pos[:, 0]
            y = pos[:, 1]
            z = pos[:, 2]
            vx = vel[:, 0]
            vy = vel[:, 1]
            vz = vel[:, 2]
            ID_minV = np.argmin(V)
        return x, y, z, vx, vy, vz, ID_minV, V

    '''
    def radial_cut(self, r_cut=100):
        GoodIDs = np.where(self.x ** 2 + self.y ** 2 + self.z ** 2 < r_cut ** 2)
        x = self.x[GoodIDs]
        y = self.y[GoodIDs]
        z = self.z[GoodIDs]
        vx = self.vx[GoodIDs]
        vy = self.vy[GoodIDs]
        vz = self.vz[GoodIDs]
        V = self.V[GoodIDs]

    def centralized_coords(self):
        """Changes x, y and z so that the cluster is centered."""
        x = self.x - self.x[self.ID_minV]
        y = self.y - self.y[self.ID_minV]
        z = self.z - self.z[self.ID_minV]

    def centralized_velocities(self):
        """Changes vx, vy and vz so that the velocities are centered."""
        vx = self.vx - np.medium(self.vx)
        vy = self.vy - np.medium(self.vy)
        vz = self.vz - np.medium(self.vz)
    '''


halo = LoadHalo('0G00_IC_000.hdf5')
print(halo.read_arepo_snapshot())
# print(halo.centralized_coords())

"""
R_xyz = ravf.modulus(x, y, z)
R = ravf.modulus(x - xC, y - yC, z - zC)

R_limit_min = 400.
R_limit_max = 500.
# R_limit = 100.

# Removes all particles that is far away from the cluster.
GoodIDs_1 = np.where(R < R_limit_max)
GoodIDs_2 = np.where(R < R_limit)
# GoodIDs_3 = np.where((R < R_limit_max) * (R > R_limit_min))

# Cluster
xcl = x[GoodIDs_1]
ycl = y[GoodIDs_1]
zcl = z[GoodIDs_1]
vxcl = vx[GoodIDs_1]
vycl = vy[GoodIDs_1]
vzcl = vz[GoodIDs_1]
# vxnew = vx[GoodIDs_1] - np.median(vxcl)
# vynew = vy[GoodIDs_1] - np.median(vycl)
# vznew = vz[GoodIDs_1] - np.median(vzcl)
R_hob_par = R[GoodIDs_1]
Rvector = np.array([xcl, ycl, zcl])  # positions
v_vector = np.array([vxnew, vynew, vznew])  # velocities
Vcl = V[GoodIDs_1]
Rcl = R[GoodIDs_1]

# Now slice the cluster into a rectangular shape still 1000 kpc wide,
# but only 100 kpc tall
GoodIDs_rec = np.where((R < R_limit) * (yC - 50.0 < y) * (y < yC + 50.0))

xclrec = x[GoodIDs_rec]
yclrec = y[GoodIDs_rec]
zclrec = z[GoodIDs_rec]
vxclrec = vx[GoodIDs_rec]
vyclrec = vy[GoodIDs_rec]
vzclrec = vz[GoodIDs_rec]

vxnew = vx[GoodIDs_rec] - np.median(vxclrec)
vynew = vy[GoodIDs_rec] - np.median(vyclrec)
vznew = vz[GoodIDs_rec] - np.median(vzclrec)

Vclrec = V[GoodIDs_rec]
Rclrec = R[GoodIDs_rec]

bins_202 = 0
bins_102 = 0
# Reduce number of radial bins in analysis code.
# This makes them larger and they therefore contain more particles.
larger_fewer_bins = 1
largest_R_limit = 1  # Analyze larger volume of structure, set R_limit to 10000.
large_R_limit = 0  # Analyze large volume of structure, sets R_limit to 5000.

IC_R_middle = 0
keep_IC_R_middle = 0
new_R_middle = 0
large_R_middle = 0
R_bin_automatic = 0

if large_R_middle:
    R_middle = 10 ** 1.5  # 10 ** 1.3

# make R_limit_min and R_limit_max selection automatic
R_limit_min, R_limit_max = R_middle

# min_binning_R = -1.5
# max_binning_R = np.log10(500.0)
# nr_binning_bins = 300

a = 0
x0 = x
while (len(x0) < 10000 or a == 0):
    R_limit_min = R_limit_min - .000005
    R_limit_max = R_limit_max + .000005
    a = 1
    GoodIDs = np.where((R < R_limit_max) * (R > R_limit_min))
    x0 = x[GoodIDs[0]]

DoInnerCut = 0
if DoInnerCut:
    GoodIDs = np.where(R < R_limit_max)
else:
    GoodIDs = np.where((R < R_limit_max) * (R > R_limit_min))

x, y, z = x[GoodIDs], y[GoodIDs], z[GoodIDs]
vx, vy, vz = vx[GoodIDs], vy[GoodIDs], vz[GoodIDs]
vx -= np.median(vx)
vy -= np.median(vy)
vz -= np.median(vz)

# if test or A or B or E:
#     nr_binning_bins = 102
# if CS1 or CS2 or CS3:
#     nr_binning_bins = 53

min_binning_R_unitRmax = .00001  # end-value of first bin
max_binning_R_unitRmax = 1.0  # end-value of last bin
nr_binning_bins = 1000.0  # number of bins 1000.0
"""
