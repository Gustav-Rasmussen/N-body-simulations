# -*- coding: utf-8 -*-

import pylab
import fileLsts as lsts

# filename, label: f, l
datalistMartinIC = [(pylab.loadtxt(f), l)
                    for f, l in lsts.fileLstMartinIC]
datalistMartinFinal = [(pylab.loadtxt(f), l)
                       for f, l in lsts.fileLstMartinFinal]

datalistA = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstA]
datalistA_R10000 = [(pylab.loadtxt(f), l)
                    for f, l in lsts.fileLstA_R10000]
datalist_A_R10000_20bins = [(pylab.loadtxt(f), l)
                            for f, l in lsts.FileLstA_R10000_20bins]

datalistB = [(pylab.loadtxt(f), l)
             for f, l in lsts.fileLstB]
datalistB20 = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstB20]
datalistB_R10000 = [(pylab.loadtxt(f), l)
                    for f, l in lsts.fileLstB_R10000]
datalist_B_R10000_20bins = [(pylab.loadtxt(f), l)
                            for f, l in lsts.FileLstB_R10000_20bins]
datalist_B_Almost_Final_R5000 = [(pylab.loadtxt(f), l)
                                 for f, l in lsts.FileLstB_Almost_Final_R5000]

datalistC_IC = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstC_IC]

datalist_CS4CS5CS6_Final = [(pylab.loadtxt(f), l)
                            for f, l in lsts.FileLstCS4CS5CS6_Final]

datalist_CS4CS5CS6_Final_R5000 = [(pylab.loadtxt(f), l)
                                  for f, l
                                  in lsts.FileLstCS4CS5CS6_Final_R5000]

datalistCS4CS5CS6_R10000 = [(pylab.loadtxt(f), l)
                            for f, l in lsts.fileLstCS4CS5CS6_R10000]


datalist_DS1D2_IC = [(pylab.loadtxt(f), l) for f, l in lsts.FileLstDS1D2_IC]
datalist_DS1D2_IC_R10000 = [(pylab.loadtxt(f), l)
                            for f, l in lsts.FileLstDS1D2_IC_R10000]
datalist_DS1D2_Almost_Final_R5000 = [(pylab.loadtxt(f), l)
                                     for f, l
                                     in lsts.FileLstDS1D2_Almost_Final_R5000]
datalist_DS1D2_Final = [(pylab.loadtxt(f), l)
                        for f, l in lsts.FileLstDS1D2_Final]
datalist_DS1D2_Final_R10000 = [(pylab.loadtxt(f), l)
                               for f, l in lsts.FileLstDS1D2_Final_R10000]

datalistDS1_SoftD2_R10000 = [(pylab.loadtxt(f), l)
                             for f, l in lsts.fileLstDS1_SoftD2_R10000]

datalist_E = [(pylab.loadtxt(f), l) for f, l in lsts.FileLstE]
datalistE_R10000 = [(pylab.loadtxt(f), l)
                    for f, l in lsts.fileLstE_R10000]

datalistA_R32 = [(pylab.loadtxt(f), l)
                 for f, l in lsts.fileLstA_Rlimit32_50bins]
datalistB_R32 = [(pylab.loadtxt(f), l)
                 for f, l in lsts.fileLstB_Rlimit32_50bins]
datalistCS4_R32 = [(pylab.loadtxt(f), l)
                   for f, l in lsts.fileLstCS4_Rlimit32_20bins]
datalistCS5_R32 = [(pylab.loadtxt(f), l)
                   for f, l in lsts.fileLstCS5_Rlimit32_20bins]
datalistCS6_R32 = [(pylab.loadtxt(f), l)
                   for f, l in lsts.fileLstCS6_Rlimit32_20bins]
datalistDS1_R32 = [(pylab.loadtxt(f), l)
                   for f, l in lsts.fileLstDS1_Rlimit32_20bins]
datalistSoftD2_R32 = [(pylab.loadtxt(f), l)
                      for f, l in lsts.fileLstSoft_D2_Rlimit32_20bins]
datalistE_R32 = [(pylab.loadtxt(f), l)
                 for f, l in lsts.fileLstE_Rlimit32_50bins]

datalist_rfp = [(pylab.loadtxt(f), l) for f, l in lsts.FileLstrfp]
datalist_rfp_R32 = [(pylab.loadtxt(f), l) for f, l in lsts.FileLstrfp_R32]


def plot_test():
    # [(pylab.loadtxt(f), l) for f, l in bins3A[0]]
    return datalistMartinIC
    # f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,
    #                                            sharex='col', sharey='row')
    # data, label = datalistMartinIC[0]
    # ax1.plot(data[:, 0], data[:, 1],\
    #                  color={colours[fileNum]}, ls='--', lw=2, ms=7)")


# plot_test()
