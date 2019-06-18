#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:56:42 2019

@author: gustavcollinrasmussen
"""

import pylab

# [5],[6],[7] : log9, log7, log8 : r, Theta, Phi

#  B_G_Pert_different_gammas_HQ10000_G1_0_0_000:
B_HQ0 = 'B_HQ10000_G1.0_0_000'

# VT_i_BinAvg_sigmaT_gamma_
# VT_i_BinAvg_sigmaT_R_middle
# logx10_gamma_-1.50.txt' 10 9 7 8
# _avg_logx10_gamma_%.2f.txt'

FileLstbin1HQ10000_G1_0_0_000 = [(B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-1.50.txt',
                                  B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-1.50'),
                                 (B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-1.50.txt',
                                  B_HQ0 + 'VR_i_BinAvg_sigmaR_gamma_-1.50'),
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

FileLstbin2HQ10000_G1_0_0_000 = [(B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-2.00.txt',
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

FileLstbin3HQ10000_G1_0_0_000 = [(B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-2.50.txt',
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

FileLstbin4HQ10000_G1_0_0_000 = [(B_HQ0 + 'VT_i_BinAvg_sigmaT_gamma_-3.00.txt',
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
                                  + 'VT_i_BinAvg_sigmaT_R_middle_19.95'),
                                 (B_HQ0
                                  + 'VR_i_BinAvg_sigmaR_R_middle_19.95.txt',
                                  B_HQ0 + 'VR_i_BinAvg_sigmaR_R_middle_19.95'),
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
                                              FileLstbin1HQ10000_G1_0_0_000]
bin2_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2HQ10000_G1_0_0_000]
bin3_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3HQ10000_G1_0_0_000]
bin4_different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin4HQ10000_G1_0_0_000]
datalist_bin5different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin5HQ10000_G1_0_0_000]
datalist_bin6different_gammas_B_HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l) for f, l in FileLstbin6HQ10000_G1_0_0_000]

#  B_G_Pert_different_gammas_HQ10000_G1_0_5_005:
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

#  B_G_Pert_different_gammas_HQ10000_G1_0_10_005:
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

bin1_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin1HQ10000_G1_0_10_005]
bin2_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin2HQ10000_G1_0_10_005]
bin3_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin3HQ10000_G1_0_10_005]
bin4_different_gammas_B_HQ10000_G1_0_10_005 = [(pylab.loadtxt(f), l) for f, l in FileLstbin4HQ10000_G1_0_10_005]

#  B_G_Pert_different_gammas_HQ10000_G1_0_198_000:
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

#  B_G_Pert_different_gammas_HQ10000_G1_0_198_093:
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

#  B_G_Pert_different_gammas_HQ10000_G1_0_199_093:
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
