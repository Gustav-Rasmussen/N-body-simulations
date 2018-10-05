# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

'''
This script defines Rho, Gaussian and Tsallis functions,
and compares the last two visually
'''


def rho_Hernquist(rho_0_HQ, rs, x):
    return rho_0_HQ / (x / rs * (1 + x / rs) ** 3)


def rho_NFW(rho_0_NFW, rs, x):
    return rho_0_NFW / (x / rs * (1 + x / rs) ** 2)


# Constants -------------------------------------------------------------------

log10x = 1
x = 10.0 ** log10x

# Gaussian functions ----------------------------------------------------------


def func1(x, a, b):
    return a * x * np.exp(-b * x ** 2.)


def func2(x, a=1, b=.5):
    return a * np.exp(-b * x ** 2.)


def func_1_add(x, a, b, c):
    return a * x * np.exp(-b * x ** 2) + c


def func_2_add(x, a, b, c):
    return a * np.exp(-b * x ** 2) + c


def func3(x, a, b):
    return a * x ** 2 * np.exp(-b * x ** 2.)


def func1Log(log10x, a, b):
    return a * x * np.exp(-b * x ** 2.)


def func2Log(log10x, a, b):
    return a * np.exp(-b * x ** 2.)


def func3Log(log10x, a, b):
    return a * x ** 2 * np.exp(-b * x ** 2.)

# Tsallis functions -----------------------------------------------------------


def func4(x, a=1, q=.5, b=1):
    return a * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func5(x, b, q):
    return (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func4Log(log10x, a, q, b):
    return a * x * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func_6(x, a, b, q):
    return a * x * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func_7_log(log10x, a, b, q):
    x = 10.0 ** log10x
    return a * x ** 2 * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


# Figure switches -------------------------------------------------------------

GaussianFits = 0
QFits = 0
CompareFits = 0

# Figure definitions ----------------------------------------------------------

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))
xPlot = np.linspace(-5, 5, 50)
y1 = 10 ** -3
y2 = 10 ** 1
c = ['Red', 'Blue', 'Green', 'Orange', 'Violet', 'Black']

if GaussianFits:
    ax1.plot(xPlot, func2(xPlot, b=1), '-o', mew=0,
             color=c[0], label=r'$a=1, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot, a=1.5, b=1), '-o', mew=0,
             color=c[1], label=r'$a=1.5, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot, b=1.5), '-o', mew=0,
             color=c[2], label=r'$a=1, b=1.5$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot, a=0.5, b=1), '-o', mew=0,
             color=c[3], label=r'$a=0.5, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot), '-o', mew=0,
             color=c[4], label=r'$a=1, b=0.5$', lw=2, ms=7)
    ax1.set_xlabel(r'x', fontsize=20)
    ax1.set_ylabel(r'$a e^{-b x^2}$', fontsize=20)
    ax1.set_title(r'Gaussian fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=1, ncol=1,
               frameon=1, loc=0, handlelength=2.5)
    ax1.set_xlim(-3, 3)
    ax1.grid()

    ax2.plot(xPlot, func2(xPlot, b=1), '-o', mew=0,
             color=c[0], lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot, a=1.5, b=1), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot, b=1.5), '-o', mew=0,
             color=c[2], lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot, a=.5, b=1), '-o', mew=0,
             color=c[3], lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot), '-o', mew=0,
             color=c[4], lw=2, ms=7)
    ax2.set_xlim(10 ** -1, y2)
    ax2.set_ylim(0, 1.6)
    ax2.set_xlabel(r'$\log x$', fontsize=20)
    ax2.set_ylabel(r'$a e^{-b x^2}$', fontsize=20)
    ax2.grid()
    ax2.set_xscale('log')

    ax3.plot(xPlot, func2(xPlot, b=1), '-o', mew=0,
             color=c[0], lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot, a=1.5, b=1), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot, b=1.5), '-o', mew=0,
             color=c[2], lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot, a=.5, b=1), '-o', mew=0,
             color=c[3], lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot), '-o', mew=0,
             color=c[4], lw=2, ms=7)
    ax3.set_xlim(-4, 4)
    ax3.set_ylim(y1, y2)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$ \log \left( a e^{-b x^2} \right)$', fontsize=20)
    ax3.grid()
    ax3.set_yscale('log')

    ax4.plot(xPlot, func2(xPlot, b=1), '-o', mew=0,
             color=c[0], lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot, a=1.5, b=1), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot, b=1.5), '-o', mew=0,
             color=c[2], lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot, a=.5, b=1), '-o', mew=0,
             color=c[3], lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot), '-o', mew=0,
             color=c[4], lw=2, ms=7)
    ax4.set_xlim(-4, 4)
    ax4.set_ylim(y1, y2)
    ax4.set_xlabel(r'$\log x$', fontsize=20)
    ax4.set_ylabel(r'$\log \left(a e^{-b x^2} \right)$', fontsize=20)
    ax4.grid()
    ax4.set_xscale('log')
    ax4.set_yscale('log')

if QFits:
    ax1.plot(xPlot, func4(xPlot, q=.9), '-o', mew=0,
             color=c[0], label=r'$a=1, q=0.9, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=.9, b=1.5), '-o', mew=0,
             color=c[1], label=r'$a=1, q=0.9, b=1.5$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, a=1.5, q=.9), '-o', mew=0,
             color=c[2], label=r'$a=1.5, q=0.9, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=1.2), '-o', mew=0,
             color=c[3], label=r'$a=1, q=1.2, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=1.5), '-o', mew=0,
             color=c[4], label=r'$a=1 , q=1.5, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[5], label=r'$a=1, q=\frac{5}{3}, b=1$', lw=2, ms=7)
    ax1.set_xlabel(r'x', fontsize=20)
    ax1.set_ylabel(r'$a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac {q}{1-q}}$',
                   fontsize=20)
    ax1.set_title(r'q-fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=1, ncol=1,
               frameon=1, loc=0, handlelength=2.5)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(0, 1.6)
    ax1.grid()

    ax2.plot(xPlot, func4(xPlot, q=.9), '-o', mew=0,
             color=c[0], lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=.9, b=1.5), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, a=1.5, q=.9), '-o', mew=0,
             color=c[2], lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=1.2), '-o', mew=0,
             color=c[3], lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=1.5), '-o', mew=0,
             color=c[4], lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[5], lw=2, ms=7)
    ax2.set_xlim([-3, 3])
    ax2.set_xlabel(r'$ \log x$', fontsize=20)
    ax2.set_ylabel(r'$ a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac {q}{1-q}}$',
                   fontsize=20)
    ax2.grid()
    ax2.set_xscale('log')

    ax3.plot(xPlot, func4(xPlot, q=.9), '-o', mew=0,
             color=c[0], lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=.9, b=1.5), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, a=1.5, q=.9), '-o', mew=0,
             color=c[2], lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=1.2), '-o', mew=0,
             color=c[3], lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=1.5), '-o', mew=0,
             color=c[4], lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[5], lw=2, ms=7)
    ax3.set_xlim(-3, 3)
    ax3.set_ylim(y1, y2)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$\log \left(a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac {q}{1-q}} \right)$',
                   fontsize=20)
    ax3.grid()
    ax3.set_yscale('log')

    ax4.plot(xPlot, func4(xPlot, q=.9), '-o', mew=0,
             color=c[0], lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=.9, b=1.5), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, a=1.5, q=.9), '-o', mew=0,
             color=c[2], lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=1.2), '-o', mew=0,
             color=c[3], lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=1.5), '-o', mew=0,
             color=c[4], lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[5], lw=2, ms=7)
    ax4.set_ylim(y1, y2)
    ax4.set_xlabel(r'$ \log x $', fontsize=20)
    ax4.set_ylabel(r'$ \log \left(a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac {q}{1-q}}\right)$',
                   fontsize=20)
    ax4.grid()
    ax4.set_xscale('log')
    ax4.set_yscale('log')

if CompareFits:
    x1 = 10 ** -1
    x2 = 10 ** 0
    y1 = 1.2 * 10 ** -1
    y2 = 1.5 * 10 ** 0

    ax1.plot(xPlot, func2(xPlot), '-o', mew=0,
             color=c[0], label=r'$a = 1, b = \frac{1}{2}$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[1], label=r'$a = 1, q=\frac{5}{3}, b = 1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot), '-o', mew=0,
             color=c[2], label=r'$a = 1, q=\frac{1}{2}, b = 1 $', lw=2, ms=7)
    ax1.set_ylabel(r'y', fontsize=20)
    ax1.set_title(r'Comparison of fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=1, ncol=1,
               frameon=1, loc=0, handlelength=2.5)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(0, 1.2)
    ax1.grid()

    ax2.plot(xPlot, func2(xPlot), '-o', mew=0, color=c[0], lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot), '-o', mew=0, color=c[2], lw=2, ms=7)
    ax2.set_xlim(x1, 5 * x2)
    ax2.set_ylim(0, 1.2)
    ax2.grid()
    ax2.set_xscale('log')

    ax3.plot(xPlot, func2(xPlot), '-o', mew=0, color=c[0], lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot), '-o', mew=0, color=c[2], lw=2, ms=7)
    ax3.set_xlim(-2.5, 2.5)
    ax3.set_ylim(y1, y2)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$\log y$', fontsize=20)
    ax3.grid()
    ax3.set_yscale('log')

    ax4.plot(xPlot, func2(xPlot), '-o', mew=0, color=c[0], lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=5. / 3.), '-o', mew=0,
             color=c[1], lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot), '-o', mew=0, color=c[2], lw=2, ms=7)
    ax4.set_xlim(x1, 3 * x2)
    ax4.set_ylim(y1, y2)
    ax4.set_xlabel(r'$\log x$', fontsize=20)
    ax4.grid()
    ax4.set_xscale('log')
    ax4.set_yscale('log')

plt.show()
