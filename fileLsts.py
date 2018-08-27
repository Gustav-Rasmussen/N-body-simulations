#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:30:48 2018

@author: gustavcollinrasmussen
"""

import os

userPath = '/Users/gustavcollinrasmussen/Desktop'
desktopPath = os.getcwd()
GADGET_G_path = desktopPath + 'RunGadget/G_perturbations/'
StablePath = 'G_perturbations/Stable_structures/'
desktopStablePath = desktopPath + StablePath
figurePath = desktopStablePath + 'figures/'
textFilesPath = desktopStablePath + 'text_files/'
MartinPath = 'Martin_IC_and_Final_Edd_and_OM/'
textMartinPath = textFilesPath + MartinPath
hdf5Path = desktopPath + 'G_perturbations/hdf5_files/'
nosyncPath = userPath + 'nosync/RunGadget/'

fileLstMartinIC = [(textMartinPath + 'OMG00_001_IC_000.txt',
                    'OMG00_001_IC_000'),
                   (textMartinPath + '0G00_IC_000.txt', '0G00_IC_000')]
fileLstMartinFinal = [(textMartinPath + '0G20_001.txt', '0G20_001'),
                      (textMartinPath + '00-5G20_001.txt', '00-5G20_001'),
                      (textMartinPath + 'om0-3.5G20_001.txt',
                       'om0-3.5G20_001'),
                      (textMartinPath + 's1G20_001.txt', 's1G20_001'),
                      (textMartinPath + 's2G20_001.txt', 's2G20_001'),
                      (textMartinPath + 's3G20_001.txt', 's3G20_001'),
                      (textMartinPath + 's4G20_001.txt', 's4G20_001')]
# (text_files_path + Martin_path + 'OMG20_Final_000.txt', 'OMG20_Final_000')]
fileLstA = [(textFilesPath + 'A/' + 'A_Hernquist10000_G1.0_0_000.txt',
             'A_Hernquist10000_G1.0_0_000'),
            (textFilesPath + 'A/' + 'A_Hernquist10000_G1.0_5_005.txt',
             'A_Hernquist10000_G1.0_5_005'),
            (textFilesPath + 'A/' + 'A_Hernquist10000_G1.0_10_005.txt',
             'A_Hernquist10000_G1.0_10_005'),
            (textFilesPath + 'A/' + 'A_Hernquist10000_G1.0_40_005.txt',
             'A_Hernquist10000_G1.0_40_005'),
            (textFilesPath + 'A/' + 'A_Hernquist10000_G1.0_48_009.txt',
             'A_Hernquist10000_G1.0_48_008')]
fileLstA_R10000 = [(textFilesPath + 'A/' +
                    'A_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                    'A_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
                   (textFilesPath + 'A/' +
                    'A_Hernquist10000_G1.0_48_009_R_limit_10000_20_radial_bins.txt',
                    'A_Hernquist10000_G1.0_48_009_R_limit_10000_20_radial_bins')]
fileLstB = [(textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_0_000.txt',
             'B_Hernquist10000_G1.0_0_000'),
            (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_5_005.txt',
             'B_Hernquist10000_G1.0_5_005'),
            (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_10_005.txt',
             'B_Hernquist10000_G1.0_10_005'),
            (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_198_000.txt',
             'B_Hernquist10000_G1.0_198_000'),
            (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_198_093.txt',
             'B_Hernquist10000_G1.0_198_093'),
            (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_199_093.txt',
             'B_Hernquist10000_G1.0_199_093')]
fileLstB20 = [(textFilesPath + 'B/' +
               'B_Hernquist10000_G1.0_0_000_20_radial_bins.txt',
               'B_Hernquist10000_G1.0_0_000_20_radial_bins'),
              (textFilesPath + 'B/' +
               'B_Hernquist10000_G1.0_199_093_20_radial_bins.txt',
               'B_Hernquist10000_G1.0_199_093_20_radial_bins')]
# (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_5_005_20_radial_bins.txt', 'B_Hernquist10000_G1.0_5_005_20_radial_bins'),
# (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_10_005_20_radial_bins.txt', 'B_Hernquist10000_G1.0_10_005_20_radial_bins'),
# (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_198_000_20_radial_bins.txt', 'B_Hernquist10000_G1.0_198_000_20_radial_bins'),
# (textFilesPath + 'B/' + 'B_Hernquist10000_G1.0_198_093_20_radial_bins.txt', 'B_Hernquist10000_G1.0_198_093_20_radial_bins')
fileLstB_R10000 = [(textFilesPath + 'B/' + 
                    'B_Hernquist10000_G1.0_0_000_R_limit_10000.txt',
                    'B_Hernquist10000_G1.0_0_000_R_limit_10000'),
                   (textFilesPath + 'B/' +
                    'B_Hernquist10000_G1.0_199_093_R_limit_10000.txt',
                    'B_Hernquist10000_G1.0_199_093_R_limit_10000'),
                   (textFilesPath + 'B/' +
                    'B_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                    'B_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
                   (textFilesPath + 'B/' +
                    'B_Hernquist10000_G1.0_199_093_R_limit_10000_20_radial_bins.txt',
                    'B_Hernquist10000_G1.0_199_093_R_limit_10000_20_radial_bins')]
fileLstC_IC = [(textFilesPath + 'CS1/' +
                'CS1_Osipkov_Merritt10000_G1.0_0_000.txt',
                'CS1_Osipkov_Merritt10000_G1.0_0_000'),
               (textFilesPath + 'CS2/' +
                'CS2_Osipkov_Merritt10000_G1.0_0_000.txt',
                'CS2_Osipkov_Merritt10000_G1.0_0_000'),
               (textFilesPath + 'CS3/' +
                'CS3_Osipkov_Merritt10000_G1.0_0_000.txt',
                'CS3_Osipkov_Merritt10000_G1.0_0_000'),
               (textFilesPath + 'CS1/' +
                'CS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt',
                'CS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'),
               (textFilesPath + 'CS2/' +
                'CS2_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt',
                'CS2_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'),
               (textFilesPath + 'CS3/' +
                'CS3_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt',
                'CS3_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins')]
# (textFilesPath + 'CS4/' + 'CS4_Osipkov_Merritt10000_G1.0_0_000.txt', 'CS4_Osipkov_Merritt10000_G1.0_0_000'),
# (textFilesPath + 'CS5/' + 'CS5_Osipkov_Merritt10000_G1.0_0_000.txt', 'CS5_Osipkov_Merritt10000_G1.0_0_000'),
# (textFilesPath + 'CS6/' + 'CS6_Osipkov_Merritt10000_G1.0_0_000.txt', 'CS6_Osipkov_Merritt10000_G1.0_0_000'),
# (textFilesPath + 'CS4/' + 'CS4_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt', 'CS4_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'),
# (textFilesPath + 'CS5/' + 'CS5_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt', 'CS5_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'),
# (textFilesPath + 'CS6/' + 'CS6_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt', 'CS6_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins')]
fileLstCS4CS5CS6_R10000 = [# (textFilesPath + 'CS4/' + 'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000.txt', 'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000'),
# (textFilesPath + 'CS5/' + 'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000.txt', 'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000'),
# (textFilesPath + 'CS6/' + 'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000.txt', 'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000'),
                           (textFilesPath + 'CS4/' +
                            'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                            'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
                           (textFilesPath + 'CS5/' +
                            'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                            'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
                           (textFilesPath + 'CS6/' +
                            'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                            'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
# (textFilesPath + 'CS4/' + 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000.txt', 'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000'),
# (textFilesPath + 'CS5/' + 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000.txt', 'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000'),
# (textFilesPath + 'CS6/' + 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000.txt', 'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000'),
                           (textFilesPath + 'CS4/' +
                            'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt',
                            'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins'),
                           (textFilesPath + 'CS5/' +
                            'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt',
                            'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins'),
                           (textFilesPath + 'CS6/' +
                            'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins.txt',
                            'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_10000_20_radial_bins')]
fileLstCS4CS5CS6_Final =  [# (textFilesPath + 'CS4/' + 'CS4_Osipkov_Merritt10000_G1.0_48_093.txt', 'CS4_Osipkov_Merritt10000_G1.0_48_093'),
                           # (textFilesPath + 'CS5/' + 'CS5_Osipkov_Merritt10000_G1.0_48_093.txt', 'CS5_Osipkov_Merritt10000_G1.0_48_093'),
                           # (textFilesPath + 'CS6/' + 'CS6_Osipkov_Merritt10000_G1.0_48_093.txt', 'CS6_Osipkov_Merritt10000_G1.0_48_093'),
                           (textFilesPath + 'CS4/' +
                            'CS4_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt',
                            'CS4_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins'),
                           (textFilesPath + 'CS5/' +
                            'CS5_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt',
                            'CS5_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins'),
                           (textFilesPath + 'CS6/' +
                            'CS6_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt',
                            'CS6_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins')]
fileLstDS1D2_IC = [(textFilesPath + 'DS1/' +
                    'DS1_Osipkov_Merritt10000_G1.0_0_000.txt',
                    'DS1_Osipkov_Merritt10000_G1.0_0_000'),
                   (textFilesPath + 'D2/' +
                    'D2_Hernquist10000_G1.0_0_000.txt',
                    'D2_Hernquist10000_G1.0_0_000'),
                   (textFilesPath + 'DS1/' +
                    'DS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins.txt',
                    'DS1_Osipkov_Merritt10000_G1.0_0_000_20_radial_bins'),
                   (textFilesPath + 'D2/' +
                    'D2_Hernquist10000_G1.0_0_000_20_radial_bins.txt',
                    'D2_Hernquist10000_G1.0_0_000_20_radial_bins')]
fileLstDS1D2_Final = [(textFilesPath + 'DS1/' +
                       'DS1_Osipkov_Merritt10000_G1.0_48_093.txt',
                       'DS1_Osipkov_Merritt10000_G1.0_48_093'),
                      (textFilesPath + 'D2/' +
                       'D2_Hernquist10000_G1.0_48_093.txt',
                       'D2_Hernquist10000_G1.0_48_093'),
                      (textFilesPath + 'DS1/' +
                       'DS1_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins.txt',
                       'DS1_Osipkov_Merritt10000_G1.0_48_093_20_radial_bins'),
                      (textFilesPath + 'D2/' +
                       'D2_Hernquist10000_G1.0_48_093_20_radial_bins.txt',
                       'D2_Hernquist10000_G1.0_48_093_20_radial_bins'),
                      (textFilesPath + 'DS1/' +
                       'DS1_Osipkov_Merritt10000_G1.0_49_093.txt',
                       'DS1_Osipkov_Merritt10000_G1.0_49_093'),
                      (textFilesPath + 'D2/' +
                       'D2_Hernquist10000_G1.0_49_093.txt',
                       'D2_Hernquist10000_G1.0_49_093'),
                      (textFilesPath + 'DS1/' +
                       'DS1_Osipkov_Merritt10000_G1.0_49_093_20_radial_bins.txt',
                       'DS1_Osipkov_Merritt10000_G1.0_49_093_20_radial_bins'),
                      (textFilesPath + 'D2/' +
                       'D2_Hernquist10000_G1.0_49_093_20_radial_bins.txt',
                       'D2_Hernquist10000_G1.0_49_093_20_radial_bins')]
fileLstDS1_SoftD2_R10000 = [(textFilesPath + 'DS1/' +
                             'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                             'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
                            (textFilesPath + 'D2/' +
                             'D2_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                             'D2_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
                            # (textFilesPath + 'DS1/' + 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000.txt', 'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000'),
                            # (textFilesPath + 'D2/' + 'D2_Hernquist10000_G1.0_49_093_R_limit_10000.txt', 'D2_Hernquist10000_G1.0_49_093_R_limit_10000'),
                            (textFilesPath + 'DS1/' +
                             'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_20_radial_bins.txt',
                             'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_10000_20_radial_bins'),
                            (textFilesPath + 'D2/' +
                             'D2_Hernquist10000_G1.0_49_093_R_limit_10000_20_radial_bins.txt',
                             'D2_Hernquist10000_G1.0_49_093_R_limit_10000_20_radial_bins')]
fileLstE = [(textFilesPath + 'E/' + 'E_Hernquist10000_G1.0_0_000.txt',
             'E_Hernquist10000_G1.0_0_000'),
            (textFilesPath + 'E/' + 'E_Hernquist10000_G1.0_5_005.txt',
             'E_Hernquist10000_G1.0_5_005'),
            (textFilesPath + 'E/' + 'E_Hernquist10000_G1.0_10_005.txt',
             'E_Hernquist10000_G1.0_10_005'),
            (textFilesPath + 'E/' + 'E_Hernquist10000_G1.0_198_000.txt',
             'E_Hernquist10000_G1.0_198_000'),
            (textFilesPath + 'E/' + 'E_Hernquist10000_G1.0_198_093.txt',
             'E_Hernquist10000_G1.0_198_093')]
fileLstE_R10000 = [(textFilesPath + 'E/' +
                    'E_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins.txt',
                    'E_Hernquist10000_G1.0_0_000_R_limit_10000_20_radial_bins'),
                   (textFilesPath + 'E/' +
                    'E_Hernquist10000_G1.0_198_093_R_limit_10000_20_radial_bins.txt',
                    'E_Hernquist10000_G1.0_198_093_R_limit_10000_20_radial_bins')]
fileLstA_Rlimit32_50bins = [(textFilesPath + 'A/' +
                             'A_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins.txt',
                             'A_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins'),
                            (textFilesPath + 'A/' +
                             'A_Hernquist10000_G1.0_48_009_R_limit_32_50_radial_bins.txt',
                             'A_Hernquist10000_G1.0_48_009_R_limit_32_50_radial_bins')]
fileLstB_Rlimit32_50bins = [(textFilesPath + 'B/' +
                             'B_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins.txt',
                             'B_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins'),
                            (textFilesPath + 'B/' +
                             'B_Hernquist10000_G1.0_199_093_R_limit_32_50_radial_bins.txt',
                             'B_Hernquist10000_G1.0_199_093_R_limit_32_50_radial_bins')]
fileLstCS4_Rlimit32_20bins = [(textFilesPath + 'CS4/' +
                               'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt',
                               'CS4_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'),
                              (textFilesPath + 'CS4/' +
                               'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt',
                               'CS4_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins')]
fileLstCS5_Rlimit32_20bins = [(textFilesPath + 'CS5/' +
                               'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt',
                               'CS5_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'),
                              (textFilesPath + 'CS5/' +
                               'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt',
                               'CS5_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins')]
fileLstCS6_Rlimit32_20bins = [(textFilesPath + 'CS6/' +
                               'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt',
                               'CS6_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'),
                              (textFilesPath + 'CS6/' +
                               'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt',
                               'CS6_Osipkov_Merritt10000_G1.0_48_093_R_limit_32_20_radial_bins.txt')]
fileLstDS1_Rlimit32_20bins = [(textFilesPath + 'DS1/' +
                               'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins.txt',
                               'DS1_Osipkov_Merritt10000_G1.0_0_000_R_limit_32_20_radial_bins'),
                              (textFilesPath + 'DS1/' +
                               'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_32_20_radial_bins.txt',
                               'DS1_Osipkov_Merritt10000_G1.0_49_093_R_limit_32_20_radial_bins')]
fileLstSoftD2_Rlimit32_20bins = [(textFilesPath + 'Soft_D2/' +
                                  'Soft_D2_Hernquist10000_G1.0_0_000_R_limit_32_20_radial_bins.txt',
                                  'Soft_D2_Hernquist10000_G1.0_0_000_R_limit_32_20_radial_bins'),
                                  (textFilesPath + 'Soft_D2/' +
                                  'Soft_D2_Hernquist10000_G1.0_49_093_R_limit_32_20_radial_bins.txt',
                                  'Soft_D2_Hernquist10000_G1.0_49_093_R_limit_32_20_radial_bins')]
fileLstE_Rlimit32_50bins = [(textFilesPath + 'E/' +
                             'E_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins.txt',
                             'E_Hernquist10000_G1.0_0_000_R_limit_32_50_radial_bins'),
                            (textFilesPath + 'E/' +
                             'E_Hernquist10000_G1.0_198_093_R_limit_32_50_radial_bins.txt',
                             'E_Hernquist10000_G1.0_198_093_R_limit_32_50_radial_bins')]
# Bound particles only (rfp). All 50 bins, final products, RLimit10000
fileLstrfp = [(textFilesPath + 'B/' +
               'B_bound_particles_G1.0_200_rfp_093_R_limit_10000.txt',
               'B_bound_particles_G1.0_200_rfp_093_R_limit_10000'),
              (textFilesPath + 'CS4/' +
               'CS4_bound_particles_G1.0_49_rfp_093_R_limit_10000.txt',
               'CS4_bound_particles_G1.0_49_rfp_093_R_limit_10000'),
              (textFilesPath + 'CS5/' +
               'CS5_bound_particles_G1.0_49_rfp_093_R_limit_10000.txt',
               'CS5_bound_particles_G1.0_49_rfp_093_R_limit_10000'),
              (textFilesPath + 'CS6/' +
               'CS6_bound_particles_G1.0_49_rfp_093_R_limit_10000.txt',
               'CS6_bound_particles_G1.0_49_rfp_093_R_limit_10000'),
              (textFilesPath + 'DS1/' +
               'DS1_bound_particles_G1.0_50_rfp_093_R_limit_10000.txt',
               'DS1_bound_particles_G1.0_50_rfp_093_R_limit_10000'),
              (textFilesPath + 'D2/' +
               'D2_bound_particles_G1.0_50_rfp_093_R_limit_10000.txt',
               'D2_bound_particles_G1.0_50_rfp_093_R_limit_10000')]
