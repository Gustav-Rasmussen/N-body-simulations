# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import numpy as np

from load_halo import LoadHalo


@dataclass
class BinHalo(LoadHalo):
    """Divide halo into bins."""
    min_binning_R: float = -1.5  # end-value of first bin
    max_binning_R: float = np.log10(500.0)  # end-value of last bin
    nr_bins: int = 300  # number of bins
    # min_binning_R_unitRmax = .000_01
    # max_binning_R_unitRmax = 1.0

    (sigma2_arr, sigmarad2_arr, sigmatheta2_arr, sigmaphi2_arr, sigmatan2_arr, v2_arr, gamma_arr, kappa_arr,
     beta_arr, density_arr, rho_arr, Volume_arr, r, Phi, Theta, VR,
     VTheta, VPhi, VR_i_avg_in_bin, bin_radius_arr) = ([] for i in range(20))

    binning_arr_lin_log10 = np.logspace(min_binning_R, max_binning_R, nr_bins)

    for i in range(nr_bins - 2):
        min_R_i = binning_arr_lin_log10[i]
        max_R_i = binning_arr_lin_log10[i + 1]
        posR_par_i = np.where((R > min_R_i) & (R < max_R_i))
        nr_par_i = len(posR_par_i[0])
        if nr_par_i == 0:
            continue

        x = x[posR_par_i]
        y = y[posR_par_i]
        z = z[posR_par_i]
        vx = vx[posR_par_i]
        vy = vy[posR_par_i]
        vz = vz[posR_par_i]

        v = ravf.modulus(vx, vy, vz)
        v2_i = v ** 2
        sigma2_i = mean_velocity_slice(nr_par_i, v2_i)  # sigma2 total
        vrad2_i = v_r[posR_par_i] ** 2
        sigmarad2_i = mean_velocity_slice(nr_par_i, vrad2_i)
        Volume_cl = volume_slice(min_R_i, max_R_i)  # volume of cluster
        den_cl = nr_par_i / Volume_cl  # density
        rho = den_cl * m
        r_i = ravf.modulus(x, y, z)
        Phi_i = phi(x, y)
        Theta_i = theta(z, r_i)
        VR_i = vr_spherical(Theta_i, Phi_i, vx, vy, vz)
        VTheta_i = theta_velocity(Theta_i, Phi_i, vx, vy, vz)
        VPhi_i = phi_velocity(Phi_i, vx, vy)
        VR_i_avg_i = mean_velocity_slice(nr_par_i, VR_i)
        VTheta2_i = VTheta_i ** 2
        sigmatheta2_i = mean_velocity_slice(nr_par_i, VTheta2_i)
        VPhi2_i = VPhi_i ** 2
        sigmaphi2_i = mean_velocity_slice(nr_par_i, VPhi2_i)
        sigmatan = (sigmatheta2_i + sigmaphi2_i) ** .5
        sigmatan2 = sigmatan ** 2

        # save arrays
        sigma2_arr.append(sigma2_i)
        bin_radius_arr.append((max_R_i + min_R_i) / 2)
        sigmarad2_arr.append(sigmarad2_i)
        sigmatheta2_arr.append(sigmatheta2_i)
        sigmaphi2_arr.append(sigmaphi2_i)
        sigmatan2_arr.append(sigmatan2)
        density_arr.append(den_cl)
        rho_arr.append(rho)
        Volume_arr.append(Volume_cl)
        r.append(r_i)
        Phi.append(Phi_i)
        Theta.append(Theta_i)
        VR.append(VR_i)
        VR_i_avg.append(VR_i_avg_i)
        VTheta.append(VTheta_i)
        VPhi.append(VPhi_i)

    # Change the necessary lists into arrays
    sigma2_arr = np.array(sigma2_arr)
    sigmarad2_arr = np.array(sigmarad2_arr)
    bin_radius_arr = np.array(bin_radius_arr)
    r_arr = np.array(r)
    Phi_arr = np.array(Phi)
    Theta_arr = np.array(Theta)
    VR_arr = np.array(VR)
    VTheta_arr = np.array(VTheta)
    VPhi_arr = np.array(VPhi)
    VR_i_avg_arr = np.array(VR_i_avg)
    return (sigma2_arr, sigmarad2_arr, bin_radius_arr, r_arr, Phi_arr,
           Theta_arr, VR_arr, VTheta_arr, VPhi_arr, VR_i_avg_arr)

    @staticmethod
    def modulus(*args):
        """Modulus of vector of arbitrary size."""
        return sum([i ** 2 for i in args]) ** .5

    def r_bin_automatic(self):
        """Make R_limit_min and R_limit_max selection automatic."""
        r_middle = 10 ** 1.3
        r_cut_min, r_cut_max = r_middle
        a = 0
        x0 = self.x
        while len(x0) < 10_000 or a == 0:
            r_cut_min -= .000_005
            r_cut_max += .000_005
            a = 1
            good_ids = np.where((R < r_cut_max) * (R > r_cut_min))
            x0 = halo.x[good_ids[0]]
        return r_cut_min, r_cut_max


halo = BinHalo('0G00_IC_000.hdf5')

R = halo.modulus(halo.x, halo.y, halo.z)
# R = halo.modulus(x - xC, y - yC, z - zC)
# R = np.array([xcl, ycl, zcl])

v = np.array([halo.vx, halo.vy, halo.vz])  # velocities

bins_202 = 0
bins_102 = 0

# Reduce number of radial bins in analysis code.
# This makes them larger and contain more particles.
larger_fewer_bins = 1
largest_r_cut = 1  # Analyze larger volume of structure, set R_limit to 10_000.
large_r_cut = 0  # Analyze large volume of structure, sets R_limit to 5_000.

IC_R_middle = 0
keep_IC_R_middle = 0
new_R_middle = 0
large_R_middle = 0
R_bin_automatic = 0

if large_R_middle:
    R_middle = 10 ** 1.5  # 10 ** 1.3

# if test or A or B or E:
#     nr_bins = 102
# if CS1 or CS2 or CS3:
#     nr_bins = 53
