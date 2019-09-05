
def bin_halo_radially():
    (sigma2_arr, sigmarad2_arr, sigmatheta2_arr, sigmaphi2_arr, sigmatan2_arr, v2_arr, gamma_arr, kappa_arr,
     beta_arr, density_arr, rho_arr, Volume_arr, r, Phi, Theta, VR,
     VTheta, VPhi, VR_i_avg_in_bin, bin_radius_arr) = ([] for i in range(20))

    binning_arr_lin_log10 = np.logspace(min_binning_R, max_binning_R, nr_bins) 

    for i in range(nr_bins - 2):      
        min_R_i = binning_arr_lin_log10[i]   
        max_R_i = binning_arr_lin_log10[i + 1]
        posR_par_i = np.where((R_hob_par > min_R_i) & (R_hob_par < max_R_i))
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

    # Change the nesessary lists into arrays
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
    return sigma2_arr, sigmarad2_arr, bin_radius_arr, r_arr, Phi_arr, Theta_arr, VR_arr, VTheta_arr, VPhi_arr, VR_i_avg_arr
