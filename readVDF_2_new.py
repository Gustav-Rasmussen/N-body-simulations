# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pylab


def func_1(x, a, b):  # Gaussian fits
    return a * x*np.exp(-b * x**2.)


def func_2(x, a, b):
    return a * np.exp(-b * x**2.)


def func_3(x, a, b):
    return a * x**2*np.exp(-b * x**2.)


def func_1_log(log10x, a, b):
    x = 10.0 ** log10x
    return a * x * np.exp(-b * x**2.)


def func_2_log(log10x, a, b):
    x = 10.0 ** log10x
    return a * np.exp(-b * x ** 2.)


def func_3_log(log10x, a, b):
    x = 10.0 ** log10x
    return a * x ** 2 * np.exp(-b * x ** 2.)


def func_4(x, a, b, q):  # q-fits
    return a * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func_5(x, b, q):
    return (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func_6(x, a, b, q):
    return a * x * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func_7_log(log10x, a, b, q):
    x = 10.0 ** log10x
    return a * x ** 2 * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


# Filename = 'HQ1000000_150311_000.hdf5'
# Filename = 'OM_150310_000.hdf5'
# Filename = 'RunGadget/G_HQ_1000000_test/output/HQ10000_G0.8_2_000.hdf5'

# Switches ---------------------------------------------------------
Gamma_on = 1
Beta_on = 0

test = 0
test2 = 0
A = 0
B = 0
C = 0
D = 0

# Figures ---------------------------------------------------------
Fig1_vr_vphi_vtheta = 0  # Works for test and test2
Fig1_vr_vphi_vtheta_with_fit = 0  # Works for test and test2
Fig1_vt = 0  # Works for test and test2
Fig1_vt_with_fit = 0  # Works for test, test2 and B

Fig2_vr_vphi_vtheta_divided_by_gauss = 0  # Works for test and test2
Fig2a_vt_divided_by_gauss = 0  # Works for test and test2

Fig6_Gperturbations_same_gammas_as_IC_vr = 0  # Works for test. test2?
Fig6_Gperturbations_G1_2_same_gammas_as_IC_vt = 0  # Not yet created

Fig7_Gperturbations_different_gammas_vr_vphi_vtheta = 0  # Not yet created

Fig8_Gperturbations_different_gammas_vr_vphi_vtheta_divided_by_gauss = 0  # Not yet created

Fig9_Gperturbations_different_gammas_vr = 0  # Not yet created
 
Fig10_Gperturbations_different_gammas_vt = 0  # Works for test, test2 and B

Fig11_Gperturbations_gammas_1_5_vt_divided_by_gauss_and_Tsallis = 0  # Works for test, test2, B

Fig12_Gperturbations_gammas_2_0_vt_divided_by_gauss_and_Tsallis = 0  # Works for test, test2, B

Fig13_Gperturbations_gammas_2_5_vt_divided_by_gauss_and_Tsallis = 0  # Works for test, test2, B

Fig14_Gperturbations_gammas_3_0_vt_divided_by_gauss_and_Tsallis = 0  # Works for test, test2, B

Fig15_Gperturbations_R_middle_19_95_vt_divided_by_gauss_and_Tsallis = 0  # Works for A, B

Fig16_Gperturbations_R_middle_31_62_vt_divided_by_gauss_and_Tsallis = 0  # Works for A, B

# Files ---------------------------------------------------------
G_perturbation_HQ10000_G1_0_0_000 = 1
G_perturbation_HQ10000_G1_2_1_005 = 1
G_perturbation_HQ10000_G0_8_2_005 = 1
G_perturbation_HQ10000_G1_2_3_005 = 1
G_perturbation_HQ10000_G1_2_5_005 = 1
G_perturbation_HQ10000_G1_2_7_005 = 1
G_perturbation_HQ10000_G1_2_9_005 = 1
G_perturbation_HQ10000_G1_0_10_009 = 1

G_perturbation_different_gammas_HQ10000_G1_2_1_005 = 1
G_perturbation_different_gammas_HQ10000_G1_2_3_005 = 1
G_perturbation_different_gammas_HQ10000_G1_2_5_005 = 1
G_perturbation_different_gammas_HQ10000_G1_2_7_005 = 1
G_perturbation_different_gammas_HQ10000_G1_2_9_005 = 1

# Create new files (for Eddington test 2, HQ, N = 10^6)
test2_G_perturbation_HQ10000_G1_0_0_000 = 1
test2_G_perturbation_HQ10000_G1_0_5_005 = 1
test2_G_perturbation_HQ10000_G0_0_10_005 = 1
test2_G_perturbation_HQ10000_G1_0_15_005 = 1
test2_G_perturbation_HQ10000_G1_0_25_005 = 1

test2_G_perturbation_different_gammas_HQ10000_G1_0_0_000 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_5_005 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_10_005 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_15_005 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_005 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_010 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_015 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_020 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_025 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_030 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_035 = 1
test2_G_perturbation_different_gammas_HQ0000_G1_0_18_040 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_18_053 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_20_005 = 1
test2_G_perturbation_different_gammas_HQ10000_G1_0_25_005 = 1

# Create new files (for Eddington A, HQ, N = 10^6)
A_G_perturbation_different_gammas_HQ10000_G1_0_0_000 = 1  # already exist (test2 files)
A_G_perturbation_different_gammas_HQ10000_G1_0_5_005 = 1  # already exist (test2 files)
A_G_perturbation_different_gammas_HQ10000_G1_0_10_005 = 1  # already exist (test2 files)
A_G_perturbation_different_gammas_HQ10000_G1_0_40_005 = 1
A_G_perturbation_different_gammas_HQ10000_G1_2_46_005 = 1
A_G_perturbation_different_gammas_HQ10000_G0_8_47_005 = 1
A_G_perturbation_different_gammas_HQ10000_G1_0_48_009 = 1  # Not yet listed in readVDF_2.py
A_G_perturbation_different_gammas_HQ10000_G1_0_48_093 = 1

# Create new files (for Eddington B, HQ, N = 10^6)
B_G_perturbation_different_gammas_HQ10000_G1_0_0_000 = 1  # already exist (test2 files)
B_G_perturbation_different_gammas_HQ10000_G1_0_5_005 = 1 
B_G_perturbation_different_gammas_HQ10000_G1_0_10_005 = 1
B_G_perturbation_different_gammas_HQ10000_G1_0_198_000 = 1
B_G_perturbation_different_gammas_HQ10000_G1_0_198_093 = 1
B_G_perturbation_different_gammas_HQ10000_G1_0_199_093 = 1

# Create new files (for OM C, HQ, N = 10^6)
C_G_perturbation_different_gammas_HQ10000_G1_0_0_000 = 1
C_G_perturbation_different_gammas_HQ10000_G1_0_5_005 = 1
C_G_perturbation_different_gammas_HQ10000_G1_0_10_005 = 1
C_G_perturbation_different_gammas_HQ10000_G1_0_40_005 = 1
C_G_perturbation_different_gammas_HQ10000_G1_2_46_005 = 1
C_G_perturbation_different_gammas_HQ10000_G0_8_47_005 = 1
C_G_perturbation_different_gammas_HQ10000_G1_0_48_009 = 0  # Not yet listed in readVDF_2.py
C_G_perturbation_different_gammas_HQ10000_G1_0_48_093 = 1

# Create new files (for OM D, HQ, N = 10^6)
D_G_perturbation_different_gammas_HQ10000_G1_0_0_000 = 1
D_G_perturbation_different_gammas_HQ10000_G1_0_5_005 = 1
D_G_perturbation_different_gammas_HQ10000_G1_0_10_005 = 1
D_G_perturbation_different_gammas_HQ10000_G1_0_160_005 = 1
D_G_perturbation_different_gammas_HQ10000_G1_05_196_005 = 1
D_G_perturbation_different_gammas_HQ10000_G0_95_197_005 = 1
D_G_perturbation_different_gammas_HQ10000_G1_0_198_009 = 0  # Not yet listed in readVDF_2.py
D_G_perturbation_different_gammas_HQ10000_G1_0_198_093 = 1

# [5],[6],[7] : log9, log7, log8 : r, theta, phi

if B_G_perturbation_different_gammas_HQ10000_G1_0_0_000:
    B_HQ0 = 'B_HQ10000_G1.0_0_000'  
# _new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_
# _large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle
# _new_R_middle_logx10_gamma_-1.50.txt' 10 9 7 8
# _average_logx10_gamma_%.2f.txt'
    
    list_of_files_innerbin_HQ10000_G1_0_0_000 = [(B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50'),
                                                 (B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50'),
                                                 (B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50'),
                                                 (B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50'),
                                                 (B_HQ0 + '_new_R_middle_average_logx10_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx10_gamma_-1.50'),
                                                 (B_HQ0 + '_new_R_middle_average_logx9_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx9_gamma_-1.50'),
                                                 (B_HQ0 + '_new_R_middle_average_logx7_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx7_gamma_-1.50'),
                                                 (B_HQ0 + '_new_R_middle_average_logx8_gamma_-1.50.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx8_gamma_-1.50')]

    list_of_files_first_middlebin_HQ10000_G1_0_0_000 = [(B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00'),
                                                        (B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00'),
                                                        (B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00'),
                                                        (B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00'),
                                                        (B_HQ0 + '_new_R_middle_average_logx10_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_average_logx10_gamma_-2.00'),
                                                        (B_HQ0 + '_new_R_middle_average_logx9_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_average_logx9_gamma_-2.00'),
                                                        (B_HQ0 + '_new_R_middle_average_logx7_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_average_logx7_gamma_-2.00'),
                                                        (B_HQ0 + '_new_R_middle_average_logx8_gamma_-2.00.txt',
                                                         B_HQ0 + '_new_R_middle_average_logx8_gamma_-2.00')]

    list_of_files_second_middlebin_HQ10000_G1_0_0_000 = [(B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50'),
                                                         (B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50'),
                                                         (B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50'),
                                                         (B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50'),
                                                         (B_HQ0 + '_new_R_middle_average_logx10_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_average_logx10_gamma_-2.50'),
                                                         (B_HQ0 + '_new_R_middle_average_logx9_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_average_logx9_gamma_-2.50'),
                                                         (B_HQ0 + '_new_R_middle_average_logx7_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_average_logx7_gamma_-2.50'),
                                                         (B_HQ0 + '_new_R_middle_average_logx8_gamma_-2.50.txt',
                                                          B_HQ0 + '_new_R_middle_average_logx8_gamma_-2.50')]

    list_of_files_outerbin_HQ10000_G1_0_0_000 = [(B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00'),
                                                 (B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00'),
                                                 (B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00'),
                                                 (B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00'),
                                                 (B_HQ0 + '_new_R_middle_average_logx10_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx10_gamma_-3.00'),
                                                 (B_HQ0 + '_new_R_middle_average_logx9_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx9_gamma_-3.00'),
                                                 (B_HQ0 + '_new_R_middle_average_logx7_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx7_gamma_-3.00'),
                                                 (B_HQ0 + '_new_R_middle_average_logx8_gamma_-3.00.txt',
                                                  B_HQ0 + '_new_R_middle_average_logx8_gamma_-3.00')]

    list_of_files_large_R_middle_19_95_HQ10000_G1_0_0_000 = [(B_HQ0 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_19.95'),
                                                             (B_HQ0 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_19.95'),
                                                             (B_HQ0 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_19.95'),
                                                             (B_HQ0 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_19.95'),
                                                             (B_HQ0 + '_large_R_middle_average_logx10_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx10_R_middle_19.95'),
                                                             (B_HQ0 + '_large_R_middle_average_logx9_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx9_R_middle_19.95'),
                                                             (B_HQ0 + '_large_R_middle_average_logx7_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx7_R_middle_19.95'),
                                                             (B_HQ0 + '_large_R_middle_average_logx8_R_middle_19.95.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx8_R_middle_19.95')]

    list_of_files_large_R_middle_31_62_HQ10000_G1_0_0_000 = [(B_HQ0 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_31.62'),
                                                             (B_HQ0 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_31.62'),
                                                             (B_HQ0 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_31.62'),
                                                             (B_HQ0 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_31.62'),
                                                             (B_HQ0 + '_large_R_middle_average_logx10_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx10_R_middle_31.62'),
                                                             (B_HQ0 + '_large_R_middle_average_logx9_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx9_R_middle_31.62'),
                                                             (B_HQ0 + '_large_R_middle_average_logx7_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx7_R_middle_31.62'),
                                                             (B_HQ0 + '_large_R_middle_average_logx8_R_middle_31.62.txt',
                                                              B_HQ0 + '_large_R_middle_average_logx8_R_middle_31.62')]

    bin1_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_innerbin_HQ10000_G1_0_0_000]
    bin2_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_first_middlebin_HQ10000_G1_0_0_000]
    bin3_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_second_middlebin_HQ10000_G1_0_0_000]
    bin4_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_outerbin_HQ10000_G1_0_0_000]
    datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_large_R_middle_19_95_HQ10000_G1_0_0_000]
    datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_large_R_middle_31_62_HQ10000_G1_0_0_000]

if B_G_perturbation_different_gammas_HQ10000_G1_0_5_005:
    B_HQ36 = 'B_HQ10000_G1.0_5_005'

    list_of_files_innerbin_HQ10000_G1_0_5_005 = [(B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50'),
                                                 (B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50'),
                                                 (B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50'),
                                                 (B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50'),
                                                 (B_HQ36 + '_new_R_middle_average_logx10_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_average_logx10_gamma_-1.50'),
                                                 (B_HQ36 + '_new_R_middle_average_logx9_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_average_logx9_gamma_-1.50'),
                                                 (B_HQ36 + '_new_R_middle_average_logx7_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_average_logx7_gamma_-1.50'),
                                                 (B_HQ36 + '_new_R_middle_average_logx8_gamma_-1.50.txt',
                                                  B_HQ36 + '_new_R_middle_average_logx8_gamma_-1.50')]

    list_of_files_first_middlebin_HQ10000_G1_0_5_005 = [(B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00'),
                                                        (B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00'),
                                                        (B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00'),
                                                        (B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00'),
                                                        (B_HQ36 + '_new_R_middle_average_logx10_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_average_logx10_gamma_-2.00'),
                                                        (B_HQ36 + '_new_R_middle_average_logx9_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_average_logx9_gamma_-2.00'),
                                                        (B_HQ36 + '_new_R_middle_average_logx7_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_average_logx7_gamma_-2.00'),
                                                        (B_HQ36 + '_new_R_middle_average_logx8_gamma_-2.00.txt',
                                                         B_HQ36 + '_new_R_middle_average_logx8_gamma_-2.00')]

    list_of_files_second_middlebin_HQ10000_G1_0_5_005 = [(B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50'),
                                                                          (B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50'),
                                                                          (B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50'),
                                                                          (B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx10_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx10_gamma_-2.50'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx9_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx9_gamma_-2.50'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx7_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx7_gamma_-2.50'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx8_gamma_-2.50.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx8_gamma_-2.50')]

    list_of_files_outerbin_HQ10000_G1_0_5_005 = [(B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00'),
                                                                          (B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00'),
                                                                          (B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00'),
                                                                          (B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx10_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx10_gamma_-3.00'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx9_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx9_gamma_-3.00'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx7_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx7_gamma_-3.00'),
                                                                          (B_HQ36 + '_new_R_middle_average_logx8_gamma_-3.00.txt',
                                                                           B_HQ36 + '_new_R_middle_average_logx8_gamma_-3.00')]

    list_of_files_large_R_middle_19_95_HQ10000_G1_0_5_005 = [(B_HQ36 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_19.95'),
                                                                                 (B_HQ36 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_19.95'),
                                                                                 (B_HQ36 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_19.95'),
                                                                                 (B_HQ36 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_19.95'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx10_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx10_R_middle_19.95'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx9_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx9_R_middle_19.95'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx7_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx7_R_middle_19.95'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx8_R_middle_19.95.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx8_R_middle_19.95')]

    list_of_files_large_R_middle_31_62_HQ10000_G1_0_5_005 = [(B_HQ36 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_VT_i_average_inside_bin_sigmatan_R_middle_31.62'),
                                                                                 (B_HQ36 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_VR_i_average_inside_bin_sigmarad_R_middle_31.62'),
                                                                                 (B_HQ36 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_VTheta_i_average_inside_bin_sigmatheta_R_middle_31.62'),
                                                                                 (B_HQ36 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_VPhi_i_average_inside_bin_sigmaphi_R_middle_31.62'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx10_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx10_R_middle_31.62'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx9_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx9_R_middle_31.62'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx7_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx7_R_middle_31.62'),
                                                                                 (B_HQ36 + '_large_R_middle_average_logx8_R_middle_31.62.txt',
                                                                                  B_HQ36 + '_large_R_middle_average_logx8_R_middle_31.62')]

    # This works.
    # list_of_files_innerbin_HQ10000_G1_0_5_005 = [tuple(map(lambda i: str.replace(i, '_new_R_middle_VT_sigmatan_gamma_','_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_'), tup)) for tup in list_of_files_innerbin_HQ10000_G1_0_5_005]
    # print('list_of_files_innerbin_HQ10000_G1_0_5_005', list_of_files_innerbin_HQ10000_G1_0_5_005)

    datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_innerbin_HQ10000_G1_0_5_005]
    datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_first_middlebin_HQ10000_G1_0_5_005]
    datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_second_middlebin_HQ10000_G1_0_5_005]
    datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_outerbin_HQ10000_G1_0_5_005]
    datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_large_R_middle_19_95_HQ10000_G1_0_5_005]
    datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_5_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_large_R_middle_31_62_HQ10000_G1_0_5_005]

if B_G_perturbation_different_gammas_HQ10000_G1_0_10_005:
    B_HQ66 = 'B_HQ10000_G1.0_10_005'

    list_of_files_innerbin_HQ10000_G1_0_10_005 = [(B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50'),
                                                                          (B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50'),
                                                                          (B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50'),
                                                                          (B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx10_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx10_gamma_-1.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx9_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx9_gamma_-1.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx7_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx7_gamma_-1.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx8_gamma_-1.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx8_gamma_-1.50')]

    list_of_files_first_middlebin_HQ10000_G1_0_10_005 = [(B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00'),
                                                                          (B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00'),
                                                                          (B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00'),
                                                                          (B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx10_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx10_gamma_-2.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx9_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx9_gamma_-2.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx7_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx7_gamma_-2.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx8_gamma_-2.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx8_gamma_-2.00')]

    list_of_files_second_middlebin_HQ10000_G1_0_10_005 = [(B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50'),
                                                                          (B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50'),
                                                                          (B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50'),
                                                                          (B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx10_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx10_gamma_-2.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx9_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx9_gamma_-2.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx7_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx7_gamma_-2.50'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx8_gamma_-2.50.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx8_gamma_-2.50')]

    list_of_files_outerbin_HQ10000_G1_0_10_005 = [(B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00'),
                                                                          (B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00'),
                                                                          (B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00'),
                                                                          (B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx10_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx10_gamma_-3.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx9_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx9_gamma_-3.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx7_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx7_gamma_-3.00'),
                                                                          (B_HQ66 + '_new_R_middle_average_logx8_gamma_-3.00.txt',
                                                                           B_HQ66 + '_new_R_middle_average_logx8_gamma_-3.00')]

    datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_innerbin_HQ10000_G1_0_10_005 ]
    datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_first_middlebin_HQ10000_G1_0_10_005 ]
    datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_second_middlebin_HQ10000_G1_0_10_005 ]
    datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in list_of_files_outerbin_HQ10000_G1_0_10_005 ]

if B_G_perturbation_different_gammas_HQ10000_G1_0_198_000:
    B_HQ294 = 'B_HQ10000_G1.0_198_000'

    list_of_files_innerbin_HQ10000_G1_0_198_000 = [(B_HQ294 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50.txt', B_HQ294+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50'),
                                                                          (B_HQ294 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50.txt', B_HQ294+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50'),
                                                                          (B_HQ294 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50.txt', B_HQ294+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50'),
                                                                          (B_HQ294 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50.txt', B_HQ294+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx10_gamma_-1.50.txt',B_HQ294+'_new_R_middle_average_logx10_gamma_-1.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx9_gamma_-1.50.txt',B_HQ294+'_new_R_middle_average_logx9_gamma_-1.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx7_gamma_-1.50.txt',B_HQ294+'_new_R_middle_average_logx7_gamma_-1.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx8_gamma_-1.50.txt',B_HQ294+'_new_R_middle_average_logx8_gamma_-1.50')]

    list_of_files_first_middlebin_HQ10000_G1_0_198_000 = [(B_HQ294 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00.txt', B_HQ294+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00'),
                                                                          (B_HQ294 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00.txt', B_HQ294+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00'),
                                                                          (B_HQ294 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00.txt', B_HQ294+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00'),
                                                                          (B_HQ294 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00.txt', B_HQ294+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx10_gamma_-2.00.txt',B_HQ294+'_new_R_middle_average_logx10_gamma_-2.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx9_gamma_-2.00.txt',B_HQ294+'_new_R_middle_average_logx9_gamma_-2.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx7_gamma_-2.00.txt',B_HQ294+'_new_R_middle_average_logx7_gamma_-2.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx8_gamma_-2.00.txt',B_HQ294+'_new_R_middle_average_logx8_gamma_-2.00')]

    list_of_files_second_middlebin_HQ10000_G1_0_198_000 = [(B_HQ294 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50.txt', B_HQ294+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50'),
                                                                          (B_HQ294 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50.txt', B_HQ294+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50'),
                                                                          (B_HQ294 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50.txt', B_HQ294+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50'),
                                                                          (B_HQ294 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50.txt', B_HQ294+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx10_gamma_-2.50.txt',B_HQ294+'_new_R_middle_average_logx10_gamma_-2.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx9_gamma_-2.50.txt',B_HQ294+'_new_R_middle_average_logx9_gamma_-2.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx7_gamma_-2.50.txt',B_HQ294+'_new_R_middle_average_logx7_gamma_-2.50'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx8_gamma_-2.50.txt',B_HQ294+'_new_R_middle_average_logx8_gamma_-2.50')]

    list_of_files_outerbin_HQ10000_G1_0_198_000 = [(B_HQ294 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00.txt', B_HQ294+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00'),
                                                                          (B_HQ294 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00.txt', B_HQ294+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00'),
                                                                          (B_HQ294 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00.txt', B_HQ294+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00'),
                                                                          (B_HQ294 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00.txt', B_HQ294+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx10_gamma_-3.00.txt',B_HQ294+'_new_R_middle_average_logx10_gamma_-3.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx9_gamma_-3.00.txt',B_HQ294+'_new_R_middle_average_logx9_gamma_-3.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx7_gamma_-3.00.txt',B_HQ294+'_new_R_middle_average_logx7_gamma_-3.00'),
                                                                          (B_HQ294 + '_new_R_middle_average_logx8_gamma_-3.00.txt',B_HQ294+'_new_R_middle_average_logx8_gamma_-3.00')]

    datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_innerbin_HQ10000_G1_0_198_000 ]
    datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_first_middlebin_HQ10000_G1_0_198_000 ]
    datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_second_middlebin_HQ10000_G1_0_198_000 ]
    datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000 = [(pylab.loadtxt(f), l) for f, l in list_of_files_outerbin_HQ10000_G1_0_198_000 ]

if B_G_perturbation_different_gammas_HQ10000_G1_0_198_093:
    B_HQ382 = 'B_HQ10000_G1.0_198_093'

    list_of_files_innerbin_HQ10000_G1_0_198_093 = [(B_HQ382 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50.txt', B_HQ382+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50'),
                                                                          (B_HQ382 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50.txt', B_HQ382+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50'),
                                                                          (B_HQ382 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50.txt', B_HQ382+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50'),
                                                                          (B_HQ382 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50.txt', B_HQ382+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx10_gamma_-1.50.txt',B_HQ382+'_new_R_middle_average_logx10_gamma_-1.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx9_gamma_-1.50.txt',B_HQ382+'_new_R_middle_average_logx9_gamma_-1.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx7_gamma_-1.50.txt',B_HQ382+'_new_R_middle_average_logx7_gamma_-1.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx8_gamma_-1.50.txt',B_HQ382+'_new_R_middle_average_logx8_gamma_-1.50')]

    list_of_files_first_middlebin_HQ10000_G1_0_198_093 = [(B_HQ382 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00.txt', B_HQ382+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00'),
                                                                          (B_HQ382 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00.txt', B_HQ382+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00'),
                                                                          (B_HQ382 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00.txt', B_HQ382+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00'),
                                                                          (B_HQ382 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00.txt', B_HQ382+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx10_gamma_-2.00.txt',B_HQ382+'_new_R_middle_average_logx10_gamma_-2.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx9_gamma_-2.00.txt',B_HQ382+'_new_R_middle_average_logx9_gamma_-2.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx7_gamma_-2.00.txt',B_HQ382+'_new_R_middle_average_logx7_gamma_-2.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx8_gamma_-2.00.txt',B_HQ382+'_new_R_middle_average_logx8_gamma_-2.00')]

    list_of_files_second_middlebin_HQ10000_G1_0_198_093 = [(B_HQ382 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50.txt', B_HQ382+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50'),
                                                                          (B_HQ382 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50.txt', B_HQ382+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50'),
                                                                          (B_HQ382 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50.txt', B_HQ382+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50'),
                                                                          (B_HQ382 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50.txt', B_HQ382+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx10_gamma_-2.50.txt',B_HQ382+'_new_R_middle_average_logx10_gamma_-2.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx9_gamma_-2.50.txt',B_HQ382+'_new_R_middle_average_logx9_gamma_-2.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx7_gamma_-2.50.txt',B_HQ382+'_new_R_middle_average_logx7_gamma_-2.50'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx8_gamma_-2.50.txt',B_HQ382+'_new_R_middle_average_logx8_gamma_-2.50')]

    list_of_files_outerbin_HQ10000_G1_0_198_093 = [(B_HQ382 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00.txt', B_HQ382+'_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00'),
                                                                          (B_HQ382 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00.txt', B_HQ382+'_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00'),
                                                                          (B_HQ382 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00.txt', B_HQ382+'_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00'),
                                                                          (B_HQ382 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00.txt', B_HQ382+'_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx10_gamma_-3.00.txt',B_HQ382+'_new_R_middle_average_logx10_gamma_-3.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx9_gamma_-3.00.txt',B_HQ382+'_new_R_middle_average_logx9_gamma_-3.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx7_gamma_-3.00.txt',B_HQ382+'_new_R_middle_average_logx7_gamma_-3.00'),
                                                                          (B_HQ382 + '_new_R_middle_average_logx8_gamma_-3.00.txt',B_HQ382+'_new_R_middle_average_logx8_gamma_-3.00')]

    datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_innerbin_HQ10000_G1_0_198_093]
    datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_first_middlebin_HQ10000_G1_0_198_093]
    datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_second_middlebin_HQ10000_G1_0_198_093]
    datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_outerbin_HQ10000_G1_0_198_093]

if B_G_perturbation_different_gammas_HQ10000_G1_0_199_093:
    B_HQ475 = 'B_HQ10000_G1.0_199_093'

    list_of_files_innerbin_HQ10000_G1_0_199_093 = [(B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-1.50'),
                                                   (B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-1.50'),
                                                   (B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-1.50'),
                                                   (B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-1.50'),
                                                   (B_HQ475 + '_new_R_middle_average_logx10_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx10_gamma_-1.50'),
                                                   (B_HQ475 + '_new_R_middle_average_logx9_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx9_gamma_-1.50'),
                                                   (B_HQ475 + '_new_R_middle_average_logx7_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx7_gamma_-1.50'),
                                                   (B_HQ475 + '_new_R_middle_average_logx8_gamma_-1.50.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx8_gamma_-1.50')]

    list_of_files_first_middlebin_HQ10000_G1_0_199_093 = [(B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.00'),
                                                          (B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.00'),
                                                          (B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.00'),
                                                          (B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.00'),
                                                          (B_HQ475 + '_new_R_middle_average_logx10_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_average_logx10_gamma_-2.00'),
                                                          (B_HQ475 + '_new_R_middle_average_logx9_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_average_logx9_gamma_-2.00'),
                                                          (B_HQ475 + '_new_R_middle_average_logx7_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_average_logx7_gamma_-2.00'),
                                                          (B_HQ475 + '_new_R_middle_average_logx8_gamma_-2.00.txt',
                                                           B_HQ475 + '_new_R_middle_average_logx8_gamma_-2.00')]

    list_of_files_second_middlebin_HQ10000_G1_0_199_093 = [(B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-2.50'),
                                                           (B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-2.50'),
                                                           (B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-2.50'),
                                                           (B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-2.50'),
                                                           (B_HQ475 + '_new_R_middle_average_logx10_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_average_logx10_gamma_-2.50'),
                                                           (B_HQ475 + '_new_R_middle_average_logx9_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_average_logx9_gamma_-2.50'),
                                                           (B_HQ475 + '_new_R_middle_average_logx7_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_average_logx7_gamma_-2.50'),
                                                           (B_HQ475 + '_new_R_middle_average_logx8_gamma_-2.50.txt',
                                                            B_HQ475 + '_new_R_middle_average_logx8_gamma_-2.50')]

    list_of_files_outerbin_HQ10000_G1_0_199_093 = [(B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_VT_i_average_inside_bin_sigmatan_gamma_-3.00'),
                                                   (B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_VR_i_average_inside_bin_sigmarad_gamma_-3.00'),
                                                   (B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_VTheta_i_average_inside_bin_sigmatheta_gamma_-3.00'),
                                                   (B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_VPhi_i_average_inside_bin_sigmaphi_gamma_-3.00'),
                                                   (B_HQ475 + '_new_R_middle_average_logx10_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx10_gamma_-3.00'),
                                                   (B_HQ475 + '_new_R_middle_average_logx9_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx9_gamma_-3.00'),
                                                   (B_HQ475 + '_new_R_middle_average_logx7_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx7_gamma_-3.00'),
                                                   (B_HQ475 + '_new_R_middle_average_logx8_gamma_-3.00.txt',
                                                    B_HQ475 + '_new_R_middle_average_logx8_gamma_-3.00')]
    
    datalist_innerbin_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_innerbin_HQ10000_G1_0_199_093 ]
    datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_first_middlebin_HQ10000_G1_0_199_093 ]
    datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_second_middlebin_HQ10000_G1_0_199_093 ]
    datalist_outerbin_different_gammas_B_HQ10000_G1_0_199_093 = [(pylab.loadtxt(f), l) for f, l in list_of_files_outerbin_HQ10000_G1_0_199_093 ]

if Fig1_vr_vphi_vtheta:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1], color='Green', ls='--', lw=2, ms=7)
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0], data[:, 1], color='Red', ls='--', lw=2, ms=7)
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0], data[:, 1], color='Black', ls='--', lw=2, ms=7)

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1], color='Green', ls=':', lw=4, ms=7)
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0], data[:, 1], color='Red', ls=':', lw=4, ms=7)
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0], data[:, 1], color='Black', ls=':', lw=2, ms=7)

        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1], color='Green', ls='-.', lw=2, ms=7)
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0], data[:, 1], color='Red', ls='-.', lw=2, ms=7)
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0], data[:, 1], color='Black', ls='-.', lw=2, ms=7)

        data, label = datalist_outerbin_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1], color='Green',
                 label=r'$v_r$', lw=2, ms=7)
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:, 0], data[:, 1], color='Red',
                 label=r'$v_{\theta}$', lw=2, ms=7)
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:, 0], data[:, 1], color='Black',
                 label=r'$v_{\phi}$', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left(u \right)$', fontsize=20)
        ax1.set_title(f'File = {HQ12}', fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:, 0], data[:, 1], color='Green', ls='--', lw=2, ms=7)
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -1.5 $',ls = '--',lw=2,ms=7 )

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -2.0 $',ls = ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -2.5 $', ls =  '-.',lw=2,ms=7 )

        data, label = datalist_outerbin_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_HQ10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -1.5 $',ls ='--',lw=2,ms=7 )
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls =  '--',lw=2,ms=7 )
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--',lw=2,ms=7 )

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.5 $', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )

        data, label = datalist_outerbin_HQ10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )

        ax3.set_xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f(u) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_HQ10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -1.5 $',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = ':', lw=2,ms=7 )

        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.5 $', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.', lw=2,ms=7 )

        data, label = datalist_outerbin_HQ10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left(|u_rn|, u_rp \right)$,\
                       $\log \left(|u_{\theta}n|, u_{\theta}p \right)$ and\
                       $\log \left( |u_{\phi}n|, u_{\phi}p \right)$',
                       fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:
        
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls ='--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls =  '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls =  '--',lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls =  ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',label=r'$v_r$',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',label=r'$v_{\theta}$',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',label=r'$v_{\phi}$',lw=2,ms=7 )

        ax1.set_ylabel(r'$f\left(u \right)$', fontsize=20)
        ax1.set_title(r' File = %s' %test2_HQ0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'$\gamma = -1.5 $',ls = '--',lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'$\gamma = -2.0 $',ls = ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:, 0], data[:, 1], color='Black',
                 label=r'$\gamma = -2.5 $', ls='-.', lw=2, ms=7)

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'$\gamma = -3.0 $',lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls ='--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls =  '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls =  '--',lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls =  ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',label=r'$v_r$',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',label=r'$v_{\theta}$',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',label=r'$v_{\phi}$',lw=2,ms=7 )
 
        ax3.set_xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f(u) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--',lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

if Fig1_vr_vphi_vtheta_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Fits to file = %s, $\gamma = -2.0 $' %HQ12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$ \frac{v_r}{\sigma_r} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'$ \frac{v_{\theta}}{\sigma_{\theta}} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$ \frac{v_{\phi}}{\sigma_{\phi}} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )

        ax3.set_xlabel(r'$ u_r $, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)        
        ax1.set_title(r'Fits to file = %s, $\gamma = -2.0 $' %test2_HQ0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',label=r'$ \frac{v_r}{\sigma_r} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'$ \frac{v_{\theta}}{\sigma_{\theta}} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$ \frac{v_{\phi}}{\sigma_{\phi}} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )

        ax3.set_xlabel(r'$ u_r $, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$',
                       fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

if Fig1_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
 
     
        ax1.set_ylabel(r'$f\left(u_t \right)$', fontsize=20)
        ax1.set_title(r' File = %s' %HQ12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.', label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'$\gamma = -3.0 $',lw=2,ms=7 )
 
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.grid()

        data, label = datalist_innerbin_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',label=r'$\gamma = -3.0 $',lw=2,ms=7 )
     
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left(u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.', label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', label=r'$\gamma = -3.0 $',lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')


    if test2:

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',label=r'$\gamma = -3.0 $',lw=2,ms=7 )
      
        ax1.set_ylabel(r'$f\left(u_t \right)$', fontsize=20)
        ax1.set_title(r' File = %s' %test2_HQ0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.', label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'$\gamma = -3.0 $',lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',label=r'$\gamma = -3.0 $',lw=2,ms=7 )
     
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left(u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.', label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', label=r'$\gamma = -3.0 $',lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

if Fig1_vt_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if B:
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        popt, pcov = curve_fit(func_3, data[:,0], data[:,1])
        y_fit = func_3(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',label=r'$axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        popt, pcov = curve_fit(func_4, data[:,0], data[:,1])
        y_fit = func_4(data[:,0],popt[0],popt[1],popt[2])
        ax1.plot(data[:,0],y_fit,':',lw=3,color='green',label=r'$ax(1- (1 - q )bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $' %(popt[0],popt[1],popt[2]))

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=26)
        ax1.set_title(r'Fit to %s' %B_HQ0 , fontsize=20)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_3_log, data[:,0], data[:,1]) 
        y_fit = func_3_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',label=r'$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        popt, pcov = curve_fit(func_7_log, data[:,0], data[:,1])
        y_fit = func_7_log(data[:,0],popt[0],popt[1],popt[2])
        ax2.plot(data[:,0],y_fit,':',lw=3,color='green',label=r'$a\cdot \log(x)^2(1- (1 - q )b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $' %(popt[0],popt[1],popt[2]))

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=26)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',label=r'$\gamma = -3.0 $',lw=2,ms=7 )
     
        ax3.set_xlabel(r'$ u_t $', fontsize=26)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=26)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.', label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', label=r'$\gamma = -3.0 $',lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=26)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=26)
        ax4.grid()
        ax4.set_yscale('log')
    
if Fig2_vr_vphi_vtheta_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[1]
        ax1.plot(data[:,0], data[:,1]/(478.006*np.exp(-0.456*data[:,0]**2)),color = 'Green',label=r'$r, a=478.006, b=0.456$', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1]/(482.605*np.exp(-0.473*data[:,0]**2)),color = 'Red',label=r'$\theta, a=482.605, b=0.473$',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1]/(502.652*np.exp(-0.477*data[:,0]**2)),color = 'Black',label=r'$\phi, a=502.652, b=0.477$',ls =  ':',lw=2,ms=7 )

        ax1.set_xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left(u \right)}{ae^{-bx^2}}$', fontsize=20)
        ax1.set_title(r' File = %s, $\gamma = -2.0 $' %HQ12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1]/(1433.228*10**data[:,0]*np.exp(-0.472*(10**data[:,0])**2)),color = 'Green',label=r'$a=1433.228, b=0.472$', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1]/(1416.346*10**data[:,0]*np.exp(-0.473*(10**data[:,0])**2)),color = 'Red', label=r'$ a=1416.346, b=0.473 $', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1]/(1405.914*10**data[:,0]*np.exp(-0.470*(10**data[:,0])**2)),color = 'Black', label=r'$ a=1405.914, b=0.470$',ls = ':', lw=2,ms=7 )

        ax2.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$', fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{axe^{-b\log (x)^2}}$', fontsize=20)  # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

    if test2:        
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1]/(478.006*np.exp(-0.456*data[:,0]**2)),color = 'Green',label=r'$r, a=478.006, b=0.456$', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1]/(482.605*np.exp(-0.473*data[:,0]**2)),color = 'Red',label=r'$\theta, a=482.605, b=0.473$',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1]/(502.652*np.exp(-0.477*data[:,0]**2)),color = 'Black',label=r'$\phi, a=502.652, b=0.477$',ls =  ':',lw=2,ms=7 )

        ax1.set_xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left(u \right)}{ae^{-bx^2}}$', fontsize=20)
        ax1.set_title(r' File = %s, $\gamma = -2.0 $' %test2_HQ0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1]/(1433.228*10**data[:,0]*np.exp(-0.472*(10**data[:,0])**2)),color = 'Green',label=r'$a=1433.228, b=0.472$', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1]/(1416.346*10**data[:,0]*np.exp(-0.473*(10**data[:,0])**2)),color = 'Red', label=r'$ a=1416.346, b=0.473 $', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1]/(1405.914*10**data[:,0]*np.exp(-0.470*(10**data[:,0])**2)),color = 'Black', label=r'$ a=1405.914, b=0.470$',ls = ':', lw=2,ms=7 )

        ax2.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$', fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{axe^{-b\log (x)^2}}$', fontsize=20)  
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

if Fig2a_vt_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:
        data, label = datalist_innerbin_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0],data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',ls = '--',label=r'$ \gamma = -1.5 $',lw=3)
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue', ls =  ':',label=r'$ \gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue', ls =  '-.',label=r'$ \gamma = -2.5 $',lw=4,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',label=r'$ \gamma = -3.0 $',lw=2,ms=7 )

        ax1.set_ylim(0,2)
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$', fontsize=20)
        ax1.set_title(r' File = %s' %HQ12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',ls = '--', label=r'$ \gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue', ls =  ':', label=r'$ \gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue', ls =  '-.', label=r'$ \gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue', label=r'$ \gamma = -3.0 $',lw=2,ms=7 )

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3400.442x^2e^{-0.930x^2}}$', fontsize=20)  # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}
        ax2.grid()

    if test2:
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0],data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',ls = '--',label=r'$ \gamma = -1.5 $',lw=3)
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue', ls =  ':',label=r'$ \gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue', ls =  '-.',label=r'$ \gamma = -2.5 $',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',label=r'$ \gamma = -3.0 $',lw=2,ms=7 )

        ax1.set_ylim(0,2)
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$', fontsize=20)
        ax1.set_title(r' File = %s' %test2_HQ0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',ls = '--', label=r'$ \gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue', ls =  ':', label=r'$ \gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue', ls =  '-.', label=r'$ \gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue', label=r'$ \gamma = -3.0 $',lw=2,ms=7 )

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3400.442x^2e^{-0.930x^2}}$', fontsize=20)  
        ax2.grid()

if Fig6_Gperturbations_same_gammas_as_IC_vr:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    data, label = datalist_innerbin_HQ10000_G1_0_0_000[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
             label=r'%s' %HQ0[len('HQ10000_G'):],lw=2,ms=7 )   
    data, label = datalist_innerbin_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
             label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
             label=r'%s' %HQ18[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
             label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
             label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--',
             label=r'%s' %HQ70[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet',ls ='--',lw=2,ms=7 )

    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[0] # ,label=r'$\gamma = -2.0$'
    ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=4,ms=7 )

    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[0] # ,label=r'$\gamma = -2.5$'
    ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet', ls =  '-.',lw=4,ms=7 )

    data, label = datalist_outerbin_HQ10000_G1_0_0_000[0] # ,label=r'$\gamma = -3.0$'
    ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7 )

    ax1.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
    ax1.set_title(r' Time evolution of files = %s' %HQ0[:-9], fontsize=20)
    ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
               frameon=True,loc=0,handlelength=2.5)
    ax1.grid()

    data, label = datalist_innerbin_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -1.5$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
             label=r'%s' %HQ0[len('HQ10000_G'):],lw=2,ms=7 )   
    data, label = datalist_innerbin_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],
             color = 'Skyblue',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
             label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
             label=r'%s' %HQ18[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
             label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
             label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--',
             label=r'%s' %HQ70[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet',ls = '--',lw=2,ms=7 )

    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[4] # label=r'$\gamma = -2.0$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[4]
    ax2.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=2,ms=7 )

    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[4] # label=r'$\gamma = -2.5$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet', ls =  '-.',lw=2,ms=7 )

    data, label = datalist_outerbin_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -3.0$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7 )

    ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$', fontsize=20)
    ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
    ax2.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax2.grid()

    data, label = datalist_innerbin_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -1.5$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
             label=r'%s' %HQ0[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
             label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
             label=r'%s' %HQ18[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
             label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
             label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--',
             label=r'%s' %HQ70[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet',ls ='--',lw=2,ms=7 )

    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -2.0$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=4,ms=7 )

    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -2.5$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet', ls =  '-.',lw=4,ms=7 )

    data, label = datalist_outerbin_HQ10000_G1_0_0_000[0]  # label=r'$\gamma = -3.0$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7 )

    ax3.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
    ax3.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')

    data, label = datalist_innerbin_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -1.5$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s' %HQ0[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s' %HQ18[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--', label=r'%s' %HQ70[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet',ls = '--',lw=2,ms=7 )

    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -2.0$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=2,ms=7 )

    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -2.5$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet',ls =  '-.',lw=2,ms=7 )

    data, label = datalist_outerbin_HQ10000_G1_0_0_000[4]  # label=r'$\gamma = -3.0$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7 )

    ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$', fontsize=20)
    ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
    ax4.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax4.grid()
    ax4.set_yscale('log')

if Fig6_Gperturbations_G1_2_same_gammas_as_IC_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    data, label = datalist_innerbin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7)
    data, label = datalist_innerbin_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
    data, label = datalist_innerbin_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7)
    data, label = datalist_first_middlebin_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7)
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7)
    data, label = datalist_first_middlebin_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7)
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7)
 
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7)
    data, label = datalist_second_middlebin_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7)
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7)
    data, label = datalist_second_middlebin_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7)
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7)

    data, label = datalist_outerbin_HQ10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
    data, label = datalist_outerbin_HQ10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
    data, label = datalist_outerbin_HQ10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
 
    ax1.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
    ax1.set_title(r' Time evolution of files = %s' %HQ0[:-9] , fontsize=20)
    ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax1.grid()

    data, label = datalist_innerbin_HQ10000_G1_2_1_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
             label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_3_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
             label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
             label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_7_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',
             label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
             label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_3_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_7_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )

    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_3_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )    
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_7_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[4] 
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
  
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_3_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_7_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[4]  
    ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
   
    ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$', fontsize=20)
    ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
    ax2.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax2.grid()

    data, label = datalist_innerbin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
             label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
             label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
             label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',
             label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
             label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
    
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
    
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

    ax3.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
    ax3.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')

    data, label = datalist_innerbin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
             label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
             label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 ) 
    data, label = datalist_innerbin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
             label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',
             label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
             label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
 
    data, label = datalist_first_middlebin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 ) 
    data, label = datalist_first_middlebin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
    
    data, label = datalist_second_middlebin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
    
    data, label = datalist_outerbin_HQ10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
    data, label = datalist_outerbin_HQ10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    
    ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$',
                   fontsize=20)
    ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                   fontsize=20)
    ax4.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    ax4.grid()
    ax4.set_yscale('log')

if Fig10_Gperturbations_different_gammas_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:    
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
      
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
     
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )

        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
     
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins' %HQ0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )    
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
      
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
       
        #ax2.set_xlim(-3,0)
        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
        
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
                 label=r'%s' %HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )
     
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
        
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
        
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:    
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'%s' %test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins' %test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')
        
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if B:
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--',
                 label=r'%s' %B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
     
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins' %B_HQ0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()
        
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',lw=2,ms=7 )

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )    
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4] 
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',lw=2,ms=7 )
        
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',lw=2,ms=7 )
     
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
        
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
        
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        
if Fig11_Gperturbations_gammas_1_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s, different r bins, $\gamma = -1.5$' %HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0] ** 2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()
        
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -1.5$' %test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])       
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color='Blue', lw=2, ms=7)

        ax6.set_xticklabels([])
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -1.5$' %A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %A_HQ36[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %A_HQ246[len('A_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %A_HQ298[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 ) 

        ax7.set_ylim(0.5,1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0.5,1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if B:        
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -1.5$' %B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])         
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Orange',lw=2,ms=7)

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
 
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

if Fig12_Gperturbations_gammas_2_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_first_middlebin__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$' %HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$' %test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if A:        
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.0$' %A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %A_HQ36[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %A_HQ246[len('A_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %A_HQ298[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 ) 

        ax7.set_ylim(0.5,1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax8.plot(data[:,0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.0$' %B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Red',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Green',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Black',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Brown',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:,0],
                 data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Orange',lw=2,ms=7)

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
 
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

if Fig13_Gperturbations_gammas_2_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:        
        data, label = datalist_second_middlebin__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.5$' %HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left(|u_n|, u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.5 $' %test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2}}$',
                                fontsize=20)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 )

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.5$' %A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %A_HQ36[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %A_HQ246[len('A_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %A_HQ298[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(.5, 1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1 - (1 - .946) * .908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 ) 

        ax7.set_ylim(.5, 1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis}$', fontsize=20)
        ax7.grid()

        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0.5,1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.5$' %B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Orange',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

if Fig14_Gperturbations_gammas_3_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_outerbin__different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -3.0$' %HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],
                 color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],
                 color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -3.0 $' %test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %test2_HQ36[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %test2_HQ96[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %test2_HQ126[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %test2_HQ159[len('test2_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left(|u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_15_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_20_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -3.0$' %A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %A_HQ36[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %A_HQ246[len('A_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %A_HQ298[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$',
                       fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 ) 

        ax7.set_ylim(0.5,1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_40_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_009[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(.5, 1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$',
                       fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1], color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1], color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1], color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1], color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1], color = 'Orange', lw=2, ms=7)

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -3.0$' %B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %B_HQ36[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %B_HQ66[len('B_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %B_HQ294[len('B_HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %B_HQ382[len('B_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),
                 color = 'Orange',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_5_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_000[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_HQ10000_G1_0_198_093[4]  
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Orange',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

# datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_25_005  

if Fig15_Gperturbations_R_middle_19_95_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -1.5$' %HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7 )

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$',
                                fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_3_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_5_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_7_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_HQ10000_G1_2_9_005[4]  
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s ,  $ R_{middle} = 19.95 $' %test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % test2_HQ0[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %test2_HQ66[len('test2_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %test2_HQ166[len('test2_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

    
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )
   
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s ,  $ R_{middle} = 19.95 $' %A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],
                 color = 'Red', lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],
                 color = 'Black', lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],
                 color = 'Blue', lw=2,ms=7 )

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )
   
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
 
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Black',lw=2,ms=7 )
 
        data, label = datalist_large_R_middle_19_95_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Blue',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)        

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s ,  $ R_{middle} = 19.95 $' %B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % B_HQ0[len('B_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color='Red', lw=2, ms=7)

        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )

        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7 )

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()
 
if Fig16_Gperturbations_R_middle_31_62_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)

        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$' %HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % HQ12[len('HQ10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %HQ24[len('HQ10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %HQ36[len('HQ10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %HQ48[len('HQ10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %HQ60[len('HQ10000_G'):],lw=2,ms=7)

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)

        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 ) 
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )

        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
                       fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )

        ax5.set_xticklabels([])         
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Red',lw=2,ms=7 ) 
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Green',lw=2,ms=7 )
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Black',lw=2,ms=7 )
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Brown',lw=2,ms=7 )
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),
                 color = 'Orange',lw=2,ms=7 )

        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                                fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , $ R_{middle} = 31.62$' %test2_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % test2_HQ0[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %test2_HQ66[len('HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %test2_HQ166[len('HQ10000_G'):],lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[4]  
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp\
                       \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Blue',lw=2,ms=7 )
 
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x\
                                \cdot e^{-0.922 \cdot x^2} }$',
                                fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*
                     np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*
                     np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(data[:,0],
                 data[:,1]/(3424.993*(10**data[:,0])**2*
                     np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',lw=2,ms=7 )

        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                                {3424.993 \cdot x^2 \cdot e^{-0.930\
                                \cdot x^2 }}$',
                                fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(data[:,0],
                 data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color = 'Blue',lw=2,ms=7 )

        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis}$', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*
                 .924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color = 'Red',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                 .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                                             .924 * 10 ** (data[:, 0] ** 2)) **
                                 (.987 / (1. - .987))),
                 color='Blue', lw=2, ms=7)

        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                                       \right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s, $ R_{middle} = 31.62 $'\
                      % A_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % A_HQ0[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %A_HQ66[len('A_HQ10000_G'):],lw=2,ms=7 )
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'%s' %A_HQ382[len('A_HQ10000_G'):],lw=2,ms=7 )

        ax2.set_ylabel(r'$f\left(\log \left(|u_tn|, u_tp \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], color='Red', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax3.plot(data[:, 0], data[:, 1], color='Black', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax3.plot(data[:, 0], data[:, 1], color='Blue', lw=2, ms=7)

        ax3.set_ylabel(r'$\log \left(f\left(u_t \right) \right)$',
                       fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:, 0], data[:, 1], color='Red', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax4.plot(data[:, 0], data[:, 1], color='Black', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[4]  
        ax4.plot(data[:, 0], data[:, 1], color='Blue', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|, u_tp \right)\
                                             \right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                     np.exp(-.922 * data[:, 0] ** 2)),
                 color='Red', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                     np.exp(-.922 * data[:, 0] ** 2)),
                 color='Black', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                     np.exp(-.922 * data[:, 0] ** 2)),
                 color='Blue', lw=2, ms=7)
      
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2} }$',
                       fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                 np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 color='Red', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                 np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 color='Black', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                 np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 color='Blue', lw=2, ms=7)

        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left(|u_tn|, u_tp\
                       \right)\right)}\{3424.993 \cdot x^2 \cdot e^{-0.930\
                       \cdot x^2 }}$',
                       fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946) * .908 *
                     data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 color='Red', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946) * .908 *
                     data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 color='Black', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946) * .908 *
                     data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 color='Blue', lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                     .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 color='Red', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_10_005[4]  
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                     .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. -.987))),
                 color='Black', lw=2, ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                     .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 color='Blue', lw=2, ms=7)

        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|, u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                                       \right)}{Tsallis}$',
                       fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax1.plot(data[:, 0], data[:, 1], color='Red', lw=2, ms=7)

        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s, $R_{middle} = 31.62$'
                      % B_HQ0[:-9],
                      fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax2.plot(data[:, 0], data[:, 1], color='Red',
                 label=r'%s' % B_HQ0[len('B_HQ10000_G'):], lw=2, ms=7)

        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax3.plot(data[:, 0], data[:, 1], color='Red', lw=2, ms=7)

        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000[4]  
        ax4.plot(data[:, 0], data[:, 1], color='Red', lw=2, ms=7)

        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|, u_tp \right)\
                                             \right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (887.569 * data[:, 0] *
                               np.exp(-.922 * data[:, 0] ** 2)),
                 color='Red', lw=2, ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x\
                                \cdot e^{-0.922 \cdot x^2} }$',
                       fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(data[:, 0],
                 data[:, 1] / (3424.993 * (10 ** data[:, 0]) ** 2 *
                               np.exp(-.930 * (10 ** data[:, 0]) ** 2)),
                 color='Red', lw=2, ms=7)
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp \right)\right)}\
                                {3424.993 \cdot x^2\
                                \cdot e^{-0.930 \cdot x^2 }}$',
                       fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(data[:, 0],
                 data[:, 1] / (864.543 * data[:, 0] * (1 - (1 - .946) *
                     .908 * data[:, 0] ** 2) ** (.946 / (1 - .946))),
                 color='Red', lw=2, ms=7)

        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(data[:, 0],
                 data[:, 1] / (3391.113 * 10 ** data[:, 0] * (1 - (1 - .987) *
                     .924 * 10 ** (data[:, 0] ** 2)) ** (.987 / (1. - .987))),
                 color='Red', lw=2, ms=7)
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|, u_tp\
                                                  \right)\right)}{Tsallis}$',
                       fontsize=20)
        ax8.grid()

plt.show()
