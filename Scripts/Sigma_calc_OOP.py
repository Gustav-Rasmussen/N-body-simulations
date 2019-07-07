# -*- coding: utf-8 -*-

import numpy as np
import pylab
import scipy as sp
from dataclasses import dataclass

simulations = ['A/', 'B/', 'Soft_B/', 'CS4/', 'CS5/', 'CS6/', 'DS1/',
               'Soft_D2/', 'E/']

A = B = 0

# text_files_path = textFilesPath / simulations[0]

# Number of bins
bins_list = [202, 102, 52, 22]
bins = bins_list[0]
R_limit = 100
R_hob_par = R[GoodIDs]
G = 1.  # Gravitational constant

Gammas = [-1.5, -2.0, -2.5, -3.0]
Gamma = Gammas[0]
if Gamma == -2.0:
    r_2 = R_middle


@dataclass
class BinnedHalo():
    '''Divide structure into radial bins.'''
    Bin_type: str = "Radial"
    radii = bin_radius_arr
    density = density_arr
    len_obj = sigma2_arr
    len_obj_1 = density
    sigma_r2 = sigmarad2_arr
    Min: float
    Max: float
    bins: int = 100
    mode : str = "lin"
    sigmatheta2
    sigmarad2
        
    def binning(self):
        '''Create linear or logarithmic bins.'''
        if self.mode == "lin":
            return np.linspace(self.Min, self.Max, self.bins)
        elif self.mode == "log":
            return np.logspace(self.Min, self.Max, self.bins)
    
    def beta(self):
        '''Calculate beta.'''
        return 1. - sigmatheta2 / sigmarad2
    
    def gamma(self):
        '''Calculate gamma.'''
        for i in range(len(len_obj_1)):
            if i in (0, len(len_obj) - 1):
                gamma_arr.append(np.nan)
                continue
            dlogr = np.log10(radii[i + 1]) - np.log10(radii[i - 1])
            dlogrho = np.log10(density[i + 1]) - np.log10(density[i - 1])
            gamma_arr.append(dlogrho / dlogr)
        return np.array(gamma_arr)
    
    def kappa(self):
        '''Calculate kappa.'''
        for i in range(len(len_obj)):
            if i in (0, len(len_obj) - 1):
                kappa_arr.append(np.nan)
                continue
            dlogr = np.log10(radii[i + 1]) - np.log10(radii[i - 1])
            dlogsigmarad2 = np.log10(sigma_r2[i + 1]) -\
                            np.log10(sigma_r2[i - 1])
            kappa_arr.append(dlogsigmarad2 / dlogr)
        return np.array(kappa_arr)
    
    def add_params(self, param=None):
        if param is None:
            param = []
        return param.append((beta(), gamma(), kappa()))


# Create instance of BinnedHalo:
halo = BinnedHalo(Min=-1.5, Max=np.log10(R_limit), bins=bins_list[0],
                  mode="lin")

# File switches -------------------------------------------------------------
save_lnr_beta_gamma_kappa_VR_r_sigma_r_rr2_rho = 0
save_particle_tracking_ASCII = 0
save_combine_ASCII = 0
save_sigma = 0

# Functions -------------------------------------------------------------------


def modulus(x, y, z):
    '''Modulus of vector.'''
    return (x ** 2 + y ** 2 + z ** 2) ** .5


def radial_velocities(x, y, z, vx, vy, vz):
    '''Doc-string here.'''
    return (vx * x + vy * y + vz * z) / modulus(x, y, z)


def particle_positions():
    '''Position of particles inside halo.'''
    return np.where(R_hob_par < r_2)


def particle_number():
    '''Number of particles inside halo.'''
    return len(particle_positions()[0])


def particle_mass(m):
    '''Combined mass of particles inside halo.'''
    return particle_number() * m


def circular_velocity():
    '''Circular velocity of halo.'''
    return (G * particle_mass() / r_2) ** .5


def chi_2(param=gamma_arr):
    '''Doc-string here.'''
    Chi2 = 0
    i = 0
    while (i < len(param)):
        if np.isnan(param[i]):
            print('nan at index: ', i)
        else:
            Chi2 += ((param[i] - y_plot[i]) ** 2) / (param[i] * .2) ** 2
        i += 1
    Chi2 = (1.0 / (len(param) - 1)) * Chi2
    return Chi2


# Set values and instantiate functions ----------------------------------------

posR_par_inside_halo = particle_positions()
nr_par_inside_halo = particle_number()
M_2 = particle_mass()
v_circ_2 = circular_velocity()
r = modulus(x, y, z)
v = modulus(vx, vy, vz)
r_r2 = r / r_2

snapshot_num = ['IC', '10_005', '48_009', '198_093']

file_str = "_particle_tracking_"

out_names = [f'A{file_str}IC_ASCII', f'A{file_str}5_005_ASCII',
             f'A{file_str}10_005_ASCII', f'A{file_str}40_005_ASCII',
             f'A{file_str}48_009_ASCII', f'B{file_str}IC_ASCII',
             f'B{file_str}5_005_ASCII', f'B{file_str}10_005_ASCII',
             f'B{file_str}198_000_ASCII', f'B{file_str}198_093_ASCII',
             f'B{file_str}199_093_ASCII']

# Note ------------------------------------------------------------------------
# Calculates the median of vx, vy, vz for all particles
# which are inside the cluster.
# Thereafter the cluster is centered in velocity-space.
# Using the median is better than using the mean,
# because the median is insensitive to outliers.
# vx = vx[GoodIDs] - np.median(vx)
# vy = vy[GoodIDs] - np.median(vy)
# vz = vz[GoodIDs] - np.median(vz)

(sigma2_lst, sigmarad2_lst, sigmatheta2_lst, sigmaphi2_lst,
 sigmatan2_lst, v2_lst, gamma_lst, kappa_lst, beta_lst, density_lst,
 rho_lst, Volume_lst, r_lst, Phi_lst, Theta_lst, VR_lst, VTheta_lst, VPhi_lst,
 VR_i_avg_bin_lst, bin_radius_lst) = ([] for i in range(20))

v_r = radial_velocities()


def particle_positions_slice(bin_start, bin_end):
    '''Position of particles inside a radial bin.'''
    return np.where((R_hob_par > bin_start) & (R_hob_par < bin_end))


def particle_number_slice():
    '''Number of particles inside a radial bin.'''
    return len(particle_positions_slice()[0])


def sigma_squared_slice(nr_par_bin, v_bin):
    '''Velocity dispersion squared, for particles inside a radial bin.'''
    return (1. / (nr_par_bin + 1.)) * np.sum(v_bin ** 2)


def radius_slice(bin_start, bin_end):
    '''Doc-string here.'''
    return (bin_start + bin_end) / 2


def volume_slice(bin_start, bin_end):
    '''Calculate volume of radial cluster-slice.'''
    return (4. / 3.) * np.pi * (bin_end ** 3 - bin_start ** 3)


def density_slice(m, nr_par_bin, Volume_bin):
    '''Doc-string here.'''
    return (nr_par_bin * m) / Volume_bin


def sigmarad2_slice(nr_par_bin, vrad2_bin):
    '''Doc-string here.'''
    return (1. / (nr_par_bin + 1.)) * np.sum(vrad2_bin)


def phi(x, y):
    '''Doc-string here.'''
    return sp.arctan2(y, x)


def theta(z, r):
    '''Doc-string here.'''
    return sp.arccos(z / r)


def radial_velocity(theta, phi, vx, vy, vz):
    '''Doc-string here.'''
    return (sp.sin(theta) * sp.cos(phi) * vx
            + sp.sin(theta) * sp.sin(phi) * vy + sp.cos(theta) * vz)


def theta_velocity(theta, phi, vx, vy, vz):
    '''Doc-string here.'''
    return (sp.cos(theta) * sp.cos(phi) * vx + sp.cos(theta)
            * sp.sin(phi) * vy - sp.sin(theta) * vz)


def phi_velocity(phi, vx, vy):
    '''Doc-string here.'''
    return -sp.sin(phi) * vx + sp.cos(phi) * vy


def mean_velocity_slice(nr_par_bin, v):
    '''Doc-string here.'''
    return (1. / (nr_par_bin + 1.)) * np.sum(v)


for i in range(bins - 2):
    min_R_bin = binning_arr_lin_log10[i]  # start of bin
    max_R_bin = binning_arr_lin_log10[i + 1]  # end of bin

    posR_par_bin = particle_positions_slice(min_R_bin, max_R_bin)
    nr_par_bin = particle_number_slice()
    if nr_par_bin == 0:
        continue

    v_bin = modulus(vx[posR_par_bin], vy[posR_par_bin], vz[posR_par_bin])
    sigma2_bin = sigma_squared_slice(nr_par_bin, v_bin)
    sigma2_lst.append(sigma2_bin)
    bin_radius = radius_slice(min_R_bin, max_R_bin)
    bin_radius_lst.append(bin_radius)
    vrad2_bin = v_r[posR_par_bin] ** 2
    sigmarad2_bin = sigmarad2_slice(nr_par_bin, vrad2_bin)
    sigmarad2_lst.append(sigmarad2_bin)

    Volume_bin = volume_slice(min_R_bin, max_R_bin)
    rho = density_slice(nr_par_bin, Volume_bin)
    r_bin = radii(x[posR_par_bin], y[posR_par_bin], z[posR_par_bin])
    Phi_i = phi(x[posR_par_bin], y[posR_par_bin])
    Theta_i = theta(z[posR_par_bin], r_bin)
    VR_i = radial_velocity(Theta_i, Phi_i, vx[posR_par_bin], vy[posR_par_bin],
                           vz[posR_par_bin])
    VTheta_i = theta_velocity(Theta_i, Phi_i, vx[posR_par_bin],
                              vy[posR_par_bin], vz[posR_par_bin])
    VPhi_i = phi_velocity(Phi_i, vx[posR_par_bin], vy[posR_par_bin])
    VR_i_avg_bin = mean_velocity_slice(nr_par_bin, VR_i)
    VTheta2_bin = VTheta_i ** 2
    sigmatheta2_bin = mean_velocity_slice(nr_par_bin, VTheta2_bin)
    sigmatheta2_lst.append(sigmatheta2_bin)
    VPhi2_bin = VPhi_i ** 2
    sigmaphi2_bin = mean_velocity_slice(nr_par_bin, VPhi2_bin)
    sigmaphi2_lst.append(sigmaphi2_bin)
    sigmatan = (sigmatheta2_bin + sigmaphi2_bin) ** .5
    sigmatan2 = sigmatan ** 2

    sigmatan2_lst.append(sigmatan2)
    density_lst.append(den_cl)
    rho_lst.append(rho)
    Volume_lst.append(Volume_cl)
    r_lst.append(r_i)
    Phi_lst.append(Phi_i)
    Theta_lst.append(Theta_i)
    VR_lst.append(VR_i)
    VR_i_avg_bin_lst.append(VR_i_avg_bin)
    VTheta_lst.append(VTheta_i)
    VPhi_lst.append(VPhi_i)

# Change lists into arrays
sigma2_arr = np.array(sigma2_lst)
sigmarad2_arr = np.array(sigmarad2_lst)
bin_radius_arr = np.array(bin_radius_lst)
r_arr = np.array(r_lst)
Phi_arr = np.array(Phi_lst)
Theta_arr = np.array(Theta_lst)
VR_arr = np.array(VR_lst)
VTheta_arr = np.array(VTheta_lst)
VPhi_arr = np.array(VPhi_lst)
VR_i_avg_bin_arr = np.array(VR_i_avg_bin_lst)

# Save (logr, beta, gamma, kappa etc.) as text file,
# so they can be plotted in Sigma_plot.py
if save_lnr_beta_gamma_kappa_VR_r_sigma_r_rr2_rho:
    logr_arr = np.array(np.log10(bin_radius_arr))
    beta_arr = np.array(beta_arr)
    gamma_arr = np.array(gamma_arr)
    kappa_arr = np.array(kappa_arr)
    r_arr = 10 ** (logr_arr)
    sigmarad2_arr = np.array(sigmarad2_arr)
    rho_arr = np.array(rho_arr)
    GoodIDs = np.where(gamma_arr == gamma_arr)
    logr_arr = logr_arr[GoodIDs]
    gamma_arr = gamma_arr[GoodIDs]
    beta_arr = beta_arr[GoodIDs]
    kappa_arr = kappa_arr[GoodIDs]
    r_arr = r_arr[GoodIDs]
    sigmarad2_arr = sigmarad2_arr[GoodIDs]
    VR_i_avg_in_bin_arr = VR_i_avg_in_bin_arr[GoodIDs]

    if Gamma == -2.0:
        r_r2_arr = r_arr / r_2
        print('r_r2_arr = ', r_r2_arr)
        rho_arr = rho_arr[GoodIDs]
        x = np.array((logr_arr, beta_arr, gamma_arr, kappa_arr,
                      VR_i_avg_in_bin_arr, r_arr, sigmarad2_arr,
                      r_r2_arr, rho_arr))
        x = x.transpose()
        out_name = text_files_path + F + '.txt'
        np.savetxt(out_name, x, delimiter=' ',
                   header='\t logr \t beta \t gamma \t kappa \t VR_average \t\
                          r \t sigmarad2 \t r_r2 \t rho')
    else:
        x = np.array((logr_arr, beta_arr, gamma_arr, kappa_arr,
                      VR_i_avg_in_bin_arr, r_arr, sigmarad2_arr))
        x = x.transpose()
        out_name = text_files_path + F + '.txt'
        np.savetxt(out_name, x, delimiter=' ',
                   header='\t logr \t beta \t gamma \t kappa \t VR_average \t\
                          r \t sigmarad2')

if save_particle_tracking_ASCII:
    TimeMax = {'A, B IC': 100,
               'A, B 5_005': 600,
               'A, B 10_005': 1100,
               'A, 40_005': 4100,
               'A, 48_009': 4970,
               'B, 198_000': 19800,
               'B, 198_093': 22100,
               'B, 199_093': 24400}

    xx = [['TimeMax',
           'x[100000]', 'y[100000]', 'z[100000]', 'R_xyz[100000]',
           'x[200000]', 'y[200000]', 'z[200000]', 'R_xyz[200000]',
           'x[300000]', 'y[300000]', 'z[300000]', 'R_xyz[300000]',
           'x[400000]', 'y[400000]', 'z[400000]', 'R_xyz[400000]']]

    for value in TimeMax.values():
          xx.append([value,
                     x[100000], y[100000], z[100000], R_xyz[100000],
                     x[200000], y[200000], z[200000], R_xyz[200000],
                     x[300000], y[300000], z[300000], R_xyz[300000],
                     x[400000], y[400000], z[400000], R_xyz[400000]])

    out_name = text_files_path + out_names[0] + '.txt'

    with open(out_name, 'w') as f:
        for i in range(len(xx)):
            if i == 0:
                f.write('# TimeMax \t x[100] \t y[100] \t z[100] \t\
                         R_xyz[100] \t x[200] \t y[200] \t z[200] \t\
                         R_xyz[200] \n')

                f.write(f'{xx[i][0]} \t {xx[i][1]} \t {xx[i][2]} \t {xx[i][3]}\
                        \t {xx[i][4]} \t {xx[i][5]} \t {xx[i][6]} \t\
                        {xx[i][7]} \t {xx[i][8]} \t {xx[i][9]} \t {xx[i][10]}\
                        \t {xx[i][11]} \t {xx[i][12]} \t {xx[i][13]} \t\
                        {xx[i][14]} \t {xx[i][15]} \t {xx[i][16]} \n')

            else:
                f.write(f'{xx[i][0]} \t {xx[i][1]} \t {xx[i][2]} \t {xx[i][3]}\
                        \t {xx[i][4]} \t {xx[i][5]} \t {xx[i][6]} \t\
                        {xx[i][7]} \t {xx[i][8]} \t {xx[i][9]} \t {xx[i][10]}\
                        \t {xx[i][11]} \t {xx[i][12]} \t {xx[i][13]} \t\
                        {xx[i][14]} \t {xx[i][15]} \t {xx[i][16]} \n')

if save_combine_ASCII:
    if A:
        lf = [f"{text_files_path}{out_names[i]}.txt" for i in range(5)]
        dl_lf = [pylab.loadtxt(filename) for filename in lf]
        out_name = text_files_path + 'A_particle_tracking.txt'
        with open(out_name, 'w') as f:
            for i in range(len(dl_lf)):
                if i == 0:
                    f.write('# TimeMax \t x[100000] \t y[100000] \t z[100000]\
                            \t R_xyz[100000] \t x[200000] \t y[200000] \t\
                            z[200000] \t R_xyz[200000] \t x[300000] \t\
                            y[300000] \t z[300000] \t R_xyz[300000] \t\
                            x[400000] \t y[400000] \t z[400000] \t\
                            R_xyz[400000] \n')

                    f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f\
                            \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t\
                            %f \n' % (dl_lf[i][0], dl_lf[i][1], dl_lf[i][2],
                                      dl_lf[i][3], dl_lf[i][4], dl_lf[i][5],
                                      dl_lf[i][6], dl_lf[i][7], dl_lf[i][8],
                                      dl_lf[i][9], dl_lf[i][10], dl_lf[i][11],
                                      dl_lf[i][12], dl_lf[i][13], dl_lf[i][14],
                                      dl_lf[i][15], dl_lf[i][16]))

                else:
                    f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f\
                            \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t\
                            %f \n' % (dl_lf[i][0], dl_lf[i][1], dl_lf[i][2],
                                      dl_lf[i][3], dl_lf[i][4], dl_lf[i][5],
                                      dl_lf[i][6], dl_lf[i][7], dl_lf[i][8],
                                      dl_lf[i][9], dl_lf[i][10], dl_lf[i][11],
                                      dl_lf[i][12], dl_lf[i][13], dl_lf[i][14],
                                      dl_lf[i][15], dl_lf[i][16]))

    elif B:
        lf = [f"{text_files_path}{out_names[i]}.txt" for i in range(5, 11)]
        dl_lf = [pylab.loadtxt(filename) for filename in lf]
        out_name = text_files_path + 'B_particle_tracking.txt'
        with open(out_name, 'w') as f:
            for i in range(len(dl_lf)):
                if i == 0:
                    f.write('# TimeMax \t x[100000] \t y[100000] \t z[100000]\
                            \t R_xyz[100000] \t x[200000] \t y[200000] \t\
                            z[200000] \t R_xyz[200000] \t x[300000] \t\
                            y[300000] \t z[300000] \t R_xyz[300000] \t\
                            x[400000] \t y[400000] \t z[400000] \t\
                            R_xyz[400000] \n')

                    f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f\
                            \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t\
                            %f \n' % (dl_lf[i][0], dl_lf[i][1], dl_lf[i][2],
                                      dl_lf[i][3], dl_lf[i][4], dl_lf[i][5],
                                      dl_lf[i][6], dl_lf[i][7], dl_lf[i][8],
                                      dl_lf[i][9], dl_lf[i][10], dl_lf[i][11],
                                      dl_lf[i][12], dl_lf[i][13], dl_lf[i][14],
                                      dl_lf[i][15], dl_lf[i][16]))
                else:
                    f.write('%i \t \t %f \t %f \t %f \t %f \t %f \t %f \t %f\
                            \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t\
                            %f \n' % (dl_lf[i][0], dl_lf[i][1], dl_lf[i][2],
                                      dl_lf[i][3], dl_lf[i][4], dl_lf[i][5],
                                      dl_lf[i][6], dl_lf[i][7], dl_lf[i][8],
                                      dl_lf[i][9], dl_lf[i][10], dl_lf[i][11],
                                      dl_lf[i][12], dl_lf[i][13], dl_lf[i][14],
                                      dl_lf[i][15], dl_lf[i][16]))

if save_sigma:
    x = np.array((sigma2_arr, sigmarad2_arr, sigmatheta2_arr, sigmaphi2_arr))
    x = x.transpose()
    np.savetxt(Filename.strip('.hdf5') + '_sigma.txt', x, delimiter=' ',
               header='sigma2_arr \t sigmarad2_arr \t sigmatheta2_arr\
                      \t sigmaphi2_arr')
