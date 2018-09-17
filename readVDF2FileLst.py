#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 21:36:43 2018

@author: Gustav Collin Rasmussen
"""

import numpy as np
import pylab
import os
import RhoAndGaussianAndTsallis

userPath = os.getcwd()
desktopPath = userPath + 'Desktop/'
GADGET_G_path = desktopPath + 'RunGadget/Gperturbations/'
stablePath = desktopPath + 'Gperturbations/StableStructures/'
figurePath = stablePath + 'figures/'
textFilesPath = stablePath + 'textFiles/'
MartinPath = 'MartinICandFinalEddandOM/'
hdf5Path = desktopPath + 'Gperturbations/hdf5Files/'
nosyncPath = userPath + 'nosync/RunGadget/'


# [5],[6],[7] : log9, log7, log8 : r, theta, phi
# x10 is tangential part.

# Write OS script to change name of files.

nameLst1 = ['HQ10000_G1.0_0_000',  # 0.th/IC set of files
            'HQ10000_G1.2_1_005',
            'HQ10000_G0.8_2_005',
            'HQ10000_G1.2_3_005',
            'HQ10000_G1.2_5_005',
            'HQ10000_G1.2_7_005',
            'HQ10000_G1.2_9_005',
            'HQ10000_G1.0_10_009'
            ]

gammaLst = [-1.50, -2.00, -2.50, -3.00]

bins1 = [[(f"{i}VTSigmaTGamma_{g}.txt",
           f"{i}VTSigmaTGamma_{g}"),
          (f"{i}VRSigmaRGamma_{g}.txt",
           f"{i}VRSigmaRGamma_{g}"),
          (f"{i}VThetaSigmaThetaGamma_{g}.txt",
           f"{i}VThetaSigmaThetaGamma_{g}"),
          (f"{i}VPhiSigmaPhiGamma_{g}.txt",
           f"{i}VPhiSigmaPhiGamma_{g}"),
          (f"{i}Logx10Gamma_{g}.txt",
           f"{i}Logx10Gamma_{g}"),
          (f"{i}Logx9Gamma_{g}.txt",
           f"{i}Logx9Gamma_{g}"),
          (f"{i}Logx7Gamma_{g}.txt",
           f"{i}Logx7Gamma_{g}"),
          (f"{i}Logx8Gamma_{g}.txt",
           f"{i}Logx8Gamma_{g}")] for i in nameLst1 for g in gammaLst]


def numberOfElements(fileLst):
    return str(fileLst).count(",") + 1


NumberOfFiles = numberOfElements(bins1)
print(f'Number of files in the bins1 list is: {NumberOfFiles}')  # 8*4*16 = 512

# load files ------------------------------------------------------------------
filelst = ['_G1_0_0_000', '_G1_2_1_005', '_G0_8_2_005', '_G1_2_3_005',
           '_G1_2_5_005', '_G1_2_7_005', '_G1_2_9_005', '_G1_0_10_009'
           ]

'''
vars()[[f'Bin{num}HQ10000{file}'
        for num in range(1, 5) for file in filelst]] =\
        [(f, l) for f, l in bins1[index] for index in range(4 * len(filelst))]
'''

index = 0
for file in filelst:
    for num in range(1, 5):
        vars()[f'Bin{num}HQ10000{file}'] = \
         [(f, l) for f, l in bins1[index]]
        # vars()[f'Bin{num}HQ10000{file}'] = index  # \
        # [(pylab.loadtxt(f), l) for f, l in bins1[index]]
        index += 1

# print(globals())
# print(locals())

print(Bin1HQ10000_G0_8_2_005[0][0])

nameLst2 = [nameLst1[1],
            nameLst1[3],
            nameLst1[4],
            nameLst1[5],
            nameLst1[6]
            ]

bins2 = [[(f"{i}NewRMiddleVTSigmaTGamma_{g}.txt",
           f"{i}NewRMiddleVTSigmaTGamma_{g}"),
          (f"{i}NewRMiddleVRSigmaRGamma_{g}.txt",
           f"{i}NewRMiddleVRSigmaRGamma_{g}"),
          (f"{i}NewRMiddleVThetaSigmaThetaGamma_{g}.txt",
           f"{i}NewRMiddleVThetaSigmaThetaGamma_{g}"),
          (f"{i}NewRMiddleVPhiSigmaPhiGamma_{g}.txt",
           f"{i}NewRMiddleVPhiSigmaPhiGamma_{g}"),
          (f"{i}NewRMiddleLogx10Gamma_{g}.txt",
           f"{i}NewRMiddleLogx10Gamma_{g}"),
          (f"{i}NewRMiddleLogx9Gamma_{g}.txt",
           f"{i}NewRMiddleLogx9Gamma_{g}"),
          (f"{i}NewRMiddleLogx7Gamma_{g}.txt",
           f"{i}NewRMiddleLogx7Gamma_{g}"),
          (f"{i}NewRMiddleLogx8Gamma_{g}.txt",
           f"{i}NewRMiddleLogx8Gamma_{g}")] for i in nameLst2
         for g in gammaLst]

NumberOfFiles2 = numberOfElements(bins2)
print(f'Number of files in the bins2 list is: {NumberOfFiles2}')  # 320

fileLst2 = ['_G1_2_1_005', '_G1_2_3_005', '_G1_2_5_005', '_G1_2_7_005',
            '_G1_2_9_005'
            ]

index = 0
for file in fileLst2:
    for num in range(1, 5):
        vars()[f'Bin{num}newRMiddleHQ10000{file}'] = \
         [(f, l) for f, l in bins2[index]]
        index += 1

print(Bin1newRMiddleHQ10000_G1_2_1_005[0][0])


# 'Hernquist10000_G1.2_1_005_new_R_middle_VT_sigmatan_gamma_-1.50.txt' becomes:
# 'HQ10000_G1.2_1_005_newRMiddle_VTSigmaTanGamma_-1.50.txt'

# Bin1newRMiddleHQ
# '_innerbin_different_gammas_Hernquist'


nameLst3A = ['test2HQ10000_G1.0_0_000', 'test2HQ10000_G1.0_5_005',
             'test2HQ10000_G1.0_10_005', 'test2HQ10000_G1.0_15_005',
             'test2HQ10000_G1.0_20_005', 'test2HQ10000_G1.0_25_005',
             'AHQ10000_G1.0_0_000', 'AHQ10000_G1.0_5_005',
             'A_HQ10000_G1.0_10_005', 'A_HQ10000_G1.0_40_005',
             'A_HQ10000_G1.0_48_009', 'A_HQ10000_G1.0_48_093',
             'B_HQ10000_G1.0_0_000', 'B_HQ10000_G1.0_5_005',
             'B_HQ10000_G1.0_10_005', 'B_HQ10000_G1.0_198_000',
             'B_HQ10000_G1.0_198_093'
             ]

nameLst3B = ['test2HQ10000_G1.0_0_000', 'test2HQ10000_G1.0_5_005',
             'test2HQ10000_G1.0_10_005', 'test2HQ10000_G1.0_15_005',
             'test2HQ10000_G1.0_20_005', 'test2HQ10000_G1.0_25_005',
             'AHQ10000_G1.0_0_000', 'AHQ10000_G1.0_5_005',
             'A_HQ10000_G1.0_10_005', 'A_HQ10000_G1.0_40_005',
             'A_HQ10000_G1.0_48_009', 'A_HQ10000_G1.0_48_093',
             'B_HQ10000_G1.0_0_000', 'B_HQ10000_G1.0_5_005',
             'B_HQ10000_G1.0_10_005', 'B_HQ10000_G1.0_198_000',
             'B_HQ10000_G1.0_198_093',
             'test2HQ10000_G1.0_18_053', 'A_HQ10000_G1.2_46_005',
             'A_HQ10000_G0.8_47_005'
             ]

bins3A = [[(f"{i}NewRMiddleVTSigmaTGamma_{g}.txt",
            f"{i}NewRMiddleVTSigmaTGamma_{g}"),
           (f"{i}NewRMiddleVRSigmaRGamma_{g}.txt",
            f"{i}NewRMiddleVRSigmaRGamma_{g}"),
           (f"{i}NewRMiddleVThetaSigmaThetaGamma_{g}.txt",
            f"{i}NewRMiddleVThetaSigmaThetaGamma_{g}"),
           (f"{i}NewRMiddleVPhiSigmaPhiGamma_{g}.txt",
            f"{i}NewRMiddleVPhiSigmaPhiGamma_{g}"),
           (f"{i}NewRMiddleLogx10Gamma_{g}.txt",
            f"{i}NewRMiddleLogx10Gamma_{g}"),
           (f"{i}NewRMiddleLogx9Gamma_{g}.txt",
            f"{i}NewRMiddleLogx9Gamma_{g}"),
           (f"{i}NewRMiddleLogx7Gamma_{g}.txt",
            f"{i}NewRMiddleLogx7Gamma_{g}"),
           (f"{i}NewRMiddleLogx8Gamma_{g}.txt",
            f"{i}NewRMiddleLogx8Gamma_{g}")] for i in nameLst3A
          for g in gammaLst]

middleRadii = [19.95, 31.62]

bins3B = [[(f"{i}LargeRmiddle{rM}VTSigmaT.txt",
            f"{i}LargeRmiddle{rM}VTSigmaT"),
           (f"{i}LargeRmiddle{rM}VRSigmaR.txt",
            f"{i}LargeRmiddle{rM}VRSigmaR"),
           (f"{i}LargeRmiddle{rM}VThetaSigmaTheta.txt",
            f"{i}LargeRmiddle{rM}VThetaSigmaTheta"),
           (f"{i}LargeRmiddle{rM}VPhiSigmaPhi.txt",
            f"{i}LargeRmiddle{rM}VPhiSigmaPhi"),
           (f"{i}LargeRmiddle{rM}Logx10.txt",
            f"{i}LargeRmiddle{rM}Logx10"),
           (f"{i}LargeRmiddle{rM}Logx9.txt",
            f"{i}LargeRmiddle{rM}Logx9"),
           (f"{i}LargeRmiddle{rM}Logx7.txt",
            f"{i}LargeRmiddle{rM}Logx7"),
           (f"{i}LargeRmiddle{rM}Logx8.txt",
            f"{i}LargeRmiddle{rM}Logx8")] for i in nameLst3B
          for rM in middleRadii]

NumberOfFiles3A = numberOfElements(bins3A)
print(f'Number of files in the bins3A list is: {NumberOfFiles3A}')

NumberOfFiles3B = numberOfElements(bins3B)
print(f'Number of files in the bins3B list is: {NumberOfFiles3B}')


Bin1differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[0]]
Bin2differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[1]]
Bin3differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[2]]
Bin4differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[3]]
largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[0]]
largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[1]]

bin1DifferentGammasTest2HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[4]]
bin2DifferentGammasTest2HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[5]]
bin3DifferentGammasTest2HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[6]]
bin4DifferentGammasTest2HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[7]]
largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[2]]
largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[3]]

Bin1differentGammasTest2HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[8]]
Bin2differentGammasTest2HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[9]]
Bin3differentGammasTest2HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[10]]
Bin4differentGammasTest2HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[11]]
largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[4]]
largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[5]]

Bin1differentGammasTest2HQ10000_G1_0_15_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[12]]
Bin2differentGammasTest2HQ10000_G1_0_15_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[13]]
Bin3differentGammasTest2HQ10000_G1_0_15_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[14]]
Bin4differentGammasTest2HQ10000_G1_0_15_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[15]]
largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_15_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[6]]
largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_15_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[7]]

bin1differentGammasTest2HQ10000_G1_0_20_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[16]]
bin2differentGammasTest2HQ10000_G1_0_20_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[17]]
bin3differentGammasTest2HQ10000_G1_0_20_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[18]]
bin4differentGammasTest2HQ10000_G1_0_20_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[19]]
largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_20_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[8]]
largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_20_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[9]]

bin1differentGammasTest2HQ10000_G1_0_25_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[20]]
bin2differentGammasTest2HQ10000_G1_0_25_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[21]]
bin3differentGammasTest2HQ10000_G1_0_25_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[22]]
bin4differentGammasTest2HQ10000_G1_0_25_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[23]]
largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_25_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[10]]
largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_25_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[11]]

largeRmiddle_19_95_differentGammasTest2_HQ10000_G1_0_18_053 = [(pylab.loadtxt(f), l) for f, l in bins3B[12]]
largeRmiddle_31_62_differentGammasTest2_HQ10000_G1_0_18_053 = [(pylab.loadtxt(f), l) for f, l in bins3B[13]]

Bin1differentGammasAHQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[24]]
Bin2differentGammasAHQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[25]]
Bin3differentGammasAHQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[26]]
Bin4differentGammasAHQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[27]]
largeRmiddle_19_95_differentGammasAHQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[14]]
largeRmiddle_31_62_differentGammasAHQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[15]]

Bin1differentGammas_A_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[28]]
Bin2differentGammas_A_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[29]]
Bin3differentGammas_A_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[30]]
Bin4differentGammas_A_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[31]]
largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[16]]
largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[17]]

Bin1differentGammas_A_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[32]]
Bin2differentGammas_A_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[33]]
Bin3differentGammas_A_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[34]]
Bin4differentGammas_A_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[35]]
largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[18]]
largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[19]]

Bin1differentGammas_A_HQ10000_G1_0_40_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[36]]
Bin2differentGammas_A_HQ10000_G1_0_40_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[37]]
Bin3differentGammas_A_HQ10000_G1_0_40_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[38]]
Bin4differentGammas_A_HQ10000_G1_0_40_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[39]]
largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_40_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[20]]
largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_40_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[21]]

largeRmiddle_19_95_differentGammasAHQ10000_G1_2_46_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[22]]
largeRmiddle_31_62_differentGammasAHQ10000_G1_2_46_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[23]]

largeRmiddle_19_95_differentGammas_A_HQ10000_G0_8_47_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[24]]
largeRmiddle_31_62_differentGammas_A_HQ10000_G0_8_47_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[25]]

Bin1differentGammas_A_Hernquist10000_G1_0_48_009 = [(pylab.loadtxt(f), l) for f, l in bins3A[40]]
Bin2differentGammas_A_Hernquist10000_G1_0_48_009 = [(pylab.loadtxt(f), l) for f, l in bins3A[41]]
Bin3differentGammas_A_Hernquist10000_G1_0_48_009 = [(pylab.loadtxt(f), l) for f, l in bins3A[42]]
Bin4differentGammas_A_Hernquist10000_G1_0_48_009 = [(pylab.loadtxt(f), l) for f, l in bins3A[43]]
largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_48_009 = [(pylab.loadtxt(f), l) for f, l in bins3B[26]]
largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_48_009 = [(pylab.loadtxt(f), l) for f, l in bins3B[27]]

Bin1differentGammasAHQ10000_G1_0_48_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[44]]
Bin2differentGammasAHQ10000_G1_0_48_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[45]]
Bin3differentGammasAHQ10000_G1_0_48_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[46]]
Bin4differentGammasAHQ10000_G1_0_48_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[47]]
largeRmiddle_19_95_differentGammasAHQ10000_G1_0_48_093 = [(pylab.loadtxt(f), l) for f, l in bins3B[28]]
largeRmiddle_31_62_differentGammasAHQ10000_G1_0_48_093 = [(pylab.loadtxt(f), l) for f, l in bins3B[29]]

Bin1differentGammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[48]]
Bin2differentGammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[49]]
Bin3differentGammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[50]]
Bin4differentGammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[51]]
largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[30]]
largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[31]]

bin1differentGammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[52]]
bin2differentGammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[53]]
bin3differentGammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[54]]
bin4differentGammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[55]]
largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[32]]
largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[33]]

bin1differentGammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[56]]
bin2differentGammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[57]]
bin3differentGammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[58]]
bin4differentGammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3A[59]]
largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[34]]
largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in bins3B[35]]

bin1differentGammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[60]]
bin2differentGammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[61]]
bin2differentGammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[62]]
bin3differentGammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in bins3A[63]]
largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[36]]
largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in bins3B[37]]

Bin1differentGammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[64]]
Bin2differentGammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[65]]
Bin3differentGammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[66]]
Bin4differentGammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in bins3A[67]]
largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in bins3B[38]]
largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in bins3B[39]]
