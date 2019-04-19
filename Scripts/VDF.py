# -*- coding: utf-8 -*-

# from __future__ import division
import h5py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
from pylab import *
import pylab
from scipy.stats import norm
import matplotlib.mlab as mlab
import scipy as sp
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from pathlib import Path
import Gammas_and_R_middles
import RhoAndGaussianAndTsallis
import getSnapshotValues
import snapshotFiles
from definePaths import *
import radius_and_velocity_funcs as ravf

# Run 3D plots with this command from terminal:
# ~/python/3dplot/bin/python VDF.py

# readline will not be well behaved unless this is installed:
# pip install gnureadline

# Make switches to control figures, print statements, binning etc.
Fig_xz = 0
Fig_3D_xyz = 0
vspherical = 0
calc_sigma_binned_lin_radius = 0
vsphericalnew_sigma = 0
print_Vp_Vn = 0
print_sigma_binned_lin_radius = 0

if Fig_xz:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)

    ax1.plot(x, y, "o", ms=1)
    ax1.set_xlabel("x", fontsize=30)
    ax1.set_ylabel("y", fontsize=30)
    ax1.set_title(r"positions ($N = %i$)" % len(x), fontsize=30)

    ax2.plot(x, z, "o", ms=1)
    ax2.set_xlabel("x", fontsize=30)
    ax2.set_ylabel("z", fontsize=30)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")

    f.savefig(figurePath + "Fig_xz.png")


def randrange(n, vmin, vmax):  # 3D scatterplot of positions
    """."""
    return (vmax - vmin) * np.random.rand(n) + vmin


if Fig_3D_xyz:
    f = plt.figure()
    ax = f.add_subplot(111, projection="3d")
    n = 100
    for c, m, zl, zh in [("r", "o", -50, -25), ("b", "^", -30, -5)]:
        ax.scatter(x, y, z, c=c, marker=m)
    ax.set_xlabel("x", fontsize=20)
    ax.set_ylabel("y", fontsize=20)
    ax.set_zlabel("z", fontsize=20)
    ax.set_title(
        "3D view of halo structure.($N = %i$, $\gamma = %.2f$)"
        % (len(x), Gamma),
        fontsize=20,
    )

# radial and tangential velocities
if vspherical:
    r = ravf.radius(x, y, z)
    Phi = ravf.phi(x, y)
    Theta = ravf.theta(r, z)
    VR = ravf.v_R(vx, vy, vz, Theta, Phi)
    VTheta = ravf.v_theta(vx, vy, vz, Theta, Phi)
    VPhi = ravf.v_phi(vx, vy, Phi)
    VT = ravf.v_tan(VTheta, VPhi)


def sigma2(num=nr_par_inside_bin_i, v2):
    """num: number of particles. v2: velocity squared"""
    return (1.0 / (num + 1.0)) * np.sum(v2)


if calc_sigma_binned_lin_radius:
    R_hob_par = R[GoodIDs]
    v2 = ravf.speed(vx, vy, vz) ** 2

    (
        sigma2,
        sigmarad2,
        sigmatheta2,
        sigmaphi2,
        sigmatan2,
        sigma,
        sigmarad,
        sigmatheta,
        sigmaphi,
        sigmatan,
        VR_sigmarad,
        VTheta_sigmatheta,
        VPhi_sigmaphi,
        VT_sigmatan,
        r,
        Phi,
        Theta,
        VR,
        VTheta,
        VPhi,
        VT,
        VR_i_average_inside_bin,
        VT_i_average_inside_bin,
        VTheta_i_average_inside_bin,
        VPhi_i_average_inside_bin,
        VR_i_average_inside_bin_sigmarad,
        VT_i_average_inside_bin_sigmatan,
        VTheta_i_average_inside_bin_sigmatheta,
        VPhi_i_average_inside_bin_sigmaphi,
        bin_radius_arr,
    ) = ([] for i in range(30))

    min_binning_R = -1.5
    max_binning_R = np.log10(R_limit)
    # min_binning_R = R_limit_min
    # max_binning_R = R_limit_max

    binning_arr = np.logspace(min_binning_R, max_binning_R, nr_binning_bins)
    # binning_arr = np.linspace(R_limit_min, R_limit_max, nr_binning_bins)

    j = 0
    for i in range(nr_binning_bins - 2):
        min_R_bin_i = binning_arr[j]  # start of bin
        max_R_bin_i = binning_arr[j + 1]  # end of bin
        # position of particles inside a radial bin
        posR_par_inside_bin_i = np.where(
            (R_hob_par > min_R_bin_i) & (R_hob_par < max_R_bin_i)
        )
        nr_par_inside_bin_i = len(posR_par_inside_bin_i[0])
        if nr_par_inside_bin_i == 0:
            print("-", i)
            continue
        print("+", i)
        
        x = x[posR_par_inside_bin_i]
        y = y[posR_par_inside_bin_i]
        z = z[posR_par_inside_bin_i]

        vx = vx[posR_par_inside_bin_i]
        vy = vy[posR_par_inside_bin_i]
        vz = vz[posR_par_inside_bin_i]        

        r_i = ravf.radius(x, y, z)
        Phi_i = ravf.phi(x, y)
        Theta_i = ravf.theta(r_i, z)
        VR_i = ravf.v_R(vx, vy, vz, Theta_i, Phi_i)
        VTheta_i = ravf.v_theta(vx, vy, vz, Theta_i, Phi_i)
        VPhi_i = ravf.v_phi(vx, vy, Phi_i)

        VT_i = (VTheta_i ** 2 + VPhi_i ** 2) ** .5

        # sigma2 total
        v2_inside_bin_i = v2[posR_par_inside_bin_i]
        sigma2_inside_bin_i = sigma2(v2_inside_bin_i)
        sigma2.append(sigma2_inside_bin_i)
        bin_radius_arr.append((max_R_bin_i + min_R_bin_i) / 2)

        # sigmatan2
        vtan2_inside_bin_i = VT_i ** 2
        sigmatan2_inside_bin_i = sigma2(vtan2_inside_bin_i)
        sigmatan2.append(sigmatan2_inside_bin_i)

        # sigmarad2 radial
        vrad2_inside_bin_i = VR_i ** 2
        sigmarad2_inside_bin_i = sigma2(vrad2_inside_bin_i)
        sigmarad2.append(sigmarad2_inside_bin_i)

        # sigmatheta2
        VTheta2_inside_bin_i = VTheta_i ** 2
        sigmatheta2_inside_bin_i = sigma2(VTheta2_inside_bin_i)
        sigmatheta2.append(sigmatheta2_inside_bin_i)

        # sigmaphi2
        VPhi2_inside_bin_i = VPhi_i ** 2
        sigmaphi2_inside_bin_i = sigma2(VPhi2_inside_bin_i)
        sigmaphi2.append(sigmaphi2_inside_bin_i)

        VR_i_average_inside_bin_i = sigma2(VR_i)
        VT_i_average_inside_bin_i = sigma2(VT_i)
        VTheta_i_average_inside_bin_i = sigma2(VTheta_i)
        VPhi_i_average_inside_bin_i = sigma2(VPhi_i)

        VR_i_average_inside_bin.append(VR_i_average_inside_bin_i)
        VT_i_average_inside_bin.append(VT_i_average_inside_bin_i)
        VTheta_i_average_inside_bin.append(VTheta_i_average_inside_bin_i)
        VPhi_i_average_inside_bin.append(VPhi_i_average_inside_bin_i)

        sigma_i = (sigma2[j]) ** .5
        sigmarad_i = (sigmarad2[j]) ** .5
        sigmatheta_i = (sigmatheta2[j]) ** .5
        sigmaphi_i = (sigmaphi2[j]) ** .5
        sigmatan_i = (sigmatan2[j]) ** .5

        sigma.append(sigma_i)
        sigmarad.append(sigmarad_i)
        sigmatheta.append(sigmatheta_i)
        sigmaphi.append(sigmaphi_i)
        sigmatan.append(sigmatan_i)
        r.append(r_i)
        Phi.append(Phi_i)
        Theta.append(Theta_i)
        VR.append(VR_i)
        VTheta.append(VTheta_i)
        VPhi.append(VPhi_i)
        VT.append(VT_i)
        VR_sigmarad.append(VR_i / sigmarad_i)
        VTheta_sigmatheta.append(VTheta_i / sigmatheta_i)
        VPhi_sigmaphi.append(VPhi_i / sigmaphi_i)
        VT_sigmatan.append(VT_i / sigmatan_i)
        VR_i_average_inside_bin_sigmarad.append(
            VR_i_average_inside_bin_i / sigmarad_i
        )
        VT_i_average_inside_bin_sigmatan.append(
            VT_i_average_inside_bin_i / sigmatan_i
        )
        VTheta_i_average_inside_bin_sigmatheta.append(
            VTheta_i_average_inside_bin_i / sigmatheta_i
        )
        VPhi_i_average_inside_bin_sigmaphi.append(
            VPhi_i_average_inside_bin_i / sigmaphi_i
        )

        j += 1

    sigma2 = np.array(sigma2)
    sigmarad2 = np.array(sigmarad2)
    sigmatheta2 = np.array(sigmatheta2)
    sigmaphi2 = np.array(sigmaphi2)
    sigmatan2 = np.array(sigmatan2)
    sigma = np.array(sigma)
    sigmarad = np.array(sigmarad)
    sigmatheta = np.array(sigmatheta)
    sigmaphi = np.array(sigmaphi)
    sigmatan = np.array(sigmatan)

if vsphericalnew_sigma:
    (
        VR_sigmarad_p,
        VR_sigmarad_n,
        VTheta_sigmatheta_p,
        VTheta_sigmatheta_n,
        VPhi_sigmaphi_p,
        VPhi_sigmaphi_n,
        VT_sigmatan_p,
        VT_sigmatan_n,
    ) = ([] for i in range(8))

    for i in range(len(VR_sigmarad)):
        if VR_sigmarad[i] >= 0.0:
            VR_sigmarad_p.append(VR_sigmarad[i])
        else:
            VR_sigmarad_n.append(VR_sigmarad[i])
    VR_sigmarad_p_arr = np.asarray(VR_sigmarad_p)
    VR_sigmarad_n_arr = np.asarray(VR_sigmarad_n)

    for i in range(len(VR_sigmarad)):
        if VTheta_sigmatheta[i] >= 0.0:
            VTheta_sigmatheta_p.append(VTheta_sigmatheta[i])
        else:
            VTheta_sigmatheta_n.append(VTheta_sigmatheta[i])
    VTheta_sigmatheta_p_arr = np.asarray(VTheta_sigmatheta_p)
    VTheta_sigmatheta_n_arr = np.asarray(VTheta_sigmatheta_n)

    for i in range(len(VR_sigmarad)):
        if VPhi_sigmaphi[i] >= 0.0:
            VPhi_sigmaphi_p.append(VPhi_sigmaphi[i])
        else:
            VPhi_sigmaphi_n.append(VPhi_sigmaphi[i])
    VPhi_sigmaphi_p_arr = np.asarray(VPhi_sigmaphi_p)
    VPhi_sigmaphi_n_arr = np.asarray(VPhi_sigmaphi_n)

    for i in range(len(VR_sigmarad)):
        if VT_sigmatan[i] >= 0.0:
            VT_sigmatan_p.append(VT_sigmatan[i])
        else:
            VT_sigmatan_n.append(VT_sigmatan[i])
    VT_sigmatan_p_arr = np.asarray(VT_sigmatan_p)
    VT_sigmatan_n_arr = np.asarray(VT_sigmatan_n)

    (
        VR_i_average_inside_bin_sigmarad_p,
        VR_i_average_inside_bin_sigmarad_n,
        VT_i_average_inside_bin_sigmatan_p,
        VT_i_average_inside_bin_sigmatan_n,
        VPhi_i_average_inside_bin_sigmaphi_p,
        VPhi_i_average_inside_bin_sigmaphi_n,
        VTheta_i_average_inside_bin_sigmatheta_p,
        VTheta_i_average_inside_bin_sigmatheta_n,
    ) = ([] for i in range(8))

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VR_i_average_inside_bin_sigmarad[i] >= 0.0:
            VR_i_average_inside_bin_sigmarad_p.append(
                VR_i_average_inside_bin_sigmarad[i]
            )
        else:
            VR_i_average_inside_bin_sigmarad_n.append(
                VR_i_average_inside_bin_sigmarad[i]
            )
    VR_i_average_inside_bin_sigmarad_p_arr = np.asarray(
        VR_i_average_inside_bin_sigmarad_p
    )
    VR_i_average_inside_bin_sigmarad_n_arr = np.asarray(
        VR_i_average_inside_bin_sigmarad_n
    )

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VTheta_i_average_inside_bin_sigmatheta[i] >= 0.0:
            VTheta_i_average_inside_bin_sigmatheta_p.append(
                VTheta_i_average_inside_bin_sigmatheta[i]
            )
        else:
            VTheta_i_average_inside_bin_sigmatheta_n.append(
                VTheta_i_average_inside_bin_sigmatheta[i]
            )
    VTheta_i_average_inside_bin_sigmatheta_p_arr = np.asarray(
        VTheta_i_average_inside_bin_sigmatheta_p
    )
    VTheta_i_average_inside_bin_sigmatheta_n_arr = np.asarray(
        VTheta_i_average_inside_bin_sigmatheta_n
    )

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VPhi_i_average_inside_bin_sigmaphi[i] >= 0.0:
            VPhi_i_average_inside_bin_sigmaphi_p.append(
                VPhi_i_average_inside_bin_sigmaphi[i]
            )
        else:
            VPhi_i_average_inside_bin_sigmaphi_n.append(
                VPhi_i_average_inside_bin_sigmaphi[i]
            )
    VPhi_i_average_inside_bin_sigmaphi_p_arr = np.asarray(
        VPhi_i_average_inside_bin_sigmaphi_p
    )
    VPhi_i_average_inside_bin_sigmaphi_n_arr = np.asarray(
        VPhi_i_average_inside_bin_sigmaphi_n
    )

    for i in range(len(VR_i_average_inside_bin_sigmarad)):
        if VT_i_average_inside_bin_sigmatan[i] >= 0.0:
            VT_i_average_inside_bin_sigmatan_p.append(
                VT_i_average_inside_bin_sigmatan[i]
            )
        else:
            VT_i_average_inside_bin_sigmatan_n.append(
                VT_i_average_inside_bin_sigmatan[i]
            )
    VT_i_average_inside_bin_sigmatan_p_arr = np.asarray(
        VT_i_average_inside_bin_sigmatan_p
    )
    VT_i_average_inside_bin_sigmatan_n_arr = np.asarray(
        VT_i_average_inside_bin_sigmatan_n
    )

if print_Vp_Vn:
    if print_sigma_binned_lin_radius:
        print(
            f"sigmarad2 = {sigmarad2}",
            f"sigmarad2.shape = {sigmarad2.shape}",
            f"sigmatheta2 = {sigmatheta2}",
            f"sigmatheta2.shape = {sigmatheta2.shape}",
            f"sigmaphi2 = {sigmaphi2}",
            f"sigmaphi2.shape = {sigmaphi2.shape}",
            f"sigmarad = {sigmarad}",
            f"sigmarad.shape = {sigmarad.shape}",
            f"sigmatheta = {sigmatheta}",
            f"sigmatheta.shape = {sigmatheta.shape}",
            f"sigmaphi = {sigmaphi}",
            f"sigmaphi.shape = {sigmaphi.shape}",
            f"VR = {VR}",
            f"VR.shape = {VR.shape}",
            f"VTheta = {VTheta}",
            f"VTheta.shape = {VTheta.shape}",
            f"VPhi = {VPhi}",
            f"VPhi.shape = {VPhi.shape}",
            f"VR_sigmarad.shape = {(VR / sigmarad).shape}",
            f"VR_sigmarad = {VR / sigmarad}",
            f"np.where(sigmarad == 0) = {np.where(sigmarad == 0)}",
            f"np.where(sigmatheta == 0) = {np.where(sigmatheta == 0)}",
            f"np.where(sigmaphi == 0) = {np.where(sigmaphi == 0)}",
        )

# All figures with log(v) can instead be plotted as log(v) vs. f(v)/v.
# the idea is, that a flat tail will appear towards small velocities.
# Next I will plot v/sigma along the x-axes instead of v
# (and with log(v/sigma) as well).
# Plotting v/sigma makes it easier to compare different radial bins,
# because the x-axis will almost always be the same,
# even though they actually have very different sigma.
