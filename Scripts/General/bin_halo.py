# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import numpy as np
from typing import List

from load_halo import LoadHalo


@dataclass
class BinHalo(LoadHalo):
    """Divide halo into bins."""
    # TODO:  # mode: str = 'radial'.  # min_binning_R_unitRmax = .000_01  # max_binning_R_unitRmax = 1.0
    nr_bins: int = 102  # 202.  # Reduce number of radial bins to makes them larger / contain more particles.
    r_middle: float = 10 ** 1.3  # 10 ** 1.5
    r_cut_min: float = -1.5  # end-value of first bin
    r_cut_max: float = np.log10(500.0)  # end-value of last bin
    R: np.ndarray = field(init=False, repr=False)
    r_arr: List = field(init=False, repr=False, default_factory=list)
    # sigma2_arr: List = field(init=False, repr=False)
    # sigmarad2_arr: List = field(init=False, repr=False)
    # bin_radius_arr: List = field(init=False, repr=False)
    # Phi_arr: List = field(init=False, repr=False)
    # Theta_arr: List = field(init=False, repr=False)
    # VR_arr: List = field(init=False, repr=False)
    # VTheta_arr: List = field(init=False, repr=False)
    # VPhi_arr: List = field(init=False, repr=False)
    # VR_i_avg_arr: List = field(init=False, repr=False)
    # v = np.array([halo.vx, halo.vy, halo.vz])  # velocities

    def __post_init__(self):
        super().__post_init__()
        self.R = self.get_moduli(self.x, self.y, self.z)
        # self.r_bin_automatic()
        self.binning_loop()

    def get_moduli(self, *args) -> np.ndarray:
        """Moduli of vector of arbitrary size."""
        return np.array(list(map(lambda x: sum(y ** 2 for y in x) ** .5, zip(*args))))

    def binning_loop(self):
        self.r_arr = []
        # sigmatheta2_arr,
        # sigmaphi2_arr,
        # sigmatan2_arr,
        # v2_arr,
        # density_arr,
        # rho_arr,
        # Volume_arr,
        # Theta,
        # VR,
        # VTheta,
        # VPhi,
        # VR_i_avg_in_bin,
        # bin_radius_arr,
        # beta_arr,
        # gamma_arr,
        # kappa_arr
        # ) = ([] for i in range(1))

        bin_arr = np.logspace(self.r_cut_min, self.r_cut_max, self.nr_bins)
        for i in range(self.nr_bins - 2):
            min_r_i = bin_arr[i]
            max_r_i = bin_arr[i + 1]
            pos_r_par_i = np.where((min_r_i < self.R) * (self.R < max_r_i))
            nr_par_i = len(pos_r_par_i[0])
            if nr_par_i == 0:
                continue
            x = self.x[pos_r_par_i]
            y = self.y[pos_r_par_i]
            z = self.z[pos_r_par_i]
            vx = self.vx[pos_r_par_i]
            vy = self.vy[pos_r_par_i]
            vz = self.vz[pos_r_par_i]
            v = self.get_moduli(vx, vy, vz)
            v2_i = v ** 2
            # sigma2_arr.append(mean_velocity_slice(nr_par_i, v2_i))  # sigma2 total
            # vrad2_i = v_r[posR_par_i] ** 2
            # sigmarad2_arr.append(mean_velocity_slice(nr_par_i, vrad2_i))
            # Volume_cl = volume_slice(min_R_i, max_R_i)  # volume of cluster
            # den_cl = nr_par_i / Volume_cl  # density
            # rho_arr.append(den_cl * m)
            r_i = self.get_moduli(x, y, z)
            # Phi_i = phi(x, y)
            # Theta_i = theta(z, r_i)
            # VR_i = vr_spherical(Theta_i, Phi_i, vx, vy, vz)
            # VPhi_i = phi_velocity(Phi_i, vx, vy)
            # VR_i_avg.append(mean_velocity_slice(nr_par_i, VR_i))
            # VTheta_i = theta_velocity(Theta_i, Phi_i, vx, vy, vz)
            # VTheta2_i = VTheta_i ** 2
            # sigmatheta2_arr.append(mean_velocity_slice(nr_par_i, VTheta2_i))
            # VPhi2_i = VPhi_i ** 2
            # sigmaphi2_i = mean_velocity_slice(nr_par_i, VPhi2_i)
            # sigmatan2_arr.append(abs(sigmatheta2_i) + abs(sigmaphi2_i))
            # bin_radius_arr.append((max_R_i + min_R_i) / 2)
            # sigmaphi2_arr.append(sigmaphi2_i)
            # density_arr.append(den_cl)
            # Volume_arr.append(Volume_cl)
            self.r_arr.append(r_i)
            # Phi_arr.append(Phi_i)
            # Theta.append(Theta_i)
            # VR.append(VR_i)
            # VTheta.append(VTheta_i)
            # VPhi.append(VPhi_i)
        # sigma2_arr = np.array(sigma2_arr)
        # sigmarad2_arr = np.array(sigmarad2_arr)
        # bin_radius_arr = np.array(bin_radius_arr)
        self.r_arr = np.array(self.r_arr)
        # Phi_arr = np.array(Phi_arr)
        # Theta_arr = np.array(Theta)
        # VR_arr = np.array(VR)
        # VTheta_arr = np.array(VTheta)
        # VPhi_arr = np.array(VPhi)
        # VR_i_avg_arr = np.array(VR_i_avg)

    def r_bin_automatic(self) -> None:
        """Make R_limit_min and R_limit_max selection automatic."""
        self.r_cut_min, self.r_cut_max = self.r_middle
        a = 0
        x0 = self.x
        while len(x0) < 10_000 or a == 0:
            self.r_cut_min -= .000_005
            self.r_cut_max += .000_005
            a = 1
            good_ids = np.where((self.R < self.r_cut_max) * (self.R > self.r_cut_min))
            x0 = self.x[good_ids[0]]


def main():
    bin_dict = {
                'test': 102,
                'A': 102,
                'B': 102,
                'E': 102,
                'CS1': 53,
                'CS2': 53,
                'CS3': 53
    }

    halo = BinHalo('0G00_IC_000.hdf5')
    print(f"halo.filename: {halo.filename}")
    print(f"halo.x: {halo.x}")
    print(f"halo.R: {halo.R}")


if __name__ == '__main__':
    main()
