# -*- coding: utf-8 -*-

import h5py
import numpy             as     np
import matplotlib.pyplot as     plt
import IPython
from   matplotlib.colors import LogNorm
import time
import pylab
import seaborn           as     sns

User_path                  =                                      '/Users/gustav.c.rasmussen/'
Desktop_path               =  User_path                         + 'Desktop/'
GADGET_G_path              =  Desktop_path                      + 'RunGadget/G_perturbations/'
Stable_path                =                                      'G_perturbations/Stable_structures/'
figure_path                =  Desktop_path + Stable_path        + 'figures/'
text_files_path            =  Desktop_path + Stable_path        + 'text_files/'
Martin_path                =                                      'Martin_IC_and_Final_Edd_and_OM/'
hdf5_path                  =  Desktop_path                      + 'G_perturbations/hdf5_files/'
nosync_path                =  User_path                         + 'nosync/RunGadget/'

Colors                     =  ['red', 'blue','black','brown','yellow','green'    ]*3
Colors2                    =  ['maroon','cyan','green','grey', 'SkyBlue','orange']*2
Symbols                    =  ['-o','-s','-<','--v','--*','--s','--d'            ]*3

list_of_files_Martin_IC                 =  [ (text_files_path + Martin_path + 'OMG00_001_IC_000.txt', 'OMG00_001_IC_000'),
                                             (text_files_path + Martin_path + '0G00_IC_000.txt'     , '0G00_IC_000'     )]
list_of_files_Martin_Final              =  [ (text_files_path + Martin_path + '0G20_001.txt'        , '0G20_001'        ),
                                             (text_files_path + Martin_path + '00-5G20_001.txt'     , '00-5G20_001'     ),
                                             (text_files_path + Martin_path + 'om0-3.5G20_001.txt'  , 'om0-3.5G20_001'  ),
                                             (text_files_path + Martin_path + 's1G20_001.txt'       , 's1G20_001'       ),
                                             (text_files_path + Martin_path + 's2G20_001.txt'       , 's2G20_001'       ),
                                             (text_files_path + Martin_path + 's3G20_001.txt'       , 's3G20_001'       ),
                                             (text_files_path + Martin_path + 's4G20_001.txt'       , 's4G20_001'       ),
                                             (text_files_path + Martin_path + 'OMG20_Final_000.txt' , 'OMG20_Final_000' )]                     
# Datasets below are structured as follows: Column 0: lnr, Column 1: beta, Column 2: gamma, Column 3: kappa, Column 4: VR, Column 5: r, Column 6: sigmarad2, Column 7: r_r2, Column 8: rho.
list_of_files_A                         =  [ (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_0_000.txt'                                       , 'A_Hernquist10000_G1.0_0_000'                                       ),
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_5_005.txt'                                       , 'A_Hernquist10000_G1.0_5_005'                                       ),
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_10_005.txt'                                      , 'A_Hernquist10000_G1.0_10_005'                                      ),   
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_40_005.txt'                                      , 'A_Hernquist10000_G1.0_40_005'                                      ), 
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_48_009.txt'                                      , 'A_Hernquist10000_G1.0_48_008'                                      )]
list_of_files_B                         =  [ (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_0_000.txt'                                       , 'B_Hernquist10000_G1.0_0_000'                                       ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_5_005.txt'                                       , 'B_Hernquist10000_G1.0_5_005'                                       ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_10_005.txt'                                      , 'B_Hernquist10000_G1.0_10_005'                                      ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_000.txt'                                     , 'B_Hernquist10000_G1.0_198_000'                                     ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_093.txt'                                     , 'B_Hernquist10000_G1.0_198_093'                                     )]
list_of_files_C_IC                      =  [ (text_files_path + 'CS1/'      + 'CS1_Osipkov_Merritt10000_G1.0_0_000.txt'                               , 'CS1_Osipkov_Merritt10000_G1.0_0_000'                               ),
                                             (text_files_path + 'CS2/'      + 'CS2_Osipkov_Merritt10000_G1.0_0_000.txt'                               , 'CS2_Osipkov_Merritt10000_G1.0_0_000'                               ),
                                             (text_files_path + 'CS3/'      + 'CS3_Osipkov_Merritt10000_G1.0_0_000.txt'                               , 'CS3_Osipkov_Merritt10000_G1.0_0_000'                               ),
                                             (text_files_path + 'CS1/'      + 'CS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt'                , 'CS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'                ),
                                             (text_files_path + 'CS2/'      + 'CS2_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt'                , 'CS2_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'                ),
                                             (text_files_path + 'CS3/'      + 'CS3_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt'                , 'CS3_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'                ),
                                             (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_0_000.txt'                               , 'CS4_Osipkov_Merritt10000_G1.0_0_000'                               ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_0_000.txt'                               , 'CS5_Osipkov_Merritt10000_G1.0_0_000'                               ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_0_000.txt'                               , 'CS6_Osipkov_Merritt10000_G1.0_0_000'                               ),
                                             (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt'                , 'CS4_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'                ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt'                , 'CS5_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'                ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt'                , 'CS6_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'                )]
list_of_files_CS4CS5CS6_Final           =  [ (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_48_093.txt'                              , 'CS4_Osipkov_Merritt10000_G1.0_48_093'                              ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_48_093.txt'                              , 'CS5_Osipkov_Merritt10000_G1.0_48_093'                              ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_48_093.txt'                              , 'CS6_Osipkov_Merritt10000_G1.0_48_093'                              ),
                                             (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt'               , 'CS4_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins'               ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt'               , 'CS5_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins'               ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt'               , 'CS6_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins'               )]
list_of_files_DS1D2_IC                  =  [ (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_0_000.txt'                               , 'DS1_Osipkov_Merritt10000_G1.0_0_000'                               ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_0_000.txt'                                      , 'D2_Hernquist10000_G1.0_0_000'                                      ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt'                , 'DS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'                ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_0_000_20_radial_bins.txt'                       , 'D2_Hernquist10000_G1.0_0_000_20_radial_bins'                       )]
list_of_files_DS1D2_Final               =  [ (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093.txt'                              , 'DS1_Osipkov_Merritt10000_G1.0_48_093'                              ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093.txt'                                     , 'D2_Hernquist10000_G1.0_48_093'                                     ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt'               , 'DS1_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins'               ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093_20_radial_bins.txt'                      , 'D2_Hernquist10000_G1.0_48_093_20_radial_bins'                      )]
list_of_files_E                         =  [ (text_files_path + 'E/'        + 'E_Hernquist10000_G1.0_0_000.txt'                                       , 'E_Hernquist10000_G1.0_0_000'                                       ),
                                             (text_files_path + 'E/'        + 'E_Hernquist10000_G1.0_5_005.txt'                                       , 'E_Hernquist10000_G1.0_5_005'                                       ),
                                             (text_files_path + 'E/'        + 'E_Hernquist10000_G1.0_10_005.txt'                                      , 'E_Hernquist10000_G1.0_10_005'                                      ),
                                             (text_files_path + 'E/'        + 'E_Hernquist10000_G1.0_198_000.txt'                                     , 'E_Hernquist10000_G1.0_198_000'                                     ),
                                             (text_files_path + 'E/'        + 'E_Hernquist10000_G1.0_198_093.txt'                                     , 'E_Hernquist10000_G1.0_198_093'                                     )]
list_of_files_B_IC_R10000               =  [ (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_0_000_R_limit_10000.txt'                         , 'B_Hernquist10000_G1.0_0_000_R_limit_10000'                         ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'          , 'B_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'          )]
list_of_files_B_Almost_Final_R10000     =  [ (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_093_R_limit_10000.txt'                       , 'B_Hernquist10000_G1.0_198_093_R_limit_10000'                       ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_093_R_limit_10000_20_radial_bins.txt'        , 'B_Hernquist10000_G1.0_198_093_R_limit_10000_20_radial_bins'        )]
list_of_files_B_Final_R10000            =  [ (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_199_093_R_limit_10000.txt'                       , 'B_Hernquist10000_G1.0_199_093_R_limit_10000'                       ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_199_093_R_limit_10000_20_radial_bins.txt'        , 'B_Hernquist10000_G1.0_199_093_R_limit_10000_20_radial_bins'        )] # Not created yet.
list_of_files_CS4CS5CS6_IC_R10000       =  [ (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000.txt'                 , 'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000'                 ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000.txt'                 , 'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000'                 ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000.txt'                 , 'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000'                 ),
                                             (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'  , 'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'  ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'  , 'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'  ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'  , 'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'  )]
list_of_files_CS4CS5CS6_Final_R10000    =  [ (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000.txt'                , 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000'                ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000.txt'                , 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000'                ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000.txt'                , 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000'                ),
                                             (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt' , 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins' ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt' , 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins' ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt' , 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins' )]
list_of_files_DS1D2_IC_R10000           =  [ (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000.txt'                 , 'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000'                 ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_0_000_R_limit_10000.txt'                        , 'D2_Hernquist10000_G1.0_0_000_R_limit_10000'                        ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'  , 'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'  ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'         , 'D2_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'         )]
list_of_files_DS1D2_Almost_Final_R10000 =  [ (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000.txt'                , 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000'                ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093_R_limit_10000.txt'                       , 'D2_Hernquist10000_G1.0_48_093_R_limit_10000'                       ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt' , 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins' ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt'        , 'D2_Hernquist10000_G1.0_48_093_R_limit_10000_20_radial_bins'        ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_100_radial_bins.txt', 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_100_radial_bins'),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093_R_limit_10000_100_radial_bins.txt'       , 'D2_Hernquist10000_G1.0_48_093_R_limit_10000_100_radial_bins'       ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_200_radial_bins.txt', 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_200_radial_bins'),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093_R_limit_10000_200_radial_bins.txt'       , 'D2_Hernquist10000_G1.0_48_093_R_limit_10000_200_radial_bins'       )]
list_of_files_DS1D2_Final_R10000        =  [ (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000.txt'                , 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000'                ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_49_093_R_limit_10000.txt'                       , 'D2_Hernquist10000_G1.0_49_093_R_limit_10000'                       ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_20_radial_bins.txt' , 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_20_radial_bins' ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_49_093_R_limit_10000_20_radial_bins.txt'        , 'D2_Hernquist10000_G1.0_49_093_R_limit_10000_20_radial_bins'        ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_100_radial_bins.txt', 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_100_radial_bins'),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_49_093_R_limit_10000_100_radial_bins.txt'       , 'D2_Hernquist10000_G1.0_49_093_R_limit_10000_100_radial_bins'       ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_200_radial_bins.txt', 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_200_radial_bins'),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_49_093_R_limit_10000_200_radial_bins.txt'       , 'D2_Hernquist10000_G1.0_49_093_R_limit_10000_200_radial_bins'       )]
list_of_files_B_Almost_Final_R5000      =  [ (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_093_R_limit_5000.txt'                        , 'B_Hernquist10000_G1.0_198_093_R_limit_5000'                        ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_093_R_limit_5000_20_radial_bins.txt'         , 'B_Hernquist10000_G1.0_198_093_R_limit_5000_20_radial_bins'         )]
list_of_files_CS4CS5CS6_Final_R5000     =  [ (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000.txt'                 , 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000'                 ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000.txt'                 , 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000'                 ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000.txt'                 , 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000'                 ),
                                             (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins.txt'  , 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins'  ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins.txt'  , 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins'  ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins.txt'  , 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins'  )]
list_of_files_DS1D2_Almost_Final_R5000  =  [ (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000.txt'                 , 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000'                 ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093_R_limit_5000.txt'                        , 'D2_Hernquist10000_G1.0_48_093_R_limit_5000'                        ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins.txt'  , 'DS1_Osipkov_Merritt10000_G1.0_48_093_R_limit_5000_20_radial_bins'  ),
                                             (text_files_path + 'D2/'       + 'D2_Hernquist10000_G1.0_48_093_R_limit_5000_20_radial_bins.txt'         , 'D2_Hernquist10000_G1.0_48_093_R_limit_5000_20_radial_bins'         )]





list_of_files_A_R10000_20bins           =  [ (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'          , 'A_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'          ),
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_5_005_R_limit_10000_20_radial_bins.txt'          , 'A_Hernquist10000_G1.0_5_005_R_limit_10000_20_radial_bins'          ),
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_10_005_R_limit_10000_20_radial_bins.txt'         , 'A_Hernquist10000_G1.0_10_005_R_limit_10000_20_radial_bins'         ),   
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_40_005_R_limit_10000_20_radial_bins.txt'         , 'A_Hernquist10000_G1.0_40_005_R_limit_10000_20_radial_bins'         ), 
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_48_009_R_limit_10000_20_radial_bins.txt'         , 'A_Hernquist10000_G1.0_48_008_R_limit_10000_20_radial_bins'         )]

list_of_files_B_R10000_20bins           =  [ (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt'          , 'B_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'          ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_5_005_R_limit_10000_20_radial_bins.txt'          , 'B_Hernquist10000_G1.0_5_005_R_limit_10000_20_radial_bins'          ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_10_005_R_limit_10000_20_radial_bins.txt'         , 'B_Hernquist10000_G1.0_10_005_R_limit_10000_20_radial_bins'         ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_000_R_limit_10000_20_radial_bins.txt'        , 'B_Hernquist10000_G1.0_198_000_R_limit_10000_20_radial_bins'        ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_198_093_R_limit_10000_20_radial_bins.txt'        , 'B_Hernquist10000_G1.0_198_093_R_limit_10000_20_radial_bins'        )]






list_of_files_A_Rlimit32_50bins         =  [ (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins.txt'            ,'A_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins'             ),
                                             (text_files_path + 'A/'        + 'A_Hernquist10000_G1.0_48_009_R_limit_32_50_radial_bins.txt'           ,'A_Hernquist10000_G1.0_48_009_R_limit_32_50_radial_bins'            )]
list_of_files_B_Rlimit32_50bins         =  [ (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins.txt'            ,'B_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins'             ),
                                             (text_files_path + 'B/'        + 'B_Hernquist10000_G1.0_199_093_R_limit_32_50_radial_bins.txt'          ,'B_Hernquist10000_G1.0_199_093_R_limit_32_50_radial_bins'           )]
list_of_files_CS4_Rlimit32_20bins       =  [ (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt'    ,'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'     ),
                                             (text_files_path + 'CS4/'      + 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt'   ,'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins'    )]
list_of_files_CS5_Rlimit32_20bins       =  [ (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt'    ,'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'     ),
                                             (text_files_path + 'CS5/'      + 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt'   ,'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins'    )]
list_of_files_CS6_Rlimit32_20bins       =  [ (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt'    ,'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'     ),
                                             (text_files_path + 'CS6/'      + 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt'   ,'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt')]
list_of_files_DS1_Rlimit32_20bins       =  [ (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt'    ,'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'     ),
                                             (text_files_path + 'DS1/'      + 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_32_20_radial_bins.txt'   ,'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_32_20_radial_bins'    )]
list_of_files_Soft_D2_Rlimit32_20bins   =  [ (text_files_path + 'Soft_D2/'  + 'Soft_D2_Hernquist10000_G1.0_0_000_R_limit_32_20_radial_bins.txt'      ,'Soft_D2_Hernquist10000_G1.0_0_000_R_limit_32_20_radial_bins'       ),
                                             (text_files_path + 'Soft_D2/'  + 'Soft_D2_Hernquist10000_G1.0_49_093_R_limit_32_20_radial_bins.txt'     ,'Soft_D2_Hernquist10000_G1.0_49_093_R_limit_32_20_radial_bins'      )]
list_of_files_E_Rlimit32_50bins         =  [ (text_files_path + 'E/'        + 'E_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins.txt'            ,'E_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins'             ),
                                             (text_files_path + 'E/'        + 'E_Hernquist10000_G1.0_198_093_R_limit_32_50_radial_bins.txt'          ,'E_Hernquist10000_G1.0_198_093_R_limit_32_50_radial_bins'           )]




# Bound particles only (rfp).
# All 50 bins, final products, largest R_limit.
list_of_files_rfp                       =  [ (text_files_path + 'B/'        + 'B_bound_particles_G1.0_200_rfp_093_R_limit_10000.txt'                  , 'B_bound_particles_G1.0_200_rfp_093_R_limit_10000'                  ),
                                             (text_files_path + 'CS4/'      + 'CS4_bound_particles_G1.0_49_rfp_093_R_limit_10000.txt'                 , 'CS4_bound_particles_G1.0_49_rfp_093_R_limit_10000'                 ),
                                             (text_files_path + 'CS5/'      + 'CS5_bound_particles_G1.0_49_rfp_093_R_limit_10000.txt'                 , 'CS5_bound_particles_G1.0_49_rfp_093_R_limit_10000'                 ),
                                             (text_files_path + 'CS6/'      + 'CS6_bound_particles_G1.0_49_rfp_093_R_limit_10000.txt'                 , 'CS6_bound_particles_G1.0_49_rfp_093_R_limit_10000'                 ),
                                             (text_files_path + 'DS1/'      + 'DS1_bound_particles_G1.0_50_rfp_093_R_limit_10000.txt'                 , 'DS1_bound_particles_G1.0_50_rfp_093_R_limit_10000'                 ),
                                             (text_files_path + 'D2/'       + 'D2_bound_particles_G1.0_50_rfp_093_R_limit_10000.txt'                  , 'D2_bound_particles_G1.0_50_rfp_093_R_limit_10000'                  )]

datalist_Martin_IC                      =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_Martin_IC                ]
datalist_Martin_Final                   =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_Martin_Final             ]
datalist_A                              =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_A                        ]
datalist_B                              =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_B                        ]
#datalist_C_IC                           =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_C_IC                     ]
#datalist_CS4CS5CS6_Final                =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_CS4CS5CS6_Final          ]
#datalist_DS1D2_IC                       =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_DS1D2_IC                 ]
#datalist_DS1D2_Final                    =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_DS1D2_Final              ]
#datalist_E                              =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_E                        ]
datalist_B_IC_R10000                    =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_B_IC_R10000              ]
datalist_B_Almost_Final_R10000          =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_B_Almost_Final_R10000    ]
datalist_B_Final_R10000                 =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_B_Final_R10000           ]
#datalist_CS4CS5CS6_IC_R10000            =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_CS4CS5CS6_IC_R10000      ]
#datalist_CS4CS5CS6_Final_R10000         =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_CS4CS5CS6_Final_R10000   ]
#datalist_DS1D2_IC_R10000                =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_DS1D2_IC_R10000          ]
#datalist_DS1D2_Almost_Final_R10000      =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_DS1D2_Almost_Final_R10000]
#datalist_DS1D2_Final_R10000             =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_DS1D2_Final_R10000       ]
datalist_B_Almost_Final_R5000           =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_B_Almost_Final_R5000     ]
#datalist_CS4CS5CS6_Final_R5000          =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_CS4CS5CS6_Final_R5000    ]
#datalist_DS1D2_Almost_Final_R5000       =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_DS1D2_Almost_Final_R5000 ]
datalist_A_R10000_20bins                =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_A_R10000_20bins          ]
datalist_B_R10000_20bins                =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_B_R10000_20bins          ]

#datalist_rfp                            =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_rfp                      ]

datalist_A_R32                          =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_A_Rlimit32_50bins         ]
datalist_B_R32                          =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_B_Rlimit32_50bins         ]
datalist_CS4_R32                        =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_CS4_Rlimit32_20bins       ]
datalist_CS5_R32                        =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_CS5_Rlimit32_20bins       ]
datalist_CS6_R32                        =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_CS6_Rlimit32_20bins       ]
datalist_DS1_R32                        =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_DS1_Rlimit32_20bins       ]
datalist_Soft_D2_R32                    =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_Soft_D2_Rlimit32_20bins   ]
datalist_E_R32                          =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_E_Rlimit32_50bins         ] 
#datalist_rfp_R32                       =  [ ( pylab.loadtxt(filename), label ) for filename, label in list_of_files_rfp_R32                   ]


# Switches for figures

logr_rho_IC_Final_R32                          = 1
log_r_r2_rho_IC_Final_R32                      = 1

logr_rho                                       = 0
log_r_r2_rho                                   = 0

A                                              = 0
B                                              = 0
CS1CS2CS3                                      = 0
CS4CS5CS6                                      = 0
DS1D2                                          = 0
BCS4CS5CS6DS1D2                                = 0
DS1D2_final_evolution                          = 0
DS1                                            = 0
D2                                             = 0
rfp_B                                          = 0
rfp_CS4CS5CS6                                  = 0
rfp_DS1D2                                      = 0
rfp_BCS4CS5CS6DS1D2                            = 0
Overplot_IC_Final                              = 0
beta_vs_gamma_plus_kappa                       = 0
Attractor_3D                                   = 0
Time_evolution_beta_gamma_kappa                = 0
Overplot_logr_gamma                            = 0
Overplot_ln_rdividedbyd3_gamma                 = 0
lnr_VR_IC_Final_50bins_20bins                  = 0
lnr_sigmarad2_IC_Final_50bins_20bins           = 0
lnr_sigmarad2_vr_Final_50bins                  = 0
R_limit_10000_logr_sigmarad2_vr_Final_20bins   = 0
R_limit_5000_lnr_sigmarad2_vr_Final_50bins     = 0
R_limit_10000_logr_r_vr_IC_Final_20bins_50bins = 0
R_limit_10000_logr_r_ur_Final_20bins_50bins    = 0
R_limit_10000_logr_ur_Final_20bins_50bins      = 0
Overplot_logr_gamma_4_different_bins           = 0 # Panel created
R_limit_10000_logr_vr_Final_rfp_50bins         = 0 # Panel created





if logr_rho_IC_Final_R32:
    f,(ax1,ax2)=plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0) 
    # IC
    # A
    data, label = datalist_A_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[0],color=Colors[0],label='A',lw=2,ms=7)
    # B
    data, label = datalist_B_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[1],color=Colors[1],label='B',lw=2,ms=7)
    # CS4
    data, label = datalist_CS4_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[2],color=Colors[2],label='CS4',lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[3],color=Colors[3],label='CS5',lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[4],color=Colors[4],label='CS6',lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[5],color=Colors[5],label='DS1',lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[6],color=Colors[6],label='Soft_D2',lw=2,ms=7)
    # E
    data, label = datalist_E_R32[0]
    ax1.plot(data[:,0],np.log10(data[:,8]),Symbols[7],color=Colors[7],label='E',lw=2,ms=7)

    ax1.set_title(r'IC ($I: \Delta G, R_{limit}=32$)',fontsize=30)
    ax1.set_xlabel(r'$\log r$'   ,fontsize=30)
    ax1.set_ylabel(r'$\log \rho$',fontsize=30)
    leg = ax1.legend(prop=dict(size=18),numpoints=1,ncol=1,loc=0,fancybox=True,handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    # Final
    # A
    data, label = datalist_A_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[0],color=Colors[0],lw=2,ms=7)
    # B
    data, label = datalist_B_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[1],color=Colors[1],lw=2,ms=7)
    # CS4
    data, label = datalist_CS4_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[2],color=Colors[2],lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[3],color=Colors[3],lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[4],color=Colors[4],lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[5],color=Colors[5],lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[6],color=Colors[6],lw=2,ms=7)
    # E
    data, label = datalist_E_R32[1]
    ax2.plot(data[:,0],np.log10(data[:,8]),Symbols[7],color=Colors[7],lw=2,ms=7)

    ax2.set_xlabel(r'$\log r$',fontsize=30)
    ax2.set_title(r'Final'    ,fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figure_path + 'logr_rho_IC_Final_R32.png')

if log_r_r2_rho_IC_Final_R32:
    f,(ax1,ax2)=plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0) 
    # IC
    # A
    data, label = datalist_A_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[0],color=Colors[0],label='A',lw=2,ms=7)
    # B
    data, label = datalist_B_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[1],color=Colors[1],label='B',lw=2,ms=7)
    # CS4
    data, label = datalist_CS4_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[2],color=Colors[2],label='CS4',lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[3],color=Colors[3],label='CS5',lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[4],color=Colors[4],label='CS6',lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[5],color=Colors[5],label='DS1',lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[6],color=Colors[6],label='Soft_D2',lw=2,ms=7)
    # E
    data, label = datalist_E_R32[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[7],color=Colors[7],label='E',lw=2,ms=7)

    ax1.set_title(r'IC ($I: \Delta G, R_{limit}=32$)',fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$'   ,fontsize=30)
    ax1.set_ylabel(r'$\log \rho$',fontsize=30)
    leg = ax1.legend(prop=dict(size=18),numpoints=1,ncol=1,loc=0,fancybox=True,handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    # Final
    # A
    data, label = datalist_A_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[0],color=Colors[0],lw=2,ms=7)
    # B
    data, label = datalist_B_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[1],color=Colors[1],lw=2,ms=7)
    # CS4
    data, label = datalist_CS4_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[2],color=Colors[2],lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[3],color=Colors[3],lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[4],color=Colors[4],lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[5],color=Colors[5],lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[6],color=Colors[6],lw=2,ms=7)
    # E
    data, label = datalist_E_R32[1]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[7],color=Colors[7],lw=2,ms=7)

    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_title(r'Final'                     ,fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figure_path + 'log_r_r2_rho_IC_Final_R32.png')


























if logr_rho:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0) 
    
    for i in range(len(datalist_A_R10000_20bins)):
        data, label = datalist_A_R10000_20bins[i]
        a = label[22:-29]
        print a
        ax1.plot( data[:,0], np.log10(data[:,8]),Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    ax1.set_title(r'Sim. I of A ($R_{limit}=10^4, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\log r$'   ,fontsize=30)
    ax1.set_ylabel(r'$\log \rho$',fontsize=30)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    for i in range(len(datalist_B_R10000_20bins)):
        data, label = datalist_B_R10000_20bins[i]
        a = label[22:-29]
        ax2.plot( data[:,0], np.log10(data[:,8]),Symbols[i],color = Colors[i],  label=a,lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\log r$'   ,fontsize=30)
    ax2.set_title(r'Sim. I of B',fontsize=30)
    #ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='on',labelleft='on')
    ax2.yaxis.tick_right()
    f.savefig(figure_path + 'logr_rho.png')


if log_r_r2_rho:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0) 
    
    for i in range(len(datalist_A_R10000_20bins)):
        data, label = datalist_A_R10000_20bins[i]
        a = label[22:-29]
        ax1.plot( np.log10(data[:,7]), np.log10(data[:,8]),Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    ax1.set_title(r'Sim. I of A ($R_{limit}=10^4, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax1.set_ylabel(r'$\log \rho$',fontsize=30)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    for i in range(len(datalist_B_R10000_20bins)):
        data, label = datalist_B_R10000_20bins[i]
        a = label[22:-29]
        ax2.plot( np.log10(data[:,7]), np.log10(data[:,8]),Symbols[i],color = Colors[i],  label=a,lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_title(r'Sim. I of B',fontsize=30)
    ax2.yaxis.tick_right()
    f.savefig(figure_path + 'log_r_r2_rho.png')






if Overplot_IC_Final:
    f = plt.figure()
    plt.subplot(121)
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        plt.plot( data[:,0], data[:,1],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(len(datalist_Martin_Final)-1):
        data, label = datalist_Martin_Final[i]
        plt.plot( data[:,4], data[:,5],Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7)
    data, label = datalist_Martin_Final[7]
    plt.plot( data[:,0], data[:,1],Symbols[i], color=Colors2[7],label=label ,lw=2,ms=7)
    plt.title(r'IC and Final',fontsize=20)
    plt.xlabel(r'$\beta$',fontsize=24)
    plt.ylabel(r'$\gamma$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=4,handlelength=2.5)

    plt.subplot(122)
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i],  label=label,lw=2,ms=7)
    for i in range(len(datalist_Martin_Final)-1):
        data, label = datalist_Martin_Final[i]
        plt.plot( data[:,4], data[:,6],Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7)
    data, label = datalist_Martin_Final[7]
    plt.plot( data[:,0], data[:,2],Symbols[i], color=Colors2[7],label=label ,lw=2,ms=7)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=4,handlelength=2.5)
    plt.title(r'IC and Final',fontsize=20)
    plt.xlabel(r'$\beta$',fontsize=24)
    plt.ylabel(r'$\kappa$',fontsize=24)
    f.savefig(figure_path + 'Overplot_IC_Final.png')

if beta_vs_gamma_plus_kappa:
    f = plt.figure()
    plt.subplot(121)
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        plt.plot( data[:,0], data[:,1] + data[:,2] ,Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    plt.title(r'Initial conditions',fontsize=20)
    plt.xlabel(r'$\beta$',fontsize=24)
    plt.ylabel(r'$\gamma + \kappa$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(122)
    for i in range(len(datalist_Martin_Final)-1):
        data, label = datalist_Martin_Final[i]
        plt.plot( data[:,4], data[:,5] + data[:,6],Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7)
    data, label = datalist_Martin_Final[7]
    plt.plot( data[:,0], data[:,1] + data[:,2],Symbols[i], color=Colors2[7],label=label ,lw=2,ms=7)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)
    plt.title(r'Final products',fontsize=20)
    plt.xlabel(r'$\beta$',fontsize=24)
    plt.ylabel(r'$\gamma + \kappa$',fontsize=24)
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa.png')

# 3D plots of attractor, IC and Final.

if Attractor_3D:
    '''
    f = plt.figure()
    ax = f
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()
    '''
    f  = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    n  = 100
    #for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    for i in range(len(datalist_Martin_IC)):
        data, label = datalist_Martin_IC[i]
        ax.scatter(data[:,0], data[:,1], data[:,2], Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        #plt.plot( data[:,0], data[:,1] + data[:,2] ,Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        # ax.scatter(x, y, z, c=c, marker=m)
    ax.set_xlabel(r'$2 \beta$')
    ax.set_ylabel(r'$\gamma$')
    ax.set_zlabel(r'$\kappa$')
    ax.set_title('3D view of attractor')
    f.savefig(figure_path + 'Attractor_3D.png')

if Time_evolution_beta_gamma_kappa:
    f = plt.figure()
    if A:
        plt.subplot(131)
        for i in range(len(datalist_A)):
            data, label = datalist_A[i]
            plt.plot( data[:,0] , data[:,1] ,Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'$\beta$',fontsize=24)

        plt.subplot(132)
        for i in range(len(datalist_A)):
            data, label = datalist_A[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation A',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'$\gamma$',fontsize=24)
       
        plt.subplot(133)
        for i in range(len(datalist_A)):
            data, label = datalist_A[i]
            plt.plot( data[:,0], data[:,3] ,Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'$\kappa$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'A_Time_evolution_beta_gamma_kappa.png')
    
    if B:           
        plt.subplot(131)
        for i in range(len(datalist_B)):
            data, label = datalist_B[i]
            plt.plot( data[:,0] , data[:,1] ,Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'$\beta$',fontsize=24)

        plt.subplot(132)
        for i in range(len(datalist_B)):
            data, label = datalist_B[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation B',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'$\gamma$',fontsize=24)
       
        plt.subplot(133)
        for i in range(len(datalist_B)):
            data, label = datalist_B[i]
            plt.plot( data[:,0], data[:,3] ,Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'$\kappa$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'B_Time_evolution_beta_gamma_kappa.png')

if Overplot_logr_gamma:
    f = plt.figure() # Plot structures for R = 10000, except for CS1, CS2 and CS3.
    if CS1CS2CS3:
        for i in range(0,6): # Does the same as the line just above: loop over 1.st to 5.th datafile and label.
            data, label = datalist_C_IC[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.title(r'$\gamma $ for CS1, CS2 and CS3',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'$\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'CS1CS2CS3_Overplot_logr_gamma.png')

    if CS4CS5CS6:
        plt.subplot(121)
        # IC
        for i in range(len(datalist_CS4CS5CS6_IC_R10000)):    
            data, label = datalist_CS4CS5CS6_IC_R10000[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        plt.title(r'Time evolution of $\gamma $ for CS4, CS5 and CS6',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Initial $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

        plt.subplot(122)
        # Final
        for i in range(len(datalist_CS4CS5CS6_Final)):
            data, label = datalist_CS4CS5CS6_Final[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for CS4, CS5 and CS6',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'CS4CS5CS6_Overplot_logr_gamma.png')        

    if DS1D2:
        plt.subplot(121)
        # IC
        for i in range(len(datalist_DS1D2_IC_R10000)):
            data, label = datalist_DS1D2_IC_R10000[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color=Colors[i],label=label,lw=2,ms=7)
        plt.title(r'Time evolution of $\gamma $ for DS1 and D2',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Initial $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2,ncol=1,frameon=True,loc=0,handlelength=2.5)

        plt.subplot(122)
        # Final
        for i in range(len(datalist_DS1D2_Final_R10000)):
            data, label = datalist_DS1D2_Final_R10000[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color=Colors[i],label=label,lw=2,ms=7)
        #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for DS1 and D2',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2,ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'DS1D2_Overplot_logr_gamma.png') 

    if BCS4CS5CS6DS1D2:
        plt.subplot(121)
        # IC
        for i in range(len(datalist_CS4CS5CS6_IC_R10000)):               
            data, label = datalist_CS4CS5CS6_IC_R10000[i]
            plt.plot( data[:,0], data[:,2],Symbols[i-3],color=Colors[i-3], label=label,lw=2,ms=7)
        for i in range(0,2):
            data, label = datalist_DS1D2_IC[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color=Colors[i], label=label,lw=2,ms=7)
        data, label = list_of_files_B_IC_R10000[0]
        plt.plot( data[:,0], data[:,2],Symbols[2],color=Colors[2], label=label,lw=2,ms=7)
        
        plt.title(r'Time evolution of $\gamma $ for B, CS4, CS5, CS6, DS1 and D2',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Initial $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        plt.ylim(-5,1)

        # Final
        plt.subplot(122)
        # C
        for i in range(0,3):
            data, label = datalist_C_Final[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        # D
        for i in range(0,2):
            data, label = datalist_DS1D2_Final[i]
            plt.plot( data[:,0], data[:,2],Symbols[i+3],color = Colors[i+3], label=label,lw=2,ms=7)
        # B
        data, label = list_of_files_B_Final_R10000[0]
        plt.plot( data[:,0], data[:,2],Symbols[5],color = Colors[5], label=label,lw=2,ms=7)
        
        #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for DS1 and D2',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        plt.ylim(-5,1)
        f.savefig(figure_path + 'BCS4CS5CS6DS1D2_Overplot_logr_gamma.png')

    if DS1D2_final_evolution:
        # DS1, Run 48 and 49, 50 bins
        plt.subplot(221)
        data, label = datalist_13[0]
        plt.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='DS1, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[0]
        plt.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='DS1, run 49_093',lw=2,ms=7)
        plt.title(r'Time evolution of $\gamma $ for DS1 and D2. 50 bins',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        plt.ylim(-5,1)

        # D2, Run 48 and 49, 50 bins
        plt.subplot(222)
        data, label = datalist_13[1]
        plt.plot( data[:,0], data[:,2],Symbols[2],color = Colors[2], label='D2, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[1]
        plt.plot( data[:,0], data[:,2],Symbols[3],color = Colors[3], label='D2, run 49_093',lw=2,ms=7)
        plt.title(r'50 bins',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        plt.ylim(-5,1)

        # DS1, Run 48 and 49, 20 bins
        plt.subplot(223)
        data, label = datalist_13[2]
        plt.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='DS1, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[2]
        plt.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='DS1, run 49_093',lw=2,ms=7)
        plt.title(r'20 bins',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        plt.ylim(-5,1)

        # D2, Run 48 and 49, 20 bins
        plt.subplot(224)
        data, label = datalist_13[3]
        plt.plot( data[:,0], data[:,2],Symbols[2],color = Colors[2], label='D2, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[3]
        plt.plot( data[:,0], data[:,2],Symbols[3],color = Colors[3], label='D2, run 49_093',lw=2,ms=7)
        plt.title(r'20 bins',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        plt.ylim(-5,1)
        f.savefig(figure_path + 'DS1D2_final_evolution_Overplot_logr_gamma.png')

    if rfp_B:
        data, label = datalist_9b[0]
        plt.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label=label,lw=2,ms=7)
        data, label = datalist_17[0]
        plt.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
        plt.ylim(-4,1)
        plt.title(r'$\gamma$ for B Final product, with bound structure (50 bins)',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'rfp_B_Overplot_logr_gamma.png')

    if rfp_CS4CS5CS6:
        for i in range(0,3):
            data, label = datalist_11[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        for i in range(1,4):
            data, label = datalist_17[i]
            plt.plot( data[:,0], data[:,2],Symbols[i+2],color = Colors[i+2], label=label,lw=2,ms=7)
        plt.ylim(-4,1)
        plt.title(r'$\gamma$ for CS4, CS5 and CS6 Final products, with bound structures (50 bins)',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'rfp_CS4CS5CS6_Overplot_logr_gamma.png')

    if rfp_DS1D2:
        for i in range(0,2):
            data, label = datalist_13b[i]
            plt.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        for i in range(4,6):
            data, label = datalist_17[i]
            plt.plot( data[:,0], data[:,2],Symbols[i-2],color = Colors[i-2], label=label,lw=2,ms=7)
        plt.ylim(-4,1)
        plt.title(r'$\gamma$ for DS1 and D2 Final products, with bound structures (50 bins)',fontsize=20)
        plt.xlabel(r'$\log r$',fontsize=24)
        plt.ylabel(r'Final $\gamma$',fontsize=24)
        plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'rfp_DS1D2_Overplot_logr_gamma.png')

    if rfp_BCS4CS5CS6DS1D2:
        f, (ax1, ax2, ax3) = plt.subplots(3, 1)
        data, label = datalist_9b[0]
        ax1.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label=label,lw=2,ms=7)
        data, label = datalist_17[0]
        ax1.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
        ax1.set_ylim(-4,1)
        ax1.set_title(r'$\gamma$ for Final products, with bound structure (50 bins)',fontsize=20)
        ax1.set_ylabel(r'B',fontsize=24)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.axes.get_xaxis().set_visible(False)

        for i in range(0,3):
            data, label = datalist_11[i]
            ax2.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        for i in range(1,4):
            data, label = datalist_17[i]
            ax2.plot( data[:,0], data[:,2],Symbols[i+2],color = Colors[i+2], label=label,lw=2,ms=7)
        ax2.set_ylim(-4,1)
        ax2.set_ylabel(r'CS4, CS5 and CS6',fontsize=24)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        ax2.axes.get_xaxis().set_visible(False)

        for i in range(0,2):
            data, label = datalist_13b[i]
            ax3.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
        for i in range(4,6):
            data, label = datalist_17[i]
            ax3.plot( data[:,0], data[:,2],Symbols[i-2],color = Colors[i-2], label=label,lw=2,ms=7)
        ax3.set_ylim(-4,1)
        ax3.set_xlabel(r'$\log r$',fontsize=24)
        ax3.set_ylabel(r'DS1 and D2',fontsize=24)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        f.savefig(figure_path + 'rfp_BCS4CS5CS6DS1D2_Overplot_logr_gamma.png')

if Overplot_ln_rdividedbyd3_gamma:
    f = plt.figure()
    # Below are only Final files with 50 radial bins.
    list_of_minima_CS4 = [ (0                    , 'd1'),
                           (0                    , 'd2'),
                           (0                    , 'd3')]
    list_of_maxima_CS4 = [ (0                    , 'p1'),
                           (0                    , 'p2'),
                           (0                    , 'p3')]
    list_of_minima_CS5 = [ (0                    , 'd1'),
                           (0                    , 'd2'),
                           (0                    , 'd3')]
    list_of_maxima_CS5 = [ (0                    , 'p1'),
                           (0                    , 'p2'),
                           (0                    , 'p3')]
    list_of_minima_CS6 = [ (0                    , 'd1'),
                           (0                    , 'd2'),
                           (0                    , 'd3')]
    list_of_maxima_CS6 = [ (0                    , 'p1'),
                           (0                    , 'p2'),
                           (0                    , 'p3')]
    list_of_minima_DS1 = [ (0                    , 'd1'),
                           (0                    , 'd2'),
                           (0                    , 'd3')]
    list_of_maxima_DS1 = [ (0                    , 'p1'),
                           (0                    , 'p2'),
                           (0                    , 'p3')]
    list_of_minima_D2  = [ (0                    , 'd1'),
                           (0                    , 'd2'),
                           (-3.705065011901715444, 'd3')]
    list_of_maxima_D2  = [ (0                    , 'p1'),
                           (0                    , 'p2'),
                           (0                    , 'p3')]

    d_data_CS4    =   [ ( value, label_d ) for value, label_d in list_of_minima_CS4 ]
    d_data_CS5    =   [ ( value, label_d ) for value, label_d in list_of_minima_CS5 ]
    d_data_CS6    =   [ ( value, label_d ) for value, label_d in list_of_minima_CS6 ]
    d_data_DS1    =   [ ( value, label_d ) for value, label_d in list_of_minima_DS1 ]
    d_data_D2     =   [ ( value, label_d ) for value, label_d in list_of_minima_D2  ]

    p_data_CS4    =   [ ( value, label_p ) for value, label_p in list_of_maxima_CS4 ]
    p_data_CS5    =   [ ( value, label_p ) for value, label_p in list_of_maxima_CS5 ]
    p_data_CS6    =   [ ( value, label_p ) for value, label_p in list_of_maxima_CS6 ]
    p_data_DS1    =   [ ( value, label_p ) for value, label_p in list_of_maxima_DS1 ]
    p_data_D2     =   [ ( value, label_p ) for value, label_p in list_of_maxima_D2  ]
        
    #for i in range(0,3):
    data, label    = datalist_6[0]
    value, label_d = d_data_C4[2]
    plt.plot( np.log(data[:,5]/-value), data[:,2],Symbols[0],color = Colors[0], label=label,lw=2,ms=7)
    data, label    = datalist_6[1]
    value, label_d = d_data_C5[2]
    plt.plot( np.log(data[:,5]/-value), data[:,2],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    data, label    = datalist_6[2]
    value, label_d = d_data_C6[2]
    plt.plot( np.log(data[:,5]/-value), data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    #for i in range(0,2):
    data, label    = datalist_8[0]
    value, label_d = d_data_D1[2]
    plt.plot( np.log(data[:,5]/-value), data[:,2],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    data, label    = datalist_8[1]
    value, label_d = d_data_D2[2]
    plt.plot( np.log(data[:,5]/-value), data[:,2],Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    plt.title(r'Final $\gamma $ for CS4, CS5, CS6, DS1 and D2',fontsize=20)
    plt.xlabel(r'$ \log \frac{r}{|d_3|} $',fontsize=24)
    plt.ylabel(r'Final $\gamma$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'Overplot_ln_rdividedbyd3_gamma.png')

if lnr_VR_IC_Final_50bins_20bins:
    f = plt.figure()
    # Initial, 50 bins
    plt.subplot(221)
    for i in range(6,9):    
        data, label = datalist_5[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_7[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    plt.title(r'Time evolution of $v_r $ for Simulation CS4, CS5, CS6, DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Initial $v_r$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    # Final, 50 bins
    plt.subplot(222)
    for i in range(0,3):
        data, label = datalist_6[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_8[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $v_r$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    # Initial, 20 bins
    plt.subplot(223)
    for i in range(9,12):
        data, label = datalist_5[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_7[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Initial $v_r$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    # Final, 20 bins
    plt.subplot(224)
    for i in range(3,6):
        data, label = datalist_6[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_8[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $v_r$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'lnr_VR_IC_Final_50bins_20bins.png')

if lnr_sigmarad2_IC_Final_50bins_20bins:
    f = plt.figure()
    # Initial, 50 bins
    plt.subplot(221)
    for i in range(6,9):    
        data, label = datalist_5[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_7[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    plt.title(r'Time evolution of $\sigma_r^2 $ for Simulation CS4, CS5, CS6, DS1 and D2',fontsize=20) # Include Sim B as well.
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Initial $\sigma_r^2$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    # Final, 50 bins
    plt.subplot(222)
    for i in range(0,3):
        data, label = datalist_6[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_8[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $\sigma_r^2$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    # Initial, 20 bins
    plt.subplot(223)
    for i in range(9,12):
        data, label = datalist_5[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_7[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Initial $ \sigma_r^2 $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    # Final, 20 bins
    plt.subplot(224)
    for i in range(3,6):
        data, label = datalist_6[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_8[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    #plt.title(r'Time evolution of $\beta$, $\gamma $ and $\kappa$ for Simulation DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $ \sigma_r^2 $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'lnr_sigmarad2_IC_Final_50bins_20bins.png')

if lnr_sigmarad2_vr_Final_50bins:
    f = plt.figure()
    plt.subplot(121)
    for i in range(0,3):
        data, label = datalist_6[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_8[i]
        plt.plot( data[:,0], data[:,6],Symbols[i+3],color = Colors[i+3], label=label,lw=2,ms=7)
    data, label = datalist_4[4]
    plt.plot( data[:,0], data[:,6],Symbols[5],color = Colors[5], label=label,lw=2,ms=7)
    plt.title(r'Final $\sigma_r^2 $ for Simulation B, CS4, CS5, CS6, DS1 and D2',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $\sigma_r^2$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(122)
    for i in range(0,3):
        data, label = datalist_6[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_8[i]
        plt.plot( data[:,0], data[:,4],Symbols[i+3],color = Colors[i+3], label=label,lw=2,ms=7)
    data, label = datalist_4[4]
    plt.plot( data[:,0], data[:,4],Symbols[5],color = Colors[5], label=label,lw=2,ms=7)
    plt.title(r'Final $v_r $ for Simulation B, CS4, CS5, CS6, DS1 and D2',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $v_r$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'lnr_sigmarad2_vr_Final_50bins.png')

if R_limit_10000_logr_sigmarad2_vr_Final_20bins:
    f, (ax1, ax2) = plt.subplots(2, 1)
    # CS4,CS5,CS6: datalist_10 (IC), datalist_11 (Final)
    for i in range(3,6):
        data, label = datalist_11[i]
        ax1.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    # DS1,D2: datalist_12 (IC), datalist_13 (Final)
    for i in range(2,4):
        data, label = datalist_13[i]
        ax1.plot( data[:,0], data[:,6],Symbols[i-2],color = Colors[i-2], label=label,lw=2,ms=7)
    # B: datalist_9 (Final)
    data, label = datalist_9[1]
    ax1.plot( data[:,0], data[:,6],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    ax1.set_title(r'Final B, CS4, CS5, CS6, DS1 and D2. $R_{limit} = 10^4$. 20 bins',fontsize=20) 
    ax1.set_ylabel(r'$\sigma_r^2$',fontsize=24)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(3,6):
        data, label = datalist_11[i]
        ax2.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_13[i]
        ax2.plot( data[:,0], data[:,4],Symbols[i-2],color = Colors[i-2], label=label,lw=2,ms=7)
    data, label = datalist_9[1]
    ax2.plot( data[:,0], data[:,4],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    ax2.set_xlabel(r'$\log r$',fontsize=24)
    ax2.set_ylabel(r'$v_r$',fontsize=24)
    ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'R_limit_10000_logr_sigmarad2_vr_Final_20bins.png')

if R_limit_5000_lnr_sigmarad2_vr_Final_50bins:
    f = plt.figure()
    plt.subplot(121)
    # CS4,CS5,CS6: datalist_15 (Final)
    for i in range(0,3):
        data, label = datalist_15[i]
        plt.plot( data[:,0], data[:,6],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    # DS1,D2: datalist_16 (Final)
    for i in range(0,2):
        data, label = datalist_16[i]
        plt.plot( data[:,0], data[:,6],Symbols[i+3],color = Colors[i+3], label=label,lw=2,ms=7)
    # B: datalist_14 (Final)
    data, label = datalist_14[0]
    plt.plot( data[:,0], data[:,6],Symbols[5],color = Colors[5], label=label,lw=2,ms=7)
    plt.title(r'Simulation B, CS4, CS5, CS6, DS1 and D2. $R_{limit} = 5 \cdot 10^3$. 50 bins',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $\sigma_r^2$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(122)
    for i in range(0,3):
        data, label = datalist_15[i]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=label,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_16[i]
        plt.plot( data[:,0], data[:,4],Symbols[i+3],color = Colors[i+3], label=label,lw=2,ms=7)
    data, label = datalist_14[0]
    plt.plot( data[:,0], data[:,4],Symbols[5],color = Colors[5], label=label,lw=2,ms=7)
    #plt.title(r'Final $v_r $ for Simulation B, CS4, CS5, CS6, DS1 and D2',fontsize=20)
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'Final $v_r$',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'R_limit_5000_lnr_sigmarad2_vr_Final_50bins.png')

if R_limit_10000_logr_r_vr_IC_Final_20bins_50bins:
    f = plt.figure()
    plt.subplot(221)
    for i in range(3,6):
        data, label = datalist_11[i]
        a           = label[:-62]
        # print a
        plt.plot( data[:,5], data[:,4],Symbols[i],color = Colors[i], label = a,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_13b[i]
        # data, label = datalist_13[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot( data[:,5], data[:,4],Symbols[i-1],color = Colors[i-1], label = a,lw=2,ms=7)
    data, label = datalist_9[1]
    a           = label[:-57]
    plt.plot( data[:,5], data[:,4],Symbols[0],color = Colors[0], label = a,lw=2,ms=7)
    plt.title(r'Final products, $R_{limit} = 10^4$, 20 bins',fontsize=20) 
    plt.xlabel(r'$ r $',fontsize=24)
    plt.ylabel(r'$ v_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(222)
    for i in range(3,6):
        data, label = datalist_11[i]
        a           = label[:-62]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label = a,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot( data[:,0], data[:,4],Symbols[i-1],color = Colors[i-1], label=a,lw=2,ms=7)
    data, label = datalist_9[1]
    a           = label[:-57]
    plt.plot( data[:,0], data[:,4],Symbols[0],color = Colors[0], label=a,lw=2,ms=7)
    plt.title(r'20 bins',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r' $ v_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(223)
    for i in range(0,3):
        data, label = datalist_11[i]
        a           = label[:-47]
        plt.plot( data[:,5], data[:,4],Symbols[i],color = Colors[i], label = a,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot( data[:,5], data[:,4],Symbols[i+3],color = Colors[i+3], label = a,lw=2,ms=7)
    data, label = datalist_9[0]
    a           = label[:-42]
    plt.plot( data[:,5], data[:,4],Symbols[5],color = Colors[5], label = a,lw=2,ms=7)
    plt.title(r'50 bins',fontsize=20) 
    plt.xlabel(r'$ r $',fontsize=24)
    plt.ylabel(r' $ v_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(224)
    for i in range(0,3):
        data, label = datalist_11[i]
        a           = label[:-47]
        plt.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot( data[:,0], data[:,4],Symbols[i+3],color = Colors[i+3], label=a,lw=2,ms=7)

    data, label = datalist_9[0]
    a           = label[:-42]
    plt.plot( data[:,0], data[:,4],Symbols[5],color = Colors[5], label=a,lw=2,ms=7)
    plt.title(r'50 bins',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'$ v_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'R_limit_10000_logr_r_vr_IC_Final_20bins_50bins.png')

if R_limit_10000_logr_r_ur_Final_20bins_50bins:
    f = plt.figure()
    plt.subplot(221)
    for i in range(3,6):
        data, label = datalist_11[i]
        a = label[:-62]
        plt.plot( data[:,5], data[:,4]/(data[:,6]**.5),Symbols[i],color = Colors[i], label = a,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_13b[i]
        #data, label = datalist_13[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot( data[:,5], data[:,4]/(data[:,6]**.5),Symbols[i-1],color = Colors[i-1], label = a,lw=2,ms=7)
    data, label = datalist_9[1]
    a = label[:-57]
    plt.plot( data[:,5], data[:,4]/(data[:,6]**.5),Symbols[0],color = Colors[0], label = a,lw=2,ms=7)
    plt.title(r'Final products, $R_{limit} = 10^4$, 20 bins',fontsize=20) 
    plt.xlabel(r'$ r $',fontsize=24)
    plt.ylabel(r'$ u_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(222)
    for i in range(3,6):
        data, label = datalist_11[i]
        a = label[:-62]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i],color = Colors[i], label = a,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i-1],color = Colors[i-1], label=a,lw=2,ms=7)
    data, label = datalist_9[1]
    a = label[:-57]
    plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[0],color = Colors[0], label=a,lw=2,ms=7)
    plt.title(r'20 bins',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r' $ u_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(223)
    for i in range(0,3):
        data, label = datalist_11[i]
        a = label[:-47]
        plt.plot( data[:,5], data[:,4]/(data[:,6]**.5),Symbols[i],color = Colors[i], label = a,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot( data[:,5], data[:,4]/(data[:,6]**.5),Symbols[i+3],color = Colors[i+3], label = a,lw=2,ms=7)
    data, label = datalist_9[0]
    a = label[:-42]
    plt.plot( data[:,5], data[:,4]/(data[:,6]**.5),Symbols[5],color = Colors[5], label = a,lw=2,ms=7)
    plt.title(r'50 bins',fontsize=20) 
    plt.xlabel(r'$ r $',fontsize=24)
    plt.ylabel(r' $ u_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(224)
    for i in range(0,3):
        data, label = datalist_11[i]
        a = label[:-47]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i+3],color = Colors[i+3], label=a,lw=2,ms=7)
    data, label = datalist_9[0]
    a = label[:-42]
    plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[5],color = Colors[5], label=a,lw=2,ms=7)
    plt.title(r'50 bins',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'$ u_r $',fontsize=24)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'R_limit_10000_logr_r_ur_Final_20bins_50bins.png')

if R_limit_10000_logr_ur_Final_20bins_50bins:
    # subplot 2,4 are reused from previous figure. changes: datalist9 -> datalist9b, datalist_11 -> ? datalist_11b ?,datalist_13 -> datalist_13b.
    f = plt.figure()
    plt.subplot(121)
    for i in range(3,6):
        data, label = datalist_11[i]
        a           = label[:-62]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i],color = Colors[i], label = a,lw=2,ms=7)
    for i in range(2,4):
        data, label = datalist_13b[i]
        if i == 2:
            a = label[:-62]
        else:
            a = label[:-56]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i-1],color = Colors[i-1], label=a,lw=2,ms=7)
    data, label = datalist_9b[1]
    a           = label[:-57]
    plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[0],color = Colors[0], label=a,lw=2,ms=7)
    plt.title(r'Final products, $R_{limit} = 10^4$, 20 bins',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r' $ u_r $',fontsize=24)
    plt.xlim(-1,2)
    plt.ylim(-.2,.2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)

    plt.subplot(122)
    for i in range(0,3):
        data, label = datalist_11[i]
        a           = label[:-47]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    for i in range(0,2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-47]
        else:
            a = label[:-41]
        plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[i+3],color = Colors[i+3], label=a,lw=2,ms=7)
    data, label = datalist_9b[0]
    a           = label[:-42]
    plt.plot( data[:,0], data[:,4]/(data[:,6]**.5),Symbols[5],color = Colors[5], label=a,lw=2,ms=7)
    plt.title(r'50 bins',fontsize=20) 
    plt.xlabel(r'$\log r$',fontsize=24)
    plt.ylabel(r'$ u_r $',fontsize=24)
    plt.xlim(-1,2)
    plt.ylim(-.2,.2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)
    f.savefig(figure_path + 'R_limit_10000_logr_ur_Final_20bins_50bins.png')

if Overplot_logr_gamma_4_different_bins:
    f, ((ax1, ax5), (ax2, ax6), (ax3, ax7), (ax4, ax8)) = plt.subplots(4, 2)
    if DS1D2:
        data, label = datalist_13[2]
        ax1.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='DS1, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[2]
        ax1.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='DS1, run 49_093',lw=2,ms=7)
        ax1.set_title(r'Time evolution of $\gamma $ for Simulation DS1',fontsize=20)
        ax1.set_ylabel(r'20 bins',fontsize=24)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.set_ylim(-5,1)
        ax1.axes.get_xaxis().set_visible(False)
 
        data, label = datalist_13[0]
        ax2.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='DS1, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[0]
        ax2.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='DS1, run 49_093',lw=2,ms=7)
        ax2.set_ylabel(r'50 bins',fontsize=24)
        ax2.set_ylim(-5,1)
        ax2.axes.get_xaxis().set_visible(False)

        data, label = datalist_13[4]
        ax3.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='DS1, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[4]
        ax3.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='DS1, run 49_093',lw=2,ms=7)
        ax3.set_ylabel(r'100 bins',fontsize=24)
        ax3.set_ylim(-5,1)
        ax3.axes.get_xaxis().set_visible(False)
        
        data, label = datalist_13[6]
        ax4.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='DS1, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[6]
        ax4.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='DS1, run 49_093',lw=2,ms=7)
        ax4.set_ylabel(r'200 bins',fontsize=24)
        ax4.set_ylim(-5,1)

        data, label = datalist_13[3]
        ax5.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='D2, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[3]
        ax5.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='D2, run 49_093',lw=2,ms=7)
        ax5.set_title(r'D2',fontsize=20)
        ax5.set_xlabel(r'$\log r$',fontsize=24)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.set_ylim(-5,1)
        ax5.axes.get_xaxis().set_visible(False)
        ax5.yaxis.tick_right()

        data, label = datalist_13[1]
        ax6.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='D2, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[1]
        ax6.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='D2, run 49_093',lw=2,ms=7)
        ax6.set_xlabel(r'$\log r$',fontsize=24)
        ax6.set_ylim(-5,1)
        ax6.axes.get_xaxis().set_visible(False)
        ax6.yaxis.tick_right()

        data, label = datalist_13[5]
        ax7.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='D2, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[5]
        ax7.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='D2, run 49_093',lw=2,ms=7)
        ax7.set_xlabel(r'$\log r$',fontsize=24)
        ax7.set_ylim(-5,1)
        ax7.axes.get_xaxis().set_visible(False)
        ax7.yaxis.tick_right()

        data, label = datalist_13[7]
        ax8.plot( data[:,0], data[:,2],Symbols[0],color = Colors[0], label='D2, run 48_093',lw=2,ms=7)
        data, label = datalist_13b[7]
        ax8.plot( data[:,0], data[:,2],Symbols[1],color = Colors[1], label='D2, run 49_093',lw=2,ms=7)
        ax8.set_xlabel(r'$\log r$',fontsize=24)
        ax8.set_ylim(-5,1)
        ax8.yaxis.tick_right()
        f.savefig(figure_path + 'Overplot_logr_gamma_4_different_bins.png')

if R_limit_10000_logr_vr_Final_rfp_50bins:
    f, ((ax1, ax4), (ax2, ax5), (ax3, ax6)) = plt.subplots(3, 2)
    data, label = datalist_9b[0]
    a           = label[:-14]
    ax1.plot( data[:,0], data[:,4],Symbols[0],color = Colors[0], label=a,lw=2,ms=7) 
    data, label = datalist_17[0]
    a           = label[:-14]
    ax1.plot( data[:,0], data[:,4],Symbols[1],color = Colors[1], label=a,lw=2,ms=7)
    ax1.set_xlim(-2,4)
    ax1.set_ylim(-.1,.2)
    ax1.set_ylabel(r'B',fontsize=24)
    ax1.set_title(r'Radial velocity, $ v_r $. $R_{limit} = 10^4$, 50 bins',fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(0,3):
        data, label = datalist_11[i]
        a           = label[:-14]
        ax2.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    for i in range(1,4):
        data, label = datalist_17[i]
        a           = label[:-14]
        ax2.plot( data[:,0], data[:,4],Symbols[i+2],color = Colors[i+2], label=a,lw=2,ms=7)
    ax2.set_xlim(-2,4)
    ax2.set_ylim(-.1,.2)
    ax2.set_ylabel(r'CS',fontsize=24)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    ax2.axes.get_xaxis().set_visible(False)

    for i in range(0,2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-14]
        else:
            a = label[:-14]
        ax3.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    for i in range(4,6):
        data, label = datalist_17[i]
        a           = label[:-14]
        ax3.plot( data[:,0], data[:,4],Symbols[i-2],color = Colors[i-2], label=a,lw=2,ms=7)
    ax3.set_xlim(-2,4)
    ax3.set_ylim(-.1,.2)
    ax3.set_ylabel(r'DS1 and D2',fontsize=24)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)

    data, label = datalist_9b[0]
    a           = label[:-14]
    ax4.plot( data[:,0], data[:,4],Symbols[0],color = Colors[0], label=a,lw=2,ms=7)
    data, label = datalist_17[0]
    a           = label[:-14]
    ax4.plot( data[:,0], data[:,4],Symbols[1],color = Colors[1], label=a,lw=2,ms=7)
    ax4.yaxis.tick_right()
    ax4.set_xlim(-1.5,3)
    ax4.set_ylim(-.005,.005)
    ax4.set_title(r'Zoom',fontsize=20)
    ax4.axes.get_xaxis().set_visible(False)
    
    for i in range(0,3):
        data, label = datalist_11[i]
        a           = label[:-14]
        ax5.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    for i in range(1,4):
        data, label = datalist_17[i]
        a           = label[:-14]
        ax5.plot( data[:,0], data[:,4],Symbols[i+2],color = Colors[i+2], label=a,lw=2,ms=7)
    ax5.yaxis.tick_right()
    ax5.set_xlim(-1.5,3)
    ax5.set_ylim(-.005,.005)
    ax5.axes.get_xaxis().set_visible(False)

    for i in range(0,2):
        data, label = datalist_13b[i]
        if i == 0:
            a = label[:-14]
        else:
            a = label[:-14]
        ax6.plot( data[:,0], data[:,4],Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    for i in range(4,6):
        data, label = datalist_17[i]
        a           = label[:-14]
        ax6.plot( data[:,0], data[:,4],Symbols[i-2],color = Colors[i-2], label=a,lw=2,ms=7)
    ax6.yaxis.tick_right()
    ax6.set_xlim(-1.5,3)
    ax6.set_ylim(-.005,.005)
    ax6.set_xlabel(r'$\log r$',fontsize=24)
    f.savefig(figure_path + 'R_limit_10000_logr_vr_Final_rfp_50bins.png')

plt.show()




