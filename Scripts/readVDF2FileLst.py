#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 21:36:43 2018

@author: Gustav Collin Rasmussen
"""

import pylab
from pathlib import Path
import re

textFilesPath = Path.cwd().parent / 'textFiles/'
APath = textFilesPath / 'A'
BPath = textFilesPath / 'B'

pattern = re.compile('[A-Z]?HQ.*')

middleRadii = [19.95, 31.62]
gammaLst = [-1.5, -2.0, -2.5, -3.0]


def numberOfElements(fileLst):
    return str(fileLst).count(",") + 1


def load_files(filelst, file_name, bins):
    index = 0
    for file in filelst:
        for num in range(1, 5):
            vars()[f'Bin{num}{file_name}{file}'] =\
                [(pylab.loadtxt(bins[num - 1][index][0]),
                  bins[num - 1][index][1])]
            index += 1


# Name lists ------------------------------------------------------------------
nameLstA = [f'{APath}/AHQ10000G1.0_0_000', f'{APath}/AHQ10000G1.0_5_005',
            f'{APath}/AHQ10000G1.0_10_005', f'{APath}/AHQ10000G1.0_40_005',
            f'{APath}/AHQ10000G1.2_46_005', f'{APath}/AHQ10000G0.8_47_005',
            f'{APath}/AHQ10000G1.0_48_009', f'{APath}/AHQ10000G1.0_48_093']

nameLstB = [f'{BPath}/BHQ10000G1.0_0_000', f'{BPath}/BHQ10000G1.0_5_005',
            f'{BPath}/BHQ10000G1.0_10_005', f'{BPath}/BHQ10000G1.0_198_000',
            f'{BPath}/BHQ10000G1.0_198_093']

# Bins ------------------------------------------------------------------------
bins_A_New = [[(f"{i}NewRmiddleVTSigmaTGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVTSigmaTGamma_{g}"),
               (f"{i}NewRmiddleVRSigmaRGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVRSigmaRGamma_{g}"),
               (f"{i}NewRmiddleVThetaSigmaThetaGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVThetaSigmaThetaGamma_{g}"),
               (f"{i}NewRmiddleVPhiSigmaPhiGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVPhiSigmaPhiGamma_{g}"),
               (f"{i}NewRmiddleLogx10Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx10Gamma_{g}"),
               (f"{i}NewRmiddleLogx9Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx9Gamma_{g}"),
               (f"{i}NewRmiddleLogx7Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx7Gamma_{g}"),
               (f"{i}NewRmiddleLogx8Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx8Gamma_{g}")
               ] for i in nameLstA for g in gammaLst]

bins_A_Large = [[(f"{i}LargeRmiddle{rM}VTSigmaT.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VTSigmaT"),
                 (f"{i}LargeRmiddle{rM}VRSigmaR.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VRSigmaR"),
                 (f"{i}LargeRmiddle{rM}VThetaSigmaTheta.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VThetaSigmaTheta"),
                 (f"{i}LargeRmiddle{rM}VPhiSigmaPhi.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VPhiSigmaPhi"),
                 (f"{i}LargeRmiddle{rM}Logx10.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx10"),
                 (f"{i}LargeRmiddle{rM}Logx9.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx9"),
                 (f"{i}LargeRmiddle{rM}Logx7.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx7"),
                 (f"{i}LargeRmiddle{rM}Logx8.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx8")
                 ] for i in nameLstA for rM in middleRadii]


bins_B_New = [[(f"{i}NewRmiddleVTSigmaTGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVTSigmaTGamma_{g}"),
               (f"{i}NewRmiddleVRSigmaRGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVRSigmaRGamma_{g}"),
               (f"{i}NewRmiddleVThetaSigmaThetaGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVThetaSigmaThetaGamma_{g}"),
               (f"{i}NewRmiddleVPhiSigmaPhiGamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleVPhiSigmaPhiGamma_{g}"),
               (f"{i}NewRmiddleLogx10Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx10Gamma_{g}"),
               (f"{i}NewRmiddleLogx9Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx9Gamma_{g}"),
               (f"{i}NewRmiddleLogx7Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx7Gamma_{g}"),
               (f"{i}NewRmiddleLogx8Gamma_{g}.txt",
                f"{pattern.findall(i)[0]}NewRmiddleLogx8Gamma_{g}")
               ] for i in nameLstB for g in gammaLst]

bins_B_Large = [[(f"{i}LargeRmiddle{rM}VTSigmaT.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VTSigmaT"),
                 (f"{i}LargeRmiddle{rM}VRSigmaR.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VRSigmaR"),
                 (f"{i}LargeRmiddle{rM}VThetaSigmaTheta.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VThetaSigmaTheta"),
                 (f"{i}LargeRmiddle{rM}VPhiSigmaPhi.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}VPhiSigmaPhi"),
                 (f"{i}LargeRmiddle{rM}Logx10.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx10"),
                 (f"{i}LargeRmiddle{rM}Logx9.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx9"),
                 (f"{i}LargeRmiddle{rM}Logx7.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx7"),
                 (f"{i}LargeRmiddle{rM}Logx8.txt",
                  f"{pattern.findall(i)[0]}LargeRmiddle{rM}Logx8")
                 ] for i in nameLstB for rM in middleRadii]

# File lists ------------------------------------------------------------------
fileLst00 = ['G1_0_0_000', 'G1_2_1_005', 'G0_8_2_005', 'G1_2_3_005',
             'G1_2_5_005', 'G1_2_7_005', 'G1_2_9_005', 'G1_0_10_009']

fileLst10 = [fileLst00[1], fileLst00[3], fileLst00[4], fileLst00[5],
             fileLst00[6]]

# load files ------------------------------------------------------------------
# tests
# loaded_file = pylab.loadtxt(bins20[0][0][0])
# label = bins20[0][0][1]
# load_list = [(loaded_file, label)]
# load_list2 = [(pylab.loadtxt(bins20[0][0][0]), bins20[0][0][1])]

# Must be debugged:
# [(pylab.loadtxt(filename), label) for filename, label in bins20[0][0]]

# vars()[f'Bin1HQ10000{fileLst00[0]}'] =\
#     [(pylab.loadtxt(bins20[0][0][0]), bins20[0][0][1])]

load_files(fileLst10, 'differentGammasTest2HQ10000', bins_A_New)

'''
Bin1differentGammasTest2HQ10000G1_0_0_000 =\
    [(pylab.loadtxt(filename), label) for filename, label in bins20[0][0]]

Bin2differentGammasTest2HQ10000G1_0_0_000 =\
   [(pylab.loadtxt(filename), label) for filename, label in bins20[0][1]]

Bin3differentGammasTest2HQ10000G1_0_0_000 =\
    [(pylab.loadtxt(filename), label) for filename, label in bins20[0][2]]

Bin4differentGammasTest2HQ10000G1_0_0_000 =\
    [(pylab.loadtxt(filename), label) for filename, label in bins20[0][3]]

largeRmiddle_19_95_differentGammasTest2HQ10000G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins21[0]]

largeRmiddle_31_62_differentGammasTest2HQ10000G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins21[1]]

# bin1DifferentGammasTest2HQ10000_G1_0_5_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[4]]

# bin2DifferentGammasTest2HQ10000_G1_0_5_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[5]]

# bin3DifferentGammasTest2HQ10000_G1_0_5_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[6]]

# bin4DifferentGammasTest2HQ10000_G1_0_5_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[7]]

largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[2]]

largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[3]]

# Bin1differentGammasTest2HQ10000_G1_0_10_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[8]]

# Bin2differentGammasTest2HQ10000_G1_0_10_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[9]]

# Bin3differentGammasTest2HQ10000_G1_0_10_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[10]]

# Bin4differentGammasTest2HQ10000_G1_0_10_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[11]]

largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[4]]

largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[5]]

# Bin1differentGammasTest2HQ10000_G1_0_15_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[12]]

# Bin2differentGammasTest2HQ10000_G1_0_15_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[13]]

# Bin3differentGammasTest2HQ10000_G1_0_15_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[14]]

# Bin4differentGammasTest2HQ10000_G1_0_15_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[15]]

largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_15_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[6]]

largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_15_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[7]]

# bin1differentGammasTest2HQ10000_G1_0_20_005 =\
#    [(pylab.loadtxt(f), l) for f, l in bins3A[16]]

# bin2differentGammasTest2HQ10000_G1_0_20_005 =\
#    [(pylab.loadtxt(f), l) for f,l in bins3A[17]]

# bin3differentGammasTest2HQ10000_G1_0_20_005 =\
#     [(pylab.loadtxt(f), l) for f, l in bins3A[18]]

# bin4differentGammasTest2HQ10000_G1_0_20_005 =\
# [(pylab.loadtxt(f), l) for f, l in bins3A[19]]

largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_20_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[8]]

largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_20_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[9]]

# bin1differentGammasTest2HQ10000_G1_0_25_005 =\
#    [(pylab.loadtxt(f), l) for f, l in bins3A[20]]

# bin2differentGammasTest2HQ10000_G1_0_25_005 =\
#    [(pylab.loadtxt(f), l) for f, l in bins3A[21]]

# bin3differentGammasTest2HQ10000_G1_0_25_005 =\
#    [(pylab.loadtxt(f), l) for f, l in bins3A[22]]

# bin4differentGammasTest2HQ10000_G1_0_25_005 =\
#    [(pylab.loadtxt(f), l) for f, l in bins3A[23]]

largeRmiddle_19_95_differentGammasTest2HQ10000_G1_0_25_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[10]]

largeRmiddle_31_62_differentGammasTest2HQ10000_G1_0_25_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[11]]

largeRmiddle_19_95_differentGammasTest2_HQ10000_G1_0_18_053 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[12]]

largeRmiddle_31_62_differentGammasTest2_HQ10000_G1_0_18_053 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[13]]

Bin1differentGammasAHQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[24]]

Bin2differentGammasAHQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[25]]

Bin3differentGammasAHQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[26]]

Bin4differentGammasAHQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[27]]

largeRmiddle_19_95_differentGammasAHQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[14]]

largeRmiddle_31_62_differentGammasAHQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[15]]

Bin1differentGammas_A_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[28]]

Bin2differentGammas_A_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[29]]

Bin3differentGammas_A_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[30]]

Bin4differentGammas_A_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[31]]

largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[16]]

largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[17]]

Bin1differentGammas_A_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[32]]

Bin2differentGammas_A_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[33]]

Bin3differentGammas_A_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[34]]

Bin4differentGammas_A_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[35]]

largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[18]]

largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[19]]

Bin1differentGammas_A_HQ10000_G1_0_40_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[36]]

Bin2differentGammas_A_HQ10000_G1_0_40_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[37]]

Bin3differentGammas_A_HQ10000_G1_0_40_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[38]]

Bin4differentGammas_A_HQ10000_G1_0_40_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[39]]

largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_40_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[20]]

largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_40_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[21]]

largeRmiddle_19_95_differentGammasAHQ10000_G1_2_46_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[22]]

largeRmiddle_31_62_differentGammasAHQ10000_G1_2_46_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[23]]

largeRmiddle_19_95_differentGammas_A_HQ10000_G0_8_47_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[24]]

largeRmiddle_31_62_differentGammas_A_HQ10000_G0_8_47_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[25]]

Bin1differentGammas_A_Hernquist10000_G1_0_48_009 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[40]]

Bin2differentGammas_A_Hernquist10000_G1_0_48_009 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[41]]

Bin3differentGammas_A_Hernquist10000_G1_0_48_009 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[42]]

Bin4differentGammas_A_Hernquist10000_G1_0_48_009 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[43]]

largeRmiddle_19_95_differentGammas_A_HQ10000_G1_0_48_009 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[26]]

largeRmiddle_31_62_differentGammas_A_HQ10000_G1_0_48_009 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[27]]

# Bin1differentGammasAHQ10000_G1_0_48_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[44]]
# IndexError: list index out of range

Bin2differentGammasAHQ10000_G1_0_48_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[45]]
# IndexError: list index out of range

Bin3differentGammasAHQ10000_G1_0_48_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[46]]
# IndexError: list index out of range

Bin4differentGammasAHQ10000_G1_0_48_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[47]]
# IndexError: list index out of range

largeRmiddle_19_95_differentGammasAHQ10000_G1_0_48_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[28]]
# IndexError: list index out of range

largeRmiddle_31_62_differentGammasAHQ10000_G1_0_48_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[29]]
# IndexError: list index out of range

Bin1differentGammas_B_HQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[48]]
# IndexError: list index out of range

Bin2differentGammas_B_HQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[49]]
# IndexError: list index out of range

Bin3differentGammas_B_HQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[50]]
# IndexError: list index out of range

Bin4differentGammas_B_HQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[51]]
# IndexError: list index out of range

largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[30]]
# IndexError: list index out of range

largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_0_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[31]]
# IndexError: list index out of range

bin1differentGammas_B_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[52]]
# IndexError: list index out of range

bin2differentGammas_B_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[53]]
# IndexError: list index out of range

bin3differentGammas_B_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[54]]
# IndexError: list index out of range

bin4differentGammas_B_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[55]]
# IndexError: list index out of range

largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[32]]
# IndexError: list index out of range

largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_5_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[33]]
# IndexError: list index out of range

bin1differentGammas_B_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[56]]
# IndexError: list index out of range

bin2differentGammas_B_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[57]]
# IndexError: list index out of range

bin3differentGammas_B_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[58]]
# IndexError: list index out of range

bin4differentGammas_B_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[59]]
# IndexError: list index out of range

largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[34]]
# IndexError: list index out of range

largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_10_005 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[35]]
# IndexError: list index out of range

bin1differentGammas_B_HQ10000_G1_0_198_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[60]]
# IndexError: list index out of range

bin2differentGammas_B_HQ10000_G1_0_198_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[61]]
# IndexError: list index out of range

bin2differentGammas_B_HQ10000_G1_0_198_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[62]]
# IndexError: list index out of range

bin3differentGammas_B_HQ10000_G1_0_198_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[63]]
# IndexError: list index out of range

largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_198_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[36]]
# IndexError: list index out of range

largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_198_000 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[37]]
# IndexError: list index out of range

Bin1differentGammas_B_HQ10000_G1_0_198_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[64]]
# IndexError: list index out of range

Bin2differentGammas_B_HQ10000_G1_0_198_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[65]]
# IndexError: list index out of range

Bin3differentGammas_B_HQ10000_G1_0_198_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[66]]
# IndexError: list index out of range

Bin4differentGammas_B_HQ10000_G1_0_198_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3A[67]]
# IndexError: list index out of range

largeRmiddle_19_95_differentGammas_B_HQ10000_G1_0_198_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[38]]
# IndexError: list index out of range

largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_198_093 =\
    [(pylab.loadtxt(f), l) for f, l in bins3B[39]]
# IndexError: list index out of range
'''


def main():
    # print(globals())
    # print(locals())
    NumberOfFiles = numberOfElements(bins1)
    NumberOfFiles2 = numberOfElements(bins2)
    NumberOfFiles3A = numberOfElements(bins3A)
    NumberOfFiles3B = numberOfElements(bins3B)
    # print(f'Number of files in the bins1 list is: {NumberOfFiles}')
    # print(f'Number of files in the bins2 list is: {NumberOfFiles2}')
    # print(f'Number of files in the bins3A list is: {NumberOfFiles3A}')
    # print(f'Number of files in the bins3B list is: {NumberOfFiles3B}')

    # with open(f"{APath}/{bins3A[0][0][0]}", "r") as f:
    #     print(f.readlines())
    # print(f"{APath}/{bins3A[0][0][0]}")
    # f, l = f"{APath}/{bins3A[0][0][0]}", bins3A[0][0][1]
    # print(f)
    # print(l)
    # testbin = [(pylab.loadtxt(f), l)]


if __name__ == '__main__':
    main()

# [5],[6],[7] : log9, log7, log8 : r, theta, phi
# x10 is tangential part.
