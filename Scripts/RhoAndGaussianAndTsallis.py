# -*- coding: utf-8 -*-

'''This script defines Rho, Gaussian and Tsallis fitting functions,
and compares the last two visually.

Density profiles used:
Hernquist
NFW
'''

import numpy as np
import matplotlib.pyplot as plt


def rho_Hernquist(rho_0_HQ, rs, x):
    """Return Hernquist density profile."""
    return rho_0_HQ / (x / rs * (1 + x / rs) ** 3)


def rho_NFW(rho_0_NFW, rs, x):
    """Return NFW density profile."""
    return rho_0_NFW / (x / rs * (1 + x / rs) ** 2)


# Constants -------------------------------------------------------------------

log10x = 1
x = 10.0 ** log10x
# Renames:
# LOG_10_X = 1
# X = 10.0 ** LOG_10_X

# Gaussian functions ----------------------------------------------------------


def func1(x, a, b):
    """Return Gaussian function."""
    return a * x * np.exp(-b * x ** 2.)


def func2(x, a=1, b=.5):
    """Return Gaussian function."""
    return a * np.exp(-b * x ** 2.)


def func_1_add(x, a, b, c):
    """Return Gaussian function."""
    return a * x * np.exp(-b * x ** 2) + c


def func_2_add(x, a, b, c):
    """Return Gaussian function."""
    return a * np.exp(-b * x ** 2) + c


def func3(x, a, b):
    """Return Gaussian function."""
    return a * x ** 2 * np.exp(-b * x ** 2.)


def func1Log(log10x, a, b):
    """Return Gaussian function."""
    return a * x * np.exp(-b * x ** 2.)


def func2Log(log10x, a, b):
    """Return Gaussian function."""
    return a * np.exp(-b * x ** 2.)


def func3Log(log10x, a, b):
    """Return Gaussian function."""
    return a * x ** 2 * np.exp(-b * x ** 2.)


# Tsallis functions -----------------------------------------------------------


def func4(x, a=1, q=.5, b=1):
    """Return Tsallis function."""
    return a * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func5(x, b, q):
    """Return Tsallis function."""
    return (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func4Log(log10x, a, q, b):
    """Return Tsallis function."""
    return a * x * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func_6(x, a, b, q):
    """Return Tsallis function."""
    return a * x * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


def func_7_log(log10x, a, b, q):
    """Return Tsallis function."""
    x = 10.0 ** log10x
    return a * x ** 2 * (1. - (1. - q) * b * x ** 2.) ** (q / (1. - q))


# Figure switches -------------------------------------------------------------
GaussianFits = 0
QFits = 0
CompareFits = 0

# Figure definitions ----------------------------------------------------------
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))
for i in range(1, 5):
    exec(f"ax{i}.grid()")
xPlot = np.linspace(-5, 5, 50)
y1 = 10 ** -3
y2 = 10 ** 1

if GaussianFits:
    ax1.plot(xPlot, func2(xPlot, b=1), 'r-o', mew=0,
             label=r'$a=1, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot, a=1.5, b=1), 'b-o', mew=0,
             label=r'$a=1.5, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot, b=1.5), 'g-o', mew=0,
             label=r'$a=1, b=1.5$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot, a=0.5, b=1), 'k-o', mew=0,
             label=r'$a=0.5, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func2(xPlot), 'm-o', mew=0,
             label=r'$a=1, b=0.5$', lw=2, ms=7)
    ax1.set_xlabel('x', fontsize=20)
    ax1.set_ylabel(r'$a e^{-b x^2}$', fontsize=20)
    ax1.set_title('Gaussian fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=1, ncol=1,
               frameon=1, loc=0, handlelength=2.5)
    ax1.set_xlim(-3, 3)

    ax2.plot(xPlot, func2(xPlot, b=1), 'r-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot, a=1.5, b=1), 'b-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot, b=1.5), 'g-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot, a=.5, b=1), 'k-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func2(xPlot), 'm-o', mew=0, lw=2, ms=7)
    ax2.set_xlim(10 ** -1, y2)
    ax2.set_ylim(0, 1.6)
    ax2.set_xlabel(r'$\log x$', fontsize=20)
    ax2.set_ylabel(r'$a e^{-b x^2}$', fontsize=20)
    ax2.set_xscale('log')

    ax3.plot(xPlot, func2(xPlot, b=1), 'r-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot, a=1.5, b=1), 'b-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot, b=1.5), 'g-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot, a=.5, b=1), 'k-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func2(xPlot), 'm-o', mew=0, lw=2, ms=7)
    ax3.set_xlim(-4, 4)
    ax3.set_ylim(y1, y2)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$ \log \left( a e^{-b x^2} \right)$', fontsize=20)
    ax3.set_yscale('log')

    ax4.plot(xPlot, func2(xPlot, b=1), 'r-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot, a=1.5, b=1), 'b-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot, b=1.5), 'g-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot, a=.5, b=1), 'k-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func2(xPlot), 'm-o', mew=0, lw=2, ms=7)
    ax4.set_xlim(-4, 4)
    ax4.set_ylim(y1, y2)
    ax4.set_xlabel(r'$\log x$', fontsize=20)
    ax4.set_ylabel(r'$\log \left(a e^{-b x^2} \right)$', fontsize=20)
    ax4.set_xscale('log')
    ax4.set_yscale('log')

if QFits:
    for i in range(1, 4):
        exec(f"ax{i}.set_xlim(-3, 3)")
    ax1.plot(xPlot, func4(xPlot, q=.9), 'r-o', mew=0,
             label=r'$a=1, q=0.9, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=.9, b=1.5), 'b-o', mew=0,
             label=r'$a=1, q=0.9, b=1.5$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, a=1.5, q=.9), 'g-o', mew=0,
             label=r'$a=1.5, q=0.9, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=1.2), 'k-o', mew=0,
             label=r'$a=1, q=1.2, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=1.5), 'm-o', mew=0,
             label=r'$a=1 , q=1.5, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=5. / 3.), 'c-o', mew=0,
             label=r'$a=1, q=\frac{5}{3}, b=1$', lw=2, ms=7)
    ax1.set_xlabel('x', fontsize=20)
    ax1.set_ylabel(r'$a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac {q}{1-q}}$',
                   fontsize=20)
    ax1.set_title('q-fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=1, ncol=1,
               frameon=1, loc=0, handlelength=2.5)
    ax1.set_ylim(0, 1.6)

    ax2.plot(xPlot, func4(xPlot, q=.9), 'r-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=.9, b=1.5), 'b-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, a=1.5, q=.9), 'g-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=1.2), 'k-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=1.5), 'm-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=5. / 3.), 'c-o', mew=0, lw=2, ms=7)
    ax2.set_xlabel(r'$\log x$', fontsize=20)
    ax2.set_ylabel(r'$a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac{q}{1-q}}$',
                   fontsize=20)
    ax2.set_xscale('log')

    ax3.plot(xPlot, func4(xPlot, q=.9), 'r-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=.9, b=1.5), 'b-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, a=1.5, q=.9), 'g-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=1.2), 'k-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=1.5), 'm-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=5. / 3.), 'c-o', mew=0, lw=2, ms=7)
    ax3.set_ylim(y1, y2)
    ax3.set_xlabel('x', fontsize=20)
    ax3.set_ylabel(r'$\log \left(a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac {q}{1-q}} \right)$',
                   fontsize=20)
    ax3.set_yscale('log')

    ax4.plot(xPlot, func4(xPlot, q=.9), 'r-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=.9, b=1.5), 'b-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, a=1.5, q=.9), 'g-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=1.2), 'k-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=1.5), 'm-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=5. / 3.), 'c-o', mew=0, lw=2, ms=7)
    ax4.set_ylim(y1, y2)
    ax4.set_xlabel(r'$\log x$', fontsize=20)
    ax4.set_ylabel(r'$\log \left(a \cdot (1-(1-q)\cdot b\cdot x^2)^{\frac {q}{1-q}}\right)$',
                   fontsize=20)
    ax4.set_xscale('log')
    ax4.set_yscale('log')

if CompareFits:
    x1 = 10 ** -1
    x2 = 10 ** 0
    y1 = 1.2 * 10 ** -1
    y2 = 1.5 * 10 ** 0

    ax1.plot(xPlot, func2(xPlot), 'r-o', mew=0, label=r'$a=1, b=\frac{1}{2}$',
             lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot, q=5./3.), 'b-o', mew=0,
             label=r'$a=1, q=\frac{5}{3}, b=1$', lw=2, ms=7)
    ax1.plot(xPlot, func4(xPlot), 'g-o', mew=0,
             label=r'$a=1, q=\frac{1}{2}, b=1$', lw=2, ms=7)
    ax1.set_ylabel('y', fontsize=20)
    ax1.set_title('Comparison of fits', fontsize=20)
    ax1.legend(prop=dict(size=13), numpoints=1, ncol=1,
               frameon=1, loc=0, handlelength=2.5)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(0, 1.2)

    ax2.plot(xPlot, func2(xPlot), 'r-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot, q=5. / 3.), 'b-o', mew=0, lw=2, ms=7)
    ax2.plot(xPlot, func4(xPlot), 'g-o', mew=0, lw=2, ms=7)
    ax2.set_xlim(x1, 5 * x2)
    ax2.set_ylim(0, 1.2)
    ax2.set_xscale('log')

    ax3.plot(xPlot, func2(xPlot), 'r-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot, q=5. / 3.), 'b-o', mew=0, lw=2, ms=7)
    ax3.plot(xPlot, func4(xPlot), 'g-o', mew=0, lw=2, ms=7)
    ax3.set_xlim(-2.5, 2.5)
    ax3.set_ylim(y1, y2)
    ax3.set_xlabel(r'x', fontsize=20)
    ax3.set_ylabel(r'$\log y$', fontsize=20)
    ax3.set_yscale('log')

    ax4.plot(xPlot, func2(xPlot), 'r-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot, q=5./3.), 'b-o', mew=0, lw=2, ms=7)
    ax4.plot(xPlot, func4(xPlot), 'g-o', mew=0, lw=2, ms=7)
    ax4.set_xlim(x1, 3 * x2)
    ax4.set_ylim(y1, y2)
    ax4.set_xlabel(r'$\log x$', fontsize=20)
    ax4.set_xscale('log')
    ax4.set_yscale('log')

plt.show()
