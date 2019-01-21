
# -*- coding: utf-8 -*-

import h5py
import numpy as np
# from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# import IPython
# from matplotlib.colors import LogNorm
# import time
# from pylab import *
# from scipy.stats import norm
# import matplotlib.mlab as mlab
# import getSnapshotValues

# Filename = desktopPath / 'RunGadget/G_HQ_1000000_test\
#            /output/HQ10000_G0.8_2_000.hdf5'

Snapshot_files = ['0G00_IC_000', '0G20_Final_000', 'OMG00_001_IC_000',
                  'OMG20_Final_000', 'ics_10MPC_128_022',
                  'ICS_10mpc_res256_022'
                  ]

Filename = Snapshot_files[0] + '.hdf5'
SnapshotFile = h5py.File(Filename, 'r')

# radial and tangential velocities
v_t1_arr, v_t2_arr = ([] for i in range(2))

# Initialize velocities
v_r, v_theta, v_phi = np.zeros([1000000, 1])
v_t = np.zeros([1000000, 3])
for i in range(1000000):
    v_r[i] = np.divide(np.dot(Rvector[:, i], v_vector[:, i]),
                       linalg.norm(Rvector[:, i]))
    v_t[i] = np.divide(np.cross(Rvector[:, i], v_vector[:, i], axis=0),
                       linalg.norm(Rvector[:, i]))
    v_theta[i] = ((vxnew[i] * ycl[i] - xcl[i] * vynew[i]) /
                  (xcl[i] ** 2 + ycl[i] ** 2))
    v_phi[i] = ((zcl[i] * (xcl[i] * vxnew[i] + ycl[i] * vynew[i])
                - (xcl[i] ** 2 + ycl[i] ** 2) * vznew[i]) /
                ((xcl[i] ** 2 + ycl[i] ** 2 + zcl[i] ** 2)
                * np.sqrt(xcl[i] ** 2 + ycl[i] ** 2)))

plt.figure(1)
plt.xlabel(r'$v_r, v_{\theta}$ and $v_{\phi}$')
# plt.xlabel(r'$v_{\theta}$ and $v_{\phi}$ of particles 400 to 500 kpc\
#            from centre of structure')
plt.ylabel('Number of particles')
plt.title(r'VDF of Hernquist structure with $10^6$ particles')
plt.hist(v_theta, bins=40, histtype='step', color='red', range=(-2, 2),
         label=r'$v_{\theta}$', lw=2)
# plt.hist(v_theta, bins=300, histtype='step', color='red',
#          range=(-2, 2), label=r'$v_{\theta}$', normed=True, lw=2)
plt.hist(v_phi, bins=40, histtype='step', color='skyblue',
         range=(-2, 2), label=r'$v_{\phi}$', lw=2)
plt.hist(v_r, bins=40, histtype='step', color='black',
         range=(-2, 2), label=r'$v_r$', lw=2)
plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
           frameon=True, loc=2, handlelength=2.5)
plt.show()

# Plot abs(v), og plot så lin-log, log-lin, log-log.
# Plot det hele ved 3 forskellige radielle bins.
# Proev at binne i log(v)
# Og lav et fit til exp(-v^2 / 2 s^2), bare for at se forskellen på formen

'''
v_ttrans = np.transpose(v_t)
print('v_ttrans = ', v_ttrans)

# Components of first direction vector for tangent plane

bx = np.ones(1000000)
by = -(vxnew*zcl - vznew*xcl)/(vznew*ycl - vynew*zcl)
bz = -(xcl + ycl*by)/(zcl)

# direction vectors for tangent plane

B1 = np.array([bx, by, bz])
print('B1 = ', B1)

B2 = zeros([1000000, 3])
for i in range(1000000):
    B2[i] = np.cross(Rvector[:, i], B1[:, i]))
print('B2 = ', B2)

# normalized direction vectors for tangent plane

t1, t2 = zeros([1000000, 3])
B3 = np.transpose(B2)

for i in range(1000000):
    t1[i] = np.divide(B1[:, i], linalg.norm(B1[:, i]))
    t2[i] = np.divide(B3[:, i], linalg.norm(B3[:, i]))
print('t1 = ', t1)
print('t2 = ', t2)

# split v_t into two components
v_t1, v_t2 = zeros([1000000, 1])

for i in range(1000000):
    v_t1[i] = np.dot(v_t[i, :], t1[i, :])
    v_t2[i] = np.dot(v_t[i, :], t2[i, :])
print('v_t1 = ', v_t1)
print('v_t2 = ', v_t2)
'''
