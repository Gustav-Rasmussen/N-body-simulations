#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:30:48 2018

@author: gustavcollinrasmussen
"""

from definePaths import *

Sparre = ['OMG00_001_IC_000', '0G00_IC_000', '0G20_001', '00-5G20_001',
          'om0-3.5G20_001', 's1G20_001', 's2G20_001', 's3G20_001',
          's4G20_001', 'OMG20_Final_000']

fileLstMartinIC = [(textMartinPath / Sparre[i] + '.txt', Sparre[i])
                   for i in range(2)]

fileLstMartinFinal = [(textMartinPath / Sparre[i] + '.txt', Sparre[i])
                      for i in range(2, 10)]

A_pre = 'A_HQ10000_G1.0_'
A_post = ['0_000', '5_005', '10_005', '40_005', '48_009']
A_lst = [A_pre + i for i in A_post]
fileLstA = [(textFilesPath / 'A' / A_lst[i] + '.txt', A_lst[i])
            for i in range(5)]

A_Rlim10000 = [A_lst[i] + '_Rlim_10000_20_RBins' for i in range(5)]
fileLstA_R10000 = [(textFilesPath / 'A' / A_Rlim10000[i] + '.txt',
                    A_Rlim10000[i]) for i in range(5)]

post = '_Rlim_32_50_RBins'
A_Rlim32 = [A_pre + '0_000' + post, A_pre + '48_009' + post]
FileLstA_Rlimit32_50bins = [(textFilesPath / 'A' / A_Rlim32[i] + '.txt',
                             A_Rlim32[i]) for i in range(2)]

B_pre = 'B_HQ10000_G1.0_'
B_post = ['0_000', '5_005', '10_005', '198_000', '198_093', '199_093']
B_lst = [B_pre + i for i in B_post]
fileLstB = [(textFilesPath / 'B' / B_lst[i] + '.txt', B_lst[i])
            for i in range(6)]

Bin_str = '_20_RBins'
snaps = ['0_000', '199_093', '5_005', '10_005', '198_000', '198_093']
B20 = [B_pre + snap + Bin_str for snap in snaps]
fileLstB20 = [(textFilesPath / 'B' / B20[i] + '.txt', B20[i])
              for i in range(6)]

R_str = '_Rlim_10000'
snaps = ['0_000', '198_093', '199_093', '0_000', '5_005', '10_005', '198_000',
         '198_093', '199_093']
B_R10000 = [B_pre + snap + R_str for snap in snaps]
for i in range(3, 9):
    B_R10000[i] = B_R10000[i] + Bin_str

fileLstB_R10000 = [(textFilesPath / 'B' / B_R10000[i] + '.txt', B_R10000[i])
                   for i in range(9)]

snapLim = '198_093_Rlim_5000'
B_R5000 = [B_pre + snapLim, B_pre + snapLim + Bin_str]

FileLstB_SecondLast_R5000 = [(textFilesPath / 'B' / B_R5000[i] + '.txt',
                              B_R5000[i]) for i in range(2)]

RBin = '_Rlim_32_50_RBins'
B_R32 = [B_pre + '0_000' + RBin, B_pre + '199_093' + RBin]

FileLstB_Rlimit32_50bins = [(textFilesPath / 'B' / B_R32[i] + '.txt',
                             B_R32[i]) for i in range(2)]

OM_str = '_OM10000_G1.0_0_000'
IC = ['CS1' + OM_str,
      'CS2' + OM_str,
      'CS3' + OM_str,
      'CS1' + OM_str + Bin_str,
      'CS2' + OM_str + Bin_str,
      'CS3' + OM_str + Bin_str,
      'CS4' + OM_str,
      'CS5' + OM_str,
      'CS6' + OM_str,
      'CS4' + OM_str + Bin_str,
      'CS5' + OM_str + Bin_str,
      'CS6' + OM_str + Bin_str]

fileLstC_IC = [(textFilesPath / 'CS1' / IC[0] + '.txt', IC[0]),
               (textFilesPath / 'CS2' / IC[1] + '.txt', IC[1]),
               (textFilesPath / 'CS3' / IC[2] + '.txt', IC[2]),
               (textFilesPath / 'CS1' / IC[3] + '.txt', IC[3]),
               (textFilesPath / 'CS2' / IC[4] + '.txt', IC[4]),
               (textFilesPath / 'CS3' / IC[5] + '.txt', IC[5]),
               (textFilesPath / 'CS4' / IC[6] + '.txt', IC[6]),
               (textFilesPath / 'CS5' / IC[7] + '.txt', IC[7]),
               (textFilesPath / 'CS6' / IC[8] + '.txt', IC[8]),
               (textFilesPath / 'CS4' / IC[9] + '.txt', IC[9]),
               (textFilesPath / 'CS5' / IC[10] + '.txt', IC[10]),
               (textFilesPath / 'CS6' / IC[11] + '.txt', IC[11])]

OM_48 = '_OM10000_G1.0_48_093'
CS = ['CS4' + OM_str + R_str,
      'CS5' + OM_str + R_str,
      'CS6' + OM_str + R_str,
      'CS4' + OM_str + R_str + Bin_str,
      'CS5' + OM_str + R_str + Bin_str,
      'CS6' + OM_str + R_str + Bin_str,
      'CS4' + OM_48 + R_str,
      'CS5' + OM_48 + R_str,
      'CS6' + OM_48 + R_str,
      'CS4' + OM_48 + R_str + Bin_str,
      'CS5' + OM_48 + R_str + Bin_str,
      'CS6' + OM_48 + R_str + Bin_str]

fileLstCS4CS5CS6_R10000 = [(textFilesPath / 'CS4' / CS[0] + '.txt', CS[0]),
                           (textFilesPath / 'CS5' / CS[1] + '.txt', CS[1]),
                           (textFilesPath + 'CS6/' + CS[2] + '.txt', CS[2]),
                           (textFilesPath + 'CS4/' + CS[3] + '.txt', CS[3]),
                           (textFilesPath + 'CS5/' + CS[4] + '.txt', CS[4]),
                           (textFilesPath + 'CS6/' + CS[5] + '.txt', CS[5]),
                           (textFilesPath + 'CS4/' + CS[6] + '.txt', CS[6]),
                           (textFilesPath + 'CS5/' + CS[7] + '.txt', CS[7]),
                           (textFilesPath + 'CS6/' + CS[8] + '.txt', CS[8]),
                           (textFilesPath + 'CS4/' + CS[9] + '.txt', CS[9]),
                           (textFilesPath + 'CS5/' + CS[10] + '.txt', CS[10]),
                           (textFilesPath + 'CS6/' + CS[11] + '.txt', CS[11])]

fileLstCS4CS5CS6_Final = [(textFilesPath + 'CS4/' + 'CS4' + OM_48 + '.txt',
                           'CS4' + OM_48),
                          (textFilesPath + 'CS5/' + 'CS5' + OM_48 + '.txt',
                           'CS5' + OM_48),
                          (textFilesPath + 'CS6/' + 'CS6' + OM_48 + '.txt',
                           'CS6' + OM_48),
                          (textFilesPath + 'CS4/' + 'CS4' + OM_48 + Bin_str
                           + '.txt', 'CS4' + OM_48 + Bin_str),
                          (textFilesPath + 'CS5/' + 'CS5' + OM_48 + Bin_str
                           + '.txt', 'CS5' + OM_48 + Bin_str),
                          (textFilesPath + 'CS6/' + 'CS6' + OM_48 + Bin_str
                           + '.txt', 'CS6' + OM_48 + Bin_str)]

FileLstCS4CS5CS6_Final_R5000 = [(textFilesPath + 'CS4/' +
                                 'CS4' + OM_48 + '_Rlim_5000.txt',
                                 'CS4' + OM_48 + '_Rlim_5000'),
                                (textFilesPath + 'CS5/' +
                                 'CS5' + OM_48 + '_Rlim_5000.txt',
                                 'CS5' + OM_48 + '_Rlim_5000'),
                                (textFilesPath + 'CS6/' +
                                 'CS6' + OM_48 + '_Rlim_5000.txt',
                                 'CS6' + OM_48 + '_Rlim_5000'),
                                (textFilesPath + 'CS4/' +
                                 'CS4' + OM_48 + '_Rlim5000_20RBins.txt',
                                 'CS4' + OM_48 + '_Rlim5000_20RBins'),
                                (textFilesPath + 'CS5/' +
                                 'CS5' + OM_48 + '_Rlim5000_20RBins.txt',
                                 'CS5' + OM_48 + '_Rlim5000_20RBins'),
                                (textFilesPath + 'CS6/' +
                                 'CS6' + OM_48 + '_Rlim5000_20RBins.txt',
                                 'CS6' + OM_48 + '_Rlim5000_20RBins')]

RBin = '_Rlim_32_20_RBins'
FileLstCS4_Rlimit32_20bins = [(textFilesPath + 'CS4/' +
                               'CS4' + OM_str + RBin + '.txt',
                               'CS4' + OM_str + RBin),
                              (textFilesPath + 'CS4/' +
                               'CS4' + OM_48 + RBin + '.txt',
                               'CS4' + OM_48 + RBin)]

FileLstCS5_Rlimit32_20bins = [(textFilesPath + 'CS5/' +
                               'CS5' + OM_str + RBin + '.txt',
                               'CS5' + OM_str + RBin),
                              (textFilesPath + 'CS5/' +
                               'CS5' + OM_48 + RBin + '.txt',
                               'CS5' + OM_48 + RBin)]

FileLstCS6_Rlimit32_20bins = [(textFilesPath + 'CS6/' +
                               'CS6' + OM_str + RBin + '.txt',
                               'CS6' + OM_str + RBin),
                              (textFilesPath + 'CS6/' +
                               'CS6' + OM_48 + RBin + '.txt',
                               'CS6' + OM_48 + RBin + '.txt')]

HQ_str = '_HQ10000_G1.0_0_000'
RBin = '_Rlim_10000_20_RBins'
FileLstDS1D2_IC_R10000 = [(textFilesPath + 'DS1/' +
                           'DS1' + OM_str + '_Rlim_10000.txt',
                           'DS1' + OM_str + '_Rlim_10000'),
                          (textFilesPath + 'D2/' +
                           'D2' + HQ_str + '_Rlim_10000.txt',
                           'D2' + HQ_str + '_Rlim_10000'),
                          (textFilesPath + 'DS1/' +
                           'DS1' + OM_str + RBin + '.txt',
                           'DS1' + OM_str + RBin),
                          (textFilesPath + 'D2/' +
                           'D2' + HQ_str + RBin + '.txt', 'D2' + HQ_str + RBin)
                          ]

fileLstDS1D2_IC = [(textFilesPath + 'DS1/' + 'DS1' + OM_str + '.txt',
                    'DS1' + OM_str),
                   (textFilesPath + 'D2/' + 'D2' + HQ_str + '.txt',
                    'D2' + HQ_str),
                   (textFilesPath + 'DS1/' + 'DS1' + OM_str + '_20_RBins.txt',
                    'DS1' + OM_str + '_20_RBins'),
                   (textFilesPath + 'D2/' + 'D2' + HQ_str + '_20_RBins.txt',
                    'D2' + HQ_str + '_20_RBins')]

HQ_48 = '_HQ10000_G1.0_48_093'
RBin = '_Rlim5000_20RBins'
FileLstDS1D2_SecondLast_R5000 = [(textFilesPath + 'DS1/' +
                                  'DS1' + OM_48 + '_Rlim_5000.txt',
                                  'DS1' + OM_48 + '_Rlim_5000'),
                                 (textFilesPath + 'D2/' +
                                  'D2' + HQ_48 + '_Rlim_5000.txt',
                                  'D2' + HQ_48 + '_Rlim_5000'),
                                 (textFilesPath + 'DS1/' +
                                  'DS1' + OM_48 + RBin + '.txt',
                                  'DS1' + OM_48 + RBin),
                                 (textFilesPath + 'D2/' +
                                  'D2' + HQ_48 + RBin + '.txt',
                                  'D2' + HQ_48 + RBin)]

OM_49 = '_OM10000_G1.0_49_093'
HQ_49 = '_HQ10000_G1.0_49_093'
fileLstDS1D2_Final = [(textFilesPath + 'DS1/' + 'DS1' + OM_48 + '.txt',
                       'DS1' + OM_48),
                      (textFilesPath + 'D2/' + 'D2' + HQ_48 + '.txt',
                       'D2' + HQ_48),
                      (textFilesPath + 'DS1/' +
                       'DS1' + OM_48 + '_20_RBins.txt',
                       'DS1' + OM_48 + '_20_RBins'),
                      (textFilesPath + 'D2/' +
                       'D2' + HQ_48 + '_20_RBins.txt',
                       'D2' + HQ_48 + '_20_RBins'),
                      (textFilesPath + 'DS1/' + 'DS1' + OM_49 + '.txt',
                       'DS1' + OM_49),
                      (textFilesPath + 'D2/' + 'D2' + HQ_49 + '.txt',
                       'D2' + HQ_49),
                      (textFilesPath + 'DS1/' + 'DS1' + OM_49
                       + '_20_RBins.txt', 'DS1' + OM_49 + '_20_RBins'),
                      (textFilesPath + 'D2/' + 'D2' + HQ_49 + '_20_RBins.txt',
                       'D2' + HQ_49 + '_20_RBins')]

RBin = '_Rlim_10000_20_RBins'
fileLstDS1_SoftD2_R10000 = [(textFilesPath + 'DS1/' +
                             'DS1' + OM_str + RBin + '.txt',
                             'DS1' + OM_str + RBin),
                            (textFilesPath + 'D2/' +
                             'D2' + HQ_str + RBin + '.txt',
                             'D2' + HQ_str + RBin),
                            (textFilesPath + 'DS1/' +
                             'DS1' + OM_49 + '_Rlim_10000.txt',
                             'DS1' + OM_49 + '_Rlim_10000'),
                            (textFilesPath + 'D2/' +
                             'D2' + HQ_49 + '_Rlim_10000.txt',
                             'D2' + HQ_49 + '_Rlim_10000'),
                            (textFilesPath + 'DS1/' +
                             'DS1' + OM_49 + RBin + '.txt',
                             'DS1' + OM_49 + RBin),
                            (textFilesPath + 'D2/' +
                             'D2' + HQ_49 + RBin + '.txt',
                             'D2' + HQ_49 + RBin),
                            (textFilesPath + 'DS1/' +
                             'DS1' + OM_49 + RBin + '.txt',
                             'DS1' + OM_49 + '_Rlim10000_100RBins'),
                            (textFilesPath + 'D2/' +
                             'D2' + HQ_49 + '_Rlim_10000_100_RBins.txt',
                             'D2' + HQ_49 + '_Rlim_10000_100_RBins'),
                            (textFilesPath + 'DS1/' +
                             'DS1' + OM_49 + '_Rlim10000_200RBins.txt',
                             'DS1' + OM_49 + '_Rlim10000_200RBins'),
                            (textFilesPath + 'D2/' +
                             'D2' + HQ_49 + '_Rlim_10000_200_RBins.txt',
                             'D2' + HQ_49 + '_Rlim_10000_200_RBins')]

FileLstDS1D2_SecondLast_R10000 = [(textFilesPath + 'DS1/' +
                                   'DS1' + OM_48 + '_Rlim_10000.txt',
                                   'DS1' + OM_48 + '_Rlim_10000'),
                                  (textFilesPath + 'D2/' +
                                   'D2' + HQ_48 + '_Rlim_10000.txt',
                                   'D2' + HQ_48 + '_Rlim_10000'),
                                  (textFilesPath + 'DS1/' +
                                   'DS1' + OM_48 + RBin + '.txt',
                                   'DS1' + OM_48 + RBin),
                                  (textFilesPath + 'D2/' +
                                   'D2' + HQ_48 + RBin + '.txt',
                                   'D2' + HQ_48 + RBin),
                                  (textFilesPath + 'DS1/' +
                                   'DS1' + OM_48 + '_Rlim10000_100RBins.txt',
                                   'DS1' + OM_48 + '_Rlim10000_100RBins'),
                                  (textFilesPath + 'D2/' +
                                   'D2' + HQ_48 + '_Rlim10000_100RBins.txt',
                                   'D2' + HQ_48 + '_Rlim10000_100RBins'),
                                  (textFilesPath + 'DS1/' +
                                   'DS1' + OM_48 + '_Rlim10000_200RBins.txt',
                                   'DS1' + OM_48 + '_Rlim10000_200RBins'),
                                  (textFilesPath + 'D2/' +
                                   'D2' + HQ_48 + '_Rlim10000_200RBins.txt',
                                   'D2' + HQ_48 + '_Rlim10000_200RBins')
                                  ]

FileLstDS1_Rlimit32_20bins = [(textFilesPath + 'DS1/' +
                               'DS1' + OM_str + '_Rlim_32_20_RBins.txt',
                               'DS1' + OM_str + '_Rlim_32_20_RBins'),
                              (textFilesPath + 'DS1/' +
                               'DS1' + OM_49 + '_Rlim_32_20_RBins.txt',
                               'DS1' + OM_49 + '_Rlim_32_20_RBins')]

FileLstSoft_D2_Rlimit32_20bins = [(textFilesPath + 'Soft_D2/' +
                                   'Soft_D2' + HQ_str + '_Rlim32_20RBins.txt',
                                   'Soft_D2' + HQ_str + '_Rlim32_20RBins'),
                                  (textFilesPath + 'Soft_D2/' +
                                   'Soft_D2' + HQ_49 + '_Rlim32_20RBins.txt',
                                   'Soft_D2' + HQ_49 + '_Rlim32_20RBins')
                                  ]

HQ_198 = '_HQ10000_G1.0_198_093'
fileLstE = [(textFilesPath + 'E/' + 'E_' + HQ_str + '.txt', 'E' + HQ_str),
            (textFilesPath + 'E/' + 'E_HQ10000_G1.0_5_005.txt',
             'E_HQ10000_G1.0_5_005'),
            (textFilesPath + 'E/' + 'E_HQ10000_G1.0_10_005.txt',
             'E_HQ10000_G1.0_10_005'),
            (textFilesPath + 'E/' + 'E_HQ10000_G1.0_198_000.txt',
             'E_HQ10000_G1.0_198_000'),
            (textFilesPath + 'E/' + 'E' + HQ_198 + '.txt', 'E' + HQ_198)]

fileLstE_R10000 = [(textFilesPath + 'E/' +
                    'E' + HQ_str + '_Rlim_10000_20_RBins.txt',
                    'E' + HQ_str + '_Rlim_10000_20_RBins'),
                   (textFilesPath + 'E/' +
                    'E' + HQ_198 + '_Rlim_10000_20_RBins.txt',
                    'E' + HQ_198 + '_Rlim_10000_20_RBins')]

FileLstE_Rlimit32_50bins = [(textFilesPath + 'E/' +
                             'E' + HQ_str + '_Rlim_32_50_RBins.txt',
                             'E' + HQ_str + '_Rlim_32_50_RBins'),
                            (textFilesPath + 'E/' +
                             'E' + HQ_198 + '_Rlim_32_50_RBins.txt',
                             'E' + HQ_198 + '_Rlim_32_50_RBins')]

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
