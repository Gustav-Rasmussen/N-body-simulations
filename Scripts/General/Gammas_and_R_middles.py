import numpy as np

# Choices: Gamma, (R_limit_32, R_limit_500, R_limit_5000, R_limit_10000)

F = 'IamAtestFileName'
Gammas = [-1.5, -2.0, -2.5, -3.0]
Gamma = Gammas[1]
Beta = 1.
keep_IC_R_middle = 0
new_R_middle = 0
R_bin_automatic = 0

# Analyse larger volume of structure
R_limit_32 = 0
R_limit_500 = 0
R_limit_5000 = 0
R_limit_10000 = 0
large_R_middle = 0
# Analyse larger volume of structure, sets R_limit to 10000
largest_R_limit = 0
# Analyse large volume of structure, sets R_limit to 5000
large_R_limit = 0

if large_R_middle:
    # R_middle = 10 ** 1.3
    R_middle = 10 ** 1.5
# print('R_middle = ', R_middle)

# Reduce number of radial bins in analysis code.
# This makes them larger and they therefore contain more particles.
bins_202 = 0
bins_102 = 0
bins_52 = 0
bins_22 = 0

larger_fewer_bins = 1

R_limit = 'R_limit_10000'
R_limit_Dict = {'R_limit_10000': 10000.,
                'R_limit_5000': 5000.,
                'R_limit_500': 500.,
                'R_limit_32': 32.,
                'largest_R_limit': 10000.,
                'large_R_limit': 5000.
                }
R_limit = R_limit_Dict.get(R_limit, 500.)
F += '_R_limit_' + R_limit

nr_bins = 'bins_202'
bins_Dict = {'bins_202': 202,
             'bins_102': 102,
             'larger_fewer_bins': 22
             }
nr_bins = bins_Dict.get(nr_bins, 52)
F += f'{nr_bins}_radial_bins'


if keep_IC_R_middle:  # For R_limit_10000 and 20 bins.
    if F.startswith('HQ10000_G'):
        R_middles = [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** -.30]
    if F.startswith(('OM_', 'test2_')):
        R_middles = [0, 0, 0, 0]

new_R_middle_dict = {'A_HQ10000_G1.0_0_000': [10 ** -.7, 10 ** -.35, 1., 10 ** .25],
                     'A_HQ10000_G1.0_5_005': [10 ** -.38, 10 ** -.18, 1., 10 ** .4],
                     'A_HQ10000_G1.0_10_005': [10 ** -.35, 10 ** -.18, 1., 10 ** .4],
                     'A_HQ10000_G1.0_40_005': [10 ** -.08, 1., 10 ** .07, 10 ** .38],
                     'A_HQ10000_G1.0_48_009': [10 ** -.08, 1., 10 ** .07, 10 ** .25],
                     'A_HQ10000_G1.0_48_093': [10 ** -.05, 1., 10 ** .07, 10 ** .57],
                     'B_HQ10000_G1.0_0_000': [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** .3],
                     'B_HQ10000_G1.0_5_005': [10 ** -.4, 10 ** -.15, 10 ** .1, 10 ** .25],
                     'B_HQ10000_G1.0_10_005': [10 ** -.25, 10 ** -.14, 1., 10 ** .4],
                     'B_HQ10000_G1.0_198_000': [10 ** .1, 10 ** .2, 10 ** .3, 10 ** .45],
                     'B_HQ10000_G1.0_198_093': [10 ** .1, 10 ** .15, 10 ** .25, 10 ** .5],
                     'B_HQ10000_G1.0_199_093': [10 ** .12, 10 ** .2, 10 ** .25, 10 ** .42],
                     'CS1_OM10000_G1.0_0_000': [10 ** -.95, 10 ** -.25, 1., 10 ** .35],
                     'CS2_OM10000_G1.0_0_000': [10 ** -1.1, 10 ** -.4, 1., 10 ** .4],
                     'CS3_OM10000_G1.0_0_000': [10 ** -.7, 10 ** -.4, 1., 10 ** .4],
                     'CS4_OM10000_G1.0_0_000': [10 ** -.75, 10 ** -.4, 1., 10 ** .3],
                     'CS4_OM10000_G1.0_48_093': [10 ** -.05, 1., 10 ** .08, 10 ** .5],
                     'CS5_OM10000_G1.0_0_000': [10 ** -.75, 10 ** -.4, 1., 10 ** .3],
                     'CS5_OM10000_G1.0_48_093': [10 ** -.05, 1., 10 ** .08, 10 ** .7],
                     'CS6_OM10000_G1.0_0_000': [10 ** -.8, 10 ** -.25, 1., 10 ** .3],
                     'CS6_OM10000_G1.0_48_093': [10 ** -.05, 1., 10 ** .08, 10.],
                     'DS1_OM10000_G1.0_0_000': [10 ** -.4, 10 ** -.2, 10 ** .05, 10 ** .2],
                     'DS1_OM10000_G1.0_49_093': [10 ** -.25, 10 ** -.1, 10 ** .1, 10 ** .65],
                     'Soft_D2_HQ10000_G1.0_0_000': [10 ** -.45, 10 ** -.2, 10 ** .05, 10 ** .2],
                     'Soft_D2_HQ10000_G1.0_49_093': [10 ** -.3, 10 ** -.1, 10 ** .1, 10 ** 1.4],
                     'E_HQ10000_G1.0_0_000': [10 ** -.75, 10 ** -.4, 1., 10 ** .4],
                     'E_HQ10000_G1.0_198_093': [10 ** -.3, 10 ** -.1, 10 ** .1, 10 ** .4],
                     'Hernquist10000_G1.0_0_000': [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** -.30],
                     'Hernquist10000_G1.2_1_005': [10 ** -.55, 10 ** -.4, 10 ** -.1, 10 ** .2],
                     'Hernquist10000_G0.8_2_005': [0, 0, 0, 0],
                     'Hernquist10000_G1.2_3_005': [10 ** -.6, 10 ** -.4, 10 ** .0, 10 ** .4],
                     'Hernquist10000_G1.2_5_005': [10 ** -.45, 10 ** -.35, 10 ** -.1, 10 ** .45],
                     'Hernquist10000_G1.2_7_005': [10 ** -.35, 10 ** -.25, 10 ** -.1, 10 ** .48],
                     'Hernquist10000_G1.2_9_005': [10 ** -.35, 10 ** -.3, 10 ** -.15, 10 ** .5],
                     'Hernquist10000_G1.0_10_009': [10 ** -.25, 10 ** -.15, 10 ** .0, 10 ** .5],
                     'test2_Hernquist10000_G1.0_0_000': [10 ** -.7, 10 ** -.38, 10 ** -.0, 10 ** .25],
                     'test2_Hernquist10000_G1.0_5_005': [10 ** -.5, 10 ** -.18, 10 ** .0, 10 ** .45],
                     'test2_Hernquist10000_G1.0_10_005': [10 ** -.4, 10 ** -.2, 10 ** .0, 10 ** .38],
                     'test2_Hernquist10000_G1.0_15_005': [10 ** -.25, 10 ** -.14, 10 ** .0, 10 ** .38],
                     'test2_Hernquist10000_G1.0_20_005': [10 ** -.24, 10 ** -.12, 10 ** .0, 10 ** .5],
                     'test2_Hernquist10000_G1.0_25_005': [10 ** -.17, 10 ** -.08, 10 ** .05, 10 ** .45]
                     }

if new_R_middle:  # Choose new R_middle for each file.
    R_middles = new_R_middle_dict.get(F, "No such filename")

Gamma_Rmiddle_Dict = {Gammas[i]: R_middles[i] for i in range(4)}
R_middle = Gamma_Rmiddle_Dict.get(Gamma, "Invalid Gamma value")


def R_bin_automatic(R_middle, x, R):
    '''Make R_limit_min and R_limit_max selection automatic.'''
    R_limit_min, R_limit_max = R_middle
    a = 0  # makes sure the while loop is entered.
    x0 = x
    while (len(x0) < 10000 or a == 0):
        R_limit_min -= .000005
        R_limit_max += .000005
        a += 1
        GoodIDs = np.where((R < R_limit_max) * (R > R_limit_min))
        x0 = x[GoodIDs[0]]
    return R_limit_min, R_limit_max


if R_bin_automatic:
    R_limit_min, R_limit_max = R_bin_automatic(R_middle, x, R)
