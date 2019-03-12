# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pylab
# import RhoAndGaussianAndTsallis
# import snapshotFiles

# Switches ---------------------------------------------------------
Gamma_on = 1
Beta_on = 0

# Figures ---------------------------------------------------------
Fig1_vr_vPhi_vTheta = 0  # Works for test and test2
Fig1_vr_vPhi_vTheta_with_fit = 0  # Works for test and test2
Fig1_vt = 0  # Works for test and test2
Fig1_vt_with_fit = 0  # Works for test, test2 and B

Fig2_vr_vPhi_vTheta_divided_by_gauss = 0  # Works for test and test2
Fig2a_vt_divided_by_gauss = 0  # Works for test and test2

Fig6_GPerts_same_gammas_as_IC_vr = 0  # Works for test. test2?
Fig6_GPerts_G1_2_same_gammas_as_IC_vt = 0  # Not yet created

Fig7_GPerts_different_gammas_vr_vPhi_vTheta = 0  # Not yet created

# Not yet created
Fig8_GPerts_different_gammas_vr_vPhi_vTheta_divided_by_gauss = 0

Fig9_GPerts_different_gammas_vr = 0  # Not yet created

Fig10_GPerts_different_gammas_vt = 0  # Works for test, test2 and B

# Next 4 figures works for test, test2, B:
Fig11_GPerts_gammas_1_5_vt_divided_by_gauss_and_Tsallis = 0
Fig12_GPerts_gammas_2_0_vt_divided_by_gauss_and_Tsallis = 0
Fig13_GPerts_gammas_2_5_vt_divided_by_gauss_and_Tsallis = 0
Fig14_GPerts_gammas_3_0_vt_divided_by_gauss_and_Tsallis = 0

# Next 2 figures works for A, B:
Fig15_GPerts_R_middle_19_95_vt_divided_by_gauss_and_Tsallis = 0
Fig16_GPerts_R_middle_31_62_vt_divided_by_gauss_and_Tsallis = 0

# Files ---------------------------------------------------------
G_Pert_HQ10000_G1_0_0_000 = 1
G_Pert_HQ10000_G1_2_1_005 = 1
G_Pert_HQ10000_G0_8_2_005 = 1
G_Pert_HQ10000_G1_2_3_005 = 1
G_Pert_HQ10000_G1_2_5_005 = 1
G_Pert_HQ10000_G1_2_7_005 = 1
G_Pert_HQ10000_G1_2_9_005 = 1
G_Pert_HQ10000_G1_0_10_009 = 1

G_Pert_different_gammas_HQ10000_G1_2_1_005 = 1
G_Pert_different_gammas_HQ10000_G1_2_3_005 = 1
G_Pert_different_gammas_HQ10000_G1_2_5_005 = 1
G_Pert_different_gammas_HQ10000_G1_2_7_005 = 1
G_Pert_different_gammas_HQ10000_G1_2_9_005 = 1

# Create new files (for Edd test 2, HQ, N = 10^6)
test2_G_Pert_HQ10000_G1_0_0_000 = 1
test2_G_Pert_HQ10000_G1_0_5_005 = 1
test2_G_Pert_HQ10000_G0_0_10_005 = 1
test2_G_Pert_HQ10000_G1_0_15_005 = 1
test2_G_Pert_HQ10000_G1_0_25_005 = 1

test2_G_Pert_different_gammas_HQ10000_G1_0_0_000 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_5_005 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_10_005 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_15_005 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_005 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_010 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_015 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_020 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_025 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_030 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_035 = 1
test2_G_Pert_different_gammas_HQ0000_G1_0_18_040 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_18_053 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_20_005 = 1
test2_G_Pert_different_gammas_HQ10000_G1_0_25_005 = 1

# Create new files (for Edd A, HQ, N = 10^6)

# Next 3 files already exist (test2 files)
A_G_Pert_different_gammas_HQ10000_G1_0_0_000 = 1
A_G_Pert_different_gammas_HQ10000_G1_0_5_005 = 1
A_G_Pert_different_gammas_HQ10000_G1_0_10_005 = 1

A_G_Pert_different_gammas_HQ10000_G1_0_40_005 = 1
A_G_Pert_different_gammas_HQ10000_G1_2_46_005 = 1
A_G_Pert_different_gammas_HQ10000_G0_8_47_005 = 1

# Not yet listed in readVDF_2.py
A_G_Pert_different_gammas_HQ10000_G1_0_48_009 = 1
A_G_Pert_different_gammas_HQ10000_G1_0_48_093 = 1

# Create new files (for Edd B, HQ, N = 10^6)
B_G_Pert_different_gammas_HQ10000_G1_0_0_000 = 1  # already exist (test2 files)
B_G_Pert_different_gammas_HQ10000_G1_0_5_005 = 1
B_G_Pert_different_gammas_HQ10000_G1_0_10_005 = 1
B_G_Pert_different_gammas_HQ10000_G1_0_198_000 = 1
B_G_Pert_different_gammas_HQ10000_G1_0_198_093 = 1
B_G_Pert_different_gammas_HQ10000_G1_0_199_093 = 1

# Create new files (for OM C, HQ, N = 10^6)
C_G_Pert_different_gammas_HQ10000_G1_0_0_000 = 1
C_G_Pert_different_gammas_HQ10000_G1_0_5_005 = 1
C_G_Pert_different_gammas_HQ10000_G1_0_10_005 = 1
C_G_Pert_different_gammas_HQ10000_G1_0_40_005 = 1
C_G_Pert_different_gammas_HQ10000_G1_2_46_005 = 1
C_G_Pert_different_gammas_HQ10000_G0_8_47_005 = 1

# Not yet listed in readVDF_2.py
C_G_Pert_different_gammas_HQ10000_G1_0_48_009 = 0
C_G_Pert_different_gammas_HQ10000_G1_0_48_093 = 1

# Create new files (for OM D, HQ, N = 10^6)
D_G_Pert_different_gammas_HQ10000_G1_0_0_000 = 1
D_G_Pert_different_gammas_HQ10000_G1_0_5_005 = 1
D_G_Pert_different_gammas_HQ10000_G1_0_10_005 = 1
D_G_Pert_different_gammas_HQ10000_G1_0_160_005 = 1
D_G_Pert_different_gammas_HQ10000_G1_05_196_005 = 1
D_G_Pert_different_gammas_HQ10000_G0_95_197_005 = 1

# Not yet listed in readVDF_2.py
D_G_Pert_different_gammas_HQ10000_G1_0_198_009 = 0
D_G_Pert_different_gammas_HQ10000_G1_0_198_093 = 1

# [5],[6],[7] : log9, log7, log8 : r, Theta, Phi

if B_G_Pert_different_gammas_HQ10000_G1_0_0_000:
    B_HQ0 = 'B_HQ10000_G1.0_0_000'

    # VT_i_BinAvg_sigmaT_gamma_
    # VT_i_BinAvg_sigmaT_R_middle
    # logx10_gamma_-1.50.txt' 10 9 7 8
    # _avg_logx10_gamma_%.2f.txt'

    FileLstbin1HQ10000_G1_0_0_000 = [(B_HQ0 +
                                      'VT_i_BinAvg_sigmaT_gamma_-1.50.txt',
                                      B_HQ0 +
                                      'VT_i_BinAvg_sigmaT_gamma_-1.50'),
                                     (B_HQ0 +
                                      'VR_i_BinAvg_sigmaR_gamma_-1.50.txt',
                                      B_HQ0 +
                                      'VR_i_BinAvg_sigmaR_gamma_-1.50'),
                                     (B_HQ0 +
                                      'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50.txt',
                                      B_HQ0 +
                                      'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50'),
                                     (B_HQ0 +
                                      'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50.txt',
                                      B_HQ0 +
                                      'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50'),
                                     (B_HQ0 + 'avg_logx10_gamma_-1.50.txt',
                                      B_HQ0 + 'avg_logx10_gamma_-1.50'),
                                     (B_HQ0 + 'avg_logx9_gamma_-1.50.txt',
                                      B_HQ0 + 'avg_logx9_gamma_-1.50'),
                                     (B_HQ0 + 'avg_logx7_gamma_-1.50.txt',
                                      B_HQ0 + 'avg_logx7_gamma_-1.50'),
                                     (B_HQ0 + 'avg_logx8_gamma_-1.50.txt',
                                      B_HQ0 + 'avg_logx8_gamma_-1.50')]

    FileLstbin2HQ10000_G1_0_0_000 = [(B_HQ0 +
                                      'VT_i_BinAvg_sigmaT_gamma_-2.00.txt',
                                      B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-2.00'),
                                     (B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-2.00.txt',
                                      B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-2.00'),
                                     (B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00.txt',
                                      B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00'),
                                     (B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00.txt',
                                      B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00'),
                                     (B_HQ0 + 'avg_logx10_gamma_-2.00.txt',
                                      B_HQ0 + 'avg_logx10_gamma_-2.00'),
                                     (B_HQ0 + 'avg_logx9_gamma_-2.00.txt',
                                      B_HQ0 + 'avg_logx9_gamma_-2.00'),
                                     (B_HQ0 + 'avg_logx7_gamma_-2.00.txt',
                                      B_HQ0 + 'avg_logx7_gamma_-2.00'),
                                     (B_HQ0 + 'avg_logx8_gamma_-2.00.txt',
                                      B_HQ0 + 'avg_logx8_gamma_-2.00')]

    FileLstbin3HQ10000_G1_0_0_000 = [(B_HQ0 +
                                      'VT_i_BinAvg_sigmaT_gamma_-2.50.txt',
                                      B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-2.50'),
                                     (B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-2.50.txt',
                                      B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-2.50'),
                                     (B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50.txt',
                                      B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50'),
                                     (B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50.txt',
                                      B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50'),
                                     (B_HQ0 + 'avg_logx10_gamma_-2.50.txt',
                                      B_HQ0 + 'avg_logx10_gamma_-2.50'),
                                     (B_HQ0 + 'avg_logx9_gamma_-2.50.txt',
                                      B_HQ0 + 'avg_logx9_gamma_-2.50'),
                                     (B_HQ0 + 'avg_logx7_gamma_-2.50.txt',
                                      B_HQ0 + 'avg_logx7_gamma_-2.50'),
                                     (B_HQ0 + 'avg_logx8_gamma_-2.50.txt',
                                      B_HQ0 + 'avg_logx8_gamma_-2.50')]

    FileLstbin4HQ10000_G1_0_0_000 = [(B_HQ0 +
                                      'VT_i_BinAvg_sigmaT_gamma_-3.00.txt',
                                      B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-3.00'),
                                     (B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-3.00.txt',
                                      B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-3.00'),
                                     (B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00.txt',
                                      B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00'),
                                     (B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00.txt',
                                      B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00'),
                                     (B_HQ0 + 'avg_logx10_gamma_-3.00.txt',
                                      B_HQ0 + 'avg_logx10_gamma_-3.00'),
                                     (B_HQ0 + 'avg_logx9_gamma_-3.00.txt',
                                      B_HQ0 + 'avg_logx9_gamma_-3.00'),
                                     (B_HQ0 + 'avg_logx7_gamma_-3.00.txt',
                                      B_HQ0 + 'avg_logx7_gamma_-3.00'),
                                     (B_HQ0 + 'avg_logx8_gamma_-3.00.txt',
                                      B_HQ0 + 'avg_logx8_gamma_-3.00')]

    FileLstbin5HQ10000_G1_0_0_000 = [(B_HQ0
                                      + 'VT_i_BinAvg_sigmaT_R_middle_19.95.txt',
                                      B_HQ0
                                      + 'VT_i_BinAvg_sigmaT_R_middle_19.95'
                                     ),
                                     (B_HQ0
                                      + 'VR_i_BinAvg_sigmaR_R_middle_19.95.txt',
                                      B_HQ0
                                      + 'VR_i_BinAvg_sigmaR_R_middle_19.95'),
                                     (B_HQ0
                                      + 'VTheta_i_BinAvg_sigmaTheta_R_middle_19.95.txt',
                                      B_HQ0
                                      + 'VTheta_i_BinAvg_sigmaTheta_R_middle_19.95'),
                                     (B_HQ0
                                      + 'VPhi_i_BinAvg_sigmaPhi_R_middle_19.95.txt',
                                      B_HQ0
                                      + 'VPhi_i_BinAvg_sigmaPhi_R_middle_19.95'),
                                     (B_HQ0 + 'avg_logx10_R_middle_19.95.txt',
                                      B_HQ0 + 'avg_logx10_R_middle_19.95'),
                                     (B_HQ0 + 'avg_logx9_R_middle_19.95.txt',
                                      B_HQ0 + 'avg_logx9_R_middle_19.95'),
                                     (B_HQ0 + 'avg_logx7_R_middle_19.95.txt',
                                      B_HQ0 + 'avg_logx7_R_middle_19.95'),
                                     (B_HQ0 + 'avg_logx8_R_middle_19.95.txt',
                                      B_HQ0 + 'avg_logx8_R_middle_19.95')]

    FileLstbin6HQ10000_G1_0_0_000 = [(B_HQ0 +
                                      'VT_i_BinAvg_sigmaT_R_middle_31.62.txt',
                                      B_HQ0 + 'VT_i_BinAvg_sigmaT_R_middle_31.62'),
                                     (B_HQ0 + 'VR_i_BinAvg_sigmaR_R_middle_31.62.txt',
                                      B_HQ0 + 'VR_i_BinAvg_sigmaR_R_middle_31.62'),
                                     (B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_R_middle_31.62.txt',
                                      B_HQ0 + 'VTheta_i_BinAvg_sigmaTheta_R_middle_31.62'),
                                     (B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_R_middle_31.62.txt',
                                      B_HQ0 + 'VPhi_i_BinAvg_sigmaPhi_R_middle_31.62'),
                                     (B_HQ0 + 'avg_logx10_R_middle_31.62.txt',
                                      B_HQ0 + 'avg_logx10_R_middle_31.62'),
                                     (B_HQ0 + 'avg_logx9_R_middle_31.62.txt',
                                      B_HQ0 + 'avg_logx9_R_middle_31.62'),
                                     (B_HQ0 + 'avg_logx7_R_middle_31.62.txt',
                                      B_HQ0 + 'avg_logx7_R_middle_31.62'),
                                     (B_HQ0 + 'avg_logx8_R_middle_31.62.txt',
                                      B_HQ0 + 'avg_logx8_R_middle_31.62')]

    bin1_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l)
                                                  for f, l in
                                                  FileLstbin1HQ10000_G1_0_0_000
                                                  ]
    bin2_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2HQ10000_G1_0_0_000]
    bin3_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3HQ10000_G1_0_0_000]
    bin4_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin4HQ10000_G1_0_0_000]
    datalist_bin5different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin5HQ10000_G1_0_0_000]
    datalist_bin6different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin6HQ10000_G1_0_0_000]

if B_G_Pert_different_gammas_HQ10000_G1_0_5_005:
    B_HQ36 = 'B_HQ10000_G1.0_5_005'

    FileLstbin1HQ10000_G1_0_5_005 = [(B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-1.50.txt',
                                      B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-1.50'),
                                     (B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-1.50.txt',
                                      B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-1.50'),
                                     (B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50.txt',
                                      B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50'),
                                     (B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50.txt',
                                      B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50'),
                                     (B_HQ36 + 'avg_logx10_gamma_-1.50.txt',
                                      B_HQ36 + 'avg_logx10_gamma_-1.50'),
                                     (B_HQ36 + 'avg_logx9_gamma_-1.50.txt',
                                      B_HQ36 + 'avg_logx9_gamma_-1.50'),
                                     (B_HQ36 + 'avg_logx7_gamma_-1.50.txt',
                                      B_HQ36 + 'avg_logx7_gamma_-1.50'),
                                     (B_HQ36 + 'avg_logx8_gamma_-1.50.txt',
                                      B_HQ36 + 'avg_logx8_gamma_-1.50')]

    FileLstbin2HQ10000_G1_0_5_005 = [(B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-2.00.txt',
                                      B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-2.00'),
                                     (B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-2.00.txt',
                                      B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-2.00'),
                                     (B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00.txt',
                                      B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00'),
                                     (B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00.txt',
                                      B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00'),
                                     (B_HQ36 + 'avg_logx10_gamma_-2.00.txt',
                                      B_HQ36 + 'avg_logx10_gamma_-2.00'),
                                     (B_HQ36 + 'avg_logx9_gamma_-2.00.txt',
                                      B_HQ36 + 'avg_logx9_gamma_-2.00'),
                                     (B_HQ36 + 'avg_logx7_gamma_-2.00.txt',
                                      B_HQ36 + 'avg_logx7_gamma_-2.00'),
                                     (B_HQ36 + 'avg_logx8_gamma_-2.00.txt',
                                      B_HQ36 + 'avg_logx8_gamma_-2.00')]

    FileLstbin3HQ10000_G1_0_5_005 = [(B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-2.50.txt',
                                      B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-2.50'),
                                     (B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-2.50.txt',
                                      B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-2.50'),
                                     (B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50.txt',
                                      B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50'),
                                     (B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50.txt',
                                      B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50'),
                                     (B_HQ36 + 'avg_logx10_gamma_-2.50.txt',
                                      B_HQ36 + 'avg_logx10_gamma_-2.50'),
                                     (B_HQ36 + 'avg_logx9_gamma_-2.50.txt',
                                      B_HQ36 + 'avg_logx9_gamma_-2.50'),
                                     (B_HQ36 + 'avg_logx7_gamma_-2.50.txt',
                                      B_HQ36 + 'avg_logx7_gamma_-2.50'),
                                     (B_HQ36 + 'avg_logx8_gamma_-2.50.txt',
                                      B_HQ36 + 'avg_logx8_gamma_-2.50')]

    FileLstbin4HQ10000_G1_0_5_005 = [(B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-3.00.txt',
                                      B_HQ36 + 'VT_i_BinAvg_sigmaT_gamma_-3.00'),
                                     (B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-3.00.txt',
                                      B_HQ36 + 'VR_i_BinAvg_sigmaR_gamma_-3.00'),
                                     (B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00.txt',
                                      B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00'),
                                     (B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00.txt',
                                      B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00'),
                                     (B_HQ36 + 'avg_logx10_gamma_-3.00.txt',
                                      B_HQ36 + 'avg_logx10_gamma_-3.00'),
                                     (B_HQ36 + 'avg_logx9_gamma_-3.00.txt',
                                      B_HQ36 + 'avg_logx9_gamma_-3.00'),
                                     (B_HQ36 + 'avg_logx7_gamma_-3.00.txt',
                                      B_HQ36 + 'avg_logx7_gamma_-3.00'),
                                     (B_HQ36 + 'avg_logx8_gamma_-3.00.txt',
                                      B_HQ36 + 'avg_logx8_gamma_-3.00')]

    FileLstbin5HQ10000_G1_0_5_005 = [(B_HQ36 + 'VT_i_BinAvg_sigmaT_R_middle_19.95.txt',
                                      B_HQ36 + 'VT_i_BinAvg_sigmaT_R_middle_19.95'),
                                     (B_HQ36 + 'VR_i_BinAvg_sigmaR_R_middle_19.95.txt',
                                      B_HQ36 + 'VR_i_BinAvg_sigmaR_R_middle_19.95'),
                                     (B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_R_middle_19.95.txt',
                                      B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_R_middle_19.95'),
                                     (B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_R_middle_19.95.txt',
                                      B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_R_middle_19.95'),
                                     (B_HQ36 + 'avg_logx10_R_middle_19.95.txt',
                                      B_HQ36 + 'avg_logx10_R_middle_19.95'),
                                     (B_HQ36 + 'avg_logx9_R_middle_19.95.txt',
                                      B_HQ36 + 'avg_logx9_R_middle_19.95'),
                                     (B_HQ36 + 'avg_logx7_R_middle_19.95.txt',
                                      B_HQ36 + 'avg_logx7_R_middle_19.95'),
                                     (B_HQ36 + 'avg_logx8_R_middle_19.95.txt',
                                      B_HQ36 + 'avg_logx8_R_middle_19.95')]

    FileLstbin6HQ10000_G1_0_5_005 = [(B_HQ36 + 'VT_i_BinAvg_sigmaT_R_middle_31.62.txt',
                                      B_HQ36 + 'VT_i_BinAvg_sigmaT_R_middle_31.62'),
                                     (B_HQ36 + 'VR_i_BinAvg_sigmaR_R_middle_31.62.txt',
                                      B_HQ36 + 'VR_i_BinAvg_sigmaR_R_middle_31.62'),
                                     (B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_R_middle_31.62.txt',
                                      B_HQ36 + 'VTheta_i_BinAvg_sigmaTheta_R_middle_31.62'),
                                     (B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_R_middle_31.62.txt',
                                      B_HQ36 + 'VPhi_i_BinAvg_sigmaPhi_R_middle_31.62'),
                                     (B_HQ36 + 'avg_logx10_R_middle_31.62.txt',
                                      B_HQ36 + 'avg_logx10_R_middle_31.62'),
                                     (B_HQ36 + 'avg_logx9_R_middle_31.62.txt',
                                      B_HQ36 + 'avg_logx9_R_middle_31.62'),
                                     (B_HQ36 + 'avg_logx7_R_middle_31.62.txt',
                                      B_HQ36 + 'avg_logx7_R_middle_31.62'),
                                     (B_HQ36 + 'avg_logx8_R_middle_31.62.txt',
                                      B_HQ36 + 'avg_logx8_R_middle_31.62')]

    # This works.
    # FileLstbin1HQ10000_G1_0_5_005 =
    # [tuple(map(lambda i: str.replace(i, 'VT_sigmaT_gamma_',
    #  'VT_i_BinAvg_sigmaT_gamma_'), tup))
    # for tup in FileLstbin1HQ10000_G1_0_5_005]
    # print('FileLstbin1HQ10000_G1_0_5_005', FileLstbin1HQ10000_G1_0_5_005)

    bin1_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin1HQ10000_G1_0_5_005]
    bin2_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2HQ10000_G1_0_5_005]
    bin3_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3HQ10000_G1_0_5_005]
    bin4_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin4HQ10000_G1_0_5_005]
    datalist_bin5different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin5HQ10000_G1_0_5_005]
    datalist_bin6different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin6HQ10000_G1_0_5_005]

if B_G_Pert_different_gammas_HQ10000_G1_0_10_005:
    B_HQ66 = 'B_HQ10000_G1.0_10_005'

    FileLstbin1HQ10000_G1_0_10_005 = [(B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-1.50.txt',
                                       B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-1.50'),
                                      (B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-1.50.txt',
                                       B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-1.50'),
                                      (B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50.txt',
                                       B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50'),
                                      (B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50.txt',
                                       B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50'),
                                      (B_HQ66 + 'avg_logx10_gamma_-1.50.txt',
                                       B_HQ66 + 'avg_logx10_gamma_-1.50'),
                                      (B_HQ66 + 'avg_logx9_gamma_-1.50.txt',
                                       B_HQ66 + 'avg_logx9_gamma_-1.50'),
                                      (B_HQ66 + 'avg_logx7_gamma_-1.50.txt',
                                       B_HQ66 + 'avg_logx7_gamma_-1.50'),
                                      (B_HQ66 + 'avg_logx8_gamma_-1.50.txt',
                                       B_HQ66 + 'avg_logx8_gamma_-1.50')]

    FileLstbin2HQ10000_G1_0_10_005 = [(B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-2.00.txt',
                                       B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-2.00'),
                                      (B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-2.00.txt',
                                       B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-2.00'),
                                      (B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00.txt',
                                       B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00'),
                                      (B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00.txt',
                                       B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00'),
                                      (B_HQ66 + 'avg_logx10_gamma_-2.00.txt',
                                       B_HQ66 + 'avg_logx10_gamma_-2.00'),
                                      (B_HQ66 + 'avg_logx9_gamma_-2.00.txt',
                                       B_HQ66 + 'avg_logx9_gamma_-2.00'),
                                      (B_HQ66 + 'avg_logx7_gamma_-2.00.txt',
                                       B_HQ66 + 'avg_logx7_gamma_-2.00'),
                                      (B_HQ66 + 'avg_logx8_gamma_-2.00.txt',
                                       B_HQ66 + 'avg_logx8_gamma_-2.00')]

    FileLstbin3HQ10000_G1_0_10_005 = [(B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-2.50.txt',
                                       B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-2.50'),
                                      (B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-2.50.txt',
                                       B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-2.50'),
                                      (B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50.txt',
                                       B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50'),
                                      (B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50.txt',
                                       B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50'),
                                      (B_HQ66 + 'avg_logx10_gamma_-2.50.txt',
                                       B_HQ66 + 'avg_logx10_gamma_-2.50'),
                                      (B_HQ66 + 'avg_logx9_gamma_-2.50.txt',
                                       B_HQ66 + 'avg_logx9_gamma_-2.50'),
                                      (B_HQ66 + 'avg_logx7_gamma_-2.50.txt',
                                       B_HQ66 + 'avg_logx7_gamma_-2.50'),
                                      (B_HQ66 + 'avg_logx8_gamma_-2.50.txt',
                                       B_HQ66 + 'avg_logx8_gamma_-2.50')]

    FileLstbin4HQ10000_G1_0_10_005 = [(B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-3.00.txt',
                                       B_HQ66 + 'VT_i_BinAvg_sigmaT_gamma_-3.00'),
                                      (B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-3.00.txt',
                                       B_HQ66 + 'VR_i_BinAvg_sigmaR_gamma_-3.00'),
                                      (B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00.txt',
                                       B_HQ66 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00'),
                                      (B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00.txt',
                                       B_HQ66 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00'),
                                      (B_HQ66 + 'avg_logx10_gamma_-3.00.txt',
                                       B_HQ66 + 'avg_logx10_gamma_-3.00'),
                                      (B_HQ66 + 'avg_logx9_gamma_-3.00.txt',
                                       B_HQ66 + 'avg_logx9_gamma_-3.00'),
                                      (B_HQ66 + 'avg_logx7_gamma_-3.00.txt',
                                       B_HQ66 + 'avg_logx7_gamma_-3.00'),
                                      (B_HQ66 + 'avg_logx8_gamma_-3.00.txt',
                                       B_HQ66 + 'avg_logx8_gamma_-3.00')]

    bin1_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin1HQ10000_G1_0_10_005 ]
    bin2_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2HQ10000_G1_0_10_005 ]
    bin3_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3HQ10000_G1_0_10_005 ]
    bin4_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin4HQ10000_G1_0_10_005 ]

if B_G_Pert_different_gammas_HQ10000_G1_0_198_000:
    B_HQ294 = 'B_HQ10000_G1.0_198_000'

    FileLstbin1HQ10000_G1_0_198_000 = [(B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-1.50.txt',
                                        B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-1.50'),
                                       (B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-1.50.txt',
                                        B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-1.50'),
                                       (B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50.txt',
                                        B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50'),
                                       (B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50.txt',
                                        B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50'),
                                       (B_HQ294 + 'avg_logx10_gamma_-1.50.txt',
                                        B_HQ294 + 'avg_logx10_gamma_-1.50'),
                                       (B_HQ294 + 'avg_logx9_gamma_-1.50.txt',
                                        B_HQ294 + 'avg_logx9_gamma_-1.50'),
                                       (B_HQ294 + 'avg_logx7_gamma_-1.50.txt',
                                        B_HQ294 + 'avg_logx7_gamma_-1.50'),
                                       (B_HQ294 + 'avg_logx8_gamma_-1.50.txt',
                                        B_HQ294 + 'avg_logx8_gamma_-1.50')]

    FileLstbin2HQ10000_G1_0_198_000 = [(B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-2.00.txt',
                                        B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-2.00'),
                                       (B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-2.00.txt',
                                        B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-2.00'),
                                       (B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00.txt',
                                        B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00'),
                                       (B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00.txt',
                                        B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00'),
                                       (B_HQ294 + 'avg_logx10_gamma_-2.00.txt',
                                        B_HQ294 + 'avg_logx10_gamma_-2.00'),
                                       (B_HQ294 + 'avg_logx9_gamma_-2.00.txt',
                                        B_HQ294 + 'avg_logx9_gamma_-2.00'),
                                       (B_HQ294 + 'avg_logx7_gamma_-2.00.txt',
                                        B_HQ294 + 'avg_logx7_gamma_-2.00'),
                                       (B_HQ294 + 'avg_logx8_gamma_-2.00.txt',
                                        B_HQ294 + 'avg_logx8_gamma_-2.00')]

    FileLstbin3HQ10000_G1_0_198_000 = [(B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-2.50.txt',
                                        B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-2.50'),
                                       (B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-2.50.txt',
                                        B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-2.50'),
                                       (B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50.txt',
                                        B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50'),
                                       (B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50.txt',
                                        B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50'),
                                       (B_HQ294 + 'avg_logx10_gamma_-2.50.txt',
                                        B_HQ294 + 'avg_logx10_gamma_-2.50'),
                                       (B_HQ294 + 'avg_logx9_gamma_-2.50.txt',
                                        B_HQ294 + 'avg_logx9_gamma_-2.50'),
                                       (B_HQ294 + 'avg_logx7_gamma_-2.50.txt',
                                        B_HQ294 + 'avg_logx7_gamma_-2.50'),
                                       (B_HQ294 + 'avg_logx8_gamma_-2.50.txt',
                                        B_HQ294 + 'avg_logx8_gamma_-2.50')]

    FileLstbin4HQ10000_G1_0_198_000 = [(B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-3.00.txt',
                                        B_HQ294 + 'VT_i_BinAvg_sigmaT_gamma_-3.00'),
                                       (B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-3.00.txt',
                                        B_HQ294 + 'VR_i_BinAvg_sigmaR_gamma_-3.00'),
                                       (B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00.txt',
                                        B_HQ294 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00'),
                                       (B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00.txt',
                                        B_HQ294 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00'),
                                       (B_HQ294 + 'avg_logx10_gamma_-3.00.txt',
                                        B_HQ294 + 'avg_logx10_gamma_-3.00'),
                                       (B_HQ294 + 'avg_logx9_gamma_-3.00.txt',
                                        B_HQ294 + 'avg_logx9_gamma_-3.00'),
                                       (B_HQ294 + 'avg_logx7_gamma_-3.00.txt',
                                        B_HQ294 + 'avg_logx7_gamma_-3.00'),
                                       (B_HQ294 + 'avg_logx8_gamma_-3.00.txt',
                                        B_HQ294 + 'avg_logx8_gamma_-3.00')]

    bin1_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin1HQ10000_G1_0_198_000]
    bin2_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2HQ10000_G1_0_198_000]
    bin3_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3HQ10000_G1_0_198_000]
    bin4_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin4HQ10000_G1_0_198_000]

if B_G_Pert_different_gammas_HQ10000_G1_0_198_093:
    B_HQ382 = 'B_HQ10000_G1.0_198_093'

    FileLstbin1HQ10000_G1_0_198_093 = [(B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-1.50.txt',
                                        B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-1.50'),
                                       (B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-1.50.txt',
                                        B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-1.50'),
                                       (B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50.txt',
                                        B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50'),
                                       (B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50.txt',
                                        B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50'),
                                       (B_HQ382 + 'avg_logx10_gamma_-1.50.txt',
                                        B_HQ382 + 'avg_logx10_gamma_-1.50'),
                                       (B_HQ382 + 'avg_logx9_gamma_-1.50.txt',
                                        B_HQ382 + 'avg_logx9_gamma_-1.50'),
                                       (B_HQ382 + 'avg_logx7_gamma_-1.50.txt',
                                        B_HQ382 + 'avg_logx7_gamma_-1.50'),
                                       (B_HQ382 + 'avg_logx8_gamma_-1.50.txt',
                                        B_HQ382 + 'avg_logx8_gamma_-1.50')]

    FileLstbin2HQ10000_G1_0_198_093 = [(B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-2.00.txt',
                                        B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-2.00'),
                                       (B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-2.00.txt',
                                        B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-2.00'),
                                       (B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00.txt',
                                        B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00'),
                                       (B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00.txt',
                                        B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00'),
                                       (B_HQ382 + 'avg_logx10_gamma_-2.00.txt',
                                        B_HQ382 + 'avg_logx10_gamma_-2.00'),
                                       (B_HQ382 + 'avg_logx9_gamma_-2.00.txt',
                                        B_HQ382 + 'avg_logx9_gamma_-2.00'),
                                       (B_HQ382 + 'avg_logx7_gamma_-2.00.txt',
                                        B_HQ382 + 'avg_logx7_gamma_-2.00'),
                                       (B_HQ382 + 'avg_logx8_gamma_-2.00.txt',
                                        B_HQ382 + 'avg_logx8_gamma_-2.00')]

    FileLstbin3HQ10000_G1_0_198_093 = [(B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-2.50.txt',
                                        B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-2.50'),
                                       (B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-2.50.txt',
                                        B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-2.50'),
                                       (B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50.txt',
                                        B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50'),
                                       (B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50.txt',
                                        B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50'),
                                       (B_HQ382 + 'avg_logx10_gamma_-2.50.txt',
                                        B_HQ382 + 'avg_logx10_gamma_-2.50'),
                                       (B_HQ382 + 'avg_logx9_gamma_-2.50.txt',
                                        B_HQ382 + 'avg_logx9_gamma_-2.50'),
                                       (B_HQ382 + 'avg_logx7_gamma_-2.50.txt',
                                        B_HQ382 + 'avg_logx7_gamma_-2.50'),
                                       (B_HQ382 + 'avg_logx8_gamma_-2.50.txt',
                                        B_HQ382 + 'avg_logx8_gamma_-2.50')]

    FileLstbin4HQ10000_G1_0_198_093 = [(B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-3.00.txt',
                                        B_HQ382 + 'VT_i_BinAvg_sigmaT_gamma_-3.00'),
                                       (B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-3.00.txt',
                                        B_HQ382 + 'VR_i_BinAvg_sigmaR_gamma_-3.00'),
                                       (B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00.txt',
                                        B_HQ382 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00'),
                                       (B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00.txt',
                                        B_HQ382 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00'),
                                       (B_HQ382 + 'avg_logx10_gamma_-3.00.txt',
                                        B_HQ382 + 'avg_logx10_gamma_-3.00'),
                                       (B_HQ382 + 'avg_logx9_gamma_-3.00.txt',
                                        B_HQ382 + 'avg_logx9_gamma_-3.00'),
                                       (B_HQ382 + 'avg_logx7_gamma_-3.00.txt',
                                        B_HQ382 + 'avg_logx7_gamma_-3.00'),
                                       (B_HQ382 + 'avg_logx8_gamma_-3.00.txt',
                                        B_HQ382 + 'avg_logx8_gamma_-3.00')]

    bin1_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in FileLstbin1HQ10000_G1_0_198_093]
    bin2_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2HQ10000_G1_0_198_093]
    bin3_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3HQ10000_G1_0_198_093]
    bin4_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in FileLstbin4HQ10000_G1_0_198_093]

if B_G_Pert_different_gammas_HQ10000_G1_0_199_093:
    B_HQ475 = 'B_HQ10000_G1.0_199_093'

    FileLstbin1HQ10000_G1_0_199_093 = [(B_HQ475 + 'VT_i_BinAvg_sigmaT_gamma_-1.50.txt',
                                        B_HQ475 + 'VT_i_BinAvg_sigmaT_gamma_-1.50'),
                                       (B_HQ475 + 'VR_i_BinAvg_sigmaR_gamma_-1.50.txt',
                                        B_HQ475 + 'VR_i_BinAvg_sigmaR_gamma_-1.50'),
                                       (B_HQ475 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50.txt',
                                        B_HQ475 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-1.50'),
                                       (B_HQ475 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50.txt',
                                        B_HQ475 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-1.50'),
                                       (B_HQ475 + 'avg_logx10_gamma_-1.50.txt',
                                        B_HQ475 + 'avg_logx10_gamma_-1.50'),
                                       (B_HQ475 + 'avg_logx9_gamma_-1.50.txt',
                                        B_HQ475 + 'avg_logx9_gamma_-1.50'),
                                       (B_HQ475 + 'avg_logx7_gamma_-1.50.txt',
                                        B_HQ475 + 'avg_logx7_gamma_-1.50'),
                                       (B_HQ475 + 'avg_logx8_gamma_-1.50.txt',
                                        B_HQ475 + 'avg_logx8_gamma_-1.50')]

    FileLstbin2HQ10000_G1_0_199_093 = [(B_HQ475 + 'VT_i_BinAvg_sigmaT_gamma_-2.00.txt',
                                        B_HQ475 + 'VT_i_BinAvg_sigmaT_gamma_-2.00'),
                                       (B_HQ475 + 'VR_i_BinAvg_sigmaR_gamma_-2.00.txt',
                                        B_HQ475 + 'VR_i_BinAvg_sigmaR_gamma_-2.00'),
                                       (B_HQ475 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00.txt',
                                        B_HQ475 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.00'),
                                       (B_HQ475 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00.txt',
                                        B_HQ475 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.00'),
                                       (B_HQ475 + 'avg_logx10_gamma_-2.00.txt',
                                        B_HQ475 + 'avg_logx10_gamma_-2.00'),
                                       (B_HQ475 + 'avg_logx9_gamma_-2.00.txt',
                                        B_HQ475 + 'avg_logx9_gamma_-2.00'),
                                       (B_HQ475 + 'avg_logx7_gamma_-2.00.txt',
                                        B_HQ475 + 'avg_logx7_gamma_-2.00'),
                                       (B_HQ475 + 'avg_logx8_gamma_-2.00.txt',
                                        B_HQ475 + 'avg_logx8_gamma_-2.00')]

    FileLstbin3HQ10000_G1_0_199_093 = [(B_HQ475 + 'VT_i_BinAvg_sigmaT_gamma_-2.50.txt',
                                        B_HQ475 + 'VT_i_BinAvg_sigmaT_gamma_-2.50'),
                                       (B_HQ475 + 'VR_i_BinAvg_sigmaR_gamma_-2.50.txt',
                                        B_HQ475 + 'VR_i_BinAvg_sigmaR_gamma_-2.50'),
                                       (B_HQ475 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50.txt',
                                        B_HQ475 + 'VTheta_i_BinAvg_sigmaTheta_gamma_-2.50'),
                                       (B_HQ475 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50.txt',
                                        B_HQ475 + 'VPhi_i_BinAvg_sigmaPhi_gamma_-2.50'),
                                       (B_HQ475 + 'avg_logx10_gamma_-2.50.txt',
                                        B_HQ475 + 'avg_logx10_gamma_-2.50'),
                                       (B_HQ475 + 'avg_logx9_gamma_-2.50.txt',
                                        B_HQ475 + 'avg_logx9_gamma_-2.50'),
                                       (B_HQ475 + 'avg_logx7_gamma_-2.50.txt',
                                        B_HQ475 + 'avg_logx7_gamma_-2.50'),
                                       (B_HQ475 + 'avg_logx8_gamma_-2.50.txt',
                                        B_HQ475 + 'avg_logx8_gamma_-2.50')]

    FileLstbin4HQ10000_G1_0_199_093 = [(B_HQ475
                                        + 'VT_i_BinAvg_sigmaT_gamma_-3.00.txt',
                                        B_HQ475
                                        + 'VT_i_BinAvg_sigmaT_gamma_-3.00'),
                                       (B_HQ475
                                        + 'VR_i_BinAvg_sigmaR_gamma_-3.00.txt',
                                        B_HQ475
                                        + 'VR_i_BinAvg_sigmaR_gamma_-3.00'),
                                       (B_HQ475
                                        + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00.txt',
                                        B_HQ475
                                        + 'VTheta_i_BinAvg_sigmaTheta_gamma_-3.00'),
                                       (B_HQ475
                                        + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00.txt',
                                        B_HQ475
                                        + 'VPhi_i_BinAvg_sigmaPhi_gamma_-3.00'),
                                       (B_HQ475 + 'avg_logx10_gamma_-3.00.txt',
                                        B_HQ475 + 'avg_logx10_gamma_-3.00'),
                                       (B_HQ475 + 'avg_logx9_gamma_-3.00.txt',
                                        B_HQ475 + 'avg_logx9_gamma_-3.00'),
                                       (B_HQ475 + 'avg_logx7_gamma_-3.00.txt',
                                        B_HQ475 + 'avg_logx7_gamma_-3.00'),
                                       (B_HQ475 + 'avg_logx8_gamma_-3.00.txt',
                                        B_HQ475 + 'avg_logx8_gamma_-3.00')]

    bin1_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l)
                                                    for f, l
                                                    in FileLstbin1HQ10000_G1_0_199_093]
    bin2_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l)
                                                    for f, l
                                                    in FileLstbin2HQ10000_G1_0_199_093]
    bin3_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l)
                                                    for f, l
                                                    in FileLstbin3HQ10000_G1_0_199_093]
    bin4_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l)
                                                    for f, l
                                                    in FileLstbin4HQ10000_G1_0_199_093]

if Fig1_vr_vPhi_vTheta:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    def Plt(i, data, cls, Label=False):
        if Label:
            return exec(f"ax{i}.plot({data}[0][:, 0],\
                          {data}[0][:, 1], {cls}, label={Label},\
                          lw=2, ms=7)")
        return exec(f"ax{i}.plot({data}[0][:, 0],\
                      {data}[0][:, 1], {cls}, lw=2, ms=7)")

    if test:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        Plt(1, bin1_HQ10000_G1_2_1_005[1], 'g--')
        # data = bin1_HQ10000_G1_2_1_005[1][0]
        # ax1.plot(data[:, 0], data[:, 1], 'g--', lw=2, ms=7)
        Plt(1, bin1_HQ10000_G1_2_1_005[2], 'r--')
        Plt(1, bin1_HQ10000_G1_2_1_005[3], 'k--')

        Plt(1, bin2_HQ10000_G1_2_1_005[1], 'g:')
        Plt(1, bin2_HQ10000_G1_2_1_005[2], 'r:')
        Plt(1, bin2_HQ10000_G1_2_1_005[3], 'k:')

        Plt(1, bin3_HQ10000_G1_2_1_005[1], 'g-.')
        Plt(1, bin3_HQ10000_G1_2_1_005[2], 'r-.')
        Plt(1, bin3_HQ10000_G1_2_1_005[3], 'k-.')

        Plt(1, bin4_HQ10000_G1_2_1_005[1], 'g', r'$v_r$')
        # data = bin4_HQ10000_G1_2_1_005[1][0]
        # ax1.plot(data[:, 0], data[:, 1], 'g', label=r'$v_r$', lw=2, ms=7)
        Plt(1, bin4_HQ10000_G1_2_1_005[2], 'r', r'$v_{\Theta}$')
        Plt(1, bin4_HQ10000_G1_2_1_005[3], 'k', r'$v_{\Phi}$')

        ax1.set_ylabel(r'$f\left(u \right)$', fontsize=20)
        ax1.set_title(f'File = {HQ12}', fontsize=20)

        Plt(2, bin1_HQ10000_G1_2_1_005[5], 'g--')
        Plt(2, bin1_HQ10000_G1_2_1_005[6], 'r--')
        Plt(2, bin1_HQ10000_G1_2_1_005[7], 'k--', r'$\gamma = -1.5$')

        Plt(2, bin2_HQ10000_G1_2_1_005[5], 'g:')
        Plt(2, bin2_HQ10000_G1_2_1_005[6], 'r:')
        Plt(2, bin2_HQ10000_G1_2_1_005[7], 'k:', r'$\gamma = -2.0$')

        Plt(2, bin3_HQ10000_G1_2_1_005[5], 'g-.')
        Plt(2, bin3_HQ10000_G1_2_1_005[6], 'r-.')
        Plt(2, bin3_HQ10000_G1_2_1_005[7], 'k-.', r'$\gamma = -2.5 $')

        Plt(2, bin4_HQ10000_G1_2_1_005[5], 'g')
        Plt(2, bin4_HQ10000_G1_2_1_005[6], 'r')
        Plt(2, bin4_HQ10000_G1_2_1_005[7], 'k', r'$\gamma = -3.0 $')

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)

        Plt(3, bin1_HQ10000_G1_2_1_005[1], 'g--', r'$\gamma = -1.5 $')
        Plt(3, bin1_HQ10000_G1_2_1_005[2], 'r--')
        Plt(3, bin1_HQ10000_G1_2_1_005[3], 'k--')

        Plt(3, bin2_HQ10000_G1_2_1_005[1], 'g:', r'$\gamma = -2.0 $')
        Plt(3, bin2_HQ10000_G1_2_1_005[2], 'r:')
        Plt(3, bin2_HQ10000_G1_2_1_005[3], 'k:')

        Plt(3, bin3_HQ10000_G1_2_1_005[1], 'g-.', r'$\gamma = -2.5$')
        Plt(3, bin3_HQ10000_G1_2_1_005[2], 'r-.')
        Plt(3, bin3_HQ10000_G1_2_1_005[3], 'k-.')

        Plt(3, bin4_HQ10000_G1_2_1_005[1], 'g', r'$\gamma = -3.0$')
        Plt(3, bin4_HQ10000_G1_2_1_005[2], 'r')
        Plt(3, bin4_HQ10000_G1_2_1_005[3], 'k')

        ax3.set_xlabel(r'$u_r$, $u_{\Theta}$ and $u_{\Phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f(u) \right)$', fontsize=20)
        ax3.set_yscale('log')

        Plt(4, bin1_HQ10000_G1_2_1_005[5], 'g--', r'$\gamma = -1.5$')
        Plt(4, bin1_HQ10000_G1_2_1_005[6], 'r--')
        Plt(4, bin1_HQ10000_G1_2_1_005[7], 'k--')

        Plt(4, bin2_HQ10000_G1_2_1_005[5], 'g:', r'$\gamma = -2.0$')
        Plt(4, bin2_HQ10000_G1_2_1_005[6], 'r:')
        Plt(4, bin2_HQ10000_G1_2_1_005[7], 'k:')

        Plt(4, bin3_HQ10000_G1_2_1_005[5], 'g-.', r'$\gamma = -2.5$')
        Plt(4, bin3_HQ10000_G1_2_1_005[6], 'r-.')
        Plt(4, bin3_HQ10000_G1_2_1_005[7], 'k-.')

        Plt(4, bin4_HQ10000_G1_2_1_005[5], 'g', r'$\gamma = -3.0$')
        Plt(4, bin4_HQ10000_G1_2_1_005[6], 'r')
        Plt(4, bin4_HQ10000_G1_2_1_005[7], 'k')

        ax4.set_xlabel(r'$\log \left(|u_rn|, u_rp \right)$,\
                       $\log \left(|u_{\Theta}n|, u_{\Theta}p \right)$ and\
                       $\log \left( |u_{\Phi}n|, u_{\Phi}p \right)$',
                       fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                       \right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

    if test2:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[1], 'g--')
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[2], 'r--')
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[3], 'k--')

        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_0_000[1], 'g:')
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_0_000[2], 'r:')
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_0_000[3], 'k:')

        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_0_000[1], 'g-.')
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_0_000[2], 'r-.')
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_0_000[3], 'k-.')

        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_0_000[1], 'g', r'$v_r$')
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_0_000[2], 'r', r'$v_{\Theta}$')
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_0_000[3], 'k', r'$v_{\Phi}$')

        ax1.set_ylabel(r'$f\left(u \right)$', fontsize=20)
        ax1.set_title(r' File = %s' % test2_HQ0, fontsize=20)

        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_0_000[5], 'g--')
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_0_000[6], 'r--')        
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_0_000[7], 'k--',
            r'$\gamma = -1.5$')

        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_0_000[5], 'g:')
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_0_000[6], 'r:')
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_0_000[7], 'k:',
            r'$\gamma = -2.0$')

        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_0_000[5], 'g-.')
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_0_000[6], 'r-.')
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_0_000[7], 'k-.',
            r'$\gamma = -2.5$')

        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_0_000[5], 'g')
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_0_000[6], 'r')
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_0_000[7], 'k',
            r'$\gamma = -3.0$')

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:, 0], data[:, 1], 'g--', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:, 0], data[:, 1], 'r--', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:, 0], data[:, 1], 'k--', lw=2, ms=7)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:, 0], data[:, 1], 'g:', lw=4, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:, 0], data[:, 1], 'r:', lw=4, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:, 0], data[:, 1], 'k:', lw=2, ms=7)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:, 0], data[:, 1], 'g-.', lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:, 0], data[:, 1], 'r-.', lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:, 0], data[:, 1], 'k-.', lw=2, ms=7)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:, 0], data[:, 1], 'g', label=r'$v_r$', lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:, 0], data[:, 1], 'r', label=r'$v_{\Theta}$',
                 lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:, 0], data[:, 1], 'k',
                 label=r'$v_{\Phi}$', lw=2, ms=7)

        ax3.set_xlabel(r'$u_r$, $u_{\Theta}$ and $u_{\Phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f(u) \right)$', fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:, 0], data[:, 1], 'g--', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:, 0], data[:, 1], 'r--', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:, 0], data[:, 1], 'k--', lw=2, ms=7)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:, 0], data[:, 1], 'g:', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:, 0], data[:, 1], 'r:', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:, 0], data[:, 1], 'k:', lw=2, ms=7)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:, 0], data[:, 1], 'g-.', lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:, 0], data[:, 1], 'r-.', lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:, 0], data[:, 1], 'k-.', lw=2, ms=7)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)

        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                       |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                       |u_{\Phi}n|,u_{\Phi}p \right)$',
                       fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left(|u_n|,u_p \right)\
                       \right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

if Fig1_vr_vPhi_vTheta_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    if test:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        data, label = bin2_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1], 'g', lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, 'c.-', lw=3,
                 label=r'$ radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        data, label = bin2_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, '.-', lw=3, 'Pink',
                 label=r'$ \Theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        data, label = bin2_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, '.-', lw=3, 'Brown',
                 label=r'$ \Phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Fits to file = %s, $\gamma = -2.0$' % HQ12,
                      fontsize=20)

        data, label = bin2_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:, 0], data[:, 1], 'g',
                 label=r'$ \frac{v_r}{\sigma_r} $', lw=2, ms=7)
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, 'c.-', lw=3,
                 label=r'$ radial: a\log xe^{-b \log(x)^2}$, $a,b = %.3f,%.3f$'
                 % (popt[0], popt[1]))

        data, label = bin2_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'$ \frac{v_{\Theta}}{\sigma_{\Theta}} $', lw=2, ms=7)
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, '.-', lw=3, 'Pink',
                 label=r'$ \Theta: a\log xe^{-b \log(x)^2}$, $a,b = %.3f,%.3f$'
                 % (popt[0], popt[1]))

        data, label = bin2_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:, 0], data[:, 1], 'k',
                 label=r'$ \frac{v_{\Phi}}{\sigma_{\Phi}}$', lw=2, ms=7)
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, '.-', lw=3, 'Brown',
                 label=r'$ \Phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)

        data, label = bin2_HQ10000_G1_2_1_005[1]
        ax3.plot(data[:, 0], data[:, 1], 'g',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[2]
        ax3.plot(data[:, 0], data[:, 1], 'r', lw=4, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[3]
        ax3.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)

        ax3.set_xlabel(r'$ u_r $, $u_{\Theta}$ and $u_{\Phi}$',
                       fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin2_HQ10000_G1_2_1_005[5]
        ax4.plot(data[:, 0], data[:, 1], 'g',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[6]
        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[7]
        ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)

        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                       |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                       |u_{\Phi}n|,u_{\Phi}p \right)$',
                       fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
                        u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

    if test2:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:, 0], data[:, 1], 'g', lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, 'c.-', lw=3,
                 label=r'$ radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=4, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, '.-', lw=3, 'Pink',
                 label=r'$ \Theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        popt, pcov = curve_fit(func_2, data[:, 0], data[:, 1])
        y_fit = func_2(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, '.-', lw=3, 'Brown',
                 label=r'$ \Phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Fits to file = %s, $\gamma = -2.0 $' % test2_HQ0,
                      fontsize=20)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:, 0], data[:, 1], 'g',
                 label=r'$ \frac{v_r}{\sigma_r} $', lw=2, ms=7)
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, 'c.-', lw=3,
                 label=r'$ radial: a\log xe^{-b \log(x)^2}$, $a,b = %.3f,%.3f$'
                 % (popt[0], popt[1]))

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'$ \frac{v_{\Theta}}{\sigma_{\Theta}} $', lw=2, ms=7)
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, '.-', lw=3, 'Pink',
                 label=r'$ \Theta: a\log xe^{-b \log(x)^2}$, $a,b = %.3f,%.3f$'
                 % (popt[0], popt[1]))

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:, 0], data[:, 1], 'k',
                 label=r'$ \frac{v_{\Phi}}{\sigma_{\Phi}} $', lw=2, ms=7)
        popt, pcov = curve_fit(func_1_log, data[:, 0], data[:, 1])
        y_fit = func_1_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, '.-', lw=3, 'Brown',
                 label=r'$ \Phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:, 0], data[:, 1], 'g',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:, 0], data[:, 1], 'r', lw=4, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)

        ax3.set_xlabel(r'$ u_r $, $u_{\Theta}$ and $u_{\Phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:, 0], data[:, 1], 'g',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)

        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                       |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                       |u_{\Phi}n|,u_{\Phi}p \right)$',
                       fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                       \right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

if Fig1_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        data, label = bin3_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left(u_t \right)$', fontsize=20)
        ax1.set_title(r' File = %s' % HQ12, fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = bin3_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)

        data, label = bin1_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        data, label = bin3_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left(u_t \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = bin3_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left(\
                       |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

    if test2:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left(u_t \right)$', fontsize=20)
        ax1.set_title(r'File = %s' % test2_HQ0, fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left(u_t \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left(\
                       |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.set_yscale('log')

if Fig1_vt_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if B:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"leg = ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                                      fancybox=True, loc=0, handlelength=2.5)")
            exec(f"leg.get_frame().set_alpha(.5)")

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        popt, pcov = curve_fit(func_3, data[:, 0], data[:, 1])
        y_fit = func_3(data[:, 0], popt[0], popt[1])
        ax1.plot(data[:, 0], y_fit, 'c.-', lw=3,
                 label=r'$axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
                       % (popt[0], popt[1]))
        popt, pcov = curve_fit(func_4, data[:, 0], data[:, 1])
        y_fit = func_4(data[:, 0], popt[0], popt[1], popt[2])
        ax1.plot(data[:, 0], y_fit, 'g:', lw=3,
                 label=r'$ax(1- (1 - q)bx^2)^{(\frac{q}{1-q})}$,\
                       $ a,b,q = %.3f,%.3f,%.3f $'
                       % (popt[0], popt[1], popt[2]))

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=26)
        ax1.set_title(r'Fit to %s' % B_HQ0, fontsize=20)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        popt, pcov = curve_fit(func_3_log, data[:, 0], data[:, 1])
        y_fit = func_3_log(data[:, 0], popt[0], popt[1])
        ax2.plot(data[:, 0], y_fit, 'c.-', lw=3,
                 label=r'$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$,\
                       $ a,b = %.3f,%.3f $'
                       % (popt[0], popt[1]))
        popt, pcov = curve_fit(func_7_log, data[:, 0], data[:, 1])
        y_fit = func_7_log(data[:, 0], popt[0], popt[1], popt[2])
        ax2.plot(data[:, 0], y_fit, 'g:', lw=3,
                 label=r'$a\cdot \log(x)^2(1- (1 - q)b \cdot \log(x)^2)^{\
                       (\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
                       % (popt[0], popt[1], popt[2]))

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=26)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1],  'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=4, ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax3.set_xlabel(r'$ u_t $', fontsize=26)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=26)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b--',
                 label=r'$\gamma = -1.5 $', lw=2, ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b:',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b-.',
                 label=r'$\gamma = -2.5 $', lw=2, ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'b',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=26)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left(\
                       |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=26)
        ax4.set_yscale('log')

if Fig2_vr_vPhi_vTheta_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        data, label = bin2_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0],
                 data[:, 1]
                 / (478.006 * np.exp(-.456 * data[:, 0] ** 2)),
                 'g:', label=r'$r, a=478.006, b=0.456$', lw=4, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0],
                 data[:, 1]
                 / (482.605 * np.exp(-.473 * data[:, 0] ** 2)),
                 'r:', label=r'$\Theta, a=482.605, b=0.473$', lw=4, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0],
                 data[:, 1]
                 / (502.652 * np.exp(-.477 * data[:, 0] ** 2)),
                 'k:', label=r'$\Phi, a=502.652, b=0.477$', lw=2, ms=7)

        ax1.set_xlabel(r'$ u_r $, $ u_{\Theta} $ and $ u_{\Phi} $',
                       fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left(u \right)}{ae^{-bx^2}}$',
                       fontsize=20)
        ax1.set_title(r'File = %s, $\gamma = -2.0$' % HQ12,
                      fontsize=20)

        data, label = bin2_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (1433.228*10 ** data[:, 0]
                    * np.exp(-0.472*(10 ** data[:, 0]) ** 2)),
                 'g:', label=r'$a=1433.228, b=0.472$', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (1416.346*10 ** data[:, 0]
                    * np.exp(-0.473*(10 ** data[:, 0]) ** 2)),
                 'r:', label=r'$ a=1416.346, b=0.473 $', lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (1405.914*10 ** data[:, 0]
                    * np.exp(-.470*(10 ** data[:, 0])**2)),
                 'k:', label=r'$ a=1405.914, b=0.470$', lw=2, ms=7)

        ax2.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                       |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                       |u_{\Phi}n|,u_{\Phi}p \right)$',
                       fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,\
                       u_p \right)\right)}{axe^{-b\log (x)^2}}$', fontsize=20)
        # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}

    if test2:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:, 0],
                 data[:, 1]
                 / (478.006 * np.exp(-.456 * data[:, 0] ** 2)),
                 'g:', label=r'$r, a=478.006, b=0.456$', lw=4, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:, 0],
                 data[:, 1]
                 / (482.605 * np.exp(-.473 * data[:, 0] ** 2)),
                 'r:', label=r'$\Theta, a=482.605, b=0.473$', lw=4, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:, 0],
                 data[:, 1]
                 / (502.652 * np.exp(-.477 * data[:, 0] ** 2)),
                 'k:', label=r'$\Phi, a=502.652, b=0.477$', lw=2, ms=7)

        ax1.set_xlabel(r'$ u_r $, $ u_{\Theta} $ and $ u_{\Phi} $',
                       fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left(u \right)}{ae^{-bx^2}}$',
                       fontsize=20)
        ax1.set_title(r'File = %s, $\gamma = -2.0$' % test2_HQ0,
                      fontsize=20)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (1433.228 * 10 ** data[:, 0]
                 * np.exp(-.472 * (10 ** data[:, 0]) ** 2)),
                 'g:', label=r'$a=1433.228, b=0.472$', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (1416.346 * 10 ** data[:, 0]
                 * np.exp(-.473 * (10 ** data[:, 0]) ** 2)),
                 'r:', label=r'$a=1416.346, b=0.473$', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:, 0],
                 data[:, 1] / (1405.914 * 10 ** data[:, 0]
                 * np.exp(-.470 * (10 ** data[:, 0]) ** 2)),
                 'k:', label=r'$ a=1405.914, b=0.470$', lw=2, ms=7)

        ax2.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                       |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                       |u_{\Phi}n|,u_{\Phi}p \right)$',
                       fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {axe^{-b\log (x)^2}}$',
                       fontsize=20)

if Fig2a_vt_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        data, label = bin1_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0],
                 data[:, 1] / (918.083 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'b--', label=r'$ \gamma = -1.5 $', lw=3)
        data, label = bin2_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0],
                 data[:, 1]/(918.083*data[:, 0]*np.exp(-0.922*data[:, 0]**2)),
                 'b:', label=r'$ \gamma = -2.0 $', lw=4, ms=7)
        data, label = bin3_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0],
                 data[:, 1]/(918.083*data[:, 0]*np.exp(-0.922*data[:, 0]**2)),
                 'b-.', label=r'$ \gamma = -2.5 $', lw=4, ms=7)
        data, label = bin4_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:, 0],
                 data[:, 1]/(918.083*data[:, 0]*np.exp(-0.922*data[:, 0]**2)),
                 'b', label=r'$ \gamma = -3.0 $', lw=2, ms=7)

        ax1.set_ylim(0, 2)
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$',
                       fontsize=20)
        ax1.set_title(r'File = %s' % HQ12, fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b--', label=r'$ \gamma = -1.5 $',
                 lw=2, ms=7)
        data, label = bin2_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b:', label=r'$ \gamma = -2.0 $', lw=2,
                 ms=7)
        data, label = bin3_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b-.', label=r'$ \gamma = -2.5 $',
                 lw=2, ms=7)
        data, label = bin4_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b', label=r'$ \gamma = -3.0 $', lw=2, ms=7)

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                       \right)}{3400.442x^2e^{-0.930x^2}}$', fontsize=20)
        # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}

    if test2:

        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0],
                 data[:, 1] / (918.083 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'b--', label=r'$ \gamma = -1.5 $', lw=3)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0],
                 data[:, 1] / (918.083 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'b:', label=r'$ \gamma = -2.0 $', lw=4, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0],
                 data[:, 1] / (918.083 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'b-.', label=r'$ \gamma = -2.5 $', lw=4, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0],
                 data[:, 1] / (918.083 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'b', label=r'$ \gamma = -3.0 $', lw=2, ms=7)

        ax1.set_ylim(0, 2)
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$',
                       fontsize=20)
        ax1.set_title(r'File = %s' % test2_HQ0, fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b--', label=r'$ \gamma = -1.5 $',
                 lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b:', label=r'$ \gamma = -2.0 $',
                 lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b-.', label=r'$ \gamma = -2.5 $',
                 lw=2, ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0],
                 data[:, 1]
                 / (3400.442 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b', label=r'$ \gamma = -3.0 $', lw=2, ms=7)

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$',
                       fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {3400.442x^2e^{-0.930x^2}}$',
                       fontsize=20)

if Fig6_GPerts_same_gammas_as_IC_vr:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                            frameon=True, loc=0, handlelength=2.5)")

    data, label = bin1_HQ10000_G1_0_0_000[0]
    ax1.plot(data[:, 0], data[:, 1], 'b--',
             label=r'%s' % HQ0[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], 'Skyblue', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r--',
             label=r'%s' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Pink', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g--',
             label=r'%s' % HQ18[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k--',
             label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Brown', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', ls='--',
             label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'y--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:, 0], data[:, 1], 'm--',
             label=r'%s' % HQ70[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], 'Violet', ls='--', lw=2, ms=7)

    data, label = bin2_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -2.0$'
    ax1.plot(data[:, 0], data[:, 1], 'b:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], 'Skyblue', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Pink', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g:', lw=4, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Chartreuse', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'y:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:, 0], data[:, 1], 'm:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], 'Violet', ls=':', lw=4, ms=7)

    data, label = bin3_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -2.5$'
    ax1.plot(data[:, 0], data[:, 1], 'b-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], 'Skyblue', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Pink', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'y-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:, 0], data[:, 1], 'm-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], 'Violet', ls='-.', lw=4, ms=7)

    data, label = bin4_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -3.0$'
    ax1.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], 'Skyblue', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Pink', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Chartreuse', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:, 0], data[:, 1], 'y', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:, 0], data[:, 1], 'm', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:, 0], data[:, 1], 'Violet', lw=2, ms=7)

    ax1.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
    ax1.set_title(r' Time evolution of files = %s' % HQ0[:-9], fontsize=20)

    data, label = bin1_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -1.5$'
    ax2.plot(data[:, 0], data[:, 1], 'b--',
             label=r'%s' % HQ0[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], 'Skyblue', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r--',
             label=r'%s' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Pink', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g--',
             label=r'%s' % HQ18[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k--',
             label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', ls='--',
             label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'y--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[4]
    ax2.plot(data[:, 0], data[:, 1], 'm--',
             label=r'%s' % HQ70[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], 'Violet', ls='--', lw=2, ms=7)

    data, label = bin2_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -2.0$'
    ax2.plot(data[:, 0], data[:, 1], 'b:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], 'Skyblue', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Pink', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g:', lw=2, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Chartreuse', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'y:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[4]
    ax2.plot(data[:, 0], data[:, 1], 'm:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], 'Violet', ls=':', lw=2, ms=7)

    data, label = bin3_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -2.5$'
    ax2.plot(data[:, 0], data[:, 1], 'b-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], 'Skyblue', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Pink', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'y-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[4]
    ax2.plot(data[:, 0], data[:, 1], 'm-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], 'Violet', ls='-.', lw=2, ms=7)

    data, label = bin4_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -3.0$'
    ax2.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], 'Skyblue', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Pink', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Chartreuse', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:, 0], data[:, 1], 'y', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[4]
    ax2.plot(data[:, 0], data[:, 1], 'm', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:, 0], data[:, 1], 'Violet', lw=2, ms=7)

    ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|\
                   ,u_rp \right)$', fontsize=20)
    ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                   fontsize=20)

    data, label = bin1_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -1.5$'
    ax3.plot(data[:, 0], data[:, 1], 'b--',
             label=r'%s' % HQ0[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], 'Skyblue', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r--',
             label=r'%s' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Pink', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g--',
             label=r'%s' % HQ18[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k--',
             label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', ls='--',
             label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'y--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:, 0], data[:, 1], 'm--',
             label=r'%s' % HQ70[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], 'Violet', ls='--', lw=2, ms=7)

    data, label = bin2_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -2.0$'
    ax3.plot(data[:, 0], data[:, 1], 'b:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], 'Skyblue', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Pink', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g:', lw=4, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Chartreuse', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'y:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:, 0], data[:, 1], 'm:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], 'Violet', ls=':', lw=4, ms=7)

    data, label = bin3_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -2.5$'
    ax3.plot(data[:, 0], data[:, 1], 'b-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], 'Skyblue', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Pink', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'y-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:, 0], data[:, 1], 'm-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], 'Violet', ls='-.', lw=4, ms=7)

    data, label = bin4_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -3.0$'
    ax3.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], 'Skyblue', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Pink', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Chartreuse', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:, 0], data[:, 1], 'y', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:, 0], data[:, 1], 'm', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:, 0], data[:, 1], 'Violet', lw=2, ms=7)

    ax3.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
    ax3.set_yscale('log')

    data, label = bin1_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -1.5$'
    ax4.plot(data[:, 0], data[:, 1], 'b--', label=r'%s'
             % HQ0[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], 'Skyblue', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r--', label=r'%s'
             % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Pink', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g--', label=r'%s'
             % HQ18[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k--', label=r'%s'
             % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', ls='--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', ls='--', label=r'%s'
             % HQ60[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'y--', lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:, 0], data[:, 1], 'm--', label=r'%s'
             % HQ70[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], 'Violet', ls='--', lw=2, ms=7)

    data, label = bin2_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -2.0$'
    ax4.plot(data[:, 0], data[:, 1], 'b:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], 'Skyblue', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Pink', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g:', lw=2, ms=7)
    data, label = bin2_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Chartreuse', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'y:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:, 0], data[:, 1], 'm:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], 'Violet', ls=':', lw=2, ms=7)

    data, label = bin3_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -2.5$'
    ax4.plot(data[:, 0], data[:, 1], 'b-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], 'Skyblue', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Pink', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Chartreuse', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'y-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:, 0], data[:, 1], 'm-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], 'Violet', ls='-.', lw=2, ms=7)

    data, label = bin4_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -3.0$'
    ax4.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], 'Skyblue', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Pink', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Chartreuse', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:, 0], data[:, 1], 'y', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:, 0], data[:, 1], 'm', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:, 0], data[:, 1], 'Violet', lw=2, ms=7)

    ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left(\
                   |u_rn|,u_rp \right)$', fontsize=20)
    ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right)\
                   \right)$', fontsize=20)
    ax4.set_yscale('log')

if Fig6_GPerts_G1_2_same_gammas_as_IC_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
               frameon=True, loc=0, handlelength=2.5)")

    data, label = bin1_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'b--',
             label=r'%s' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r--',
             label=r'%s' % HQ24[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g--',
             label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k--',
             label=r'%s' % HQ48[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', ls='--',
             label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)

    data, label = bin2_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=4, ms=7)

    data, label = bin3_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=4, ms=7)

    data, label = bin4_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

    ax1.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
    ax1.set_title(r' Time evolution of files = %s' % HQ0[:-9], fontsize=20)

    data, label = bin1_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r--',
             label=r'%s' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_3_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g--',
             label=r'%s' % HQ24[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k--',
             label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', ls='--',
             label=r'%s' % HQ48[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', ls='--',
             label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)

    data, label = bin2_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_3_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=2, ms=7)

    data, label = bin3_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_3_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=2, ms=7)

    data, label = bin4_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_3_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

    ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left(\
                   |u_rn|,u_rp \right)$', fontsize=20)
    ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                   fontsize=20)

    data, label = bin1_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r--',
             label=r'%s' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g--',
             label=r'%s' % HQ24[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k--',
             label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', ls='--',
             label=r'%s' % HQ48[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', ls='--',
             label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)

    data, label = bin2_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k:', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=4, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=4, ms=7)

    data, label = bin3_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=4, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=4, ms=7)

    data, label = bin4_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

    ax3.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
    ax3.set_yscale('log')

    data, label = bin1_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r--',
             label=r'%s' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g--',
             label=r'%s' % HQ24[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k--',
             label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', ls='--',
             label=r'%s' % HQ48[len('HQ10000_G'):], lw=2, ms=7)
    data, label = bin1_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', ls='--',
             label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)

    data, label = bin2_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k:', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', ls=':', lw=2, ms=7)
    data, label = bin2_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', ls=':', lw=2, ms=7)

    data, label = bin3_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', ls='-.', lw=2, ms=7)
    data, label = bin3_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', ls='-.', lw=2, ms=7)

    data, label = bin4_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
    data, label = bin4_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

    ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|\
                   ,u_rp \right)$', fontsize=20)
    ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right)\
                   \right)$', fontsize=20)
    ax4.set_yscale('log')

if Fig10_GPerts_different_gammas_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        for i in range(1, 5):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'b--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'r--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'k--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=4,ms=7)

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=4,ms=7)

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins' %HQ0[:-9],
                      fontsize=20)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',ls = '--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r:',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g:',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k:',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=2,ms=7)

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=2,ms=7)

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        # ax2.set_xlim(-3, 0)
        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',ls = '--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=4,ms=7)

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=4,ms=7)

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',ls = '--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r:',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g:',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k:',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=2,ms=7)

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=2,ms=7)

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

    if test2:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'b--',
                 label=r'%s' %test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'r--',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'g--',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1], 'k--',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',ls = '--',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1], 'b--',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1], 'b:',lw=4,ms=7)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1], 'b-.',lw=4,ms=7)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins'
                      % test2_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'b--',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'r--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'g--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1], 'k--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',ls = '--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1], 'b--', lw=2,ms=7)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1], 'b:',lw=4,ms=7)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1], 'b-.',lw=4,ms=7)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'b--',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'r--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'g--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'k--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',ls = '--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b--', lw=2,ms=7)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b:',lw=4,ms=7)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b-.',lw=4,ms=7)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],  'b--',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],  'r--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],  'g--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],  'k--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],  'Orange',ls = '--', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],  'b--', lw=2,ms=7)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],  'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],  'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],  'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],  'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],  'Orange', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],  'b:',lw=4,ms=7)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],  'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],  'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],  'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],  'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],  'Orange', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],  'b-.',lw=4,ms=7)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

    if B:

        for i in range(1, 5):
            exec(f"ax{i}.grid()")

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r--',
                 label=r'%s' %B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g--',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k--',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], 'Brown',ls = '--',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',ls = '--',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=4,ms=7)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=4,ms=7)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins'
                      % B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',ls = '--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',ls = '--',lw=2,ms=7)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r:',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g:',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k:',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=2,ms=7)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=2,ms=7)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g--', lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k--', lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',ls = '--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',ls = '--',lw=2,ms=7)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r:',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g:',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k:',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=4,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=4,ms=7)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=4,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=4,ms=7)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',ls = '--',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',ls = '--',lw=2,ms=7)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r:',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g:',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k:',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', ls =  ':',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', ls =  ':',lw=2,ms=7)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', ls =  '-.',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', ls =  '-.',lw=2,ms=7)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

if Fig11_GPerts_gammas_1_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'b' ,lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'k' ,lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s, different r bins, $\gamma = -1.5$'
                      % HQ0[:-9],
                      fontsize=20)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
          fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                 'r', lw=2, ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                       fontsize=20)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Orange',lw=2,ms=7)

        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                       fontsize=20)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g' ,lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k' ,lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown' ,lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange' ,lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1], 'b' ,lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -1.5$'
                      % test2_HQ0[:-9],
                      fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'b',lw=2,ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                       fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b', lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (0.946 / (1 - .946))),
                 'g', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (0.946 / (1 - .946))),
                 'k', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (0.946 / (1 - .946))),
                 'Brown', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946)
                 * .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'Orange', lw=2, ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946)
                 * .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'b', lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'b',lw=2,ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown' ,lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1], 'Orange' ,lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1], 'b' ,lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -1.5$'
                      % A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %A_HQ36[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %A_HQ246[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %A_HQ298[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'b',lw=2,ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'b',lw=2,ms=7)

        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'b',lw=2,ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)

        data, label = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Orange',lw=2,ms=7)
        data, label = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'b',lw=2,ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)

    if B:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], 'Brown' ,lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], 'Orange' ,lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -1.5$'
                      % B_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
          fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Orange',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)

        data, label = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Orange',lw=2,ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
          fontsize=20)

if Fig12_GPerts_gammas_2_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin2__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'r', lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g', lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of files = %s, different r bins, $\gamma = -2.0$'
                      % HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                 'r', lw=2, ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                 'g', lw=2, ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                 'k', lw=2, ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                 'Brown', lw=2, ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                 'Orange', lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                       fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Orange',lw=2,ms=7)

        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

    if test2:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$'
                      % test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],
                 lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],  'g',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],  'k',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],  'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],  'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],  'b',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):], lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.set_yscale('log')

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'b',lw=2,ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'b',lw=2,ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Orange',lw=2,ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'b',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'r', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:,0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'g', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:,0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'k', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:,0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'Brown', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:,0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'Orange', lw=2, ms=7)
        data, label = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:,0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'b', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {Tsallis}$',
                       fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1], 'b', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of %s, different r bins, $\gamma = -2.0$'
                      % A_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' % A_HQ36[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' % A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' % A_HQ246[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' % A_HQ298[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' % A_HQ382[len('A_HQ10000_G'):], lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 /(887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'r', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 /(887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'g', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 /(887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'k', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 /(887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'Brown', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 /(887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'Orange', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0],
                 data[:, 1]
                 /(887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'b', lw=2, ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2}}$',
                       fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1]
                 / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'r', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1]
                 / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'g', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1]
                 / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'k', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1]
                 / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'Brown', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:, 0],
                 data[:, 1]
                 / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'Orange', lw=2, ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0],
                 data[:, 1]
                 / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b', lw=2, ms=7)

        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908
                  * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908
                  * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908
                  * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908
                  * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908
                  * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                  'Orange',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908
                  * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                  'b',lw=2,ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)

        data, label = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1]/(3391.113*10**data[:,0]*(1-(1-0.987)
                  *0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]/(3391.113*10**data[:,0]*(1-(1-0.987)
                  *0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]/(3391.113*10**data[:,0]*(1-(1-0.987)
                  *0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]/(3391.113*10**data[:,0]*(1-(1-0.987)
                  *0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:, 0],
                 data[:, 1]/(3391.113*10**data[:,0]*(1-(1-0.987)
                  *0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Orange',lw=2,ms=7)
        data, label = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0],
                 data[:, 1]/(3391.113*10**data[:,0]*(1-(1-0.987)
                  *0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'b',lw=2,ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {Tsallis}$',
                       fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], 'Brown' ,lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], 'Orange' ,lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.0$'
                      % B_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]
          *np.exp(-0.930*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]
          *np.exp(-0.930*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]
          *np.exp(-0.930*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]
          *np.exp(-0.930*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]
          *np.exp(-0.930*data[:,0]**2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2
          *np.exp(-0.936*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2
          *np.exp(-0.936*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2
          *np.exp(-0.936*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2
          *np.exp(-0.936*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2
          *np.exp(-0.936*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]
          *(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]
          *(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]
                  *(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'k',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]
                  *(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Brown',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]
                  *(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Orange',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]
                 * (1 - (1 - .987) * .929 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                  'r',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]
                 * (1 - (1 - .987) * .929 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                  'g',lw=2,ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]
                 * (1 - (1 - .987) * .929 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'k', lw=2, ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]
                 * (1 - (1 - .987) * .929 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'Brown', lw=2, ms=7)
        data, label = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]
                 * (1 - (1 - .987) * .929 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'Orange', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {Tsallis}$',
                       fontsize=20)

if Fig13_GPerts_gammas_2_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin3__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.5$'
                      % HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left(|u_n|, u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
                       u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (np.log10(data[:, 0])
                 * np.exp(-.5 * data[:, 0] ** 2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Orange',lw=2,ms=7)

        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'b',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of files = %s , different r bins, $\gamma = -2.5$'
                      % test2_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
                       u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 'b', lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2}}$',
                       fontsize=20)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993
                 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'r', lw=2, ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993
                 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993
                 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993
                 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993
                 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993
                 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'b',lw=2,ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                       \right)}{3424.993 \cdot x^2 \cdot e^{-0.930\
                       \cdot x^2 }}$',
                       fontsize=20)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 *data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (.946 / (1 - .946))),
                 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 *data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (.946 / (1 - .946))),
                 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 *data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (.946 / (1 - .946))),
                 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 *data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (.946 / (1 - .946))),
                 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 *data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (.946 / (1 - .946))),
                 'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 *data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (.946 / (1 - .946))),
                 'b',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0], data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10
                 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0], data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10
                 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0], data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10
                 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:, 0], data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10
                 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:, 0], data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10
                 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                  'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:, 0], data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10
                 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                  'b',lw=2,ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp\
                       \right)\right)}{Tsallis}$',
                       fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown' ,lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1], 'Orange' ,lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1], 'b' ,lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.5$'
                      % A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s' % A_HQ0[len('A_HQ10000_G'):], lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'g',
                 label=r'%s' % A_HQ36[len('A_HQ10000_G'):], lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'k',
                 label=r'%s' % A_HQ66[len('A_HQ10000_G'):], lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'Brown',
                 label=r'%s' % A_HQ246[len('A_HQ10000_G'):], lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:, 0], data[:, 1], 'Orange',
                 label=r'%s' %A_HQ298[len('A_HQ10000_G'):], lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:, 0], data[:, 1], 'b',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):], lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:, 0], data[:, 1], 'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], 'b',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:, 0], data[:, 1], 'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], 'b',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
                       u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:, 0], data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:, 0], data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                  'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                  'b',lw=2,ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                       fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993 * (10 ** data[:, 0])
                 ** 2 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993 * (10 ** data[:, 0])
                 ** 2 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993 * (10 ** data[:, 0])
                 ** 2 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993 * (10 ** data[:, 0])
                 ** 2 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993 * (10 ** data[:, 0])
                 ** 2 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                  'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0], data[:, 1] / (3424.993 * (10 ** data[:, 0])
                 ** 2 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b', lw=2, ms=7)

        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\
                       \right)}{3424.993 \cdot x^2 \cdot e^{-0.930\
                       \cdot x^2 }}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 * data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (0.946 / (1 - .946))),
                 'r', lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 * data[:, 0]
                 * (1-(1 -0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 * data[:, 0]
                 * (1-(1 -0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 * data[:, 0]
                 * (1-(1 -0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 * data[:, 0]
                 * (1-(1 -0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Orange',lw=2,ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:, 1] / (864.543 * data[:, 0]
                 * (1-(1 -0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'b',lw=2,ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis}$',
                       fontsize=20)

        data, label = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'r', lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'g', lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'k', lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'Brown', lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'Orange', lw=2, ms=7)
        data, label = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'b', lw=2, ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,\
                       u_tp \right)\right)}{Tsallis}$',
                       fontsize=20)

    if B:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'Brown',lw=2, ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of %s, different r bins, $\gamma = -2.5$'
                      % B_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,\
                       u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,\
                       u_p \right)\right)}{3452.955 \cdot x^2\
                       \cdot e^{-0.936 \cdot x^2 }}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Orange',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'g',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'k',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Orange',lw=2,ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                       fontsize=20)

if Fig14_GPerts_gammas_3_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin4__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -3.0$'
                      % HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],
                 'r', lw=2, ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],
                 'g', lw=2, ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],
                 'k', lw=2, ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],
                 'Brown', lw=2, ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],
                 'Orange', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Orange',lw=2,ms=7)

        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

    if test2:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -3.0 $'
                      % test2_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left(|u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange', lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'b',lw=2,ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                       fontsize=20)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'b',lw=2,ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'b',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'b',lw=2,ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                       fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1], 'Brown' ,lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1], 'Orange' ,lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1], 'b' ,lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -3.0$'
                      % A_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %A_HQ36[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %A_HQ246[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %A_HQ298[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:,0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0],
                 data[:, 1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'b',lw=2,ms=7)

        ax5.set_ylim(.5, 1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'b',lw=2,ms=7)

        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'b',lw=2,ms=7)

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. -.987))),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. -.987))),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. -.987))),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. -.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. -.987))),
                  'Orange',lw=2,ms=7)
        data, label = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. -.987))),
                  'b',lw=2,ms=7)

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$',
                       fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                       fontsize=20)

    if B:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r' ,lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], 'Brown' ,lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], 'Orange', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of %s, different r bins, $\gamma=-3.0$'
                      % B_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0],
                 data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                       fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                  'Orange',lw=2,ms=7)

        ax6.set_ylim(0, 3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:, 0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:, 0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:, 0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                  'Orange',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis}$',
                       fontsize=20)

        data, label = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'g',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'k',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Brown',lw=2,ms=7)
        data, label = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'Orange',lw=2,ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                       fontsize=20)

# datalist_bin5different_gammas_test2_HQ10000_G1_0_25_005

if Fig15_GPerts_R_middle_19_95_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -1.5$'
          % HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1], 'g',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1], 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1], 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1], 'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1], 'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1], 'Orange',lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                  'Orange',lw=2,ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                       fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'r',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'g',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'k',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Brown',lw=2,ms=7)
        data, label = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                  'Orange',lw=2,ms=7)

        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

    if test2:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")
        
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s ,  $ R_{middle} = 19.95$'
                      % test2_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %test2_HQ166[len('test2_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1], 'r', lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax3.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax4.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)


        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                  'b',lw=2,ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2}}$',
                                fontsize=20)

        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'b',lw=2,ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                       \right)}{3424.993 \cdot x^2 \cdot\
                       e^{-0.930 \cdot x^2 }}$', fontsize=20)

        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0]
                 * (1 - (1 - .946) * .908 * data[:, 0] ** 2)
                 ** (.946 / (1 - .946))),
                 'b',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $',
                       fontsize=20)

        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                  'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                  'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0]
                 * (1 - (1 - .987) * .924 * 10 ** (data[:, 0] ** 2))
                 ** (.987 / (1. - .987))),
                 'b', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)

    if A:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")
        
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1], 'b',lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of files = %s, $R_{middle} = 19.95$'
                      % A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],
                  'r', lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],
                  'k', lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],
                  'b', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1], 'k', lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1], 'b', lw=2,ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 'r', lw=2, ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 'k', lw=2, ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 'b', lw=2, ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                  'b',lw=2,ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946) * .908*data[:,0]**2)**(0.946/(1-0.946))),
                  'r',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                  'k',lw=2,ms=7)
        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 'b',lw=2,ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $',
                       fontsize=20)

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                  'r',lw=2,ms=7)

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 'k', lw=2, ms=7)

        data, label = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 'b', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                       fontsize=20)

    if B:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")
        
        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of files = %s, $R_{middle} = 19.95$'
                      % B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):], lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:, 1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 'r', lw=2, ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                       fontsize=20)

        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1]
                 / (3424.993*(10**data[:,0])**2
                    * np.exp(-0.930*(10**data[:,0])**2)),
                 'r', lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)

        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 'r', lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)

        data, label = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 'r', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                       fontsize=20)

if Fig16_GPerts_R_middle_31_62_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:

        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        ax1.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$'
                      % HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s ' % HQ12[len('HQ10000_G'):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], 'g',
                 label=r'%s' % HQ24[len('HQ10000_G'):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], 'k',
                 label=r'%s' % HQ36[len('HQ10000_G'):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], 'Brown',
                 label=r'%s' % HQ48[len('HQ10000_G'):], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], 'Orange',
                 label=r'%s' % HQ60[len('HQ10000_G'):], lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        ax3.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax3.set_yscale('log')

        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], 'g', lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], 'Brown', lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], 'Orange', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax4.set_yscale('log')

        ax5.plot(data[:, 0],
                 data[:, 1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 'r', lw=2, ms=7)
        ax5.plot(data[:, 0],
                 data[:, 1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 'g', lw=2, ms=7)
        ax5.plot(data[:, 0],
                 data[:, 1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 'k', lw=2, ms=7)
        ax5.plot(data[:, 0],
                 data[:, 1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 'Brown', lw=2, ms=7)
        ax5.plot(data[:, 0],
                 data[:, 1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 'Orange', lw=2, ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
          fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        ax6.plot(data[:, 0], data[:, 1] / np.exp(-.5 * data[:, 0] ** 2),
                 'r', lw=2, ms=7)
        ax6.plot(data[:, 0], data[:, 1] / np.exp(-.5 * data[:, 0] ** 2),
                 'g',lw=2,ms=7)
        ax6.plot(data[:, 0], data[:, 1] / np.exp(-.5 * data[:, 0] ** 2),
                 'k',lw=2,ms=7)
        ax6.plot(data[:, 0], data[:, 1] / np.exp(-.5 * data[:, 0] ** 2),
                 'Brown',lw=2,ms=7)
        ax6.plot(data[:, 0], data[:, 1] / np.exp(-.5 * data[:, 0] ** 2),
                 'Orange',lw=2,ms=7)

        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

    if test2:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")
        
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], 'r',lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], 'k' ,lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:,0], data[:,1], 'b' ,lw=2,ms=7)

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , $ R_{middle} = 31.62$'
                      % test2_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1], 'r',
                 label=r'%s ' % test2_HQ0[len('HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1], 'k',
                 label=r'%s' % test2_HQ66[len('HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' % test2_HQ166[len('HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'r', lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'k', lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax3.plot(data[:, 0], data[:, 1], 'b', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax4.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|, u_tp\
                       \right)\right) \right)$', fontsize=20)
        ax4.set_yscale('log')

        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0]
                 * np.exp(-.922 * data[:, 0] ** 2)),
                 'b', lw=2, ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x\
                       \cdot e^{-0.922 \cdot x^2} }$',
                       fontsize=20)

        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2
                 * np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1]/(3424.993*(10**data[:, 0])**2
                 * np.exp(-0.930*(10**data[:, 0])**2)),
                 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(data[:, 0],
                 data[:, 1]/(3424.993*(10**data[:, 0])**2
                 * np.exp(-0.930*(10**data[:, 0])**2)),
                 'b', lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930\
                       \cdot x^2 }}$',
                       fontsize=20)

        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946)
                 * .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'r',lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946)
                 * .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'k',lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946)
                 * .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'b', lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis}$',
                       fontsize=20)

        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113*10**data[:, 0]*(1-(1-0.987)
                    * .924*10**(data[:, 0]**2))**(0.987/(1.-0.987))),
                 'r',lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987)
                    * .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 'k',lw=2,ms=7)
        data, label = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(data[:, 0],
                 data[:, 1]
                 / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987)
                    * .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 'b', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                       \right)}{Tsallis}$', fontsize=20)

    if A:

        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:, 0], data[:, 1], 'k' , lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:, 0], data[:, 1], 'b' , lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s, $ R_{middle} = 31.62 $'\
                      % A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:, 0], data[:, 1], 'k',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1], 'b',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7)

        ax2.set_ylabel(r'$f\left(\log \left(|u_tn|, u_tp \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)

        ax3.set_ylabel(r'$\log \left(f\left(u_t \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:, 0], data[:, 1], 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:, 0], data[:, 1], 'b', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|, u_tp \right)\
                       \right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                     np.exp(-.922 * data[:, 0] ** 2)),
                 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                     np.exp(-.922 * data[:, 0] ** 2)),
                 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                     np.exp(-.922 * data[:, 0] ** 2)),
                 'b', lw=2, ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2} }$',
                       fontsize=20)

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                 np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                 np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                 np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'b', lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left(|u_tn|, u_tp\
                       \right)\right)}\{3424.993 \cdot x^2 \cdot e^{-0.930\
                       \cdot x^2 }}$',
                       fontsize=20)

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946) * .908 *
                 data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946) * .908 *
                 data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946) * .908 *
                 data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'b', lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)

        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                 .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 'r', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                 .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. -.987))),
                 'k', lw=2, ms=7)
        data, label = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                 .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 'b', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|, u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                       \right)}{Tsallis}$',
                       fontsize=20)

    if B:
        
        for i in range(1, 9):
            exec(f"ax{i}.grid()")
        
        data, label = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r'Time evolution of files = %s, $R_{middle} = 31.62$'
                      % B_HQ0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:, 0], data[:, 1], 'r',
                 label=r'%s' % B_HQ0[len('B_HQ10000_G'):], lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)

        data, label = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=20)
        ax3.set_yscale('log')

        data, label = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:, 0], data[:, 1], 'r', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|, u_tp \right)\
                       \right) \right)$',
                       fontsize=20)
        ax4.set_yscale('log')

        data, label = datalist_largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                 np.exp(-.922 * data[:, 0] ** 2)),
                 'r', lw=2, ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x\
                       \cdot e^{-0.922 \cdot x^2} }$',
                       fontsize=20)

        data, label = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                 np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 'r', lw=2, ms=7)
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp \right)\right)}\
                       {3424.993 \cdot x^2\
                       \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)

        data, label = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946)
                 * .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 'r', lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)

        data, label = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987)
                 * .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 'r', lw=2, ms=7)
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp\
                       \right)\right)}{Tsallis}$',
                       fontsize=20)

plt.show()
