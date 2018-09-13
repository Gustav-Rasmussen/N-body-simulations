#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 21:36:43 2018

@author: gustavcollinrasmussen
"""

import numpy as np
import readVDF2FileLst as fls
import snapshotFiles

# Switches --------------------------------------------------------------------
Gamma_on = 1
Beta_on = 0

vRvPhivTheta = 0
vRvPhivThetaWithFit = 0
vT = 0
vTWithFit = 0
vRvPhivThetaDividedByGauss = 0
vTdividedByGauss = 0
GpertSameGammasAsICvR = 0
GpertDifferentGammasvT = 0
GpertGammas_1_5_vTdividedByGaussAndTsallis = 0
GpertGammas_2_0_vTdividedByGaussAndTsallis = 0
GpertGammas_2_5_vTdividedByGaussAndTsallis = 0
GpertGammas_3_0_vTdividedByGaussAndTsallis = 0
GpertRmiddle_19_95_vTdividedByGaussAndTsallis = 0
GpertRmiddle_31_62_vTdividedByGaussAndTsallis = 0

# Figures ---------------------------------------------------------------------

if vRvPhivTheta:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:
        data, label = fls.Bin1HQ10000_G1_2_1_005[1]
        ax1.plot(data[:, 0], data[:, 1], color='Green', ls='--', lw=2, ms=7)
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls =  '--',lw=2,ms=7)
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls =  '--',lw=2,ms=7)
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7)
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',  ls =  ':',lw=4,ms=7)
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls =  ':',lw=2,ms=7)
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7)
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7)
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',label=r'$v_r$',lw=2,ms=7)
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',label=r'$v_{\theta}$',
                 lw=2, ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',label=r'$v_{\phi}$',
                 lw=2, ms=7 )
        ax1.set_ylabel(r'$f\left(u \right)$', fontsize=20)
        ax1.set_title(r' File = %s' %Hq12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[5]
        ax2.plot(data[:, 0], data[:, 1], color='Green', ls='--', lw=2, ms=7)
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7)
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[7]
        ax2.plot(data[:, 0], data[:, 1], color='Black',
                 label=r'$\gamma = -1.5$', ls='--', lw=2, ms=7)
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -2.0 $',ls = ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -2.5 $', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
                       fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -1.5 $',ls ='--',lw=2,ms=7 )
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls =  '--',lw=2,ms=7 )
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.5 $', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        ax3.set_xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f(u) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -1.5 $',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = ':', lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.5 $', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.', lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', lw=2, ms=7)
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[7]
        ax4.plot(data[:, 0], data[:, 1], color='Black', lw=2, ms=7)
        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$',
            fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls ='--',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls =  '--',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls =  '--',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7)
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',  ls =  ':',lw=4,ms=7)
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls =  ':',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',label=r'$v_r$',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax1.plot(data[:, 0], data[:, 1], color='Red',
                 label=r'$v_{\theta}$', lw=2, ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax1.plot(data[:, 0], data[:, 1], color='Black',
                 label=r'$v_{\phi}$', lw=2, ms=7)
        ax1.set_ylabel(r'$f\left(u \right)$', fontsize=20)
        ax1.set_title(f'File = {test2_Hq0}', fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -1.5 $',ls = '--',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -2.0 $',ls = ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -2.5 $', ls =  '-.',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls ='--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls =  '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls =  '--',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls =  ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$v_r$',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'$v_{\theta}$',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$v_{\phi}$',lw=2,ms=7 )
        ax3.set_xlabel(r'$u_r$, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f(u) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax4.plot(data[:, 0], data[:, 1], color='Green', ls='--', lw=2, ms=7)
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax4.plot(data[:, 0], data[:, 1], color='Red', ls='--', lw=2, ms=7)
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax4.plot(data[:, 0], data[:, 1], color='Black', ls='--', lw=2, ms=7)
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = ':',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$',
            fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

if Fig_vr_vphi_vtheta_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f$' %(popt[0], popt[1]))
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0], popt[1]))
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0], popt[1]))
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Fits to file = %s, $\gamma = -2.0 $' %Hq12 ,
                      fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$ \frac{v_r}{\sigma_r} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0], popt[1]))
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'$ \frac{v_{\theta}}{\sigma_{\theta}} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0], popt[1]))
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$ \frac{v_{\phi}}{\sigma_{\phi}} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0], popt[1]))
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True, loc=0, handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_r $, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[5]
        ax4.plot(data[:,0], data[:,1], color='Green',
                 label=r'$\gamma = -2.0 $', lw=2, ms=7)
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2, ms=7)
        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$',
            fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        popt, pcov = curve_fit(func_2, data[:,0], data[:,1])
        y_fit = func_2(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r'Fits to file = %s, $\gamma = -2.0 $' %test2_Hq0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$ \frac{v_r}{\sigma_r} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$ radial: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'$ \frac{v_{\theta}}{\sigma_{\theta}} $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Pink',
                 label=r'$ \theta: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'$ \frac{v_{\phi}}{\sigma_{\phi}} $', lw=2, ms=7)
        popt, pcov = curve_fit(func_1_log, data[:,0], data[:,1])
        y_fit = func_1_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='Brown',
                 label=r'$ \phi: a\log xe^{-b \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax3.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_r $, $u_{\theta}$ and $u_{\phi}$', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax4.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$',
            fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

if Fig1_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if test:
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax1.set_ylabel(r'$f\left(u_t \right)$', fontsize=20)
        ax1.set_title(r' File = %s' %Hq12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $', lw=2, ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
            fontsize=20)
        ax2.grid()

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left(u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax1.set_ylabel(r'$f\left(u_t \right)$', fontsize=20)
        ax1.set_title(r' File = %s' %test2_Hq0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left(u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

if Fig_vt_with_fit:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(17, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    if test:
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
        y_fit = func_1(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        popt, pcov = curve_fit(func_6, data[:,0], data[:,1])
        y_fit = func_6(data[:,0],popt[0],popt[1],popt[2])
        ax1.plot(data[:,0],y_fit,':',lw=3,color='green',
                 label=r'$ax(1- (1 - q )bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
                 % (popt[0], popt[1], popt[2]))
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r'Fit to VDF, File = %s' %Hq12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_3_log, data[:,0], data[:,1])
        y_fit = func_3_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $'
                 % (popt[0], popt[1]))
        popt, pcov = curve_fit(func_7_log, data[:,0], data[:,1])
        y_fit = func_7_log(data[:,0],popt[0],popt[1],popt[2])
        ax2.plot(data[:,0],y_fit,':',lw=3,color='green',
                 label=r'$a\cdot \log(x)^2(1- (1 - q )b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
                 % (popt[0], popt[1], popt[2]))
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
            fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
            fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
        y_fit = func_1(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0], popt[1]))
        popt, pcov = curve_fit(func_6, data[:,0], data[:,1])
        y_fit = func_6(data[:,0],popt[0],popt[1],popt[2])
        ax1.plot(data[:,0],y_fit,':',lw=3,color='green',
                 label=r'$ax(1- (1 - q )bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
                 % (popt[0], popt[1], popt[2]))
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r'Fit to VDF, File = %s' %test2_Hq0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_3_log, data[:,0], data[:,1])
        y_fit = func_3_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',
                 label=r'$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $' %(popt[0], popt[1]))
        popt, pcov = curve_fit(func_7_log, data[:,0], data[:, 1])
        y_fit = func_7_log(data[:,0],popt[0], popt[1], popt[2])
        ax2.plot(data[:,0],y_fit,':',lw=3,color='green',
                 label=r'$a\cdot \log(x)^2(1- (1 - q )b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
                 % (popt[0], popt[1], popt[2]))
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
            fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
                       fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
                 label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
                 label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',
                 label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
                       fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if A:
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
        y_fit = func_1(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',label=r'$axe^{-bx^2}$, $ a,b = %.3f,%.3f $'
            %(popt[0],popt[1]))
        popt, pcov = curve_fit(func_6, data[:,0], data[:,1])
        y_fit = func_6(data[:,0],popt[0],popt[1],popt[2])
        ax1.plot(data[:,0],y_fit,':',lw=3,color='green',label=r'$ax(1- (1 - q )bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
            %(popt[0],popt[1],popt[2]))
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r'Fit to %s' %A_Hq0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_3_log, data[:,0], data[:,1])
        y_fit = func_3_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',label=r'$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $'
            %(popt[0],popt[1]))
        popt, pcov = curve_fit(func_7_log, data[:,0], data[:,1])
        y_fit = func_7_log(data[:,0],popt[0],popt[1],popt[2])
        ax2.plot(data[:,0],y_fit,':',lw=3,color='green',label=r'$a\cdot \log(x)^2(1- (1 - q )b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
            %(popt[0],popt[1],popt[2]))
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
            fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':', label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.', label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if B:
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        popt, pcov = curve_fit(func_1, data[:,0], data[:,1])
        y_fit = func_1(data[:,0],popt[0],popt[1])
        ax1.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',label=r'$axe^{-bx^2}$, $ a,b = %.3f,%.3f $' %(popt[0],popt[1]))
        popt, pcov = curve_fit(func_6, data[:,0], data[:,1])
        y_fit = func_6(data[:,0],popt[0],popt[1],popt[2])
        ax1.plot(data[:,0],y_fit,':',lw=3,color='green',label=r'$ax(1- (1 - q )bx^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
            % (popt[0], popt[1], popt[2]))
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r'Fit to %s' %B_Hq0 , fontsize=20)
        leg = ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
            fancybox=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        ax1.axes.get_xaxis().set_visible(False)
        ax1.set_xlim(0., 3.)
        ax1.set_ylim(0., 450.)

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
                 label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        popt, pcov = curve_fit(func_3_log, data[:,0], data[:,1])
        y_fit = func_3_log(data[:,0],popt[0],popt[1])
        ax2.plot(data[:,0],y_fit,'.-',lw=3,color='cyan',label=r'$a\cdot \log(x)^2e^{-b\cdot \log(x)^2}$, $ a,b = %.3f,%.3f $'
            % (popt[0], popt[1]))
        popt, pcov = curve_fit(func_7_log, data[:,0], data[:,1])
        y_fit = func_7_log(data[:,0],popt[0],popt[1],popt[2])
        ax2.plot(data[:,0],y_fit,':',lw=3,color='green',label=r'$a\cdot \log(x)^2(1- (1 - q )b \cdot \log(x)^2)^{(\frac{q}{1-q})}$, $ a,b,q = %.3f,%.3f,%.3f $'
            % (popt[0], popt[1], popt[2]))
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
            fontsize=20)
        leg = ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                         frameon=True,loc=0,handlelength=2.5)
        leg.get_frame().set_alpha(.5)
        ax2.yaxis.tick_right()
        ax2.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='on', left='off',
                        labelleft='off')
        ax2.yaxis.set_label_position("right")
        ax2.set_xlim(-3., 1.)
        ax2.set_ylim(0., 1500.)

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
            label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
            label=r'$\gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
            label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',
            label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
            fontsize=20)
        ax3.set_yscale('log')
        ax3.set_xlim(0., 3.)
        ax3.set_ylim(10**0., 10**3.)

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
            label=r'$\gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
            label=r'$\gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
            label=r'$\gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',
            label=r'$\gamma = -3.0 $',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
            fontsize=20)
        ax4.set_yscale('log')
        ax4.yaxis.tick_right()
        ax4.tick_params(axis='both', which='both', bottom='on', top='off',
            labelbottom='on', right='on', left='off', labelleft='off')
        ax4.yaxis.set_label_position("right")
        ax4.set_xlim(-3.,1.)
        ax4.set_ylim(10**0.,2*10**3.)
        f.savefig('vt_fit_show_abq.png')

if Fig_vr_vphi_vtheta_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[1]
        ax1.plot(data[:,0], data[:,1]/(478.006*np.exp(-0.456*data[:,0]**2)),color = 'Green',
            label=r'$r, a=478.006, b=0.456$', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[2]
        ax1.plot(data[:,0], data[:,1]/(482.605*np.exp(-0.473*data[:,0]**2)),color = 'Red',
            label=r'$\theta, a=482.605, b=0.473$',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[3]
        ax1.plot(data[:,0], data[:,1]/(502.652*np.exp(-0.477*data[:,0]**2)),color = 'Black',
            label=r'$\phi, a=502.652, b=0.477$',ls =  ':',lw=2,ms=7 )
        ax1.set_xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left(u \right)}{ae^{-bx^2}}$', fontsize=20)
        ax1.set_title(r' File = %s, $\gamma = -2.0 $' %Hq12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[5]
        ax2.plot(data[:,0], data[:,1]/(1433.228*10**data[:,0]*np.exp(-0.472*(10**data[:,0])**2)),
            color = 'Green',label=r'$a=1433.228, b=0.472$', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[6]
        ax2.plot(data[:,0], data[:,1]/(1416.346*10**data[:,0]*np.exp(-0.473*(10**data[:,0])**2)),
            color = 'Red', label=r'$ a=1416.346, b=0.473 $', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[7]
        ax2.plot(data[:,0], data[:,1]/(1405.914*10**data[:,0]*np.exp(-0.470*(10**data[:,0])**2)),
            color = 'Black', label=r'$ a=1405.914, b=0.470$',ls = ':', lw=2,ms=7 )
        ax2.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$',
            fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{axe^{-b\log (x)^2}}$',
        fontsize=20)  # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

    if test2:
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[1]
        ax1.plot(data[:,0], data[:,1]/(478.006*np.exp(-0.456*data[:,0]**2)),
            color = 'Green',label=r'$r, a=478.006, b=0.456$', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[2]
        ax1.plot(data[:,0], data[:,1]/(482.605*np.exp(-0.473*data[:,0]**2)),
            color = 'Red',label=r'$\theta, a=482.605, b=0.473$',  ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[3]
        ax1.plot(data[:,0], data[:,1]/(502.652*np.exp(-0.477*data[:,0]**2)),
            color = 'Black',label=r'$\phi, a=502.652, b=0.477$',ls =  ':',lw=2,ms=7 )
        ax1.set_xlabel(r'$ u_r $, $ u_{\theta} $ and $ u_{\phi} $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left(u \right)}{ae^{-bx^2}}$', fontsize=20)
        ax1.set_title(r' File = %s, $\gamma = -2.0 $' %test2_Hq0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[5]
        ax2.plot(data[:,0], data[:,1]/(1433.228*10**data[:,0]*np.exp(-0.472*(10**data[:,0])**2)),
            color = 'Green',label=r'$a=1433.228, b=0.472$', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[6]
        ax2.plot(data[:,0], data[:,1]/(1416.346*10**data[:,0]*np.exp(-0.473*(10**data[:,0])**2)),
            color = 'Red', label=r'$ a=1416.346, b=0.473 $', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[7]
        ax2.plot(data[:,0], data[:,1]/(1405.914*10**data[:,0]*np.exp(-0.470*(10**data[:,0])**2)),
            color = 'Black', label=r'$ a=1405.914, b=0.470$',ls = ':', lw=2,ms=7 )
        ax2.set_xlabel(r'$\log \left( |u_rn|,u_rp \right)$, $\log \left( |u_{\theta}n|,u_{\theta}p \right)$ and $\log \left( |u_{\phi}n|,u_{\phi}p \right)$',
            fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{axe^{-b\log (x)^2}}$',
            fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

if Fig_vt_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    if test:
        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0],data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue',ls = '--',label=r'$ \gamma = -1.5 $',lw=3)
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue', ls =  ':',label=r'$ \gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue', ls =  '-.',label=r'$ \gamma = -2.5 $',lw=4,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue',label=r'$ \gamma = -3.0 $',lw=2,ms=7 )
        ax1.set_ylim(0,2)
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$', fontsize=20)
        ax1.set_title(r' File = %s' %Hq12 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
            color = 'Blue',ls = '--', label=r'$ \gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
            color = 'Blue', ls =  ':', label=r'$ \gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
            color = 'Blue', ls =  '-.', label=r'$ \gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
            color = 'Blue', label=r'$ \gamma = -3.0 $',lw=2,ms=7 )
        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3400.442x^2e^{-0.930x^2}}$',
        fontsize=20)  # a \cdot \log(x) \cdot e^{-b \cdot log(x)^2}
        ax2.grid()

    if test2:
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0],data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue',ls = '--',label=r'$ \gamma = -1.5 $',lw=3)
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue', ls =  ':',label=r'$ \gamma = -2.0 $',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue', ls =  '-.',label=r'$ \gamma = -2.5 $',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1]/(918.083*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color = 'Blue',label=r'$ \gamma = -3.0 $',lw=2,ms=7 )
        ax1.set_ylim(0,2)
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$\frac{f\left( u_t \right)}{918.083xe^{-0.922x^2}}$',
            fontsize=20)
        ax1.set_title(r' File = %s' %test2_Hq0 , fontsize=20)
        ax1.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0],
                 data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue',ls = '--',
                 label=r'$ \gamma = -1.5 $',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0],
                 data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue', ls =  ':',
                 label=r'$ \gamma = -2.0 $',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0],
                 data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue', ls =  '-.',
                 label=r'$ \gamma = -2.5 $',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0],
                 data[:,1]/(3400.442*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color = 'Blue', label=r'$ \gamma = -3.0 $',lw=2,ms=7 )
        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3400.442x^2e^{-0.930x^2}}$',
            fontsize=20)
        ax2.grid()

if Fig3_vr_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
             label=r'$\gamma = -1.5 $',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Green',ls ='--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
             label=r'$\gamma = -2.0 $',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
             label=r'$\gamma = -2.5 $',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue',
             label=r'$\gamma = -3.0 $',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    ax1.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
    ax1.set_title(r' File = %s' %Hq0 , fontsize=20)
    ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
               frameon=True,loc=0,handlelength=2.5)
    ax1.grid()

    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[4]
    ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
             label=r'$\gamma = -1.5 $',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[4]
    ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
             label=r'$\gamma = -2.0 $',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[4]
    ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
             label=r'$\gamma = -2.5 $',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[4]
    ax2.plot(data[:,0], data[:,1],color = 'Blue',
             label=r'$\gamma = -3.0 $',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    ax2.set_xlim(-3,0)
    ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$',
        fontsize=20)
    ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
        fontsize=20)
    ax2.legend(prop=dict(size=18), numpoints=2, ncol=1,
               frameon=True,loc=0,handlelength=2.5)
    ax2.grid()

    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[0]
    ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
             label=r'$\gamma = -1.5 $',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Green',ls ='--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[0]
    ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
             label=r'$\gamma = -2.0 $',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[0]
    ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
             label=r'$\gamma = -2.5 $',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[0]
    ax3.plot(data[:,0], data[:,1],color = 'Blue',
             label=r'$\gamma = -3.0 $',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    ax3.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
    ax3.legend(prop=dict(size=18), numpoints=2, ncol=1,
               frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')

    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[4]
    ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',
             label=r'$\gamma = -1.5 $',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[4]
    ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',
             label=r'$\gamma = -2.0 $',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[4]
    ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',
             label=r'$\gamma = -2.5 $',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[4]
    ax4.plot(data[:,0], data[:,1],color = 'Blue',
             label=r'$\gamma = -3.0 $',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    ax4.set_xlim(-3,0)
    ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$',
        fontsize=20)
    ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
        fontsize=20)
    ax4.legend(prop=dict(size=18), numpoints=2, ncol=1,
               frameon=True, loc=0, handlelength=2.5)
    ax4.grid()
    ax4.set_yscale('log')

if Fig_Gperturbations_same_gammas_as_IC_vr:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
        % Hq0[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq18[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--',
             label=r'%s' %Hq70[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet',ls ='--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[0]  # label=r'$\gamma = -2.0$'
    ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[0]  # label=r'$\gamma = -2.5$'
    ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[0]  # label=r'$\gamma = -3.0$'
    ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[1]
    ax1.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[1]
    ax1.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[0]
    ax1.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[1]
    ax1.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7 )
    ax1.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
    ax1.set_title(r' Time evolution of files = %s' %Hq0[:-9] , fontsize=20)
    ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
        frameon=True,loc=0,handlelength=2.5)
    ax1.grid()

    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[4]  # label=r'$\gamma = -1.5$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
        % Hq0[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Skyblue',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq18[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[4]
    ax2.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--', label=r'%s'
        % Hq70[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet',ls = '--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[4] # , label=r'$\gamma = -2.0$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[4]
    ax2.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[4] # , label=r'$\gamma = -2.5$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[4]
    ax2.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[4]  # , label=r'$\gamma = -3.0$'
    ax2.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[5]
    ax2.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[5]
    ax2.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[4]
    ax2.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[5]
    ax2.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7 )
    ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$',
        fontsize=20)
    ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
        fontsize=20)
    ax2.legend(prop=dict(size=18), numpoints=2, ncol=1,
        frameon=True,loc=0,handlelength=2.5)
    ax2.grid()

    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[0]  # label=r'$\gamma = -1.5$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
        % Hq0[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq18[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow',ls ='--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--', label=r'%s'
        % Hq70[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet',ls ='--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[0] # ,label=r'$\gamma = -2.0$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[0] # ,label=r'$\gamma = -2.5$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[0] # ,label=r'$\gamma = -3.0$'
    ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[1]
    ax3.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[1]
    ax3.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[0]
    ax3.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[1]
    ax3.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7 )
    ax3.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
    ax3.legend(prop=dict(size=18), numpoints=2, ncol=1,
               frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')

    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[4] # , label=r'$\gamma = -1.5$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
        % Hq0[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq18[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow',ls = '--',lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta',ls = '--', label=r'%s'
        % Hq70[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet',ls = '--',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[4] # , label=r'$\gamma = -2.0$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet', ls =  ':',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[4] # , label=r'$\gamma = -2.5$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet',ls =  '-.',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[4] # label=r'$\gamma = -3.0$'
    ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_0_0_000[5]
    ax4.plot(data[:,0], data[:,1],color = 'Skyblue',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Pink',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G0_8_2_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Chartreuse',lw=2,ms=7)
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[5]
    ax4.plot(data[:,0], data[:,1],color = 'Yellow',lw=2,ms=7)
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[4]
    ax4.plot(data[:,0], data[:,1],color = 'Magenta',lw=2,ms=7)
    data, label = datalist_outerbin_Hernquist10000_G1_0_10_009[5]
    ax4.plot(data[:,0], data[:,1],color = 'Violet',lw=2,ms=7)
    ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$',
        fontsize=20)
    ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
        fontsize=20)
    ax4.legend(prop=dict(size=18), numpoints=2, ncol=1,
        frameon=True,loc=0,handlelength=2.5)
    ax4.grid()
    ax4.set_yscale('log')

if Fig_Gperturbations_G1_2_same_gammas_as_IC_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_3_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_7_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[0]
    ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    ax1.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
    ax1.set_title(r' Time evolution of files = %s' %Hq0[:-9] , fontsize=20)
    ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
        frameon=True,loc=0,handlelength=2.5)
    ax1.grid()

    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_3_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_7_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--', label=r'%s'
        % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_3_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_7_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_3_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_7_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_3_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_7_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[4]
    ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$',
        fontsize=20)
    ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
        fontsize=20)
    ax2.legend(prop=dict(size=18), numpoints=2, ncol=1,
        frameon=True,loc=0,handlelength=2.5)
    ax2.grid()

    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',ls = '--', label=r'%s'
        % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_3_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_7_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[0]
    ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    ax3.set_xlabel(r'$ u_t $ and $ u_r $', fontsize=20)
    ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
    ax3.legend(prop=dict(size=18), numpoints=2, ncol=1,
        frameon=True,loc=0,handlelength=2.5)
    ax3.grid()
    ax3.set_yscale('log')

    data, label = datalist_innerbin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
        % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
        % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
        % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--', label=r'%s'
        % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_innerbin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
        % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
    data, label = datalist_first_middlebin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_second_middlebin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_1_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_3_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_5_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_7_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
    data, label = datalist_outerbin_Hernquist10000_G1_2_9_005[4]
    ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
    ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$ and $\log \left( |u_rn|,u_rp \right)$',
        fontsize=20)
    ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
        fontsize=20)
    ax4.legend(prop=dict(size=18), numpoints=2, ncol=1,
               frameon=True,loc=0,handlelength=2.5)
    ax4.grid()
    ax4.set_yscale('log')

if Fig_Gperturbations_different_gammas_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    f.subplots_adjust(hspace=0, wspace=0)
    if test:
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
            % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
            % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
            % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
            % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
            % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins' % Hq0[:-9],
            fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
            % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
            % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
            % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--', label=r'%s'
            % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
            % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
            fontsize=20)
        ax2.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
            % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
            % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
            % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',ls = '--', label=r'%s'
            % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
            % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
            % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
            % Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
            % Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--', label=r'%s'
            % Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
            % Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
            fontsize=20)
        ax4.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

    if test2:
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
            % test2_Hq0[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
            % test2_Hq36[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
            % test2_Hq66[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
            % test2_Hq96[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
            % test2_Hq126[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', label=r'%s'
            % test2_Hq159[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins'
            % test2_Hq0[:-9],
            fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
            fontsize=20)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$',
            fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',ls = '--', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

    if B:
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',ls = '--', label=r'%s'
            % B_Hq0[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',ls = '--', label=r'%s'
            % B_Hq36[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',ls = '--', label=r'%s'
            % B_Hq66[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',ls = '--', label=r'%s'
            % B_Hq294[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',ls = '--', label=r'%s'
            % B_Hq382[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax1.set_xlabel(r'$ u_t $', fontsize=20)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins' % B_Hq0[:-9],
            fontsize=20)
        ax1.legend(prop=dict(size=18), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.set_xlim(0, 3)
        ax1.axes.get_xaxis().set_visible(False)
        ax1.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='off', left='on',
                        labelleft='on')

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax2.set_xlim(-3, 1)
        ax2.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$',
                       fontsize=20)
        ax2.axes.get_xaxis().set_visible(False)
        ax2.yaxis.tick_right()
        ax2.yaxis.set_label_position("right")

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',ls = '--', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=4,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=4,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax3.set_xlabel(r'$ u_t $', fontsize=20)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.set_yscale('log')
        ax3.tick_params(axis='both', which='both', bottom='on', top='off',
                        labelbottom='on', right='off', left='on',
                        labelleft='on')
        ax3.set_xlim(0, 3)

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',ls = '--',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',ls = '--',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  ':',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  ':',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', ls =  '-.',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax4.set_xlim(-3,1)
        ax4.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$',
            fontsize=20)
        ax4.set_yscale('log')
        ax4.yaxis.tick_right()
        ax4.yaxis.set_label_position("right")
        ax4.tick_params(axis='both', which='both', bottom='on', top='off',
                        labelbottom='on', right='on', left='off',
                        labelleft='off')
        f.savefig('Time_evolution_B_vt_different_rbins.png')

if Fig_Gperturbations_gammas_1_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -1.5$'
                      % Hq0[:-9], fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red',
                 label=r'%s ' % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green',
                 label=r'%s' %Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black',
                 label=r'%s' %Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown',
                 label=r'%s' %Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange',
                 label=r'%s' %Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$',
            fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
            fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (np.log10(data[:, 0]) * np.exp(-.5 * data[:, 0] ** 2)),
                 color='Red', lw=2, ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax5.plot(data[:, 0],
                 data[:, 1] / (np.log10(data[:, 0]) * np.exp(-.5 * data[:, 0] ** 2)),
                 color='Green', lw=2, ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),
                 color = 'Orange',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Orange',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$',
                       fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -1.5$' %test2_Hq0[:-9],
            fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s '
            %  test2_Hq0[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s'
            % test2_Hq36[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s'
            % test2_Hq66[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s'
            % test2_Hq96[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s'
            % test2_Hq126[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s'
            % test2_Hq159[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
            fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color='Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color='Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color='Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color='Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color='Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
            color='Blue',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$',
            fontsize=20)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color='Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color='Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color='Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color='Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color='Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),
                 color='Blue',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$',
            fontsize=20)
        ax6.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color='Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color='Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color='Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color='Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color='Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),
                 color='Blue',lw=2,ms=7 )
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color='Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color='Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color='Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color='Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color='Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),
                 color='Blue',lw=2,ms=7 )
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -1.5$' %A_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % A_Hq0[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %A_Hq36[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %A_Hq66[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %A_Hq246[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %A_Hq298[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %A_Hq382[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$',
            fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,
            frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7 )
        ax7.set_ylim(0.5,1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7 )
        ax8.set_ylim(0.5,1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -1.5$' %B_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % B_Hq0[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %B_Hq36[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %B_Hq66[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %B_Hq294[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %B_Hq382[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Orange',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Orange',lw=2,ms=7 )
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_innerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7 )
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

if Fig_Gperturbations_gammas_2_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_first_middlebin__different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$' %Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Orange',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Red',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Green',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Black',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Brown',lw=2,ms=7)
        data, label = datalist_first_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Orange',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$' %test2_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % test2_Hq0[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %test2_Hq36[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %test2_Hq66[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %test2_Hq96[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %test2_Hq126[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %test2_Hq159[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7 )
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7 )
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.0$' %A_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % A_Hq0[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %A_Hq36[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %A_Hq66[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %A_Hq246[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %A_Hq298[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %A_Hq382[len('A_Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7 )
        ax7.set_ylim(0.5,1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7 )
        ax8.set_ylim(0.5,1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.0$' %B_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % B_Hq0[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %B_Hq36[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %B_Hq66[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %B_Hq294[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %B_Hq382[len('B_Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Orange',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Orange',lw=2,ms=7 )
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_first_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7 )
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

if Fig_Gperturbations_gammas_2_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_second_middlebin__different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.5$' %Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % Hq12[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %Hq24[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %Hq36[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %Hq48[len('Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %Hq60[len('Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Orange',lw=2,ms=7 )
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Orange',lw=2,ms=7 )
        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7 )
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.5 $' %test2_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % test2_Hq0[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %test2_Hq36[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %test2_Hq66[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %test2_Hq96[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %test2_Hq126[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %test2_Hq159[len('test2_Hernquist10000_G'):],lw=2,ms=7 )
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.5$' %A_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % A_Hq0[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %A_Hq36[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %A_Hq66[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %A_Hq246[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %A_Hq298[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %A_Hq382[len('A_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0.5,1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0.5,1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -2.5$' %B_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % B_Hq0[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %B_Hq36[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %B_Hq66[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %B_Hq294[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %B_Hq382[len('B_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Orange',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_second_middlebin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

if Fig_Gperturbations_gammas_3_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_outerbin__different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -3.0$' %Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % Hq12[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %Hq24[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %Hq36[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %Hq48[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %Hq60[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Orange',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -3.0 $' %test2_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % test2_Hq0[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %test2_Hq36[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %test2_Hq66[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %test2_Hq96[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %test2_Hq126[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %test2_Hq159[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,
                   frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange', lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0],
                 data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),
                 color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_15_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_20_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_test2_Hernquist10000_G1_0_25_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -3.0$' %A_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % A_Hq0[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %A_Hq36[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %A_Hq66[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %A_Hq246[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %A_Hq298[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %A_Hq382[len('A_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylim(0.5,1.5)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylim(0.5,1.5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0.5,1.5)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_40_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_009[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0.5,1.5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red' ,lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Brown' ,lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange' ,lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of %s , different r bins, $\gamma = -3.0$' %B_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % B_Hq0[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %B_Hq36[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %B_Hq66[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %B_Hq294[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %B_Hq382[len('B_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(914.415*data[:,0]*np.exp(-0.930*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylim(0,3)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{914.415 \cdot x \cdot e^{-0.930 \cdot x^2} }$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3452.955*(10**data[:,0])**2*np.exp(-0.936*(10**data[:,0])**2)),color = 'Orange',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylim(0,3)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(894.292*data[:,0]*(1-(1-0.955)*0.918*data[:,0]**2)**(0.955/(1-0.955))),color = 'Orange',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_5_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Brown',lw=2,ms=7)
        data, label = datalist_outerbin_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3418.569*10**data[:,0]*(1-(1-0.987)*0.929*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Orange',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

if Fig_Gperturbations_R_middle_19_95_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -1.5$' %Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % Hq12[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %Hq24[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %Hq36[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %Hq48[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %Hq60[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[0]
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_1_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Red',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_3_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Green',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_5_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Black',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_7_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Brown',lw=2,ms=7)
        data, label = datalist_innerbin_different_gammas_Hernquist10000_G1_2_9_005[4]
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Orange',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s ,  $ R_{middle} = 19.95 $' %test2_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % test2_Hq0[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %test2_Hq66[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %test2_Hq166[len('test2_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s ,  $ R_{middle} = 19.95 $' %A_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % A_Hq0[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %A_Hq66[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %A_Hq382[len('A_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s ,  $ R_{middle} = 19.95 $' %B_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % B_Hq0[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %B_Hq66[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %B_Hq294[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %B_Hq382[len('B_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7)
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_19_95_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()


if Fig16_Gperturbations_R_middle_31_62_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        ax1.plot(data[:,0], data[:,1],color = 'Blue',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        ax1.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax1.set_xticklabels([])
        ax1.set_ylabel(r'$f\left( u \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , different r bins, $\gamma = -2.0$' %Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % Hq12[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %Hq24[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %Hq36[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Brown', label=r'%s' %Hq48[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.plot(data[:,0], data[:,1],color = 'Orange', label=r'%s' %Hq60[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$f\left(\log \left( |u_n|,u_p \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        ax3.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        ax3.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax3.set_xticklabels([])
        ax3.set_ylabel(r'$\log \left( f\left( u \right) \right)$', fontsize=20)
        ax3.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax3.grid()
        ax3.set_yscale('log')

        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        ax4.plot(data[:,0], data[:,1],color = 'Green',lw=2,ms=7)
        ax4.plot(data[:,0], data[:,1],color = 'Black',lw=2,ms=7)
        ax4.plot(data[:,0], data[:,1],color = 'Brown',lw=2,ms=7)
        ax4.plot(data[:,0], data[:,1],color = 'Orange',lw=2,ms=7)
        ax4.set_xticklabels([])
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_n|,u_p \right)\right) \right)$', fontsize=20)
        ax4.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax4.grid()
        ax4.set_yscale('log')

        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Brown',lw=2,ms=7)
        ax5.plot(data[:,0], data[:,1]/(np.log10(data[:,0])*np.exp(-0.5*data[:,0]**2)),color = 'Orange',lw=2,ms=7)
        ax5.set_xticklabels([])
        ax5.set_ylabel(r'$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$', fontsize=20)
        ax5.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax5.grid()

        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Red',lw=2,ms=7)
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Green',lw=2,ms=7)
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Black',lw=2,ms=7)
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Brown',lw=2,ms=7)
        ax6.plot(data[:,0], data[:,1]/np.exp(-0.5*data[:,0]**2),color = 'Orange',lw=2,ms=7)
        ax6.set_xticklabels([])
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}{e^{-0.5x^2}}$', fontsize=20)
        ax6.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax6.grid()

    if test2:
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , $ R_{middle} = 31.62 $' %test2_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % test2_Hq0[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %test2_Hq66[len('Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %test2_Hq166[len('Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_test2_Hernquist10000_G1_0_18_053[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if A:
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , $ R_{middle} = 31.62 $' %A_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % A_Hq0[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %A_Hq66[len('A_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %A_Hq382[len('A_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_A_Hernquist10000_G1_0_48_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$', fontsize=20)
        ax8.grid()

    if B:
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax1.plot(data[:,0], data[:,1],color = 'Black' ,lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax1.plot(data[:,0], data[:,1],color = 'Blue' ,lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax1.plot(data[:,0], data[:,1],color = 'Green' ,lw=2,ms=7)
        ax1.set_ylabel(r'$f\left( u_t \right)$', fontsize=20)
        ax1.set_title(r' Time evolution of files = %s , $ R_{middle} = 31.62 $' %B_Hq0[:-9] , fontsize=20)
        ax1.legend(prop=dict(size=11), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax1.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Red', label=r'%s ' % B_Hq0[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax2.plot(data[:,0], data[:,1],color = 'Black', label=r'%s' %B_Hq66[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax2.plot(data[:,0], data[:,1],color = 'Blue', label=r'%s' %B_Hq294[len('B_Hernquist10000_G'):],lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax2.plot(data[:,0], data[:,1],color = 'Green', label=r'%s' %B_Hq382[len('B_Hernquist10000_G'):],lw=2,ms=7)
        ax2.set_ylabel(r'$f\left(\log \left( |u_tn|,u_tp \right)\right)$', fontsize=20)
        ax2.legend(prop=dict(size=13), numpoints=2, ncol=1,frameon=True,loc=0,handlelength=2.5)
        ax2.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Red', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax3.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax3.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax3.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7)
        ax3.set_ylabel(r'$\log \left( f\left( u_t \right) \right)$', fontsize=20)
        ax3.grid()
        ax3.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax4.plot(data[:,0], data[:,1],color = 'Black', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax4.plot(data[:,0], data[:,1],color = 'Blue', lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax4.plot(data[:,0], data[:,1],color = 'Green', lw=2,ms=7)
        ax4.set_ylabel(r'$\log \left( f\left(\log \left( |u_tn|,u_tp \right)\right) \right)$', fontsize=20)
        ax4.grid()
        ax4.set_yscale('log')

        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax5.plot(data[:,0], data[:,1]/(887.569*data[:,0]*np.exp(-0.922*data[:,0]**2)),color = 'Green',lw=2,ms=7)
        ax5.set_ylabel(r'$\frac{f\left( u_t \right)}{887.569 \cdot x \cdot e^{-0.922 \cdot x^2} }$', fontsize=20)
        ax5.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax6.plot(data[:,0], data[:,1]/(3424.993*(10**data[:,0])**2*np.exp(-0.930*(10**data[:,0])**2)),color = 'Green',lw=2,ms=7)
        ax6.set_ylim(0,5)
        ax6.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$', fontsize=20)
        ax6.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[0]
        ax7.plot(data[:,0], data[:,1]/(864.543*data[:,0]*(1-(1-0.946)*0.908*data[:,0]**2)**(0.946/(1-0.946))),color = 'Green',lw=2,ms=7)
        ax7.set_ylim(0,2)
        ax7.set_xlabel(r'$u_t$', fontsize=20)
        ax7.set_ylabel(r'$\frac{f\left( u_t \right)}{Tsallis} $', fontsize=20)
        ax7.grid()

        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_0_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Red',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_10_005[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Black',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_000[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Blue',lw=2,ms=7)
        data, label = datalist_large_R_middle_31_62_different_gammas_B_Hernquist10000_G1_0_198_093[4]
        ax8.plot(data[:,0], data[:,1]/(3391.113*10**data[:,0]*(1-(1-0.987)*0.924*10**(data[:,0]**2))**(0.987/(1.-0.987))),color = 'Green',lw=2,ms=7)
        ax8.set_ylim(0,5)
        ax8.set_xlabel(r'$\log \left( |u_tn|,u_tp \right)$', fontsize=20)
        ax8.set_ylabel(r'$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}{Tsallis}$',
                                fontsize=20)
        ax8.grid()

plt.show()
