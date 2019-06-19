# -*- coding: utf-8 -*-

import numpy as np
# import scipy as sp
import radius_and_velocity_funcs as ravf
import matplotlib.pyplot as plt

# switches -------------------------------------------------------------
vspherical = 0
vbin = 0
nr_bins_v = 100

# radial and tangential velocities
if vspherical:
    ravf.spherical_coords_and_velocities()

if vbin:
    for i in range(nr_bins_v - 2):  # loop over 0-998
        min_v_bin_i = v_binning_arr[i]  # start of bin
        max_v_bin_i = v_binning_arr[i + 1]  # end of bin
        # position of particles inside a radial bin
        posv_par_in_bin_i = np.where(
            (v_hob_par > min_v_bin_i) * (v_hob_par < max_v_bin_i))
        # number of particles inside a radial bin
        nr_par_in_bin_i = len(posv_par_in_bin_i)
        if nr_par_in_bin_i == 0:
            continue

        v_in_bin_i = v[posv_par_in_bin_i]
        V_R_in_bin_i = VR[posv_par_in_bin_i]
        V_T_in_bin_i = VT[posv_par_in_bin_i]

        v_arr.append(v_in_bin_i)
        v_r_arr.append(v_r_in_bin_i)
        v_t_arr.append(v_t_in_bin_i)
        nr_par_in_bin.append(nr_par_in_bin_i)

    f = plt.figure()  # plot structure over velocity bins.
    plt.subplot(121)
    plt.xlabel(r"$v, v_r$ and $v_t$")
    plt.ylabel("Number of particles")
    plt.title(r"VDF (Hernquist structure, $10^6$ particles)")
    plt.hist(v_arr[15], bins=100, histtype="step", color="r",
             range=(v_limit_min, v_limit_max), label=r"$v$", lw=2)
    plt.hist(v_r_arr[15], bins=100, histtype="step", color="b",
             range=(v_limit_min, v_limit_max), label=r"$v_r$", lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=1, handlelength=2.5)
    plt.show()
    plt.hist(v_r, bins=100, histtype="step", color="g",
             range=(v_limit_min, v_limit_max), label=r"$v_r$", lw=2)
    plt.hist(v_t, bins=100, histtype="step", color="k",
             range=(-4, 4), label=r"$v_t$", lw=2)

    plt.subplot(122)
    plt.xlabel(r"$\log v$, $\log v_r$ and $\log v_t$")
    plt.hist(np.log10(np.absolute(v_arr)), bins=100, histtype="step",
             color="r", range=(-5, 1), label=r"$\log v$", lw=2)
    plt.hist(np.log10(np.absolute(v_r)), bins=100, histtype="step", color="g",
             range=(-5, 1), label=r"$\log v_r$", lw=2)
    plt.hist(np.log10(np.absolute(v_t)), bins=100, histtype="step", color="k",
             range=(-5, 1), label=r"$\log v_t$", lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)

    f = plt.figure()
    plt.xlabel(r"$v_r$ and $v_t$")
    plt.ylabel("Number of particles")
    plt.title("velocity distributions")
    plt.hist(v_r_arr[5], bins=30, histtype="step", color="r",
             range=(-4, 1), label=r"$v_r$ (bin 5)", normed=True, lw=2)
    plt.hist(v_r_arr[8], bins=30, histtype="step", color="m",
             range=(-4, 1), label=r"$v_r$ (bin 8)", normed=True, lw=2)
    plt.hist(v_r_arr[10], bins=300, histtype="step", color="k",
             range=(-1, 1), label=r"$v_r$ (bin 10)", lw=2)
    plt.hist(.5 * v_t_arr[5], bins=30, histtype="step", color="g",
             range=(-4, 1), label=r"$v_t$ (bin 5)", normed=True, lw=2)
    plt.hist(.5 * v_t_arr[8], bins=30, histtype="step", color="b",
             range=(-4, 1), label=r"$v_t$ (bin 8)", normed=True, lw=2)
    plt.hist(v_t_arr[10], bins=300, histtype="step", color="c",
             range=(-1, 1), label=r"$v_t$ (bin 10)", lw=2)
    plt.hist(.25 * v_t_arr[10], bins=300, histtype="step", color="r",
             range=(-2, 1), label=r"$\frac{1}{4}\cdot v_t$ (bin 10)", lw=2)
    plt.hist(v_t_arr[10] * v_t_arr[10], bins=300, histtype="step", color="g",
             range=(-2, 1), label=r"$v_t\cdot v_t$ (bin 10)", lw=2)
    plt.hist(2 * v_t_arr[10], bins=300, histtype="step", color="b",
             range=(-2, 1), label=r"$2 \cdot v_t$ (bin 10)", lw=2)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=2,
               frameon=True, loc=2, handlelength=2.5)
