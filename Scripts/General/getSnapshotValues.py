# -*- coding: utf-8 -*-

import h5py
import definePaths as dp
import numpy as np
import radius_and_velocity_funcs as ravf
import dataclasses
from typing import IO


@dataclasses
Class LoadHalo:
    Filename: IO = dp.desktopPath / 'RunGadget/G_HQ_1000000_test/output/\
               HQ10000_G0.8_2_000.hdf5'

    def read_hdf5(self):
        SnapshotFile = h5py.File(Filename, 'r')
        return SnapshotFile

    def get_positions(self):
        Pos = SnapshotFile['PartType1/Coordinates'].value
        return Pos

    def get_velocities(self):
        Vel = SnapshotFile['PartType1/Velocities'].value
        return Vel

    def get_potential(self):
        V = SnapshotFile['PartType1/Potential'].value
        return V

    def cartesian_positions(self):
        x = Pos[:, 0]
        y = Pos[:, 1]
        z = Pos[:, 2]
        return x, y, z

    def cartesian_velocities(self):
        vx = Vel[:, 0]
        vy = Vel[:, 1]
        vz = Vel[:, 2]
        return vx, vy, vz

    def center_of_largest_cluster(self):
        """Finds the particle with the lowest potential
        which is in the center of the largest cluster."""
        minV = np.argmin(V)
        return minV

    def centralized_coords(self):
        """Changes x, y and z so that the cluster is centered."""
        xC = x[minV]
        yC = y[minV]
        zC = z[minV]
        return xC, yC, zC

    def centralized_velocities(self):
        """Changes vx, vy and vz so that the velocities are centered."""
        vxC = vx[minV]
        vyC = vy[minV]
        vzC = vz[minV]
        return vxC, vyC, vzC


R_xyz = ravf.modulus(x, y, z)
R = ravf.modulus(x - xC, y - yC, z - zC)

R_limit_min = 400.
R_limit_max = 500.
R_limit = 100.

# Removes all particles that is far away from the cluster.
GoodIDs_1 = np.where(R < R_limit_max)
GoodIDs_2 = np.where(R < R_limit)
GoodIDs_3 = np.where((R < R_limit_max) * (R > R_limit_min))

# Cluster
xcl = x[GoodIDs_1]
ycl = y[GoodIDs_1]
zcl = z[GoodIDs_1]
vxcl = vx[GoodIDs_1]
vycl = vy[GoodIDs_1]
vzcl = vz[GoodIDs_1]
vxnew = vx[GoodIDs_1] - np.median(vxcl)
vynew = vy[GoodIDs_1] - np.median(vycl)
vznew = vz[GoodIDs_1] - np.median(vzcl)
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
