
def bin_halo_radially():
    '''Divide halo into radial bins.'''
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
    return (sigma2_arr, sigmarad2_arr, bin_radius_arr, r_arr, Phi_arr,
           Theta_arr, VR_arr, VTheta_arr, VPhi_arr, VR_i_avg_arr)


def bin_halo_by_mass():
    '''Divide structure into mass-bins. Favoured over radial bins,
    as outer region of structure has less particles.'''
    N_total = x.shape[0]
    N_particles_per_bin = 500
    N_bins = N_total / N_particles_per_bin

    (bin_radius_arr, x_GoodIDs_arr, y_GoodIDs_arr, z_GoodIDs_arr,
     vx_GoodIDs_rand_arr, vy_GoodIDs_rand_arr, vz_GoodIDs_rand_arr,
     M_GoodIDs_arr, vx_GoodIDs_rand_norm_arr, vy_GoodIDs_rand_norm_arr,
     vz_GoodIDs_rand_norm_arr, vx_final_arr, vy_final_arr, vz_final_arr,
     K_init_mean_in_bin_arr, K_rand_mean_in_bin_arr,
     K_rand_norm_mean_in_bin_arr, K_final_mean_in_bin_arr,
     V_mean_in_bin_arr, Ratio_init_mean_in_bin_arr,
     Ratio_rand_mean_in_bin_arr,
     Ratio_norm_mean_in_bin_arr) = ([] for i in range(22))

    for i in range(N_bins):
        (vx_unbound_norm_i_arr, vy_unbound_norm_i_arr, vz_unbound_norm_i_arr,
         vx_unbound_norm_i_rand_arr, vy_unbound_norm_i_rand_arr, vz_unbound_norm_i_rand_arr,
         vx_unbound_norm_i_zero_arr, vy_unbound_norm_i_zero_arr,
         vz_unbound_norm_i_zero_arr) = ([] for i in range(9))

        GoodIDs = np.arange(i * N_particles_per_bin, (i + 1) * N_particles_per_bin)
        x_GoodIDs = x_IDs[GoodIDs]
        y_GoodIDs = y_IDs[GoodIDs]
        z_GoodIDs = z_IDs[GoodIDs]
        vx_GoodIDs = vx_IDs[GoodIDs]
        vy_GoodIDs = vy_IDs[GoodIDs]
        vz_GoodIDs = vz_IDs[GoodIDs]
        M_GoodIDs = M_IDs[GoodIDs]
        V_GoodIDs = V_IDs[GoodIDs]  # Shape: 500
        R_min = R_IDs[GoodIDs][0]
        R_max = R_IDs[GoodIDs][-1]
        # 1.st randomization
        a = np.random.uniform(low=0.5, high=1.5, size=(N_particles_per_bin,))  # Shape: 500
        b = np.random.uniform(low=0.5, high=1.5, size=(N_particles_per_bin,))  # Shape: 500
        c = np.random.uniform(low=0.5, high=1.5, size=(N_particles_per_bin,))  # Shape: 500
        vx_GoodIDs_rand = a * vx_GoodIDs  # Shape: 500
        vy_GoodIDs_rand = b * vy_GoodIDs  # Shape: 500
        vz_GoodIDs_rand = c * vz_GoodIDs  # Shape: 500
        v_GoodIDs_rand = ravf.modulus(vx_GoodIDs_rand, vy_GoodIDs_rand, vz_GoodIDs_rand)  # Shape: 500
        v_GoodIDs = ravf.modulus(vx_GoodIDs, vy_GoodIDs, vz_GoodIDs)  # Shape: 500
        K_init = E_kin(v_GoodIDs)  # Kinetic energy before 1.st randomization
        K_rand = E_kin(v_GoodIDs_rand)  # -||- after -||-
        K_init_mean = np.mean(K_init)
        K_rand_mean = np.mean(K_rand)
        print(f'{K_init_mean= }\n{K_rand_mean= }')
        K_init_mean_in_bin_arr.append(K_init_mean)
        K_rand_mean_in_bin_arr.append(K_rand_mean)
        E_tot_rand = V_GoodIDs + K_rand
        UnboundIDs_rand = np.where(E_tot_rand > 0.)  # Unbound particles. Tuple with 24 entries. (IDs of 19 unbound particles)
        BoundIDs_rand = np.where(E_tot_rand <= 0.)  # Bound particles.
        # Split particles into bound and unbound
        vx_unbound = vx_GoodIDs_rand[UnboundIDs_rand]
        vy_unbound = vy_GoodIDs_rand[UnboundIDs_rand]
        vz_unbound = vz_GoodIDs_rand[UnboundIDs_rand]
        # print('vx_unbound.shape: ', vx_unbound.shape)  # 23
        vx_bound = vx_GoodIDs_rand[BoundIDs_rand]
        vy_bound = vy_GoodIDs_rand[BoundIDs_rand]
        vz_bound = vz_GoodIDs_rand[BoundIDs_rand]
        Ratio_init = np.sqrt(np.abs(V_GoodIDs) / K_init)
        Ratio_rand = np.sqrt(np.abs(V_GoodIDs) / K_rand)  # Shape: 500
        # Ratio = Ratio[GoodIDs]
        Ratio_rand_unbound = Ratio_rand[UnboundIDs_rand]
        Ratio_init_mean = np.mean(Ratio_init)
        Ratio_rand_mean = np.mean(Ratio_rand)
        Ratio_init_mean_in_bin_arr.append(Ratio_init_mean)
        Ratio_rand_mean_in_bin_arr.append(Ratio_rand_mean)
        for i in range(len(UnboundIDs_rand[0])):
            vx_unbound_norm_i = vx_unbound[i] * np.random.uniform(low=.8, high=1.) * Ratio_rand_unbound[i]  # Multiplies velocities with random number between 0.8 and 1 (1 not included)
            vy_unbound_norm_i = vy_unbound[i] * np.random.uniform(low=.8, high=1.) * Ratio_rand_unbound[i]
            vz_unbound_norm_i = vz_unbound[i] * np.random.uniform(low=.8, high=1.) * Ratio_rand_unbound[i]
            vx_unbound_norm_i_arr.append(vx_unbound_norm_i)
            vy_unbound_norm_i_arr.append(vy_unbound_norm_i)
            vz_unbound_norm_i_arr.append(vz_unbound_norm_i)
        vx_unbound_norm = np.asarray(vx_unbound_norm_i_arr)
        vy_unbound_norm = np.asarray(vy_unbound_norm_i_arr)
        vz_unbound_norm = np.asarray(vz_unbound_norm_i_arr)
        v_GoodIDs_rand_norm = ravf.modulus(vx_unbound_norm, vy_unbound_norm, vz_unbound_norm)
        v_GoodIDs_bound = ravf.modulus(vx_bound, vy_bound, vz_bound)
        v_new = np.concatenate([v_GoodIDs_bound, v_GoodIDs_rand_norm])
        K_rand_norm = E_kin(v_new)  # Kinetic energy after 1.st randomization and subsequent normalization
        K_rand_norm_mean = np.mean(K_rand_norm)
        K_rand_norm_mean_in_bin_arr.append(K_rand_norm_mean)
        Ratio_norm = np.sqrt(np.abs(V_GoodIDs) / K_rand_norm)
        Ratio_norm_mean = np.mean(Ratio_norm)
        Ratio_norm_mean_in_bin_arr.append(Ratio_norm_mean)
        E_tot_new = V_GoodIDs + E_kin(v_new)

        # This does not give the right result. There should be zero unbound perticles here! Is the sorting wrong?
        for i in range(len(E_tot_new)):
            if E_tot_new[i] > 0.:
                print('E_tot_new check. This is an unbound particle!', i)

        UnboundIDs_new = np.where(E_tot_new > 0.)
        print(f'{len(UnboundIDs_new[0])= }')
        x_GoodIDs_arr.append(x_GoodIDs)
        y_GoodIDs_arr.append(y_GoodIDs)
        z_GoodIDs_arr.append(z_GoodIDs)
        M_GoodIDs_arr.append(M_GoodIDs)
        V_mean_in_bin = np.mean(V_GoodIDs)
        V_mean_in_bin_arr.append(V_mean_in_bin)
        K_Ratio = np.sqrt(K_init_mean / K_rand_norm)
        vx = np.concatenate([vx_bound, vx_unbound_norm])
        vx *= K_Ratio
        vy = np.concatenate([vy_bound, vy_unbound_norm])
        vy *= K_Ratio
        vz = np.concatenate([vz_bound, vz_unbound_norm])
        vz *= K_Ratio
        v_final = ravf.modulus(vx, vy, vz)
        K_final = E_kin(v_final)  # Kinetic energy after 1.st randomization and subsequent normalization
        K_final_mean = np.mean(K_final)
        K_final_mean_in_bin_arr.append(K_final_mean)
        vx_final_arr.append(vx)
        vy_final_arr.append(vy)
        vz_final_arr.append(vz)
    return (np.concatenate(np.asarray(x_GoodIDs_arr), axis=0)
            , np.concatenate(np.asarray(y_GoodIDs_arr), axis=0)
            , np.concatenate(np.asarray(z_GoodIDs_arr), axis=0)
            , np.concatenate(np.asarray(vx_final_arr), axis=0)
            , np.concatenate(np.asarray(vy_final_arr), axis=0)
            , np.concatenate(np.asarray(vz_final_arr), axis=0)
            , np.concatenate(np.asarray(M_GoodIDs_arr), axis=0))

