# -*- coding: utf-8 -*-

import h5py
import numpy as np
import matplotlib.lines as lines
import matplotlib.pyplot as plt
import IPython
from matplotlib.colors import LogNorm
import time
import pylab
from mpl_toolkits.mplot3d import Axes3D
import scipy
# import matplotlib.gridspec as gridspec
import seaborn as sns
from pathlib import Path

User_path = Path.cwd()
Desktop_path = User_path + 'Desktop/'
# GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IIa/'
# GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IIb/'
GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IIc/'
# GADGET_E_path = Desktop_path + 'RunGadget/Energy_Exchange/IId/'

B = 0
B_control = 0
CS1 = 0
CS1_control = 0
CS4 = 0
CS4_control = 0
CS5 = 0
CS5_control = 0
CS6 = 0
CS6_control = 0
DS1 = 0
DS1_control = 0
D2 = 0
D2_control = 0
E = 0
E_control = 0
mass_bins_B = 0
mass_bins_B_control = 0
mass_bins_CS1 = 0
mass_bins_CS1_control = 0
mass_bins_CS4 = 0
mass_bins_CS4_control = 0
mass_bins_CS5 = 0
mass_bins_CS5_control = 0
mass_bins_CS6 = 0
mass_bins_CS6_control = 0
mass_bins_DS1 = 0
mass_bins_DS1_control = 0
mass_bins_D2 = 0
mass_bins_D2_control = 0
mass_bins_E = 0
mass_bins_E_control = 0
B_Rlimit10000_20bins = 0
B_control_Rlimit10000_20bins = 0

Colors = ['r', 'b', 'k', 'brown', 'y'] * 2
Colors2 = ['m', 'c', 'g', 'grey', 'SkyBlue', 'orange'] * 2
Symbols = ['-o','-s','-<','--v','--*','--s','--d'] * 2
# Symbols = ['--.','--s','--o','--v','--^','--<','-->'] * 2
Symbols2 = ['.','s','o','v','^','<','>'] * 2

# Switches
log_r_r2_beta_CS4CS5CS6DS1D2_Rlimit32 = 0
log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32_IIc = 0
log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32_IIc_50bins = 0

log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32 = 0
log_r_r2_kappa_CS4CS5CS6DS1D2_Rlimit32 = 0

r_rho = 0
log_r_r2_logrho = 0
logr_logrho_R10000 = 0
log_r_r2_logrho_B = 0

Fig_beta_gamma_kappa_CS1CS2CS3_20_50_bins = 0  # Panel created 
Fig_beta_gamma_kappa_CS4CS5CS6_20_50_bins = 0  # Panel created
Fig_beta_gamma_kappa_CS4CS5CS6_Final_20_50_bins = 0  # Panel created
Fig_beta_gamma_kappa_DS1D2_20_50_bins = 0  # Panel created
Fig_beta_gamma_kappa_DS1D2_Final_20_50_bins = 0  # Panel created
Fig_beta_gamma_kappa_BCS4CS5CS6DS1D2E_IC_Final_20_50_bins = 0  # Panel created  # Add E plot
Fig_beta_gamma_kappa_rfp_BCS4CS5CS6DS1D2E_Final_50_bins_R_limit_10000  = 0  # Created.  # Add E plot
Overplot_IC_Final = 0  # Panel created  # Add E plot
IC_Final_4_subplots = 0  # Panel created  # Add E plot

# beta_vs_gamma_BCS4CS5CS6DS1D2E_Rlimit32 = 1 # Fix: correct number of files. 0-4

beta_vs_gamma_CS4CS5CS6_Rlimit32 = 0
beta_vs_gamma_plus_kappa_DS1D2_Rlimit32 = 0
beta_vs_gamma_DeltaG_DS1_Rlimit32 = 0 
beta_vs_gamma_CS4_Time_evolution_Rlimit32 = 0
beta_vs_gamma_D2_Time_evolution_Rlimit32 = 0
beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit32 = 0
beta_vs_gamma_BCS4CS5CS6DS1D2E_Rlimit32_Run_5_10 = 0
beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit32_Run_5_10 = 0
beta_vs_gamma_BCS4CS5CS6DS1D2E_Rlimit10_20_bins = 0
beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit10_20_bins = 0
beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit10000_20_bins = 0 
beta_vs_gamma_plus_kappa = 0  # Panel created # Add E plot
Fig_beta_gamma_logr_IC_Final_panel = 0  # Add E plot 

beta_vs_gamma_plus_kappa_Test_CS4_Rlimit32 = 0
beta_vs_gamma_plus_kappa_Test_D2_Rlimit32 = 0 
beta_vs_gamma_plus_kappa_Test_CS4_10tdyn_Rlimit32 = 0

beta_vs_gamma_plus_kappa_IIb_CS4_Rlimit32 = 0
beta_vs_gamma_plus_kappa_IIb_D2_Rlimit32 = 0
beta_vs_gamma_plus_kappa_IIc_CS4_Rlimit32 = 0
beta_vs_gamma_plus_kappa_IIc_D2_Rlimit32 = 0 
beta_vs_gamma_plus_kappa_IId_CS4_Rlimit32 = 0
beta_vs_gamma_plus_kappa_IId_D2_Rlimit32 = 0

beta_vs_gamma_plus_kappa_IIc_ABCS4CS5CS6DS1D2E_Rlimit32 = 0

if log_r_r2_beta_CS4CS5CS6DS1D2_Rlimit32:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,1],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,1],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,1],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,1],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,1],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)

    ax1.set_title(r'IC ($IIa, R_{limit} = 32$)', fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$', fontsize=30)
    ax1.set_ylabel(r'$\beta$', fontsize=30)
    # ax1.set_xlim(-.2, 1.)
    ax1.set_ylim(-.5, 1.)

    # Final
    data, label = datalist_CS4_Rlimit32_20bins[4]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,1],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[3]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,1],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[3]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,1],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[4]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,1],Symbols[4],color = Colors[4], label=label,lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[4]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,1],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_title(r'Final', fontsize=30)
    # ax2.set_xlim(-.2, 1.)
    ax2.set_ylim(-.5, 1.)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',
                    labelbottom='on',right='off',left='off',labelleft='off')

    # Control
    data,label = datalist_CS4_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,1],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)

    data,label = datalist_CS5_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,1],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)

    data,label = datalist_CS6_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,1],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)

    data,label = datalist_DS1_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,1],Symbols[4],color = Colors[4], label=label,lw=2,ms=7)

    data,label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,1],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)

    ax3.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax3.set_title(r'Control' ,fontsize=30)
    # ax3.set_xlim(-.2, 1.)
    ax3.set_ylim(-.5, 1.)
    ax3.yaxis.tick_right()
    f.savefig(figure_path + 'log_r_r2_beta_CS4CS5CS6DS1D2_Rlimit32.png')

if log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32_IIc:
    f,(ax1,ax2) = plt.subplots(1,2,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)

    ax1.set_title(r'IC ($IIc, R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    # ax1.set_xlim(-.2, 1.)
    ax1.set_ylim(-5.,.5)

    # Final
    data, label = datalist_CS4_Rlimit32_20bins[3]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[0],color = Colors[0], label=label+ '_40_21',lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[1],color = Colors[1], label=label+ '_40_21',lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[2],color = Colors[2], label=label+ '_40_21',lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[3],color = Colors[3], label=label + '_60_21',lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[5]
    label = label[len(text_files_path) + 5:-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[4],color=Colors[4],label=label+ '_60_21',lw=2,ms=7)
    
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_title(r'Final'   ,fontsize=30)
    #ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-5.,.5)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',
                    labelbottom='on',right='off',left='off',labelleft='off')

    f.savefig(figure_path + 'log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32_IIc.png')

if log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32_IIc_50bins:
    f,(ax1,ax2) = plt.subplots(1,2,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)

    ax1.set_title(r'IC ($IIc, R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    # ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-5.,.5)

    # Final
    data, label = datalist_CS4_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[0],color = Colors[0], label=label+ '_40_21',lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[1],color = Colors[1], label=label+ '_40_21',lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[2],color = Colors[2], label=label+ '_40_21',lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[3],color = Colors[3], label=label+ '_60_21',lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[6]
    label       = label[len(text_files_path)+5:-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[4],color=Colors[4],label=label+ '_60_21',lw=2,ms=7)
    
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_title(r'Final. 50 bins'   ,fontsize=30)
    # ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-5.,.5)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',
                    labelbottom='on',right='off',left='off',labelleft='off')

    f.savefig(figure_path + 'log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32_IIc_50bins.png')

if log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)

    ax1.set_title(r'IC ($IIa, R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    #ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-4.,1.)

    # Final
    data, label = datalist_CS4_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)

    data, label = datalist_CS5_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)

    data, label = datalist_CS6_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)

    data, label = datalist_DS1_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[4],color = Colors[4], label=label,lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_title(r'Final'   ,fontsize=30)
    #ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-4.,1.)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='off',labelleft='off')

    # Control
    data,label = datalist_CS4_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,2],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)

    data,label = datalist_CS5_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)

    data,label = datalist_CS6_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,2],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)

    data,label = datalist_DS1_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,2],Symbols[4],color = Colors[4], label=label,lw=2,ms=7)

    data,label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)

    ax3.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax3.set_title(r'Control' ,fontsize=30)
    # ax3.set_xlim(-.2, 1.)
    ax3.set_ylim(-4., 1.)
    ax3.yaxis.tick_right()
    f.savefig(figure_path + 'log_r_r2_gamma_CS4CS5CS6DS1D2_Rlimit32.png')

if log_r_r2_kappa_CS4CS5CS6DS1D2_Rlimit32:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,3],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,3],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,3],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,3],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(np.log(data[:,7]),data[:,3],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)

    ax1.set_title(r'IC ($IIa, R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$' ,fontsize=30)
    ax1.set_ylabel(r'$\kappa$',fontsize=30)
    #ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-1.5,.5)

    # Final
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,3],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,3],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,3],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,3],Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(np.log(data[:,7]),data[:,3],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_title(r'Final'   ,fontsize=30)
    #ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-1.5,.5)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='off',labelleft='off')

    # Control
    # CS4
    data,label = datalist_CS4_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,3],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS5
    data,label = datalist_CS5_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,3],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # CS6
    data,label = datalist_CS6_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,3],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    # DS1
    data,label = datalist_DS1_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,3],Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    # Soft_D2
    data,label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(np.log(data[:,7]),data[:,3],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)

    ax3.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax3.set_title(r'Control' ,fontsize=30)
    #ax3.set_xlim(-.2,1.)
    ax3.set_ylim(-1.5,.5)
    ax3.yaxis.tick_right()
    f.savefig(figure_path + 'log_r_r2_kappa_CS4CS5CS6DS1D2_Rlimit32.png')

if r_rho:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    # Soft_B
    data, label = datalist_Soft_B_Rlimit32_50bins[0]
    ax1.plot(data[:,5],data[:,7],Symbols[0],color=Colors[0],label='B',lw=2,ms=7)
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[0]
    ax1.plot(data[:,5],data[:,7],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[0]
    ax1.plot(data[:,5],data[:,7],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[0]
    ax1.plot(data[:,5],data[:,7],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[0]
    ax1.plot(data[:,5],data[:,7],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    ax1.plot(data[:,5],data[:,7],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    # E
    data, label = datalist_E_Rlimit32_50bins[0]
    ax1.plot(data[:,5],data[:,7],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
        
    ax1.set_title(r'IC ($R_{limit}=32$)',fontsize=30)
    ax1.set_xlabel('r'                  ,fontsize=30)
    ax1.set_ylabel(r'$\rho$'            ,fontsize=30)
    ax1.set_ylim(.00,.02)

    # Final
    # Soft_B
    data, label = datalist_Soft_B_Rlimit32_50bins[1]
    ax2.plot(data[:,5],data[:,7],Symbols[0],color=Colors[0],label='B',lw=2,ms=7)
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[1]
    ax2.plot(data[:,5],data[:,7],Symbols[1],color=Colors[1],label='CS4',lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[1]
    ax2.plot(data[:,5],data[:,7],Symbols[2],color=Colors[2],label='CS5',lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[1]
    ax2.plot(data[:,5],data[:,7],Symbols[3],color=Colors[3],label='CS6',lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[1]
    ax2.plot(data[:,5],data[:,7],Symbols[4],color=Colors[4],label='DS1',lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[1]
    ax2.plot(data[:,5],data[:,7],Symbols[5],color=Colors[5],label='D2',lw=2,ms=7)
    # E
    data, label = datalist_E_Rlimit32_50bins[1]
    ax2.plot(data[:,5],data[:,7],Symbols[6],color=Colors[6],label='E',lw=2,ms=7)

    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_title(r'Sim. II, Final',fontsize=30)
    ax2.set_xlabel('r'             ,fontsize=30)
    ax2.set_ylim(.00,.02)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='off',labelleft='off')

    # Control, Final
    # Control Soft_B
    data, label = datalist_Soft_B_control_Rlimit32_50bins[0]
    ax3.plot(data[:,5],data[:,7],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    # Control CS4
    data, label = datalist_CS4_control_Rlimit32_20bins[0]
    ax3.plot(data[:,5],data[:,7],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    # Control CS5
    data, label = datalist_CS5_control_Rlimit32_20bins[0]
    ax3.plot(data[:,5],data[:,7],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    # Control CS6
    data, label = datalist_CS6_control_Rlimit32_20bins[0]
    ax3.plot(data[:,5],data[:,7],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    # Control DS1
    data, label = datalist_DS1_control_Rlimit32_20bins[0]
    ax3.plot(data[:,5],data[:,7],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    # Control Soft_D2
    data, label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    ax3.plot(data[:,5],data[:,7],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    # Control E
    data, label = datalist_E_control_Rlimit32_50bins[0]
    ax3.plot(data[:,5],data[:,7],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)

    ax3.set_title(r'Control, Final',fontsize=30)
    ax3.set_xlabel('r'             ,fontsize=30)
    ax3.set_ylim(.00,.02)
    #ax3.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='on',labelleft='on')
    ax3.yaxis.tick_right()

    f.savefig(figure_path + 'r_rho.png')

if log_r_r2_logrho:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    #f.tight_layout()
    # IC
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    ax1.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[5],color = Colors[5], label=label,lw=2,ms=7)

    ax1.set_title(r'IC ($R_{limit}=32$)',fontsize=30)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax1.set_ylabel(r'$\log \rho$',fontsize=30)
    ax1.set_ylim(-7.,1.)

    # Final
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[4]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[1],color = Colors[1], label='CS4',lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[3]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[2],color = Colors[2], label='CS5',lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[3]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[3],color = Colors[3], label='CS6',lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[4]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[4],color = Colors[4], label='DS1',lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[4]
    ax2.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[5],color = Colors[5], label='D2',lw=2,ms=7)

    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_title(r'IIa, Final',fontsize=30)
    ax2.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax2.set_ylim(-7.,1.)
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='off',labelleft='off')

    # Control, Final
    # Control CS4
    data, label = datalist_CS4_control_Rlimit32_20bins[0]
    ax3.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # Control CS5
    data, label = datalist_CS5_control_Rlimit32_20bins[0]
    ax3.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # Control CS6
    data, label = datalist_CS6_control_Rlimit32_20bins[0]
    ax3.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    # Control DS1
    data, label = datalist_DS1_control_Rlimit32_20bins[0]
    ax3.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    # Control Soft_D2
    data, label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    ax3.plot(np.log10(data[:,7]),np.log10(data[:,8]),Symbols[5],color = Colors[5], label=label,lw=2,ms=7)
    ax3.set_title(r'Control, Final',fontsize=30)
    ax3.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=30)
    ax3.set_ylim(-7.,1.)
    #ax3.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='on',labelleft='on')
    ax3.yaxis.tick_right()

    f.savefig(figure_path + 'logr_logrho.png')

if logr_logrho_R10000:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0) 
    for i in range(len(datalist_B_control_Rlimit10000_20bins)):
        data, label = datalist_B_control_Rlimit10000_20bins[i]
        a = label[81:-29]
        print a
        ax1.plot( data[:,0], np.log10(data[:,8]),Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    ax1.set_title(r'Control Sim. of B ($R_{limit}=10^4, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\log r$',fontsize=30)
    ax1.set_ylabel(r'$\log \rho$',fontsize=30)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    for i in range(len(datalist_B_Rlimit10000_20bins)):
        data, label = datalist_B_Rlimit10000_20bins[i]
        a = label[81:-29]
        ax2.plot( data[:,0], np.log10(data[:,8]),Symbols[i],color = Colors[i],  label=a,lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_title(r'Sim. II of B',fontsize=30)
    #ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',right='off',left='on',labelleft='on')
    ax2.yaxis.tick_right()
    f.savefig(figure_path + 'logr_logrho.png')

if log_r_r2_logrho_B:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0) 
    for i in range(len(datalist_B_control_Rlimit10000_20bins)):
        data, label = datalist_B_control_Rlimit10000_20bins[i]
        a = label[81:-29]
        ax1.plot( np.log10(data[:,7]), np.log10(data[:,8]),Symbols[i],color = Colors[i], label=a,lw=2,ms=7)
    ax1.set_title(r'Control Sim. of B ($R_{limit}=10^4, 20$ bins)',fontsize=24)
    ax1.set_xlabel(r'$\log (\frac{r}{r_{-2}})$',fontsize=24)
    ax1.set_ylabel(r'$\log \rho$',fontsize=24)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    for i in range(len(datalist_B_Rlimit10000_20bins)):
        data, label = datalist_B_Rlimit10000_20bins[i]
        a = label[81:-29]
        ax2.plot( np.log10(data[:,7]), np.log10(data[:,8]),Symbols[i],color = Colors[i],  label=a,lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,loc=0, fancybox=True, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_title(r'Sim. II of B',fontsize=24)
    ax2.yaxis.tick_right()
    f.savefig(figure_path + 'log_r_r2_logrho.png')

if Fig_beta_gamma_kappa_CS1CS2CS3_20_50_bins:
    f, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    data, label = datalist_3[0]
    ax1.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='C1',lw=2,ms=7 )
    data, label = datalist_3[1]
    ax1.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='C2',lw=2,ms=7 )
    data, label = datalist_3[2]
    ax1.plot( data[:,1], data[:,2],Symbols[8],color = Colors[8], label='C3',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax1.set_title(r'Initial conditions. 50 bins',fontsize=20)
    ax1.set_ylabel(r'$\gamma$',fontsize=24)
    ax1.set_xlim(-5.,1.1)
    ax1.set_ylim(-6.,3.)
    ax1.axes.get_xaxis().set_visible(False)
    ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
 
    data, label = datalist_3[3]
    ax2.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='C1',lw=2,ms=7 )
    data, label = datalist_3[4]
    ax2.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='C2',lw=2,ms=7 )
    data, label = datalist_3[5]
    ax2.plot( data[:,1], data[:,2],Symbols[8],color = Colors[8], label='C3',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax2.set_title(r'20 bins',fontsize=20)
    ax2.set_ylim(-6.,3.)
    ax2.set_xlim(-0.1,1.1)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    data, label = datalist_3[0]
    ax3.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label='C1',lw=2,ms=7 )
    data, label = datalist_3[1]
    ax3.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label='C2',lw=2,ms=7 )
    data, label = datalist_3[2]
    ax3.plot( data[:,1], data[:,3],Symbols[8],color = Colors[8],  label='C3',lw=2,ms=7 )
    ax3.set_xlabel(r'$\beta$',fontsize=24)
    ax3.set_ylabel(r'$\kappa$',fontsize=24)
    ax3.set_xlim(-5.,1.1)
    ax3.set_ylim(-10.,20.)

    data, label = datalist_3[3]
    ax4.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_3[4]
    ax4.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_3[5]
    ax4.plot( data[:,1], data[:,3],Symbols[8],color = Colors[8],  label=label[:-15],lw=2,ms=7 )
    ax4.set_xlim(-0.1,1.1)
    ax4.set_ylim(-10.,20.)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    ax4.axes.get_yaxis().set_visible(False)
    f.savefig(figure_path + 'CS1CS2CS3_beta_gamma_kappa.png')

if Fig_beta_gamma_kappa_CS4CS5CS6_20_50_bins:
    f, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    data, label = datalist_3[6]
    ax1.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='C4',lw=2,ms=7 )
    data, label = datalist_3[7]
    ax1.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='C5',lw=2,ms=7 )
    data, label = datalist_3[8]
    ax1.plot( data[:,1], data[:,2],Symbols[8],color = Colors[8], label='C6',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax1.set_title(r'Initial conditions. 50 bins',fontsize=20)
    ax1.set_ylabel(r'$\gamma$',fontsize=24)
    ax1.set_xlim(-.3,1.1)
    ax1.set_ylim(-4.7,-1.)
    ax1.axes.get_xaxis().set_visible(False)

    data, label = datalist_3[9]
    ax2.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='C4',lw=2,ms=7 )
    data, label = datalist_3[10]
    ax2.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='C5',lw=2,ms=7 )
    data, label = datalist_3[11]
    ax2.plot( data[:,1], data[:,2],Symbols[8],color = Colors[8], label='C6',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax2.set_title(r'20 bins',fontsize=20)
    ax2.set_xlim(-.2,1.1)
    ax2.set_ylim(-4.7,-1.)
    #ax2.yaxis.tick_right()
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    data, label = datalist_3[6]
    ax3.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label='C4',lw=2,ms=7 )
    data, label = datalist_3[7]
    ax3.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label='C5',lw=2,ms=7 )
    data, label = datalist_3[8]
    ax3.plot( data[:,1], data[:,3],Symbols[8],color = Colors[8],  label='C6',lw=2,ms=7 )
    ax3.set_xlabel(r'$\beta$',fontsize=24)
    ax3.set_ylabel(r'$\kappa$',fontsize=24)
    ax3.set_xlim(-.3,1.1)
    ax3.set_ylim(-6.,3.)

    data, label = datalist_3[9]
    ax4.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_3[10]
    ax4.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_3[11]
    ax4.plot( data[:,1], data[:,3],Symbols[8],color = Colors[8],  label=label[:-15],lw=2,ms=7 )
    ax4.set_xlim(-0.2,1.1)
    ax4.set_ylim(-6.,3.)
    ax4.axes.get_yaxis().set_visible(False)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    f.savefig(figure_path + 'CS4CS5CS6_beta_gamma_kappa.png')

if Fig_beta_gamma_kappa_CS4CS5CS6_Final_20_50_bins:
    f, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)      
    data, label = datalist_4[0]
    ax1.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='C4',lw=2,ms=7 )
    data, label = datalist_4[1]
    ax1.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='C5',lw=2,ms=7 )
    data, label = datalist_4[2]
    ax1.plot( data[:,1], data[:,2],Symbols[8],color = Colors[8], label='C6',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax1.set_title(r'Final. 50 bins',fontsize=20)
    ax1.set_ylabel(r'$\gamma$',fontsize=24)
    ax1.set_xlim(-2.,1.)
    ax1.set_ylim(-4.,3.)
    ax1.axes.get_xaxis().set_visible(False)

    data, label = datalist_4[3]
    ax2.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='C4',lw=2,ms=7 )
    data, label = datalist_4[4]
    ax2.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='C5',lw=2,ms=7 )
    data, label = datalist_4[5]
    ax2.plot( data[:,1], data[:,2],Symbols[8],color = Colors[8], label='C6',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax2.set_title(r'20 bins',fontsize=20)
    ax2.set_xlim(-.2,.9)
    ax2.set_ylim(-4.,3.)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    data, label = datalist_4[0]
    ax3.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label='C4',lw=2,ms=7 )
    data, label = datalist_4[1]
    ax3.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label='C5',lw=2,ms=7 )
    data, label = datalist_4[2]
    ax3.plot( data[:,1], data[:,3],Symbols[8],color = Colors[8],  label='C6',lw=2,ms=7 )
    #ax3.set_title(r'IC for C1 and C2',fontsize=20)
    ax3.set_xlabel(r'$\beta$',fontsize=24)
    ax3.set_ylabel(r'$\kappa$',fontsize=24)
    ax3.set_xlim(-2.,1.)
    ax3.set_ylim(-3.,7.)
    
    data, label = datalist_4[3]
    ax4.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_4[4]
    ax4.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_4[5]
    ax4.plot( data[:,1], data[:,3],Symbols[8],color = Colors[8],  label=label[:-15],lw=2,ms=7 )
    #ax4.set_title(r'IC for C1 and C2',fontsize=20)
    ax4.set_xlabel(r'$\beta$',fontsize=24)
    ax4.set_xlim(-0.2,.9)
    ax4.set_ylim(-3.,7.)
    ax4.axes.get_yaxis().set_visible(False)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    f.savefig(figure_path + 'CS4CS5CS6_beta_gamma_kappa_Final.png')

if Fig_beta_gamma_kappa_DS1D2_20_50_bins:
    f, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    data, label = datalist_5[0]
    ax1.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='D1',lw=2,ms=7 )
    data, label = datalist_5[1]
    ax1.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='D2',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax1.set_title(r'Initial conditions. 50 bins',fontsize=20)
    ax1.set_ylabel(r'$\gamma$',fontsize=24)
    ax1.set_xlim(-.3,1.1)
    ax1.set_ylim(-5.,1.)
    ax1.axes.get_xaxis().set_visible(False)

    data, label = datalist_5[2]
    ax2.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='D1',lw=2,ms=7 )
    data, label = datalist_5[3]
    ax2.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='D2',lw=2,ms=7 )
    x = np.linspace(-2.,2.)
    y = -2*x
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 4, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax2.set_title(r'20 bins',fontsize=20)
    ax2.set_xlim(-.1,1.1)
    ax2.set_ylim(-5.,1.)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    data, label = datalist_5[0]
    ax3.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label='D1',lw=2,ms=7 )
    data, label = datalist_5[1]
    ax3.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label='D2',lw=2,ms=7 )
    ax3.set_xlabel(r'$\beta$',fontsize=24)
    ax3.set_ylabel(r'$\kappa$',fontsize=24)
    ax3.set_xlim(-.3,1.1)
    ax3.set_ylim(-6.,3.)
    
    data, label = datalist_5[2]
    ax4.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_5[3]
    ax4.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label=label[:-15],lw=2,ms=7 )
    ax4.set_xlim(-.1,1.1)
    ax4.set_ylim(-6.,3.)
    ax4.axes.get_yaxis().set_visible(False)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    f.savefig(figure_path + 'DS1D2_beta_gamma_kappa.png')

if Fig_beta_gamma_kappa_DS1D2_Final_20_50_bins:
    f, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13,11))      
    f.subplots_adjust(hspace=0,wspace=0)
    data, label = datalist_6[0]
    ax1.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='D1',lw=2,ms=7 )
    data, label = datalist_6[1]
    ax1.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='D2',lw=2,ms=7 )
    x = np.linspace(-.5,2.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 1, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax1.set_title(r'Final. 50 bins',fontsize=20)
    ax1.set_ylabel(r'$\gamma$',fontsize=24)
    ax1.set_xlim(-4.,1.5)
    ax1.set_ylim(-4.,1.)
    ax1.axes.get_xaxis().set_visible(False)

    data, label = datalist_6[2]
    ax2.plot( data[:,1], data[:,2],Symbols[6],color = Colors[6], label='D1',lw=2,ms=7 )
    data, label = datalist_6[3]
    ax2.plot( data[:,1], data[:,2],Symbols[7],color = Colors[7], label='D2',lw=2,ms=7 )
    x = np.linspace(-.5,2.)
    y = -2*x
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 1, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax2.set_title(r'20 bins',fontsize=20)
    ax2.set_xlim(-.6,1.1)
    ax2.set_ylim(-4.,1.)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    data, label = datalist_6[0]
    ax3.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label='D1',lw=2,ms=7 )
    data, label = datalist_6[1]
    ax3.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label='D2',lw=2,ms=7 )
    ax3.set_xlabel(r'$\beta$',fontsize=24)
    ax3.set_ylabel(r'$\kappa$',fontsize=24)
    ax3.set_xlim(-4.,1.5)
    ax3.set_ylim(-3.,6.)

    data, label = datalist_6[2]
    ax4.plot( data[:,1], data[:,3],Symbols[6],color = Colors[6],  label=label[:-15],lw=2,ms=7 )
    data, label = datalist_6[3]
    ax4.plot( data[:,1], data[:,3],Symbols[7],color = Colors[7],  label=label[:-15],lw=2,ms=7 )
    ax4.set_xlim(-.6,1.1)
    ax4.set_ylim(-3.,6.)
    ax4.axes.get_yaxis().set_visible(False)
    leg = ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    f.savefig(figure_path + 'DS1D2_beta_gamma_kappa_Final.png')

if Fig_beta_gamma_kappa_BCS4CS5CS6DS1D2E_IC_Final_20_50_bins:
    f,((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8))=plt.subplots(4,2,figsize=(13,11))
    #f.tight_layout()
    f.subplots_adjust(hspace=0,wspace=0)
    # IC     
    # B
    data, label = datalist_B[0]
    ax1.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label,lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(6,9):
        data, label = datalist_3[i]
        ax1.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-5], color=Colors2[i-5],label=label ,lw=2,ms=7)
    # DS1 and D2
    for i in range(0,2):
        data, label = datalist_5[i]
        ax1.plot( data[:,1], data[:,2] + data[:,3], Symbols[i+4], color=Colors2[i+4],label=label ,lw=2,ms=7)
    # E
        
    # Restriction
    x = np.linspace(-.3,1.1)
    y = -2*x
    ax1.plot( x, y, color='Pink', lw=2, ms=7 )
    ax1.fill_between(x, 10, y,color='Violet')
    ax1.set_title(r'IC $\gamma + \kappa$',fontsize=20)
    ax1.set_ylabel(r'50 bins',fontsize=18)
    ax1.set_xlim(-.3,1.1)
    ax1.set_ylim(-10.,10.)
    leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.axes.get_xaxis().set_visible(False)
    
    # Final
    # B
    data, label = datalist_B[5]
    ax2.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label,lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(0,3):
        data, label = datalist_4[i]
        ax2.plot( data[:,1], data[:,2] + data[:,3], Symbols[i+1], color=Colors2[i+1],label=label ,lw=2,ms=7)
    # DS1 and D2
    for i in range(4,6):
        data, label = datalist_6[i]
        ax2.plot( data[:,1], data[:,2] + data[:,3], Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7)
    # E
    
    # Restriction
    x = np.linspace(-10.,2.)
    y = -2*x
    ax2.plot( x, y, color='Pink', lw=2, ms=7 )
    ax2.fill_between(x, 10, y,color='Violet') 
    ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
    ax2.set_title(r'Final $\gamma + \kappa$',fontsize=20)
    ax2.set_xlim(-1.,1.5)
    ax2.set_ylim(-10.,10.)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_ylabel(r'$R_{limit} = 5 \cdot 10^2$',fontsize=18)
    ax2.yaxis.set_label_position("right")

    # IC
    # B
    data, label = datalist_B20[0]
    ax3.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label[:-15],lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(9,12):
        data, label = datalist_3[i]
        ax3.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-8], color=Colors2[i-8],label=label[:-15] ,lw=2,ms=7)
    # DS1 and D2
    for i in range(2,4):
        data, label = datalist_5[i]
        ax3.plot( data[:,1], data[:,2] + data[:,3], Symbols[i+2], color=Colors2[i+2],label=label[:-15] ,lw=2,ms=7)
    # E
    
    # Restriction
    x = np.linspace(-.3,1.1)
    y = -2*x
    ax3.plot( x, y, color='Pink', lw=2, ms=7 )
    ax3.fill_between(x, 10, y,color='Violet') 
    ax3.set_ylabel(r'20 bins',fontsize=18)
    ax3.set_xlim(-.3,1.1)
    ax3.set_ylim(-10.,10.)
    ax3.axes.get_xaxis().set_visible(False)

    # Final
    # B
    data, label = datalist_B20[1]
    ax4.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label[:-15],lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(3,6):
        data, label = datalist_4[i]
        ax4.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-2], color=Colors2[i-2],label=label[:-15] ,lw=2,ms=7)
    # DS1 and D2
    for i in range(6,8):
        data, label = datalist_6[i]
        ax4.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-2], color=Colors2[i-2],label=label[:-15] ,lw=2,ms=7)
    # E
    
    # Restriction
    x = np.linspace(-10.,2.)
    y = -2*x
    ax4.plot( x, y, color='Pink', lw=2, ms=7 )
    ax4.fill_between(x, 10, y,color='Violet') 
    ax4.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
    ax4.set_xlim(-1.,1.5)
    ax4.set_ylim(-10.,10.)
    ax4.set_ylabel(r'$R_{limit} = 5 \cdot 10^2$',fontsize=18)
    ax4.yaxis.set_label_position("right")

    # IC    
    # B
    data, label = datalist_B_R_limit_10000[0]
    ax5.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label[:-14],lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(0,3):
        data, label = datalist_C4C5C6_R_limit_10000[i]
        ax5.plot( data[:,1], data[:,2] + data[:,3], Symbols[i+1], color=Colors2[i+1],label=label[:-14] ,lw=2,ms=7)
    # DS1 and D2
    for i in range(0,2):
        data, label = datalist_D1D2_R_limit_10000[i]
        ax5.plot( data[:,1], data[:,2] + data[:,3], Symbols[i+4], color=Colors2[i+4],label=label[:-14] ,lw=2,ms=7)
    # E
    
    # Restriction
    x = np.linspace(-.3,1.1)
    y = -2*x
    ax5.plot( x, y, color='Pink', lw=2, ms=7 )
    ax5.fill_between(x, 10, y,color='Violet')
    ax5.set_ylabel(r'50 bins',fontsize=18)
    ax5.set_xlim(-.3,1.1)
    ax5.set_ylim(-10.,10.)
    ax5.axes.get_xaxis().set_visible(False)
    
    # Final
    # B
    data, label = datalist_B_R_limit_10000[1]
    ax6.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label[:-14],lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(6,9):
        data, label = datalist_C4C5C6_R_limit_10000[i]
        ax6.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-5], color=Colors2[i-5],label=label[:-14] ,lw=2,ms=7)
    # DS1 and D2
    for i in range(4,6):
        data, label = datalist_D1D2_R_limit_10000[i]
        ax6.plot( data[:,1], data[:,2] + data[:,3], Symbols[i], color=Colors2[i],label=label[:-14] ,lw=2,ms=7)
    # E
    
    # Restriction
    x = np.linspace(-10.,2.)
    y = -2*x
    ax6.plot( x, y, color='Pink', lw=2, ms=7 )
    ax6.fill_between(x, 10, y,color='Violet') 
    ax6.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
    ax6.set_xlim(-1.,1.5)
    ax6.set_ylim(-10.,10.)
    #ax6.axes.get_xaxis().set_visible(False)
    ax6.set_ylabel(r'$R_{limit} = 10^4$',fontsize=18)
    #ax6.yaxis.tick_right()
    ax6.yaxis.set_label_position("right")

    # IC
    # B
    data, label = datalist_B_R_limit_10000[2]
    ax7.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label[:-29],lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(3,6):
        data, label = datalist_C4C5C6_R_limit_10000[i]
        ax7.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-2], color=Colors2[i-2],label=label[:-29] ,lw=2,ms=7)
    # DS1 and D2
    for i in range(2,4):
        data, label = datalist_D1D2_R_limit_10000[i]
        ax7.plot( data[:,1], data[:,2] + data[:,3], Symbols[i+2], color=Colors2[i+2],label=label[:-29] ,lw=2,ms=7)
    # E
    
    # Restriction
    x = np.linspace(-.3,1.1)
    y = -2*x
    ax7.plot( x, y, color='Pink', lw=2, ms=7 )
    ax7.fill_between(x, 10, y,color='Violet') 
    ax7.set_xlabel(r'$\beta$',fontsize=18)
    ax7.set_ylabel(r'20 bins',fontsize=18)
    ax7.set_xlim(-.3,1.1)
    ax7.set_ylim(-10.,10.)

    # Final
    # B
    data, label = datalist_B_R_limit_10000[3]
    ax8.plot( data[:,1], data[:,2] + data[:,3],Symbols[0],color = Colors[0], label=label[:-29],lw=2,ms=7 )
    # CS4, CS5 and CS6
    for i in range(9,12):
        data, label = datalist_C4C5C6_R_limit_10000[i]
        ax8.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-8], color=Colors2[i-8],label=label[:-29] ,lw=2,ms=7)
    # DS1 and D2
    for i in range(6,8):
        data, label = datalist_D1D2_R_limit_10000[i]
        ax8.plot( data[:,1], data[:,2] + data[:,3], Symbols[i-2], color=Colors2[i-2],label=label[:-29] ,lw=2,ms=7)
    # E
    
    # Restriction
    x = np.linspace(-10.,2.)
    y = -2*x
    ax8.plot( x, y, color='Pink', lw=2, ms=7 )
    ax8.fill_between(x, 10, y,color='Violet') 
    ax8.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='off', left='off', labelleft='off')
    ax8.set_xlim(-1.,1.5)
    ax8.set_ylim(-10.,10.)
    ax8.set_ylabel(r'$R_{limit} = 10^4$',fontsize=18)
    #ax8.yaxis.tick_right()
    ax8.yaxis.set_label_position("right")
    ##f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/Attractor_fig4.png')
    f.savefig(figure_path + 'Attractor_stable_fig4.png')

if Fig_beta_gamma_kappa_rfp_BCS4CS5CS6DS1D2E_Final_50_bins_R_limit_10000:
    f = plt.figure(figsize=(13,11))
    for i in range(len(datalist_rfp)):
        data, label = datalist_rfp[i]
        plt.plot( data[:,1], data[:,2] + data[:,3], Symbols[i], color=Colors2[i],label=label[:-14] ,lw=2,ms=7)
    plt.title(r'Bound particles. 50 bins. $R_{limit} = 10^4$' , fontsize=20)
    plt.xlabel(r'$\beta$' , fontsize=26)
    plt.ylabel(r'$\gamma$ + $\kappa$' , fontsize=26)
    plt.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    ##f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/Attractor_fig5.png')
    f.savefig(figure_path + 'Attractor_stable_fig5.png')

if Overplot_IC_Final:
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,9))
    f.subplots_adjust(hspace=0,wspace=0)
    for i in range(len(datalist)):
        data, label = datalist[i]
        ax1.plot( data[:,0], data[:,1],Symbols[i],color = Colors[i], label=label,lw=2,ms=7 )
    for i in range(len(datalist_2)):
        data, label = datalist_2[i]
        ax1.plot( data[:,4], data[:,5],Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7)
    x = np.linspace(0,1.1)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') # Forbidden region. Restriction: r'$\beta > -\frac{\gamma }{2}$' by An & Evans 2006. Ciotto et Al.
    ax1.set_title(r'IC and Final',fontsize=20)
    ax1.set_ylabel(r'$\gamma$',fontsize=24)
    ax1.set_xlim(-0.1,1.1)
    ax1.set_ylim(-4.,0.)
    ax1.axes.get_xaxis().set_visible(False)

    for i in range(len(datalist)):
        data, label = datalist[i]
        ax2.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i],  label=label,lw=2,ms=7 )
    for i in range(len(datalist_2)):
        data, label = datalist_2[i]
        ax2.plot( data[:,4], data[:,6],Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7 )
    ax2.set_xlabel(r'$\beta$',fontsize=24)
    ax2.set_ylabel(r'$\kappa$',fontsize=24)
    ax2.set_xlim(-0.1,1.1)
    ax2.set_ylim(-2.,2.)
    leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=2,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(0.5)
    ##f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/Attractor_fig1.png')
    f.savefig(figure_path + 'Attractor_stable_fig1.png')

if IC_Final_4_subplots:
    f, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    for i in range(len(datalist)):
        data, label = datalist[i]
        ax1.plot( data[:,0], data[:,1],Symbols[i],color = Colors[i], label=label,lw=2,ms=7 )
    x = np.linspace(0,1.1)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'IC',fontsize=20)
    ax1.set_ylabel(r'$\gamma$',fontsize=24)
    ax1.set_xlim(-0.1,1.1)
    ax1.set_ylim(-6.,0.)
    ax1.axes.get_xaxis().set_visible(False)
    
    for i in range(len(datalist_2)):
        data, label = datalist_2[i]
        ax2.plot( data[:,4], data[:,5],Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7)
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax2.set_title(r'Final',fontsize=20)
    ax2.set_xlim(-0.1,1.1)
    ax2.set_ylim(-6.,0.)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)
 
    for i in range(len(datalist)):
        data, label = datalist[i]
        ax3.plot( data[:,0], data[:,2],Symbols[i],color = Colors[i],  label=label,lw=2,ms=7 )
    ax3.set_xlabel(r'$\beta$',fontsize=24)
    ax3.set_ylabel(r'$\kappa$',fontsize=24)
    ax3.set_xlim(-0.1,1.1)
    ax3.set_ylim(-5.,2.)
    ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
   
    for i in range(len(datalist_2)):
        data, label = datalist_2[i]
        ax4.plot( data[:,4], data[:,6],Symbols[i], color=Colors2[i],label=label ,lw=2,ms=7 )  
    ax4.set_xlim(-0.1,1.1)
    ax4.set_ylim(-5.,2.)
    ax4.legend(prop=dict(size=13), numpoints=2, ncol=2,frameon=True,loc=0,handlelength=2.5)
    ax4.axes.get_yaxis().set_visible(False)
    ##f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/Attractor_fig2.png')
    f.savefig(figure_path + 'Attractor_stable_fig2.png')

if beta_vs_gamma_BCS4CS5CS6DS1D2E_Rlimit32_Run_5_10:
    f, (ax1, ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # Snapshot 5
    # Soft_B
    data, label = datalist_Soft_B_Rlimit32_50bins_Run_5_10[0]
    label       = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins_Run_5_10[0]
    label       = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    
    data, label = datalist_CS5_Rlimit32_20bins_Run_5_10[0]
    label       = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    
    data, label = datalist_CS6_Rlimit32_20bins_Run_5_10[0]
    label       = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    
    data, label = datalist_DS1_Rlimit32_20bins_Run_5_10[0]
    label       = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    
    data, label = datalist_Soft_D2_Rlimit32_20bins_Run_5_10[0]
    label       = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    
    data, label = datalist_E_Rlimit32_50bins_Run_5_10[0]
    label       = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$',lw=2,ms=7)
    ax1.fill_between(x,0,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'FileNo 5 ($II: \Delta E , R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$' ,fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-7.,0.)

    # Snapshot 10    
    data, label = datalist_Soft_B_Rlimit32_50bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    
    data, label = datalist_CS4_Rlimit32_20bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    
    data, label = datalist_CS5_Rlimit32_20bins_Run_5_10[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    
    data, label = datalist_CS6_Rlimit32_20bins_Run_5_10[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    
    data, label = datalist_DS1_Rlimit32_20bins_Run_5_10[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    
    data, label = datalist_Soft_D2_Rlimit32_20bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    
    data, label = datalist_E_Rlimit32_50bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    
    # Martin Final
    data, label = datalist_Martin_Final[0]
    ax2.plot(data[:,4],data[:,5],Symbols[8],color=Colors2[2],label=label[:]+'_Sparre',lw=2,ms=7)
    
    ax2.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7)
    ax2.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$'                  ,fontsize=30)
    ax2.set_title(r'FileNo 10 (without cuts)',fontsize=30)
    ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-7.,0.)
    ax2.yaxis.tick_right()
    
    #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/beta_vs_gamma_BCS4CS5CS6DS1D2E_Rlimit32_Run_5_10.png')
    f.savefig(figure_path + 'beta_vs_gamma_BCS4CS5CS6DS1D2E_Rlimit32_Run_5_10.png')

if beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit32_Run_5_10:
    f, (ax1, ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # Snapshot 5
    data, label = datalist_Soft_B_Rlimit32_50bins_Run_5_10[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    data, label = datalist_CS4_Rlimit32_20bins_Run_5_10[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    data, label = datalist_CS5_Rlimit32_20bins_Run_5_10[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    data, label = datalist_CS6_Rlimit32_20bins_Run_5_10[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    data, label = datalist_DS1_Rlimit32_20bins_Run_5_10[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_Rlimit32_20bins_Run_5_10[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_Rlimit32_50bins_Run_5_10[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'FileNo 5 ($II: \Delta E , R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$'          ,fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-7.,0.)

    # Snapshot 10    
    data, label = datalist_Soft_B_Rlimit32_50bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    data, label = datalist_CS4_Rlimit32_20bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    data, label = datalist_CS5_Rlimit32_20bins_Run_5_10[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    data, label = datalist_CS6_Rlimit32_20bins_Run_5_10[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    data, label = datalist_DS1_Rlimit32_20bins_Run_5_10[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_Rlimit32_20bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_Rlimit32_50bins_Run_5_10[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    
    # Martin Final
    data, label = datalist_Martin_Final[0]
    ax2.plot(data[:,4],data[:,5]+data[:,6],Symbols[8],color=Colors2[2],label=label[:]+'_Sparre',lw=2,ms=7)
    
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot( x, -5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7 )
    leg = ax2.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$'                  ,fontsize=30)
    ax2.set_title(r'FileNo 10 (without cuts)',fontsize=30)
    ax2.set_xlim(-.5,1.)
    ax2.set_ylim(-7.,0.)
    ax2.yaxis.tick_right()
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit32_Run_5_10.png')

if beta_vs_gamma_D2_Time_evolution_Rlimit32:
    f,(ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    # D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label       = label[len(text_files_path)+5:-38]
    ax1.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label + '_IC',lw=2,ms=7)
    
    data, label = datalist_Soft_D2_Rlimit32_20bins[1]
    label       = label[len(text_files_path)+5:-38]
    ax1.plot(data[:,1],data[:,2],Symbols[1],color=Colors[1],label=label + '10_005',lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[2]
    label       = label[len(text_files_path)+5:-38]
    ax1.plot(data[:,1],data[:,2],Symbols[2],color=Colors[2],label=label + '20_005',lw=2,ms=7)

    data, label = datalist_Soft_D2_Rlimit32_20bins[3]
    label       = label[len(text_files_path)+5:-38]
    ax1.plot(data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label + '30_005',lw=2,ms=7)    

    data, label = datalist_Soft_D2_Rlimit32_20bins[4]
    label       = label[len(text_files_path)+5:-38]
    ax1.plot(data[:,1],data[:,2],Symbols[4],color=Colors[4],label=label + 'Final',lw=2,ms=7) 
    
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$',lw=2,ms=7)
    ax1.fill_between(x,0,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$' ,fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-4.,0.)
    
    f.savefig(figure_path + 'beta_vs_gamma_D2_Time_evolution_Rlimit32.png')

if beta_vs_gamma_CS4_Time_evolution_Rlimit32:
    f,(ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label + '_IC',lw=2,ms=7)

    data, label = datalist_CS4_Rlimit32_20bins[1]
    label       = label[len(text_files_path):-38]
    ax1.plot(data[:,1],data[:,2],Symbols[1],color=Colors[1],label=label + '10_005',lw=2,ms=7)

    data, label = datalist_CS4_Rlimit32_20bins[2]
    label       = label[len(text_files_path):-38]
    ax1.plot(data[:,1],data[:,2],Symbols[2],color=Colors[2],label=label + '20_005',lw=2,ms=7)    

    data, label = datalist_CS4_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-38]
    ax1.plot(data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label + '30_005',lw=2,ms=7) 

    data, label = datalist_CS4_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-38]
    ax1.plot(data[:,1],data[:,2],Symbols[4],color=Colors[4],label=label + '40_021',lw=2,ms=7) 
    
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$',lw=2,ms=7)
    ax1.fill_between(x,0,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax1.set_title(r'IC ($IIa, R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$' ,fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-4.,0.)
    
    f.savefig(figure_path + 'beta_vs_gamma_CS4_Time_evolution_Rlimit32_IIa.png')

if beta_vs_gamma_DeltaG_DS1_Rlimit32:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    # DS1
    '''
    data, label = datalist_DS1_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    # DS1 Delta G
    data, label = datalist_DeltaG_DS1_Rlimit32_20bins[0]
    ax1.plot(data[:,1],data[:,2],Symbols[1],color=Colors[1],label=r'DS1 IC ($\Delta$G)',lw=2,ms=7)
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$',lw=2,ms=7)
    ax1.fill_between(x,0,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$' ,fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-4.,0.)

    # Final
    # DS1
    '''
    data, label = datalist_DS1_Rlimit32_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[0],color = Colors[0], label=label,lw=2,ms=7)
    '''
    # DS1 Delta G
    data, label = datalist_DeltaG_DS1_Rlimit32_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[1],color = Colors[1],label=r'DS1 Final ($\Delta$G)',lw=2,ms=7)
    # Martin Final
    data, label = datalist_Martin_Final[0]
    ax2.plot(data[:,4],data[:,5],Symbols[2],color=Colors2[2],label=label[:]+'_Sparre',lw=2,ms=7)
    
    ax2.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma}{2}$',lw=2,ms=7)
    ax2.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$',lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    ax2.set_title(r'Final'   ,fontsize=30)
    ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-4.,0.)
    ax2.yaxis.tick_right()

    # Control
    # DS1
    '''
    data,label = datalist_DS1_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    # DS1 Delta G
    data,label = datalist_DeltaG_DS1_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2],Symbols[1],color=Colors[1],label=r'DS1 control,Final ($\Delta$G)',lw=2,ms=7) 
    ax3.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma}{2}$' ,lw=2,ms=7)
    ax3.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax3.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7)
    ax3.set_xlabel(r'$\beta$',fontsize=30)
    ax3.set_title(r'Control' ,fontsize=30)
    ax3.set_xlim(-.2,1.)
    ax3.set_ylim(-4.,0.)
    ax3.yaxis.tick_right()
    f.savefig(figure_path + 'beta_vs_gamma_DeltaG_DS1_Rlimit32.png')

if beta_vs_gamma_plus_kappa_DS1D2_Rlimit32:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    '''
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2]+data[:,3],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2]+data[:,3],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2]+data[:,3],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2]+data[:,3],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2]+data[:,3],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$',lw=2,ms=7)
    ax1.fill_between(x,0,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.set_title(r'IC ($IIa, R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$' ,fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-4.,0.)

    # Final
    '''
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2]+data[:,3],Symbols[0],color = Colors[0], label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2]+data[:,3],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[3]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2]+data[:,3],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[4]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2]+data[:,3],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    '''
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2]+data[:,3],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    # Martin Final
    data, label = datalist_Martin_Final[0]
    ax2.plot(data[:,4],data[:,5]+data[:,6],Symbols[5],color=Colors2[5],label=label[:]+'_Sparre',lw=2,ms=7)
    
    ax2.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma}{2}$',lw=2,ms=7)
    ax2.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$',lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    ax2.set_title(r'Final'   ,fontsize=30)
    ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-4.,0.)
    ax2.yaxis.tick_right()

    # Control
    '''
    # CS4
    data,label = datalist_CS4_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2]+data[:,3],Symbols[0],color = Colors[0], label=label,lw=2,ms=7)
    # CS5
    data,label = datalist_CS5_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2]+data[:,3],Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS6
    data,label = datalist_CS6_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2]+data[:,3],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # DS1
    data,label = datalist_DS1_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2]+data[:,3],Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    '''
    # Soft_D2
    data,label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label      = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2]+data[:,3],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)

    ax3.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma}{2}$' ,lw=2,ms=7)
    ax3.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax3.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7)
    ax3.set_xlabel(r'$\beta$',fontsize=30)
    ax3.set_title(r'Control' ,fontsize=30)
    ax3.set_xlim(-.2,1.)
    ax3.set_ylim(-4.,0.)
    ax3.yaxis.tick_right()
    
    #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/beta_vs_gamma_BCS1CS4CS5CS6DS1D2E_Rlimit10_20_bins.png')
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_CS4CS5CS6DS1D2_Rlimit32.png')

if beta_vs_gamma_CS4CS5CS6_Rlimit32:
    f,(ax1,ax2,ax3,ax4) = plt.subplots(1,4,figsize=(15,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    '''
    # Soft_B
    data, label = datalist_Soft_B_Rlimit32_50bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    # E
    data, label = datalist_E_Rlimit32_50bins[0]
    label       = label[len(text_files_path):-38]
    ax1.plot( data[:,1],data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    '''
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$',lw=2,ms=7)
    ax1.fill_between(x,0,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    #leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    #leg.get_frame().set_alpha(.5)
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$' ,fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-4.,0.)

    # File 10
    '''
    # Soft_B
    data, label = datalist_Soft_B_Rlimit32_50bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    # E
    data, label = datalist_E_Rlimit32_50bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    '''
    # Martin Final
    data, label = datalist_Martin_Final[0]
    ax2.plot(data[:,4],data[:,5],Symbols[8],color=Colors2[2],label=label[:]+'_Sparre',lw=2,ms=7)
    
    ax2.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7)
    ax2.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7)
    leg = ax2.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    ax2.set_title(r'10th. files'   ,fontsize=30)
    ax2.set_xlim(-.2,1.)
    ax2.set_ylim(-4.,0.)
    ax2.yaxis.tick_right()

    # Final
    '''
    # Soft_B
    data, label = datalist_Soft_B_Rlimit32_50bins[2]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    # CS4
    data, label = datalist_CS4_Rlimit32_20bins[2]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    # DS1
    data, label = datalist_DS1_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_Rlimit32_20bins[2]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    # E
    data, label = datalist_E_Rlimit32_50bins[2]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    '''
    # Martin Final
    data, label = datalist_Martin_Final[0]
    ax3.plot(data[:,4],data[:,5],Symbols[8],color=Colors2[2],label=label[:]+'_Sparre',lw=2,ms=7)
    
    ax3.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma}{2}$',lw=2,ms=7)
    ax3.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax3.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$',lw=2,ms=7)
    #leg = ax3.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    #leg.get_frame().set_alpha(.5)
    ax3.set_xlabel(r'$\beta$',fontsize=30)
    ax3.set_title(r'Final'   ,fontsize=30)
    ax3.set_xlim(-.2,1.)
    ax3.set_ylim(-4.,0.)
    ax3.yaxis.tick_right()

    # Control
    '''
    # Soft_B control
    data, label = datalist_Soft_B_control_Rlimit32_50bins[0]
    label       = label[len(text_files_path):-39]
    ax4.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    # CS4
    data, label = datalist_CS4_control_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-39]
    ax4.plot(data[:,1],data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    # CS5
    data, label = datalist_CS5_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax4.plot(data[:,1],data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    # CS6
    data, label = datalist_CS6_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax4.plot(data[:,1],data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    # DS1
    data, label = datalist_DS1_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax4.plot(data[:,1],data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    # Soft_D2
    data, label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-39]
    ax4.plot(data[:,1],data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    # E
    data, label = datalist_E_control_Rlimit32_50bins[0]
    label       = label[len(text_files_path):-39]
    ax4.plot(data[:,1],data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    '''
    ax4.plot(x,y,color='Pink',label=r'$\beta=-\frac{\gamma}{2}$' ,lw=2,ms=7)
    ax4.fill_between(x,5,y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax4.plot(x,-5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7)
    #leg = ax4.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    #leg.get_frame().set_alpha(.5)
    ax4.set_xlabel(r'$\beta$',fontsize=30)
    ax4.set_title(r'Control' ,fontsize=30)
    ax4.set_xlim(-.2,1.)
    ax4.set_ylim(-4.,0.)
    ax4.yaxis.tick_right()
    
    #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/beta_vs_gamma_BCS1CS4CS5CS6DS1D2E_Rlimit10_20_bins.png')
    f.savefig(figure_path + 'beta_vs_gamma_CS4CS5CS6_Rlimit32.png')

if beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit32:
    f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    '''
    data, label = datalist_Soft_B_Rlimit32_50bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    data, label = datalist_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color=Colors[1],label=label,lw=2,ms=7)
    data, label = datalist_CS5_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color=Colors[2],label=label,lw=2,ms=7)
    data, label = datalist_CS6_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    data, label = datalist_DS1_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[4],color=Colors[4],label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_Rlimit32_50bins[0]
    label = label[len(text_files_path):-38]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    '''
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    #leg = ax1.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    #leg.get_frame().set_alpha(.5)
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 32$)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-6.,0.)

    # Final
    '''
    data, label = datalist_Soft_B_Rlimit32_50bins[2]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    data, label = datalist_CS4_Rlimit32_20bins[2]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    data, label = datalist_CS5_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    data, label = datalist_CS6_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    data, label = datalist_DS1_Rlimit32_20bins[2]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_Rlimit32_20bins[2]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_Rlimit32_50bins[2]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    '''
    # Martin Final
    data, label = datalist_Martin_Final[0]
    ax2.plot(data[:,4],data[:,5]+data[:,6],Symbols[8],color=Colors2[2],label=label[:]+'_Sparre',lw=2,ms=7)
    
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot( x, -5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7 )
    leg = ax2.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    ax2.set_title(r'Final'   ,fontsize=30)
    ax2.set_xlim(-.5,1.)
    ax2.set_ylim(-6.,0.)
    ax2.yaxis.tick_right()

    # Control
    '''
    data, label = datalist_Soft_B_control_Rlimit32_50bins[0]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,3]+data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    '''
    data, label = datalist_CS4_control_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    data, label = datalist_CS5_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,3]+data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    data, label = datalist_CS6_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,3]+data[:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    '''
    data, label = datalist_DS1_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-39]
    ax3.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,3]+data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_control_Rlimit32_50bins[0]
    label       = label[len(text_files_path):-39]
    ax3.plot(data[:,1],data[:,3]+data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    '''
    ax3.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax3.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax3.plot( x, -5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7 )
    #leg = ax3.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    #leg.get_frame().set_alpha(.5)
    ax3.set_xlabel(r'$\beta$',fontsize=30)
    ax3.set_title(r'Control' ,fontsize=30)
    ax3.set_xlim(-.5,1.)
    ax3.set_ylim(-6.,0.)
    ax3.yaxis.tick_right()
    
    # f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_BCS1CS4CS5CS6DS1D2E_Rlimit10_20_bins.png')
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_BCS1CS4CS5CS6DS1D2E_Rlimit32.png')

if beta_vs_gamma_BCS4CS5CS6DS1D2E_Rlimit10_20_bins:
    f, (ax1, ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    data, label = datalist_Soft_B_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[0],color = Colors[0], label=label,lw=2,ms=7 )
    data, label = datalist_CS4_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[1],color = Colors[1], label=label,lw=2,ms=7 )
    data, label = datalist_CS5_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7 )
    data, label = datalist_CS6_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[3],color = Colors[3], label=label,lw=2,ms=7 )
    data, label = datalist_DS1_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[4],color = Colors[4], label=label,lw=2,ms=7 )
    data, label = datalist_Soft_D2_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[5],color = Colors[5], label=label,lw=2,ms=7 )
    data, label = datalist_E_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1],data[:,2],Symbols[6],color = Colors[6], label=label,lw=2,ms=7 )
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 10, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-4.,0.)

    # Final
    data, label = datalist_Soft_B_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    data, label = datalist_CS4_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    data, label = datalist_CS5_Rlimit10_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    data, label = datalist_CS6_Rlimit10_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[2:,1],data[2:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    data, label = datalist_DS1_Rlimit10_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot( x, -5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7 )
    leg = ax2.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    ax2.set_title(r'Final (without cuts)',fontsize=30)
    ax2.set_xlim(-1.,1.)
    ax2.set_ylim(-7.,2.)
    ax2.yaxis.tick_right()
    #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/beta_vs_gamma_BCS1CS4CS5CS6DS1D2E_Rlimit10_20_bins.png')
    f.savefig(figure_path + 'beta_vs_gamma_BCS1CS4CS5CS6DS1D2E_Rlimit10_20_bins.png')

if beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit10_20_bins:
    f, (ax1, ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    data, label = datalist_Soft_B_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[0],color = Colors[0], label=label,lw=2,ms=7 )
    data, label = datalist_CS4_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7 )
    data, label = datalist_CS5_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[2],color = Colors[2], label=label,lw=2,ms=7 )
    data, label = datalist_CS6_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[3],color = Colors[3], label=label,lw=2,ms=7 )
    data, label = datalist_DS1_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7 )
    data, label = datalist_Soft_D2_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[5],color = Colors[5], label=label,lw=2,ms=7 )
    data, label = datalist_E_Rlimit10_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[6],color = Colors[6], label=label,lw=2,ms=7 )
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 10, 20$ bins)',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-5.,0.)

    # Final
    data, label = datalist_Soft_B_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    data, label = datalist_CS4_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    data, label = datalist_CS5_Rlimit10_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    data, label = datalist_CS6_Rlimit10_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[2:,1],data[2:,3]+data[2:,2],Symbols[3],color=Colors[3],label=label,lw=2,ms=7)
    data, label = datalist_DS1_Rlimit10_20bins[1]
    label = label[len(text_files_path):-39]
    ax2.plot(data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_Rlimit10_20bins[1]
    label       = label[len(text_files_path):-39]
    ax2.plot(data[:,1],data[:,3]+data[:,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot( x, -5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7 )
    leg = ax2.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    ax2.set_title(r'Final (without cuts)',fontsize=30)
    ax2.set_xlim(-1.,1.)
    ax2.set_ylim(-10.,4.)
    ax2.yaxis.tick_right()
    #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/beta_vs_gamma_plus_kappa_BCS1CS4CS5CS6DS1D2E_Rlimit10_20_bins.png')
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_BCS1CS4CS5CS6DS1D2E_Rlimit10_20_bins.png')

if beta_vs_gamma_plus_kappa_BCS4CS5CS6DS1D2E_Rlimit10000_20_bins:
    f, (ax1, ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)
    # IC
    data, label = datalist_Soft_B_Rlimit10000_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[0],color = Colors[0], label=label,lw=2,ms=7 )
    data, label = datalist_CS4_Rlimit10000_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7 )
    data, label = datalist_CS5_Rlimit10000_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[2],color = Colors[2], label=label,lw=2,ms=7 )
    data, label = datalist_CS6_Rlimit10000_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[3],color = Colors[3], label=label,lw=2,ms=7 )
    data, label = datalist_DS1_Rlimit10000_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7 )
    data, label = datalist_Soft_D2_Rlimit10000_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[5],color = Colors[5], label=label,lw=2,ms=7 )
    data, label = datalist_E_Rlimit10000_20bins[0]
    label = label[len(text_files_path):-41]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[6],color = Colors[6], label=label,lw=2,ms=7 )
    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 0, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 10^4, 20$ bins)',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.5,1.)
    ax1.set_ylim(-10.,0.)
    #leg = ax1.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    #leg.get_frame().set_alpha(.5)
    #ax1.axes.get_xaxis().set_visible(False)

    # Final
    data, label = datalist_Soft_B_Rlimit10000_20bins[1]
    label       = label[len(text_files_path):-42]
    ax2.plot(data[13:-15,1],data[13:-15,3]+data[13:-15,2],Symbols[0],color=Colors[0],label=label,lw=2,ms=7)
    data, label = datalist_CS4_Rlimit10000_20bins[1]
    label       = label[len(text_files_path):-42]
    ax2.plot(data[11:-19,1], data[11:-19,3] + data[11:-19,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7)
    data, label = datalist_CS5_Rlimit10000_20bins[1]
    label = label[len(text_files_path):-42]
    ax2.plot(data[12:-16,1], data[12:-16,3] + data[12:-16,2] ,Symbols[2],color = Colors[2], label=label,lw=2,ms=7)
    data, label = datalist_CS6_Rlimit10000_20bins[1]
    label = label[len(text_files_path):-42]
    ax2.plot(data[12:-17,1], data[12:-17,3] + data[12:-17,2] ,Symbols[3],color = Colors[3], label=label,lw=2,ms=7)
    data, label = datalist_DS1_Rlimit10000_20bins[1]
    label = label[len(text_files_path):-42]
    ax2.plot(data[10:-22,1], data[10:-22,3] + data[10:-22,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7)
    data, label = datalist_Soft_D2_Rlimit10000_20bins[1]
    label       = label[len(text_files_path):-42]
    ax2.plot(data[9:-16,1],data[9:-16,3]+data[9:-16,2],Symbols[5],color=Colors[5],label=label,lw=2,ms=7)
    data, label = datalist_E_Rlimit10000_20bins[1]
    label       = label[len(text_files_path):-42]
    ax2.plot(data[13:-16,1],data[13:-16,3]+data[13:-16,2],Symbols[6],color=Colors[6],label=label,lw=2,ms=7)
    
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot( x, -5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7 )
    leg = ax2.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    #ax2.set_ylabel(r'Final',fontsize=30)
    ax2.set_title(r'Final (with cuts)',fontsize=30)
    ax2.set_xlim(-.6,0.)
    ax2.set_ylim(-5.,0.)
    #ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
    ax2.yaxis.tick_right()
    #ax2.yaxis.set_label_position("right")
    #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/beta_vs_gamma_plus_kappa_BCS1CS4CS5CS6DS1D2E_Rlimit10000_20_bins.png')
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_BCS1CS4CS5CS6DS1D2E_Rlimit10000_20_bins.png')

if beta_vs_gamma_plus_kappa:
    f, (ax1, ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    # IC
    data, label = datalist_CS4[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7 )
    
    data, label = datalist_CS5[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[2],color = Colors[2], label=label,lw=2,ms=7 )
    
    data, label = datalist_CS6[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[3],color = Colors[3], label=label,lw=2,ms=7 )
    
    data, label = datalist_DS1[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7 )
    
    data, label = datalist_Soft_D2[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[5],color = Colors[5], label=label,lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'IC ($II: \Delta E , R_{limit} = 500, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.5,1.)
    ax1.set_ylim(-10.,1.)
    #leg = ax1.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    #leg.get_frame().set_alpha(.5)
    #ax1.axes.get_xaxis().set_visible(False)

    # Final
    data, label = datalist_CS4[1]
    label       = label[len(text_files_path):-13]
    ax2.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[1],color = Colors[1], label=label,lw=2,ms=7 )
    
    data, label = datalist_CS5[1]
    label = label[len(text_files_path):-13]
    ax2.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[2],color = Colors[2], label=label,lw=2,ms=7 )
    
    data, label = datalist_CS6[1]
    label = label[len(text_files_path):-13]
    ax2.plot( data[2:,1], data[2:,3] + data[2:,2] ,Symbols[3],color = Colors[3], label=label,lw=2,ms=7 )
    
    data, label = datalist_DS1[1]
    label = label[len(text_files_path):-13]
    ax2.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[4],color = Colors[4], label=label,lw=2,ms=7 )

    data, label = datalist_Soft_D2[1]
    label       = label[len(text_files_path):-13]
    ax2.plot( data[:,1], data[:,3] + data[:,2] ,Symbols[5],color = Colors[5], label=label,lw=2,ms=7 )
    
    ax2.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax2.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$')
    ax2.plot( x, -5*x-.8, color='black',label=r'$\beta=-0.2(\gamma+0.8)$' ,lw=2,ms=7 )
    leg = ax2.legend(prop=dict(size=16), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    ax2.set_xlabel(r'$\beta$',fontsize=30)
    #ax2.set_ylabel(r'Final',fontsize=30)
    ax2.set_xlim(-3.,1.)
    ax2.set_ylim(-15.,5.)
    ax2.set_title(r'Final',fontsize=30)
    ax2.yaxis.tick_right()
    #f.savefig('/Users/gustav.c.rasmussen/Desktop/Thesis/Attractor_fig3.png')
    f.savefig(figure_path + 'Attractor_stable_fig3.png')

'''
if Fig_beta_gamma_logr_IC_Final_panel:
    f, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    if B:                    
        f.savefig(figure_path + 'B_beta_gamma_logr_IC_Final_panel.png')
    if B_control:
        f.savefig(figure_path + 'B_control_beta_gamma_logr_IC_Final_panel.png')

    if CS1:
        data, label = datalist_C1[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC (%s)' %label , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        ax1.set_xlim(-1.5,2.)
        
        data, label = datalist_C1[1]
        label = label[len(text_files_path):]
        ax2.set_title('Final (%s)' %label , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        ax2.set_xlim(-1.,3.)
        
        data, label = datalist_C1[0]
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$')  
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.grid()
        ax3.set_xlim(-1.5,2.)

        data, label = datalist_C1[1] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        ax4.set_xlim(-1.
        #f.savefig(figure_path + 'CS1_beta_gamma_logr_IC_Final_panel.png')

    if CS1_control:
        data, label = datalist_C1_control[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        ax1.set_xlim(-1.5,2.)
        
        data, label = datalist_C1_control[1]
        label = label[len(text_files_path):]
        ax2.set_title('Final (%s)' %label , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        ax2.set_xlim(-1.5,2.5)
        
        data, label = datalist_C1_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.grid()
        ax3.set_xlim(-1.5,2.)

        data, label = datalist_C1_control[1] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        ax4.set_xlim(-1.5,2.5)
        f.savefig(figure_path + 'CS1_control_beta_gamma_logr_IC_Final_panel.png')
       
    if CS4:
        data, label = datalist_C4[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC (%s)' %label , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        ax1.set_xlim(-1.5,2.)

        data, label = datalist_C4[1]
        label = label[len(text_files_path):]
        ax2.set_title('Final (%s)' %label , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        ax2.set_xlim(-1.,3.)
        
        data, label = datalist_C4[0]
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$')  
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.grid()
        ax3.set_xlim(-1.5,2.)

        data, label = datalist_C4[1] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        ax4.set_xlim(-1.,3.)
        f.savefig(figure_path + 'CS4_beta_gamma_logr_IC_Final_panel.png')

    if CS4_control:
        data, label = datalist_CS4_control[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC', fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        ax1.set_xlim(-1.5,2.)
        data, label = datalist_CS4_control[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_CS4_control[2]
        label = label[len(text_files_path):]
        ax2.set_title('Final', fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        ax2.set_xlim(-1.5,2.5)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_CS4_control[0] 
        ax3.set_xlabel(r'$\log$ r' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.grid()
        ax3.set_xlim(-1.5,2.)
        data, label = datalist_CS4_control[1] 
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=r'$\beta$') 

        data, label = datalist_CS4_control[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        ax4.set_xlim(-1.5,2.5)
        f.savefig(figure_path + 'CS4_control_beta_gamma_logr_IC_Final_panel.png')

    if CS5:                    
        f.savefig(figure_path + 'CS5_beta_gamma_logr_IC_Final_panel.png')
    if CS5_control:
        f.savefig(figure_path + 'CS5_control_beta_gamma_logr_IC_Final_panel.png')

    if CS6:                    
        f.savefig(figure_path + 'CS6_beta_gamma_logr_IC_Final_panel.png')
    if CS6_control:
        f.savefig(figure_path + 'CS6_control_beta_gamma_logr_IC_Final_panel.png')

    if DS1:                    
        f.savefig(figure_path + 'DS1_beta_gamma_logr_IC_Final_panel.png')
    if DS1_control:
        f.savefig(figure_path + 'DS1_control_beta_gamma_logr_IC_Final_panel.png')

    if D2:                    
        f.savefig(figure_path + 'D2_beta_gamma_logr_IC_Final_panel.png')
    if D2_control:
        f.savefig(figure_path + 'D2_control_beta_gamma_logr_IC_Final_panel.png')

    if E:                    
        f.savefig(figure_path + 'E_beta_gamma_logr_IC_Final_panel.png')
    if E_control:
        f.savefig(figure_path + 'E_control_beta_gamma_logr_IC_Final_panel.png')
                     
    if mass_bins_B:
        data, label = datalist_mass_bins_B[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('ICs ' , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_B[1]
        label       = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_B[2]
        label       = label[len(text_files_path):]
        ax2.set_title('Final', fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax2.set_xlim(-.1,.8)
        
        data, label = datalist_mass_bins_B[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_B[1]
        label       = label[len(text_files_path):]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_B[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.1,.8)
        f.savefig(figure_path + 'mass_bins_B_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_B_control:
        data, label = datalist_mass_bins_B_control[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC' , fontsize=18) 
        #ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_B_control[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        #ax1.set_xlim(-.5,1.4)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_B_control[2]
        label = label[len(text_files_path):]
        ax2.set_title('Final' , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        #ax2.set_xlim(-.4,1.4)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_B_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_B_control[1]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=r'$\beta$') 
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_B_control[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.4,1.4)
        f.savefig(figure_path + 'mass_bins_B_control_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_CS1:
        data, label = datalist_mass_bins_C1[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC (%s)' %label , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_C1[1]
        label       = label[len(text_files_path):]
        ax2.set_title('Final (%s)' %label , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        ax2.set_xlim(-.1,.8)

        data, label = datalist_mass_bins_C1[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.grid()
        ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C1[1] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        ax4.set_xlim(-.1,.8)
        f.savefig(figure_path + 'mass_bins_CS1_beta_gamma_logr_IC_Final_panel.png')
    
    if mass_bins_CS1_control:
        data, label = datalist_mass_bins_C1_control[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_C1_control[1]
        label       = label[len(text_files_path):]
        ax2.set_title('Final (%s)' %label , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        ax2.set_xlim(-.4,1.4)
        
        data, label = datalist_mass_bins_C1_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.grid()
        ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C1_control[1] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        ax4.set_xlim(-.4,1.4)
        f.savefig(figure_path + 'mass_bins_CS1_control_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_CS4:
        data, label = datalist_mass_bins_C4[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('ICs ' , fontsize=18)
        #ax1.set_title('IC (%s)' %label , fontsize=18)
        #ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_C4[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=2,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_C4[2]
        label       = label[len(text_files_path):]
        ax2.set_title('Final (%s)' %label , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\gamma$')
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        #ax2.set_xlim(-.1,.8)

        data, label = datalist_mass_bins_C4[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C4[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.1,.8)
        f.savefig(figure_path + 'mass_bins_CS4_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_CS4_control:
        data, label = datalist_mass_bins_C4_control[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC' , fontsize=18) 
        #ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_C4_control[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        #ax1.set_xlim(-.5,1.4)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_C4_control[2]
        label = label[len(text_files_path):]
        ax2.set_title('Final' , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        #ax2.set_xlim(-.4,1.4)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_C4_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_C4_control[1]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=r'$\beta$') 
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C4_control[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.4,1.4)
        f.savefig(figure_path + 'mass_bins_CS4_control_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_CS5:
        data, label = datalist_mass_bins_C5[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('ICs ' , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_C5[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_C5[2]
        label = label[len(text_files_path):]
        ax2.set_title('Final', fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax2.set_xlim(-.1,.8)
        
        data, label = datalist_mass_bins_C5[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_C5[1]
        label = label[len(text_files_path):]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C5[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.1,.8)
        f.savefig(figure_path + 'mass_bins_CS5_beta_gamma_logr_IC_Final_panel.png')
    
    if mass_bins_CS5_control:
        data, label = datalist_mass_bins_C5_control[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC' , fontsize=18) 
        #ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_C5_control[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        #ax1.set_xlim(-.5,1.4)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_C5_control[2]
        label       = label[len(text_files_path):]
        ax2.set_title('Final' , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        #ax2.set_xlim(-.4,1.4)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_C5_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_C5_control[1]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=r'$\beta$') 
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C5_control[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.4,1.4)
        f.savefig(figure_path + 'mass_bins_CS5_control_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_CS6:        
        data, label = datalist_mass_bins_C6[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('ICs ' , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_C6[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_C6[2]
        label = label[len(text_files_path):]
        ax2.set_title('Final', fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax2.set_xlim(-.1,.8)
        
        data, label = datalist_mass_bins_C6[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_C6[1]
        label = label[len(text_files_path):]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C6[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.1,.8)
        f.savefig(figure_path + 'mass_bins_CS6_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_CS6_control:
        data, label = datalist_mass_bins_C6_control[0]
        label = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC' , fontsize=18) 
        #ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_C6_control[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        #ax1.set_xlim(-.5,1.4)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_C6_control[2]
        label = label[len(text_files_path):]
        ax2.set_title('Final' , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        #ax2.set_xlim(-.4,1.4)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_C6_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_C6_control[1]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=r'$\beta$') 
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_C6_control[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.4,1.4)
        f.savefig(figure_path + 'mass_bins_CS6_control_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_DS1:
        data, label = datalist_mass_bins_D1[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('ICs ' , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_D1[1]
        label       = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_D1[2]
        label       = label[len(text_files_path):]
        ax2.set_title('Final', fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax2.set_xlim(-.1,.8)
        
        data, label = datalist_mass_bins_D1[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_D1[1]
        label       = label[len(text_files_path):]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_D1[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.1,.8)
        f.savefig(figure_path + 'mass_bins_DS1_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_DS1_control:
        data, label = datalist_mass_bins_D1_control[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC' , fontsize=18) 
        #ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_D1_control[1]
        label       = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        #ax1.set_xlim(-.5,1.4)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_D1_control[2]
        label       = label[len(text_files_path):]
        ax2.set_title('Final' , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        #ax2.set_xlim(-.4,1.4)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_D1_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_D1_control[1]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=r'$\beta$') 
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)
        #ax3.set_ylim(-.5,1.)

        data, label = datalist_mass_bins_D1_control[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.4,1.4)
        #ax4.set_ylim(-.5,1.)
        f.savefig(figure_path + 'mass_bins_DS1_control_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_D2:
        data, label = datalist_mass_bins_D2[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('ICs ' , fontsize=18)
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        data, label = datalist_mass_bins_D2[1]
        label = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax1.set_xlim(-.5,1.4)
        
        data, label = datalist_mass_bins_D2[2]
        label       = label[len(text_files_path):]
        ax2.set_title('Final', fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        #ax2.set_xlim(-.1,.8)
        
        data, label = datalist_mass_bins_D2[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax3.set_ylim(-.5,1.)
        data, label = datalist_mass_bins_D2[1]
        label       = label[len(text_files_path):]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)

        data, label = datalist_mass_bins_D2[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.1,.8)
        ax4.set_ylim(-.5,1.)
        f.savefig(figure_path + 'mass_bins_D2_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_D2_control:
        data, label = datalist_mass_bins_D2_control[0]
        label       = label[len(text_files_path):]
        ax1.set_ylabel(r'$\gamma$' , fontsize=20)
        ax1.set_title('IC' , fontsize=18) 
        #ax1.set_title('IC (%s)' %label , fontsize=18) 
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        tt = np.linspace(-1,2,15)
        ax1.plot(tt,-1-3*10.0**tt/(1+10.0**tt),'--',color='orange')
        #ax1.plot(tt,1/tt**3*(-1/(1+tt)**6-3/(1+tt)**5),'--',color='orange')
        data, label = datalist_mass_bins_D2_control[1]
        label       = label[len(text_files_path):]
        ax1.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='blue',label=label)
        ax1.grid()
        ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
        #ax1.set_xlim(-.5,1.4)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_D2_control[2]
        label       = label[len(text_files_path):]
        ax2.set_title('Final' , fontsize=18) 
        ax2.plot(data[:,0],data[:,2],'-o',ms=7,lw=2,mew=0,color='black',label=label)
        ax2.grid()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='on', left='off', labelleft='off')
        ax2.yaxis.tick_right()
        #ax2.set_xlim(-.4,1.4)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(0.5)
        
        data, label = datalist_mass_bins_D2_control[0] 
        ax3.set_xlabel(r'$\log$ r (kpc)' , fontsize=20)
        ax3.set_ylabel(r'$\beta$' , fontsize=20)
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax3.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        data, label = datalist_mass_bins_D2_control[1]
        ax3.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='blue',label=r'$\beta$') 
        ax3.grid()
        #ax3.set_xlim(-.5,1.4)
        ax3.set_ylim(-.5,1.)

        data, label = datalist_mass_bins_D2_control[2] 
        ax4.plot(data[:,0],data[:,1],'-o',ms=7,lw=2,mew=0,color='black',label=r'$\beta$') 
        ax4.plot(data[:,0],0*data[:,0],'--',lw=2,color='grey')
        ax4.grid()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off', labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.tick_right()
        #ax4.set_xlim(-.4,1.4)
        ax4.set_ylim(-.5,1.)
        f.savefig(figure_path + 'mass_bins_D2_control_beta_gamma_logr_IC_Final_panel.png')

    if mass_bins_E:
        f.savefig(figure_path + 'mass_bins_E_beta_gamma_logr_IC_Final_panel.png')
    if mass_bins_E_control:
        f.savefig(figure_path + 'mass_bins_E_control_beta_gamma_logr_IC_Final_panel.png')
'''

if beta_vs_gamma_plus_kappa_Test_CS4_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_Test_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'IC',lw=2,ms=7 )

    data, label = datalist_Test_CS4_Rlimit32_20bins[7]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'perturbation 4',lw=2,ms=7 )
    
    data, label = datalist_Test_CS4_Rlimit32_20bins[8]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'flow 4',lw=2,ms=7 )

    data, label = datalist_Test_CS4_Rlimit32_20bins[11]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color = Colors[3], label=r'perturbation 6',lw=2,ms=7 )
    
    data, label = datalist_Test_CS4_Rlimit32_20bins[12]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[4],color = Colors[4], label=r'flow 6',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'CS4 ($IIa Test, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.5,1.)
    ax1.set_ylim(-10.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_Test_CS4_Rlimit32.png')

if beta_vs_gamma_plus_kappa_Test_D2_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_Test_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'IC',lw=2,ms=7 )

    data, label = datalist_Test_D2_Rlimit32_20bins[7]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'perturbation 4',lw=2,ms=7 )
    
    data, label = datalist_Test_D2_Rlimit32_20bins[8]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'flow 4',lw=2,ms=7 )

    data, label = datalist_Test_D2_Rlimit32_20bins[11]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color = Colors[3], label=r'perturbation 6',lw=2,ms=7 )
    
    data, label = datalist_Test_D2_Rlimit32_20bins[12]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[4],color = Colors[4], label=r'flow 6',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'D2 ($IIa Test, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.5,1.)
    ax1.set_ylim(-10.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_Test_D2_Rlimit32.png')

if beta_vs_gamma_plus_kappa_Test_CS4_10tdyn_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_Test_CS4_10tdyn_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'IC',lw=2,ms=7 )

    data, label = datalist_Test_CS4_10tdyn_Rlimit32_20bins[1]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'1_041',lw=2,ms=7 )
    
    data, label = datalist_Test_CS4_10tdyn_Rlimit32_20bins[2]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'2_041',lw=2,ms=7 )

    data, label = datalist_Test_CS4_10tdyn_Rlimit32_20bins[3]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color = Colors[3], label=r'3_041',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'CS4 ($IIa Test, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.5,1.)
    ax1.set_ylim(-10.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_Test_CS4_10tdyn_Rlimit32.png')

if beta_vs_gamma_plus_kappa_IIb_CS4_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'0_005',lw=2,ms=7 )

    data, label = datalist_CS4_Rlimit32_20bins[1]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'20_021',lw=2,ms=7 )

    data, label = datalist_CS4_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'control final',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'$CS_4$ ($IIb, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.5,1.)
    ax1.set_ylim(-6.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_IIb_CS4_Rlimit32.png')

if beta_vs_gamma_plus_kappa_IIb_D2_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'0_005',lw=2,ms=7 )

    data, label = datalist_Soft_D2_Rlimit32_20bins[1]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'20_021',lw=2,ms=7 )
    
    data, label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'control final',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'$D_2$ ($IIb, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.5,.4)
    ax1.set_ylim(-6.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_IIb_D2_Rlimit32.png')

if beta_vs_gamma_plus_kappa_IIc_CS4_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'0_005',lw=2,ms=7 )

    data, label = datalist_CS4_Rlimit32_20bins[1]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'10_005',lw=2,ms=7 )

    data, label = datalist_CS4_Rlimit32_20bins[2]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'20_021',lw=2,ms=7 )

    data, label = datalist_CS4_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color = Colors[3], label=r'control final',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'$CS_4$ ($IIc, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-6.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_IIc_CS4_Rlimit32.png')

if beta_vs_gamma_plus_kappa_IIc_D2_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'0_005',lw=2,ms=7 )

    data, label = datalist_Soft_D2_Rlimit32_20bins[1]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'10_005',lw=2,ms=7 )

    data, label = datalist_Soft_D2_Rlimit32_20bins[2]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'20_021',lw=2,ms=7 )

    data, label = datalist_Soft_D2_Rlimit32_20bins[3]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color = Colors[3], label=r'30_021',lw=2,ms=7 )

    data, label = datalist_Soft_D2_Rlimit32_20bins[4]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[4],color = Colors[4], label=r'40_021',lw=2,ms=7 )
    
    data, label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[5],color = Colors[5], label=r'control final',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'$D_2$ ($IIc, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,.8)
    ax1.set_ylim(-6.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_IIc_D2_Rlimit32.png')

if beta_vs_gamma_plus_kappa_IId_CS4_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'0_005',lw=2,ms=7 )

    data, label = datalist_CS4_Rlimit32_20bins[1]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'20_013',lw=2,ms=7 )

    data, label = datalist_CS4_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'control final',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'$CS_4$ ($IId, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-6.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_IId_CS4_Rlimit32.png')

if beta_vs_gamma_plus_kappa_IId_D2_Rlimit32:
    f, (ax1) = plt.subplots(1,1,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'0_005',lw=2,ms=7 )

    data, label = datalist_Soft_D2_Rlimit32_20bins[1]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'20_013',lw=2,ms=7 )
    
    data, label = datalist_Soft_D2_control_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'control final',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'$\beta=-\frac{\gamma }{2}$' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    ax1.set_title(r'$D_2$ ($IId, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.1,.2)
    ax1.set_ylim(-6.,1.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    
    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_IId_D2_Rlimit32.png')

if beta_vs_gamma_plus_kappa_IIc_ABCS4CS5CS6DS1D2E_Rlimit32:
    f, (ax1,ax2) = plt.subplots(1,2,figsize=(13,11))
    f.subplots_adjust(hspace=0,wspace=0)

    data, label = datalist_CS4_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[0],color = Colors[0], label=r'$CS_4$',lw=2,ms=7 )
    data, label = datalist_CS5_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[1],color = Colors[1], label=r'$CS_5$',lw=2,ms=7 )
    data, label = datalist_CS6_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[2],color = Colors[2], label=r'$CS_6$',lw=2,ms=7 )
    data, label = datalist_DS1_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[3],color = Colors[3], label=r'$DS_1$',lw=2,ms=7 )
    data, label = datalist_Soft_D2_Rlimit32_20bins[0]
    label = label[len(text_files_path):-13]
    ax1.plot( data[:,1], data[:,3] + data[:,2],Symbols[4],color = Colors[4], label=r'$D_2$',lw=2,ms=7 )

    x = np.linspace(-4.,3.)
    y = -2*x
    ax1.plot( x, y, color='Pink',label=r'An & Evans' ,lw=2,ms=7 )
    ax1.fill_between(x, 5, y,color='Violet',label=r'$\beta > -\frac{\gamma }{2}$') 
    #ax1.set_title(r'($IIc, IC, R_{limit} = 32, 20$ bins)',fontsize=30)
    ax1.set_title(r'IC',fontsize=30)
    ax1.set_xlabel(r'$\beta$',fontsize=30)
    ax1.set_ylabel(r'$\gamma + \kappa$',fontsize=30)
    ax1.set_xlim(-.2,1.)
    ax1.set_ylim(-6.,0.)
    leg = ax1.legend(prop=dict(size=16),numpoints=2,ncol=1,fancybox=True,loc=0,handlelength=2.5)
    leg.get_frame().set_alpha(.5)

    data, label = datalist_CS4_Rlimit32_20bins[3]
    label = label[len(text_files_path):-13]
    ax2.plot(data[3:,1], data[3:,3] + data[3:,2],Symbols[0],color = Colors[0], label=r'40_021',lw=2,ms=7 )
    data, label = datalist_CS5_Rlimit32_20bins[2]
    label = label[len(text_files_path):-13]
    ax2.plot(data[3:,1], data[3:,3] + data[3:,2],Symbols[1],color = Colors[1], label=r'40_021',lw=2,ms=7 )
    data, label = datalist_CS6_Rlimit32_20bins[2]
    label = label[len(text_files_path):-13]
    ax2.plot(data[3:,1], data[3:,3] + data[3:,2],Symbols[2],color = Colors[2], label=r'40_021',lw=2,ms=7 )
    data, label = datalist_DS1_Rlimit32_20bins[2]
    label = label[len(text_files_path):-13]
    ax2.plot(data[3:,1], data[3:,3] + data[3:,2],Symbols[3],color = Colors[3], label=r'60_021',lw=2,ms=7 )
    data, label = datalist_Soft_D2_Rlimit32_20bins[5]
    label = label[len(text_files_path):-13]
    ax2.plot(data[3:,1], data[3:,3] + data[3:,2],Symbols[4],color = Colors[4], label=r'60_021',lw=2,ms=7 )

    x = np.linspace(-4., 3.)
    y = -2 * x
    ax2.plot(x, y, color='Pink', lw=2, ms=7)
    ax2.fill_between(x, 5, y, color='Violet')
    y = -5. * x - .8
    ax2.plot(x, y, color='k', label='Hansen-Moore relation', lw=2, ms=7)
    ax2.set_title(r'Final (IIc)', fontsize=30)
    ax2.set_xlabel(r'$\beta$', fontsize=30)
    ax2.set_xlim(-.2, 1.)
    ax2.set_ylim(-6., 0.)
    leg = ax2.legend(prop=dict(size=16), numpoints=2, ncol=1,
                     fancybox=True, loc=0, handlelength=2.5)
    leg.get_frame().set_alpha(.5)
    # ax2.tick_params(axis='both', which='both', bottom='on', top='off',
    #                 labelbottom='on', right='on', left='off', labelleft='off')
    ax2.yaxis.tick_right()

    f.savefig(figure_path + 'beta_vs_gamma_plus_kappa_IIc_ABCS4CS5CS6DS1D2E_Rlimit32.png')

plt.show()
