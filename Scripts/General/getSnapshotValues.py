# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import h5py
import numpy as np
from pathlib import Path
from pprint import pprint as pp
from typing import IO

# import definePaths as dp
# import radius_and_velocity_funcs as ravf

data_folder = Path.home() / 'Documents/Hdf5/'


@dataclass
class LoadHalo:
    '''Class for loading a halo.'''
    V: np.ndarray = field(init=False, repr=False)
    x: np.ndarray = field(init=False, repr=False)
    y: np.ndarray = field(init=False, repr=False)
    z: np.ndarray = field(init=False, repr=False)
    vx: np.ndarray = field(init=False, repr=False)
    vy: np.ndarray = field(init=False, repr=False)
    vz: np.ndarray = field(init=False, repr=False)
    ID_minV: np.ndarray = field(init=False, repr=False)
    filename: str = '0G00_IC_000.hdf5'

    def __post_init__(self):
        self.read_arepo_snapshot()
        self.centralized_coords()
        self.radial_cut()
        self.centralized_velocities()

    def read_arepo_snapshot(self):
        filepath = data_folder / self.filename
        with h5py.File(filepath, 'r') as snapshotfile:
            pos = snapshotfile['PartType1/Coordinates']
            vel = snapshotfile['PartType1/Velocities']
            self.V = snapshotfile['PartType1/Potential'][:]
            self.x = pos[:, 0]
            self.y = pos[:, 1]
            self.z = pos[:, 2]
            self.vx = vel[:, 0]
            self.vy = vel[:, 1]
            self.vz = vel[:, 2]
            self.ID_minV = np.argmin(self.V)

    def radial_cut(self, r_cut=100):
        GoodIDs = np.where(self.x ** 2 + self.y ** 2 + self.z ** 2 < r_cut ** 2)
        self.x = self.x[GoodIDs]
        self.y = self.y[GoodIDs]
        self.z = self.z[GoodIDs]
        self.vx = self.vx[GoodIDs]
        self.vy = self.vy[GoodIDs]
        self.vz = self.vz[GoodIDs]
        self.V = self.V[GoodIDs]

    def centralized_coords(self):
        """Changes x, y and z so that the cluster is centered."""
        self.x = self.x - self.x[self.ID_minV]
        self.y = self.y - self.y[self.ID_minV]
        self.z = self.z - self.z[self.ID_minV]

    def centralized_velocities(self):
        """Changes vx, vy and vz so that the velocities are centered."""
        self.vx = self.vx - np.median(self.vx)
        self.vy = self.vy - np.median(self.vy)
        self.vz = self.vz - np.median(self.vz)

    def modulus(self, *args):
        """Modulus of vector of arbitrary size."""
        return sum([i ** 2 for i in args]) ** .5


halo = LoadHalo('0G00_IC_000.hdf5')
'''
print(f"Filename: {halo.filename}")
pp(f"x: {halo.x}")
pp(f"y: {halo.y}")
pp(f"z: {halo.z}")
pp(f"vx: {halo.vx}")
pp(f"vy: {halo.vy}")
pp(f"vz: {halo.vz}")
pp(f"Potential: {halo.V}")
print(f"ID_minV: {halo.ID_minV}")
'''

R_xyz = halo.modulus(halo.x, halo.y, halo.z)
# R = halo.modulus(x - xC, y - yC, z - zC)

"""
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
