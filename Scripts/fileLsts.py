#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:30:48 2018

@author: gustavcollinrasmussen
"""

from definePaths import *

Sparre = ['OMG00_001_IC_000', '0G00_IC_000', '0G20_001', '00-5G20_001',
          'om0-3.5G20_001', 's1G20_001', 's2G20_001', 's3G20_001', 's4G20_001',
          'OMG20_Final_000']

fileLstMartinIC = [(textMartinPath / Sparre[0] + '.txt', Sparre[0]),
                   (textMartinPath / Sparre[1] + '.txt', Sparre[1])]

fileLstMartinFinal = [(textMartinPath / Sparre[2] + '.txt', Sparre[2]),
                      (textMartinPath / Sparre[3] + '.txt', Sparre[3]),
                      (textMartinPath / Sparre[4] + '.txt', Sparre[4]),
                      (textMartinPath / Sparre[5] + '.txt', Sparre[5]),
                      (textMartinPath / Sparre[6] + '.txt', Sparre[6]),
                      (textMartinPath / Sparre[7] + '.txt', Sparre[7]),
                      (textMartinPath / Sparre[8] + '.txt', Sparre[8]),
                      (textMartinPath / Sparre[9] + '.txt', Sparre[9])]

A_lst = ['A_HQ10000_G1.0_0_000', 'A_HQ10000_G1.0_5_005',
         'A_HQ10000_G1.0_10_005', 'A_HQ10000_G1.0_40_005',
         'A_HQ10000_G1.0_48_009']

fileLstA = [(textFilesPath / 'A' / A_lst[0] + '.txt', A_lst[0]),
            (textFilesPath / 'A' / A_lst[1] + '.txt', A_lst[1]),
            (textFilesPath / 'A' / A_lst[2] + '.txt', A_lst[2]),
            (textFilesPath / 'A' / A_lst[3] + '.txt', A_lst[3]),
            (textFilesPath / 'A' / A_lst[4] + '.txt', A_lst[4])]

A_Rlim10000 = ['A_HQ10000_G1.0_0_000_Rlim_10000_20_RBins',
               'A_HQ10000_G1.0_5_005_Rlim_10000_20_RBins',
               'A_HQ10000_G1.0_10_005_Rlim_10000_20_RBins',
               'A_HQ10000_G1.0_40_005_Rlim_10000_20_RBins',
               'A_HQ10000_G1.0_48_009_Rlim_10000_20_RBins']

fileLstA_R10000 = [(textFilesPath / 'A' / A_Rlim10000[0] + '.txt',
                    A_Rlim10000[0]),
                   (textFilesPath / 'A' / A_Rlim10000[1] + '.txt',
                    A_Rlim10000[1]),
                   (textFilesPath / 'A' / A_Rlim10000[2] + '.txt',
                    A_Rlim10000[2]),
                   (textFilesPath / 'A' / A_Rlim10000[3] + '.txt',
                    A_Rlim10000[3]),
                   (textFilesPath / 'A' / A_Rlim10000[4] + '.txt',
                    A_Rlim10000[4])]

FileLstA_Rlimit32_50bins = [(textFilesPath / 'A' /
                             'A_HQ10000_G1.0_0_000_Rlim_32_50_RBins.txt',
                             'A_HQ10000_G1.0_0_000_Rlim_32_50_RBins'),
                            (textFilesPath / 'A' /
                             'A_HQ10000_G1.0_48_009_Rlim_32_50_RBins.txt',
                             'A_HQ10000_G1.0_48_009_Rlim_32_50_RBins')]

fileLstB = [(textFilesPath / 'B' / 'B_HQ10000_G1.0_0_000.txt',
             'B_HQ10000_G1.0_0_000'),
            (textFilesPath / 'B' / 'B_HQ10000_G1.0_5_005.txt',
             'B_HQ10000_G1.0_5_005'),
            (textFilesPath / 'B' / 'B_HQ10000_G1.0_10_005.txt',
             'B_HQ10000_G1.0_10_005'),
            (textFilesPath / 'B' / 'B_HQ10000_G1.0_198_000.txt',
             'B_HQ10000_G1.0_198_000'),
            (textFilesPath / 'B' / 'B_HQ10000_G1.0_198_093.txt',
             'B_HQ10000_G1.0_198_093'),
            (textFilesPath / 'B' / 'B_HQ10000_G1.0_199_093.txt',
             'B_HQ10000_G1.0_199_093')]

fileLstB20 = [(textFilesPath / 'B' / 'B_HQ10000_G1.0_0_000_20_RBins.txt',
               'B_HQ10000_G1.0_0_000_20_RBins'),
              (textFilesPath / 'B' / 'B_HQ10000_G1.0_199_093_20_RBins.txt',
               'B_HQ10000_G1.0_199_093_20_RBins'),
              (textFilesPath / 'B' / 'B_HQ10000_G1.0_5_005_20_RBins.txt',
               'B_HQ10000_G1.0_5_005_20_RBins'),
              (textFilesPath / 'B' / 'B_HQ10000_G1.0_10_005_20_RBins.txt',
               'B_HQ10000_G1.0_10_005_20_RBins'),
              (textFilesPath / 'B' / 'B_HQ10000_G1.0_198_000_20_RBins.txt',
               'B_HQ10000_G1.0_198_000_20_RBins'),
              (textFilesPath / 'B/' / 'B_HQ10000_G1.0_198_093_20_RBins.txt',
               'B_HQ10000_G1.0_198_093_20_RBins')]

fileLstB_R10000 = [(textFilesPath / 'B' /
                    'B_HQ10000_G1.0_0_000_Rlim_10000.txt',
                    'B_HQ10000_G1.0_0_000_Rlim_10000'),
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_198_093_Rlim_10000.txt',
                    'B_HQ10000_G1.0_198_093_Rlim_10000')
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_199_093_Rlim_10000.txt',
                    'B_HQ10000_G1.0_199_093_Rlim_10000'),
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                    'B_HQ10000_G1.0_0_000_Rlim_10000_20_RBins'),
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_5_005_Rlim_10000_20_RBins.txt',
                    'B_HQ10000_G1.0_5_005_Rlim_10000_20_RBins'),
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_10_005_Rlim_10000_20_RBins.txt',
                    'B_HQ10000_G1.0_10_005_Rlim_10000_20_RBins'),
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_198_000_Rlim_10000_20_RBins.txt',
                    'B_HQ10000_G1.0_198_000_Rlim_10000_20_RBins'),
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_198_093_Rlim_10000_20_RBins.txt',
                    'B_HQ10000_G1.0_198_093_Rlim_10000_20_RBins')
                   (textFilesPath / 'B' /
                    'B_HQ10000_G1.0_199_093_Rlim_10000_20_RBins.txt',
                    'B_HQ10000_G1.0_199_093_Rlim_10000_20_RBins')]

FileLstB_SecondLast_R5000 = [(textFilesPath / 'B' /
                              'B_HQ10000_G1.0_198_093_Rlim_5000.txt',
                              'B_HQ10000_G1.0_198_093_Rlim_5000'),
                             (textFilesPath / 'B' /
                              'B_HQ10000_G1.0_198_093_Rlim_5000_20_RBins.txt',
                              'B_HQ10000_G1.0_198_093_Rlim_5000_20_RBins')]

FileLstB_Rlimit32_50bins = [(textFilesPath / 'B' /
                             'B_HQ10000_G1.0_0_000_Rlim_32_50_RBins.txt',
                             'B_HQ10000_G1.0_0_000_Rlim_32_50_RBins'),
                            (textFilesPath / 'B' /
                             'B_HQ10000_G1.0_199_093_Rlim_32_50_RBins.txt',
                             'B_HQ10000_G1.0_199_093_Rlim_32_50_RBins')]

fileLstC_IC = [(textFilesPath / 'CS1' / 'CS1_OM10000_G1.0_0_000.txt',
                'CS1_OM10000_G1.0_0_000'),
               (textFilesPath / 'CS2' / 'CS2_OM10000_G1.0_0_000.txt',
                'CS2_OM10000_G1.0_0_000'),
               (textFilesPath / 'CS3' / 'CS3_OM10000_G1.0_0_000.txt',
                'CS3_OM10000_G1.0_0_000'),
               (textFilesPath / 'CS1' / 'CS1_OM10000_G1.0_0_000_20_RBins.txt',
                'CS1_OM10000_G1.0_0_000_20_RBins'),
               (textFilesPath / 'CS2' / 'CS2_OM10000_G1.0_0_000_20_RBins.txt',
                'CS2_OM10000_G1.0_0_000_20_RBins'),
               (textFilesPath / 'CS3' / 'CS3_OM10000_G1.0_0_000_20_RBins.txt',
                'CS3_OM10000_G1.0_0_000_20_RBins')
               (textFilesPath / 'CS4' / 'CS4_OM10000_G1.0_0_000.txt',
                'CS4_OM10000_G1.0_0_000'),
               (textFilesPath / 'CS5' / 'CS5_OM10000_G1.0_0_000.txt',
                'CS5_OM10000_G1.0_0_000'),
               (textFilesPath / 'CS6' / 'CS6_OM10000_G1.0_0_000.txt',
                'CS6_OM10000_G1.0_0_000'),
               (textFilesPath / 'CS4' / 'CS4_OM10000_G1.0_0_000_20_RBins.txt',
                'CS4_OM10000_G1.0_0_000_20_RBins'),
               (textFilesPath / 'CS5' / 'CS5_OM10000_G1.0_0_000_20_RBins.txt',
                'CS5_OM10000_G1.0_0_000_20_RBins'),
               (textFilesPath / 'CS6' / 'CS6_OM10000_G1.0_0_000_20_RBins.txt',
                'CS6_OM10000_G1.0_0_000_20_RBins')]

fileLstCS4CS5CS6_R10000 = [(textFilesPath / 'CS4' /
                            'CS4_OM10000_G1.0_0_000_Rlim_10000.txt',
                            'CS4_OM10000_G1.0_0_000_Rlim_10000'),
                           (textFilesPath / 'CS5' /
                            'CS5_OM10000_G1.0_0_000_Rlim_10000.txt',
                            'CS5_OM10000_G1.0_0_000_Rlim_10000'),
                           (textFilesPath + 'CS6/' +
                            'CS6_OM10000_G1.0_0_000_Rlim_10000.txt',
                            'CS6_OM10000_G1.0_0_000_Rlim_10000'),
                           (textFilesPath + 'CS4/' +
                            'CS4_OM10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                            'CS4_OM10000_G1.0_0_000_Rlim_10000_20_RBins'),
                           (textFilesPath + 'CS5/' +
                            'CS5_OM10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                            'CS5_OM10000_G1.0_0_000_Rlim_10000_20_RBins'),
                           (textFilesPath + 'CS6/' +
                            'CS6_OM10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                            'CS6_OM10000_G1.0_0_000_Rlim_10000_20_RBins'),
                           (textFilesPath + 'CS4/' +
                            'CS4_OM10000_G1.0_48_093_Rlim_10000.txt',
                            'CS4_OM10000_G1.0_48_093_Rlim_10000'),
                           (textFilesPath + 'CS5/' +
                            'CS5_OM10000_G1.0_48_093_Rlim_10000.txt',
                            'CS5_OM10000_G1.0_48_093_Rlim_10000'),
                           (textFilesPath + 'CS6/' +
                            'CS6_OM10000_G1.0_48_093_Rlim_10000.txt',
                            'CS6_OM10000_G1.0_48_093_Rlim_10000'),
                           (textFilesPath + 'CS4/' +
                            'CS4_OM10000_G1.0_48_093_Rlim_10000_20_RBins.txt',
                            'CS4_OM10000_G1.0_48_093_Rlim_10000_20_RBins'),
                           (textFilesPath + 'CS5/' +
                            'CS5_OM10000_G1.0_48_093_Rlim_10000_20_RBins.txt',
                            'CS5_OM10000_G1.0_48_093_Rlim_10000_20_RBins'),
                           (textFilesPath + 'CS6/' +
                            'CS6_OM10000_G1.0_48_093_Rlim_10000_20_RBins.txt',
                            'CS6_OM10000_G1.0_48_093_Rlim_10000_20_RBins')]

fileLstCS4CS5CS6_Final = [(textFilesPath + 'CS4/' +
                           'CS4_OM10000_G1.0_48_093.txt',
                           'CS4_OM10000_G1.0_48_093'),
                          (textFilesPath + 'CS5/' +
                           'CS5_OM10000_G1.0_48_093.txt',
                           'CS5_OM10000_G1.0_48_093'),
                          (textFilesPath + 'CS6/' +
                           'CS6_OM10000_G1.0_48_093.txt',
                           'CS6_OM10000_G1.0_48_093'),
                          (textFilesPath + 'CS4/' +
                           'CS4_OM10000_G1.0_48_093_20_RBins.txt',
                           'CS4_OM10000_G1.0_48_093_20_RBins'),
                          (textFilesPath + 'CS5/' +
                           'CS5_OM10000_G1.0_48_093_20_RBins.txt',
                           'CS5_OM10000_G1.0_48_093_20_RBins'),
                          (textFilesPath + 'CS6/' +
                           'CS6_OM10000_G1.0_48_093_20_RBins.txt',
                           'CS6_OM10000_G1.0_48_093_20_RBins')]

FileLstCS4CS5CS6_Final_R5000 = [(textFilesPath + 'CS4/' +
                                 'CS4_OM10000_G1.0_48_093_Rlim_5000.txt',
                                 'CS4_OM10000_G1.0_48_093_Rlim_5000'),
                                (textFilesPath + 'CS5/' +
                                 'CS5_OM10000_G1.0_48_093_Rlim_5000.txt',
                                 'CS5_OM10000_G1.0_48_093_Rlim_5000'),
                                (textFilesPath + 'CS6/' +
                                 'CS6_OM10000_G1.0_48_093_Rlim_5000.txt',
                                 'CS6_OM10000_G1.0_48_093_Rlim_5000'),
                                (textFilesPath + 'CS4/' +
                                 'CS4_OM10000_G1.0_48_093_Rlim5000_20RBins.txt',
                                 'CS4_OM10000_G1.0_48_093_Rlim5000_20RBins'),
                                (textFilesPath + 'CS5/' +
                                 'CS5_OM10000_G1.0_48_093_Rlim5000_20RBins.txt',
                                 'CS5_OM10000_G1.0_48_093_Rlim5000_20RBins'),
                                (textFilesPath + 'CS6/' +
                                 'CS6_OM10000_G1.0_48_093_Rlim5000_20RBins.txt',
                                 'CS6_OM10000_G1.0_48_093_Rlim5000_20RBins')]

FileLstCS4_Rlimit32_20bins = [(textFilesPath + 'CS4/' +
                               'CS4_OM10000_G1.0_0_000_Rlim_32_20_RBins.txt',
                               'CS4_OM10000_G1.0_0_000_Rlim_32_20_RBins'),
                              (textFilesPath + 'CS4/' +
                               'CS4_OM10000_G1.0_48_093_Rlim_32_20_RBins.txt',
                               'CS4_OM10000_G1.0_48_093_Rlim_32_20_RBins')]

FileLstCS5_Rlimit32_20bins = [(textFilesPath + 'CS5/' +
                               'CS5_OM10000_G1.0_0_000_Rlim_32_20_RBins.txt',
                               'CS5_OM10000_G1.0_0_000_Rlim_32_20_RBins'),
                              (textFilesPath + 'CS5/' +
                               'CS5_OM10000_G1.0_48_093_Rlim_32_20_RBins.txt',
                               'CS5_OM10000_G1.0_48_093_Rlim_32_20_RBins')]

FileLstCS6_Rlimit32_20bins = [(textFilesPath + 'CS6/' +
                               'CS6_OM10000_G1.0_0_000_Rlim_32_20_RBins.txt',
                               'CS6_OM10000_G1.0_0_000_Rlim_32_20_RBins'),
                              (textFilesPath + 'CS6/' +
                               'CS6_OM10000_G1.0_48_093_Rlim_32_20_RBins.txt',
                               'CS6_OM10000_G1.0_48_093_Rlim_32_20_RBins.txt')]

FileLstDS1D2_IC_R10000 = [(textFilesPath + 'DS1/' +
                           'DS1_OM10000_G1.0_0_000_Rlim_10000.txt',
                           'DS1_OM10000_G1.0_0_000_Rlim_10000'),
                          (textFilesPath + 'D2/' +
                           'D2_HQ10000_G1.0_0_000_Rlim_10000.txt',
                           'D2_HQ10000_G1.0_0_000_Rlim_10000'),
                          (textFilesPath + 'DS1/' +
                           'DS1_OM10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                           'DS1_OM10000_G1.0_0_000_Rlim_10000_20_RBins'),
                          (textFilesPath + 'D2/' +
                           'D2_HQ10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                           'D2_HQ10000_G1.0_0_000_Rlim_10000_20_RBins')]

fileLstDS1D2_IC = [(textFilesPath + 'DS1/' + 'DS1_OM10000_G1.0_0_000.txt',
                    'DS1_OM10000_G1.0_0_000'),
                   (textFilesPath + 'D2/' + 'D2_HQ10000_G1.0_0_000.txt',
                    'D2_HQ10000_G1.0_0_000'),
                   (textFilesPath + 'DS1/' +
                    'DS1_OM10000_G1.0_0_000_20_RBins.txt',
                    'DS1_OM10000_G1.0_0_000_20_RBins'),
                   (textFilesPath + 'D2/' +
                    'D2_HQ10000_G1.0_0_000_20_RBins.txt',
                    'D2_HQ10000_G1.0_0_000_20_RBins')]

FileLstDS1D2_SecondLast_R5000 = [(textFilesPath + 'DS1/' +
                                  'DS1_OM10000_G1.0_48_093_Rlim_5000.txt',
                                  'DS1_OM10000_G1.0_48_093_Rlim_5000'),
                                 (textFilesPath + 'D2/' +
                                  'D2_HQ10000_G1.0_48_093_Rlim_5000.txt',
                                  'D2_HQ10000_G1.0_48_093_Rlim_5000'),
                                 (textFilesPath + 'DS1/' +
                                  'DS1_OM10000_G1.0_48_093_Rlim5000_20RBins.txt',
                                  'DS1_OM10000_G1.0_48_093_Rlim5000_20RBins'),
                                 (textFilesPath + 'D2/' +
                                  'D2_HQ10000_G1.0_48_093_Rlim5000_20RBins.txt',
                                  'D2_HQ10000_G1.0_48_093_Rlim5000_20RBins')]

fileLstDS1D2_Final = [(textFilesPath + 'DS1/' + 'DS1_OM10000_G1.0_48_093.txt',
                       'DS1_OM10000_G1.0_48_093'),
                      (textFilesPath + 'D2/' + 'D2_HQ10000_G1.0_48_093.txt',
                       'D2_HQ10000_G1.0_48_093'),
                      (textFilesPath + 'DS1/' +
                       'DS1_OM10000_G1.0_48_093_20_RBins.txt',
                       'DS1_OM10000_G1.0_48_093_20_RBins'),
                      (textFilesPath + 'D2/' +
                       'D2_HQ10000_G1.0_48_093_20_RBins.txt',
                       'D2_HQ10000_G1.0_48_093_20_RBins'),
                      (textFilesPath + 'DS1/' + 'DS1_OM10000_G1.0_49_093.txt',
                       'DS1_OM10000_G1.0_49_093'),
                      (textFilesPath + 'D2/' + 'D2_HQ10000_G1.0_49_093.txt',
                       'D2_HQ10000_G1.0_49_093'),
                      (textFilesPath + 'DS1/' +
                       'DS1_OM10000_G1.0_49_093_20_RBins.txt',
                       'DS1_OM10000_G1.0_49_093_20_RBins'),
                      (textFilesPath + 'D2/' +
                       'D2_HQ10000_G1.0_49_093_20_RBins.txt',
                       'D2_HQ10000_G1.0_49_093_20_RBins')]

fileLstDS1_SoftD2_R10000 = [(textFilesPath + 'DS1/' +
                             'DS1_OM10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                             'DS1_OM10000_G1.0_0_000_Rlim_10000_20_RBins'),
                            (textFilesPath + 'D2/' +
                             'D2_HQ10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                             'D2_HQ10000_G1.0_0_000_Rlim_10000_20_RBins'),
                            (textFilesPath + 'DS1/' +
                             'DS1_OM10000_G1.0_49_093_Rlim_10000.txt',
                             'DS1_OM10000_G1.0_49_093_Rlim_10000'),
                            (textFilesPath + 'D2/' +
                             'D2_HQ10000_G1.0_49_093_Rlim_10000.txt',
                             'D2_HQ10000_G1.0_49_093_Rlim_10000'),
                            (textFilesPath + 'DS1/' +
                             'DS1_OM10000_G1.0_49_093_Rlim_10000_20_RBins.txt',
                             'DS1_OM10000_G1.0_49_093_Rlim_10000_20_RBins'),
                            (textFilesPath + 'D2/' +
                             'D2_HQ10000_G1.0_49_093_Rlim_10000_20_RBins.txt',
                             'D2_HQ10000_G1.0_49_093_Rlim_10000_20_RBins'),
                            (textFilesPath + 'DS1/' +
                             'DS1_OM10000_G1.0_49_093_Rlim10000_100RBins.txt',
                             'DS1_OM10000_G1.0_49_093_Rlim10000_100RBins'),
                            (textFilesPath + 'D2/' +
                             'D2_HQ10000_G1.0_49_093_Rlim_10000_100_RBins.txt',
                             'D2_HQ10000_G1.0_49_093_Rlim_10000_100_RBins'),
                            (textFilesPath + 'DS1/' +
                             'DS1_OM10000_G1.0_49_093_Rlim10000_200RBins.txt',
                             'DS1_OM10000_G1.0_49_093_Rlim10000_200RBins'),
                            (textFilesPath + 'D2/' +
                             'D2_HQ10000_G1.0_49_093_Rlim_10000_200_RBins.txt',
                             'D2_HQ10000_G1.0_49_093_Rlim_10000_200_RBins')]

FileLstDS1D2_SecondLast_R10000 = [(textFilesPath + 'DS1/' +
                                   'DS1_OM10000_G1.0_48_093_Rlim_10000.txt',
                                   'DS1_OM10000_G1.0_48_093_Rlim_10000'),
                                  (textFilesPath + 'D2/' +
                                   'D2_HQ10000_G1.0_48_093_Rlim_10000.txt',
                                   'D2_HQ10000_G1.0_48_093_Rlim_10000'),
                                  (textFilesPath + 'DS1/' +
                                   'DS1_OM10000_G1.0_48_093_Rlim10000_20RBins.txt',
                                   'DS1_OM10000_G1.0_48_093_Rlim10000_20RBins'),
                                  (textFilesPath + 'D2/' +
                                   'D2_HQ10000_G1.0_48_093_Rlim10000_20RBins.txt',
                                   'D2_HQ10000_G1.0_48_093_Rlim10000_20RBins'),
                                  (textFilesPath + 'DS1/' +
                                   'DS1_OM10000_G1.0_48_093_Rlim10000_100RBins.txt',
                                   'DS1_OM10000_G1.0_48_093_Rlim10000_100RBins'),
                                  (textFilesPath + 'D2/' +
                                   'D2_HQ10000_G1.0_48_093_Rlim10000_100RBins.txt',
                                   'D2_HQ10000_G1.0_48_093_Rlim10000_100RBins'),
                                  (textFilesPath + 'DS1/' +
                                   'DS1_OM10000_G1.0_48_093_Rlim10000_200RBins.txt',
                                   'DS1_OM10000_G1.0_48_093_Rlim10000_200RBins'),
                                  (textFilesPath + 'D2/' +
                                   'D2_HQ10000_G1.0_48_093_Rlim10000_200RBins.txt',
                                   'D2_HQ10000_G1.0_48_093_Rlim10000_200RBins')
                                  ]

FileLstDS1_Rlimit32_20bins = [(textFilesPath + 'DS1/' +
                               'DS1_OM10000_G1.0_0_000_Rlim_32_20_RBins.txt',
                               'DS1_OM10000_G1.0_0_000_Rlim_32_20_RBins'),
                              (textFilesPath + 'DS1/' +
                               'DS1_OM10000_G1.0_49_093_Rlim_32_20_RBins.txt',
                               'DS1_OM10000_G1.0_49_093_Rlim_32_20_RBins')]

FileLstSoft_D2_Rlimit32_20bins = [(textFilesPath + 'Soft_D2/' +
                                   'Soft_D2_HQ10000_G1.0_0_000_Rlim32_20RBins.txt',
                                   'Soft_D2_HQ10000_G1.0_0_000_Rlim32_20RBins'),
                                  (textFilesPath + 'Soft_D2/' +
                                   'Soft_D2_HQ10000_G1.0_49_093_Rlim32_20RBins.txt',
                                   'Soft_D2_HQ10000_G1.0_49_093_Rlim32_20RBins')
                                  ]

fileLstE = [(textFilesPath + 'E/' + 'E_HQ10000_G1.0_0_000.txt',
             'E_HQ10000_G1.0_0_000'),
            (textFilesPath + 'E/' + 'E_HQ10000_G1.0_5_005.txt',
             'E_HQ10000_G1.0_5_005'),
            (textFilesPath + 'E/' + 'E_HQ10000_G1.0_10_005.txt',
             'E_HQ10000_G1.0_10_005'),
            (textFilesPath + 'E/' + 'E_HQ10000_G1.0_198_000.txt',
             'E_HQ10000_G1.0_198_000'),
            (textFilesPath + 'E/' + 'E_HQ10000_G1.0_198_093.txt',
             'E_HQ10000_G1.0_198_093')]

fileLstE_R10000 = [(textFilesPath + 'E/' +
                    'E_HQ10000_G1.0_0_000_Rlim_10000_20_RBins.txt',
                    'E_HQ10000_G1.0_0_000_Rlim_10000_20_RBins'),
                   (textFilesPath + 'E/' +
                    'E_HQ10000_G1.0_198_093_Rlim_10000_20_RBins.txt',
                    'E_HQ10000_G1.0_198_093_Rlim_10000_20_RBins')]

FileLstE_Rlimit32_50bins = [(textFilesPath + 'E/' +
                             'E_HQ10000_G1.0_0_000_Rlim_32_50_RBins.txt',
                             'E_HQ10000_G1.0_0_000_Rlim_32_50_RBins'),
                            (textFilesPath + 'E/' +
                             'E_HQ10000_G1.0_198_093_Rlim_32_50_RBins.txt',
                             'E_HQ10000_G1.0_198_093_Rlim_32_50_RBins')]

# ----------------------------------------------------------------------

# Bound particles only (rfp). All 50 bins, final products, RLimit10000
fileLstrfp = [(textFilesPath + 'B/' +
               'B_bound_particles_G1.0_200_rfp_093_Rlim_10000.txt',
               'B_bound_particles_G1.0_200_rfp_093_Rlim_10000'),
              (textFilesPath + 'CS4/' +
               'CS4_bound_particles_G1.0_49_rfp_093_Rlim_10000.txt',
               'CS4_bound_particles_G1.0_49_rfp_093_Rlim_10000'),
              (textFilesPath + 'CS5/' +
               'CS5_bound_particles_G1.0_49_rfp_093_Rlim_10000.txt',
               'CS5_bound_particles_G1.0_49_rfp_093_Rlim_10000'),
              (textFilesPath + 'CS6/' +
               'CS6_bound_particles_G1.0_49_rfp_093_Rlim_10000.txt',
               'CS6_bound_particles_G1.0_49_rfp_093_Rlim_10000'),
              (textFilesPath + 'DS1/' +
               'DS1_bound_particles_G1.0_50_rfp_093_Rlim_10000.txt',
               'DS1_bound_particles_G1.0_50_rfp_093_Rlim_10000'),
              (textFilesPath + 'D2/' +
               'D2_bound_particles_G1.0_50_rfp_093_Rlim_10000.txt',
               'D2_bound_particles_G1.0_50_rfp_093_Rlim_10000')]
