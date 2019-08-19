# -*- coding: utf-8 -*-

import h5py
import numpy              as     np
import matplotlib.pyplot  as     plt
import IPython
from   matplotlib.colors  import LogNorm
import time
from   pylab              import *
from   scipy.stats        import norm
from   scipy.optimize     import curve_fit
import scipy              as     sp
import seaborn            as     sns
import matplotlib.patches as     mpatches

User_path        =                                      '/Users/gustav.c.rasmussen/'
Desktop_path     = User_path                          + 'Desktop/'
GADGET_E_path    = Desktop_path                       + 'RunGadget/Energy_Exchange/'
Stable_path      =                                      'Energy_exchange/Stable_structures/'
figure_path      = Desktop_path + Stable_path         + 'figures/'

#text_files_path = Desktop_path + Stable_path         + 'text_files/Soft_B/'

Soft_B_path      = 'E_HQ_1000000_B/output/'
Filename         = GADGET_E_path + Soft_B_path        + 'B_E_G2P_0_000.hdf5'
SnapshotFile     = h5py.File(Filename,'r')
F                = 'Soft_B' + Filename[len(GADGET_E_path + Soft_B_path + 'B'):-5]

Fig_v_logx_before      = 0
Fig_v_logx_after       = 1

Masses = SnapshotFile['PartType1/Masses'].value 
Pos    = SnapshotFile['PartType1/Coordinates'].value 
Vel    = SnapshotFile['PartType1/Velocities'].value  
V      = SnapshotFile['PartType1/Potential'].value     
M      = Masses
x      = Pos[:,0]
y      = Pos[:,1]
z      = Pos[:,2]
vx     = Vel[:,0]
vy     = Vel[:,1]
vz     = Vel[:,2]
minV   = np.argmin(V)  
xC     = x[minV] 
yC     = y[minV]
zC     = z[minV]
vxC    = vx[minV]
vyC    = vy[minV]
vzC    = vz[minV]
R      = ((x-xC)**2+(y-yC)**2+(z-zC)**2)**.5
x      =  x - np.median(x)
y      =  y - np.median(y)
z      =  z - np.median(z)
vx     = vx - np.median(vx)
vy     = vy - np.median(vy)
vz     = vz - np.median(vz)
#M_limit = np.sum(M) # total mass
IDs = np.argsort(R)
x_IDs  = x[IDs]
y_IDs  = y[IDs]
z_IDs  = z[IDs]
vx_IDs = vx[IDs]
vy_IDs = vy[IDs]
vz_IDs = vz[IDs]
R_IDs  = R[IDs]
V_IDs  = V[IDs]
M_IDs  = M[IDs]

N_total             = x.shape[0]
N_particles_per_bin = 500
N_bins              = N_total/N_particles_per_bin

bin_radius_arr                  = []
x_GoodIDs_arr                   = []
y_GoodIDs_arr                   = []
z_GoodIDs_arr                   = []
vx_GoodIDs_rand_arr             = []
vy_GoodIDs_rand_arr             = []
vz_GoodIDs_rand_arr             = []
M_GoodIDs_arr                   = []
vx_GoodIDs_rand_norm_arr        = []
vy_GoodIDs_rand_norm_arr        = []
vz_GoodIDs_rand_norm_arr        = []
vx_final_arr                    = []
vy_final_arr                    = []
vz_final_arr                    = []
K_init_mean_inside_bin_arr      = []
K_rand_mean_inside_bin_arr      = []
K_rand_norm_mean_inside_bin_arr = []
K_final_mean_inside_bin_arr     = []
V_mean_inside_bin_arr           = []
Ratio_init_mean_inside_bin_arr  = []
Ratio_rand_mean_inside_bin_arr  = []
Ratio_norm_mean_inside_bin_arr  = []

if Fig_v_logx_before:
    v = (vx**2+vy**2+vz**2)**.5
    f,(ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    ax1.set_xlabel(r'$\log x$'      ,fontsize=30)
    ax1.set_ylabel(r'$v_{tot}$',fontsize=30)
    ax1.plot(np.log10(x),v,'o',color='Blue',label='Soft B 0_005',lw=3,ms=2)
    leg = ax1.legend(prop=dict(size=18),numpoints=1,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'II: $\Delta E$ (before perturbations)',fontsize=30)
    f.savefig(figure_path + 'Soft_B_0_005_v_logx_II.png')

for i in range(N_bins): # Divide structure into mass-bins. Favoured over radial bins, as outer region of structure has less particles.
    vx_unbound_norm_i_arr      = []
    vy_unbound_norm_i_arr      = []
    vz_unbound_norm_i_arr      = []
    vx_unbound_norm_i_rand_arr = []
    vy_unbound_norm_i_rand_arr = []
    vz_unbound_norm_i_rand_arr = []
    vx_unbound_norm_i_zero_arr = []
    vy_unbound_norm_i_zero_arr = []
    vz_unbound_norm_i_zero_arr = []
    GoodIDs                    = np.arange(i*N_particles_per_bin,(i+1)*N_particles_per_bin)
    x_GoodIDs                  = x_IDs[GoodIDs]
    y_GoodIDs                  = y_IDs[GoodIDs]
    z_GoodIDs                  = z_IDs[GoodIDs]
    vx_GoodIDs                 = vx_IDs[GoodIDs]
    vy_GoodIDs                 = vy_IDs[GoodIDs]
    vz_GoodIDs                 = vz_IDs[GoodIDs]
    M_GoodIDs                  = M_IDs[GoodIDs]
    V_GoodIDs                  = V_IDs[GoodIDs] 
    R_min                      = R_IDs[GoodIDs][0]
    R_max                      = R_IDs[GoodIDs][-1]
    
    # 1.st randomization
    a = np.random.uniform(low=.9999,high=1.00001,size=(N_particles_per_bin,)) 
    b = np.random.uniform(low=.9999,high=1.00001,size=(N_particles_per_bin,)) 
    c = np.random.uniform(low=.9999,high=1.00001,size=(N_particles_per_bin,))
    vx_GoodIDs_rand = a*vx_GoodIDs
    vy_GoodIDs_rand = b*vy_GoodIDs 
    vz_GoodIDs_rand = c*vz_GoodIDs
    v_GoodIDs_rand  = (vx_GoodIDs_rand**2+vy_GoodIDs_rand**2+vz_GoodIDs_rand**2)**.5    
    
    x_GoodIDs_arr.append(x_GoodIDs)
    y_GoodIDs_arr.append(y_GoodIDs)
    z_GoodIDs_arr.append(z_GoodIDs)
    
    vx           = vx_GoodIDs_rand
    vy           = vy_GoodIDs_rand
    vz           = vz_GoodIDs_rand

    # Split particles into bound and unbound
    K_rand          = .5*v_GoodIDs_rand**2
    E_tot_rand      = V_GoodIDs + K_rand
    UnboundIDs_rand = np.where(E_tot_rand>0.)  # Unbound particles. 
    BoundIDs_rand   = np.where(E_tot_rand<=0.) # Bound particles.
    vx_unbound = vx_GoodIDs_rand[UnboundIDs_rand]
    vy_unbound = vy_GoodIDs_rand[UnboundIDs_rand]
    vz_unbound = vz_GoodIDs_rand[UnboundIDs_rand]
    vx_bound   = vx_GoodIDs_rand[BoundIDs_rand]
    vy_bound   = vy_GoodIDs_rand[BoundIDs_rand]
    vz_bound   = vz_GoodIDs_rand[BoundIDs_rand]
    
    # Normalize unbound particles
    for i in range(len(UnboundIDs_rand[0])):
        if np.sum(K_rand[UnboundIDs_rand]) != 0:        
            vx_unbound_norm_i = vx_unbound[i]*np.random.uniform(low=.8, high=1.)*(np.sum(np.abs(V_GoodIDs[UnboundIDs_rand]))/np.sum(K_rand[UnboundIDs_rand]))**.5 
            vy_unbound_norm_i = vy_unbound[i]*np.random.uniform(low=.8, high=1.)*(np.sum(np.abs(V_GoodIDs[UnboundIDs_rand]))/np.sum(K_rand[UnboundIDs_rand]))**.5
            vz_unbound_norm_i = vz_unbound[i]*np.random.uniform(low=.8, high=1.)*(np.sum(np.abs(V_GoodIDs[UnboundIDs_rand]))/np.sum(K_rand[UnboundIDs_rand]))**.5
        else:
            print 'vx_unbound_norm_i/vx_unbound[i] = ', vx_unbound_norm_i/vx_unbound[i]
        vx_unbound_norm_i_arr.append(vx_unbound_norm_i)
        vy_unbound_norm_i_arr.append(vy_unbound_norm_i)
        vz_unbound_norm_i_arr.append(vz_unbound_norm_i)
    vx_unbound_norm     = np.asarray(vx_unbound_norm_i_arr)
    vy_unbound_norm     = np.asarray(vy_unbound_norm_i_arr)
    vz_unbound_norm     = np.asarray(vz_unbound_norm_i_arr)
    v_GoodIDs_rand_norm = (vx_unbound_norm**2+vy_unbound_norm**2+vz_unbound_norm**2)**.5 
    v_GoodIDs_bound     = (vx_bound**2+vy_bound**2+vz_bound**2)**.5  
    v_new               = np.concatenate([v_GoodIDs_bound,v_GoodIDs_rand_norm])




    #v_final      = (vx**2+vy**2+vz**2)**.5

    vx           = np.concatenate([vx_bound,vx_unbound_norm])
    vy           = np.concatenate([vy_bound,vy_unbound_norm])
    vz           = np.concatenate([vz_bound,vz_unbound_norm])

    vx_final_arr.append(vx)
    vy_final_arr.append(vy)
    vz_final_arr.append(vz)

x      = np.asarray(x_GoodIDs_arr)
y      = np.asarray(y_GoodIDs_arr)
z      = np.asarray(z_GoodIDs_arr)
vx     = np.asarray(vx_final_arr)
vy     = np.asarray(vy_final_arr)
vz     = np.asarray(vz_final_arr)

x      = np.concatenate(x, axis=0)
y      = np.concatenate(y, axis=0)
z      = np.concatenate(z, axis=0)
vx     = np.concatenate(vx, axis=0)
vy     = np.concatenate(vy, axis=0)
vz     = np.concatenate(vz, axis=0)














   
if Fig_v_logx_after:
    v = (vx**2+vy**2+vz**2)**.5
    f,(ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    ax1.set_xlabel(r'$\log x$'      ,fontsize=30)
    ax1.set_ylabel(r'$v_{tot}$',fontsize=30)
    ax1.plot(np.log10(x),v,'o',color='Blue',label='Soft B 0_005 P2G',lw=3,ms=2)
    leg = ax1.legend(prop=dict(size=18),numpoints=1,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'II: $\Delta E$ (tiny perturbations, normalization of unbound par.)',fontsize=30)

    f.savefig(figure_path + 'Soft_B_0_005_P2G_v_logx_II_rand_unboundnorm.png')


    








plt.show()







