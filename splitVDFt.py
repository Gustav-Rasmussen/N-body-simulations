
# -*- coding: utf-8 -*-

import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
from pylab import *
from scipy.stats import norm
import matplotlib.mlab as mlab

Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G0.8_2_000.hdf5'
#Filename = 'OMG20_Final_000.hdf5'

#SnapshotFile = h5py.File('0G00_IC_000.hdf5','r')
#SnapshotFile = h5py.File('0G20_Final_000.hdf5','r')
#SnapshotFile = h5py.File('OMG00_001_IC_000.hdf5','r')
#SnapshotFile = h5py.File('OMG20_Final_000.hdf5','r')
#SnapshotFile = h5py.File('ics_10MPC_128_022.hdf5','r')
#SnapshotFile = h5py.File('ICS_10mpc_res256_022.hdf5','r')
#SnapshotFile = h5py.File(Filename,'r')
SnapshotFile = h5py.File(Filename,'r') 

Pos = SnapshotFile['PartType1/Coordinates'].value 
Vel = SnapshotFile['PartType1/Velocities'].value  
V = SnapshotFile['PartType1/Potential'].value     

x = Pos[:,0]
y = Pos[:,1]
z = Pos[:,2]
vx = Vel[:,0]
vy = Vel[:,1]
vz = Vel[:,2]

minV  = np.argmin(V)

xC  = x[minV]
yC  = y[minV]
zC  = z[minV]
vxC = vx[minV]
vyC = vy[minV]
vzC = vz[minV]

R = ((x-xC)**2+(y-yC)**2+(z-zC)**2)**0.5
R_limit_min = 400.
R_limit_max = 500.
GoodIDs = np.where(R<R_limit_max)

GoodIDs2 = np.where((R<R_limit_max)*(R>R_limit_min))

xcl =  x[GoodIDs]
ycl =  y[GoodIDs]
zcl =  z[GoodIDs]
vxcl = vx[GoodIDs]
vycl = vy[GoodIDs]
vzcl = vz[GoodIDs] 
vxnew = vx[GoodIDs] - np.median(vxcl)
vynew = vy[GoodIDs] - np.median(vycl)
vznew = vz[GoodIDs] - np.median(vzcl) 
R_hob_par = R[GoodIDs]
Rvector =  np.array([xcl, ycl, zcl]) # positions
v_vector = np.array([vxnew, vynew, vznew]) # velocities
    
# radial and tangential velocities
v_t1_arr = []
v_t2_arr = []
v_r = zeros([1000000,1])
v_t = zeros([1000000,3])

for i in range(1000000):
    
    v_r[i] = np.divide(np.dot(Rvector[:,i],v_vector[:,i]),linalg.norm(Rvector[:,i]))
    v_t[i] = np.divide(np.cross(Rvector[:,i],v_vector[:,i],axis=0),linalg.norm(Rvector[:,i]))

# v_theta and v_phi

v_theta = zeros([1000000,1])
v_phi = zeros([1000000,1])
 

for i in range(1000000):

    v_theta[i] = (vxnew[i]*ycl[i] - xcl[i]*vynew[i])/(xcl[i]**2 + ycl[i]**2)
    v_phi[i] = (zcl[i]*(xcl[i]*vxnew[i] + ycl[i]*vynew[i]) - (xcl[i]**2 + ycl[i]**2)*vznew[i])/((xcl[i]**2 + ycl[i]**2 + zcl[i]**2)*np.sqrt(xcl[i]**2 + ycl[i]**2))


print 'v_theta = ', v_theta
print 'v_phi = ', v_phi

plt.figure(1)
#plt.xlim(-4,1)
plt.xlabel(r'$v_r, v_{\theta}$ and $v_{\phi}$')
# plt.xlabel(r'$v_{\theta}$ and $v_{\phi}$ of particles 400 to 500 kpc from centre of structure')
plt.ylabel('Number of particles')
plt.title(r'VDF of Hernquist structure with $10^6$ particles')

plt.hist(v_theta,bins=40,histtype='step',color='red',range=(-2,2),label=r'$v_{\theta}$',lw=2)
# plt.hist(v_theta,bins=300,histtype='step',color='red',range=(-2,2),label=r'$v_{\theta}$',normed=True,lw=2)

plt.hist(v_phi,bins=40,histtype='step',color='skyblue',range=(-2,2),label=r'$v_{\phi}$',lw=2)

plt.hist(v_r,bins=40,histtype='step',color='black',range=(-2,2),label=r'$v_r$',lw=2)

plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)
plt.show()





# Plot abs(v), og plot så lin-log, log-lin, log-log. Så kan vi kigge på det sammen tirsdag. Plot det hele ved 3 forskellige radielle bins. 

# Kan du binne i log(v)?

# Og så selvfølgelig et fit til exp(-v^2/2s^2), bare for at se forskellen på formen


'''
v_ttrans = np.transpose(v_t)
print 'v_ttrans = ', v_ttrans

# Components of first direction vector for tangent plane

bx = np.ones(1000000)
by = -(vxnew*zcl - vznew*xcl)/(vznew*ycl - vynew*zcl)
bz = -(xcl + ycl*by)/(zcl)


# direction vectors for tangent plane

B1 = np.array([bx, by, bz])

print 'B1 = ', B1

B2 = zeros([1000000,3])
for i in range(1000000):
    B2[i] = np.cross(Rvector[:,i],B1[:,i]))

print 'B2 = ', B2


# normalized direction vectors for tangent plane

t1 = zeros([1000000,3])
t2 = zeros([1000000,3])
B3 = np.transpose(B2)
for i in range(1000000):


    t1[i] = np.divide(B1[:,i],linalg.norm(B1[:,i]))
    t2[i] = np.divide(B3[:,i],linalg.norm(B3[:,i]))


print 't1 = ', t1
print 't2 = ', t2


# split v_t into two components

v_t1 = zeros([1000000,1])
v_t2 = zeros([1000000,1])

for i in range(1000000):

    v_t1[i] = np.dot(v_t[i,:],t1[i,:])
    v_t2[i] = np.dot(v_t[i,:],t2[i,:])


print 'v_t1 = ', v_t1
print 'v_t2 = ', v_t2
'''

