
# Choices: Gamma, (R_limit_32, R_limit_500, R_limit_5000, R_limit_10000)

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

if R_limit_10000:
    R_limit = 10000.
    F += '_R_limit_10000'
elif R_limit_5000:
    R_limit = 5000.
    F += '_R_limit_5000'
elif R_limit_500:
    R_limit = 500.
    F += '_R_limit_500'
elif R_limit_32:
    R_limit = 32.
    F += '_R_limit_32'

if largest_R_limit:
    R_limit = 10000.
    F += '_R_limit_10000'
elif large_R_limit:
    R_limit = 5000.
    F += '_R_limit_5000'
else:
    R_limit = 500.
    # F += '_R_limit_500'

if bins_202:
    nr_binning_bins = 202
    F += '_200_radial_bins'
elif bins_102:
    nr_binning_bins = 102
    F += '_100_radial_bins'
elif larger_fewer_bins:
    nr_binning_bins = 22
    F += '_20_radial_bins'
else:
    nr_binning_bins = 52

Gammas = [-1.5, -2.0, -2.5, -3.0]
Gamma = Gammas[1]
Beta = 1.

keep_IC_R_middle = 0
new_R_middle = 0
R_bin_automatic = 0

if keep_IC_R_middle:  # For R_limit_10000 and 20 bins.
    if F.startswith('HQ10000_G'):
        R_middles = [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** -.30]
    if F.startswith(('OM_', 'test2_')):
        R_middles = [0, 0, 0, 0]
if new_R_middle:  # Choose new R_middle for each file.
    # A
    if F == 'A_HQ10000_G1.0_0_000':  # 0.th/IC file
        R_middles = [10 ** -.7, 10 ** -.35, 1., 10 ** .25]
    if F == 'A_HQ10000_G1.0_5_005':  # 5.th file
        R_middles = [10 ** -.38, 10 ** -.18, 1., 10 ** .4]
    if F == 'A_HQ10000_G1.0_10_005':  # 10.th file
        R_middles = [10 ** -.35, 10 ** -.18, 1., 10 ** .4]
    if F == 'A_HQ10000_G1.0_40_005':  # 198.th file
        R_middles = [10 ** -.08, 1., 10 ** .07, 10 ** .38]
    if F == 'A_HQ10000_G1.0_48_009':
        R_middles = [10 ** -.08, 1., 10 ** .07, 10 ** .25]
    if F == 'A_HQ10000_G1.0_48_093':
        R_middles = [10 ** -.05, 1., 10 ** .07, 10 ** .57]
    # B
    if F == 'B_HQ10000_G1.0_0_000':  # 0.th/IC file
        R_middles = [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** .3]
    if F == 'B_HQ10000_G1.0_5_005':  # 5.th file
        R_middles = [10 ** -.4, 10 ** -.15, 10 ** .1, 10 ** .25]
    if F == 'B_HQ10000_G1.0_10_005':  # 10.th file
        R_middles = [10 ** -.25, 10 ** -.14, 1., 10 ** .4]
    if F == 'B_HQ10000_G1.0_198_000':  # 198.th file
        R_middles = [10 ** .1, 10 ** .2, 10 ** .3, 10 ** .45]
    if F == 'B_HQ10000_G1.0_198_093':
        R_middles = [10 ** .1, 10 ** .15, 10 ** .25, 10 ** .5]
    if F == 'B_HQ10000_G1.0_199_093':
        R_middles = [10 ** .12, 10 ** .2, 10 ** .25, 10 ** .42]
    # CS1
    if F == 'CS1_OM10000_G1.0_0_000':
        R_middles = [10 ** -.95, 10 ** -.25, 1., 10 ** .35]
    # CS2
    if F == 'CS2_OM10000_G1.0_0_000':
        R_middles = [10 ** -1.1, 10 ** -.4, 1., 10 ** .4]
    # CS3
    if F == 'CS3_OM10000_G1.0_0_000':
        R_middles = [10 ** -.7, 10 ** -.4, 1., 10 ** .4]
    # CS4
    if F == 'CS4_OM10000_G1.0_0_000':
        R_middles = [10 ** -.75, 10 ** -.4, 1., 10 ** .3]
    if F == 'CS4_OM10000_G1.0_48_093':
        R_middles = [10 ** -.05, 1., 10 ** .08, 10 ** .5]
    # CS5
    if F == 'CS5_OM10000_G1.0_0_000':
        R_middles = [10 ** -.75, 10 ** -.4, 1., 10 ** .3]
    if F == 'CS5_OM10000_G1.0_48_093':
        R_middles = [10 ** -.05, 1., 10 ** .08, 10 ** .7]
    # CS6
    if F == 'CS6_OM10000_G1.0_0_000':
        R_middles = [10 ** -.8, 10 ** -.25, 1., 10 ** .3]
    if F == 'CS6_OM10000_G1.0_48_093':
        R_middles = [10 ** -.05, 1., 10 ** .08, 10.]
    # DS1
    if F == 'DS1_OM10000_G1.0_0_000':
        R_middles = [10 ** -.4, 10 ** -.2, 10 ** .05, 10 ** .2]
    if F == 'DS1_OM10000_G1.0_49_093':
        R_middles = [10 ** -.25, 10 ** -.1, 10 ** .1, 10 ** .65]
    # Soft_D2
    if F == 'Soft_D2_HQ10000_G1.0_0_000':
        R_middles = [10 ** -.45, 10 ** -.2, 10 ** .05, 10 ** .2]
    if F == 'Soft_D2_HQ10000_G1.0_49_093':
        R_middles = [10 ** -.3, 10 ** -.1, 10 ** .1, 10 ** 1.4]
    # E
    if F == 'E_HQ10000_G1.0_0_000':
        R_middles = [10 ** -.75, 10 ** -.4, 1., 10 ** .4]
    if F == 'E_HQ10000_G1.0_198_093':
        R_middles = [10 ** -.3, 10 ** -.1, 10 ** .1, 10 ** .4]
    # test
    if F == 'Hernquist10000_G1.0_0_000':  # 0.th/IC file
        R_middles = [10 ** -.70, 10 ** -.25, 10 ** -.0, 10 ** -.30]
    if F == 'Hernquist10000_G1.2_1_005':  # 1.st file
        R_middles = [10 ** -.55, 10 ** -.4, 10 ** -.1, 10 ** .2]
    if F == 'Hernquist10000_G0.8_2_005':  # 2.nd file
        R_middles = [0, 0, 0, 0]
    if F == 'Hernquist10000_G1.2_3_005':  # 3.rd file
        R_middles = [10 ** -.6, 10 ** -.4, 10 ** .0, 10 ** .4]
    if F == 'Hernquist10000_G1.2_5_005':  # 5.th file
        R_middles = [10 ** -.45, 10 ** -.35, 10 ** -.1, 10 ** .45]
    if F == 'Hernquist10000_G1.2_7_005':  # 7.th file
        R_middles = [10 ** -.35, 10 ** -.25, 10 ** -.1, 10 ** .48]
    if F == 'Hernquist10000_G1.2_9_005':  # 9.th file
        R_middles = [10 ** -.35, 10 ** -.3, 10 ** -.15, 10 ** .5]
    if F == 'Hernquist10000_G1.0_10_009':  # 10.th file
        R_middles = [10 ** -.25, 10 ** -.15, 10 ** .0, 10 ** .5]
    # test2
    if F == 'test2_' + 'Hernquist10000_G1.0_0_000':  # 0.th/IC file
        R_middles = [10 ** -.7, 10 ** -.38, 10 ** -.0, 10 ** .25]
    if F == 'test2_' + 'Hernquist10000_G1.0_5_005':  # 5.th file
        R_middles = [10 ** -.5, 10 ** -.18, 10 ** .0, 10 ** .45]
    if F == 'test2_' + 'Hernquist10000_G1.0_10_005':  # 10.th file
        R_middles = [10 ** -.4, 10 ** -.2, 10 ** .0, 10 ** .38]
    if F == 'test2_' + 'Hernquist10000_G1.0_15_005':  # 15.th file
        R_middles = [10 ** -.25, 10 ** -.14, 10 ** .0, 10 ** .38]
    if F == 'test2_' + 'Hernquist10000_G1.0_20_005':  # 20.th file
        R_middles = [10 ** -.24, 10 ** -.12, 10 ** .0, 10 ** .5]
    if F == 'test2_' + 'Hernquist10000_G1.0_25_005':  # 25.th file
        R_middles = [10 ** -.17, 10 ** -.08, 10 ** .05, 10 ** .45]

if Gamma == Gammas[0]:
    R_middle = R_middles[0]
elif Gamma == Gammas[1]:
    R_middle = R_middles[1]
elif Gamma == Gammas[2]:
    R_middle = R_middles[2]
elif Gamma == Gammas[3]:
    R_middle = R_middles[3]

# make R_limit_min and R_limit_max selection automatic
if R_bin_automatic:
    R_limit_min, R_limit_max = R_middle
    a = 0  # makes sure the while loop is entered.
    x0 = x
    while (len(x0) < 10000 or a == 0):
        R_limit_min -= .000005
        R_limit_max += .000005
        a += 1
        GoodIDs = np.where((R < R_limit_max) * (R > R_limit_min))
        x0 = x[GoodIDs[0]]
