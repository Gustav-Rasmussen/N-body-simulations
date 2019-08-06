#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:01:32 2019

@author: gustavcollinrasmussen
"""

textFilesPath, figurePath, F = ''

(R, Gammas, x, y, z, Rcl, Vcl, xclrec, yclrec, vxnew, vynew, vznew, VR, VTheta,
 VPhi, VT, Phi, VR_sigmaR, VTheta_sigmatheta, VPhi_sigmaphi, VT_sigmaT,
 VR_i_avg_in_bin_sigmaR, VTheta_i_avg_in_bin_sigmatheta,
 VPhi_i_avg_in_bin_sigmaphi, VT_i_avg_in_bin_sigmaT,
 sigmaR2, sigmatheta2, sigmaphi2, sigmaR, sigmatheta, sigmaphi, Beta,
 xcl2, ycl2, zcl2, vxnew2, vynew2, vznew2,
 v_t_arr, v_r_arr, VR_sigmarad) = []

GoodIDs = 0

(Gamma, R_middle, m, nr_bins, max_binning_R_unitRmax, min_binning_R_unitRmax,
 R_limit, vMin, vMax, nr_v_bins, v_t_len) = 0
