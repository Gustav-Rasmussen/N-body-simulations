# -*- coding: utf-8 -*-

# filename, label: f, l
datalistMartinIC = [(pylab.loadtxt(f), l)
                    for f, l in lsts.fileLstMartinIC]
datalistMartinFinal = [(pylab.loadtxt(f), l)
                       for f, l in lsts.fileLstMartinFinal]


datalistA = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstA]
datalistA_R10000 = [(pylab.loadtxt(f), l)
                    for f, l in lsts.fileLstA_R10000]
datalist_A_R10000_20bins = [(pylab.loadtxt(f), l)
                            for f, l in FileLstA_R10000_20bins]


datalistB = [(pylab.loadtxt(f), l)
             for f, l in lsts.fileLstB]
datalistB20 = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstB20]
datalistB_R10000 = [(pylab.loadtxt(f), l)
                    for f, l in lsts.fileLstB_R10000]
datalist_B_R10000_20bins = [(pylab.loadtxt(f), l)
                            for f, l in FileLstB_R10000_20bins]
datalist_B_Almost_Final_R5000 = [(pylab.loadtxt(f), l)
                                 for f, l in FileLstB_Almost_Final_R5000]


datalistC_IC = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstC_IC]


datalist_CS4CS5CS6_Final = [(pylab.loadtxt(f), l)
                            for f, l in FileLstCS4CS5CS6_Final]

datalist_CS4CS5CS6_Final_R5000 = [(pylab.loadtxt(f), l) for f, l in FileLstCS4CS5CS6_Final_R5000]

datalistCS4CS5CS6_R10000 = [(pylab.loadtxt(f), l)
                            for f, l in lsts.fileLstCS4CS5CS6_R10000]


datalist_DS1D2_IC = [(pylab.loadtxt(f), l) for f, l in FileLstDS1D2_IC]
datalist_DS1D2_IC_R10000 = [(pylab.loadtxt(f), l) for f, l in FileLstDS1D2_IC_R10000]
datalistDS1_SoftD2_R10000 = [(pylab.loadtxt(f), l)
                             for f, l in lsts.fileLstDS1_SoftD2_R10000]
datalist_DS1D2_Almost_Final_R5000 = [(pylab.loadtxt(f), l)
                                     for f, l in FileLstDS1D2_Almost_Final_R5000]
datalist_DS1D2_Final = [(pylab.loadtxt(f), l) for f, l in FileLstDS1D2_Final]
datalist_DS1D2_Final_R10000 = [(pylab.loadtxt(f), l) for f, l in FileLstDS1D2_Final_R10000]


datalist_E = [(pylab.loadtxt(f), l) for f, l in FileLstE]
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


datalist_rfp = [(pylab.loadtxt(f), l) for f, l in FileLstrfp]
datalist_rfp_R32 = [(pylab.loadtxt(f), l) for f, l in FileLstrfp_R32]
