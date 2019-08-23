# -*- coding: utf-8 -*-

import h5py
import numpy as     np
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
from pylab import *
from scipy.stats import norm
from scipy.optimize import curve_fit
import scipy as sp
import seaborn as sns
import matplotlib.patches as mpatches
from pathlib import Path

User_path = Path.cwd()
Desktop_path = User_path + 'Desktop/'
# GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IIa/'
# GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IIb/'
GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IIc/'
# GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IId/'
Stable_path = 'Energy_exchange/Stable_structures/'
# figure_path = Desktop_path + Stable_path + 'figures/IIa/'
# figure_path = Desktop_path + Stable_path + 'figures/IIb/'
figure_path = Desktop_path + Stable_path + 'figures/IIc/'
# figure_path = Desktop_path + Stable_path + 'figures/IId/'

# IIa
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/Soft_B/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/CS1/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/CS4/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/CS5/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/CS6/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/DS1/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/Soft_D2/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/E/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/Test_CS4/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/Test_D2/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIa/Test_CS4_10tdyn/'

# IIb
# text_files_path = Desktop_path + Stable_path + 'text_files/IIb/CS4/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIb/Soft_D2/'

# IIc
# text_files_path = Desktop_path + Stable_path + 'text_files/IIc/CS4/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIc/CS5/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIc/CS6/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IIc/DS1/'
text_files_path = Desktop_path + Stable_path + 'text_files/IIc/Soft_D2/'

# IId
# text_files_path = Desktop_path + Stable_path + 'text_files/IId/CS4/'
# text_files_path = Desktop_path + Stable_path + 'text_files/IId/Soft_D2/'

Soft_B_path = 'E_HQ_1000000_B/output/'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_1_000.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_20_005.hdf5'
CS1_path = 'E_HQ_10000_CS1/output/'
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_20_005.hdf5'

CS4_path = 'E_HQ_100000_CS4/output/' 
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_20_013.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_20_021.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_30_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_40_021.hdf5'
CS5_path = 'E_HQ_100000_CS5/output/'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_20_021.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_30_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_40_021.hdf5'
CS6_path = 'E_HQ_100000_CS6/output/'  
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_20_021.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_30_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_40_021.hdf5'
DS1_path = 'E_0_5_100000_DS1/output/'  
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_20_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_30_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_40_021.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_60_021.hdf5'

Soft_D2_path = 'E_0_5_100000_D2/output/'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_20_013.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_20_021.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_30_021.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_40_021.hdf5'
Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_60_021.hdf5'

E_path = 'E_HQ_1000000_E/output/'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_20_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_30_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_40_021.hdf5'

Test_CS4_path = 'Test_CS4/output/'
# Filename = GADGET_E_path + Test_CS4_path      + 'B_E_G2P_0_005.hdf5'
# Filename       = GADGET_E_path + 'Test_CS4/'        + 'B_E_0_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_CS4_path      + 'B_E_G2P_1_005.hdf5'
# Filename       = GADGET_E_path + 'Test_CS4/'        + 'B_E_1_005_P2G.hdf5'

# Filename       = GADGET_E_path + Test_CS4_path      + 'B_E_G2P_2_005.hdf5'
# Filename       = GADGET_E_path + 'Test_CS4/'        + 'B_E_2_005_P2G.hdf5'

# Filename       = GADGET_E_path + Test_CS4_path      + 'B_E_G2P_3_005.hdf5'
# Filename       = GADGET_E_path + 'Test_CS4/'        + 'B_E_3_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_CS4_path      + 'B_E_G2P_4_005.hdf5'
# Filename       = GADGET_E_path + 'Test_CS4/'        + 'B_E_4_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_CS4_path      + 'B_E_G2P_5_005.hdf5'
# Filename       = GADGET_E_path + 'Test_CS4/'        + 'B_E_5_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_CS4_path      + 'B_E_G2P_6_005.hdf5'

Test_D2_path   = 'Test_D2/output/'
# Filename       = GADGET_E_path + Test_D2_path      + 'B_E_G2P_0_005.hdf5'
# Filename       = GADGET_E_path + 'Test_D2/'        + 'B_E_0_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_D2_path      + 'B_E_G2P_1_005.hdf5'
# Filename       = GADGET_E_path + 'Test_D2/'        + 'B_E_1_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_D2_path      + 'B_E_G2P_2_005.hdf5'
# Filename       = GADGET_E_path + 'Test_D2/'        + 'B_E_2_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_D2_path      + 'B_E_G2P_3_005.hdf5'
# Filename       = GADGET_E_path + 'Test_D2/'        + 'B_E_3_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_D2_path      + 'B_E_G2P_4_005.hdf5'
# Filename       = GADGET_E_path + 'Test_D2/'        + 'B_E_4_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_D2_path      + 'B_E_G2P_5_005.hdf5'
# Filename       = GADGET_E_path + 'Test_D2/'        + 'B_E_5_005_P2G.hdf5'
# Filename       = GADGET_E_path + Test_D2_path      + 'B_E_G2P_6_005.hdf5'

Test_CS4_10tdyn_path   = 'Test_CS4_10tdyn/output/'
# Filename       = GADGET_E_path + Test_CS4_10tdyn_path      + 'B_E_G2P_0_005.hdf5'
# Filename       = GADGET_E_path + Test_CS4_10tdyn_path      + 'B_E_G2P_1_041.hdf5'
# Filename       = GADGET_E_path + Test_CS4_10tdyn_path      + 'B_E_G2P_2_041.hdf5'
# Filename       = GADGET_E_path + Test_CS4_10tdyn_path      + 'B_E_G2P_3_041.hdf5'

# Control
con_Soft_B_path  = 'E_HQ_1000000_B_control/output/'
# Filename        = GADGET_E_path + con_Soft_B_path    + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_Soft_B_path    + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_Soft_B_path    + 'B_E_10_005.hdf5'
# Filename        = GADGET_E_path + con_Soft_B_path    + 'B_E_20_005.hdf5'
con_CS1_path     = 'E_HQ_10000_CS1_control/output/'
# Filename        = GADGET_E_path + con_CS1_path       + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_CS1_path       + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_CS1_path       + 'B_E_20_005.hdf5'
con_CS4_path     = 'E_HQ_100000_CS4_control/output/'
# Filename        = GADGET_E_path + con_CS4_path       + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_CS4_path       + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_CS4_path       + 'B_E_20_005.hdf5'
con_CS5_path     = 'E_HQ_100000_CS5_control/output/'
# Filename        = GADGET_E_path + con_CS5_path       + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_CS5_path       + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_CS5_path       + 'B_E_20_005.hdf5'
con_CS6_path     = 'E_HQ_100000_CS6_control/output/'
# Filename        = GADGET_E_path + con_CS6_path       + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_CS6_path       + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_CS6_path       + 'B_E_20_005.hdf5'
con_DS1_path     = 'E_0_5_100000_DS1_control/output/'
# Filename        = GADGET_E_path + con_DS1_path       + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_DS1_path       + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_DS1_path       + 'B_E_20_005.hdf5'
con_Soft_D2_path = 'E_0_5_100000_D2_control/output/'
# Filename        = GADGET_E_path + con_Soft_D2_path   + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_Soft_D2_path   + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_Soft_D2_path   + 'B_E_20_005.hdf5'
con_E_path       = 'E_HQ_1000000_E_control/output/'
# Filename        = GADGET_E_path + con_E_path         + 'B_E_0_000.hdf5'
# Filename        = GADGET_E_path + con_E_path         + 'B_E_0_001.hdf5'
# Filename        = GADGET_E_path + con_E_path         + 'B_E_20_005.hdf5'

SnapshotFile = h5py.File(Filename, 'r')

# IIa
# F               = 'Soft_B'   + Filename[len(GADGET_E_path + Soft_B_path + 'B'):-5     ]
# F               = 'Soft_B'   + Filename[len(GADGET_E_path + con_Soft_B_path + 'B'):-5 ] 
# F               = 'CS1'      + Filename[len(GADGET_E_path + CS1_path + 'B'):-5        ]
# F               = 'CS1'      + Filename[len(GADGET_E_path + con_CS1_path + 'B'):-5    ]
# F               = 'CS4'      + Filename[len(GADGET_E_path + CS4_path + 'B'):-5        ]
# F               = 'CS4'      + Filename[len(GADGET_E_path + con_CS4_path + 'B'):-5    ]
# F               = 'CS5'      + Filename[len(GADGET_E_path + CS5_path + 'B'):-5        ]
# F               = 'CS5'      + Filename[len(GADGET_E_path + con_CS5_path + 'B'):-5    ]
# F               = 'CS6'      + Filename[len(GADGET_E_path + CS6_path + 'B'):-5        ]
# F               = 'CS6'      + Filename[len(GADGET_E_path + con_CS6_path + 'B'):-5    ]
# F               = 'DS1'      + Filename[len(GADGET_E_path + DS1_path + 'B'):-5        ]
# F               = 'DS1'      + Filename[len(GADGET_E_path + con_DS1_path + 'B'):-5    ]
# F               = 'Soft_D2'  + Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5    ]
# F               = 'Soft_D2'  + Filename[len(GADGET_E_path + con_Soft_D2_path + 'B'):-5]
# F               = 'E'        + Filename[len(GADGET_E_path + E_path + 'B'):-5          ]
# F               = 'E'        + Filename[len(GADGET_E_path + con_E_path + 'B'):-5      ]
# F               = 'Test_CS4' + Filename[len(GADGET_E_path + Test_CS4_path + 'B'):-5   ]
# F               = 'Test_CS4' + Filename[len(GADGET_E_path + 'Test_CS4/' + 'B'):-5      ]
# F               = 'Test_D2'  + Filename[len(GADGET_E_path + Test_D2_path + 'B'):-5    ]
# F               = 'Test_D2'  + Filename[len(GADGET_E_path + 'Test_D2/' + 'B'):-5      ]
# F               = 'Test_CS4_10tdyn' + Filename[len(GADGET_E_path + Test_CS4_10tdyn_path + 'B'):-5   ]

# IIb
# F               = 'IIb_CS4'      + Filename[len(GADGET_E_path + CS4_path + 'B'):-5          ]
# F               = 'IIb_Soft_D2'  + Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5      ]

# IIc
# F               = 'IIc_CS4'            + Filename[len(GADGET_E_path + CS4_path + 'B'):-5          ]
# F               = 'IIc_CS4_no_K_ratio' + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F               = 'IIc_CS4_unbound'    + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F               = 'IIc_CS4_no_rand'    + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F               = 'IIc_CS4_car_sph_car' + Filename[len(GADGET_E_path + 'E_HQ_100000_CS4/' + 'B'):-5]
# F               = 'IIc_Test_CS4' + Filename[len(GADGET_E_path + 'Test_CS4_path/' + 'B'):-5  ]
# F               = 'IIc_Test_CS4' + Filename[len(GADGET_E_path + 'Test_CS4/' + 'B'):-5       ]
# F               = 'IIc_CS5' + Filename[len(GADGET_E_path + CS5_path + 'B'):-5     ]
# F               = 'IIc_CS6' + Filename[len(GADGET_E_path + CS6_path + 'B'):-5     ]
# F               = 'IIc_DS1'  + Filename[len(GADGET_E_path + DS1_path + 'B'):-5     ]
F = 'IIc_Soft_D2'  + Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5      ]
# F               = 'IIc_Soft_D2'  + Filename[len(GADGET_E_path + 'E_0_5_100000_D2/' + 'B'):-5]

# IId
# F = 'IId_CS4' + Filename[len(GADGET_E_path + CS4_path + 'B'):-5]
# F = 'IId_Soft_D2'+ Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5]

Gamma = -2.0
Beta = 1.0

keep_IC_R_middle = 0
new_R_middle = 0
R_bin_automatic = 0

bins_202 = 0
bins_102 = 0
bins_52 = 0
bins_22 = 0  # Reduce number of radial bins in analysis code. This makes them larger and they therefore contain more particles.

R_limit_10000 = 0  # Analyse larger volume of structure, sets R_limit to 10000.
R_limit_5000 = 0  # Analyse large volume of structure, sets R_limit to 5000.
R_limit_50 = 0
R_limit_32 = 0

Fig_vx_x = 0
Fig_v_logr = 0
Fig_x_hist = 0
Fig_x_hist2d = 0
Fig4_beta = 0
Fig4_betafit = 0
Fig5_kappa = 0
Fig6_gamma = 0
Fig6_gammafit = 0
Fig7_betagamma = 0
save_lnr_beta_gamma_kappa_VR_r_sigma_r_r2_rho = 0

if keep_IC_R_middle: # For R_limit_10000, 20 bins.
    if F.startswith('Hernquist10000_G'):
        if   Gamma == -1.5:      
                R_middle = 0
        elif Gamma == -2.0:     
                R_middle = 0
        elif Gamma == -2.5:                   
                R_middle = 0
        elif Gamma == -3.0: 
                R_middle = 0
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
    # Soft_B
    if F == 'Soft_B_E_G2P_0_000': 
        if   Gamma == -1.5:     
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                    
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    if F == 'Soft_B_E_G2P_20_005': 
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**.2
        elif Gamma == -2.5:                 
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    # con_Soft_B
    if F == 'Soft_B_E_0_000': 
        if   Gamma == -1.5:     
            R_middle = 10**-.7
        elif Gamma == -2.0:     
            R_middle = 10**-.35
        elif Gamma == -2.5:                    
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.3
    if F == 'Soft_B_E_0_001': 
        if   Gamma == -1.5:       
            R_middle = 10**-.7
        elif Gamma == -2.0:     
            R_middle = 10**-.35
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.3
    if F == 'Soft_B_E_20_005': 
        if   Gamma == -1.5:       
            R_middle = 10**-.6
        elif Gamma == -2.0:     
            R_middle = 10**-.35
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.3              
    # CS1
    if F == 'CS1_E_G2P_0_000':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:      
            R_middle = 1
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    # CS4
    if F == 'CS4_E_G2P_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.65
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.3
    if F == 'CS4_E_G2P_2_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.52
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                 
            R_middle = 10**.05
        elif Gamma == -3.0:     
            R_middle = 10**.3
    if F == 'CS4_E_G2P_4_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.52
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                 
            R_middle = 10**.05
        elif Gamma == -3.0:     
            R_middle = 10**.27
    if F == 'CS4_E_G2P_6_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.48
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.27
    if F == 'CS4_E_G2P_8_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                 
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    if F == 'CS4_E_G2P_10_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                 
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    if F == 'CS4_E_G2P_20_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.45
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                 
            R_middle = 10**-.05
        elif Gamma == -3.0:     
            R_middle = 10**.25
    if F == 'IIc_CS4_E_G2P_40_021':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                 
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1

            
    # con_CS4 Final
    if F == 'CS4_E_20_005': 
        if   Gamma == -1.5:       
            R_middle = 10**-.4
        elif Gamma == -2.0:     
            R_middle = 10**-.23
        elif Gamma == -2.5:                 
            R_middle = 10**-.05
        elif Gamma == -3.0:     
            R_middle = 10**.25
    # CS5
    if F == 'CS5_E_G2P_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.7
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 10**.38
    if F == 'CS5_E_G2P_2_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.6
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 10**-.1
        elif Gamma == -3.0:    
            R_middle = 10**.3
    if F == 'CS5_E_G2P_4_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.55
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 10**.35
    if F == 'CS5_E_G2P_6_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.48
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 10**.3
    if F == 'CS5_E_G2P_8_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'CS5_E_G2P_10_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'CS5_E_G2P_20_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.42
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                   
            R_middle = 10**-.05
        elif Gamma == -3.0:    
            R_middle = 10**-.28
    if F == 'CS5_E_G2P_30_005':
        if   Gamma == -1.5:       
            R_middle = 1.
        elif Gamma == -2.0:     
            R_middle = 10**-.35
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 1.


    if F == 'IIc_CS5_E_G2P_40_021':
        if   Gamma == -1.5:       
            R_middle = 1.
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 1. 



            
    # con_CS5 final
    if F == 'CS5_E_20_005': 
        if   Gamma == -1.5:       
            R_middle = 10**-.45
        elif Gamma == -2.0:     
            R_middle = 10**-.23
        elif Gamma == -2.5:                 
            R_middle = 10**-.04
        elif Gamma == -3.0:     
            R_middle = 10**.3
    # CS6
    if F == 'CS6_E_G2P_0_000':
        if   Gamma == -1.5:       
            R_middle = 10**-.73
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 10**.34
    if F == 'CS6_E_G2P_2_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.55
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 10**.35
    if F == 'CS6_E_G2P_4_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.5
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 10**-.05
        elif Gamma == -3.0:    
            R_middle = 10**.32
    if F == 'CS6_E_G2P_6_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.5
        elif Gamma == -2.0:     
            R_middle = 10**-.3
        elif Gamma == -2.5:                   
            R_middle = 10**-.05
        elif Gamma == -3.0:    
            R_middle = 10**.35
    if F == 'CS6_E_G2P_8_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'CS6_E_G2P_10_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'CS6_E_G2P_20_005':
        if   Gamma == -1.5:       
            R_middle = 10**-.45
        elif Gamma == -2.0:     
            R_middle = 10**-.25
        elif Gamma == -2.5:                   
            R_middle = 10**-.08
        elif Gamma == -3.0:    
            R_middle = 10**.28
    if F == 'CS6_E_G2P_30_005':
        if   Gamma == -1.5:       
            R_middle = 1.
        elif Gamma == -2.0:     
            R_middle = 10**-.35
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 1.

    if F == 'IIc_CS6_E_G2P_40_021':
        if   Gamma == -1.5:       
            R_middle = 1.
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                   
            R_middle = 1.
        elif Gamma == -3.0:    
            R_middle = 1.
            
    # con_CS6 final
    if F == 'CS6_E_20_005': 
        if   Gamma == -1.5:       
            R_middle = 10**-.42
        elif Gamma == -2.0:     
            R_middle = 10**-.23
        elif Gamma == -2.5:                 
            R_middle = 1.
        elif Gamma == -3.0:     
            R_middle = 10**.3
    # DS1
    if F == 'DS1_E_G2P_0_000':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'DS1_E_G2P_20_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'DS1_E_G2P_40_021':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.35
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1

    if F == 'IIc_DS1_E_G2P_60_021':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
            
    # con_DS1
    if F == 'DS1_E_20_005': 
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.18
        elif Gamma == -2.5:                 
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    # Soft_D2
    if F == 'Soft_D2_E_G2P_0_000':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'Soft_D2_E_G2P_20_005':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'Soft_D2_E_G2P_40_021':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.4
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1

    if F == 'IIc_Soft_D2_E_G2P_60_021':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1

    # Soft_D2 IId
    if F == 'IId_Soft_D2_E_G2P_0_000':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.2
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
    if F == 'IId_Soft_D2_E_G2P_20_013':
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.45
        elif Gamma == -2.5:                   
            R_middle = 1
        elif Gamma == -3.0:    
            R_middle = 1
            
    # con_D2
    if F == 'Soft_D2_E_20_005': 
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 10**-.18
        elif Gamma == -2.5:                 
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
            
    # E
    if F == 'E_E_G2P_0_000':
        if   Gamma == -1.5:     
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    if F == 'E_E_G2P_20_005':
        if   Gamma == -1.5:     
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
    # E
    if F == 'E_E_20_005': 
        if   Gamma == -1.5:       
            R_middle = 1
        elif Gamma == -2.0:     
            R_middle = 1
        elif Gamma == -2.5:                 
            R_middle = 1
        elif Gamma == -3.0:     
            R_middle = 1
        
Pos   = SnapshotFile['PartType1/Coordinates'].value 
Vel   = SnapshotFile['PartType1/Velocities'].value  
V     = SnapshotFile['PartType1/Potential'].value     
x     = Pos[:,0]
y     = Pos[:,1]
z     = Pos[:,2]
vx    = Vel[:,0]
vy    = Vel[:,1]
vz    = Vel[:,2]
minV  = np.argmin(V)  # Finds the particle with the lowest potential (which is in the center of the largest cluster)
xC    = x[minV]       # Changes x, y and z so that the cluster is centered.
yC    = y[minV]
zC    = z[minV]
vxC   = vx[minV]
vyC   = vy[minV]
vzC   = vz[minV]
#xC   = np.median(x[V.argsort()[0:100]]) # Changes x, y and z so that the cluster is centered.
#yC   = np.median(y[V.argsort()[0:100]])
#zC   = np.median(z[V.argsort()[0:100]])

#R     = ((x-xC)**2+(y-yC)**2+(z-zC)**2)**.5
#R     = (x**2+y**2+z**2)**.5

if R_limit_10000:
    R_limit = 10000.
    F       = F + '_R_limit_10000'
elif R_limit_5000:
    R_limit = 5000.
    F       = F + '_R_limit_5000'
elif R_limit_50:
    R_limit = 50.
    F       = F + '_R_limit_50'
elif R_limit_32:
    R_limit = 32.
    F       = F + '_R_limit_32'
else:
    R_limit = 10.
    F       = F + '_R_limit_10'

#GoodIDs = np.where(R<R_limit) # Removes all particles that is far away from the cluster.

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
    f.savefig(figure_path + 'Fig_CS4_Final_x_hist.png')

if Fig_x_hist2d:
    f = plt.figure(figsize=(13,11))
    plt.xlabel(r'$x-x_c$',fontsize=30 )
    plt.ylabel(r'$y-y_c$',fontsize=30 )
    plt.hexbin(x-xC,y-yC ,gridsize=500)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    
    #plt.title(r'Centralized positions x and y (B, gridsize = 500)',fontsize=30 )
    #plt.title(r'Centralized positions x and y (CS4, gridsize = 500)',fontsize=30)
    #plt.title(r'Centralized positions x and y (CS5, gridsize = 500)',fontsize=30)
    #plt.title(r'Centralized positions x and y (CS6, gridsize = 500)',fontsize=30)
    #plt.title(r'Centralized positions x and y (DS1, gridsize = 500)',fontsize=30)
    #plt.title(r'Centralized positions x and y (D2, gridsize = 500)' ,fontsize=30)
    plt.title(r'Centralized positions x and y (E, gridsize = 500)'  ,fontsize=30)

    #f.savefig(figure_path + 'Fig_B_Final_x_hist2d.png'  )
    #f.savefig(figure_path + 'Fig_CS4_Final_x_hist2d.png')
    #f.savefig(figure_path + 'Fig_CS5_Final_x_hist2d.png')
    #f.savefig(figure_path + 'Fig_CS6_Final_x_hist2d.png')
    #f.savefig(figure_path + 'Fig_DS1_Final_x_hist2d.png')
    #f.savefig(figure_path + 'Fig_D2_Final_x_hist2d.png' )
    f.savefig(figure_path + 'Fig_E_Final_x_hist2d.png'  )

x       = x-np.median(x)
y       = y-np.median(y)
z       = z-np.median(z)
R       = (x**2+y**2+z**2)**.5
GoodIDs = np.where(R<R_limit) # Removes all particles that is far away from the cluster.
x       = x[GoodIDs]
y       = y[GoodIDs]
z       = z[GoodIDs]

vx      = vx[GoodIDs]
vy      = vy[GoodIDs]
vz      = vz[GoodIDs] 
vx      = vx-np.median(vx)
vy      = vy-np.median(vy)
vz      = vz-np.median(vz)

R_hob_par = R[GoodIDs]

# Declare number of particles
if F.startswith('Soft_B_') or F.startswith('E_'):
    N = 10**6
elif F.startswith('CS4_') or F.startswith('CS5_') or F.startswith('CS6_') or F.startswith('DS1_') or F.startswith('Soft_D2_') or F.startswith('IIc') or F.startswith('IId') or F.startswith('IId') or F.startswith('Test_'):    
    N = 10**5
elif F.startswith('CS1_'):
    N = 10**4    
# Declare total mass
if F.startswith('Soft_B_') or F.startswith('CS1_') or F.startswith('CS4_') or F.startswith('CS5_') or F.startswith('CS6_') or F.startswith('E_') or F.startswith('Test_') or F.startswith('IIc_CS4_') or F.startswith('IIc_CS5_') or F.startswith('IIc_CS6_') or F.startswith('IIc_Test_CS4') or F.startswith('IId_CS4'):
    M = 1.
elif F.startswith('DS1_') or F.startswith('D2_') or F.startswith('Soft_D2_') or F.startswith('IIc_Soft_D2_') or F.startswith('IIc_DS1_') or F.startswith('IId_Soft_D2_'):
    M = 1./6.
# Define particle mass 
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
print F

#GoodIDs = np.where(R<R_limit) # Removes all particles that is far away from the cluster.
#R_hob_par = R[GoodIDs]
sigma2_arr              = []   # square of total velocity dispersion
sigmarad2_arr           = []   # square of radial velosity dispersion
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
v_r                     = (vx*x+vy*y+vz*z)/(x**2+y**2+z**2)**.5
r                       = []
Phi                     = []
Theta                   = []
VR                      = []
VTheta                  = []
VPhi                    = []
VR_i_average_inside_bin = []
min_binning_R           = -1.5
max_binning_R           = np.log10(R_limit)
binning_arr_lin_log10   = np.logspace(min_binning_R,max_binning_R,nr_binning_bins)     # Array, -5-1000
bin_radius_arr          = []

for i in range(nr_binning_bins-2):      
    min_R_bin_i            = binning_arr_lin_log10[i]                                  # start of bin
    max_R_bin_i            = binning_arr_lin_log10[i+1]                                # end of bin
    posR_par_inside_bin_i  = np.where((R_hob_par>min_R_bin_i)&(R_hob_par<max_R_bin_i)) # position of particles inside a radial bin
    nr_par_inside_bin_i    = len(posR_par_inside_bin_i[0])                             # number of particles inside a radial bin
    if nr_par_inside_bin_i == 0:
        continue
    v = (vx[posR_par_inside_bin_i]**2+vy[posR_par_inside_bin_i]**2+vz[posR_par_inside_bin_i]**2)**.5
    #sigma2 total
    v2_inside_bin_i     = v**2
    sigma2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(v2_inside_bin_i)
    sigma2_arr.append(sigma2_inside_bin_i)
    bin_radius_arr.append((max_R_bin_i + min_R_bin_i)/2)
    #sigmarad2 radial
    vrad2_inside_bin_i     = v_r[posR_par_inside_bin_i]**2
    sigmarad2_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(vrad2_inside_bin_i)
    sigmarad2_arr.append(sigmarad2_inside_bin_i)

    Volume_cl = (4./3.)*np.pi*(max_R_bin_i**3 - min_R_bin_i**3) # volume of cluster
    den_cl    = nr_par_inside_bin_i/Volume_cl                   # number density
    rho       = den_cl*m                                        # density

    r_i                       = (x[posR_par_inside_bin_i]**2+y[posR_par_inside_bin_i]**2+z[posR_par_inside_bin_i]**2)**.5
    Phi_i                     = sp.arctan2(y[posR_par_inside_bin_i],x[posR_par_inside_bin_i])
    Theta_i                   = sp.arccos(z[posR_par_inside_bin_i]/r_i)
    VR_i                      = sp.sin(Theta_i)*sp.cos(Phi_i)*vx[posR_par_inside_bin_i]+sp.sin(Theta_i)*sp.sin(Phi_i)*vy[posR_par_inside_bin_i]+sp.cos(Theta_i)*vz[posR_par_inside_bin_i]
    VTheta_i                  = sp.cos(Theta_i)*sp.cos(Phi_i)*vx[posR_par_inside_bin_i]+sp.cos(Theta_i)*sp.sin(Phi_i)*vy[posR_par_inside_bin_i]-sp.sin(Theta_i)*vz[posR_par_inside_bin_i]
    VPhi_i                    =               - sp.sin(Phi_i)*vx[posR_par_inside_bin_i]+                sp.cos(Phi_i)*vy[posR_par_inside_bin_i]
    VR_i_average_inside_bin_i = (1./(nr_par_inside_bin_i+1.))*np.sum(VR_i)
    #sigmatheta2
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
rho_arr                     = np.array(rho_arr)

for  i in range(len(sigma2_arr)): #kappa
    if i == 0 or i == len(sigma2_arr)-1:
        kappa_arr.append(np.nan)
        continue   
    dlogr         = np.log10(bin_radius_arr[i+1]) - np.log10(bin_radius_arr[i-1])
    dlogsigmarad2 = np.log10(sigmarad2_arr[i+1])  - np.log10(sigmarad2_arr[i-1])
    kappa_arr.append(dlogsigmarad2/dlogr)

for  i in range(len(density_arr)): #gamma
    if i == 0 or i == len(sigma2_arr)-1:
        gamma_arr.append(np.nan)
        continue
    dlogr   = np.log10(bin_radius_arr[i+1]) - np.log10(bin_radius_arr[i-1])
    dlogrho = np.log10(density_arr[i+1])    - np.log10(density_arr[i-1])
    gamma_arr.append(dlogrho/dlogr)
    
beta_arr = 1. - sigmatheta2_arr/sigmarad2_arr # Calculate beta

if Fig_vx_x:
    f,(ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    ax1.set_xlabel(r'$\log x$'  ,fontsize=30)
    ax1.set_ylabel(r'$\log v_x$',fontsize=30)

    ax1.plot(np.log10(x),np.log10(vx),'o',color='Blue',label='Soft B 0_005',lw=3,ms=2)
    #ax1.plot(np.log10(x),np.log10(vx),'o',color='Blue',label='Soft B 1_000',lw=3,ms=2)

    leg = ax1.legend(prop=dict(size=18),numpoints=1,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'II: $\Delta E,R_{lim}=10^4$',fontsize=30)

    f.savefig(figure_path + 'Soft_B_0_005_logvx_logx_II.png'    )
    #f.savefig(figure_path + 'Soft_B_1_000_logvx_logx_II.png')

if Fig_v_logr:
    r           = (x**2+y**2+z**2)**.5
    v           = (vx**2+vy**2+vz**2)**.5
    f,(ax1,ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    ax1.set_xlabel('r',fontsize=30)
    ax1.set_ylabel(r'total velocity, $v = \sqrt{v_x^2+v_y^2+v_z^2}$',fontsize=30)

    #ax1.plot(r, v,'o',color='Blue',label='Soft B IC'    ,lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label='Soft B 10_005',lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label='Soft B 20_005',lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label='Soft B control IC',lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label='Soft B control 10_005',lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label='Soft B control 20_005',lw=3,ms=2)
    
    #ax1.plot(r, v,'o',color='Blue',label=r'$CS_4$ 2_005'    ,lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label=r'$CS_4$ 2_005 perturbation'    ,lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label=r'$CS_4$ 2_005 P2G (no K_ratio)' ,lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label=r'$CS_4$ 2_005 P2G (unbound)' ,lw=3,ms=2)
    #ax1.plot(r, v,'o',color='Blue',label=r'$CS_4$ 2_005 P2G (no rand)' ,lw=3,ms=2)
    ax1.plot(r, v,'o',color='Blue',label=r'$CS_4$ 2_005 P2G (car sph car)' ,lw=3,ms=2)

    leg = ax1.legend(prop=dict(size=18),numpoints=1,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'IIc: $R_{lim}=32, 20$ bins',fontsize=30)
    ax2.plot(np.log10(r),v,'o',color='Blue',lw=3,ms=2)
    ax2.set_xlabel(r'$\log r$',fontsize=30)
    ax2.yaxis.tick_right()

    #f.savefig(figure_path + 'Soft_B_IC_v_logr_II.png'    )
    #f.savefig(figure_path + 'Soft_B_10_005_v_logr_II.png')
    #f.savefig(figure_path + 'Soft_B_20_005_v_logr_II.png')
    #f.savefig(figure_path + 'Soft_B_control_IC_v_logr_II.png'    )
    #f.savefig(figure_path + 'Soft_B_control_10_005_v_logr_II.png')
    #f.savefig(figure_path + 'Soft_B_control_20_005_v_logr_II.png')

    #f.savefig(figure_path + 'CS4_2_005_v_logr_IIc.png'    )
    #f.savefig(figure_path + 'CS4_2_005_P2G_v_logr_IIc.png')
    #f.savefig(figure_path + 'CS4_2_005_P2G_no_K_ratio_v_logr_IIc.png')
    #f.savefig(figure_path + 'CS4_2_005_P2G_unbound_v_logr_IIc.png')
    #f.savefig(figure_path + 'CS4_2_005_P2G_no_rand_v_logr_IIc.png')
    f.savefig(figure_path + 'CS4_2_005_P2G_car_sph_car_v_logr_IIc.png')



if Fig4_beta:  # plot beta
    f = plt.figure(figsize=(13,11))
    #plt.xlim(-1.7,2.0)
    #plt.ylim(-1.,1.)
    x_plot = np.log10(bin_radius_arr)
    y_plot = beta_arr
    plt.xlabel(r'$\log$r',fontsize=30)
    plt.ylabel(r'$\beta$',fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') # from this graph we see that beta is below zero. this means sigmatheta2_arr/sigmarad2_arr > 1, which in turn means that sigmatheta2_arr > sigmarad2_arr. 
    plt.plot(x_plot,0*x_plot,'--',lw=2,color='grey')

    if Fig4_betafit: # fitting beta with two different profiles
        x      = 10**x_plot
        y_plot = x**2/(23.**2+x**2)
        plt.plot(x_plot,y_plot,'-',ms=2,mew=0,color='blue',label=r'$\frac{x^2}{23^2+x^2}$') 
        Chi2 = 0
        i    = 0 
        while (i < len(beta_arr)):
          Chi2 = Chi2 + ((beta_arr[i]-y_plot[i])**2)/(beta_arr[i]*.2)**2
          i    = i+1         
        Chi2   = (1./(len(beta_arr)-1)) * Chi2
        print 'Chi2 for betafit: ', Chi2
        # Dummy plot to add label to legend for chi2
        plt.plot([],[],ls='.',c='grey',label = r'$\chi^2 = %.6f$'%Chi2)
        leg = plt.legend(prop=dict(size=18),numpoints=2,ncol=2,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        plt.title(r'$\beta$ with fit (%s)'%F,fontsize=30)
        #f.savefig(figure_path + 'B_IC_beta_logr_fit.png'             )
        #f.savefig(figure_path + 'B_Final_beta_logr_fit.png'          )
        #f.savefig(figure_path + 'B_Final_control_beta_logr_fit.png'  )
        #f.savefig(figure_path + 'CS1_IC_beta_logr_fit.png'           )
        #f.savefig(figure_path + 'CS1_Final_beta_logr_fit.png'        )
        #f.savefig(figure_path + 'CS1_Final_control_beta_logr_fit.png')
        #f.savefig(figure_path + 'CS4_IC_beta_logr_fit.png'           )
        #f.savefig(figure_path + 'CS4_Final_beta_logr_fit.png'        )
        #f.savefig(figure_path + 'CS4_Final_control_beta_logr_fit.png')
        #f.savefig(figure_path + 'CS5_IC_beta_logr_fit.png'           )
        #f.savefig(figure_path + 'CS5_Final_beta_logr_fit.png'        )
        #f.savefig(figure_path + 'CS5_Final_control_beta_logr_fit.png')
        #f.savefig(figure_path + 'CS6_IC_beta_logr_fit.png'           )
        #f.savefig(figure_path + 'CS6_Final_beta_logr_fit.png'        )
        #f.savefig(figure_path + 'CS6_Final_control_beta_logr_fit.png')
        #f.savefig(figure_path + 'DS1_IC_beta_logr_fit.png'           )
        #f.savefig(figure_path + 'DS1_Final_beta_logr_fit.png'        )
        #f.savefig(figure_path + 'DS1_Final_control_beta_logr_fit.png')
        #f.savefig(figure_path + 'D2_IC_beta_logr_fit.png'            )
        #f.savefig(figure_path + 'D2_Final_beta_logr_fit.png'         )
        #f.savefig(figure_path + 'D2_Final_control_beta_logr_fit.png' )
        #f.savefig(figure_path + 'E_IC_beta_logr_fit.png'             )
        #f.savefig(figure_path + 'E_Final_beta_logr_fit.png'          )
        #f.savefig(figure_path + 'E_Final_control_beta_logr_fit.png'  )
    else:
        #plt.title(r'$\beta$ with zero-line(%s)'%F,fontsize=30)
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_B final, $R_{limit}=10^4$, 20 bins)',fontsize=30 )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS4 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS5 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS6 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, DS1 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, E final, $R_{limit}=10^4$, 20 bins)',fontsize=30      )

        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_B final, $R_{limit}=50$, 50 bins)',fontsize=30 )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS4 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS5 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS6 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, DS1 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=50$, 50 bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, E final, $R_{limit}=50$, 50 bins)',fontsize=30      )

        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_B final, $R_{limit}=32$, 50 bins)',fontsize=30 )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS4 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS5 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS6 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, DS1 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=32$, 20 bins)',fontsize=30)
        plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, E final, $R_{limit}=32$, 50 bins)',fontsize=30      )

        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_B final, $R_{limit}=10$, 20 bins)',fontsize=30 ) 
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS4 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS5 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, CS6 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, DS1 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10$, 20 bins)',fontsize=30)
        #plt.title(r'$\beta$ with zero-line(Sim II: $\Delta$E, E final, $R_{limit}=10$, 20 bins)',fontsize=30      )

        #f.savefig(figure_path + 'Soft_B_IC_beta_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_beta_logr_II_R10000.png'         )
        #f.savefig(figure_path + 'Soft_B_Final_control_beta_logr_II_R10000.png' )
        #f.savefig(figure_path + 'CS1_IC_beta_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS1_Final_beta_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_beta_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'CS4_IC_beta_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS4_Final_beta_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_beta_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'CS5_IC_beta_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS5_Final_beta_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_beta_logr_II_R10000.png'    ) 
        #f.savefig(figure_path + 'CS6_IC_beta_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS6_Final_beta_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_beta_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'DS1_IC_beta_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'DS1_Final_beta_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_beta_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'Soft_D2_IC_beta_logr_II_R10000.png'                )
        #f.savefig(figure_path + 'Soft_D2_Final_beta_logr_II_R10000.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_beta_logr_II_R10000.png'     )
        #f.savefig(figure_path + 'E_IC_beta_logr_II_R10000.png'                 )
        #f.savefig(figure_path + 'E_Final_beta_logr_II_R10000.png'              )
        #f.savefig(figure_path + 'E_Final_control_beta_logr_II_R10000.png'      )

        #f.savefig(figure_path + 'Soft_B_IC_beta_logr_II_R50.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_beta_logr_II_R50.png'         )
        #f.savefig(figure_path + 'Soft_B_Final_control_beta_logr_II_R50.png' )
        #f.savefig(figure_path + 'CS1_IC_beta_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS1_Final_beta_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_beta_logr_II_R50.png'    )
        #f.savefig(figure_path + 'CS4_IC_beta_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS4_Final_beta_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_beta_logr_II_R50.png'    )
        #f.savefig(figure_path + 'CS5_IC_beta_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS5_Final_beta_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_beta_logr_II_R50.png'    ) 
        #f.savefig(figure_path + 'CS6_IC_beta_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS6_Final_beta_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_beta_logr_II_R50.png'    )
        #f.savefig(figure_path + 'DS1_IC_beta_logr_II_R50.png'               )
        #f.savefig(figure_path + 'DS1_Final_beta_logr_II_R50.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_beta_logr_II_R50.png'    )
        #f.savefig(figure_path + 'Soft_D2_IC_beta_logr_II_R50.png'                )
        #f.savefig(figure_path + 'Soft_D2_Final_beta_logr_II_R50.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_beta_logr_II_R50.png'     )
        #f.savefig(figure_path + 'E_IC_beta_logr_II_R50.png'                 )
        #f.savefig(figure_path + 'E_Final_beta_logr_II_R50.png'              )
        #f.savefig(figure_path + 'E_Final_control_beta_logr_II_R50.png'      )

        #f.savefig(figure_path + 'Soft_B_IC_beta_logr_II_R32.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_beta_logr_II_R32.png'         )
        #f.savefig(figure_path + 'Soft_B_Final_control_beta_logr_II_R32.png' )
        #f.savefig(figure_path + 'CS1_IC_beta_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS1_Final_beta_logr_II_R32.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_beta_logr_II_R32.png'    )
        #f.savefig(figure_path + 'CS4_IC_beta_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS4_Final_beta_logr_II_R32.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_beta_logr_II_R32.png'    )
        #f.savefig(figure_path + 'CS5_IC_beta_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS5_Final_beta_logr_II_R32.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_beta_logr_II_R32.png'    ) 
        #f.savefig(figure_path + 'CS6_IC_beta_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS6_Final_beta_logr_II_R32.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_beta_logr_II_R32.png'    )
        #f.savefig(figure_path + 'DS1_IC_beta_logr_II_R32.png'               )
        #f.savefig(figure_path + 'DS1_Final_beta_logr_II_R32.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_beta_logr_II_R32.png'    )
        #f.savefig(figure_path + 'Soft_D2_IC_beta_logr_II_R32.png'           )
        #f.savefig(figure_path + 'Soft_D2_Final_beta_logr_II_R32.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_beta_logr_II_R32.png')
        #f.savefig(figure_path + 'E_IC_beta_logr_II_R32.png'                 )
        f.savefig(figure_path + 'E_Final_beta_logr_II_R32.png'              )
        #f.savefig(figure_path + 'E_Final_control_beta_logr_II_R32.png'      )

        #f.savefig(figure_path + 'Soft_B_IC_beta_logr_II_R10.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_beta_logr_II_R10.png'         )
        #f.savefig(figure_path + 'Soft_B_Final_control_beta_logr_II_R10.png' )
        #f.savefig(figure_path + 'CS1_IC_beta_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS1_Final_beta_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_beta_logr_II_R10.png'    )
        #f.savefig(figure_path + 'CS4_IC_beta_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS4_Final_beta_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_beta_logr_II_R10.png'    )
        #f.savefig(figure_path + 'CS5_IC_beta_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS5_Final_beta_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_beta_logr_II_R10.png'    ) 
        #f.savefig(figure_path + 'CS6_IC_beta_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS6_Final_beta_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_beta_logr_II_R10.png'    )
        #f.savefig(figure_path + 'DS1_IC_beta_logr_II_R10.png'               )
        #f.savefig(figure_path + 'DS1_Final_beta_logr_II_R10.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_beta_logr_II_R10.png'    )
        #f.savefig(figure_path + 'Soft_D2_IC_beta_logr_II_R10.png'           )
        #f.savefig(figure_path + 'Soft_D2_Final_beta_logr_II_R10.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_beta_logr_II_R10.png')
        #f.savefig(figure_path + 'E_IC_beta_logr_II_R10.png'                 )
        #f.savefig(figure_path + 'E_Final_beta_logr_II_R10.png'              )
        #f.savefig(figure_path + 'E_Final_control_beta_logr_II_R10.png'      )

if Fig5_kappa:
    f      = plt.figure(figsize=(13,11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = kappa_arr
    plt.xlabel(r'$\log $r',fontsize=30)
    plt.ylabel(r'$\kappa$',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (%s)'%F,fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=10^4$, 20 bins)',fontsize=30)

    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=50$, 50 bins)',fontsize=30 )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=50$, 50 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=50$, 50 bins)',fontsize=30      )

    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=32$, 50 bins)',fontsize=30 )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=32$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=32$, 20 bins)',fontsize=30)
    plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=32$, 50 bins)',fontsize=30      )

    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10$, 20 bins)',fontsize=30 )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS4 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS5 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, CS6 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, DS1 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10$, 20 bins)',fontsize=30)
    #plt.title(r'$\kappa$ and zero-line (Sim II: $\Delta$E, E final, $R_{limit}=10$, 20 bins)',fontsize=30      )
    
    plt.plot(x_plot,y_plot,'-o',ms=4,mew=0,color='black')
    plt.plot(x_plot,0*x_plot,'--',lw=2,color='grey')
    #f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R10000.png'  )
    #f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R10000.png'     )
    #f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R10000.png'     )
    #f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R10000.png'     )
    #f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R10000.png'     )
    #f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R10000.png'     )
    #f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R10000.png')
    #f.savefig(figure_path + 'E_Final_kappa_logr_II_R10000.png'       )

    #f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R50.png'  )
    #f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R50.png'     )
    #f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R50.png'     )
    #f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R50.png'     )
    #f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R50.png'     )
    #f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R50.png'     )
    #f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R50.png' )
    #f.savefig(figure_path + 'E_Final_kappa_logr_II_R50.png'       )

    #f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R32.png'  )
    #f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R32.png'     )
    #f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R32.png'     )
    #f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R32.png'     )
    #f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R32.png'     )
    #f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R32.png'     )
    #f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R32.png' )
    f.savefig(figure_path + 'E_Final_kappa_logr_II_R32.png'       )

    #f.savefig(figure_path + 'Soft_B_Final_kappa_logr_II_R10.png'  )
    #f.savefig(figure_path + 'CS1_Final_kappa_logr_II_R10.png'     )
    #f.savefig(figure_path + 'CS4_Final_kappa_logr_II_R10.png'     )
    #f.savefig(figure_path + 'CS5_Final_kappa_logr_II_R10.png'     )
    #f.savefig(figure_path + 'CS6_Final_kappa_logr_II_R10.png'     )
    #f.savefig(figure_path + 'DS1_Final_kappa_logr_II_R10.png'     )
    #f.savefig(figure_path + 'Soft_D2_Final_kappa_logr_II_R10.png' )
    #f.savefig(figure_path + 'E_Final_kappa_logr_II_R10.png'       )

if Fig6_gamma:
    f      = plt.figure(figsize=(13,11))
    x_plot = np.log10(bin_radius_arr)
    y_plot = gamma_arr
    #plt.xlim(0.,1.6)
    plt.ylim(-3.,-1.5)
    plt.xlabel(r'$\log $r',fontsize=30)
    plt.ylabel(r'$\gamma$',fontsize=30)
    plt.plot(x_plot,y_plot,'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')

    if Fig6_gammafit:
        x      = 10**x_plot
        y_plot = -1-3*x/(1+x)
        #plt.plot(x_plot,y_plot,'-',ms=2,mew=0,color='blue',label=r'$\frac{x^2}{23^2+x^2}$')
        plt.plot(x_plot,y_plot,'-',ms=2,mew=0,color='blue',label=r'Fit') 
        Chi2 = 0
        i    = 0
        while (i < len(gamma_arr)):
            #if gamma_arr[i] == nan :
            if isnan(gamma_arr[i]):
                #continue
                print 'nan at index: ', i
            else:
                Chi2 = Chi2 + ((gamma_arr[i]-y_plot[i])**2)/(gamma_arr[i]*.2)**2               
            i = i+1
        Chi2 = (1.0/(len(gamma_arr)-1)) * Chi2
        print 'Chi2 for gammafit: ', Chi2
        # Dummy plot to add label to legend for chi2
        plt.plot([], [], ls='.', c='grey',label = r'$\chi^2 = %.6f$' %Chi2)
        leg = plt.legend(prop=dict(size=18), numpoints=2, ncol=2,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        plt.title('Radial density slope with fit (%s)'%F,fontsize=18)
        #f.savefig(figure_path + 'B_IC_gamma_logr_fit.png'             )
        #f.savefig(figure_path + 'B_Final_gamma_logr_fit.png'          )
        #f.savefig(figure_path + 'B_Final_control_gamma_logr_fit.png'  )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr_fit.png'           )
        #f.savefig(figure_path + 'CS1_Final_gamma_logr_fit.png'        )
        #f.savefig(figure_path + 'CS1_Final_control_gamma_logr_fit.png')
        #f.savefig(figure_path + 'CS4_IC_gamma_logr_fit.png'           )
        #f.savefig(figure_path + 'CS4_Final_gamma_logr_fit.png'        )
        #f.savefig(figure_path + 'CS4_Final_control_gamma_logr_fit.png')
        #f.savefig(figure_path + 'CS5_IC_gamma_logr_fit.png'           )
        #f.savefig(figure_path + 'CS5_Final_gamma_logr_fit.png'        )
        #f.savefig(figure_path + 'CS5_Final_control_gamma_logr_fit.png')
        #f.savefig(figure_path + 'CS6_IC_gamma_logr_fit.png'           )
        #f.savefig(figure_path + 'CS6_Final_gamma_logr_fit.png'        )
        #f.savefig(figure_path + 'CS6_Final_control_gamma_logr_fit.png')             
        #f.savefig(figure_path + 'DS1_IC_gamma_logr_fit.png'           )
        #f.savefig(figure_path + 'DS1_Final_gamma_logr_fit.png'        )
        #f.savefig(figure_path + 'DS1_Final_control_gamma_logr_fit.png')
        #f.savefig(figure_path + 'D2_IC_gamma_logr_fit.png'            )
        #f.savefig(figure_path + 'D2_Final_gamma_logr_fit.png'         )
        #f.savefig(figure_path + 'D2_Final_control_gamma_logr_fit.png' )
        #f.savefig(figure_path + 'E_IC_gamma_logr_fit.png'             )
        #f.savefig(figure_path + 'E_Final_gamma_logr_fit.png'          )
        #f.savefig(figure_path + 'E_Final_control_gamma_logr_fit.png'  )
    else:
        #plt.title('Radial density slope (%s)'%F,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10^4$, 20 bins)',fontsize=30 )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=10^4$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10^4$, 20 bins)',fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=10^4$, 20 bins)',fontsize=30      )

        #plt.title('Radial density slope (Sim II: $\Delta$E, Soft_B final, $R_{limit}=50$, 50 bins)',fontsize=30 )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=50$, 50 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=50$, 50 bins)',fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=50$, 50 bins)',fontsize=30      )

        # R 32
        #plt.title('Radial density slope (Sim II: $\Delta$E, B IC, $R_{limit}=32$, 50 bins)'           ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, B 2_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, B 4_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, B 6_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, B 8_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, B 10_005, $R_{limit}=32$, 50 bins)'       ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, B final, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, B control final, $R_{limit}=32$, 50 bins)',fontsize=30)
        
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 IC, $R_{limit}=32$, 20 bins)',fontsize=30           )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 2_005, $R_{limit}=32$, 20 bins)',fontsize=30        )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 4_005, $R_{limit}=32$, 20 bins)',fontsize=30        )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 6_005, $R_{limit}=32$, 20 bins)',fontsize=30        )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 8_005, $R_{limit}=32$, 20 bins)',fontsize=30        )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 10_005, $R_{limit}=32$, 20 bins)',fontsize=30       )
        #plt.title('Radial density slope (Sim IIc, CS4 40_021, $R_{limit}=32$, 20 bins)',fontsize=30        )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 control final, $R_{limit}=32$, 20 bins)',fontsize=30)
        
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 IC, $R_{limit}=32$, 20 bins)'           ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 2_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 4_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 6_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 8_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 10_005, $R_{limit}=32$, 20 bins)'       ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 control final, $R_{limit}=32$, 20 bins)',fontsize=30)
        
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 IC, $R_{limit}=32$, 20 bins)'           ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 2_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 4_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 6_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 8_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 10_005, $R_{limit}=32$, 20 bins)'       ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 control final, $R_{limit}=32$, 20 bins)',fontsize=30)
        
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 IC, $R_{limit}=32$, 20 bins)'           ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 2_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 4_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 6_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 8_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 10_005, $R_{limit}=32$, 20 bins)'       ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 control final, $R_{limit}=32$, 20 bins)',fontsize=30)
        
        plt.title('Radial density slope (Sim II: $\Delta$E, D2 IC, $R_{limit}=32$, 20 bins)'           ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, D2 2_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, D2 4_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, D2 6_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, D2 8_005, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, D2 10_005, $R_{limit}=32$, 20 bins)'       ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, D2 final, $R_{limit}=32$, 20 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, D2 control final, $R_{limit}=32$, 20 bins)',fontsize=30)
        
        #plt.title('Radial density slope (Sim II: $\Delta$E, E IC, $R_{limit}=32$, 50 bins)'           ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E 2_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E 4_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E 6_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E 8_005, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E 10_005, $R_{limit}=32$, 50 bins)'       ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=32$, 50 bins)'        ,fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E control final, $R_{limit}=32$, 50 bins)',fontsize=30)

        # R 10
        #plt.title('Radial density slope (Sim II: $\Delta$E, Soft_B final, $R_{limit}=10$, 20 bins)',fontsize=30 )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS4 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS5 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, CS6 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, DS1 final, $R_{limit}=10$, 20 bins)',fontsize=30    )
        #plt.title('Radial density slope (Sim II: $\Delta$E, Soft_D2 final, $R_{limit}=10$, 20 bins)',fontsize=30)
        #plt.title('Radial density slope (Sim II: $\Delta$E, E final, $R_{limit}=10$, 20 bins)',fontsize=30      )

        #f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R10000.png'         )
        #f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R10000.png'       )
        #f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R10000.png' )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS4_Final_gamma_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R10000.png'    )             
        #f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R10000.png'               )
        #f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R10000.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R10000.png'    )
        #f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R10000.png'           )
        #f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R10000.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R10000.png')
        #f.savefig(figure_path + 'E_IC_gamma_logr_II_R10000.png'                 )
        #f.savefig(figure_path + 'E_Final_gamma_logr_II_R10000.png'              )
        #f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R10000.png'      )

        #f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R50.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R50.png'         )
        #f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R50.png'    )
        #f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R50.png'       )
        #f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R50.png' )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R50.png'    )
        #f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS4_Final_gamma_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R50.png'    )
        #f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R50.png'    )
        #f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R50.png'               )
        #f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R50.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R50.png'    )             
        #f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R50.png'               )
        #f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R50.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R50.png'    )
        #f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R50.png'           )
        #f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R50.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R50.png')
        #f.savefig(figure_path + 'E_IC_gamma_logr_II_R50.png'                 )
        #f.savefig(figure_path + 'E_Final_gamma_logr_II_R50.png'              )
        #f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R50.png'      )

        # R 32
        #f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R32.png'         )
        #f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R32.png'    )
        #f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R32.png'       )
        #f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R32.png' )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R32.png'    )
        
        #f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS4_2_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS4_4_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS4_6_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS4_8_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS4_10_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS4_40_gamma_logr_IIc_R32.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R32.png'    )
        
        #f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS5_2_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS5_4_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS5_6_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS5_8_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS5_10_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R32.png'    )
        
        #f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS6_2_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS6_4_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS6_6_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS6_8_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'CS6_10_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R32.png'    )
        
        #f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'DS1_2_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'DS1_4_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'DS1_6_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'DS1_8_gamma_logr_II_R32.png'                )
        #f.savefig(figure_path + 'DS1_10_gamma_logr_II_R32.png'               )
        #f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R32.png'    )
        
        #f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R32.png'           )
        #f.savefig(figure_path + 'Soft_D2_2_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'Soft_D2_4_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'Soft_D2_6_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'Soft_D2_8_gamma_logr_II_R32.png'            )
        #f.savefig(figure_path + 'Soft_D2_10_gamma_logr_II_R32.png'           )
        #f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R32.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R32.png')
        
        #f.savefig(figure_path + 'E_IC_gamma_logr_II_R32.png'                 )
        #f.savefig(figure_path + 'E_2_gamma_logr_II_R32.png'                  )
        #f.savefig(figure_path + 'E_4_gamma_logr_II_R32.png'                  )
        #f.savefig(figure_path + 'E_6_gamma_logr_II_R32.png'                  )
        #f.savefig(figure_path + 'E_8_gamma_logr_II_R32.png'                  )
        #f.savefig(figure_path + 'E_10_gamma_logr_II_R32.png'                 )
        #f.savefig(figure_path + 'E_Final_gamma_logr_II_R32.png'              )
        #f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R32.png'      )


        # R 10
        #f.savefig(figure_path + 'Soft_B_IC_gamma_logr_II_R10.png'            )
        #f.savefig(figure_path + 'Soft_B_Final_gamma_logr_II_R10.png'         )
        #f.savefig(figure_path + 'Soft_B_IC_control_gamma_logr_II_R10.png'    )
        #f.savefig(figure_path + 'Soft_B_control_gamma_logr_II_R10.png'       )
        #f.savefig(figure_path + 'Soft_B_Final_control_gamma_logr_II_R10.png' )
        #f.savefig(figure_path + 'CS1_IC_gamma_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS1_Final_gamma_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS1_Final_control_gamma_logr_II_R10.png'    )
        #f.savefig(figure_path + 'CS4_IC_gamma_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS4_Final_gamma_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS4_Final_control_gamma_logr_II_R10.png'    )
        #f.savefig(figure_path + 'CS5_IC_gamma_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS5_Final_gamma_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS5_Final_control_gamma_logr_II_R10.png'    )
        #f.savefig(figure_path + 'CS6_IC_gamma_logr_II_R10.png'               )
        #f.savefig(figure_path + 'CS6_Final_gamma_logr_II_R10.png'            )
        #f.savefig(figure_path + 'CS6_Final_control_gamma_logr_II_R10.png'    )             
        #f.savefig(figure_path + 'DS1_IC_gamma_logr_II_R10.png'               )
        #f.savefig(figure_path + 'DS1_Final_gamma_logr_II_R10.png'            )
        #f.savefig(figure_path + 'DS1_Final_control_gamma_logr_II_R10.png'    )
        #f.savefig(figure_path + 'Soft_D2_IC_gamma_logr_II_R10.png'           )
        #f.savefig(figure_path + 'Soft_D2_Final_gamma_logr_II_R10.png'        )
        #f.savefig(figure_path + 'Soft_D2_Final_control_gamma_logr_II_R10.png')
        #f.savefig(figure_path + 'E_IC_gamma_logr_II_R10.png'                 )
        #f.savefig(figure_path + 'E_Final_gamma_logr_II_R10.png'              )
        #f.savefig(figure_path + 'E_Final_control_gamma_logr_II_R10.png'      )

if Fig7_betagamma:
    f = plt.figure()
    subplot(121)
    x_plot = beta_arr
    y_plot = gamma_arr
    plt.xlabel(r'$\beta$' ,fontsize=20)
    plt.ylabel(r'$\gamma$',fontsize=20)
    plt.title(r'$\gamma$ vs $\beta$ (%s)' %F , fontsize=18)
    plt.plot(x_plot,y_plot,'-o',ms=2,mew=0,color='black')
    plt.grid()

    subplot(122)
    x_plot = beta_arr
    y_plot = kappa_arr
    plt.xlabel(r'$\beta$' ,fontsize=20)
    plt.ylabel(r'$\kappa$',fontsize=20)
    plt.title(r'$\kappa$ vs $\beta$',fontsize=20)
    plt.plot(x_plot,y_plot,'-o',ms=2,mew=0,color='black')
    plt.grid()
    #f.savefig(figure_path + 'B_betagamma.png'  )
    #f.savefig(figure_path + 'CS1_betagamma.png')
    #f.savefig(figure_path + 'CS4_betagamma.png')
    #f.savefig(figure_path + 'CS5_betagamma.png')
    #f.savefig(figure_path + 'CS6_betagamma.png')
    #f.savefig(figure_path + 'DS1_betagamma.png')
    #f.savefig(figure_path + 'D2_betagamma.png' )
    #f.savefig(figure_path + 'E_betagamma.png'  )

if save_lnr_beta_gamma_kappa_VR_r_sigma_r_r2_rho: 
    logr_arr                    = np.array(np.log10(bin_radius_arr))
    beta_arr                    = np.array(beta_arr)
    gamma_arr                   = np.array(gamma_arr)
    kappa_arr                   = np.array(kappa_arr)
    r_arr                       = 10**(logr_arr)
    sigmarad2_arr               = np.array(sigmarad2_arr)
    GoodIDs                     = np.where(gamma_arr == gamma_arr)
    logr_arr                    = logr_arr[GoodIDs]
    gamma_arr                   = gamma_arr[GoodIDs]
    beta_arr                    = beta_arr[GoodIDs]
    kappa_arr                   = kappa_arr[GoodIDs]
    r_arr                       = r_arr[GoodIDs]
    sigmarad2_arr               = sigmarad2_arr[GoodIDs]
    VR_i_average_inside_bin_arr = VR_i_average_inside_bin_arr[GoodIDs]

    if Gamma == -2.0:
        r_r2_arr = r_arr/r_2
        #print 'r_r2_arr = ', r_r2_arr
        rho_arr  = rho_arr[GoodIDs]
        x        = np.array((logr_arr,beta_arr,gamma_arr,kappa_arr,VR_i_average_inside_bin_arr,r_arr,sigmarad2_arr,r_r2_arr,rho_arr))
        x        = x.transpose()
        out_name = text_files_path + F +'.txt'
        np.savetxt(out_name,x,delimiter=' ',header='          logr                   beta                      gamma                  kappa                  VR_average                  r                  sigmarad2                  r_r2                   rho')
    else:
        rho_arr  = rho_arr[GoodIDs]
        x        = np.array((logr_arr,beta_arr,gamma_arr,kappa_arr,VR_i_average_inside_bin_arr,r_arr,sigmarad2_arr,rho_arr))
        x        = x.transpose()
        out_name = text_files_path + F +'.txt'
        np.savetxt(out_name,x,delimiter=' ',header='          logr                   beta                      gamma                  kappa                  VR_average                  r                  sigmarad2                  rho')
        print 'out_name = ', out_name

plt.show()
