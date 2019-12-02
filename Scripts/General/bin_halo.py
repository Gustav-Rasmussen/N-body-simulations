# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import numpy as np
from typing import List

from load_halo import LoadHalo


@dataclass
class BinHalo(LoadHalo):
    """Divide halo into bins."""
    mode: str = 'radial'
    # Reduce number of radial bins to makes them larger / contain more particles.
    # if test or A or B or E:
    #     nr_bins = 102
    # if CS1 or CS2 or CS3:
    #     nr_bins = 53
    nr_bins: int = 300  # 202  # 102
    r_middle: float = 10 ** 1.3
    min_binning_R: float = -1.5  # end-value of first bin
    max_binning_R: float = np.log10(500.0)  # end-value of last bin
    # min_binning_R_unitRmax = .000_01
    # max_binning_R_unitRmax = 1.0
    R: List = field(init=False, repr=False)
    sigma2_arr: List = field(init=False, repr=False)
    sigmarad2_arr: List = field(init=False, repr=False)
    bin_radius_arr: List = field(init=False, repr=False)
    r_arr: List = field(init=False, repr=False)
    Phi_arr: List = field(init=False, repr=False)
    Theta_arr: List = field(init=False, repr=False)
    VR_arr: List = field(init=False, repr=False)
    VTheta_arr: List = field(init=False, repr=False)
    VPhi_arr: List = field(init=False, repr=False)
    VR_i_avg_arr: List = field(init=False, repr=False)
    # xC, yC, zC = 0  # Mock
    # v = np.array([halo.vx, halo.vy, halo.vz])  # velocities
    # r_cut = 10_000  # 5_000
    # R_middle = 10 ** 1.5  # 10 ** 1.3

    # def __post_init__(self):
    #     self.R = self.modulus(self.x, self.y, self.z)
    #     # self.R = np.array([self.x, self.y, self.z])

    def binning_loop(self):
        (sigmatheta2_arr,
         sigmaphi2_arr,
         sigmatan2_arr,
         v2_arr,
         density_arr,
         rho_arr,
         Volume_arr,
         Theta,
         VR,
         VTheta,
         VPhi,
         VR_i_avg_in_bin,
         bin_radius_arr,
         beta_arr,
         gamma_arr,
         kappa_arr) = ([] for i in range(17))

        binning_arr = np.logspace(self.min_binning_R, self.max_binning_R, self.nr_bins)
        for i in range(self.nr_bins - 2):
            min_R_i = binning_arr[i]
            max_R_i = binning_arr[i + 1]
            '''
            posR_par_i = np.where(min_R_i < self.R < max_R_i)
            nr_par_i = len(posR_par_i[0])
            if nr_par_i == 0:
                continue
            x = self.x[posR_par_i]
            y = self.y[posR_par_i]
            z = self.z[posR_par_i]
            vx = self.vx[posR_par_i]
            vy = self.vy[posR_par_i]
            vz = self.vz[posR_par_i]
            v = self.modulus(vx, vy, vz)
            v2_i = v ** 2
            sigma2_arr.append(mean_velocity_slice(nr_par_i, v2_i))  # sigma2 total
            vrad2_i = v_r[posR_par_i] ** 2
            sigmarad2_arr.append(mean_velocity_slice(nr_par_i, vrad2_i))
            Volume_cl = volume_slice(min_R_i, max_R_i)  # volume of cluster
            den_cl = nr_par_i / Volume_cl  # density
            rho_arr.append(den_cl * m)
            r_i = self.modulus(x, y, z)
            Phi_i = phi(x, y)
            Theta_i = theta(z, r_i)
            VR_i = vr_spherical(Theta_i, Phi_i, vx, vy, vz)
            VPhi_i = phi_velocity(Phi_i, vx, vy)
            VR_i_avg.append(mean_velocity_slice(nr_par_i, VR_i))
            VTheta_i = theta_velocity(Theta_i, Phi_i, vx, vy, vz)
            VTheta2_i = VTheta_i ** 2
            sigmatheta2_arr.append(mean_velocity_slice(nr_par_i, VTheta2_i))
            VPhi2_i = VPhi_i ** 2
            sigmaphi2_i = mean_velocity_slice(nr_par_i, VPhi2_i)
            sigmatan2_arr.append(abs(sigmatheta2_i) + abs(sigmaphi2_i))
            '''
            bin_radius_arr.append((max_R_i + min_R_i) / 2)
            # sigmaphi2_arr.append(sigmaphi2_i)
            # density_arr.append(den_cl)
            # Volume_arr.append(Volume_cl)
            # r_arr.append(r_i)
            # Phi_arr.append(Phi_i)
            # Theta.append(Theta_i)
            # VR.append(VR_i)
            # VTheta.append(VTheta_i)
            # VPhi.append(VPhi_i)

        # sigma2_arr = np.array(sigma2_arr)
        # sigmarad2_arr = np.array(sigmarad2_arr)
        bin_radius_arr = np.array(bin_radius_arr)
        # r_arr = np.array(r_arr)
        # Phi_arr = np.array(Phi_arr)
        # Theta_arr = np.array(Theta)
        # VR_arr = np.array(VR)
        # VTheta_arr = np.array(VTheta)
        # VPhi_arr = np.array(VPhi)
        # VR_i_avg_arr = np.array(VR_i_avg)

    def r_bin_automatic(self):
        """Make R_limit_min and R_limit_max selection automatic."""
        r_cut_min, r_cut_max = self.r_middle
        a = 0
        x0 = self.x
        while len(x0) < 10_000 or a == 0:
            r_cut_min -= .000_005
            r_cut_max += .000_005
            a = 1
            good_ids = np.where((self.R < r_cut_max) * (self.R > r_cut_min))
            x0 = self.x[good_ids[0]]
        return r_cut_min, r_cut_max

    def modulus(*args: List) -> List:
        """Modulus of vector of arbitrary size."""
        return sum([i ** 2 for i in args]) ** .5


def main():
    halo = BinHalo('0G00_IC_000.hdf5')
    # print(f"{halo.r_middle}")
    # print(f"{halo.bin_radius_arr}")
    print(f"{halo.x}")
    # print(f"{halo.R}")


if __name__ == '__main__':
    main()
