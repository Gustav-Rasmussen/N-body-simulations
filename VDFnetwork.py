# -*- coding: utf-8 -*-

from __future__ import division
import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
from pylab import *
import pylab
from scipy.stats import norm
import matplotlib.mlab as mlab
import scipy
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D


# test
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G1.0_0_000.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G1.2_1_005.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G0.8_2_000.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G0.8_2_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G1.2_3_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G1.2_5_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G1.2_7_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G1.2_9_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/Hernquist10000_G1.0_10_009.hdf5'


# test2
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_0_000.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_5_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_10_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_15_005.hdf5'

    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_005.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_010.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_015.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_020.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_025.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_030.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_035.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_040.hdf5'
    #Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_045.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_18_053.hdf5'

#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_20_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/Hernquist10000_G1.0_25_005.hdf5'




# A

#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G1.0_0_000.hdf5'  # This file is already run in VDF.py, from test2. re-use that one.
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G1.0_5_005.hdf5'  # This file is already run in VDF.py, from test2. re-use that one.
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G1.0_10_005.hdf5' # This file is already run in VDF.py, from test2. re-use that one.

#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G1.0_40_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G1.2_46_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G0.8_47_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G1.0_48_009.hdf5'
#Filename = '/Users/gustav.c.rasmussen/nosync/RunGadget/G_HQ_1000000_A/output/Hernquist10000_G1.0_48_093.hdf5'





# B



Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G1.0_0_000.hdf5'  # This file is already run in VDF.py, from test2. re-use that one.
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G1.0_5_005.hdf5' 
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G1.0_10_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G1.0_198_000.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G1.0_198_093.hdf5'


##Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G1.0_160_005.hdf5'
##Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G1.05_196_005.hdf5'
##Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/Hernquist10000_G0.95_197_005.hdf5'







# C




#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G1.0_0_000.hdf5' 
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G1.0_5_005.hdf5' 
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G1.0_10_005.hdf5'

#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G1.0_40_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G1.2_46_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G0.8_47_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G1.0_48_009.hdf5'
#Filename = '/Users/gustav.c.rasmussen/nosync/RunGadget/G_HQ_1000000_C/output/Hernquist10000_G1.0_48_093.hdf5'





# D



#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G1.0_0_000.hdf5' 
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G1.0_5_005.hdf5' 
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G1.0_10_005.hdf5' 

#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G1.0_160_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G1.05_196_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G0.95_197_005.hdf5'
#Filename = '/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G1.0_198_009.hdf5'
#Filename = '/Users/gustav.c.rasmussen/nosync/RunGadget/G_HQ_1000000_D/output/Hernquist10000_G1.0_198_093.hdf5'










# Filename = 'Hq1000000_150311_000.hdf5'
# Filename = 'OsipkovMerritt_150310_000.hdf5'

SnapshotFile = h5py.File(Filename,'r')

#F = Filename[len('/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test/output/'):-5]
#F = 'test2_' + Filename[len('/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_test2/output/'):-5]
#F = 'A_' + Filename[len('/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_A/output/'):-5]
#F = 'A_' + Filename[len('/Users/gustav.c.rasmussen/nosync/RunGadget/G_HQ_1000000_A/output/'):-5]
F = 'B_' + Filename[len('/Users/gustav.c.rasmussen/Desktop/RunGadget/G_HQ_1000000_B/output/'):-5]




#Gamma = -3.0
#Beta  = 1.0

test  = 0
test2 = 0
A     = 0
B     = 1
C     = 0
D     = 0


keep_IC_R_middle = 0
new_R_middle     = 0
large_R_middle   = 1



if keep_IC_R_middle:

    if test:

        if F.startswith('Hernquist10000_G'):
            if   Gamma == -1.5:     # logr = -0.70, r = 10**-0.70  
                    R_middle = 10**-0.70 
            elif Gamma == -2.0:     # logr = -0.25, r = 10**-0.25
                    R_middle = 10**-0.25
            elif Gamma == -2.5:     # logr = 0.0 , r = 10**0.0               
                    R_middle = 10**-0.0 
            elif Gamma == -3.0:     # logr = 0.30 , r = 10**0.30
                    R_middle = 10**-0.30

        if F.startswith('OsipkovMerritt_'):

            if   Gamma == -1.5:     # logr =  
                R_middle =  0
            elif Gamma == -2.0:     # logr = 
                R_middle = 0
            elif Gamma == -2.5:     # logr =               
                R_middle = 0
            elif Gamma == -3.0:     # logr = 
                R_middle = 0

    if test2:

        if F.startswith('test2_' + 'Hernquist10000_G'):
            if   Gamma == -1.5:     # logr = 
                    R_middle = 0 
            elif Gamma == -2.0:     # logr = 
                    R_middle = 0
            elif Gamma == -2.5:     # logr =               
                    R_middle =  0
            elif Gamma == -3.0:     # logr = 
                    R_middle = 0

        if F.startswith('OsipkovMerritt_'):

            if   Gamma == -1.5:     # logr =  
                R_middle =  0
            elif Gamma == -2.0:     # logr = 
                R_middle = 0
            elif Gamma == -2.5:     # logr =               
                R_middle = 0
            elif Gamma == -3.0:     # logr = 
                R_middle = 0

if new_R_middle:# Choose new R_middle for each file.

    if test:

        if F == 'Hernquist10000_G1.0_0_000': # 0.th/IC file
            if   Gamma == -1.5:     # logr = -0.70, r = 10**-0.70  
                R_middle = 10**-0.70 
            elif Gamma == -2.0:     # logr = -0.25, r = 10**-0.25
                R_middle = 10**-0.25
            elif Gamma == -2.5:     # logr = 0.0 , r = 10**0.0               
                R_middle = 10**-0.0 
            elif Gamma == -3.0:     # logr = 0.30 , r = 10**0.30
                R_middle = 10**-0.30

        if F == 'Hernquist10000_G1.2_1_005': # 1.st file
            if   Gamma == -1.5:     # logr =  
                R_middle =  10**-0.55
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.4
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**-0.1
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.2

        if F == 'Hernquist10000_G0.8_2_005': # 2.nd file

            if   Gamma == -1.5:     # logr =  
                R_middle =  0
            elif Gamma == -2.0:     # logr = 
                R_middle = 0
            elif Gamma == -2.5:     # logr =                
                R_middle =  0
            elif Gamma == -3.0:     # logr = 
                R_middle = 0

        if F == 'Hernquist10000_G1.2_3_005': # 3.rd file
            if   Gamma == -1.5:     # logr =  
                R_middle =  10**-0.6
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.4
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**0.0
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.4

        if F == 'Hernquist10000_G1.2_5_005': # 5.th file
            if   Gamma == -1.5:     # logr =  
                R_middle = 10**-0.45 
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.35
            elif Gamma == -2.5:     # logr =               
                R_middle =  10**-0.1
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.45

        if F == 'Hernquist10000_G1.2_7_005': # 7.th file
            if   Gamma == -1.5:     # logr =  
                R_middle =  10**-0.35
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.25
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**-0.1
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.48

        if F == 'Hernquist10000_G1.2_9_005': # 9.th file
            if   Gamma == -1.5:     # logr =   
                R_middle = 10**-0.35
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.3
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**-0.15
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.5

        if F == 'Hernquist10000_G1.0_10_009': # 10.th file

            if   Gamma == -1.5:     # logr =   
                R_middle = 10**-0.25
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.15
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**0.0
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.5

    if test2:

        if F == 'test2_' + 'Hernquist10000_G1.0_0_000': # 0.th/IC file
            if   Gamma == -1.5:     # logr = 
                R_middle = 10**-0.7
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.38
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**-0.0
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.25

        if F == 'test2_' + 'Hernquist10000_G1.0_5_005': # 5.th file
            if   Gamma == -1.5:     # logr =  
                R_middle =  10**-0.5
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.18
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**0.0
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.45

        if F == 'test2_' + 'Hernquist10000_G1.0_10_005': # 10.th file

            if   Gamma == -1.5:     # logr =  
                R_middle =  10**-0.4
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.2
            elif Gamma == -2.5:     # logr =                
                R_middle =  10**0.0
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.38

        if F == 'test2_' + 'Hernquist10000_G1.0_15_005': # 15.th file
            if   Gamma == -1.5:     # logr =  
                R_middle =  10**-0.25
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.14
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**0.0
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.38

        if F == 'test2_' + 'Hernquist10000_G1.0_20_005': # 20.th file
            if   Gamma == -1.5:     # logr =  
                R_middle = 10**-0.24
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.12
            elif Gamma == -2.5:     # logr =               
                R_middle =  10**0.0
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.5

        if F == 'test2_' + 'Hernquist10000_G1.0_25_005': # 25.th file
            if   Gamma == -1.5:     # logr =  
                R_middle =  10**-0.17
            elif Gamma == -2.0:     # logr = 
                R_middle = 10**-0.08
            elif Gamma == -2.5:     # logr =               
                R_middle = 10**0.05
            elif Gamma == -3.0:     # logr = 
                R_middle = 10**0.45






if large_R_middle:
    #R_middle =  10**1.3
    R_middle =  10**1.5

                












#print 'R_middle = ', R_middle        

# Hq1000000_150311_000.hdf5
# Gamma = -1.5, logr = -0.75, r = 10^-0.75   
# Gamma = -2, logr = -0.35, r = 10^-0.35     
# Gamma = -2.5, logr = 0.0 , r = 10^0.0      

# OsipkovMerritt_150310_000.hdf5

# beta = 0.0 , logr = -1.0 , r = 10^-1.0   
# beta = 0.87 , logr = 0.5,  r = 10^0.5   
# beta = 0.07 , logr = -0.5, r = 10^-0.5  
# beta = 0.4  , logr = 0.0, r = 10^0.0    
# beta = 1.0  , logr = 1.2, r = 10^1.2     

# Gamma = -1.5, logr = -0.7, r = 10^-0.7   
# Gamma = -2, logr = -0.28, r = 10^-0.28   
# Gamma = -2.5, logr = 0.0, r = 10^0.0     

# Hernquist10000_G0.8_2_000.hdf5
# Gamma = -1.5, logr = -0.65, r = 10^-0.65 
# Gamma = -2, logr = -0.35, r = 10^-0.35   
# Gamma = -2.5, logr = -0.08, r = 10^-0.08

# Hernquist10000_G1.2_9_005.hdf5
## Gamma = -1, logr = -0.5, r = 10^-0.5 
# Gamma = -1.5, logr = -0.4, r = 10^-0.4
# Gamma = -2, logr = -0.25, r = 10^-0.25 
# Gamma = -2.5, logr = -0.15, r = 10^-0.15 
## Gamma = -3, logr = 0.5, r = 10^0.5 

#print 'R_middle = ', R_middle
#IPython.embed()

Pos = SnapshotFile['PartType1/Coordinates'].value 
Vel = SnapshotFile['PartType1/Velocities'].value  
V   = SnapshotFile['PartType1/Potential'].value     

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

# make R_limit_min and R_limit_max selection automatic
R_limit_min = R_middle
R_limit_max = R_middle

a = 0 # makes sure the while loop is entered.
x0 = x
while len(x0)<10000 or a==0:
    R_limit_min = R_limit_min - 0.000005
    R_limit_max = R_limit_max + 0.000005
    a += 1
    GoodIDs = np.where((R<R_limit_max)*(R>R_limit_min))

    ##    print 'R.shape = ', R.shape
    ##    print 'x = ', x
    ##    print 'x.shape = ', x.shape
    ##    print 'len(GoodIDs) = ', len(GoodIDs[0])
    ##    print 'GoodIDs = ', GoodIDs[0]

    x0 =  x[GoodIDs[0]]
    ##    print 'a = ', a
    ##    print 'len(x) = ', len(x0)

#print 'len(x0) = ', len(x0)
#print 'len(x) = ', len(x)
#IPython.embed()
   
##DoInnerCut = False
##if DoInnerCut:
##    GoodIDs = np.where(R<R_limit_max)
##else:
##    GoodIDs = np.where((R<R_limit_max)*(R>R_limit_min))

x =  x[GoodIDs]
y =  y[GoodIDs]
z =  z[GoodIDs]
vx = vx[GoodIDs]
vy = vy[GoodIDs]
vz = vz[GoodIDs] 
vx = vx - np.median(vx)
vy = vy - np.median(vy)
vz = vz - np.median(vz)

nr_binning_bins = 102

Fig1_xy                           = 0 # Make switches to control figures, print statements, binning etc.
Fig2_xz                           = 0
Fig3_3D_xyz                       = 0
Fig4_vspherical_hist_old          = 0
Fig5_vspherical_hist_logfail_new  = 0
Fig6_v_hist_logfail               = 0
Fig7_vspherical_hist_logfail_old  = 0
Fig8_vspherical_hist_log_vpvn     = 0
Fig9_VPhiminus                    = 0
Fig10_concatenate_x789            = 0
Fig11_vspherical_hist_log_n123    = 0
calc_sigma_binned_lin_radius      = 1
print_sigma                       = 0
Fig12_n123_sigma                  = 0
Fig12_x789_sigma                  = 0

Fig12_vr_vtheta_vphi_sigma        = 0
Fig12_vr_vtheta_vphi_vt_sigma     = 1

Fig13_vspherical_hist_old         = 0
velocitycheck                     = 0
vsphericalold                     = 0
vsphericalnew                     = 1
vsphericalnew_sigma               = 1
plotvelocitycheckold              = 0
plotvelocitychecknew              = 0
vbin                              = 0
x14_25_36_same_length             = 0
print_vp_vn                       = 0
print_Vp_Vn                       = 0
print_x123456                     = 0
print_sigma_binned_lin_radius     = 0
print_sigma_unbinned              = 0
save_r_v_as_txt                   = 0
Fig14_sigmas                      = 0
Fig15_gaussian_fits               = 0
Fig16_q_fits                      = 0
Fig17_compare_fits                = 0

if Fig1_xy:
    figure()
    plt.subplot(121)
    plt.plot(x,y)
    plt.xlabel(r'$x_{cluster}$')
    plt.ylabel(r'$y_{cluster}$')
    plt.title(r'positions ($N = %i$, $\gamma = %.2f $)' %(len(x),Gamma) )
    plt.grid()

    plt.subplot(122)
    plt.plot (x,z)
    plt.xlabel(r'$x_{cluster}$')
    plt.ylabel(r'$z_{cluster}$')
    plt.grid()

if Fig2_xz:
    figure()
    plt.subplot(121)
    plt.plot(x,y,'o', ms=1)
    plt.xlabel(r'$x_{cluster}$')
    plt.ylabel(r'$y_{cluster}$')
    plt.title(r'positions ($N = %i$, $\gamma = %.2f $)' %(len(x),Gamma) )
    plt.grid()

    plt.subplot(122)
    plt.plot (x,z,'o', ms=1)
    plt.xlabel(r'$x_{cluster}$')
    plt.ylabel(r'$z_{cluster}$')
    plt.grid()

def randrange(n, vmin, vmax): # 3D scatterplot of positions
    return (vmax-vmin)*np.random.rand(n) + vmin

if Fig3_3D_xyz:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    n = 100
    for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        ax.scatter(x, y, z, c=c, marker=m)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D view of halo structure.($N = %i$, $\gamma = %.2f $)' %(len(x),Gamma) )

##sigma_1 =0.205
##sigma_2 =0.335
##min_binning_R = -1.5
##max_binning_R = np.log10(500.0)
##nr_binning_bins = 300

# Use 3 simple particles to check the velocities (vr and vtheta)
if velocitycheck:
    x[0] = 0.
    y[0] = 0.
    z[0] = 1.
    vx[0] = 1.
    vy[0] = 1.
    vz[0] = 0.

    x[1] = 0.
    y[1] = 1.
    z[1] = 0.
    vx[1] = 1.
    vy[1] = 0.
    vz[1] = 0.

    x[2] = 1.
    y[2] = 0.
    z[2] = 0.
    vx[2] = 1.
    vy[2] = 0.
    vz[2] = 0.

# radial and tangential velocities
if vsphericalnew:
    r = np.sqrt(x**2 + y**2+ z**2)
    Phi = scipy.arctan2(y,x)
    Theta = scipy.arccos(z/r)
    VR = scipy.sin(Theta)*scipy.cos(Phi) * vx + scipy.sin(Theta)*scipy.sin(Phi) * vy + scipy.cos(Theta) * vz
    VTheta = scipy.cos(Theta)*scipy.cos(Phi) * vx + scipy.cos(Theta)*scipy.sin(Phi) * vy - scipy.sin(Theta) * vz
    VPhi = - scipy.sin(Phi) * vx + scipy.cos(Phi) * vy
    VT = VTheta + VPhi

# Use 3 simple particles to check the velocities (vr and vtheta) continued:

if velocitycheck:
    print 'VR[0] = ', VR[0]           # = 0.0
    print 'VTheta[0] = ', VTheta[0]   # = 1.0
    print 'VPhi[0] = ', VPhi[0]       # = 1.0
    print 'VR[1] = ', VR[1]           # =  -4.37114e-08
    print 'VTheta[1] = ', VTheta[1]   # = 1.91069e-15
    print 'VPhi[1] = ', VPhi[1]       # = -1.0
    print 'VR[2] = ', VR[2]           # =  1.0
    print 'VTheta[2] = ', VTheta[2]   # =  -4.37114e-08
    print 'VPhi[2] = ', VPhi[2]       # =  0.0

if vsphericalold:
    Rvector =  np.array([x, y, z])    # positions
    vvector =  np.array([vx, vy, vz]) # velocities    
    v_r = zeros([len(x),1])
    v_t = zeros([len(x),3])
    print 'Rvector.shape = ', Rvector.shape
    print 'vvector.shape = ', vvector.shape
    for i in range(len(x)):
        v_r[i] = np.divide(np.dot(Rvector[:,i],vvector[:,i]),linalg.norm(Rvector[:,i]))
        v_t[i] = np.divide(np.cross(Rvector[:,i],vvector[:,i],axis=0),linalg.norm(Rvector[:,i]))
    print 'v_r = ', v_r
    print 'v_r.shape = ', v_r.shape
    print 'v_t = ', v_t
    print 'v_t.shape = ', v_t.shape
    v = (vx**2 + vy**2 + vz**2)**0.5
    # v_theta and v_phi
    v_theta = zeros([len(x),1])
    v_phi = zeros([len(x),1])
    for i in range(len(x)):
        if  x[i]**2 + y[i]**2 > 0.:
            v_theta[i] = (x[i]*vy[i] - y[i]*vx[i])/(x[i]**2 + y[i]**2)
    for i in range(len(x)):
     #   if (x[i]**2+y[i]**2+z[i]**2)**0.5 > 0.:
     #       if z[i]!=(x[i]**2+y[i]**2+z[i]**2)**0.5:
        if ( (x[i]**2+y[i]**2+z[i]**2)**0.5 > 0.)*(z[i]!=(x[i]**2+y[i]**2+z[i]**2)**0.5):
            v_phi[i] = ((x[i]**2+y[i]**2+z[i]**2)**0.5*vz[i] - z[i]*v_r[i])/((x[i]**2+y[i]**2+z[i]**2)*(1 - (z[i]/((x[i]**2+y[i]**2+z[i]**2)**0.5))**2)**0.5)
      #  v_phi[i] = (z[i]*(x[i]*vx[i] + y[i]*vy[i]) - (x[i]**2 + y[i]**2)*vz[i])/((x[i]**2 + y[i]**2 + z[i]**2)*np.sqrt(x[i]**2 + y[i]**2))
    #     v_theta[i] = np.dot()
    #     v_phi[i]   = np.cross()
    print 'v_r[0] = ', v_r[0]         #  = [ 0.]
    print 'v_theta[0] = ', v_theta[0] #  = [ 0.]
    print 'v_phi[0] = ', v_phi[0]     #  = [ 0.]

if plotvelocitycheckold: # Check old velocities are correct
    y1 = v_theta**2 + v_phi**2      # v_t^2
    y2 = v**2 - v_r**2              # v_t^2

    figure()
    plt.plot (y1, y2,'o', ms=1.)
    plt.xlabel(r'$ v_{\theta}^2 + v_{\phi}^2 $')
    plt.ylabel(r'$  v^2 - v_r^2$')
    plt.title(r'check if $ v_{\theta}^2 + v_{\phi}^2 =  v^2 - v_r^2 $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()

    figure()
    plt.ylim(-10,10)
    plt.plot (v_r, v_theta,'o', ms=1.)
    plt.xlabel(r'$ v_r $')
    plt.ylabel(r'$  v_{\theta}$')
    plt.title(r'check if $ v_{\theta} = v_r $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()

    figure()
    plt.plot (v_r, v_phi,'o', ms=1.)
    plt.xlabel(r'$ v_r $')
    plt.ylabel(r'$  v_{\Phi}$')
    plt.title(r'check if $ v_{\Phi} = v_r $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()

    figure()
    plt.xlim(-20,20)
    plt.plot (v_theta, v_phi,'o', ms=1.)
    plt.xlabel(r'$ v_{\theta} $')
    plt.ylabel(r'$  v_{\phi}$')
    plt.title(r'check if $ v_{\phi} = v_{\theta} $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()
    plt.show()

if plotvelocitychecknew:   # Check new velocities are correct
    y1 = VTheta**2 + VPhi**2      # v_t^2
    y2 = v**2 - VR**2             # v_t^2

    figure()
    plt.plot (y1, y2,'o', ms=1.)
    plt.xlabel(r'$ v_{\theta}^2 + v_{\phi}^2 $')
    plt.ylabel(r'$  v^2 - v_r^2$')
    plt.title(r'check if $ v_{\theta}^2 + v_{\phi}^2 =  v^2 - v_r^2 $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()

    figure()
    plt.plot (VR, VTheta,'o', ms=1.)
    plt.xlabel(r'$ v_r $')
    plt.ylabel(r'$  v_{\theta}$')
    plt.title(r'check if $ v_{\theta} = v_r $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()

    figure()
    plt.plot (VR, VPhi,'o', ms=1.)
    plt.xlabel(r'$ v_r $')
    plt.ylabel(r'$  v_{\Phi}$')
    plt.title(r'check if $ v_{\Phi} = v_r $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()

    figure()
    plt.plot (VTheta, VPhi,'o', ms=1.)
    plt.xlabel(r'$ v_{\Theta} $')
    plt.ylabel(r'$  v_{\Phi}$')
    plt.title(r'check if $ v_{\Phi} = v_{\Theta} $ ($N=%i$, $\gamma = %.2f$)' % (len(x),Gamma) )
    plt.grid()

if Fig4_vspherical_hist_old:
    nr_binning_bins_v = 30       
    v_arr = []
    # v_binning_arr = np.logspace(min_binning_v,max_binning_v,nr_binning_bins_v) # Array
    v_binning_arr = np.linspace(v_limit_min,v_limit_max,nr_binning_bins_v)

    plt.figure()
    plt.subplot(121)
    plt.xlabel(r'$v$, $v_r$, $v_t$, $ v_{\theta}$ and $ v_{\phi}$')
    plt.ylabel('Number of particles')
    plt.title(r'f(v) (Hernquist structure, $N=%i$, $\gamma = %.2f$' % (len(x),Gamma) )
    plt.hist(v,bins=100,histtype='step',color='red',range=(v_limit_min,v_limit_max),label=r'$v$',lw=2)
    plt.hist(v_r,bins=100,histtype='step',color='blue',range=(v_limit_min,v_limit_max),label=r'$v_r$',lw=2)
    plt.hist(v_t_len,bins=100,histtype='step',color='Indigo',range=(v_limit_min,v_limit_max),label=r'$v_t$',lw=2)
    plt.hist(v_theta,bins=100,histtype='step',color='black',range=(v_limit_min,v_limit_max),label=r'$v_{\theta}$',lw=2)
    plt.hist(v_phi,bins=100,histtype='step',color='cyan',range=(v_limit_min,v_limit_max),label=r'$v_{\phi}$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=1,handlelength=2.5)

    plt.subplot(122)
    plt.xlabel(r'$\log v$, $ \log v_r$,  $ \log v_t$, $ \log v_{\theta}$ and $ \log v_{\phi}$')
    plt.hist(np.log10(np.absolute(v)),bins=100,histtype='step',color='red',range=(-5,0),label=r'$\log v$',lw=2)
    plt.hist(np.log10(np.absolute(v_r)),bins=100,histtype='step',color='blue',range=(-5,0),label=r'$\log v_r$',lw=2)
    plt.hist(np.log10(np.absolute(v_t_len)),bins=100,histtype='step',color='Indigo',range=(-5,0),label=r'$\log v_r$',lw=2)
    plt.hist(np.log10(np.absolute(v_theta)),bins=100,histtype='step',color='black',range=(-5,0),label=r'$\log v_{\theta}$',lw=2)
    plt.hist(np.log10(np.absolute(v_phi)),bins=100,histtype='step',color='cyan',range=(-5,0),label=r'$\log v_{\phi}$',lw=2)
    plt.legend(prop=dict(size=11), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

def func_1(x, a, b):
    return a * x*np.exp(-b * x**2.)

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
    
if Fig5_vspherical_hist_logfail_new:
    fig = plt.figure()
    ax = fig.add_subplot(121)

    (mu, sigma) = norm.fit(VR)
    n, bins, patches = plt.hist(VR, 100,histtype='step',color='red',label=r'$ v_r $', alpha=0.75)
    # n, bins, patches = plt.hist(VR, 100,histtype='step', normed=1,color='red',label=r'$ v_r $', alpha=0.75)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    #popt, pcov = curve_fit(func_4, xdata, ydata)
    #y_fit = func_4(xdata,popt[0],popt[1],popt[2])
    #plt.plot(xdata,y_fit,'--',lw=3,color='red',label=r'$v_r-fit= a \cdot (1- (1 - q )\cdot b \cdot x^2)^{(\frac{q}{1-q})}$, $ q = %.3f $' %popt[1])
    #popt, pcov = curve_fit(func_2, xdata, ydata)
    #y_fit = func_2(xdata,popt[0],popt[1])
    #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$v_r-fit= a \cdot e^{-b \cdot x^2}$ ($\mu=%.3f$, $\sigma=%.3f$)' %(mu, sigma))

    (mu, sigma) = norm.fit(VTheta)
    n, bins, patches = plt.hist(VTheta, 100,histtype='step',color='blue',label=r'$v_{\theta}$', alpha=0.75)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    ##popt, pcov = curve_fit(func_4, xdata, ydata)
    ##y_fit = func_4(xdata,popt[0],popt[1],popt[2])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='SkyBlue',label=r'$v_{\theta}-fit= a \cdot (1- (1 - q )\cdot b \cdot x^2)^{(\frac{q}{1-q})}$, $ q = %.3f $' %popt[1])
    ##popt, pcov = curve_fit(func_2, xdata, ydata)
    ##y_fit = func_2(xdata,popt[0],popt[1])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='blue',label=r'$v_{\theta}-fit= a \cdot e^{-b \cdot x^2}$ ($\mu=%.3f$, $\sigma=%.3f$)' %(mu, sigma))

    (mu, sigma) = norm.fit(VPhi)
    n, bins, patches = plt.hist(VPhi, 100,histtype='step',color='green',label=r'$ v_{\phi}$', alpha=0.75)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    ##popt, pcov = curve_fit(func_4, xdata, ydata)
    ##y_fit = func_4(xdata,popt[0],popt[1],popt[2])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='green',label=r'$v_{\phi}-fit= a \cdot (1- (1 - q )\cdot b \cdot x^2)^{(\frac{q}{1-q})}$, $ q = %.3f $' %popt[1])
    ##popt, pcov = curve_fit(func_2, xdata, ydata)
    ##y_fit = func_2(xdata,popt[0],popt[1])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='cyan',label=r'$v_{\phi}-fit= a \cdot e^{-b \cdot x^2}$ ($\mu=%.3f$, $\sigma=%.3f$)' %(mu, sigma))

    plt.xlabel(r'$v_r$, $v_{\theta}$ and $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\gamma = %.2f$,  File = %s )' %(len(x), Gamma , F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=1,handlelength=2.5)
    plt.grid()

    ax.set_yscale('log')

    subplot(122)

    (mu, sigma) = norm.fit(np.log10(np.absolute(VR)))
    n, bins, patches = plt.hist(np.log10(np.absolute(VR)), 100,histtype='step',color='red',label=r'$ \log |v_r| $', alpha=0.75)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    ##popt, pcov = curve_fit(func_4_log, xdata, ydata)
    ##y_fit = func_4_log(xdata,popt[0],popt[1],popt[2])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='red',label=r'$\log |v_r|-fit= a \cdot log(x) \cdot (1- (1 - q )\cdot b \cdot log(x)^2)^{(\frac{q}{1-q})}$, $ q = %.3f $' %popt[1])
    ##popt, pcov = curve_fit(func_1_log, xdata, ydata)
    ##y_fit = func_1_log(xdata,popt[0],popt[1])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\log |v_r|-fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    (mu, sigma) = norm.fit(np.log10(np.absolute(VTheta)))
    n, bins, patches = plt.hist(np.log10(np.absolute(VTheta)), 100,histtype='step',color='blue', label=r'$ \log |v_{\theta}|$', alpha=0.75)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    ##popt, pcov = curve_fit(func_4_log, xdata, ydata)
    ##y_fit = func_4_log(xdata,popt[0],popt[1],popt[2])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='SkyBlue',label=r'$\log |v_{\theta}|-fit= a \cdot log(x) \cdot (1- (1 - q )\cdot b \cdot log(x)^2)^{(\frac{q}{1-q})}$, $ q = %.3f $' %popt[1])
    ##popt, pcov = curve_fit(func_1_log, xdata, ydata)
    ##y_fit = func_1_log(xdata,popt[0],popt[1])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='blue',label=r'$\log |v_{\theta}|-fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    (mu, sigma) = norm.fit(np.log10(np.absolute(VPhi)))
    n, bins, patches = plt.hist(np.log10(np.absolute(VPhi)), 100,histtype='step', color='green', label=r'$ \log |v_{\phi}|$', alpha=0.75)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    ##popt, pcov = curve_fit(func_4_log, xdata, ydata)
    ##y_fit = func_4_log(xdata,popt[0],popt[1],popt[2])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='green',label=r'$\log |v_{\phi}|-fit= a \cdot log(x) \cdot (1- (1 - q )\cdot b \cdot log(x)^2)^{(\frac{q}{1-q})}$, $ q = %.3f $' %popt[1])
    ##popt, pcov = curve_fit(func_1_log, xdata, ydata)
    ##y_fit = func_1_log(xdata,popt[0],popt[1])
    ##plt.plot(xdata,y_fit,'--',lw=3,color='cyan',label=r'$\log |v_{\phi}|-fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\log |v_r|$, $\log |v_{\theta}|$, $\log |v_{\phi}|$')
    plt.ylabel('number of particles')
    plt.title(r'$ f(\log |v|)$ ')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

if Fig6_v_hist_logfail:
    plt.figure()
    (mu, sigma) = norm.fit(np.log10(np.absolute(v)))
    n, bins, patches = plt.hist(np.log10(np.absolute(v)), 100,histtype='step', normed=1,color='blue',label=r'$\log v$', alpha=0.75)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata,popt[0],popt[1],popt[2])
    plt.plot(xdata,y_fit,'--',lw=3,color='SkyBlue', label=r'Fit to $\log v$')
    plt.xlabel(r'$\log v$')
    plt.ylabel('number of particles')
    plt.title(r'VDF ($\mu=%.2f$, $\sigma=%.2f$)' %(mu, sigma))
    plt.grid()
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

if vbin:
    for i in range(nr_binning_bins_v-2):      # loop over 0-998
        min_v_bin_i = v_binning_arr[i]    # start of bin
        max_v_bin_i = v_binning_arr[i+1]  # end of bin
        posv_par_inside_bin_i = np.where((v_hob_par>min_v_bin_i) * (v_hob_par<max_v_bin_i)) # position of particles inside a radial bin
        nr_par_inside_bin_i = len(posv_par_inside_bin_i)                       # number of particles inside a radial bin
        if nr_par_inside_bin_i == 0:
            continue                      

        v_inside_bin_i = v[posv_par_inside_bin_i]
        v_r_inside_bin_i = v_r[posv_par_inside_bin_i]
        v_t_inside_bin_i = v_t[posv_par_inside_bin_i]

        v_arr.append(v_inside_bin_i)
        v_r_arr.append(v_r_inside_bin_i)
        v_t_arr.append(v_t_inside_bin_i)
        nr_par_inside_bin.append(nr_par_inside_bin_i)

    plt.figure() # plot structure over velocity bins.
    plt.subplot(121)
    plt.xlabel(r'$v, v_r$ and $v_t$')
    plt.ylabel('Number of particles')
    plt.title(r'VDF (Hernquist structure, $10^6$ particles)')
    plt.hist(v_arr[15],bins=100,histtype='step',color='red',range=(v_limit_min,v_limit_max),label=r'$v$',lw=2)
    #plt.hist(v_t_arr[15],bins=100,histtype='step',color='black',range=(v_limit_min,v_limit_max),label=r'$v_t$',lw=2)
    plt.hist(v_r_arr[15],bins=100,histtype='step',color='blue',range=(v_limit_min,v_limit_max),label=r'$v_r$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=1,handlelength=2.5)
    plt.show()
    plt.hist(v_r,bins=100,histtype='step',color='skyblue',range=(v_limit_min,v_limit_max),label=r'$v_r$',lw=2)
    plt.hist(v_t,bins=100,histtype='step',color='black',range=(-4,4),label=r'$v_t$',lw=2)

    plt.subplot(122)
    plt.xlabel(r'$\log v$, $ \log v_r$ and $ \log v_t$')
    plt.hist(np.log10(np.absolute(v_arr)),bins=100,histtype='step',color='red',range=(-5,1),label=r'$\log v$',lw=2)
    plt.hist(np.log10(np.absolute(v_r)),bins=100,histtype='step',color='skyblue',range=(-5,1),label=r'$\log v_r$',lw=2)
    plt.hist(np.log10(np.absolute(v_t)),bins=100,histtype='step',color='black',range=(-5,1),label=r'$\log v_t$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

    plt.figure()
    plt.xlabel(r'$v_r$ and $v_t$')
    plt.ylabel('Number of particles')
    plt.title('velocity distributions')
    plt.hist(v_r_arr[5],bins=30,histtype='step',color='red',range=(-4,1),label=r'$v_r$ (bin 5)',normed=True,lw=2)
    plt.hist(v_r_arr[8],bins=30,histtype='step',color='skyblue',range=(-4,1),label=r'$v_r$ (bin 8)',normed=True,lw=2)
    plt.hist(v_r_arr[10],bins=300,histtype='step',color='black',range=(-1,1),label=r'$v_r$ (bin 10)',lw=2)
    plt.hist(0.5*v_t_arr[5],bins=30,histtype='step',color='green',range=(-4,1),label=r'$v_t$ (bin 5)',normed=True)
    plt.hist(0.5*v_t_arr[8],bins=30,histtype='step',color='blue',range=(-4,1),label=r'$v_t$ (bin 8)',normed=True)
    plt.hist(v_t_arr[10],bins=300,histtype='step',color='orange',range=(-1,1),label=r'$v_t$ (bin 10)')
    plt.hist(0.25*v_t_arr[10],bins=300,histtype='step',color='red',range=(-2,1),label=r'$\frac{1}{4}\cdot v_t$ (bin 10)')
    plt.hist(v_t_arr[10]*v_t_arr[10],bins=300,histtype='step',color='green',range=(-2,1),label=r'$v_t\cdot v_t$ (bin 10)')
    plt.hist(2*v_t_arr[10],bins=300,histtype='step',color='blue',range=(-2,1),label=r'$2 \cdot v_t$ (bin 10)')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

if Fig7_vspherical_hist_logfail_old:
    plt.figure() # plot structure over radial bins.
    plt.subplot(121)
    #plt.xlim(-4,1)
    plt.xlabel(r'$v_r, v_{\theta}$ and $v_{\phi}$')
    plt.ylabel('Number of particles')
    plt.title(r'VDF (Hernquist structure, $10^6$ particles). distance: 0.5 to 0.25 kpc from center ')
    plt.hist(v_theta,bins=100,histtype='step',color='red',range=(-0.7,1),label=r'$v_{\theta}$',lw=2)
    # plt.hist(v_theta,bins=300,histtype='step',color='red',range=(-2,2),label=r'$v_{\theta}$',normed=True,lw=2)
    plt.hist(v_phi,bins=100,histtype='step',color='skyblue',range=(-0.7,1),label=r'$v_{\phi}$',lw=2)
    plt.hist(v_r,bins=100,histtype='step',color='black',range=(-0.7,1),label=r'$v_r$',lw=2)
    # plt.hist(v2_arr**0.5,bins=40,histtype='step',color='green',range=(-2,2),label=r'$v_{total}$',lw=2)
    # plt.hist(v3,bins=40,histtype='step',color='green',range=(-2,2),label=r'$v_{total}$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=1,handlelength=2.5)

    plt.subplot(122)
    plt.xlabel(r'$\log v_r, \log v_{\theta}$ and $ \log v_{\phi}$')
    # plt.ylabel('Number of particles')
    # plt.title(r'VDF of Hernquist structure with $10^6$ particles')
    plt.hist(np.log10(np.absolute(v_theta)),bins=100,histtype='step',color='red',range=(-5,1),label=r'$\log v_{\theta}$',lw=2)
    # plt.hist(v_theta,bins=300,histtype='step',color='red',range=(-2,2),label=r'$v_{\theta}$',normed=True,lw=2)
    plt.hist(np.log10(np.absolute(v_phi)),bins=100,histtype='step',color='skyblue',range=(-5,1),label=r'$\log v_{\phi}$',lw=2)
    plt.hist(np.log10(np.absolute(v_r)),bins=100,histtype='step',color='black',range=(-5,1),label=r'$\log v_r$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

if calc_sigma_binned_lin_radius:
    R_hob_par = R[GoodIDs]
    v2 = vx**2+vy**2+vz**2

    sigma2            = []
    sigmarad2         = []
    sigmatheta2       = []
    sigmaphi2         = []
    sigmatan2         = []
    sigma             = []
    sigmarad          = []
    sigmatheta        = []
    sigmaphi          = []
    sigmatan          = []
    VR_sigmarad       = []
    VTheta_sigmatheta = []
    VPhi_sigmaphi     = []
    VT_sigmatan       = []
    r                 = []
    Phi               = []
    Theta             = []
    VR                = []
    VTheta            = []
    VPhi              = []
    VT                = []

    binning_arr       = np.linspace(R_limit_min,R_limit_max,nr_binning_bins) 
    bin_radius_arr    = []

    for i in range(nr_binning_bins-2):
    #for i in range(nr_binning_bins):    
        min_R_bin_i = binning_arr[i]    # start of bin
        max_R_bin_i = binning_arr[i+1]  # end of bin
        posR_par_inside_bin_i = np.where((R_hob_par>min_R_bin_i) & (R_hob_par<max_R_bin_i)) # position of particles inside a radial bin
        nr_par_inside_bin_i = len(posR_par_inside_bin_i[0]) 
        if nr_par_inside_bin_i == 0:
            continue

        r_i = np.sqrt(x[posR_par_inside_bin_i]**2 + y[posR_par_inside_bin_i]**2+ z[posR_par_inside_bin_i]**2)
        Phi_i = scipy.arctan2(y[posR_par_inside_bin_i],x[posR_par_inside_bin_i])
        Theta_i = scipy.arccos(z[posR_par_inside_bin_i]/r_i)
        VR_i = scipy.sin(Theta_i)*scipy.cos(Phi_i) * vx[posR_par_inside_bin_i] + scipy.sin(Theta_i)*scipy.sin(Phi_i) * vy[posR_par_inside_bin_i] + scipy.cos(Theta_i) * vz[posR_par_inside_bin_i]
        VTheta_i = scipy.cos(Theta_i)*scipy.cos(Phi_i) * vx[posR_par_inside_bin_i] + scipy.cos(Theta_i)*scipy.sin(Phi_i) * vy[posR_par_inside_bin_i] - scipy.sin(Theta_i) * vz[posR_par_inside_bin_i]
        VPhi_i = - scipy.sin(Phi_i) * vx[posR_par_inside_bin_i] + scipy.cos(Phi_i) * vy[posR_par_inside_bin_i]

        VT_i = (VTheta_i**2 + VPhi_i**2)**0.5
        #VT_i = VTheta_i + VPhi_i
        
        # sigmatan2
        vtan2_inside_bin_i = VT_i**2
        sigmatan2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(vtan2_inside_bin_i)
        sigmatan2.append(sigmatan2_inside_bin_i)
        #print sigmatan2_inside_bin_i, np.std(VT_i)**2
        #print sigmatan2_inside_bin_i, np.mean(VT_i**2), nr_par_inside_bin_i

        #sigma2 total
        v2_inside_bin_i = v2[posR_par_inside_bin_i]
        sigma2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(v2_inside_bin_i)
        sigma2.append(sigma2_inside_bin_i)
        bin_radius_arr.append((max_R_bin_i + min_R_bin_i)/2)

        #sigmarad2 radial
        vrad2_inside_bin_i = VR_i**2
        sigmarad2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(vrad2_inside_bin_i)
        sigmarad2.append(sigmarad2_inside_bin_i)

        #sigmatheta2
        VTheta2_inside_bin_i = VTheta_i**2
        sigmatheta2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VTheta2_inside_bin_i)
        sigmatheta2.append(sigmatheta2_inside_bin_i)

        #sigmaphi2
        VPhi2_inside_bin_i = VPhi_i**2
        sigmaphi2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VPhi2_inside_bin_i)
        sigmaphi2.append(sigmaphi2_inside_bin_i)

        sigma_i      = (sigma2[i])**0.5
        sigmarad_i   = (sigmarad2[i])**0.5
        sigmatheta_i = (sigmatheta2[i])**0.5
        sigmaphi_i   = (sigmaphi2[i])**0.5
        sigmatan_i   = (sigmatan2[i])**0.5

        sigma.append(sigma_i)
        sigmarad.append(sigmarad_i)
        sigmatheta.append(sigmatheta_i)
        sigmaphi.append(sigmaphi_i)
        sigmatan.append(sigmatan_i)

        r.append(r_i)   #save arrays
        Phi.append(Phi_i)
        Theta.append(Theta_i)
        VR.append(VR_i)
        VTheta.append(VTheta_i)
        VPhi.append(VPhi_i)
        VT.append(VT_i)
        #np.array(VT)
        
        VR_sigmarad.append(VR_i/sigmarad_i)
        VTheta_sigmatheta.append(VTheta_i/sigmatheta_i)
        VPhi_sigmaphi.append(VPhi_i/sigmaphi_i)
        VT_sigmatan.append(VT_i/sigmatan_i)

    sigma2      = np.array(sigma2) 
    sigmarad2   = np.array(sigmarad2)
    sigmatheta2 = np.array(sigmatheta2)
    sigmaphi2   = np.array(sigmaphi2)
    sigmatan2   = np.array(sigmatan2)
    sigma       = np.array(sigma)
    sigmarad    = np.array(sigmarad)
    sigmatheta  = np.array(sigmatheta)
    sigmaphi    = np.array(sigmaphi)
    sigmatan    = np.array(sigmatan)

    ##    print r'$\sigma_{tan} = $ '    , linalg.norm(sigmatan)
    ##    print r'$\sigma = $ '          , linalg.norm(sigma)
    ##    print r'$\sigma_{rad} = $ '    , linalg.norm(sigmarad)
    ##    print r'$\sigma_{\phi} = $ '   , linalg.norm(sigmaphi)
    ##    print r'$\sigma_{\theta} = $ ' , linalg.norm(sigmatheta)

    #print 'np.concatenate(np.array(VT_sigmatan),axis = 0) = ', np.concatenate(np.array(VT_sigmatan),axis = 0)
    #print sigmatan2_inside_bin_i, np.mean(VT_i**2)
    #IPython.embed()
    
    ##    r           = np.array(r)
    ##    Phi         = np.array(Phi)
    ##    Theta       = np.array(Theta)
    ##    VR          = np.array(VR)
    ##    VTheta      = np.array(VTheta)
    ##    VPhi        = np.array(VPhi)
    ##    VT          = np.array(VT)

    #print 'VR = ', VR
    #IPython.embed()

    r            = np.concatenate(np.array(r),axis = 0)
    Phi          = np.concatenate(np.array(Phi),axis = 0)
    Theta        = np.concatenate(np.array(Theta),axis = 0)
    VR           = np.concatenate(np.array(VR),axis = 0)
    VTheta       = np.concatenate(np.array(VTheta),axis = 0)
    VPhi         = np.concatenate(np.array(VPhi),axis = 0)
    VT           = np.concatenate(np.array(VT),axis = 0)
    VR_sigmarad           = np.concatenate(np.array(VR_sigmarad),axis = 0)
    VTheta_sigmatheta     = np.concatenate(np.array(VTheta_sigmatheta),axis = 0)
    VPhi_sigmaphi         = np.concatenate(np.array(VPhi_sigmaphi),axis = 0)
    VT_sigmatan           = np.concatenate(np.array(VT_sigmatan),axis = 0)

    #np.savetxt('v_sigma_Martin.txt',VT_sigmatan)
    #np.savetxt('vtan_Martin.txt',VT)
    #IPython.embed()

if Fig14_sigmas:
    plt.figure()
    plt.subplot(121)
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma2)
    plt.plot(x_plot,y_plot,'-o',ms=8,mew=0,color='red',label=r'$\log \sigma_{total}^2$')
    y_plot = np.log10(sigmarad2)
    plt.plot(x_plot,y_plot,'--s',ms=8,mew=0,color='blue',label=r'$\log \sigma_{r}^2$')
    y_plot = np.log10(sigmatheta2)
    plt.plot(x_plot,y_plot,'--v',ms=8,mew=0,color='green',label=r'$\log \sigma_{\theta}^2$')
    y_plot = np.log10(sigmaphi2)
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='black',label=r'$\log \sigma_{\phi}^2$')
    y_plot = np.log10(sigmatan2) 
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='Violet',label=r'$\log \sigma_{tan}^2$')
    plt.xlabel(r'$\log $r (kpc)' , fontsize=20)
    plt.ylabel(r'$\log \sigma^2$' , fontsize=20)
    plt.title(r'Velocity dispersions (File = %s, $\gamma=%.2f$)' %(F,Gamma) , fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=3,handlelength=2.5)
    plt.grid()

    plt.subplot(122)
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma)
    plt.plot(x_plot,y_plot,'-o',ms=8,mew=0,color='red',label=r'$\log \sigma_{total}$')
    y_plot = np.log10(sigmarad)
    plt.plot(x_plot,y_plot,'--s',ms=8,mew=0,color='blue',label=r'$\log \sigma_r$')
    y_plot = np.log10(sigmatheta)
    plt.plot(x_plot,y_plot,'--v',ms=8,mew=0,color='green',label=r'$\log \sigma_{\theta}$')
    y_plot = np.log10(sigmaphi)
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='black',label=r'$\log \sigma_{\phi}$')
    y_plot = np.log10(sigmatan) 
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='Violet',label=r'$\log \sigma_{tan}$')
    plt.xlabel(r'$\log $r (kpc)' , fontsize=20)
    plt.ylabel(r'$\log \sigma$' , fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=3,handlelength=2.5)
    plt.grid()

v_rp = []    # divide into 6 graphs
v_rn = []
v_thetap = []
v_thetan = []
v_phip = []
v_phin = []
v_tp = []
v_tn = []

if vsphericalold:
    for i in range(len(x)):
        if v_r[i] >= 0.:
            v_rp.append(v_r[i])
        else:
            v_rn.append(v_r[i])
    v_rp_arr = np.asarray(v_rp)
    v_rn_arr = np.asarray(v_rn)
    for i in range(len(x)):
        if v_theta[i] >= 0.:
            v_thetap.append(v_theta[i])
        else:
            v_thetan.append(v_theta[i])
    v_thetap_arr = np.asarray(v_thetap)
    v_thetan_arr = np.asarray(v_thetan)
    for i in range(len(x)):
        if v_phi[i] >= 0.:
            v_phip.append(v_phi[i])
        else:
            v_phin.append(v_phi[i])
    v_phip_arr = np.asarray(v_phip)
    v_phin_arr = np.asarray(v_phin)

if vsphericalnew:
    #IPython.embed()
    #for i in range(len(x)):
    for i in range(len(VR)):
        if VR[i] >= 0.:
            v_rp.append(VR[i])
        else:
            v_rn.append(VR[i])
    v_rp_arr = np.asarray(v_rp)
    v_rn_arr = np.asarray(v_rn)

    #for i in range(len(x)):
    for i in range(len(VTheta)):
        if VTheta[i] >= 0.:
            v_thetap.append(VTheta[i])
        else:
            v_thetan.append(VTheta[i])
    v_thetap_arr = np.asarray(v_thetap)
    v_thetan_arr = np.asarray(v_thetan)

    #for i in range(len(x)):
    for i in range(len(VPhi)):    
        if VPhi[i] >= 0.:
            v_phip.append(VPhi[i])
        else:
            v_phin.append(VPhi[i])
    v_phip_arr = np.asarray(v_phip)
    v_phin_arr = np.asarray(v_phin)

    #for i in range(len(x)):
    for i in range(len(VT)):
        if VT[i] >= 0.:
            v_tp.append(VT[i])
        else:
            v_tn.append(VT[i])
    v_tp_arr = np.asarray(v_tp)
    v_tn_arr = np.asarray(v_tn)

if print_vp_vn:
    ##    print 'v_rp_arr = ', v_rp_arr
    ##    print 'v_rp_arr.shape = ', v_rp_arr.shape
    ##    print 'v_rn_arr = ', v_rn_arr
    ##    print 'v_rn_arr.shape = ', v_rn_arr.shape
    ##    print 'v_thetap_arr = ', v_thetap_arr
    ##    print 'v_thetap_arr.shape = ', v_thetap_arr.shape
    ##    print 'v_thetan_arr = ', v_thetan_arr
    ##    print 'v_thetan_arr.shape = ', v_thetan_arr.shape
    ##    print 'v_phip_arr = ', v_phip_arr
    ##    print 'v_phip_arr.shape = ', v_phip_arr.shape
    ##    print 'v_phin_arr = ', v_phin_arr
    ##    print 'v_phin_arr.shape = ', v_phin_arr.shape

    print 'v_tp_arr = ', v_tp_arr
    print 'v_tp_arr.shape = ', v_tp_arr.shape
    print 'v_tn_arr = ', v_tn_arr
    print 'v_tn_arr.shape = ', v_tn_arr.shape

if Fig8_vspherical_hist_log_vpvn:
    plt.figure()
    plt.xlabel(r'$\log v_rp, \log v_{\theta}p$, $ \log v_{\phi}p$, $\log v_rn, \log v_{\theta}n$ and $ \log v_{\phi}n$')
    plt.ylabel('Number of particles')
    plt.title(r'Positive and negative f(v) ($N=%.3f$, $\gamma = %.1f$,  File = %s )' %(len(x), Gamma, F))
    plt.hist(np.log10(v_thetap_arr),bins=100,histtype='step',color='red',range=(-5,1),label=r'$\log v_{\theta}p$',lw=2)
    plt.hist(np.log10(v_phip_arr),bins=100,histtype='step',color='skyblue',range=(-5,1),label=r'$\log v_{\phi}p$',lw=2)
    plt.hist(np.log10(v_rp_arr),bins=100,histtype='step',color='black',range=(-5,1),label=r'$\log v_rp$',lw=2)
    plt.hist(np.log10(np.absolute(v_thetan_arr)),bins=100,histtype='step',color='green',range=(-5,1),label=r'$\log v_{\theta}n$',lw=2)
    plt.hist(np.log10(np.absolute(v_phin_arr)),bins=100,histtype='step',color='blue',range=(-5,1),label=r'$\log v_{\phi}n$',lw=2)
    plt.hist(np.log10(np.absolute(v_rn_arr)),bins=100,histtype='step',color='cyan',range=(-5,1),label=r'$\log v_rn$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

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

if print_x123456:
    print 'x1 = ', x1
    print 'x1.shape = ', x1.shape
    print 'x4.shape = ', x4.shape
    print 'v_thetap_arr.shape = ', v_thetap_arr.shape
    print 'v_thetan_arr.shape = ', v_thetan_arr.shape
    print 'x2 = ', x2
    print 'x2.shape = ', x2.shape
    print 'x5.shape = ', x5.shape
    print 'x3 = ', x3
    print 'x3.shape = ', x3.shape
    print 'x6.shape = ', x6.shape
    print 'type(x1) = ', type(x1)

if Fig9_VPhiminus: # test VPhi and VPhiminus = -VPhi
    VPhiminus = scipy.sin(Phi) * vx - scipy.cos(Phi) * vy
    plt.figure()
    plt.subplot(121)
    plt.xlabel(r' $ v_{\phi}$ , $ -v_{\phi} $,  $ \log |v_{\phi}| $ and $ \log |-v_{\phi}|$')
    plt.ylabel('Number of particles')
    plt.title(r' f(v) comparison ($N=%.3f$, $\gamma = %.1f$,  File = %s )' %(len(x), Gamma, F))
    plt.hist(VPhi,bins=100,histtype='step',color='red',range=(-5,1),label=r'$ v_{\phi}$',lw=2)
    plt.hist(VPhiminus,bins=100,histtype='step',color='skyblue',range=(-5,1),label=r'$ -v_{\phi}$',lw=2)
    plt.hist(np.log10(np.absolute(VPhi)),bins=100,histtype='step',color='green',range=(-5,1),label=r'$\log |v_{\phi}|$',lw=2)
    plt.hist(np.log10(np.absolute(VPhiminus)),bins=100,histtype='step',color='blue',range=(-5,1),label=r'$\log |-v_{\phi}|$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)
    plt.subplot(122)
    plt.xlabel(r'$\log v_rp + \log |v_rn|$, $\log v_{\theta}p + \log |v_{\theta}n|$ and $ \log v_{\phi}p + \log |v_{\phi}n|$')
    plt.ylabel('Number of particles')
    plt.title(r'Positive and negative f(v) summed ')
    plt.hist(np.log10(x1)+np.log10(np.absolute(x4)),bins=100,histtype='step',color='red',range=(-5,1),label=r'$\log v_{\theta}p + \log |v_{\theta}n|$',lw=2)
    plt.hist(np.log10(x2)+np.log10(np.absolute(x5)),bins=100,histtype='step',color='blue',range=(-5,1),label=r'$\log v_{\phi}p + \log |v_{\phi}n|$',lw=2)
    plt.hist(np.log10(x3)+np.log10(np.absolute(x6)),bins=100,histtype='step',color='green',range=(-5,1),label=r'$\log v_rp + \log |v_rn|$',lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

if vsphericalnew_sigma:
    VR_sigmarad_p = []
    VR_sigmarad_n = []
    VTheta_sigmatheta_p = []
    VTheta_sigmatheta_n = []
    VPhi_sigmaphi_p = []
    VPhi_sigmaphi_n = []
    VT_sigmatan_p = []
    VT_sigmatan_n = []

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

if print_Vp_Vn:
    ##    print 'VR_sigmarad_p_arr = ', VR_sigmarad_p_arr
    ##    print 'VR_sigmarad_p_arr.shape = ', VR_sigmarad_p_arr.shape
    ##    print 'VR_sigmarad_n_arr = ', VR_sigmarad_n_arr
    ##    print 'VR_sigmarad_n_arr.shape = ', VR_sigmarad_n_arr.shape
    ##    print 'VTheta_sigmatheta_p_arr = ', VTheta_sigmatheta_p_arr
    ##    print 'VTheta_sigmatheta_p_arr.shape = ', VTheta_sigmatheta_p_arr.shape
    ##    print 'VTheta_sigmatheta_n_arr = ', VTheta_sigmatheta_n_arr
    ##    print 'VTheta_sigmatheta_n_arr.shape = ', VTheta_sigmatheta_n_arr.shape
    ##    print 'VPhi_sigmaphi_p_arr = ', VPhi_sigmaphi_p_arr
    ##    print 'VPhi_sigmaphi_p_arr.shape = ', VPhi_sigmaphi_p_arr.shape
    ##    print 'VPhi_sigmaphi_n_arr = ', VPhi_sigmaphi_n_arr
    ##    print 'VPhi_sigmaphi_n_arr.shape = ', VPhi_sigmaphi_n_arr.shape
    print 'VT_sigmatan_p_arr = ', VT_sigmatan_p_arr
    print 'VT_sigmatan_p_arr.shape = ', VT_sigmatan_p_arr.shape
    print 'VT_sigmatan_n_arr = ', VT_sigmatan_n_arr
    print 'VT_sigmatan_n_arr.shape = ', VT_sigmatan_n_arr.shape
    ##    VTheta = np.array(VTheta)
    ##    VPhi   = np.array(VPhi)
    ##    VR_sigmarad = np.array(VR_sigmarad)
    ##    VTheta_sigmatheta = np.array(VTheta_sigmatheta)
    ##    VPhi_sigmaphi = np.array(VPhi_sigmaphi)

    if print_sigma_binned_lin_radius:
        print 'sigmarad2 = ', sigmarad2
        print 'sigmarad2.shape = ', sigmarad2.shape
        print 'sigmatheta2 = ', sigmatheta2
        print 'sigmatheta2.shape = ', sigmatheta2.shape
        print 'sigmaphi2 = ', sigmaphi2
        print 'sigmaphi2.shape = ', sigmaphi2.shape
        print 'sigmarad = ', sigmarad
        print 'sigmarad.shape = ', sigmarad.shape
        print 'sigmatheta = ', sigmatheta
        print 'sigmatheta.shape = ', sigmatheta.shape
        print 'sigmaphi = ', sigmaphi
        print 'sigmaphi.shape = ', sigmaphi.shape
        print 'VR = ', VR
        print 'VR.shape = ', VR.shape
        print 'VTheta = ', VTheta
        print 'VTheta.shape = ', VTheta.shape
        print 'VPhi = ', VPhi
        print 'VPhi.shape = ', VPhi.shape
        print 'VR_sigmarad.shape = ', (VR/sigmarad).shape
        print 'VR_sigmarad = ', VR/sigmarad
        print 'np.where(sigmarad == 0) = ', np.where(sigmarad == 0)
        print 'np.where(sigmatheta == 0) = ', np.where(sigmatheta == 0)
        print 'np.where(sigmaphi == 0) = ', np.where(sigmaphi == 0)

if Fig10_concatenate_x789:        # check new log, concatenate lists x1 and x4, x2 and x5, x3 and x6.
    x7 = np.asarray(x1 + list(np.absolute(v_thetan_arr)))
    x8 = np.asarray(x2 + list(np.absolute(v_phin_arr)))
    x9 = np.asarray(x3 + list(np.absolute(v_rn_arr)))
    
    fig = plt.figure()
    ax = fig.add_subplot(121)
    n, bins, patches = plt.hist(VR, 100,histtype='step',color='red',label=r'$ v_r $', alpha=0.75)
    n, bins, patches = plt.hist(VTheta, 100,histtype='step',color='blue',label=r'$v_{\theta}$', alpha=0.75)
    n, bins, patches = plt.hist(VPhi, 100,histtype='step',color='green',label=r'$ v_{\phi}$', alpha=0.75)
    plt.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\beta = %.2f$,  File = %s )' %(len(x), Beta, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=1,handlelength=2.5)
    plt.grid()
    ax.set_yscale('log')

    ax = fig.add_subplot(122)
    n, bins, patches = plt.hist(np.log10(x7),bins=100,histtype='step',color='red',range=(-5,1),label=r'$\log (|v_{\theta}n|,v_{\theta}p)$',lw=2)
    n, bins, patches = plt.hist(np.log10(x8),bins=100,histtype='step',color='blue',range=(-5,1),label=r'$\log (|v_{\phi}n|,v_{\phi}p)$',lw=2)
    n, bins, patches = plt.hist(np.log10(x9),bins=100,histtype='step',color='green',range=(-5,1),label=r'$\log (|v_rn|,v_rp)$',lw=2)
    plt.xlabel(r'$\log (|v_rn|,v_rp)$, $\log (|v_{\theta}n|,v_{\theta}p)$ and $\log (|v_{\phi}n|,v_{\phi}p)$')
    plt.ylabel('Number of particles')
    plt.title(r'$ f(\log (|v_n|,v_p)) $')
    plt.grid()
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)

if Fig11_vspherical_hist_log_n123:
    fig = plt.figure()
    ax = fig.add_subplot(121)
    #(mu, sigma) = norm.fit(VR)
    n, bins, patches = plt.hist(VR, 100,histtype='step',color='red',label=r'$ v_r $', alpha=0.75)
    #(mu, sigma) = norm.fit(VTheta)
    n, bins, patches = plt.hist(VTheta, 100,histtype='step',color='blue',label=r'$v_{\theta}$', alpha=0.75)
    #(mu, sigma) = norm.fit(VPhi)
    n, bins, patches = plt.hist(VPhi, 100,histtype='step',color='green',label=r'$ v_{\phi}$', alpha=0.75)
    plt.xlabel(r'$v_r$, $v_{\theta}$, $v_{\phi}$')
    plt.ylabel(r'$\log$ number of particles')
    plt.title(r'f(v) ($N=%i$, $\gamma = %.2f$,  File = %s )' %(len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=1,handlelength=2.5)
    plt.grid()
    ax.set_yscale('log')
    #plt.ylim(10**-1,10**3)

    subplot(122)
    ##plt.xlim(-4,1)
    ##plt.ylim(0,250)
    n1 = np.absolute(x4) + x1
    n2 = np.absolute(x5) + x2
    n3 = np.absolute(x6) + x3
    #(mu, sigma) = norm.fit(np.log10(n3))
    n, bins, patches = plt.hist(np.log10(n3), 100,histtype='step',color='red',label=r'$\log (v_rp + |v_rn|)$', alpha=0.75)
    #(mu, sigma) = norm.fit(np.log10(n1))
    n, bins, patches = plt.hist(np.log10(n1), 100,histtype='step',color='blue', label=r'$\log (v_{\theta}p + |v_{\theta}n|)$', alpha=0.75)
    #(mu, sigma) = norm.fit(np.log10(n2))
    n, bins, patches = plt.hist(np.log10(n2), 100,histtype='step', color='green', label=r'$\log (v_{\phi}p + |v_{\phi}n|)$', alpha=0.75)
    plt.xlabel(r'$\log (v_{\theta}p + |v_{\theta}n|)$, $\log (v_{\phi}p + |v_{\phi}n|)$ and $\log (v_rp + |v_rn|)$' )
    plt.ylabel('number of particles')
    plt.title(r'Positive and negative f(v) summed ')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

# All figures with log(v) can instead be plotted as log(v) vs. f(v)/v. the idea is, that a flat tail will appear towards small velocities.
# Next I will plot v/sigma along the x-axes instead (or maybe with log(v/sigma)).
# Plotting v/sigma makes it easier to compare different radial bins, because the x-axis will almost always be the same, even though they actually have very different sigma.

if Fig12_n123_sigma:
    # txt = open(Filename.strip('.hdf5')+'_sigma.txt','r')
    # print txt.read()
    txt = Filename.strip('.hdf5')+'_sigma.txt'
    TXT = pylab.loadtxt(txt)
    if print_sigma:
        print r' $\sigma_{tot}^2$ , TXT[:,0] = ', TXT[:,0] 
        print r' $\sigma_r^2$ , TXT[:,1] = ', TXT[:,1] 
        print r' $\sigma_{\theta}^2$ , TXT[:,2] = ', TXT[:,2] 
        print r' $\sigma_{\phi}^2$ , TXT[:,3] = ', TXT[:,3] 

    TXT_tot_arr   = np.asarray(TXT[:,0] )
    TXT_r_arr     = np.asarray(TXT[:,1] )
    TXT_theta_arr = np.asarray(TXT[:,2] )
    TXT_phi_arr   = np.asarray(TXT[:,3] )
    normTXT_tot_arr   = np.asarray(TXT[:,0] )**0.5
    normTXT_r_arr     = np.asarray(TXT[:,1] )**0.5
    normTXT_theta_arr = np.asarray(TXT[:,2] )**0.5
    normTXT_phi_arr   = np.asarray(TXT[:,3] )**0.5

    plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(n3)/linalg.norm(VR), 100,histtype='step',color='red',label=r'$\frac{f(\log (v_rp + |v_rn|))}{||v_r||}$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(n1)/linalg.norm(VTheta), 100,histtype='step',color='blue', label=r'$\frac{f(\log (v_{\theta}p + |v_{\theta}n|))}{||v_{\theta}||}$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(n2)/linalg.norm(VPhi), 100,histtype='step', color='green', label=r'$\frac{f(\log (v_{\phi}p + |v_{\phi}n|))}{||v_{\phi}||}$', alpha=0.75)
    plt.xlabel(r'$\frac{\log (v_rp + |v_rn|)}{||v_r||}$, $\frac{\log (v_{\theta}p + |v_{\theta}n|)}{||v_{\theta}||}$ and $\frac{\log (v_{\phi}p + |v_{\phi}n|)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (v_p + |v_n|)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s' %(len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR/linalg.norm(normTXT_r_arr), 100,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=0.75)
    n, bins, patches = plt.hist(VTheta/linalg.norm(normTXT_theta_arr), 100,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$', alpha=0.75)
    n, bins, patches = plt.hist(VPhi/linalg.norm(normTXT_phi_arr), 100,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$', alpha=0.75)
    plt.xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $')
    plt.ylabel(r'$f\left( u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(n3), 100,histtype='step',color='red',label=r'$f(\log (v_rp + |v_rn|))$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(n1), 100,histtype='step',color='blue', label=r'$f(\log (v_{\theta}p + |v_{\theta}n|))$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(n2), 100,histtype='step', color='green', label=r'$f(\log (v_{\phi}p + |v_{\phi}n|))$', alpha=0.75)
    plt.xlabel(r'$\log (v_rp + |v_rn|)$, $\log (v_{\theta}p + |v_{\theta}n|)$ and $\log (v_{\phi}p + |v_{\phi}n|)$')
    plt.ylabel(r'$f(\log (v_p + |v_n|))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(n3/linalg.norm(normTXT_r_arr)), 100,histtype='step',color='red',label=r'$f\left(\log \left( \frac{v_rp + |v_rn|}{\sigma_r}\right)\right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(n1/linalg.norm(normTXT_theta_arr)), 100,histtype='step',color='blue', label=r'$f\left(\log \left( \frac{v_{\theta}p + |v_{\theta}n|}{\sigma_{\theta}}\right)\right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(n2/linalg.norm(normTXT_phi_arr)), 100,histtype='step', color='green', label=r'$f\left(\log \left( \frac{v_{\phi}p + |v_{\phi}n|}{\sigma_{\phi}}\right)\right)$', alpha=0.75)
    plt.xlabel(r'$\log \left( u_rp + |u_rn| \right)$, $\log \left( u_{\theta}p + |u_{\theta}n| \right)$ and $\log \left( u_{\phi}p + |u_{\phi}n| \right)$')
    plt.ylabel(r'$f\left(\log \left( u_p + |u_n| \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

if Fig12_x789_sigma:

    x7 = np.asarray(x1 + list(np.absolute(v_thetan_arr)))
    x8 = np.asarray(x2 + list(np.absolute(v_phin_arr)))
    x9 = np.asarray(x3 + list(np.absolute(v_rn_arr)))
    txt = Filename.strip('.hdf5')+'_sigma.txt'
    TXT = pylab.loadtxt(txt)

    if print_sigma:
        print r' $\sigma_{tot}^2$ , TXT[:,0] = ', TXT[:,0] 
        print r' $\sigma_r^2$ , TXT[:,1] = ', TXT[:,1] 
        print r' $\sigma_{\theta}^2$ , TXT[:,2] = ', TXT[:,2] 
        print r' $\sigma_{\phi}^2$ , TXT[:,3] = ', TXT[:,3] 

    TXT_tot_arr   = np.asarray(TXT[:,0] )
    TXT_r_arr     = np.asarray(TXT[:,1] )
    TXT_theta_arr = np.asarray(TXT[:,2] )
    TXT_phi_arr   = np.asarray(TXT[:,3] )
    normTXT_tot_arr   = np.asarray(TXT[:,0] )**0.5
    normTXT_r_arr     = np.asarray(TXT[:,1] )**0.5
    normTXT_theta_arr = np.asarray(TXT[:,2] )**0.5
    normTXT_phi_arr   = np.asarray(TXT[:,3] )**0.5

    plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(x9)/linalg.norm(VR), 100,histtype='step',color='red',range=(-0.1,0.0),label=r'$f\left( \frac{\log (|v_rn|,v_rp))}{||v_r||} \right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x7)/linalg.norm(VTheta), 100,histtype='step',color='blue',range=(-0.1,0.0), label=r'$f\left( \frac{\log (|v_{\theta}n|,v_{\theta}p))}{||v_{\theta}||} \right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x8)/linalg.norm(VPhi), 100,histtype='step', color='green',range=(-0.1,0.0), label=r'$f\left( \frac{\log (|v_{\phi}n|,v_{\phi}p))}{||v_{\phi}||} \right)$', alpha=0.75)
    plt.xlabel(r'$\frac{\log (|v_rn|,v_rp)}{||v_r||}$, $\frac{\log (|v_{\theta}n|,v_{\theta}p)}{||v_{\theta}||}$ and $\frac{\log (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (|v_n|,v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s' %(len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR/linalg.norm(normTXT_r_arr), 100,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=0.75)
    n, bins, patches = plt.hist(VTheta/linalg.norm(normTXT_theta_arr), 100,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$', alpha=0.75)
    n, bins, patches = plt.hist(VPhi/linalg.norm(normTXT_phi_arr), 100,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$', alpha=0.75)
    plt.xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $')
    plt.ylabel(r'$f\left( u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(x9), 100,histtype='step',color='red',range=(-3,0), label=r'$f(\log (|v_rn|,v_rp))$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x7), 100,histtype='step',color='blue',range=(-3,0), label=r'$f(\log (|v_{\theta}n|,v_{\theta}p))$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x8), 100,histtype='step', color='green',range=(-3,0), label=r'$f(\log (|v_{\phi}n|,v_{\phi}p))$', alpha=0.75)
    plt.xlabel(r'$\log (|v_rn|,v_rp)$, $\log (|v_{\theta}n|,v_{\theta}p)$ and $\log (|v_{\phi}n|,v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|,v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9/linalg.norm(normTXT_r_arr)), 100,histtype='step',color='red',range=(-3,0),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x7/linalg.norm(normTXT_theta_arr)), 100,histtype='step',color='blue',range=(-3,0), label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x8/linalg.norm(normTXT_phi_arr)), 100,histtype='step', color='green',range=(-3,0), label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', alpha=0.75)
    plt.xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
    plt.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

if Fig12_vr_vtheta_vphi_sigma:
    v_rpn = np.asarray(list(v_rp_arr) + list(np.absolute(v_rn_arr)))
    v_thetapn = np.asarray(list(v_thetap_arr) + list(np.absolute(v_thetan_arr)))
    v_phipn = np.asarray(list(v_phip_arr) + list(np.absolute(v_phin_arr)))
    x7 = np.asarray(list(VTheta_sigmatheta_p_arr) + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8 = np.asarray(list(VPhi_sigmaphi_p_arr) + list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9 = np.asarray(list(VR_sigmarad_p_arr) + list(np.absolute(VR_sigmarad_n_arr)))
    
    plt.figure()
    plt.subplot(221)
    n, bins, patches = plt.hist(np.log10(v_rpn)/linalg.norm(VR), 100,histtype='step',color='red',range=(-0.1,0.0),label=r'$f\left( \frac{\log (|v_rn|,v_rp)}{||v_r||}\right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn)/linalg.norm(VTheta), 100,histtype='step',color='blue',range=(-0.1,0.0), label=r'$f\left( \frac{\log (|v_{\theta}n|,v_{\theta}p))}{||v_{\theta}||} \right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(v_phipn)/linalg.norm(VPhi), 100,histtype='step', color='green',range=(-0.1,0.0), label=r'$f\left( \frac{\log (|v_{\phi}n|,v_{\phi}p))}{||v_{\phi}||} \right)$', alpha=0.75)

    (mu, sigma) = norm.fit(np.log10(v_rpn)/linalg.norm(VR))
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata,popt[0],popt[1])
    plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$ \frac{ \log ( v_r )}{|| v_r ||}  -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
    
    plt.xlabel(r'$\frac{\log (|v_rn|,v_rp)}{||v_r||}$, $\frac{\log (|v_{\theta}n|,v_{\theta}p)}{||v_{\theta}||}$ and $\frac{\log (|v_{\phi}n|,v_{\phi}p)}{||v_{\phi}||}$')
    plt.ylabel(r'$f \left( \frac{\log (|v_n|,v_p)}{||v||}\right)$')
    plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s' %(len(x), Gamma, F))
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(222)
    n, bins, patches = plt.hist(VR_sigmarad, 100,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=0.75)
    n, bins, patches = plt.hist(VTheta_sigmatheta, 100,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$', alpha=0.75)
    n, bins, patches = plt.hist(VPhi_sigmaphi, 100,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$', alpha=0.75)

    (mu, sigma) = norm.fit(VR_sigmarad)
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    popt, pcov = curve_fit(func_2, xdata, ydata)
    y_fit = func_2(xdata,popt[0],popt[1])
    plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')

    plt.xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $')
    plt.ylabel(r'$f\left( u \right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(223)
    n, bins, patches = plt.hist(np.log10(v_rpn), 100,histtype='step',color='red',range=(-3,0), label=r'$f(\log (|v_rn|,v_rp))$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(v_thetapn), 100,histtype='step',color='blue',range=(-3,0), label=r'$f(\log (|v_{\theta}n|,v_{\theta}p))$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(v_phipn), 100,histtype='step', color='green',range=(-3,0), label=r'$f(\log (|v_{\phi}n|,v_{\phi}p))$', alpha=0.75)

    (mu, sigma) = norm.fit(np.log10(v_rpn))
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata,popt[0],popt[1])
    plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\log ( v_r ) -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\log (|v_rn|,v_rp)$, $\log (|v_{\theta}n|,v_{\theta}p)$ and $\log (|v_{\phi}n|,v_{\phi}p)$')
    plt.ylabel(r'$f(\log (|v_n|,v_p))$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

    plt.subplot(224)
    n, bins, patches = plt.hist(np.log10(x9), 100,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x7), 100,histtype='step',color='blue',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$', alpha=0.75)
    n, bins, patches = plt.hist(np.log10(x8), 100,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', alpha=0.75)

    (mu, sigma) = norm.fit(np.log10(x9))
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    popt, pcov = curve_fit(func_1_log, xdata, ydata)
    y_fit = func_1_log(xdata,popt[0],popt[1])
    plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')

    plt.xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
    plt.ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$')
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
    plt.grid()

if Fig12_vr_vtheta_vphi_vt_sigma:
    
    v_rpn = np.asarray(list(v_rp_arr) + list(np.absolute(v_rn_arr)))
    v_thetapn = np.asarray(list(v_thetap_arr) + list(np.absolute(v_thetan_arr)))
    v_phipn = np.asarray(list(v_phip_arr) + list(np.absolute(v_phin_arr)))
    v_tpn = np.asarray(list(v_tp_arr) + list(np.absolute(v_tn_arr)))
    x7  = np.asarray(list(VTheta_sigmatheta_p_arr) + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8  = np.asarray(list(VPhi_sigmaphi_p_arr) + list(np.absolute(VPhi_sigmaphi_n_arr)))
    x9  = np.asarray(list(VR_sigmarad_p_arr) + list(np.absolute(VR_sigmarad_n_arr)))
    x10 = np.asarray(list(VT_sigmatan_p_arr) + list(np.absolute(VT_sigmatan_n_arr)))

    if keep_IC_R_middle:
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s' %(len(VR), Gamma, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50,histtype='step',color='Black',label=r'$f\left(\frac{v_t}{\sigma_t}\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_VT_sigmatan_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        #print 'F+_VT_sigmatan_gamma_%.2f.txt %Gamma = ', F+'_VT_sigmatan_gamma_%.2f.txt' %Gamma

        n, bins, patches = plt.hist(VR_sigmarad, 50,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_VR_sigmarad_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_VTheta_sigmatheta_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VPhi_sigmaphi, 50,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$', alpha=0.75)
        #(mu, sigma) = norm.fit(VR_sigmarad)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        #popt, pcov = curve_fit(func_2, xdata, ydata)
        #y_fit = func_2(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_VPhi_sigmaphi_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta}$ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2 = fig.add_subplot(122)

        n, bins, patches = plt.hist(np.log10(x10), 50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_logx10_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_logx9_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50,histtype='step',color='blue',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_logx7_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', alpha=0.75)
        #(mu, sigma) = norm.fit(np.log10(x9))
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        #popt, pcov = curve_fit(func_1_log, xdata, ydata)
        #y_fit = func_1_log(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_logx8_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        ax2.set_yscale('log')
        #plt.ylim(10**-1,10**3)
        #plt.xlim(-3.5,0)
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()

    if new_R_middle:
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s , new R_middle' %(len(VR), Gamma, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50,histtype='step',color='Black',label=r'$f\left(\frac{v_t}{\sigma_t}\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_VT_sigmatan_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        #print 'F+_VT_sigmatan_gamma_%.2f.txt %Gamma = ', F+'_VT_sigmatan_gamma_%.2f.txt' %Gamma

        n, bins, patches = plt.hist(VR_sigmarad, 50,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_VR_sigmarad_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_VTheta_sigmatheta_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VPhi_sigmaphi, 50,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$', alpha=0.75)
        #(mu, sigma) = norm.fit(VR_sigmarad)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        #popt, pcov = curve_fit(func_2, xdata, ydata)
        #y_fit = func_2(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_VPhi_sigmaphi_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2 = fig.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_logx10_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_logx9_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50,histtype='step',color='blue',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_logx7_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', alpha=0.75)
        #(mu, sigma) = norm.fit(np.log10(x9))
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        #popt, pcov = curve_fit(func_1_log, xdata, ydata)
        #y_fit = func_1_log(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
        x = np.array((xdata , ydata))
        x = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_logx8_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        ax2.set_yscale('log')
        #plt.ylim(10**-1,10**3)
        #plt.xlim(-3.5,0)
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()










        

    if large_R_middle:
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        plt.title(r'$N=%i$, $R_{middle} = %.2f$ ,  File = %s , new R_middle' %(len(VR), R_middle, F))

        n, bins, patches = plt.hist(VT_sigmatan, 50,histtype='step',color='Black',label=r'$f\left( u_t \right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_VT_sigmatan_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VR_sigmarad, 50,histtype='step',color='red',label=r'$f\left( u_r \right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_VR_sigmarad_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left( u_{\theta} \right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_VTheta_sigmatheta_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50,histtype='step', color='green', label=r'$f\left( u_{\phi} \right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_VPhi_sigmaphi_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()





        ax2 = fig.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_logx10_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( |u_rn|,u_rp \right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_logx9_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50,histtype='step',color='blue',range=(-3,1), label=r'$f\left(\log \left( |u_{\theta}n|,u_{\theta}p \right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_logx7_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( |u_{\phi}n|,u_{\phi}p \right)\right)$', alpha=0.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_large_R_middle_logx8_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()



if Fig13_vspherical_hist_old:
    plt.figure()
    (mu, sigma) = norm.fit(v_t_arr[6]) # best fit of data
    n, bins, patches = plt.hist(v_t_arr[6], 100, normed=1,color='green', alpha=0.75) # the histogram of the data
    # add a 'best fit' line
    #y = mlab.normpdf( bins, mu, sigma)
    #l = plt.plot(bins, y, 'r--', linewidth=2)
    #plt.plot(v_t_arr[10], fit, 'b--', linewidth=2)
    #plot
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    popt, pcov = curve_fit(func_1, xdata, ydata)
    y_fit = func_1(xdata,popt[0],popt[1],popt[2])
    plt.plot(xdata,y_fit,'--',lw=3,color='SkyBlue')
    plt.xlabel(r'$v_t$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
    plt.grid()

    x = np.array((xdata , ydata))
    x = x.transpose()
    print 'x.shape:', x.shape
    np.savetxt('Hernquist10000_G1.2_9_005_bin6_VDFt.txt', x, delimiter = ' ', header='    bins                         n')

    plt.figure()
    (mu, sigma) = norm.fit(v_r_arr[6])
    # the histogram of the data
    n, bins, patches = plt.hist(v_r_arr[6], 100, normed=1,color='blue', alpha=0.75)
    # add a 'best fit' line
    #y = mlab.normpdf( bins, mu, sigma)
    #l = plt.plot(bins, y, 'r--', linewidth=2)
    #plot
    xdata = bins[0:-1]+(bins[1]-bins[0])*0.5
    ydata = n
    popt, pcov = curve_fit(func_2, xdata, ydata)
    y_fit = func_2(xdata,popt[0],popt[1],popt[2])
    plt.plot(xdata,y_fit,'--',lw=3,color='SkyBlue')
    plt.xlabel(r'$v_r$')
    plt.ylabel('number of particles')
    plt.title(r'$\mathrm{Histogram\ of\ VDF:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
    plt.grid()

    x = np.array((xdata , ydata))
    x = x.transpose()
    print 'x.shape:', x.shape
    np.savetxt('Hernquist10000_G1.2_9_005_bin6_VDFr.txt', x, delimiter = ' ', header='    bins                         n')
    #np.log10(0.5*np.fabs())

if save_r_v_as_txt:
    x = np.array((xcl2 , ycl2, zcl2, vxnew2, vynew2, vznew2))
    x = x.transpose()
    print 'x.shape:', x.shape
    np.savetxt('HQ10000_G1.2_9_005_bin0_05to0_25kpc_VDF.txt', x, delimiter = ' ', header=' xcl2      ycl2      zcl2      vxnew2      vynew2      vznew2 ')

if Fig15_gaussian_fits:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) # func_2 (Gaussian) (x,a,b) 
    #x_plot = np.log10(bin_radius_arr)
    x_plot = np.linspace(-5, 5, 50)
    
    ax1.plot(x_plot, func_2(x_plot,1,1),'-o',mew=0 ,color = 'Red', label=r'$ a = 1, b = 1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_2(x_plot,1.5,1),'-o',mew=0 ,color = 'Blue', label=r'$  a = 1.5, b = 1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_2(x_plot,1,1.5),'-o',mew=0 ,color = 'Green', label=r'$  a = 1, b = 1.5 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_2(x_plot,0.5,1),'-o',mew=0 ,color = 'Orange', label=r'$  a = 0.5, b = 1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Violet', label=r'$  a = 1, b = 0.5 $',lw=2,ms=7 )
 
    ax1.set_xlabel(r'x', fontsize=20)
    ax1.set_ylabel(r'$a e^{-b x^2}$', fontsize=20)
    ax1.set_title(r' Gaussian fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax1.set_xlim(-3,3)
    ax1.grid()
 
    ax2.plot(x_plot, func_2(x_plot,1,1),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax2.plot(x_plot, func_2(x_plot,1.5,1),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax2.plot(x_plot, func_2(x_plot,1,1.5),'-o',mew=0 ,color = 'Green',lw=2,ms=7 )
    ax2.plot(x_plot, func_2(x_plot,0.5,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )
    ax2.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Violet',lw=2,ms=7 )

    ax2.set_xlim(10**-1,10**1)
    ax2.set_ylim(0,1.6)
    ax2.set_xlabel(r'$\log x$', fontsize=20)
    ax2.set_ylabel(r'$ a e^{-b  x^2}$', fontsize=20)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax2.grid()
    ax2.set_xscale('log')
    
    ax3.plot(x_plot, func_2(x_plot,1,1),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax3.plot(x_plot, func_2(x_plot,1.5,1),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax3.plot(x_plot, func_2(x_plot,1,1.5),'-o',mew=0 ,color = 'Green',lw=2,ms=7 )
    ax3.plot(x_plot, func_2(x_plot,0.5,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )
    ax3.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Violet',lw=2,ms=7 )

    ax3.set_xlim(-4,4)
    ax3.set_ylim(10**-3,10**1)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$ \log \left( a e^{-b x^2} \right) $', fontsize=20)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')

    ax4.plot(x_plot, func_2(x_plot,1,1),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax4.plot(x_plot, func_2(x_plot,1.5,1),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax4.plot(x_plot, func_2(x_plot,1,1.5),'-o',mew=0 ,color = 'Green',lw=2,ms=7 )
    ax4.plot(x_plot, func_2(x_plot,0.5,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )
    ax4.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Violet',lw=2,ms=7 )
  
    ax4.set_xlim(-4,4)
    ax4.set_ylim(10**-3,10**1)
    ax4.set_xlabel(r'$\log x$', fontsize=20)
    ax4.set_ylabel(r'$ \log \left( a e^{-b x^2} \right) $', fontsize=20)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax4.grid()
    ax4.set_xscale('log')
    ax4.set_yscale('log')

if Fig16_q_fits:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) # func_4 (q-fit) (x,a,q,b)
    #x_plot = np.log10(bin_radius_arr)
    x_plot = np.linspace(-5, 5, 50)
    
    ax1.plot(x_plot, func_4(x_plot,1,0.9,1),'-o',mew=0 ,color = 'Red', label=r'$ a = 1, q = 0.9, b = 1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_4(x_plot,1,0.9,1.5),'-o',mew=0 ,color = 'Blue', label=r'$ a = 1, q = 0.9, b = 1.5 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_4(x_plot,1.5,0.9,1),'-o',mew=0 ,color = 'Green', label=r'$ a = 1.5, q = 0.9, b = 1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_4(x_plot,1,1.2,1),'-o',mew=0 ,color = 'Orange', label=r'$ a = 1, q = 1.2, b = 1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_4(x_plot,1,1.5,1),'-o',mew=0 ,color = 'Violet', label=r'$ a = 1, q = 1.5, b = 1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Black', label=r'$ a = 1, q = \frac{5}{3}, b = 1 $',lw=2,ms=7 )
    
    ax1.set_xlabel(r'x', fontsize=20)
    ax1.set_ylabel(r'$ a \cdot (1- (1 - q )\cdot b\cdot x^2) ^{\frac {q}{ 1 - q}}$', fontsize=20)
    ax1.set_title(r' q-fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax1.set_xlim(-3,3)
    ax1.set_ylim(0,1.6)
    ax1.grid()
 
    ax2.plot(x_plot, func_4(x_plot,1,0.9,1),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax2.plot(x_plot, func_4(x_plot,1,0.9,1.5),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax2.plot(x_plot, func_4(x_plot,1.5,0.9,1),'-o',mew=0 ,color = 'Green',lw=2,ms=7 )
    ax2.plot(x_plot, func_4(x_plot,1,1.2,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )
    ax2.plot(x_plot, func_4(x_plot,1,1.5,1),'-o',mew=0 ,color = 'Violet',lw=2,ms=7 )
    ax2.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Black',lw=2,ms=7 )

    ax2.set_xlim([-3,3])
    ax2.set_xlabel(r'$ \log x $', fontsize=20)
    ax2.set_ylabel(r'$ a \cdot (1- (1 - q )\cdot b\cdot x^2) ^{\frac {q}{ 1 - q}}$', fontsize=20)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax2.grid()
    ax2.set_xscale('log')

    ax3.plot(x_plot, func_4(x_plot,1,0.9,1),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax3.plot(x_plot, func_4(x_plot,1,0.9,1.5),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax3.plot(x_plot, func_4(x_plot,1.5,0.9,1),'-o',mew=0 ,color = 'Green',lw=2,ms=7 )
    ax3.plot(x_plot, func_4(x_plot,1,1.2,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )
    ax3.plot(x_plot, func_4(x_plot,1,1.5,1),'-o',mew=0 ,color = 'Violet',lw=2,ms=7 )
    ax3.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Black',lw=2,ms=7 )

    ax3.set_xlim(-3,3)
    ax3.set_ylim(10**-3,10**1)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$ \log \left( a \cdot (1- (1 - q )\cdot b\cdot x^2) ^{\frac {q}{ 1 - q}} \right)$', fontsize=20)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')
    
    ax4.plot(x_plot, func_4(x_plot,1,0.9,1),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax4.plot(x_plot, func_4(x_plot,1,0.9,1.5),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax4.plot(x_plot, func_4(x_plot,1.5,0.9,1),'-o',mew=0 ,color = 'Green',lw=2,ms=7 )
    ax4.plot(x_plot, func_4(x_plot,1,1.2,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )
    ax4.plot(x_plot, func_4(x_plot,1,1.5,1),'-o',mew=0 ,color = 'Violet',lw=2,ms=7 )
    ax4.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Black',lw=2,ms=7 )
    
    #ax4.set_xlim(-3,0)
    ax4.set_ylim(10**-3,10**1)
    ax4.set_xlabel(r'$ \log x $', fontsize=20)
    ax4.set_ylabel(r'$ \log \left( a \cdot (1- (1 - q )\cdot b\cdot x^2) ^{\frac {q}{ 1 - q}} \right)$', fontsize=20)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax4.grid()
    ax4.set_xscale('log')
    ax4.set_yscale('log')

if Fig17_compare_fits:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) # func_2 (Gaussian) (x,a,b) and func_4 (q-fit) (x,a,q,b)
 
    #x_plot = np.log10(bin_radius_arr)
    x_plot = np.linspace(-5, 5, 50)
    
    ax1.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Red', label=r'$ a=1, b=\frac{1}{2} $',lw=2,ms=7 )
    ax1.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Blue', label=r'$ a=1, q=\frac{5}{3}, b=1 $',lw=2,ms=7 )
    ax1.plot(x_plot, func_4(x_plot,1,0.5,1),'-o',mew=0 ,color = 'Orange', label=r'$ a=1, q=\frac{1}{2}, b=1 $',lw=2,ms=7 )

    ax1.set_xlabel(r'x', fontsize=20)
    ax1.set_ylabel(r' y ', fontsize=20)
    ax1.set_title(r' Comparison of fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax1.set_xlim(-3,3)
    ax1.set_ylim(0,1.2)
    ax1.grid()
 
    ax2.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax2.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax2.plot(x_plot, func_4(x_plot,1,0.5,1),'-o',mew=0 ,color = 'Orange', lw=2,ms=7 )

    ax2.set_ylim(0,1.2)   
    ax2.set_xlim(10**-1,5*10**0)
    ax2.set_xlabel(r'$ \log x $', fontsize=20)
    ax2.set_ylabel(r' y ', fontsize=20)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax2.grid()
    ax2.set_xscale('log')

    ax3.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax3.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax3.plot(x_plot, func_4(x_plot,1,0.5,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )

    ax3.set_xlim(-2.5,2.5)
    ax3.set_ylim(1.2*10**-1,1.5*10**0)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$ \log y$', fontsize=20)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')
    
    ax4.plot(x_plot, func_2(x_plot,1,0.5),'-o',mew=0 ,color = 'Red',lw=2,ms=7 )
    ax4.plot(x_plot, func_4(x_plot,1,5./3.,1),'-o',mew=0 ,color = 'Blue',lw=2,ms=7 )
    ax4.plot(x_plot, func_4(x_plot,1,0.5,1),'-o',mew=0 ,color = 'Orange',lw=2,ms=7 )
    
    ax4.set_xlim(10**-1,3*10**0)
    ax4.set_ylim(1.2*10**-1,1.5*10**0)
    ax4.set_xlabel(r'$ \log x $', fontsize=20)
    ax4.set_ylabel(r'$ \log y$', fontsize=20)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax4.grid()
    ax4.set_xscale('log')
    ax4.set_yscale('log')

plt.show()
