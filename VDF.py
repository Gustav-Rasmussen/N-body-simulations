# -*- coding: utf-8 -*-

from   __future__           import division
import h5py
import numpy                as     np
from   scipy.optimize       import curve_fit
import matplotlib.pyplot    as     plt
import IPython
from   matplotlib.colors    import LogNorm
import time
from   pylab                import *
import pylab
from   scipy.stats          import norm
import matplotlib.mlab      as     mlab
import scipy                as     sp
from   astropy.io           import ascii
from   mpl_toolkits.mplot3d import Axes3D
import seaborn              as     sns

# Run 3D plots with this command from terminal:
# ~/python/3dplot/bin/python VDF.py

# readline will not be well behaved unless this is installed:
# pip install gnureadline

User_path        =                                    '/Users/gustav.c.rasmussen/'
Desktop_path     = User_path                        + 'Desktop/'
GADGET_G_path    = Desktop_path                     + 'RunGadget/G_perturbations/'
Stable_path      =                                    'G_perturbations/Stable_structures/'
figure_path      = Desktop_path + Stable_path       + 'figures/'
text_files_path  = Desktop_path + Stable_path       + 'text_files/'
Martin_path      =                                    'Martin_IC_and_Final_Edd_and_OM/'
hdf5_path        = Desktop_path                     + 'G_perturbations/hdf5_files/'
nosync_path      = User_path                        + 'nosync/RunGadget/'

test_path        = 'G_HQ_1000000_test/output/'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G1.2_1_005.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G0.8_2_000.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G0.8_2_005.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G1.2_3_005.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G1.2_5_005.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G1.2_7_005.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G1.2_9_005.hdf5'
#Filename        = GADGET_G_path + test_path        + 'Hernquist10000_G1.0_10_009.hdf5'
A_path           = 'G_HQ_1000000_A/output/'
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_0_000.hdf5'  # This file is already run in VDF.py, from test2. re-use that one.
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_5_005.hdf5'  # This file is already run in VDF.py, from test2. re-use that one.
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_10_005.hdf5' # This file is already run in VDF.py, from test2. re-use that one.
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_40_005.hdf5'   
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_48_009.hdf5'  
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_48_093.hdf5'   
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.2_46_005.hdf5'  # has not yet been analysed
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G0.8_47_005.hdf5'  # has not yet been analysed
B_path           = 'G_HQ_1000000_B/output/'
Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_0_000.hdf5'  # This file is already run in VDF.py, from test2. re-use that one.
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_5_005.hdf5' 
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_198_000.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_198_093.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_199_093.hdf5'
##Filename       = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_160_005.hdf5'
##Filename       = GADGET_G_path + B_path           + 'Hernquist10000_G1.05_196_005.hdf5'
##Filename       = GADGET_G_path + B_path           + 'Hernquist10000_G0.95_197_005.hdf5'
Soft_B_path      = 'Soft_G_HQ_1000000_B/output/'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_5_005.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_198_000.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_198_093.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_199_093.hdf5'
CS1_path         = 'G_OM_10000_C1/output/'
#Filename        = GADGET_G_path + CS1_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5' 
CS2_path         = 'G_OM_10000_C2/output/'
#Filename        = GADGET_G_path + CS2_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5' 
CS3_path         = 'G_OM_10000_C3/output/'
#Filename        = GADGET_G_path + CS3_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS4_path         = 'G_HQ_100000_CS4/output/'
#Filename        = GADGET_G_path + CS4_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + CS4_path         + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
CS5_path         = 'G_HQ_100000_CS5/output/'
#Filename        = GADGET_G_path + CS5_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + CS5_path         + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
CS6_path         = 'G_HQ_100000_CS6/output/'
#Filename        = GADGET_G_path + CS6_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + CS6_path         + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
DS1_path         = 'G_0_5_100000_DS1/output/'
#Filename        = GADGET_G_path + DS1_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + DS1_path         + 'Osipkov_Merritt10000_G1.0_48_093.hdf5'
#Filename        = GADGET_G_path + DS1_path         + 'Osipkov_Merritt10000_G1.0_49_093.hdf5'
D2_path          = 'G_0_5_100000_D2/output/'
#Filename        = GADGET_G_path + D2_path          + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + D2_path          + 'Hernquist10000_G1.0_48_093.hdf5'
#Filename        = GADGET_G_path + D2_path          + 'Hernquist10000_G1.0_49_093.hdf5'
Soft_D2_path     = 'Soft_G_0_5_100000_D2/output/'
#Filename        = GADGET_G_path + Soft_D2_path     + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + Soft_D2_path     + 'Hernquist10000_G1.0_48_093.hdf5'
#Filename        = GADGET_G_path + Soft_D2_path     + 'Hernquist10000_G1.0_49_093.hdf5'
E_path           = 'G_HQ_1000000_E/output/'
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G1.0_0_000.hdf5' 
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G1.0_5_005.hdf5' 
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G1.0_10_005.hdf5' 
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G1.0_160_005.hdf5'
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G1.05_196_005.hdf5'
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G0.95_197_005.hdf5'
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G1.0_198_009.hdf5'
#Filename        = GADGET_G_path + E_path           + 'Hernquist10000_G1.0_198_093.hdf5'

# Bound particles only:
B_rfp_path       = 'G_HQ_1000000_B/rfp_output/'
#Filename        = GADGET_G_path + B_rfp_path       + 'B_G1.0_200_rfp_011.hdf5'
#Filename        = GADGET_G_path + B_rfp_path       + 'B_G1.0_200_rfp_093.hdf5'
Soft_B_rfp_path  = 'Soft_G_HQ_1000000_B/rfp_output/'
#Filename        = GADGET_G_path + Soft_B_rfp_path  + 'B_G1.0_200_rfp_011.hdf5'
#Filename        = GADGET_G_path + Soft_B_rfp_path  + 'B_G1.0_200_rfp_093.hdf5'
CS4_rfp_path     = 'G_HQ_100000_CS4/rfp_output/'
#Filename        = GADGET_G_path + CS4_rfp_path     + 'CS4_G1.0_49_rfp_093.hdf5'
CS5_rfp_path     = 'G_HQ_100000_CS5/rfp_output/'
#Filename        = GADGET_G_path + CS5_rfp_path     + 'CS5_G1.0_49_rfp_093.hdf5'
CS6_rfp_path     = 'G_HQ_100000_CS6/rfp_output/'
#Filename        = GADGET_G_path + CS6_rfp_path     + 'CS6_G1.0_49_rfp_093.hdf5'
DS1_rfp_path     = 'G_0_5_100000_DS1/rfp_output/'
#Filename        = GADGET_G_path + DS1_rfp_path     + 'DS1_G1.0_50_rfp_093.hdf5'
D2_rfp_path      = 'G_0_5_100000_D2/rfp_output/'
#Filename        = GADGET_G_path + D2_rfp_path      + 'D2_G1.0_50_rfp_093.hdf5'
Soft_D2_rfp_path = 'Soft_G_0_5_100000_D2/rfp_output/'
#Filename        = GADGET_G_path + Soft_D2_rfp_path + 'D2_G1.0_50_rfp_093.hdf5'
E_rfp_path       = 'G_HQ_1000000_E/rfp_output/'

SnapshotFile     = h5py.File(Filename,'r')

#F               = 'test_'                          + Filename[len(GADGET_G_path + test_path):-5                   ]
#F               = 'A_'                             + Filename[len(GADGET_G_path + A_path):-5                      ]
#F               = 'A_'                             + Filename[len(nosync_path   + A_path):-5                      ]
F               = 'B_'                             + Filename[len(GADGET_G_path + B_path):-5                      ]
#F               = 'Soft_B_'                        + Filename[len(GADGET_G_path + Soft_B_path):-5                 ]
#F               = 'CS1_'                           + Filename[len(GADGET_G_path + CS1_path):-5                    ]
#F               = 'CS2_'                           + Filename[len(GADGET_G_path + CS2_path):-5                    ]
#F               = 'CS3_'                           + Filename[len(GADGET_G_path + CS3_path):-5                    ]
#F               = 'CS4_'                           + Filename[len(GADGET_G_path + CS4_path):-5                    ]
#F               = 'CS5_'                           + Filename[len(GADGET_G_path + CS5_path):-5                    ]
#F               = 'CS6_'                           + Filename[len(GADGET_G_path + CS6_path):-5                    ]
#F               = 'DS1_'                           + Filename[len(GADGET_G_path + DS1_path):-5                    ]
#F               = 'D2_'                            + Filename[len(GADGET_G_path + D2_path):-5                     ]           
#F               = 'Soft_D2_'                       + Filename[len(GADGET_G_path + Soft_D2_path):-5                ]
#F               = 'E_'                             + Filename[len(GADGET_G_path + E_path):-5                      ]

# Bound particles only:
#F               = 'B_bound_particles_'             + Filename[len(GADGET_G_path + B_rfp_path + 'B_'):-5           ]
#F               = 'Soft_B_bound_particles_'        + Filename[len(GADGET_G_path + Soft_B_rfp_path + 'B_'):-5      ]
#F               = 'CS4_bound_particles_'           + Filename[len(GADGET_G_path + CS4_rfp_path + 'CS4_'):-5       ]
#F               = 'CS5_bound_particles_'           + Filename[len(GADGET_G_path + CS5_rfp_path + 'CS5_'):-5       ]
#F               = 'CS6_bound_particles_'           + Filename[len(GADGET_G_path + CS6_rfp_path +  'CS6_'):-5      ]
#F               = 'DS1_bound_particles_'           + Filename[len(GADGET_G_path + DS1_rfp_path + 'DS1_'):-5       ]
#F               = 'D2_bound_particles_'            + Filename[len(GADGET_G_path + D2_rfp_path + 'D2_'):-5         ]
#F               = 'Soft_D2_bound_particles_'       + Filename[len(GADGET_G_path + Soft_D2_rfp_path + 'D2_'):-5    ]
#F               = 'E_bound_particles_'             + Filename[len(GADGET_G_path + E_rfp_path + 'E_'):-5           ]

Gamma            = -3.
#Beta            = 1.

test             = 0
A                = 0
B                = 1
CS1              = 0
CS2              = 0
CS3              = 0
CS4              = 0 # These files are not yet incorporated into VDF.py
CS5              = 0
CS6              = 0
DS1              = 0
D2               = 0
E                = 0

keep_IC_R_middle = 0
new_R_middle     = 1
R_bin_automatic  = 0
large_R_middle   = 0


bins_202                                       = 0
bins_102                                       = 0
larger_fewer_bins                              = 1 # Reduce number of radial bins in analysis code. 

largest_R_limit                                = 1 # Analyse larger volume of structure, sets R_limit to 10000.
large_R_limit                                  = 0 # Analyse large volume of structure, sets R_limit to 5000.

if keep_IC_R_middle:
    if test: # Below values are for file Hernquist10000_G1.0_0_000
        if   Gamma == -1.5:       
                R_middle = 10**-0.70 
        elif Gamma == -2.0:     
                R_middle = 10**-0.25
        elif Gamma == -2.5:                   
                R_middle = 10**-0.0 
        elif Gamma == -3.0:     
                R_middle = 10**-0.30

if new_R_middle:# Choose new R_middle for each file.
    if test:
        if F == 'Hernquist10000_G1.0_0_000': # 0.th/IC file
            if   Gamma == -1.5:       
                R_middle = 10**-0.70 
            elif Gamma == -2.0:     
                R_middle = 10**-0.25
            elif Gamma == -2.5:                    
                R_middle = 10**-0.0 
            elif Gamma == -3.0:     
                R_middle = 10**-0.30
        if F == 'Hernquist10000_G1.2_1_005': # 1.st file
            if   Gamma == -1.5:      
                R_middle =  10**-0.55
            elif Gamma == -2.0:     
                R_middle = 10**-0.4
            elif Gamma == -2.5:                   
                R_middle = 10**-0.1
            elif Gamma == -3.0:     
                R_middle = 10**0.2
        if F == 'Hernquist10000_G0.8_2_005': # 2.nd file
            if   Gamma == -1.5:      
                R_middle =  0
            elif Gamma == -2.0:     
                R_middle = 0
            elif Gamma == -2.5:                    
                R_middle =  0
            elif Gamma == -3.0:     
                R_middle = 0
        if F == 'Hernquist10000_G1.2_3_005': # 3.rd file
            if   Gamma == -1.5:       
                R_middle =  10**-0.6
            elif Gamma == -2.0:   
                R_middle = 10**-0.4
            elif Gamma == -2.5:                 
                R_middle = 10**0.0
            elif Gamma == -3.0:     
                R_middle = 10**0.4
        if F == 'Hernquist10000_G1.2_5_005': # 5.th file
            if   Gamma == -1.5:      
                R_middle = 10**-0.45 
            elif Gamma == -2.0:     
                R_middle = 10**-0.35
            elif Gamma == -2.5:                   
                R_middle =  10**-0.1
            elif Gamma == -3.0:     
                R_middle = 10**0.45
        if F == 'Hernquist10000_G1.2_7_005': # 7.th file
            if   Gamma == -1.5:     
                R_middle =  10**-0.35
            elif Gamma == -2.0: 
                R_middle = 10**-0.25
            elif Gamma == -2.5:               
                R_middle = 10**-0.1
            elif Gamma == -3.0:     
                R_middle = 10**0.48
        if F == 'Hernquist10000_G1.2_9_005': # 9.th file
            if   Gamma == -1.5:      
                R_middle = 10**-0.35
            elif Gamma == -2.0:    
                R_middle = 10**-0.3
            elif Gamma == -2.5:                    
                R_middle = 10**-0.15
            elif Gamma == -3.0:     
                R_middle = 10**0.5
        if F == 'Hernquist10000_G1.0_10_009': # 10.th file
            if   Gamma == -1.5:       
                R_middle = 10**-0.25
            elif Gamma == -2.0:     
                R_middle = 10**-0.15
            elif Gamma == -2.5:                    
                R_middle = 10**0.0
            elif Gamma == -3.0:   
                R_middle = 10**0.5
    if A:
        if F == 'A_' + 'Hernquist10000_G1.0_0_000': # 0.th/IC file
            if   Gamma == -1.5:      
                R_middle = 10**-0.7
            elif Gamma == -2.0:      
                R_middle = 10**-0.35
            elif Gamma == -2.5:                   
                R_middle = 10**0.0
            elif Gamma == -3.0:     
                R_middle = 10**0.25
        if F == 'A_' + 'Hernquist10000_G1.0_5_005': # 5.th file
            if   Gamma == -1.5:     
                R_middle =  10**-0.38
            elif Gamma == -2.0:     
                R_middle = 10**-0.18
            elif Gamma == -2.5:                    
                R_middle = 10**0.0
            elif Gamma == -3.0:     
                R_middle = 10**0.4
        if F == 'A_' + 'Hernquist10000_G1.0_10_005': # 10.th file
            if   Gamma == -1.5:      
                R_middle =  10**-0.35
            elif Gamma == -2.0:     
                R_middle = 10**-0.18
            elif Gamma == -2.5:                    
                R_middle =  10**0.0
            elif Gamma == -3.0:     
                R_middle = 10**0.4
        if F == 'A_' + 'Hernquist10000_G1.0_40_005': # 15.th file
            if   Gamma == -1.5:      
                R_middle =  10**-0.08
            elif Gamma == -2.0:     
                R_middle = 10**0.0
            elif Gamma == -2.5:                   
                R_middle = 10**0.07
            elif Gamma == -3.0:     
                R_middle = 10**0.38
        if F == 'A_' + 'Hernquist10000_G1.0_48_009': # 20.th file
            if   Gamma == -1.5:      
                R_middle = 10**-0.08
            elif Gamma == -2.0:     
                R_middle = 10**0.0
            elif Gamma == -2.5:                   
                R_middle =  10**0.07
            elif Gamma == -3.0:     
                R_middle = 10**0.25
        if F == 'A_' + 'Hernquist10000_G1.0_48_093': # 25.th file
            if   Gamma == -1.5:     
                R_middle =  10**-0.05
            elif Gamma == -2.0:     
                R_middle = 10**0.0
            elif Gamma == -2.5:                   
                R_middle = 10**0.07
            elif Gamma == -3.0:     
                R_middle = 10**0.57
    if B:
        if F == 'B_' + 'Hernquist10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**-0.7
            elif Gamma == -2.0:     
                R_middle = 10**-0.35
            elif Gamma == -2.5:                   
                R_middle = 10**0.0
            elif Gamma == -3.0: 
                R_middle = 10**0.25
        if F == 'B_' + 'Hernquist10000_G1.0_5_005': # 5.th perturbation (36.th file)
            if   Gamma == -1.5:      
                R_middle =  10**-0.4
            elif Gamma == -2.0:     
                R_middle = 10**-0.15
            elif Gamma == -2.5:                   
                R_middle = 10**0.1
            elif Gamma == -3.0:    
                R_middle = 10**0.25
        if F == 'B_' + 'Hernquist10000_G1.0_10_005': # 10.th perturbation (66.th file)
            if   Gamma == -1.5:     
                R_middle =  10**-0.25
            elif Gamma == -2.0:     
                R_middle = 10**-0.14
            elif Gamma == -2.5:                    
                R_middle =  10**0
            elif Gamma == -3.0:     
                R_middle = 10**0.4
        if F == 'B_' + 'Hernquist10000_G1.0_198_000': # 198.th perturbation (289.th file)
            if   Gamma == -1.5:      
                R_middle =  10**0.1
            elif Gamma == -2.0:     
                R_middle = 10**0.2
            elif Gamma == -2.5:                   
                R_middle = 10**0.3
            elif Gamma == -3.0:     
                R_middle = 10**0.45
        if F == 'B_' + 'Hernquist10000_G1.0_198_093': # 198.th perturbation (382.th file)
            if   Gamma == -1.5:      
                R_middle = 10**0.1
            elif Gamma == -2.0:     
                R_middle = 10**0.15
            elif Gamma == -2.5:                   
                R_middle =  10**0.25
            elif Gamma == -3.0:     
                R_middle = 10**0.5
        if F == 'B_' + 'Hernquist10000_G1.0_199_093': # 198.th perturbation (382.th file)
            if   Gamma == -1.5:      
                R_middle = 10**0.1
            elif Gamma == -2.0:     
                R_middle = 10**0.2
            elif Gamma == -2.5:                   
                R_middle =  10**0.35
            elif Gamma == -3.0:     
                R_middle = 10**0.6
    '''            
    if CS1:
        if F == 'CS1_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if CS2:
        if F == 'CS2_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if CS3:
        if F == 'CS3_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if CS4:
        if F == 'CS4_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if CS5:
        if F == 'CS5_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if CS6:
        if F == 'CS6_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if DS1:
        if F == 'DS1_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if D2:
        if F == 'D2_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    if E:
        if F == 'E_' + 'Osipkov_Merritt10000_G1.0_0_000': # 0.th perturbation (IC file)
            if   Gamma == -1.5:     
                R_middle = 10**
            elif Gamma == -2.0:     
                R_middle = 10**
            elif Gamma == -2.5:                   
                R_middle = 10**
            elif Gamma == -3.0: 
                R_middle = 10**
    '''

if large_R_middle:
    #R_middle =  10**1.3
    R_middle  =  10**1.5
#print 'R_middle = ', R_middle        

Pos   = SnapshotFile['PartType1/Coordinates'].value 
Vel   = SnapshotFile['PartType1/Velocities'].value  
V     = SnapshotFile['PartType1/Potential'].value     
x     = Pos[:,0]
y     = Pos[:,1]
z     = Pos[:,2]
vx    = Vel[:,0]
vy    = Vel[:,1]
vz    = Vel[:,2]
minV  = np.argmin(V)
xC    = x[minV]
yC    = y[minV]
zC    = z[minV]
vxC   = vx[minV]
vyC   = vy[minV]
vzC   = vz[minV]
R     = ((x-xC)**2+(y-yC)**2+(z-zC)**2)**.5

if largest_R_limit:
    R_limit = 10000.
    F       = F + '_R_limit_10000'
elif large_R_limit:
    R_limit = 5000.
    F       = F + '_R_limit_5000'
else:
    R_limit = 500.
    #F      = F + '_R_limit_500'

GoodIDs = np.where(R<R_limit) # Removes all particles that is far away from the cluster.

# make R_limit_min and R_limit_max selection automatic
if R_bin_automatic: # make R_limit_min and R_limit_max selection automatic
    R_limit_min = R_middle
    R_limit_max = R_middle
    a           = 0 # makes sure the while loop is entered.
    x0          = x
    while len(x0)<10000 or a==0:
        R_limit_min = R_limit_min - 0.000005
        R_limit_max = R_limit_max + 0.000005        
        a          += 1
        GoodIDs     = np.where((R<R_limit_max)*(R>R_limit_min))
        x0          =  x[GoodIDs[0]]
   
#DoInnerCut = False
#if DoInnerCut:
#    GoodIDs = np.where(R<R_limit_max)
#else:
#    GoodIDs = np.where((R<R_limit_max)*(R>R_limit_min))

x  =  x[GoodIDs]
y  =  y[GoodIDs]
z  =  z[GoodIDs]
vx =  vx[GoodIDs]
vy =  vy[GoodIDs]
vz =  vz[GoodIDs] 
vx =  vx - np.median(vx)
vy =  vy - np.median(vy)
vz =  vz - np.median(vz)

if bins_202:
    nr_binning_bins = 202
    F               = F + '_200_radial_bins'
elif bins_102:
    nr_binning_bins = 102
    F               = F + '_100_radial_bins'
elif larger_fewer_bins:
    nr_binning_bins = 22
    F               = F + '_20_radial_bins'
else:      
    nr_binning_bins = 52

# Make switches to control figures, print statements, binning etc.
Fig_xz                                       = 1
Fig_3D_xyz                                   = 0
vspherical                                   = 0
calc_sigma_binned_lin_radius                 = 1
Fig_sigmas                                   = 0
vsphericalnew_sigma                          = 0
print_Vp_Vn                                  = 0
print_sigma_binned_lin_radius                = 0
Fig_vr_vtheta_vphi_vt_sigma                  = 0
Fig_vr_vtheta_vphi_vt_sigma_bin_average      = 0



print 'x = ', x
print 'y = ', y
print 'z = ', z

if Fig_xz:
    '''
    f = figure()
    plt.subplot(121)
    #plt.plot(x,y)
    plt.plot(x,y,'o', ms=1)
    plt.xlabel(r'$x_{cluster}$',fontsize=20)
    plt.ylabel(r'$y_{cluster}$',fontsize=20)
    plt.title(r'positions ($N = %i$, $\gamma = %.2f $)' %(len(x),Gamma),fontsize=20)
    plt.grid()

    plt.subplot(122)
    #plt.plot (x,z)
    plt.plot (x,z,'o', ms=1)
    plt.xlabel(r'$x_{cluster}$',fontsize=20)
    plt.ylabel(r'$z_{cluster}$',fontsize=20)
    plt.grid()
    '''


    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    ax1.plot(x,y,'o', ms=1)
    ax1.set_xlabel(r'$x$',fontsize=30)
    ax1.set_ylabel(r'$y$',fontsize=30)
    ax1.set_title(r'positions ($N = %i$)' %len(x),fontsize=30)

    ax2.plot (x,z,'o', ms=1)
    ax2.set_xlabel(r'$x$',fontsize=30)
    ax2.set_ylabel(r'$z$',fontsize=30)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    
    f.savefig(figure_path + 'Fig_xz.png')









#def randrange(n, vmin, vmax): # 3D scatterplot of positions
#    return (vmax-vmin)*np.random.rand(n) + vmin

if Fig_3D_xyz:
    f  = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    n = 100
    for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        ax.scatter(x, y, z, c=c, marker=m)
    ax.set_xlabel('x',fontsize = 20)
    ax.set_ylabel('y',fontsize = 20)
    ax.set_zlabel('z',fontsize = 20)
    ax.set_title('3D view of halo structure.($N = %i$, $\gamma = %.2f $)' %(len(x),Gamma),fontsize = 20)

#sigma_1         = .205
#sigma_2         = .335
#min_binning_R   = -1.5
#max_binning_R   = np.log10(500.0)
#nr_binning_bins = 300

# radial and tangential velocities
if vspherical:
    r      = (x**2 + y**2+ z**2)**.5
    Phi    = sp.arctan2(y,x)
    Theta  = sp.arccos(z/r)
    VR     = sp.sin(Theta)*sp.cos(Phi) * vx + sp.sin(Theta)*sp.sin(Phi) * vy + sp.cos(Theta) * vz
    VTheta = sp.cos(Theta)*sp.cos(Phi) * vx + sp.cos(Theta)*sp.sin(Phi) * vy - sp.sin(Theta) * vz
    VPhi   =             - sp.sin(Phi) * vx +               sp.cos(Phi) * vy
    VT     = VTheta + VPhi

def func_1(x,a,b):
    return a*x*np.exp(-b*x**2.)

def func_2(x,a,b):
    return a*np.exp(-b*x**2.)

def func_3(x,a,b):
    return a*x**2*np.exp(-b*x**2.)

def func_1_log(log10x,a,b):
    x=10.0**log10x
    return a*x*np.exp(-b*x**2.)

def func_2_log(log10x,a,b):
    x=10.0**log10x
    return a*np.exp(-b*x**2.)

def func_3_log(log10x,a,b):
    x=10.0**log10x
    return a*x**2*np.exp(-b*x**2.)

def func_4(x,a,q,b):
    return a*(1.-(1.-q)*b*x**2.)**(q/(1.-q))

def func_5(x,b,q):
    return (1.-(1.-q)*b*x**2.)**(q/(1.-q))

def func_4_log(log10x,a,q,b):
    x=10.0**log10x
    return a*x*(1.-(1.-q)*b*x**2.)**(q/(1.-q))

if calc_sigma_binned_lin_radius:
    R_hob_par = R[GoodIDs]
    v2        = vx**2+vy**2+vz**2

    sigma2                                   = []
    sigmarad2                                = []
    sigmatheta2                              = []
    sigmaphi2                                = []
    sigmatan2                                = []
    sigma                                    = []
    sigmarad                                 = []
    sigmatheta                               = []
    sigmaphi                                 = []
    sigmatan                                 = []
    VR_sigmarad                              = []
    VTheta_sigmatheta                        = []
    VPhi_sigmaphi                            = []
    VT_sigmatan                              = []
    r                                        = []
    Phi                                      = []
    Theta                                    = []
    VR                                       = []
    VTheta                                   = []
    VPhi                                     = []
    VT                                       = []
    VR_i_average_inside_bin                  = []
    VT_i_average_inside_bin                  = []
    VTheta_i_average_inside_bin              = []
    VPhi_i_average_inside_bin                = []
    VR_i_average_inside_bin_sigmarad         = []
    VT_i_average_inside_bin_sigmatan         = []
    VTheta_i_average_inside_bin_sigmatheta   = []
    VPhi_i_average_inside_bin_sigmaphi       = []


    min_binning_R       = -1.5
    max_binning_R       = np.log10(R_limit)
    ##min_binning_R     = R_limit_min
    ##max_binning_R     = R_limit_max

    binning_arr                              = np.logspace(min_binning_R,max_binning_R,nr_binning_bins)
    #binning_arr                             = np.linspace(R_limit_min,R_limit_max,nr_binning_bins) 
    bin_radius_arr                           = []

    j = 0
    for i in range(nr_binning_bins-2):
    #for i in range(nr_binning_bins):    
        min_R_bin_i            = binning_arr[j]    # start of bin
        max_R_bin_i            = binning_arr[j+1]  # end of bin
        posR_par_inside_bin_i  = np.where((R_hob_par>min_R_bin_i)&(R_hob_par<max_R_bin_i)) # position of particles inside a radial bin
        nr_par_inside_bin_i    = len(posR_par_inside_bin_i[0]) 
        if nr_par_inside_bin_i == 0:
            print '-',i
            continue
        print '+',i

        r_i      = (x[posR_par_inside_bin_i]**2 + y[posR_par_inside_bin_i]**2+ z[posR_par_inside_bin_i]**2)**.5
        Phi_i    = sp.arctan2(y[posR_par_inside_bin_i],x[posR_par_inside_bin_i])
        Theta_i  = sp.arccos(z[posR_par_inside_bin_i]/r_i)
        VR_i     = sp.sin(Theta_i)*sp.cos(Phi_i) * vx[posR_par_inside_bin_i] + sp.sin(Theta_i)*sp.sin(Phi_i) * vy[posR_par_inside_bin_i] + sp.cos(Theta_i) * vz[posR_par_inside_bin_i]
        VTheta_i = sp.cos(Theta_i)*sp.cos(Phi_i) * vx[posR_par_inside_bin_i] + sp.cos(Theta_i)*sp.sin(Phi_i) * vy[posR_par_inside_bin_i] - sp.sin(Theta_i) * vz[posR_par_inside_bin_i]
        VPhi_i   =               - sp.sin(Phi_i) * vx[posR_par_inside_bin_i] +                 sp.cos(Phi_i) * vy[posR_par_inside_bin_i]
        VT_i     = (VTheta_i**2 + VPhi_i**2)**.5

        #sigma2 total
        v2_inside_bin_i     = v2[posR_par_inside_bin_i]
        sigma2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(v2_inside_bin_i)
        sigma2.append(sigma2_inside_bin_i)
        bin_radius_arr.append((max_R_bin_i + min_R_bin_i)/2)

        # sigmatan2
        vtan2_inside_bin_i     = VT_i**2
        sigmatan2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(vtan2_inside_bin_i)
        sigmatan2.append(sigmatan2_inside_bin_i)
        #print sigmatan2_inside_bin_i, np.std(VT_i)**2
        #print sigmatan2_inside_bin_i, np.mean(VT_i**2), nr_par_inside_bin_i

        #sigmarad2 radial
        vrad2_inside_bin_i     = VR_i**2
        sigmarad2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(vrad2_inside_bin_i)
        sigmarad2.append(sigmarad2_inside_bin_i)

        #sigmatheta2
        VTheta2_inside_bin_i     = VTheta_i**2
        sigmatheta2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VTheta2_inside_bin_i)
        sigmatheta2.append(sigmatheta2_inside_bin_i)

        #sigmaphi2
        VPhi2_inside_bin_i     = VPhi_i**2
        sigmaphi2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VPhi2_inside_bin_i)
        sigmaphi2.append(sigmaphi2_inside_bin_i)

        VR_i_average_inside_bin_i     = (1./(nr_par_inside_bin_i+1.))*np.sum(VR_i)
        VT_i_average_inside_bin_i     = (1./(nr_par_inside_bin_i+1.))*np.sum(VT_i)
        VTheta_i_average_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VTheta_i)
        VPhi_i_average_inside_bin_i   = (1./(nr_par_inside_bin_i+1.))*np.sum(VPhi_i)

        VR_i_average_inside_bin.append(VR_i_average_inside_bin_i)
        VT_i_average_inside_bin.append(VT_i_average_inside_bin_i)
        VTheta_i_average_inside_bin.append(VTheta_i_average_inside_bin_i)
        VPhi_i_average_inside_bin.append(VPhi_i_average_inside_bin_i)
        '''
        sigma_i      = sigma2_inside_bin_i**.5
        sigma.append(sigma_i)
        print 'sigma = ', sigma 
        sigmarad_i   = sigmarad2_inside_bin_i**.5
        sigmarad.append(sigmarad_i)
        sigmatheta_i = sigmatheta2_inside_bin_i**.5
        sigmatheta.append(sigmatheta_i)
        sigmaphi_i   = sigmaphi2_inside_bin_i**.5
        sigmaphi.append(sigmaphi_i)
        sigmatan_i   = sigmatan2_inside_bin_i**.5
        sigmatan.append(sigmatan_i)
        '''
        sigma_i      = (sigma2[j]     )**.5
        sigmarad_i   = (sigmarad2[j]  )**.5
        sigmatheta_i = (sigmatheta2[j])**.5
        sigmaphi_i   = (sigmaphi2[j]  )**.5
        sigmatan_i   = (sigmatan2[j]  )**.5

        sigma.append(sigma_i          )
        sigmarad.append(sigmarad_i    )
        sigmatheta.append(sigmatheta_i)
        sigmaphi.append(sigmaphi_i    )
        sigmatan.append(sigmatan_i    )
        r.append(r_i                  )   #save arrays
        Phi.append(Phi_i              )
        Theta.append(Theta_i          )
        VR.append(VR_i                )
        VTheta.append(VTheta_i        )
        VPhi.append(VPhi_i            )
        VT.append(VT_i                )
        #np.array(VT                                  )
        VR_sigmarad.append(VR_i/sigmarad_i            )
        VTheta_sigmatheta.append(VTheta_i/sigmatheta_i)
        VPhi_sigmaphi.append(VPhi_i/sigmaphi_i        )
        VT_sigmatan.append(VT_i/sigmatan_i            )
        VR_i_average_inside_bin_sigmarad.append(VR_i_average_inside_bin_i/sigmarad_i            )         
        VT_i_average_inside_bin_sigmatan.append(VT_i_average_inside_bin_i/sigmatan_i            )          
        VTheta_i_average_inside_bin_sigmatheta.append(VTheta_i_average_inside_bin_i/sigmatheta_i)    
        VPhi_i_average_inside_bin_sigmaphi.append(VPhi_i_average_inside_bin_i/sigmaphi_i        )               

        j += 1
    #print 'VR: ', VR
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
    # print r'$\sigma_{tan} = $ '    , linalg.norm(sigmatan  )
    # print r'$\sigma = $ '          , linalg.norm(sigma     )
    # print r'$\sigma_{rad} = $ '    , linalg.norm(sigmarad  )
    # print r'$\sigma_{\phi} = $ '   , linalg.norm(sigmaphi  )
    # print r'$\sigma_{\theta} = $ ' , linalg.norm(sigmatheta)
    # print 'np.concatenate(np.array(VT_sigmatan),axis = 0) = ', np.concatenate(np.array(VT_sigmatan),axis = 0)
    # print sigmatan2_inside_bin_i                             , np.mean(VT_i**2)
    # r           = np.array(r)
    # Phi         = np.array(Phi)
    # Theta       = np.array(Theta)
    # VR          = np.array(VR)
    # VTheta      = np.array(VTheta)
    # VPhi        = np.array(VPhi)
    # VT          = np.array(VT)
    # print 'VR = ', VR
    '''
    r                     = np.concatenate(np.array(r),axis = 0                )
    Phi                   = np.concatenate(np.array(Phi),axis = 0              )
    Theta                 = np.concatenate(np.array(Theta),axis = 0            )
    VR                    = np.concatenate(np.array(VR),axis = 0               )
    VTheta                = np.concatenate(np.array(VTheta),axis = 0           )
    VPhi                  = np.concatenate(np.array(VPhi),axis = 0             )
    VT                    = np.concatenate(np.array(VT),axis = 0               )
    VR_sigmarad           = np.concatenate(np.array(VR_sigmarad),axis = 0      )
    VTheta_sigmatheta     = np.concatenate(np.array(VTheta_sigmatheta),axis = 0)
    VPhi_sigmaphi         = np.concatenate(np.array(VPhi_sigmaphi),axis = 0    )
    VT_sigmatan           = np.concatenate(np.array(VT_sigmatan),axis = 0      )
    '''
    #np.savetxt('v_sigma_Martin.txt',VT_sigmatan)
    #np.savetxt('vtan_Martin.txt',VT)

if Fig_sigmas:
    f = plt.figure()
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
    plt.plot(x_plot,y_plot,'-o', ms=8,mew=0,color='red',   label=r'$\log \sigma_{total}$')
    y_plot = np.log10(sigmarad)
    plt.plot(x_plot,y_plot,'--s',ms=8,mew=0,color='blue',  label=r'$\log \sigma_r$')
    y_plot = np.log10(sigmatheta)
    plt.plot(x_plot,y_plot,'--v',ms=8,mew=0,color='green', label=r'$\log \sigma_{\theta}$')
    y_plot = np.log10(sigmaphi)
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='black', label=r'$\log \sigma_{\phi}$')
    y_plot = np.log10(sigmatan) 
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='Violet',label=r'$\log \sigma_{tan}$')
    plt.xlabel(r'$\log $r (kpc)' , fontsize=20)
    plt.ylabel(r'$\log \sigma$' , fontsize=20)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=3,handlelength=2.5)
    plt.grid()

if vsphericalnew_sigma:
    VR_sigmarad_p       = []
    VR_sigmarad_n       = []
    VTheta_sigmatheta_p = []
    VTheta_sigmatheta_n = []
    VPhi_sigmaphi_p     = []
    VPhi_sigmaphi_n     = []
    VT_sigmatan_p       = []
    VT_sigmatan_n       = []

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
    
    VR_i_average_inside_bin_sigmarad_p       = []
    VR_i_average_inside_bin_sigmarad_n       = []
    VT_i_average_inside_bin_sigmatan_p       = []
    VT_i_average_inside_bin_sigmatan_n       = []
    VPhi_i_average_inside_bin_sigmaphi_p     = []
    VPhi_i_average_inside_bin_sigmaphi_n     = []
    VTheta_i_average_inside_bin_sigmatheta_p = []
    VTheta_i_average_inside_bin_sigmatheta_n = []

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VR_i_average_inside_bin_sigmarad[i] >= 0.:
            VR_i_average_inside_bin_sigmarad_p.append(VR_i_average_inside_bin_sigmarad[i])
        else:
            VR_i_average_inside_bin_sigmarad_n.append(VR_i_average_inside_bin_sigmarad[i])
    VR_i_average_inside_bin_sigmarad_p_arr = np.asarray(VR_i_average_inside_bin_sigmarad_p)
    VR_i_average_inside_bin_sigmarad_n_arr = np.asarray(VR_i_average_inside_bin_sigmarad_n)
    
    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VTheta_i_average_inside_bin_sigmatheta[i] >= 0.:
            VTheta_i_average_inside_bin_sigmatheta_p.append(VTheta_i_average_inside_bin_sigmatheta[i])
        else:
            VTheta_i_average_inside_bin_sigmatheta_n.append(VTheta_i_average_inside_bin_sigmatheta[i])
    VTheta_i_average_inside_bin_sigmatheta_p_arr = np.asarray(VTheta_i_average_inside_bin_sigmatheta_p)
    VTheta_i_average_inside_bin_sigmatheta_n_arr = np.asarray(VTheta_i_average_inside_bin_sigmatheta_n)
    
    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VPhi_i_average_inside_bin_sigmaphi[i] >= 0.:
            VPhi_i_average_inside_bin_sigmaphi_p.append(VPhi_i_average_inside_bin_sigmaphi[i])
        else:
            VPhi_i_average_inside_bin_sigmaphi_n.append(VPhi_i_average_inside_bin_sigmaphi[i])
    VPhi_i_average_inside_bin_sigmaphi_p_arr = np.asarray(VPhi_i_average_inside_bin_sigmaphi_p)
    VPhi_i_average_inside_bin_sigmaphi_n_arr = np.asarray(VPhi_i_average_inside_bin_sigmaphi_n)
    
    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VT_i_average_inside_bin_sigmatan[i] >= 0.:
            VT_i_average_inside_bin_sigmatan_p.append(VT_i_average_inside_bin_sigmatan[i])
        else:
            VT_i_average_inside_bin_sigmatan_n.append(VT_i_average_inside_bin_sigmatan[i])
    VT_i_average_inside_bin_sigmatan_p_arr = np.asarray(VT_i_average_inside_bin_sigmatan_p)
    VT_i_average_inside_bin_sigmatan_n_arr = np.asarray(VT_i_average_inside_bin_sigmatan_n)

if print_Vp_Vn:

    # VTheta            = np.array(VTheta           )
    # VPhi              = np.array(VPhi             )
    # VR_sigmarad       = np.array(VR_sigmarad      )
    # VTheta_sigmatheta = np.array(VTheta_sigmatheta)
    # VPhi_sigmaphi     = np.array(VPhi_sigmaphi    )
    if print_sigma_binned_lin_radius:
        # print 'sigmarad2 = '                , sigmarad2
        # print 'sigmarad2.shape = '          , sigmarad2.shape
        # print 'sigmatheta2 = '              , sigmatheta2
        # print 'sigmatheta2.shape = '        , sigmatheta2.shape
        # print 'sigmaphi2 = '                , sigmaphi2
        # print 'sigmaphi2.shape = '          , sigmaphi2.shape
        # print 'sigmarad = '                 , sigmarad
        # print 'sigmarad.shape = '           , sigmarad.shape
        # print 'sigmatheta = '               , sigmatheta
        # print 'sigmatheta.shape = '         , sigmatheta.shape
        # print 'sigmaphi = '                 , sigmaphi
        # print 'sigmaphi.shape = '           , sigmaphi.shape
        # print 'VR = '                       , VR
        # print 'VR.shape = '                 , VR.shape
        # print 'VTheta = '                   , VTheta
        # print 'VTheta.shape = '             , VTheta.shape
        # print 'VPhi = '                     , VPhi
        # print 'VPhi.shape = '               , VPhi.shape
        # print 'VR_sigmarad.shape = '        , (VR/sigmarad).shape
        # print 'VR_sigmarad = '              , VR/sigmarad
        # print 'np.where(sigmarad == 0) = '  , np.where(sigmarad   == 0)
        # print 'np.where(sigmatheta == 0) = ', np.where(sigmatheta == 0)
        # print 'np.where(sigmaphi == 0) = '  , np.where(sigmaphi   == 0)
        pass

# All figures with log(v) can instead be plotted as log(v) vs. f(v)/v. the idea is, that a flat tail will appear towards small velocities.
# Next I will plot v/sigma along the x-axes instead of v (and with log(v/sigma) as well).
# Plotting v/sigma makes it easier to compare different radial bins, because the x-axis will almost always be the same, even though they actually have very different sigma.

if Fig_vr_vtheta_vphi_vt_sigma:
    x7        = np.asarray(list(VTheta_sigmatheta_p_arr) + list(np.absolute(VTheta_sigmatheta_n_arr)))
    x8        = np.asarray(list(VPhi_sigmaphi_p_arr)     + list(np.absolute(VPhi_sigmaphi_n_arr    )))
    x9        = np.asarray(list(VR_sigmarad_p_arr)       + list(np.absolute(VR_sigmarad_n_arr      )))
    x10       = np.asarray(list(VT_sigmatan_p_arr)       + list(np.absolute(VT_sigmatan_n_arr      )))
    if keep_IC_R_middle:
        f   = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$ , File = %s'%(len(x),Gamma,F))
        n, bins, patches = plt.hist(VT_sigmatan, 50,histtype='step',color='Black',label=r'$f\left(\frac{v_t}{\sigma_t}\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_VT_sigmatan_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        #print 'F+_VT_sigmatan_gamma_%.2f.txt %Gamma = ', F+'_VT_sigmatan_gamma_%.2f.txt' %Gamma

        n, bins, patches = plt.hist(VR_sigmarad, 50,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_VR_sigmarad_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_VTheta_sigmatheta_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VPhi_sigmaphi, 50,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$', alpha=.75)
        #(mu, sigma)     = norm.fit(VR_sigmarad)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        #popt, pcov      = curve_fit(func_2, xdata, ydata)
        #y_fit           = func_2(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_VPhi_sigmaphi_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta}$ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_logx10_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_logx9_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50,histtype='step',color='blue',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_logx7_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', alpha=.75)
        #(mu, sigma)     = norm.fit(np.log10(x9))
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        #popt, pcov      = curve_fit(func_1_log, xdata, ydata)
        #y_fit           = func_1_log(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_logx8_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        ax2.set_yscale('log')
        #plt.ylim(10**-1,10**3)
        #plt.xlim(-3.5,0)
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()

    if new_R_middle:
        f   = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$,File=%s,new R_middle'%(len(x),Gamma,F))
        n, bins, patches = plt.hist(VT_sigmatan,50,histtype='step',color='Black',label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        #print 'x.shape:', x.shape
        np.savetxt(F+'_new_R_middle_VT_sigmatan_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        #print 'F+_VT_sigmatan_gamma_%.2f.txt %Gamma = ', F+'_VT_sigmatan_gamma_%.2f.txt' %Gamma

        n, bins, patches = plt.hist(VR_sigmarad, 50,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_VR_sigmarad_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_VTheta_sigmatheta_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VPhi_sigmaphi, 50,histtype='step', color='green', label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$', alpha=.75)
        #(mu, sigma)     = norm.fit(VR_sigmarad)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        #popt, pcov      = curve_fit(func_2, xdata, ydata)
        #y_fit           = func_2(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\frac{v_r}{\sigma_r}-fit= a \cdot e^{-b \cdot x^2}$')
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_VPhi_sigmaphi_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        #print 'x.shape:',x.shape
        np.savetxt(F+'_new_R_middle_logx10_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_logx9_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50,histtype='step',color='blue',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_logx7_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', alpha=.75)
        #(mu, sigma)     = norm.fit(np.log10(x9))
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        #popt, pcov      = curve_fit(func_1_log, xdata, ydata)
        #y_fit           = func_1_log(xdata,popt[0],popt[1])
        #plt.plot(xdata,y_fit,'--',lw=3,color='pink',label=r'$\log \left( \frac{v_r}{\sigma_r} \right) -fit= a \cdot log(x) \cdot e^{-b \cdot log(x)^2}$')
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_logx8_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        ax2.set_yscale('log')
        #plt.ylim(10**-1,10**3)
        #plt.xlim(-3.5,0)
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()

    if large_R_middle:
        f                = plt.figure()
        ax1              = f.add_subplot(121)
        plt.title(r'$N=%i$, $R_{middle} = %.2f$ ,  File = %s , new R_middle' %(len(x), R_middle, F))
        n, bins, patches = plt.hist(VT_sigmatan, 50,histtype='step',color='Black',label=r'$f\left( u_t \right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VT_sigmatan_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VR_sigmarad, 50,histtype='step',color='red',label=r'$f\left( u_r \right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VR_sigmarad_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left( u_{\theta} \right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VTheta_sigmatheta_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_sigmaphi, 50,histtype='step', color='green', label=r'$f\left( u_{\phi} \right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VPhi_sigmaphi_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_logx10_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( |u_rn|,u_rp \right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_logx9_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7), 50,histtype='step',color='blue',range=(-3,1), label=r'$f\left(\log \left( |u_{\theta}n|,u_{\theta}p \right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_logx7_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( |u_{\phi}n|,u_{\phi}p \right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_logx8_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()

if Fig_vr_vtheta_vphi_vt_sigma_bin_average:
    x7        = np.asarray(list(VTheta_i_average_inside_bin_sigmatheta_p_arr) + list(np.absolute(VTheta_i_average_inside_bin_sigmatheta_n_arr)))
    x8        = np.asarray(list(VPhi_i_average_inside_bin_sigmaphi_p_arr)     + list(np.absolute(VPhi_i_average_inside_bin_sigmaphi_n_arr    )))
    x9        = np.asarray(list(VR_i_average_inside_bin_sigmarad_p_arr)       + list(np.absolute(VR_i_average_inside_bin_sigmarad_n_arr      )))
    x10       = np.asarray(list(VT_i_average_inside_bin_sigmatan_p_arr)       + list(np.absolute(VT_i_average_inside_bin_sigmatan_n_arr      )))

    if keep_IC_R_middle:
        f                = plt.figure()
        ax1              = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s' %(len(x), Gamma, F))
        n, bins, patches = plt.hist(VT_i_average_inside_bin_sigmatan,50,histtype='step',color='Black',label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_VT_i_average_inside_bin_sigmatan_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')
       
        n, bins, patches = plt.hist(VR_i_average_inside_bin_sigmarad, 50,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_VR_i_average_inside_bin_sigmarad_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')
        
        n, bins, patches = plt.hist(VTheta_i_average_inside_bin_sigmatheta,50,histtype='step',color='blue',label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_VTheta_i_average_inside_bin_sigmatheta_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')
        
        n, bins, patches = plt.hist(VPhi_i_average_inside_bin_sigmaphi,50,histtype='step',color='green',label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',alpha=.75)
        xdata = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata = n
        x = np.array((xdata , ydata))
        x = x.transpose()
        np.savetxt(F+'_VPhi_i_average_inside_bin_sigmaphi_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')

        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta}$ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13),numpoints=2,ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10),50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left(\frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_average_logx10_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_average_logx9_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7),50,histtype='step',color='blue',range=(-3,1),label=r'$f\left(\log \left(\frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_average_logx7_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step', color='green',range=(-3,1), label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$', alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_average_logx8_gamma_%.2f.txt'%Gamma,x,delimiter=' ',header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()

    if new_R_middle:
        f   = plt.figure()
        ax1 = f.add_subplot(121)
        plt.title(r'$N=%i$, $\gamma = %.2f$ ,  File = %s , new R_middle' %(len(x), Gamma, F))
        n, bins, patches = plt.hist(VT_i_average_inside_bin_sigmatan, 50,histtype='step',color='Black',label=r'$f\left(\frac{v_t}{\sigma_t}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(VR_i_average_inside_bin_sigmarad, 50,histtype='step',color='red',label=r'$f\left(\frac{v_r}{\sigma_r}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VTheta_i_average_inside_bin_sigmatheta,50,histtype='step',color='blue',label=r'$f\left(\frac{v_{\theta}}{\sigma_{\theta}}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')
        
        n, bins, patches = plt.hist(VPhi_i_average_inside_bin_sigmaphi,50,histtype='step',color='green',label=r'$f\left(\frac{v_{\phi}}{\sigma_{\phi}}\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10),50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_tn|,v_tp}{\sigma_t}\right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_average_logx10_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9),50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_rn|,v_rp}{\sigma_r}\right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_average_logx9_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7),50,histtype='step',color='blue',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_{\theta}n|,v_{\theta}p}{\sigma_{\theta}}\right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_average_logx7_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8),50,histtype='step',color='green',range=(-3,1),label=r'$f\left(\log \left( \frac{|v_{\phi}n|,v_{\phi}p}{\sigma_{\phi}}\right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_new_R_middle_average_logx8_gamma_%.2f.txt' %Gamma, x, delimiter = ' ', header='    bins                         n')

        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()

    if large_R_middle:
        f                = plt.figure()
        ax1              = f.add_subplot(121)
        plt.title(r'$N=%i$, $R_{middle} = %.2f$ ,  File = %s , new R_middle' %(len(x), R_middle, F))
        n, bins, patches = plt.hist(VT_i_average_inside_bin_sigmatan,50,histtype='step',color='Black',label=r'$f\left(u_t \right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_%.2f.txt' %R_middle,x,delimiter=' ', header='    bins                         n')

        n, bins, patches = plt.hist(VR_i_average_inside_bin_sigmarad,50,histtype='step',color='red',label=r'$f\left(u_r \right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_%.2f.txt'%R_middle,x,delimiter=' ',header='    bins                         n')

        n, bins, patches = plt.hist(VTheta_i_average_inside_bin_sigmatheta, 50,histtype='step',color='blue', label=r'$f\left( u_{\theta} \right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_%.2f.txt'%R_middle,x,delimiter=' ', header='    bins                         n')

        n, bins, patches = plt.hist(VPhi_i_average_inside_bin_sigmaphi, 50,histtype='step', color='green',label=r'$f\left( u_{\phi} \right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_%.2f.txt'%R_middle,x,delimiter=' ',header='    bins                         n')
        plt.xlabel(r'$ u_t $, $ u_r $, $ u_{\theta} $ and $ u_{\phi}$')
        plt.ylabel(r'$f\left( u \right)$')
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=1,handlelength=2.5)
        plt.grid()

        ax2              = f.add_subplot(122)
        n, bins, patches = plt.hist(np.log10(x10), 50,histtype='step',color='Black',range=(-3,1),label=r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_average_logx10_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x9), 50,histtype='step',color='red',range=(-3,1),label=r'$f\left(\log \left( |u_rn|,u_rp \right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_average_logx9_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x7),50,histtype='step',color='blue',range=(-3,1),label=r'$f\left(\log \left( |u_{\theta}n|,u_{\theta}p \right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_average_logx7_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')

        n, bins, patches = plt.hist(np.log10(x8), 50,histtype='step',color='green',range=(-3,1),label=r'$f\left(\log \left( |u_{\phi}n|,u_{\phi}p \right)\right)$',alpha=.75)
        xdata            = bins[0:-1]+(bins[1]-bins[0])*.5
        ydata            = n
        x                = np.array((xdata , ydata))
        x                = x.transpose()
        np.savetxt(F+'_large_R_middle_average_logx8_R_middle_%.2f.txt' %R_middle, x, delimiter = ' ', header='    bins                         n')
        ax2.set_yscale('log')
        plt.xlabel(r'$\log \left( |u_tn|,u_tp \right)$, $\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$')
        plt.ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$')
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=2,handlelength=2.5)
        plt.grid()

plt.show()
