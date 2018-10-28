#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 14:24:55 2018

@author: gustavcollinrasmussen
"""

import readVDF2FileLst as fls
from pathlib import Path

userPath = Path.cwd()

print(fls.bins3A[0])
# print(fls.bins3A)

'''
def plot_test():

    [(pylab.loadtxt(f), l) for f, l in bins3A[0]]

    return fls.Bin1differentGammasTest2HQ10000_G1_0_0_000
    # f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,
    #                                            sharex='col', sharey='row')

    # data, label = fls.Bin1differentGammasTest2HQ10000_G1_0_0_000[0]
    # ax1.plot(data[:, 0], data[:, 1],\
    #                  color={colours[fileNum]}, ls='--', lw=2, ms=7)")


plot_test()

breakpoint()
'''
