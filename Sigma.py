# -*- coding: utf-8 -*-

import h5py
import numpy             as     np
import matplotlib.pyplot as     plt
#from   matplotlib.pyplot import hist2d
import IPython
from   matplotlib.colors import LogNorm
import time
#from   pylab             import *
import pylab
from   scipy.stats       import norm
from   scipy.optimize    import curve_fit
import scipy             as     sp
import seaborn           as     sns

User_path        =                                    '/Users/gustav.c.rasmussen/'
Desktop_path     = User_path                        + 'Desktop/'
GADGET_G_path    = Desktop_path                     + 'RunGadget/G_perturbations/'
Stable_path      =                                    'G_perturbations/Stable_structures/'
figure_path      = Desktop_path + Stable_path       + 'figures/'

#text_files_path  = Desktop_path + Stable_path      + 'text_files/A/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/B/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/Soft_B/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/CS4/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/CS5/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/CS6/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/DS1/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/Soft_D2/'
#text_files_path  = Desktop_path + Stable_path      + 'text_files/E/'

Martin_path      =                                    'Martin_IC_and_Final_Edd_and_OM/'
hdf5_path        = Desktop_path                     + 'G_perturbations/hdf5_files/'
nosync_path      = User_path                        + 'nosync/RunGadget/'

# Filename       = hdf5_path                        + '0G00_IC_000.hdf5'
# Filename       = hdf5_path                        + '0G20_Final_000.hdf5'
# Filename       = hdf5_path                        + 'OMG00_001_IC_000.hdf5'
# Filename       = hdf5_path                        + 'OMG20_Final_000.hdf5'

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
Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_5_005.hdf5'
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_40_005.hdf5'
#Filename        = GADGET_G_path + A_path           + 'Hernquist10000_G1.0_48_009.hdf5'
#Filename        = nosync_path   + A_path           + 'Hernquist10000_G1.0_48_093.hdf5'   
B_path           = 'G_HQ_1000000_B/output/'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_5_005.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_198_000.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_198_093.hdf5'
#Filename        = GADGET_G_path + B_path           + 'Hernquist10000_G1.0_199_093.hdf5'
Soft_B_path      = 'Soft_G_HQ_1000000_B/output/'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_0_000.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_5_005.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_10_005.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_198_000.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_198_093.hdf5'
#Filename        = GADGET_G_path + Soft_B_path      + 'Hernquist10000_G1.0_199_093.hdf5'
CS1_path         = 'G_HQ_10000_CS1/output/'
#Filename        = GADGET_G_path + CS1_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS2_path         = 'G_HQ_10000_CS2/output/'
#Filename        = GADGET_G_path + CS2_path         + 'Osipkov_Merritt10000_G1.0_0_000.hdf5'
CS3_path         = 'G_HQ_10000_CS3/output/'
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
E_path           = 'Soft_G_HQ_1000000_E/output/'
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
#Filename        = GADGET_G_path + E_rfp_path       + 'E_G1.0_50_rfp_093.hdf5' # Fix filename here.

SnapshotFile     = h5py.File(Filename,'r')

#F               = 'test_'                          + Filename[len(GADGET_G_path + test_path):-5                   ]
F               = 'A_'                             + Filename[len(GADGET_G_path + A_path):-5                      ]
#F               = 'A_'                             + Filename[len(nosync_path   + A_path):-5                      ]
#F               = 'B_'                             + Filename[len(GADGET_G_path + B_path):-5                      ]
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

Gamma                                          = -2.0
Beta                                           = 1.

keep_IC_R_middle                               = 0
new_R_middle                                   = 1
R_bin_automatic                                = 0

Fig_v_logr                                     = 0
Fig_v_logr_r2                                  = 0

Fig_x_hist                                     = 0
Fig_x_hist2d                                   = 0

Fig1_xy_xz                                     = 1 # Takes forever. Do not do this plot!
Fig2_v                                         = 0

Fig3_sigma                                     = 0
Fig3_sigma_r_2                                 = 0
Fig3_sigma_divided_by_v_circ_r_2               = 0

Fig4_beta                                      = 0
Fig4_betafit                                   = 0
Fig4_beta_r_2                                  = 0

Fig5_kappa                                     = 0
Fig5_kappafit                                  = 0
Fig5_kappa_r_2                                 = 0

Fig6_gamma                                     = 0
Fig6_gammafit                                  = 0
Fig6_gamma_r_2                                 = 0

Fig7_betagamma                                 = 0
save_lnr_beta_gamma_kappa_VR_r_sigma_r_rr2_rho = 0

save_particle_tracking_ASCII                   = 0
save_combine_ASCII                             = 0
Fig_combine_ASCII                              = 0
save_sigma                                     = 0
Scatterplot_vr_logr                            = 0 # No need. use panel instead
Scatterplot_vr_r                               = 0 # No need. use panel instead
Scatterplot_V_logr                             = 0 # No need. use panel instead
V_vr_r_logr_panel                              = 0

bins_202                                       = 0
bins_102                                       = 0
bins_52                                        = 0 # Reduce number of radial bins in analysis code. This makes them larger and they therefore contain more particles.
bins_22                                        = 1

R_limit_10000                                  = 0 # Analyse larger volume of structure, sets R_limit to 10000.
R_limit_5000                                   = 0 # Analyse large volume of structure, sets R_limit to 5000.
R_limit_500                                    = 0 
R_limit_32                                     = 1

if keep_IC_R_middle: # For R_limit_10000 and 20 bins.
    if F.startswith('Hernquist10000_G'):
        if   Gamma == -1.5:      
                R_middle = 10**-0.70 
        elif Gamma == -2.0:     
                R_middle = 10**-0.25
        elif Gamma == -2.5:                    
                R_middle = 10**-0.0 
        elif Gamma == -3.0:     
                R_middle = 10**-0.30
    if F.startswith('OsipkovMerritt_'):
        if   Gamma == -1.5:      
            R_middle =  0
        elif Gamma == -2.0:     
            R_middle = 0
        elif Gamma == -2.5:                   
            R_middle = 0
        elif Gamma == -3.0:     
            R_middle = 0
if new_R_middle:# Choose new R_middle for each file.
    # A
    if F == 'A_Hernquist10000_G1.0_0_000': # 0.th/IC file
        if   Gamma == -1.5:     
            R_middle = 10**-.7 
        elif Gamma == -2.0:     
            R_middle = 10**-.35
        elif Gamma == -2.5:                    
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.25
    if F == 'A_Hernquist10000_G1.0_5_005': # 5.th file
        if   Gamma == -1.5:       
            R_middle = 10**-.38
        elif Gamma == -2.0:     
            R_middle = 10**-.18
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.4
    if F == 'A_Hernquist10000_G1.0_10_005': # 10.th file
        if   Gamma == -1.5:       
            R_middle = 10**-.35
        elif Gamma == -2.0:     
            R_middle = 10**-.18
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.4
    if F == 'A_Hernquist10000_G1.0_40_005': # 198.th file
        if   Gamma == -1.5:       
            R_middle = 10**-.08
        elif Gamma == -2.0:     
            R_middle = 1.
        elif Gamma == -2.5:                 
            R_middle = 10**.07
        elif Gamma == -3.0:     
            R_middle = 10**.38
    if F == 'A_Hernquist10000_G1.0_48_009': 
        if   Gamma == -1.5:       
            R_middle = 10**-.08
        elif Gamma == -2.0:     
            R_middle = 1.
        elif Gamma == -2.5:                 
            R_middle = 10**.07
        elif Gamma == -3.0:     
            R_middle = 10**.25
    if F == 'A_Hernquist10000_G1.0_48_093': 
        if   Gamma == -1.5:       
            R_middle = 10**-.05
        elif Gamma == -2.0:     
            R_middle = 1.
        elif Gamma == -2.5:                 
            R_middle = 10**.07
        elif Gamma == -3.0:     
            R_middle = 10**.57
    # B
    if F == 'B_Hernquist10000_G1.0_0_000': # 0.th/IC file
        if   Gamma == -1.5:     
            R_middle = 10**-.70 
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                    
            R_middle = 10**-.0 
        elif Gamma == -3.0:     
            R_middle = 10**.3
    if F == 'B_Hernquist10000_G1.0_5_005': # 5.th file
        if   Gamma == -1.5:       
            R_middle = 10**-.4
        elif Gamma == -2.0:     
            R_middle = 10**-.15
        elif Gamma == -2.5:                 
            R_middle = 10**.1
        elif Gamma == -3.0:     
            R_middle = 10**.25
    if F == 'B_Hernquist10000_G1.0_10_005': # 10.th file
        if   Gamma == -1.5:       
            R_middle = 10**-.25
        elif Gamma == -2.0:     
            R_middle = 10**-.14
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.4
    if F == 'B_Hernquist10000_G1.0_198_000': # 198.th file
        if   Gamma == -1.5:       
            R_middle = 10**.1
        elif Gamma == -2.0:     
            R_middle = 10**.2
        elif Gamma == -2.5:                 
            R_middle = 10**.3
        elif Gamma == -3.0:     
            R_middle = 10**.45
    if F == 'B_Hernquist10000_G1.0_198_093': 
        if   Gamma == -1.5:       
            R_middle = 10**.1
        elif Gamma == -2.0:     
            R_middle = 10**.15
        elif Gamma == -2.5:                 
            R_middle = 10**.25
        elif Gamma == -3.0:     
            R_middle = 10**.5
    if F == 'B_Hernquist10000_G1.0_199_093': 
        if   Gamma == -1.5:       
            R_middle = 10**.12
        elif Gamma == -2.0:     
            R_middle = 10**.2
        elif Gamma == -2.5:                 
            R_middle = 10**.25
        elif Gamma == -3.0:     
            R_middle = 10**.42            
    '''
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
            R_middle = 0
        elif Gamma == -2.0:   
            R_middle = 0
        elif Gamma == -2.5:                   
            R_middle = 0
        elif Gamma == -3.0:    
            R_middle = 0
    '''           
    # CS1
    if F == 'CS1_Osipkov_Merritt10000_G1.0_0_000':
        if   Gamma == -1.5:    
            R_middle = 10**-.95
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.35
    # CS2
    if F == 'CS2_Osipkov_Merritt10000_G1.0_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-1.1
        elif Gamma == -2.0:     
            R_middle = 10**-.4
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.4
    # CS3
    if F == 'CS3_Osipkov_Merritt10000_G1.0_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.7
        elif Gamma == -2.0:     
            R_middle = 10**-.4
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.4
    # CS4
    if F == 'CS4_Osipkov_Merritt10000_G1.0_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.75
        elif Gamma == -2.0:     
            R_middle = 10**-.4
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.3
    if F == 'CS4_Osipkov_Merritt10000_G1.0_48_093':
        if   Gamma == -1.5:       
            R_middle = 10**-.05
        elif Gamma == -2.0:     
            R_middle = 1.
        elif Gamma == -2.5:                 
            R_middle = 10**.08
        elif Gamma == -3.0:     
            R_middle = 10**.5
    # CS5
    if F == 'CS5_Osipkov_Merritt10000_G1.0_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.75
        elif Gamma == -2.0:     
            R_middle = 10**-.4
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 10**.3
    if F == 'CS5_Osipkov_Merritt10000_G1.0_48_093':
        if   Gamma == -1.5:       
            R_middle = 10**-.05
        elif Gamma == -2.0:     
            R_middle = 1.
        elif Gamma == -2.5:                 
            R_middle = 10**.08
        elif Gamma == -3.0:     
            R_middle = 10**.7
    # CS6
    if F == 'CS6_Osipkov_Merritt10000_G1.0_0_000':
        if   Gamma == -1.5:     
            R_middle = 10**-.8
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.3
    if F == 'CS6_Osipkov_Merritt10000_G1.0_48_093':
        if   Gamma == -1.5:       
            R_middle = 10**-.05
        elif Gamma == -2.0:     
            R_middle = 1.
        elif Gamma == -2.5:                 
            R_middle = 10**.08
        elif Gamma == -3.0:     
            R_middle = 10.
    # DS1
    if F == 'DS1_Osipkov_Merritt10000_G1.0_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.4
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                 
            R_middle = 10**.05
        elif Gamma == -3.0:     
            R_middle = 10**.2
    if F == 'DS1_Osipkov_Merritt10000_G1.0_49_093':
        if   Gamma == -1.5:       
            R_middle = 10**-.25
        elif Gamma == -2.0:     
            R_middle = 10**-.1
        elif Gamma == -2.5:                 
            R_middle = 10**.1
        elif Gamma == -3.0:     
            R_middle = 10**.65
    # Soft_D2
    if F == 'Soft_D2_Hernquist10000_G1.0_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.45
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                 
            R_middle = 10**.05
        elif Gamma == -3.0:     
            R_middle = 10**.2
    if F == 'Soft_D2_Hernquist10000_G1.0_49_093':
        if   Gamma == -1.5:       
            R_middle = 10**-.3
        elif Gamma == -2.0:     
            R_middle = 10**-.1
        elif Gamma == -2.5:                 
            R_middle = 10**.1
        elif Gamma == -3.0:     
            R_middle = 10**1.4
    # E
    if F == 'E_Hernquist10000_G1.0_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.75
        elif Gamma == -2.0:     
            R_middle = 10**-.4
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.4
    if F == 'E_Hernquist10000_G1.0_198_093':
        if   Gamma == -1.5:       
            R_middle = 10**-.3
        elif Gamma == -2.0:     
            R_middle = 10**-.1
        elif Gamma == -2.5:                 
            R_middle = 10**.1
        elif Gamma == -3.0:     
            R_middle = 10**.4

Pos   = SnapshotFile['PartType1/Coordinates'].value 
Vel   = SnapshotFile['PartType1/Velocities'].value  
V     = SnapshotFile['PartType1/Potential'].value     
x     = Pos[:,0]
y     = Pos[:,1]
z     = Pos[:,2]
print x.shape
vx    = Vel[:,0]
vy    = Vel[:,1]
vz    = Vel[:,2]
minV  = np.argmin(V)  # Finds the particle with the lowest potential (which is in the center of the largest cluster)
xC    = x[minV] # Changes x, y and z so that the cluster is centered.
yC    = y[minV]
zC    = z[minV]
vxC   = vx[minV]
vyC   = vy[minV]
vzC   = vz[minV]
R     = ((x-xC)**2+(y-yC)**2+(z-zC)**2)**.5
#R_xyz = (x**2+y**2+z**2)**.5

if R_limit_10000:
    R_limit = 10000.
    F       = F + '_R_limit_10000'
elif R_limit_5000:
    R_limit = 5000.
    F       = F + '_R_limit_5000'
elif R_limit_500:
    R_limit = 500.
    F      = F + '_R_limit_500'
elif R_limit_32:
    R_limit = 32.
    F      = F + '_R_limit_32'
else:
    pass

GoodIDs = np.where(R<R_limit) # Removes all particles that is far away from the cluster.

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
  
x     =  x[GoodIDs]
y     =  y[GoodIDs]
z     =  z[GoodIDs]
x     = x-np.median(x)
y     = y-np.median(y)
z     = z-np.median(z)
vx    = vx[GoodIDs]
vy    = vy[GoodIDs]
vz    = vz[GoodIDs] 
vx    = vx-np.median(vx)
vy    = vy-np.median(vy)
vz    = vz-np.median(vz)
R_xyz = (x**2+y**2+z**2)**.5

if Fig_x_hist:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0) 
    ax1.set_xlabel(r'$x-x_c$',fontsize=30)
    n, bins, patches = ax1.hist(x-xC,500,normed=1,histtype='stepfilled')
    plt.setp(patches,'facecolor','g','alpha',.75)
    ax1.set_xlim(-40,40)
    ax1.set_ylim(.0,.4)

    ax2.set_xlabel(r'$y-y_c$',fontsize=30)
    n, bins, patches = ax2.hist(y-yC,500,normed=1,histtype='stepfilled')
    plt.setp(patches,'facecolor','g','alpha',.75)
    ax2.set_title(r'Histograms of centralized positions',fontsize=30)
    ax2.set_xlim(-40,40)
    ax2.set_ylim(.0,.4)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='off',labelleft='off')

    ax3.set_xlabel(r'$z-z_c$',fontsize=30)
    n, bins, patches = ax3.hist(z-zC, 500, normed=1, histtype='stepfilled')
    plt.setp(patches, 'facecolor', 'g', 'alpha', .75)
    ax3.set_xlim(-40,40)
    ax3.set_ylim(.0,.4)
    #ax3.axes.get_yaxis().set_visible(False)
    ax3.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='off',labelleft='off')
    
    #f.savefig(figure_path + 'Fig_x_hist.png')
    f.savefig(figure_path + 'Fig_CS4_Final_x_hist_I.png')

if Fig_x_hist2d:
    f = plt.figure(figsize=(13,11))
    plt.xlabel(r'$x-x_c$',fontsize=30)
    plt.ylabel(r'$y-y_c$',fontsize=30)
    plt.hexbin(x-xC,y-yC, gridsize=200)
    plt.xlim(-4,4)
    plt.ylim(-4,4)
    plt.title(r'Histogram of centralized positions x and y (200 hexbins)',fontsize=30)
    #f.savefig(figure_path + 'Fig_x_hist2d.png')
    f.savefig(figure_path + 'Fig_CS4_Final_x_hist2d_I.png')

R_hob_par = R[GoodIDs]

if F.startswith('A_') or F.startswith('B_') or F.startswith('E_'):
    N = 10**6
elif F.startswith('CS4_') or F.startswith('CS5_') or F.startswith('CS6_') or F.startswith('DS1_') or F.startswith('D2_')or F.startswith('Soft_D2_'):
    N = 10**5
elif F.startswith('CS1_') or F.startswith('CS2_') or F.startswith('CS3_'):
    N = 10**4    


if F.startswith('A_') or F.startswith('B_') or F.startswith('CS1_') or F.startswith('CS4_') or F.startswith('CS5_') or F.startswith('CS6_') or F.startswith('E_'):
    M = 1.
elif F.startswith('DS1_') or F.startswith('D2_') or F.startswith('Soft_D2_'):
    M = 1./6.
m = M/N

if Gamma == -2.0:     
    r_2                    = R_middle
    posR_par_inside_halo   = np.where(R_hob_par < r_2) # position of particles inside halo
    nr_par_inside_halo     = len(posR_par_inside_halo[0]) 
    M_2                    = nr_par_inside_halo*m
    G                      = 1.
    v_circ_2               = (G*M_2/r_2)**.5
    #print 'r_2 = '               , r_2
    #print 'nr_par_inside_halo = ', nr_par_inside_halo
    #print 'M_2 = '               , M_2
    #print 'v_circ_2 = '          , v_circ_2

if Fig_v_logr:
    r             = (x**2+y**2+z**2)**.5
    v             = (vx**2+vy**2+vz**2)**.5
    #print 'r = ', r
    #print 'v = ', v
    f, (ax1,ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    ax1.plot(r, v,'o',color = 'Blue',lw=3,ms=2)
    ax1.set_xlabel('r', fontsize=30)
    ax1.set_ylabel(r'velocity, $v = \sqrt{v_x^2+v_y^2+v_z^2}$',fontsize=30)
    #ax1.set_title(r' %s' %F, fontsize=30)
    ax1.set_title(r'A IC (I: $\Delta G,R_{lim}=10^4$)',fontsize=30)
    #ax1.set_title(r'A 10_005 (I: $\Delta G,R_{lim}=10^4$)',fontsize=30)
    #ax1.set_title(r'A 48_009 (I: $\Delta G,R_{lim}=10^4$)',fontsize=30)

    ax2.plot(np.log10(r), v,'o',color = 'Blue',lw=3,ms=2)
    ax2.set_xlabel(r'$\log r$', fontsize=30)
    ax2.yaxis.tick_right()

    f.savefig(figure_path + 'A_IC_v_logr.png'    )
    #f.savefig(figure_path + 'A_10_005_v_logr.png')
    #f.savefig(figure_path + 'A_48_009_v_logr.png')
    #f.savefig(figure_path + 'B_v_logr.png'       )
    #f.savefig(figure_path + 'Soft_B_v_logr.png'  )
    #f.savefig(figure_path + 'CS1_v_logr.png'     )
    #f.savefig(figure_path + 'CS2_v_logr.png'     ) 
    #f.savefig(figure_path + 'CS3_v_logr.png'     ) 
    #f.savefig(figure_path + 'CS4_v_logr.png'     )
    #f.savefig(figure_path + 'CS5_v_logr.png'     )
    #f.savefig(figure_path + 'CS6_v_logr.png'     )
    #f.savefig(figure_path + 'DS1_v_logr.png'     )
    #f.savefig(figure_path + 'D2_v_logr.png'      )
    #f.savefig(figure_path + 'Soft_D2_v_logr.png' )
    #f.savefig(figure_path + 'E_v_logr.png'       )

if Fig_v_logr_r2:
    r             = (x**2+y**2+z**2)**.5
    v             = (vx**2+vy**2+vz**2)**.5
    r_r2          = r/r_2

    f, (ax1,ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    ax1.plot(r_r2, v,'o',color = 'Blue',lw=3,ms=2)
    ax1.set_xlabel(r'$\frac{r}{r_{-2}}$', fontsize=30)
    ax1.set_ylabel(r'velocity, $v = \sqrt{v_x^2+v_y^2+v_z^2}$',fontsize=30)
    #ax1.set_title(r' %s' %F, fontsize=30)
    #ax1.set_title(r'A IC (I: $\Delta G,R_{lim}=10^4$)',fontsize=30)
    #ax1.set_title(r'A 10_005 (I: $\Delta G,R_{lim}=10^4$)',fontsize=30)
    ax1.set_title(r'A 48_009 (I: $\Delta G,R_{lim}=10^4$)',fontsize=30)

    ax2.plot(np.log10(r_r2), v,'o',color = 'Blue',lw=3,ms=2)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax2.yaxis.tick_right()

    #f.savefig(figure_path + 'A_IC_v_logr_r2.png'    )
    #f.savefig(figure_path + 'A_10_005_v_logr_r2.png')
    f.savefig(figure_path + 'A_48_009_v_logr_r2.png')
    #f.savefig(figure_path + 'B_v_logr_r2.png'       )
    #f.savefig(figure_path + 'Soft_B_v_logr_r2.png'  )
    #f.savefig(figure_path + 'CS1_v_logr_r2.png'     )
    #f.savefig(figure_path + 'CS2_v_logr_r2.png'     )
    #f.savefig(figure_path + 'CS3_v_logr_r2.png'     )
    #f.savefig(figure_path + 'CS4_v_logr_r2.png'     )
    #f.savefig(figure_path + 'CS5_v_logr_r2.png'     )
    #f.savefig(figure_path + 'CS6_v_logr_r2.png'     )
    #f.savefig(figure_path + 'DS1_v_logr_r2.png'     )
    #f.savefig(figure_path + 'D2_v_logr_r2.png'      )
    #f.savefig(figure_path + 'Soft_D2_v_logr_r2.png' )
    #f.savefig(figure_path + 'E_v_logr_r2.png'       )














if Fig1_xy_xz: # plot cluster
    f, (ax1,ax2) = plt.subplots(1,2,figsize=(14,10))
    f.subplots_adjust(hspace=0,wspace=0)
    #ax1.title('File = %s'%F,fontsize=30)
    #ax1.set_title(r'$CS_1$ IC ($R_{lim}=32$)',fontsize=30)
    ax1.set_title(r'A IC ($R_{lim}=32$)',fontsize=30)
    ax1.set_xlabel('x',fontsize=30)
    ax1.set_ylabel('y',fontsize=30)
    ax1.plot(x,y,'o',ms=2,mew=0,color='blue')
    #ax1.hist2d(x,y,bins=200,norm=LogNorm())   
    #ax1.colorbar()

    ax2.set_xlabel('x',fontsize=30)
    ax2.set_ylabel('z',fontsize=30)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    ax2.plot(x,z,'o',ms=2,mew=0,color='blue')
    #ax2.hist2d(x,z,bins=200,norm=LogNorm())   
    #ax2.colorbar()
    
    f.savefig(figure_path + 'A_IC_xy_xz.png'    )
    #f.savefig(figure_path + 'B_xy_xz.png'      )
    #f.savefig(figure_path + 'Soft_B_xy_xz.png' )
    #f.savefig(figure_path + 'CS1_xy_xz.png'    )
    #f.savefig(figure_path + 'CS2_xy_xz.png'    )
    #f.savefig(figure_path + 'CS3_xy_xz.png'    )
    #f.savefig(figure_path + 'CS4_xy_xz.png'    )
    #f.savefig(figure_path + 'CS5_xy_xz.png'    )
    #f.savefig(figure_path + 'CS6_xy_xz.png'    )
    #f.savefig(figure_path + 'DS1_xy_xz.png'    )
    #f.savefig(figure_path + 'D2_xy_xz.png'     )
    #f.savefig(figure_path + 'Soft_D2_xy_xz.png')
    #f.savefig(figure_path + 'E_xy_xz.png'      )




# Calculates the median of vx,vy,vz for all particles which are inside the cluster. Thereafter the cluster is centered in velocity-space.
# Using the median is better than using the mean, because the median is insensitive to outliers.
# vx = vx[GoodIDs] - np.median(vx)
# vy = vy[GoodIDs] - np.median(vy)
# vz = vz[GoodIDs] - np.median(vz)

if Fig2_v:           # 3 plots of the velocities as function of x.
    f   = plt.figure()
    ax1 = plt.subplot(131)
    plt.ylabel('vx'  , fontsize=30)
    plt.plot(x,vx,'o',ms=2,mew=0,color='blue')

    ax2 = plt.subplot(132)
    plt.xlabel('x' ,fontsize=30)
    plt.ylabel('vy',fontsize=30)
    plt.title('Velocities (File = %s)'%F,fontsize=30)
    plt.plot(x,vy,'o',ms=2,mew=0,color='blue')
    setp( ax2.get_yticklabels(),visible=False)

    ax3 = plt.subplot(133)
    plt.ylabel('vz' , fontsize=30)
    plt.plot(x,vz,'o',ms=2,mew=0,color='blue')
    setp( ax3.get_yticklabels(),visible=False)

    #f.savefig(figure_path + 'A_v.png'      )
    #f.savefig(figure_path + 'B_v.png'      )
    #f.savefig(figure_path + 'Soft_B_v.png' )
    #f.savefig(figure_path + 'CS1_v.png'    )
    #f.savefig(figure_path + 'CS2_v.png'    )
    #f.savefig(figure_path + 'CS3_v.png'    )
    #f.savefig(figure_path + 'CS4_v.png'    )
    #f.savefig(figure_path + 'CS5_v.png'    )
    #f.savefig(figure_path + 'CS6_v.png'    )
    #f.savefig(figure_path + 'DS1_v.png'    )
    #f.savefig(figure_path + 'D2_v.png'     )
    #f.savefig(figure_path + 'Soft_D2_v.png')
    #f.savefig(figure_path + 'E_v.png'      )

# plot sigma**2 as a function of radius. Make bins and calculate mean(v^2) for the particles in each bin.

sigma2_arr              = [] # square of total velocity dispersion
sigmarad2_arr           = [] # square of radial velosity dispersion
sigmatheta2_arr         = []
sigmaphi2_arr           = []
sigmatan2_arr           = []
v2_arr                  = []
gamma_arr               = []
kappa_arr               = []
beta_arr                = []
density_arr             = []
rho_arr                 = []
Volume_arr              = []
r                       = []
Phi                     = []
Theta                   = []
VR                      = []
VTheta                  = []
VPhi                    = []
VR_i_average_inside_bin = []
v_r                     = (vx*x+vy*y+vz*z)/(x**2+y**2+z**2)**.5

min_binning_R       = -1.5
max_binning_R       = np.log10(R_limit)
##min_binning_R     = R_limit_min
##max_binning_R     = R_limit_max

if bins_202:
    nr_binning_bins = 202
    F               = F + '_200_radial_bins'
elif bins_102:
    nr_binning_bins = 102
    F               = F + '_100_radial_bins'
elif bins_52:
    nr_binning_bins = 52
    F               = F + '_50_radial_bins'
elif bins_22:      
    nr_binning_bins = 22
    F               = F + '_20_radial_bins'
else:
    pass
'''
if non_logarithmic_min_max_binning_R:
    min_binning_R   = 0.03
    max_binning_R   = R_limit
    F               = F + '_non_logarithmic_min_max'
'''   
print F

binning_arr_lin_log10 = np.logspace(min_binning_R,max_binning_R,nr_binning_bins) # Array, -5-1000
bin_radius_arr        = []

for i in range(nr_binning_bins-2):      
    min_R_bin_i            = binning_arr_lin_log10[i]    # start of bin
    max_R_bin_i            = binning_arr_lin_log10[i+1]  # end of bin
    posR_par_inside_bin_i  = np.where((R_hob_par>min_R_bin_i) & (R_hob_par<max_R_bin_i)) # position of particles inside a radial bin
    nr_par_inside_bin_i    = len(posR_par_inside_bin_i[0])                               # number of particles inside a radial bin
    if nr_par_inside_bin_i == 0:
        continue
    # v2 = vx**2+vy**2+vz**2
    v = (vx[posR_par_inside_bin_i]**2+vy[posR_par_inside_bin_i]**2+vz[posR_par_inside_bin_i]**2)**.5
    # sigma2 total
    v2_inside_bin_i     = v**2
    sigma2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(v2_inside_bin_i)
    sigma2_arr.append(sigma2_inside_bin_i)
    bin_radius_arr.append((max_R_bin_i + min_R_bin_i)/2)
    
    # sigmarad2 radial
    vrad2_inside_bin_i     = v_r[posR_par_inside_bin_i]**2
    sigmarad2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(vrad2_inside_bin_i)
    sigmarad2_arr.append(sigmarad2_inside_bin_i)

    # mean_vrad2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(v_r[posR_par_inside_bin_i]**2)
    # mean_sigmarad2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(vrad2_inside_bin_i)

    # calculate volume of cluster:
    Volume_cl = (4./3.)*np.pi*(max_R_bin_i**3 - min_R_bin_i**3)
    # density
    den_cl    = nr_par_inside_bin_i/Volume_cl
    rho       = den_cl*m
 
    r_i                       = (x[posR_par_inside_bin_i]**2+y[posR_par_inside_bin_i]**2+z[posR_par_inside_bin_i]**2)**.5
    Phi_i                     = sp.arctan2(y[posR_par_inside_bin_i],x[posR_par_inside_bin_i])
    Theta_i                   = sp.arccos(z[posR_par_inside_bin_i]/r_i)
    VR_i                      = sp.sin(Theta_i)*sp.cos(Phi_i)*vx[posR_par_inside_bin_i]+sp.sin(Theta_i)*sp.sin(Phi_i)*vy[posR_par_inside_bin_i]+sp.cos(Theta_i)*vz[posR_par_inside_bin_i]
    VTheta_i                  = sp.cos(Theta_i)*sp.cos(Phi_i)*vx[posR_par_inside_bin_i]+sp.cos(Theta_i)*sp.sin(Phi_i)*vy[posR_par_inside_bin_i]-sp.sin(Theta_i)*vz[posR_par_inside_bin_i]
    VPhi_i                    = -sp.sin(Phi_i)*vx[posR_par_inside_bin_i]+sp.cos(Phi_i)*vy[posR_par_inside_bin_i]
    VR_i_average_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VR_i)
    
    # sigmatheta2
    VTheta2_inside_bin_i     = VTheta_i**2
    sigmatheta2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VTheta2_inside_bin_i)
    sigmatheta2_arr.append(sigmatheta2_inside_bin_i)

    #sigmaphi2
    VPhi2_inside_bin_i     = VPhi_i**2
    sigmaphi2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VPhi2_inside_bin_i)
    sigmaphi2_arr.append(sigmaphi2_inside_bin_i)

    #sigmatan2
    sigmatan  = (sigmatheta2_inside_bin_i + sigmaphi2_inside_bin_i)**.5
    sigmatan2 = sigmatan**2
    sigmatan2_arr.append(sigmatan2)

    #save arrays
    density_arr.append(den_cl  )
    rho_arr.append(rho         )
    Volume_arr.append(Volume_cl)
    r.append(r_i               )
    Phi.append(Phi_i           )
    Theta.append(Theta_i       )
    VR.append(VR_i             )
    VR_i_average_inside_bin.append(VR_i_average_inside_bin_i)
    VTheta.append(VTheta_i     )
    VPhi.append(VPhi_i         )

# Change the nesessary lists into arrays
sigma2_arr                  = np.array(sigma2_arr) # square of total velocity dispersion
sigmarad2_arr               = np.array(sigmarad2_arr)
bin_radius_arr              = np.array(bin_radius_arr)
r_arr                       = np.array(r)
Phi_arr                     = np.array(Phi)
Theta_arr                   = np.array(Theta)
VR_arr                      = np.array(VR)
VTheta_arr                  = np.array(VTheta)
VPhi_arr                    = np.array(VPhi)
VR_i_average_inside_bin_arr = np.array(VR_i_average_inside_bin)
# VR_mean_arr               = np.concatenate(VR_arr,axis=0)

for  i in range(len(sigma2_arr)): #kappa
    if i == 0 or i == len(sigma2_arr)-1:
        kappa_arr.append(np.nan)
        continue
    dlogr         = np.log10(bin_radius_arr[i+1]) - np.log10(bin_radius_arr[i-1])
    dlogsigmarad2 = np.log10(sigmarad2_arr[i+1])-np.log10(sigmarad2_arr[i-1])
    kappa_arr.append(dlogsigmarad2/dlogr)

for  i in range(len(density_arr)): #gamma
    if i == 0 or i == len(sigma2_arr)-1:
        gamma_arr.append(np.nan)
        continue
    dlogr   = np.log10(bin_radius_arr[i+1]) - np.log10(bin_radius_arr[i-1])
    dlogrho = np.log10(density_arr[i+1])    - np.log10(density_arr[i-1])
    gamma_arr.append(dlogrho/dlogr)

beta_arr = 1. - sigmatheta2_arr/sigmarad2_arr # Calculate beta

if Fig3_sigma:  # Dispersions
    f      = plt.figure(figsize=(16,11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = np.log10(sigma2_arr)
 
    plt.plot(x_plot,y_plot,'-o',ms=8,mew=0,color='red',label=r'$\log (\sigma_{total}^2)$'    )
    y_plot = np.log10(sigmarad2_arr)
    plt.plot(x_plot,y_plot,'--s',ms=8,mew=0,color='blue',label=r'$\log (\sigma_{r}^2)$'      )
    y_plot = np.log10(sigmatheta2_arr)
    plt.plot(x_plot,y_plot,'--v',ms=8,mew=0,color='green',label=r'$\log (\sigma_{\theta}^2)$')
    y_plot = np.log10(sigmaphi2_arr)
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='black',label=r'$\log (\sigma_{\phi}^2)$'  )
    y_plot = np.log10(sigmatan2_arr) # plot sigma_tan
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='Violet',label=r'$\log (\sigma_{tan}^2)$'  )

    plt.xlabel(r'$\log $r'         ,fontsize=30)
    plt.ylabel(r'$\log (\sigma^2)$',fontsize=30)
    #plt.title(r'Velocity dispersions (File = %s)' %F , fontsize=30)
    #plt.title(r'Velocity dispersions (B IC, $R_{limit} = 10^4$, 20 radial bins)',fontsize=30)
    #plt.title(r'Velocity dispersions (B 198_093, $R_{limit} = 10^4$, 20 radial bins)',fontsize=30)
    leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    #f.savefig(figure_path + 'A_sigma.png'        )
    #f.savefig(figure_path + 'B_IC_sigma.png'     )
    #f.savefig(figure_path + 'B_198_093_sigma.png')
    #f.savefig(figure_path + 'Soft_B_sigma.png'   )
    #f.savefig(figure_path + 'CS1_sigma.png'      )
    #f.savefig(figure_path + 'CS2_sigma.png'      )
    #f.savefig(figure_path + 'CS3_sigma.png'      )
    #f.savefig(figure_path + 'CS4_sigma.png'      )
    #f.savefig(figure_path + 'CS5_sigma.png'      )
    #f.savefig(figure_path + 'CS6_sigma.png'      )
    #f.savefig(figure_path + 'DS1_sigma.png'      )
    #f.savefig(figure_path + 'D2_sigma.png'       )
    #f.savefig(figure_path + 'Soft_D2_sigma.png'  )
    #f.savefig(figure_path + 'E_sigma.png'        )

if Fig3_sigma_r_2:  # Dispersions
    f      = plt.figure(figsize=(16,11))
    x_plot = np.log10(bin_radius_arr/r_2)
    y_plot = np.log10(sigma2_arr)
    plt.plot(x_plot,y_plot,'-o',ms=8,mew=0,color='red',label=r'$\log (\sigma_{total}^2)$')
    y_plot = np.log10(sigmarad2_arr)
    plt.plot(x_plot,y_plot,'--s',ms=8,mew=0,color='blue',label=r'$\log (\sigma_{r}^2)$')
    y_plot = np.log10(sigmatheta2_arr)
    plt.plot(x_plot,y_plot,'--v',ms=8,mew=0,color='green',label=r'$\log (\sigma_{\theta}^2)$')
    y_plot = np.log10(sigmaphi2_arr)
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='black',label=r'$\log (\sigma_{\phi}^2)$')
    y_plot = np.log10(sigmatan2_arr) # plot sigma_tan
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='Violet',label=r'$\log (\sigma_{\tan}^2)$')
    leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    plt.ylabel(r'$\log (\sigma^2) $',fontsize=30)
    
    #plt.title(r'Velocity dispersions (File = %s)' %F , fontsize=30)
    plt.title(r'Velocity dispersions (B IC, $R_{limit} = 10^4$, 20 radial bins)',fontsize=30)
    #plt.title(r'Velocity dispersions (B 198_093, $R_{limit} = 10^4$, 20 radial bins)',fontsize=30)
    #f.savefig(figure_path + 'A_sigma_r_2.png'      )
    f.savefig(figure_path + 'B_IC_sigma_r_2.png'      )
    #f.savefig(figure_path + 'B_198_093_sigma_r_2.png'      )
    #f.savefig(figure_path + 'Soft_B_sigma_r_2.png' )
    #f.savefig(figure_path + 'CS1_sigma_r_2.png'    )
    #f.savefig(figure_path + 'CS2_sigma_r_2.png'    )
    #f.savefig(figure_path + 'CS3_sigma_r_2.png'    )
    #f.savefig(figure_path + 'CS4_sigma_r_2.png'    )
    #f.savefig(figure_path + 'CS5_sigma_r_2.png'    )
    #f.savefig(figure_path + 'CS6_sigma_r_2.png'    )
    #f.savefig(figure_path + 'DS1_sigma_r_2.png'    )
    #f.savefig(figure_path + 'D2_sigma_r_2.png'     )
    #f.savefig(figure_path + 'Soft_D2_sigma_r_2.png')
    #f.savefig(figure_path + 'E_sigma_r_2.png'      )

if Fig3_sigma_divided_by_v_circ_r_2:  # Dispersions
    f      = plt.figure(figsize=(16,11))
    x_plot = np.log10(bin_radius_arr/r_2)
    y_plot = np.log10(sigma2_arr/v_circ_2**2)
    # label=r'$\log ((\frac{\sigma_{total}}{v_{circ,2}})^2)$'
    plt.plot(x_plot,y_plot,'-o',ms=8,mew=0,color='red',label=r'$\log (\bar{\sigma_{total}}^2)$')
    y_plot = np.log10(sigmarad2_arr/v_circ_2**2)
    plt.plot(x_plot,y_plot,'--s',ms=8,mew=0,color='blue',label=r'$\log (\bar{\sigma_{r}}^2)$')
    y_plot = np.log10(sigmatheta2_arr/v_circ_2**2)
    plt.plot(x_plot,y_plot,'--v',ms=8,mew=0,color='green',label=r'$\log (\bar{\sigma_{\theta}}^2)$')
    y_plot = np.log10(sigmaphi2_arr/v_circ_2**2)
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='black',label=r'$\log (\bar{\sigma_{\phi}}^2)$')
    y_plot = np.log10(sigmatan2_arr/v_circ_2**2) # plot sigma_tan
    plt.plot(x_plot,y_plot,'--^',ms=8,mew=0,color='Violet',label=r'$\log (\bar{\sigma_{\tan}}^2)$')

    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$' , fontsize=30)
    #plt.ylabel(r'$\log (\frac{\sigma^2}{v_{circ,2}} ) $' , fontsize=26)
    plt.ylabel(r'$\log (\bar{\sigma}^2) $' , fontsize=30)
    
    #plt.title(r'Velocity dispersions (File = %s)' %F , fontsize=26)
    plt.title(r'Velocity dispersions (B IC, $R_{limit} = 10^4$, 20 radial bins)',fontsize=30)
    leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    #f.savefig(figure_path + 'A_sigma_divided_by_v_circ_r_2.png'      )
    f.savefig(figure_path + 'B_sigma_divided_by_v_circ_r_2.png'      )
    #f.savefig(figure_path + 'Soft_B_sigma_divided_by_v_circ_r_2.png' )
    #f.savefig(figure_path + 'CS1_sigma_divided_by_v_circ_r_2.png'    )
    #f.savefig(figure_path + 'CS2_sigma_divided_by_v_circ_r_2.png'    )
    #f.savefig(figure_path + 'CS3_sigma_divided_by_v_circ_r_2.png'    )
    #f.savefig(figure_path + 'CS4_sigma_divided_by_v_circ_r_2.png'    )
    #f.savefig(figure_path + 'CS5_sigma_divided_by_v_circ_r_2.png'    )
    #f.savefig(figure_path + 'CS6_sigma_divided_by_v_circ_r_2.png'    )
    #f.savefig(figure_path + 'DS1_sigma_divided_by_v_circ_r_2.png'    )
    #f.savefig(figure_path + 'D2_sigma_divided_by_v_circ_r_2.png'     )
    #f.savefig(figure_path + 'Soft_D2_sigma_divided_by_v_circ_r_2.png')
    #f.savefig(figure_path + 'E_sigma_divided_by_v_circ_r_2.png'      )

if Fig4_beta:  # plot beta
    f      = plt.figure(figsize=(16,11))
    #plt.xlim(-1.,1.0)
    plt.ylim(-1.,1.)
    x_plot = np.log10(bin_radius_arr)
    y_plot = beta_arr
    plt.xlabel(r'$\log$r',fontsize=30)
    plt.ylabel(r'$\beta$',fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black') 
    #plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') # from this graph we see that beta is below zero. this means sigmatheta2_arr/sigmarad2_arr > 1, which in turn means that sigmatheta2_arr > sigmarad2_arr. 
    plt.plot(x_plot,0*x_plot,'--',lw=2,color='grey')
    plt.plot((-.5,-.5),(-1.,1.), 'r-',label=r'inner cut')
    #plt.plot((1.,1.),(-1.,1.)  , 'b-',label=r'outer cut')

    if Fig4_betafit: # fitting beta with two different profiles
        x      = 10**x_plot
        y_plot = x**2/(4**2+x**2)
        plt.plot(x_plot,y_plot,'-',ms=2,mew=0,color='blue',label=r'$\frac{r^2}{4^2+r^2}$') 
        #plt.title(r'$\beta$ with fit (%s)' %F , fontsize=26)
        plt.title(r'$\beta$ with analytical expression (CS6 IC with 20 radial bins)',fontsize=30)
        '''
        Chi2 = 0
        i    = 0
        while (i < len(beta_arr)):
            if isnan(beta_arr[i]):
                print 'nan at index: ', i
            else:
                Chi2 = Chi2 + ((beta_arr[i]-y_plot[i])**2)/(beta_arr[i]*.2)**2               
            i = i+1
        Chi2 = (1.0/(len(beta_arr)-1)) * Chi2
        print 'Chi2 for betafit: ', Chi2
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',label = r'$\chi^2 = %.6f$' %Chi2)
        '''
        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        #f.savefig(figure_path + 'A_IC_beta_logr_fit.png'         )
        #f.savefig(figure_path + 'B_IC_beta_logr_fit.png'         )
        #f.savefig(figure_path + 'Soft_B_IC_beta_logr_fit.png'    )
        #f.savefig(figure_path + 'CS1_IC_beta_logr_fit.png'       )
        #f.savefig(figure_path + 'CS4_IC_beta_logr_fit.png'       )
        #f.savefig(figure_path + 'CS5_IC_beta_logr_fit.png'       )
        #f.savefig(figure_path + 'CS6_IC_beta_logr_fit.png'       )
        #f.savefig(figure_path + 'DS1_IC_beta_logr_fit.png'       )
        #f.savefig(figure_path + 'D2_beta_logr_fit.png'           )
        #f.savefig(figure_path + 'Soft_D2_beta_logr_fit.png'      )
        #f.savefig(figure_path + 'Soft_D2_Final_beta_logr_fit.png')
        #f.savefig(figure_path + 'E_beta_logr_fit.png'            )
       
    else:

        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        
        #plt.title(r'$\beta$ with zero-line(%s)' %F , fontsize=30)
        #plt.title(r'$\beta$ with zero-line (A 48_009, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (B 199_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (CS4 48_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (CS5 48_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (CS6 48_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (DS1 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (D2 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (Soft_D2 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (E 198_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)

        plt.title(r'$\beta$ with zero-line (A 48_009, $R_{limit}=32, 50$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (B 199_093, $R_{limit}=32, 50$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (CS4 48_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (CS5 48_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (CS6 48_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (DS1 49_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (D2 49_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (Soft_D2 49_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line (E 198_093, $R_{limit}=32, 50$ bins)',fontsize=30)

        #f.savefig(figure_path + 'A_IC_beta_logr_I_R32.png'          )
        #f.savefig(figure_path + 'A_48_009_beta_logr_I_R32.png'      )
        f.savefig(figure_path + 'A_48_009_beta_logr_I_R32_cuts.png'      )
        #f.savefig(figure_path + 'B_IC_beta_logr_I_R32.png'          )
        #f.savefig(figure_path + 'B_199_093_beta_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_B_IC_beta_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_B_Final_beta_logr_I_R32.png'  )
        #f.savefig(figure_path + 'CS1_IC_beta_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS4_IC_beta_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS4_48_093_beta_logr_I_R32.png'    )
        #f.savefig(figure_path + 'CS5_IC_beta_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS5_48_093_beta_logr_I_R32.png'    )
        #f.savefig(figure_path + 'CS6_IC_beta_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS6_48_093_beta_logr_I_R32.png'    )
        #f.savefig(figure_path + 'DS1_IC_beta_logr_I_R32.png'        )
        #f.savefig(figure_path + 'DS1_49_093_beta_logr_I_R32.png'    )
        #f.savefig(figure_path + 'D2_beta_logr_I_R32.png'            )
        #f.savefig(figure_path + 'D2_49_093_beta_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_D2_beta_logr_I_R32.png'       )
        #f.savefig(figure_path + 'Soft_D2_49_093_beta_logr_I_R32.png')
        #f.savefig(figure_path + 'E_beta_logr_I_R32.png'             )
        #f.savefig(figure_path + 'E_198_093_beta_logr_I_R32.png'     ) 

        #f.savefig(figure_path + 'A_IC_beta_logr.png'         )
        #f.savefig(figure_path + 'A_48_009_beta_logr.png'      )
        #f.savefig(figure_path + 'B_IC_beta_logr.png'         )
        #f.savefig(figure_path + 'B_199_093_beta_logr.png'      )
        #f.savefig(figure_path + 'Soft_B_IC_beta_logr.png'    )
        #f.savefig(figure_path + 'Soft_B_Final_beta_logr.png' )
        #f.savefig(figure_path + 'CS1_IC_beta_logr.png'       )
        #f.savefig(figure_path + 'CS4_IC_beta_logr.png'       )
        #f.savefig(figure_path + 'CS4_48_093_beta_logr.png'    )
        #f.savefig(figure_path + 'CS5_IC_beta_logr.png'       )
        #f.savefig(figure_path + 'CS5_48_093_beta_logr.png'    )
        #f.savefig(figure_path + 'CS6_IC_beta_logr.png'       )
        #f.savefig(figure_path + 'CS6_48_093_beta_logr.png'    )
        #f.savefig(figure_path + 'DS1_IC_beta_logr.png'       )
        #f.savefig(figure_path + 'DS1_49_093_beta_logr.png'    )
        #f.savefig(figure_path + 'D2_beta_logr.png'           )
        #f.savefig(figure_path + 'D2_49_093_beta_logr.png'     )
        #f.savefig(figure_path + 'Soft_D2_beta_logr.png'      )
        #f.savefig(figure_path + 'Soft_D2_49_093_beta_logr.png')
        #f.savefig(figure_path + 'E_beta_logr.png'            )
        #f.savefig(figure_path + 'E_198_093_beta_logr.png'      ) 

if Fig4_beta_r_2:  # plot beta
    f      = plt.figure(figsize=(16,11))
    #plt.xlim(-1.7,2.0)
    #plt.ylim(-.2,1.)
    x_plot = np.log10(bin_radius_arr/r_2)
    y_plot = beta_arr
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    plt.ylabel(r'$\beta$',fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') # from this graph we see that beta is below zero. this means sigmatheta2_arr/sigmarad2_arr > 1, which in turn means that sigmatheta2_arr > sigmarad2_arr. 
    plt.plot(x_plot,0*x_plot,'--',lw=2,color='grey')
    #plt.title(r'$\beta$ with zero-line(%s)' %F , fontsize=30)
    #plt.title(r'Velocity anisotropy (CS6 IC with 20 radial bins)', fontsize=30)
    
    #f.savefig(figure_path + 'A_IC_beta_r_2_logr.png'         )
    #f.savefig(figure_path + 'A_Final_beta_r_2_logr.png'      )
    #f.savefig(figure_path + 'B_IC_beta_r_2_logr.png'         )
    #f.savefig(figure_path + 'B_Final_beta_r_2_logr.png'      )
    #f.savefig(figure_path + 'Soft_B_IC_beta_r_2_logr.png'    )
    #f.savefig(figure_path + 'Soft_B_Final_beta_r_2_logr.png' )
    #f.savefig(figure_path + 'CS1_IC_beta_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS4_IC_beta_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS4_Final_beta_r_2_logr.png'    )
    #f.savefig(figure_path + 'CS5_IC_beta_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS5_Final_beta_r_2_logr.png'    )
    #f.savefig(figure_path + 'CS6_IC_beta_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS6_Final_beta_r_2_logr.png'    )
    #f.savefig(figure_path + 'DS1_IC_beta_r_2_logr.png'       )
    #f.savefig(figure_path + 'DS1_Final_beta_r_2_logr.png'    )
    #f.savefig(figure_path + 'D2_beta_r_2_logr.png'           )
    #f.savefig(figure_path + 'D2_Final_beta_r_2_logr.png'     )
    #f.savefig(figure_path + 'Soft_D2_beta_r_2_logr.png'      )
    #f.savefig(figure_path + 'Soft_D2_Final_beta_r_2_logr.png')
    #f.savefig(figure_path + 'E_beta_r_2_logr.png'            )
    #f.savefig(figure_path + 'E_Final_beta_r_2_logr.png'      ) 

if Fig5_kappa:
    f      = plt.figure(figsize=(16,11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = kappa_arr
    plt.xlabel(r'$\log $r',fontsize=30)
    plt.ylabel(r'$\kappa$',fontsize=30)
    plt.ylim(-4.,.4)
    plt.plot(x_plot,y_plot,'-o',ms=4,mew=0,color='black')
    #plt.plot(x_plot,y_plot,'-o',ms=4,mew=0,color='black',label=r'$\kappa$')
    #plt.plot(x_plot,0*x_plot,'--',lw=2,color='grey')
    plt.plot((-.92,-.92),(-5.,25.), 'r-',label=r'inner cut')
    #plt.plot((1.,1.),(-4.,4.), 'b-',label=r'outer cut')

    if Fig5_kappafit: # fitting beta with two different profiles
        x      = bin_radius_arr
        #x     = 10**x_plot
        l      = np.log(x)
        ll     = np.log(x+1)

        num1   = -151.9999999*x+12*ll-12*l-250*x**2-37+48*ll*x**5-48*l*x**5+204*ll*x**4-204*l*x**4+336*ll*x**3-336*l*x**3
        num2   = 264*ll*x**2-264*l*x**2+96*ll*x-96*l*x+2*10**(-8)*x**5-47.99999992*x**4-179.9999999*x**3
        denom  = (12*ll*x**4-12*l*x**4+4.049710908*10**(-9)*x**4+48*ll*x**3-48*l*x**3-11.99999998*x**3+72*ll*x**2-72*l*x**2-41.99999998*x**2+48*ll*x-48*l*x-51.99999998*x+12*ll-12*l-25)*(x+1)
        
        y_plot = (num1+num2)/denom

        #print 'y_plot.shape = ', y_plot.shape
        print 'len(y_plot) = ' , len(y_plot)
        #print 'y_plot[1.] = ', y_plot[1.] 

        plt.plot(x_plot[0:len(y_plot)-3],y_plot[0:len(y_plot)-3],'-',ms=2,mew=0,color='blue',label=r'Analytical shape')
        #plt.plot(x_plot[1:len(y_plot)-3],y_plot[1:len(y_plot)-3],'-',ms=2,mew=0,color='blue',label=r'Analytical shape')
        #plt.title(r'$\kappa$ with fit (%s)' %F , fontsize=30)
        plt.title(r'$\kappa$ with analytical expression (B IC with 20 radial bins)',fontsize=30)
        plt.ylim(-2.,.5)
        '''
        Chi2 = 0
        i    = 0
        while (i < len(kappa_arr)):
            if isnan(kappa_arr[i]):
                print 'nan at index: ', i
            else:
                Chi2 = Chi2 + ((kappa_arr[i]-y_plot[i])**2)/(kappa_arr[i]*.2)**2               
            i = i+1
        Chi2 = (1.0/(len(kappa_arr)-1)) * Chi2
        print 'Chi2 for kappafit: ', Chi2
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',label = r'$\chi^2 = %.6f$' %Chi2)
        '''
        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        
        #f.savefig(figure_path + 'A_IC_kappa_logr_fit.png'         )
        #f.savefig(figure_path + 'B_IC_kappa_logr_fit.png'         )
        #f.savefig(figure_path + 'Soft_B_IC_kappa_logr_fit.png'    )
        #f.savefig(figure_path + 'CS1_IC_kappa_logr_fit.png'       )
        #f.savefig(figure_path + 'CS2_IC_kappa_logr_fit.png'       )
        #f.savefig(figure_path + 'CS3_IC_kappa_logr_fit.png'       )
        #f.savefig(figure_path + 'CS4_IC_kappa_logr_fit.png'       )
        #f.savefig(figure_path + 'CS5_IC_kappa_logr_fit.png'       )
        #f.savefig(figure_path + 'CS6_IC_kappa_logr_fit.png'       )
        #f.savefig(figure_path + 'DS1_IC_kappa_logr_fit.png'       )
        #f.savefig(figure_path + 'D2_kappa_logr_fit.png'           )
        #f.savefig(figure_path + 'Soft_D2_kappa_logr_fit.png'      )
        #f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_fit.png')
        #f.savefig(figure_path + 'E_kappa_logr_fit.png'            )
       
    else:

        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        
        #plt.title(r'$\kappa$ and zero-line (%s)' %F,fontsize=30)
        #plt.title(r'$\kappa$ and zero-line (A 48_009, $R_{limit}=10^4, 20$ bins)',fontsize=30      )
        #plt.title(r'$\kappa$ and zero-line (B 199_093, $R_{limit}=10^4, 20$ bins)',fontsize=30     )
        #plt.title(r'$\kappa$ and zero-line (CS4 48_093, $R_{limit}=10^4, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (CS5 48_093, $R_{limit}=10^4, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (CS6 48_093, $R_{limit}=10^4, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (DS1 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (D2 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30     )
        #plt.title(r'$\kappa$ and zero-line (Soft_D2 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title(r'$\kappa$ and zero-line (E 198_093, $R_{limit}=10^4, 20$ bins)',fontsize=30     )

        plt.title(r'$\kappa$ and zero-line (A 48_009, $R_{limit}=32, 50$ bins)',fontsize=30      )
        #plt.title(r'$\kappa$ and zero-line (B 199_093, $R_{limit}=32, 50$ bins)',fontsize=30     )
        #plt.title(r'$\kappa$ and zero-line (CS4 48_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (CS5 48_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (CS6 48_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (DS1 49_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title(r'$\kappa$ and zero-line (D2 49_093, $R_{limit}=32, 20$ bins)',fontsize=30     )
        #plt.title(r'$\kappa$ and zero-line (Soft_D2 49_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title(r'$\kappa$ and zero-line (E 198_093, $R_{limit}=32, 50$ bins)',fontsize=30     )

        #f.savefig(figure_path + 'A_IC_kappa_logr_I_R32.png'          )
        #f.savefig(figure_path + 'A_48_009_kappa_logr_I_R32.png'      )
        f.savefig(figure_path + 'A_48_009_kappa_logr_I_R32_cuts.png'  )
        #f.savefig(figure_path + 'B_IC_kappa_logr_I_R32.png'          )
        #f.savefig(figure_path + 'B_199_093_kappa_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_B_IC_kappa_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_B_Final_kappa_logr_I_R32.png'  )
        #f.savefig(figure_path + 'CS1_IC_kappa_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS4_IC_kappa_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS4_48_093_kappa_logr_I_R32.png'    )
        #f.savefig(figure_path + 'CS5_IC_kappa_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS5_48_093_kappa_logr_I_R32.png'    )
        #f.savefig(figure_path + 'CS6_IC_kappa_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS6_48_093_kappa_logr_I_R32.png'    )
        #f.savefig(figure_path + 'DS1_IC_kappa_logr_I_R32.png'        )
        #f.savefig(figure_path + 'DS1_49_093_kappa_logr_I_R32.png'    )
        #f.savefig(figure_path + 'D2_kappa_logr_I_R32.png'            )
        #f.savefig(figure_path + 'D2_49_093_kappa_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_D2_kappa_logr_I_R32.png'       )
        #f.savefig(figure_path + 'Soft_D2_49_093_kappa_logr_I_R32.png')
        #f.savefig(figure_path + 'E_kappa_logr_I_R32.png'             )
        #f.savefig(figure_path + 'E_198_093_kappa_logr_I_R32.png'     ) 
        
        #f.savefig(figure_path + 'A_IC_kappa_logr.png'         )
        #f.savefig(figure_path + 'A_48_009_kappa_logr.png'      )
        #f.savefig(figure_path + 'B_IC_kappa_logr.png'         )
        #f.savefig(figure_path + 'B_199_093_kappa_logr.png'      )
        #f.savefig(figure_path + 'Soft_B_IC_kappa_logr.png'    )
        #f.savefig(figure_path + 'Soft_B_Final_kappa_logr.png' )
        #f.savefig(figure_path + 'CS1_IC_kappa_logr.png'       )
        #f.savefig(figure_path + 'CS4_IC_kappa_logr.png'       )
        #f.savefig(figure_path + 'CS4_48_093_kappa_logr.png'    )
        #f.savefig(figure_path + 'CS5_IC_kappa_logr.png'       )
        #f.savefig(figure_path + 'CS5_48_093_kappa_logr.png'    )
        #f.savefig(figure_path + 'CS6_IC_kappa_logr.png'       )
        #f.savefig(figure_path + 'CS6_48_093_kappa_logr.png'    )
        #f.savefig(figure_path + 'DS1_IC_kappa_logr.png'       )
        #f.savefig(figure_path + 'DS1_49_093_kappa_logr.png'    )
        #f.savefig(figure_path + 'D2_kappa_logr.png'           )
        #f.savefig(figure_path + 'D2_49_093_kappa_logr.png'     )
        #f.savefig(figure_path + 'Soft_D2_kappa_logr.png'      )
        #f.savefig(figure_path + 'Soft_D2_49_093_kappa_logr.png')
        #f.savefig(figure_path + 'E_kappa_logr.png'            )
        #f.savefig(figure_path + 'E_198_093_kappa_logr.png'      ) 

if Fig5_kappa_r_2:
    f      = plt.figure(figsize=(16,11))
    x_plot = np.log10(bin_radius_arr/r_2)
    y_plot = kappa_arr
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    plt.ylabel(r'$\kappa$',fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=4,mew=0,color='black',label=r'$\kappa$')
    #plt.ylim(-2.,.5)

    #plt.title(r'$\kappa$ and zero-line (%s)' %F,fontsize=30)
    plt.title(r'$\kappa$ (B IC with 20 radial bins)',fontsize=30)
    
    #f.savefig(figure_path + 'A_IC_kappa_r_2_logr.png'         )
    #f.savefig(figure_path + 'A_Final_kappa_r_2_logr.png'      )
    f.savefig(figure_path + 'B_IC_kappa_r_2_logr.png'         )
    #f.savefig(figure_path + 'B_Final_kappa_r_2_logr.png'      )
    #f.savefig(figure_path + 'Soft_B_IC_kappa_r_2_logr.png'    )
    #f.savefig(figure_path + 'Soft_B_Final_kappa_r_2_logr.png' )
    #f.savefig(figure_path + 'CS1_IC_kappa_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS4_IC_kappa_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS4_Final_kappa_r_2_logr.png'    )
    #f.savefig(figure_path + 'CS5_IC_kappa_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS5_Final_kappa_r_2_logr.png'    )
    #f.savefig(figure_path + 'CS6_IC_kappa_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS6_Final_kappa_r_2_logr.png'    )
    #f.savefig(figure_path + 'DS1_IC_kappa_r_2_logr.png'       )
    #f.savefig(figure_path + 'DS1_Final_kappa_r_2_logr.png'    )
    #f.savefig(figure_path + 'D2_kappa_r_2_logr.png'           )
    #f.savefig(figure_path + 'D2_Final_kappa_r_2_logr.png'     )
    #f.savefig(figure_path + 'Soft_D2_kappa_r_2_logr.png'      )
    #f.savefig(figure_path + 'Soft_D2_Final_kappa_r_2_logr.png')
    #f.savefig(figure_path + 'E_kappa_r_2_logr.png'            )
    #f.savefig(figure_path + 'E_Final_kappa_r_2_logr.png'      ) 

if Fig6_gamma:
    f      = plt.figure(figsize=(16,11))
    # f.set_size_inches(18.5, 10.5)
    x_plot = np.log10(bin_radius_arr)
    #x_plot = np.log10(bin_radius_arr)
    plt.ylim(-4.,1.5)    
    y_plot = gamma_arr
    plt.xlabel(r'$\log $r',fontsize=30)
    #plt.xlabel('r',fontsize=30)
    plt.ylabel(r'$\gamma$',fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black')
    #plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
    plt.plot((-.5,-.5),(-4.,4.), 'r-',label=r'inner cut')
    plt.plot((1.,1.),(-4.,4.), 'b-',label=r'outer cut')

    if Fig6_gammafit:
        x      = 10**x_plot
        y_plot = -1-3*x/(1+x)
        plt.plot(x_plot,y_plot,'-',ms=2,mew=0,color='blue',label=r'$-1-\frac{3r}{1+r}$')
        #plt.plot(x_plot[1:-2],y_plot[1:-2],'-',ms=2,mew=0,color='blue',label=r'$-1-\frac{3r}{1+r}$')
        '''
        Chi2 = 0
        i    = 0
        while (i < len(gamma_arr)):
            if isnan(gamma_arr[i]):
                print 'nan at index: ', i
            else:
                Chi2 = Chi2 + ((gamma_arr[i]-y_plot[i])**2)/(gamma_arr[i]*.2)**2               
            i = i+1
        Chi2 = (1.0/(len(gamma_arr)-1)) * Chi2
        print 'Chi2 for gammafit: ', Chi2
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',label = r'$\chi^2 = %.6f$' %Chi2)
        '''
        leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        #plt.title('Radial density slope with analytical expression (%s)' %F , fontsize=18)
        #plt.title('Radial density slope with analytical expression (B IC with 20 radial bins)',fontsize=30)
        #plt.title('Radial density slope with analytical expression (CS6 IC with 20 radial bins)',fontsize=30)
        #plt.title('Radial density slope with analytical expression (CS5 IC with 20 radial bins)',fontsize=30)
        #plt.title('Radial density slope with analytical expression (CS4 IC with 20 radial bins)',fontsize=30)
        
        #f.savefig(figure_path + 'A_IC_gamma_logr_fit.png'         )
        #f.savefig(figure_path + 'A_Final_gamma_logr_fit.png'      )
        #f.savefig(figure_path + 'B_IC_gamma_logr_fit.png'         )
        #f.savefig(figure_path + 'B_Final_gamma_logr_fit.png'      )
        #f.savefig(figure_path + 'Soft_B_IC_gamma_logr_fit.png'    )
        #f.savefig(figure_path + 'Soft_B_Final_gamma_logr_fit.png' )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr_fit.png'       )
        #f.savefig(figure_path + 'CS2_IC_gamma_logr_fit.png'       )
        #f.savefig(figure_path + 'CS3_IC_gamma_logr_fit.png'       ) 
        #f.savefig(figure_path + 'CS4_IC_gamma_logr_fit.png'       )
        #f.savefig(figure_path + 'CS4_Final_gamma_logr_fit.png'    )
        #f.savefig(figure_path + 'CS5_IC_gamma_logr_fit.png'       )
        #f.savefig(figure_path + 'CS5_Final_gamma_logr_fit.png'    )
        #f.savefig(figure_path + 'CS6_IC_gamma_logr_fit.png'       )
        #f.savefig(figure_path + 'CS6_Final_gamma_logr_fit.png'    )        
        #f.savefig(figure_path + 'DS1_IC_gamma_logr_fit.png'       )
        #f.savefig(figure_path + 'DS1_Final_gamma_logr_fit.png'    )
        #f.savefig(figure_path + 'D2_IC_gamma_logr_fit.png'        )
        #f.savefig(figure_path + 'D2_Final_gamma_logr_fit.png'     )
        #f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_fit.png'   )
        #f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_fit.png')
        #f.savefig(figure_path + 'E_IC_gamma_logr_fit.png'         )
        #f.savefig(figure_path + 'E_Final_gamma_logr_fit.png'      )
    else:
        #leg = plt.legend(prop=dict(size=30), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        #leg.get_frame().set_alpha(.5)
        
        #plt.title('Radial density slope (%s)' %F , fontsize=30)

        #plt.title('Radial density slope (A 48_009, $R_{limit}=10^4, 20$ bins)',fontsize=30      )
        #plt.title('Radial density slope (B 199_093, $R_{limit}=10^4, 20$ bins)',fontsize=30     )
        #plt.title('Radial density slope (CS4 Final, $R_{limit}=10^4, 20$ bins)',fontsize=30     )
        #plt.title('Radial density slope (CS5 Final, $R_{limit}=10^4, 20$ bins)',fontsize=30     )
        #plt.title('Radial density slope (CS6 Final, $R_{limit}=10^4, 20$ bins)',fontsize=30     )
        #plt.title('Radial density slope (DS1 IC, $R_{limit}=10^4, 20$ bins)',fontsize=30        )
        #plt.title('Radial density slope (DS1 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30    )
        #plt.title('Radial density slope (Soft_D2 IC, $R_{limit}=10^4, 20$ bins)',fontsize=30    )
        #plt.title('Radial density slope (Soft_D2 49_093, $R_{limit}=10^4, 20$ bins)',fontsize=30)
        #plt.title('Radial density slope (E IC, $R_{limit}=10^4, 20$ bins)',fontsize=30          ) 
        #plt.title('Radial density slope (E 198_093, $R_{limit}=10^4, 20$ bins)',fontsize=30     )

        #plt.title('Radial density slope (A IC, $R_{limit}=32, 50$ bins)',fontsize=30          )
        plt.title('Radial density slope (A 48_009, $R_{limit}=32, 50$ bins)',fontsize=30      )
        #plt.title('Radial density slope (B IC, $R_{limit}=32, 50$ bins)',fontsize=30          )
        #plt.title('Radial density slope (B 199_093, $R_{limit}=32, 50$ bins)',fontsize=30     )
        #plt.title('Radial density slope (CS4 IC, $R_{limit}=32, 20$ bins)',fontsize=30        )
        #plt.title('Radial density slope (CS4 48_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title('Radial density slope (CS5 IC, $R_{limit}=32, 20$ bins)',fontsize=30        )
        #plt.title('Radial density slope (CS5 48_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title('Radial density slope (CS6 IC, $R_{limit}=32, 20$ bins)',fontsize=30        )
        #plt.title('Radial density slope (CS6 48_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title('Radial density slope (DS1 IC, $R_{limit}=32, 20$ bins)',fontsize=30        )
        #plt.title('Radial density slope (DS1 49_093, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title('Radial density slope (Soft_D2 IC, $R_{limit}=32, 20$ bins)',fontsize=30    )
        #plt.title('Radial density slope (Soft_D2 49_093, $R_{limit}=32, 20$ bins)',fontsize=30)
        #plt.title('Radial density slope (E IC, $R_{limit}=32, 50$ bins)',fontsize=30          )
        #plt.title('Radial density slope (E 198_093, $R_{limit}=32, 50$ bins)',fontsize=30     )

        #f.savefig(figure_path + 'A_IC_gamma_logr_I_R32.png'          )
        #f.savefig(figure_path + 'A_48_009_gamma_logr_I_R32.png'      )
        #f.savefig(figure_path + 'A_48_009_gamma_logr_I_R32_cuts.png' )
        f.savefig(figure_path + 'A_48_009_gamma_r_I_R32.png'          )
        #f.savefig(figure_path + 'B_IC_gamma_logr_I_R32.png'          )
        #f.savefig(figure_path + 'B_199_093_gamma_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_B_IC_gamma_logr_I_R32.png'     )
        #f.savefig(figure_path + 'Soft_B_Final_gamma_logr_I_R32.png'  )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS2_IC_gamma_logr_I_R32.png'        ) 
        #f.savefig(figure_path + 'CS3_IC_gamma_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS4_IC_gamma_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS4_48_093_gamma_logr_I_R32.png'    )
        #f.savefig(figure_path + 'CS5_IC_gamma_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS5_48_093_gamma_logr_I_R32.png'    )
        #f.savefig(figure_path + 'CS6_IC_gamma_logr_I_R32.png'        )
        #f.savefig(figure_path + 'CS6_48_093_gamma_logr_I_R32.png'    )        
        #f.savefig(figure_path + 'DS1_IC_gamma_logr_I_R32.png'        )
        #f.savefig(figure_path + 'DS1_49_093_gamma_logr_I_R32.png'    )
        #f.savefig(figure_path + 'D2_IC_gamma_logr_I_R32.png'         )
        #f.savefig(figure_path + 'D2_Final_gamma_logr_I_R32.png'      )
        #f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_I_R32.png'    )
        #f.savefig(figure_path + 'Soft_D2_49_093_gamma_logr_I_R32.png')
        #f.savefig(figure_path + 'E_IC_gamma_logr_I_R32.png'          )
        #f.savefig(figure_path + 'E_198_093_gamma_logr_I_R32.png'     )

        #f.savefig(figure_path + 'A_IC_gamma_logr.png'          )
        #f.savefig(figure_path + 'A_48_009_gamma_logr.png'      )
        #f.savefig(figure_path + 'B_IC_gamma_logr.png'          )
        #f.savefig(figure_path + 'B_199_093_gamma_logr.png'     )
        #f.savefig(figure_path + 'Soft_B_IC_gamma_logr.png'     )
        #f.savefig(figure_path + 'Soft_B_Final_gamma_logr.png'  )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr.png'        )
        #f.savefig(figure_path + 'CS2_IC_gamma_logr.png'        )
        #f.savefig(figure_path + 'CS3_IC_gamma_logr.png'        )
        #f.savefig(figure_path + 'CS4_IC_gamma_logr.png'        )
        #f.savefig(figure_path + 'CS4_Final_gamma_logr.png'     )
        #f.savefig(figure_path + 'CS5_IC_gamma_logr.png'        )
        #f.savefig(figure_path + 'CS5_Final_gamma_logr.png'     )
        #f.savefig(figure_path + 'CS6_IC_gamma_logr.png'        )
        #f.savefig(figure_path + 'CS6_Final_gamma_logr.png'     )        
        #f.savefig(figure_path + 'DS1_IC_gamma_logr.png'        )
        #f.savefig(figure_path + 'DS1_49_093_gamma_logr.png'    )
        #f.savefig(figure_path + 'D2_IC_gamma_logr.png'         )
        #f.savefig(figure_path + 'D2_Final_gamma_logr.png'      )
        #f.savefig(figure_path + 'Soft_D2_IC_gamma_logr.png'    )
        #f.savefig(figure_path + 'Soft_D2_49_093_gamma_logr.png')
        #f.savefig(figure_path + 'E_IC_gamma_logr.png'          )
        #f.savefig(figure_path + 'E_198_093_gamma_logr.png'     )

if Fig6_gamma_r_2:
    f      = plt.figure(figsize=(16,11))
    x_plot = np.log10(bin_radius_arr/r_2)
    y_plot = gamma_arr
    plt.xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    plt.ylabel(r'$\gamma$',fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
    
    #plt.title('Radial density slope (%s)' %F , fontsize=30)
    #plt.title('Radial density slope  (B IC with 20 radial bins)',fontsize=30)
    #plt.title('Radial density slope (CS6 IC with 20 radial bins)',fontsize=30)
    #plt.title('Radial density slope (CS5 IC with 20 radial bins)',fontsize=30)
    #plt.title('Radial density slope (CS4 IC with 20 radial bins)',fontsize=30)
    plt.title('Radial density slope (CS4 Final with 20 radial bins)',fontsize=30)
    
    #f.savefig(figure_path + 'A_IC_gamma_r_2_logr.png'         )
    #f.savefig(figure_path + 'A_Final_gamma_r_2_logr.png'      )
    #f.savefig(figure_path + 'B_IC_gamma_r_2_logr.png'         )
    #f.savefig(figure_path + 'B_Final_gamma_r_2_logr.png'      )
    #f.savefig(figure_path + 'Soft_B_IC_gamma_r_2_logr.png'    )
    #f.savefig(figure_path + 'Soft_B_Final_gamma_r_2_logr.png' )
    #f.savefig(figure_path + 'CS1_IC_gamma_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS2_IC_gamma_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS3_IC_gamma_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS4_IC_gamma_r_2_logr.png'       )
    f.savefig(figure_path + 'CS4_Final_gamma_r_2_logr.png'    )
    #f.savefig(figure_path + 'CS5_IC_gamma_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS5_Final_gamma_r_2_logr.png'    )
    #f.savefig(figure_path + 'CS6_IC_gamma_r_2_logr.png'       )
    #f.savefig(figure_path + 'CS6_Final_gamma_r_2_logr.png'    )        
    #f.savefig(figure_path + 'DS1_IC_gamma_r_2_logr.png'       )
    #f.savefig(figure_path + 'DS1_Final_gamma_r_2_logr.png'    )
    #f.savefig(figure_path + 'D2_IC_gamma_r_2_logr.png'        )
    #f.savefig(figure_path + 'D2_Final_gamma_r_2_logr.png'     )
    #f.savefig(figure_path + 'Soft_D2_IC_gamma_r_2_logr.png'   )
    #f.savefig(figure_path + 'Soft_D2_Final_gamma_r_2_logr.png')
    #f.savefig(figure_path + 'E_IC_gamma_r_2_logr.png'         )
    #f.savefig(figure_path + 'E_Final_gamma_r_2_logr.png'      )

if Fig7_betagamma:
    f      = plt.figure()
    subplot(121)
    x_plot = beta_arr
    y_plot = gamma_arr
    plt.xlabel(r'$\beta$' , fontsize=30)
    plt.ylabel(r'$\gamma$' , fontsize=30)
    plt.title(r'$\gamma$ vs $\beta$ (%s)' %F , fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=2,mew=0,color='black')

    subplot(122)
    x_plot = beta_arr
    y_plot = kappa_arr
    plt.xlabel(r'$\beta$' , fontsize=30)
    plt.ylabel(r'$\kappa$' , fontsize=30)
    plt.title(r'$\kappa$ vs $\beta$' , fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=2,mew=0,color='black')

    #f.savefig(figure_path + 'A_betagamma.png'      )
    #f.savefig(figure_path + 'B_betagamma.png'      )
    #f.savefig(figure_path + 'Soft_B_betagamma.png' )
    #f.savefig(figure_path + 'CS1_betagamma.png'    )
    #f.savefig(figure_path + 'CS2_betagamma.png'    )
    #f.savefig(figure_path + 'CS3_betagamma.png'    )
    #f.savefig(figure_path + 'CS4_betagamma.png'    )
    #f.savefig(figure_path + 'CS5_betagamma.png'    )
    #f.savefig(figure_path + 'CS6_betagamma.png'    )
    #f.savefig(figure_path + 'DS1_betagamma.png'    )
    #f.savefig(figure_path + 'D2_betagamma.png'     )
    #f.savefig(figure_path + 'Soft_D2_betagamma.png')
    #f.savefig(figure_path + 'E_betagamma.png'      )



















if save_lnr_beta_gamma_kappa_VR_r_sigma_r_rr2_rho: # Save (logr, beta,gamma,kappa etc.) as text file, so they can be overplotted later.
    logr_arr                    = np.array(np.log10(bin_radius_arr))
    beta_arr                    = np.array(beta_arr)
    gamma_arr                   = np.array(gamma_arr)
    kappa_arr                   = np.array(kappa_arr)
    #VR_mean_arr                = np.concatenate(VR_arr,axis=0)
    r_arr                       = 10**(logr_arr)
    sigmarad2_arr               = np.array(sigmarad2_arr)
    rho_arr                     = np.array(rho_arr)
    GoodIDs                     = np.where(gamma_arr == gamma_arr)
    logr_arr                    = logr_arr[GoodIDs]
    gamma_arr                   = gamma_arr[GoodIDs]
    beta_arr                    = beta_arr[GoodIDs]
    kappa_arr                   = kappa_arr[GoodIDs]
    #VR_mean_arr                = VR_mean_arr[GoodIDs]
    r_arr                       = r_arr[GoodIDs]
    sigmarad2_arr               = sigmarad2_arr[GoodIDs]
    VR_i_average_inside_bin_arr = VR_i_average_inside_bin_arr[GoodIDs]

    if Gamma == -2.0:
        r_r2_arr                    = r_arr/r_2
        #print 'r_r2_arr = ', r_r2_arr
        #IPython.embed()
        #r_r2_arr                    = r_r2_arr[GoodIDs]
        print 'r_r2_arr = ', r_r2_arr
        rho_arr                     = rho_arr[GoodIDs]
        x        = np.array((logr_arr,beta_arr,gamma_arr,kappa_arr,VR_i_average_inside_bin_arr,r_arr,sigmarad2_arr,r_r2_arr,rho_arr))
        x        = x.transpose()
        #np.savetxt(Filename.strip('.hdf5')+'.txt', x, delimiter = ' ')
        #np.savetxt(F +'.txt', x, delimiter = ' ')
        out_name = text_files_path + F +'.txt'
        np.savetxt(out_name,x,delimiter=' ',header='          logr                   beta                      gamma                  kappa                  VR_average                  r                  sigmarad2                  r_r2                   rho')
    else:
        x        = np.array((logr_arr,beta_arr,gamma_arr,kappa_arr,VR_i_average_inside_bin_arr,r_arr,sigmarad2_arr))
        x        = x.transpose()
        out_name = text_files_path + F +'.txt'
        np.savetxt(out_name,x,delimiter=' ',header='          logr                   beta                      gamma                  kappa                  VR_average                  r                  sigmarad2 ')


















if save_particle_tracking_ASCII:    
    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # A,B IC
    #            [100 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]

    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # A,B 5_005
    #            [600 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]
                
    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # A,B 10_005
    #            [1100 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]

    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # A 40_005
    #            [4100 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]

    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # A 48_009
    #            [4970 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]

    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # B 198_000
    #            [19800 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]

    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # B 198_093
    #            [22100 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]

    #xx       = [['TimeMax','x[100000]','y[100000]','z[100000]','R_xyz[100000]','x[200000]','y[200000]','z[200000]','R_xyz[200000]','x[300000]','y[300000]','z[300000]','R_xyz[300000]','x[400000]','y[400000]','z[400000]','R_xyz[400000]'], # B 199_093
    #            [24400 , x[100000] , y[100000] , z[100000] , R_xyz[100000] , x[200000] , y[200000] , z[200000] , R_xyz[200000] , x[300000] , y[300000] , z[300000] , R_xyz[300000] , x[400000] , y[400000] , z[400000] , R_xyz[400000]]]

    #out_name = text_files_path + 'A_particle_tracking_IC_ASCII.txt'
    #out_name = text_files_path + 'A_particle_tracking_5_005_ASCII.txt'
    #out_name = text_files_path + 'A_particle_tracking_10_005_ASCII.txt'
    #out_name = text_files_path + 'A_particle_tracking_40_005_ASCII.txt'
    #out_name = text_files_path + 'A_particle_tracking_48_009_ASCII.txt'

    #out_name = text_files_path + 'B_particle_tracking_IC_ASCII.txt'
    #out_name = text_files_path + 'B_particle_tracking_5_005_ASCII.txt'
    #out_name = text_files_path + 'B_particle_tracking_10_005_ASCII.txt'
    #out_name = text_files_path + 'B_particle_tracking_198_000_ASCII.txt'
    #out_name = text_files_path + 'B_particle_tracking_198_093_ASCII.txt'
    #out_name = text_files_path + 'B_particle_tracking_199_093_ASCII.txt'
      
    f = open(out_name,'w')
    for i in range(len(xx)):
        if i == 0:
            #f.write('# TimeMax \t x[100] \t y[100] \t z[100] \t R_xyz[100] \t x[200] \t y[200] \t z[200] \t R_xyz[200] \n')
            k=''
            for j in range(len(xx[0])):
                k += k+''
            f.write('# %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \n'    % (xx[i][0],xx[i][1],xx[i][2],xx[i][3],xx[i][4],xx[i][5],xx[i][6],xx[i][7],xx[i][8],xx[i][9],xx[i][10],xx[i][11],xx[i][12],xx[i][13],xx[i][14],xx[i][15],xx[i][16]))
        else:
            f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n' % (xx[i][0],xx[i][1],xx[i][2],xx[i][3],xx[i][4],xx[i][5],xx[i][6],xx[i][7],xx[i][8],xx[i][9],xx[i][10],xx[i][11],xx[i][12],xx[i][13],xx[i][14],xx[i][15],xx[i][16]))
    f.close()

if save_combine_ASCII:
    A = 0
    B = 0
    if A:
        lf          = [text_files_path + 'A_particle_tracking_IC_ASCII.txt',text_files_path + 'A_particle_tracking_5_005_ASCII.txt',text_files_path + 'A_particle_tracking_10_005_ASCII.txt',
                       text_files_path + 'A_particle_tracking_40_005_ASCII.txt',text_files_path + 'A_particle_tracking_48_009_ASCII.txt']
        dl_lf       = [ pylab.loadtxt(filename) for filename in lf]
        out_name    = text_files_path + 'A_particle_tracking.txt'
        f           = open(out_name,'w')
        for i in range(len(dl_lf)):
            if i == 0:
                f.write('# TimeMax \t x[100000] \t y[100000] \t z[100000] \t R_xyz[100000] \t x[200000] \t y[200000] \t z[200000] \t R_xyz[200000] \t x[300000] \t y[300000] \t z[300000] \t R_xyz[300000] \t x[400000] \t y[400000] \t z[400000] \t R_xyz[400000] \n')
                k=''
                for j in range(len(dl_lf[0])):
                    k += k+''
                #f.write('%s \t \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8]))
                f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8],dl_lf[i][9],dl_lf[i][10],dl_lf[i][11],dl_lf[i][12],dl_lf[i][13],dl_lf[i][14],dl_lf[i][15],dl_lf[i][16]))
                #f.write('# %s \t %i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8]))
            else:
                f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f  \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8],dl_lf[i][9],dl_lf[i][10],dl_lf[i][11],dl_lf[i][12],dl_lf[i][13],dl_lf[i][14],dl_lf[i][15],dl_lf[i][16]))
        f.close()
    elif B:
        lf          = [text_files_path + 'B_particle_tracking_IC_ASCII.txt',text_files_path + 'B_particle_tracking_5_005_ASCII.txt',text_files_path + 'B_particle_tracking_10_005_ASCII.txt',
                       text_files_path + 'B_particle_tracking_198_000_ASCII.txt',text_files_path + 'B_particle_tracking_198_093_ASCII.txt',text_files_path + 'B_particle_tracking_199_093_ASCII.txt']
        dl_lf       = [ pylab.loadtxt(filename) for filename in lf]
        out_name    = text_files_path + 'B_particle_tracking.txt'
        f           = open(out_name,'w')
        for i in range(len(dl_lf)):
            if i == 0:
                f.write('# TimeMax \t x[100000] \t y[100000] \t z[100000] \t R_xyz[100000] \t x[200000] \t y[200000] \t z[200000] \t R_xyz[200000] \t x[300000] \t y[300000] \t z[300000] \t R_xyz[300000] \t x[400000] \t y[400000] \t z[400000] \t R_xyz[400000] \n')
                k=''
                for j in range(len(dl_lf[0])):
                    k += k+''
                #f.write('%s \t \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8]))
                f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8],dl_lf[i][9],dl_lf[i][10],dl_lf[i][11],dl_lf[i][12],dl_lf[i][13],dl_lf[i][14],dl_lf[i][15],dl_lf[i][16]))
                #f.write('# %s \t %i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8]))
            else:
                f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f  \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n' % (dl_lf[i][0],dl_lf[i][1],dl_lf[i][2],dl_lf[i][3],dl_lf[i][4],dl_lf[i][5],dl_lf[i][6],dl_lf[i][7],dl_lf[i][8],dl_lf[i][9],dl_lf[i][10],dl_lf[i][11],dl_lf[i][12],dl_lf[i][13],dl_lf[i][14],dl_lf[i][15],dl_lf[i][16]))
        f.close()

if Fig_combine_ASCII:
    #read_txt = pylab.loadtxt(text_files_path + 'A_particle_tracking.txt')
    read_txt  = pylab.loadtxt(text_files_path + 'B_particle_tracking.txt')
    Colors    = ['red', 'blue','black','brown','yellow','green']*3
    Symbols   = ['-o','-s','-<','--v','--*','--s','--d','--.'  ]*3
    f, (ax1)  = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    ax1.plot(read_txt[:,0],read_txt[:,4] ,Symbols[0],color=Colors[0],label='Particle 100000',lw=2,ms=7)
    ax1.plot(read_txt[:,0],read_txt[:,8] ,Symbols[1],color=Colors[1],label='Particle 200000',lw=2,ms=7)
    ax1.plot(read_txt[:,0],read_txt[:,12],Symbols[2],color=Colors[2],label='Particle 300000',lw=2,ms=7)
    ax1.plot(read_txt[:,0],read_txt[:,16],Symbols[3],color=Colors[3],label='Particle 400000',lw=2,ms=7)
    ax1.set_ylabel(r'Radius',fontsize=30)
    ax1.set_xlabel(r'Simulation time',fontsize=30)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    #ax1.set_xlim(-.3,1.1)
    #ax1.set_ylim(-6.,0.)
    
    #ax1.set_title(r'A (I: $\Delta $G)',fontsize=30)
    ax1.set_title(r'B (I: $\Delta $G)',fontsize=30)    
    #f.savefig(figure_path + 'Fig_combine_ASCII_A.png')    
    f.savefig(figure_path + 'Fig_combine_ASCII_B.png')    

if save_sigma: 
    x = np.array((sigma2_arr , sigmarad2_arr, sigmatheta2_arr, sigmaphi2_arr))
    x = x.transpose()
    np.savetxt(Filename.strip('.hdf5')+'_sigma.txt', x, delimiter = ' ', header='  sigma2_arr       sigmarad2_arr       sigmatheta2_arr       sigmaphi2_arr   ')

if Scatterplot_vr_logr: # Radial velocity
    r     = (x**2 + y**2 + z**2)**.5
    Phi   = sp.arctan2(y,x)
    Theta = sp.arccos(z/r)
    VR    = sp.sin(Theta)*sp.cos(Phi) * vx + sp.sin(Theta)*sp.sin(Phi) * vy + sp.cos(Theta) * vz
    f     = plt.figure()
    plt.plot(np.log10(r), VR,'o', color = 'Blue',lw=2,ms=1 )
    plt.title(r' %s' %F, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=20)
    plt.ylabel(r'$v_r$',fontsize=24)
    #plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=4,handlelength=2.5)
    plt.grid()
    f.savefig(figure_path + 'Scatterplot_vr_logr.png')

if Scatterplot_vr_r: # Radial velocity
    r     = (x**2+y**2+z**2)**.5
    Phi   = sp.arctan2(y,x)
    Theta = sp.arccos(z/r)
    VR    = sp.sin(Theta)*sp.cos(Phi)*vx+sp.sin(Theta)*sp.sin(Phi)*vy+sp.cos(Theta)*vz
    f     = plt.figure()
    plt.plot(r, VR,'o', color = 'Blue',lw=2,ms=1 )
    plt.title(r' %s' %F, fontsize=20)
    plt.xlabel(r'$ r$', fontsize=20)
    plt.ylabel(r'$v_r$',fontsize=24)
    #plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=4,handlelength=2.5)
    plt.grid()
    f.savefig(figure_path + 'Scatterplot_vr_r.png')    

if Scatterplot_V_logr: # Gravitational potential
    r = (x**2 + y**2 + z**2)**.5
    f = plt.figure()
    plt.plot(np.log10(r), V,'o', color = 'Blue',lw=2,ms=1 )
    plt.title(r' %s' %F, fontsize=20)
    plt.xlabel(r'$\log r$', fontsize=20)
    plt.ylabel(r'Gravitational potential, $\Phi$',fontsize=24)
    #plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=4,handlelength=2.5)
    plt.grid()
    f.savefig(figure_path + 'Scatterplot_V_logr.png')    

if V_vr_r_logr_panel:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(17,8))
    f.subplots_adjust(hspace=0,wspace=0)

    r     = (x**2 + y**2 + z**2)**.5
    Phi   = sp.arctan2(y,x)
    Theta = sp.arccos(z/r)
    VR    = sp.sin(Theta)*sp.cos(Phi) * vx + sp.sin(Theta)*sp.sin(Phi) * vy + sp.cos(Theta) * vz

    ax1.plot(r, VR,'o', color = 'Blue',lw=2,ms=1 )
    a = F[:-14]
    ax1.set_title(r'$v_r$', fontsize=20)
    ax1.set_xlabel(r'$ r$', fontsize=20)
    
    ax2.plot(np.log10(r), VR,'o', color = 'Blue',lw=2,ms=1 )
    ax2.set_title(r' %s ' %a, fontsize=20)
    ax2.set_xlabel(r'$\log r$', fontsize=20)
    ax2.axes.get_yaxis().set_visible(False)

    ax3.plot(np.log10(r), V,'o', color = 'Blue',lw=2,ms=1 )
    ax3.set_title(r'Potential', fontsize=20)
    ax3.set_xlabel(r'$\log r$', fontsize=20)
    #ax3.set_ylabel(r'$\Phi$',fontsize=24)
    ax3.yaxis.tick_right()

    if F.startswith('B_Hernquist10000_G1.0_199_093'):
        #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/B_final_vr_V_panel.png')
        f.savefig(figure_path + 'B_final_vr_V_panel.png') 
    elif F.startswith('B_bound_particles_G1.0_200_rfp_093'):
        #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/B_rfp_vr_V_panel.png')
        f.savefig(figure_path + 'B_rfp_vr_V_panel.png') 

    elif F.startswith('CS4_Osipkov_Merritt10000_G1.0_48_093'):
        #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/CS4_final_vr_V_panel.png')
        f.savefig(figure_path + 'CS4_final_V_vr_r_logr_panel.png')

    elif F.startswith('CS5_Osipkov_Merritt10000_G1.0_48_093'):
        #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/CS5_final_vr_V_panel.png')
        f.savefig(figure_path + 'CS5_final_V_vr_r_logr_panel.png')

    elif F.startswith('CS6_Osipkov_Merritt10000_G1.0_48_093'):
        #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/CS6_final_vr_V_panel.png')
        f.savefig(figure_path + 'CS6_final_V_vr_r_logr_panel.png')
 
    elif F.startswith('DS1_Osipkov_Merritt10000_G1.0_48_093'):
        #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/DS1_final_vr_V_panel.png')
        f.savefig(figure_path + 'DS1_final_V_vr_r_logr_panel.png')
 


plt.show()







































































