from pathlib import Path

Desktop_path = Path.cwd()
Stable_path = 'Energy_exchange/Stable_structures/'
# 'a', b', 'c', 'd'
figure_path = Desktop_path + Stable_path + 'figures/II' + 'a' + '/'
Martin_path = 'Martin_IC_and_Final_Edd_and_OM/'
# 'a', b', 'c', 'd'
text_files_path = Desktop_path + Stable_path + 'text_files/II' + 'a' + '/'

IIa = 0
IIb = 0
IIc = 0
IId = 0

# R32
file_list_Soft_B_Rlimit32_50bins = [(text_files_path + 'Soft_B/' + 'Soft_B_E_G2P_0_000_R_limit_32_50_radial_bins.txt', text_files_path + 'Soft_B_E_G2P_0_000_R_limit_32_50_radial_bins'),
                                    (text_files_path + 'Soft_B/' + 'Soft_B_E_G2P_20_005_R_limit_32_50_radial_bins.txt', text_files_path + 'Soft_B_E_G2P_20_005_R_limit_32_50_radial_bins')]
file_list_Soft_B_control_Rlimit32_50bins = [(text_files_path + 'Soft_B/' + 'Soft_B_E_20_005_R_limit_32_50_radial_bins.txt', text_files_path + 'Soft_B_E_20_005_R_limit_32_50_radial_bins')]
'''
file_list_CS1_Rlimit32_10bins = [(text_files_path + 'CS1/' + 'CS1_E_G2P_0_000_R_limit_32_10_radial_bins.txt', text_files_path + 'CS1_E_G2P_0_000_R_limit_32_10_radial_bins'),
                                 (text_files_path + 'CS1/' + 'CS1_E_G2P_20_005_R_limit_32_10_radial_bins.txt', text_files_path + 'CS1_E_G2P_20_005_R_limit_32_10_radial_bins')]
file_list_CS1_control_Rlimit32_10bins = [(text_files_path + 'CS1/' + 'CS1_E_20_005_R_limit_32_10_radial_bins.txt', text_files_path + 'CS1_E_20_005_R_limit_32_10_radial_bins')]
'''

if IIa:
    snaps_base = ['0_000', '10_005', '20_005', '30_005', '40_021']
    file_list_CS4_Rlimit32_20bins = [(text_files_path + 'CS4/' + 'CS4_E_G2P_' + snaps_base[i] + '_R_limit_32_20_radial_bins.txt',
                                      text_files_path + 'CS4_E_G2P_' + snaps_base[i] + '_R_limit_32_20_radial_bins') for i in range(5)]

    snaps = ['G2P_0_005', '0_005_P2G', 'G2P_1_005', '1_005_P2G', 'G2P_2_005', '2_005_P2G',
             'G2P_3_005', '3_005_P2G', 'G2P_4_005', '4_005_P2G', 'G2P_5_005', '5_005_P2G', 'G2P_6_005']
    file_list_Test_CS4_Rlimit32_20bins = [(text_files_path + 'Test_CS4/' + 'Test_CS4_E_' + snaps[i] + '_R_limit_32_20_radial_bins.txt',
                                           text_files_path + 'Test_CS4_E_' + snaps[i] + '_R_limit_32_20_radial_bins') for i in range(13)]

    snaps = ['0_005', '1_041', '2_041', '3_041']
    file_list_Test_CS4_10tdyn_Rlimit32_20bins = [(text_files_path + 'Test_CS4_10tdyn/' + 'Test_CS4_10tdyn_E_G2P_' + snaps[i] + '_R_limit_32_20_radial_bins.txt',
                                                  text_files_path + 'Test_CS4_E_G2P_' + snaps[i] + '_R_limit_32_20_radial_bins') for i in range(4)]

    file_list_Soft_D2_Rlimit32_20bins = [(text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_' + snaps_base[i] + '_R_limit_32_20_radial_bins.txt',
                                          text_files_path + 'Soft_D2_E_G2P_' + snaps_base[i] + '_R_limit_32_20_radial_bins') for i in range(5)]

    snaps = ['G2P_0_005', '0_005_P2G', 'G2P_1_005', '1_005_P2G', 'G2P_2_005', '2_005_P2G',
             'G2P_3_005', '3_005_P2G', 'G2P_4_005', '4_005_P2G', 'G2P_5_005', '5_005_P2G', 'G2P_6_005']
    file_list_Test_D2_Rlimit32_20bins = [(text_files_path + 'Test_D2/' + 'Test_D2_E_' + snaps[i] + '_R_limit_32_20_radial_bins.txt',
                                          text_files_path + 'Test_D2_E_' + snaps[i] + '_R_limit_32_20_radial_bins') for i in range(13)]

if IIb:
    file_list_CS4_Rlimit32_20bins = [(text_files_path + 'CS4/' + 'IIb_CS4_E_G2P_0_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_0_005_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS4/' + 'IIb_CS4_E_G2P_20_021_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_20_021_R_limit_32_20_radial_bins')]

    file_list_Soft_D2_Rlimit32_20bins = [(text_files_path + 'Soft_D2/' + 'IIb_Soft_D2_E_G2P_0_005_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_0_005_R_limit_32_20_radial_bins'),
                                         (text_files_path + 'Soft_D2/' + 'IIb_Soft_D2_E_G2P_20_021_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_20_021_R_limit_32_20_radial_bins')]
if IIc:
    file_list_CS4_Rlimit32_20bins = [(text_files_path + 'CS4/' + 'IIc_CS4_E_G2P_0_000_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_0_000_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS4/' + 'IIc_CS4_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_10_005_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS4/' + 'IIc_CS4_E_G2P_20_021_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_20_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS4/' + 'IIc_CS4_E_G2P_40_021_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_40_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS4/' + 'IIc_CS4_E_G2P_40_021_R_limit_32_50_radial_bins.txt', text_files_path + 'CS4_E_G2P_40_021_R_limit_32_50_radial_bins')]

    file_list_CS5_Rlimit32_20bins = [(text_files_path + 'CS5/' + 'IIc_CS5_E_G2P_0_000_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_0_000_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS5/' + 'IIc_CS5_E_G2P_20_021_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_20_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS5/' + 'IIc_CS5_E_G2P_40_021_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_40_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS5/' + 'IIc_CS5_E_G2P_40_021_R_limit_32_50_radial_bins.txt', text_files_path + 'CS5_E_G2P_40_021_R_limit_32_50_radial_bins')]

    file_list_CS6_Rlimit32_20bins = [(text_files_path + 'CS6/' + 'IIc_CS6_E_G2P_0_000_R_limit_32_20_radial_bins.txt', text_files_path + 'CS6_E_G2P_0_000_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS6/' + 'IIc_CS6_E_G2P_20_021_R_limit_32_20_radial_bins.txt', text_files_path + 'CS6_E_G2P_20_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS6/' + 'IIc_CS6_E_G2P_40_021_R_limit_32_20_radial_bins.txt', text_files_path + 'CS6_E_G2P_40_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS6/' + 'IIc_CS6_E_G2P_40_021_R_limit_32_50_radial_bins.txt', text_files_path + 'CS6_E_G2P_40_021_R_limit_32_50_radial_bins')]

    file_list_DS1_Rlimit32_20bins = [(text_files_path + 'DS1/' + 'IIc_DS1_E_G2P_0_000_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_0_000_R_limit_32_20_radial_bins' ),
                                     (text_files_path + 'DS1/' + 'IIc_DS1_E_G2P_40_021_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_40_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'DS1/' + 'IIc_DS1_E_G2P_60_021_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_60_021_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'DS1/' + 'IIc_DS1_E_G2P_60_021_R_limit_32_50_radial_bins.txt', text_files_path + 'DS1_E_G2P_60_021_R_limit_32_50_radial_bins')]

    file_list_Soft_D2_Rlimit32_20bins = [(text_files_path + 'Soft_D2/' + 'IIc_Soft_D2_E_G2P_0_000_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_0_000_R_limit_32_20_radial_bins' ),
                                         (text_files_path + 'Soft_D2/' + 'IIc_Soft_D2_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_10_005_R_limit_32_20_radial_bins'),
                                         (text_files_path + 'Soft_D2/' + 'IIc_Soft_D2_E_G2P_20_021_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_20_021_R_limit_32_20_radial_bins'),
                                         (text_files_path + 'Soft_D2/' + 'IIc_Soft_D2_E_G2P_30_021_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_30_021_R_limit_32_20_radial_bins'),
                                         (text_files_path + 'Soft_D2/' + 'IIc_Soft_D2_E_G2P_40_021_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_40_021_R_limit_32_20_radial_bins'),
                                         (text_files_path + 'Soft_D2/' + 'IIc_Soft_D2_E_G2P_60_021_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_60_021_R_limit_32_20_radial_bins'),
                                         (text_files_path + 'Soft_D2/' + 'IIc_Soft_D2_E_G2P_60_021_R_limit_32_50_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_60_021_R_limit_32_50_radial_bins')]

file_list_CS4_control_Rlimit32_20bins = [(text_files_path + 'CS4/' + 'CS4_E_20_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_20_005_R_limit_32_20_radial_bins')]
'''
file_list_CS5_Rlimit32_20bins = [(text_files_path + 'CS5/' + 'CS5_E_G2P_0_000_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_0_000_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'CS5/' + 'CS5_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_10_005_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'CS5/' + 'CS5_E_G2P_20_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_20_005_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'CS5/' + 'CS5_E_G2P_30_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_30_005_R_limit_32_20_radial_bins')]
'''
file_list_CS5_control_Rlimit32_20bins = [(text_files_path + 'CS5/' + 'CS5_E_20_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_20_005_R_limit_32_20_radial_bins')]
'''
file_list_CS6_Rlimit32_20bins = [(text_files_path + 'CS6/' + 'CS6_E_G2P_0_000_R_limit_32_20_radial_bins.txt',text_files_path + 'CS6_E_G2P_0_000_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'CS6/' + 'CS6_E_G2P_10_005_R_limit_32_20_radial_bins.txt',text_files_path + 'CS6_E_G2P_10_005_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'CS6/' + 'CS6_E_G2P_20_005_R_limit_32_20_radial_bins.txt',text_files_path + 'CS6_E_G2P_20_005_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'CS6/' + 'CS6_E_G2P_30_005_R_limit_32_20_radial_bins.txt',text_files_path + 'CS6_E_G2P_30_005_R_limit_32_20_radial_bins')]
'''
file_list_CS6_control_Rlimit32_20bins = [(text_files_path + 'CS6/' + 'CS6_E_20_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS6_E_20_005_R_limit_32_20_radial_bins')]
'''
file_list_DS1_Rlimit32_20bins = [(text_files_path + 'DS1/' + 'DS1_E_G2P_0_000_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_0_000_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'DS1/' + 'DS1_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_10_005_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'DS1/' + 'DS1_E_G2P_20_005_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_20_005_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'DS1/' + 'DS1_E_G2P_30_005_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_30_005_R_limit_32_20_radial_bins'),
                                 (text_files_path + 'DS1/' + 'DS1_E_G2P_40_021_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_40_021_R_limit_32_20_radial_bins')]
'''
file_list_DS1_control_Rlimit32_20bins = [(text_files_path + 'DS1/' + 'DS1_E_20_005_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_20_005_R_limit_32_20_radial_bins')]

if IId:
    file_list_CS4_Rlimit32_20bins = [(text_files_path + 'CS4/' + 'IId_CS4_E_G2P_0_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_0_005_R_limit_32_20_radial_bins'),
                                     (text_files_path + 'CS4/' + 'IId_CS4_E_G2P_20_013_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_20_013_R_limit_32_20_radial_bins')]

    file_list_Soft_D2_Rlimit32_20bins = [(text_files_path + 'Soft_D2/' + 'IId_Soft_D2_E_G2P_0_005_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_0_005_R_limit_32_20_radial_bins' ),
                                         (text_files_path + 'Soft_D2/' + 'IId_Soft_D2_E_G2P_20_013_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_20_013_R_limit_32_20_radial_bins')]

file_list_Soft_D2_control_Rlimit32_20bins = [(Desktop_path + Stable_path + 'text_files/IIa/' + 'Soft_D2/' + 'Soft_D2_E_20_005_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_20_005_R_limit_32_20_radial_bins')]

'''
file_list_E_Rlimit32_50bins = [(text_files_path + 'E/' + 'E_E_G2P_0_000_R_limit_32_50_radial_bins.txt', text_files_path + 'E_E_G2P_0_000_R_limit_32_50_radial_bins'),
                               (text_files_path + 'E/' + 'E_E_G2P_20_005_R_limit_32_50_radial_bins.txt', text_files_path + 'E_E_G2P_20_005_R_limit_32_50_radial_bins')]
file_list_E_control_Rlimit32_50bins = [(text_files_path + 'E/' + 'E_E_20_005_R_limit_32_50_radial_bins.txt', text_files_path + 'E_E_20_005_R_limit_32_50_radial_bins')]

# R32, IC and Final, DeltaG analysis code
file_list_DeltaG_DS1_Rlimit32_20bins = [(text_files_path + 'DS1/' + 'DS1_E_G2P_0_000_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_0_000_R_limit_32_DeltaG_20_radial_bins'),
                                        (text_files_path + 'DS1/' + 'DS1_E_G2P_30_005_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_30_005_R_limit_32_DeltaG_20_radial_bins')]
file_list_DeltaG_DS1_control_Rlimit32_20bins = [(text_files_path + 'DS1/' + 'DS1_E_20_005_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'DS1_E_20_005_R_limit_32_DeltaG_20_radial_bins')]
file_list_DeltaG_Soft_D2_Rlimit32_20bins = [(text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_0_000_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_0_000_R_limit_32_DeltaG_20_radial_bins'),
                                            (text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_10_005_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_10_005_R_limit_32_DeltaG_20_radial_bins'),
                                            (text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_20_005_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_20_005_R_limit_32_DeltaG_20_radial_bins'),
                                            (text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_30_005_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_30_005_R_limit_32_DeltaG_20_radial_bins')]
file_list_DeltaG_Soft_D2_control_Rlimit32_20bins = [(text_files_path + 'Soft_D2/' + 'Soft_D2_E_20_005_R_limit_32_DeltaG_20_radial_bins.txt', text_files_path + 'Soft_D2_20_005_R_limit_32_DeltaG_20_radial_bins')]

# R32, Run 5 and 10
file_list_Soft_B_Rlimit32_50bins_Run_5_10 = [(text_files_path + 'Soft_B/' + 'Soft_B_E_G2P_5_005_R_limit_32_50_radial_bins.txt', text_files_path + 'Soft_B_E_G2P_5_005_R_limit_32_50_radial_bins'),
                                             (text_files_path + 'Soft_B/' + 'Soft_B_E_G2P_10_005_R_limit_32_50_radial_bins.txt', text_files_path + 'Soft_B_E_G2P_10_005_R_limit_32_50_radial_bins')]
file_list_CS4_Rlimit32_20bins_Run_5_10 = [(text_files_path + 'CS4/' + 'CS4_E_G2P_5_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_5_005_R_limit_32_20_radial_bins'),
                                          (text_files_path + 'CS4/' + 'CS4_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS4_E_G2P_10_005_R_limit_32_20_radial_bins')]
file_list_CS5_Rlimit32_20bins_Run_5_10 = [(text_files_path + 'CS5/' + 'CS5_E_G2P_5_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_5_005_R_limit_32_20_radial_bins'),
                                          (text_files_path + 'CS5/' + 'CS5_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_10_005_R_limit_32_20_radial_bins')]
file_list_CS6_Rlimit32_20bins_Run_5_10 = [(text_files_path + 'CS6/' + 'CS6_E_G2P_5_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS6_E_G2P_5_005_R_limit_32_20_radial_bins'),
                                          (text_files_path + 'CS6/' + 'CS6_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'CS6_E_G2P_10_005_R_limit_32_20_radial_bins')]
file_list_DS1_Rlimit32_20bins_Run_5_10 = [(text_files_path + 'DS1/' + 'DS1_E_G2P_5_005_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_5_005_R_limit_32_20_radial_bins'),
                                          (text_files_path + 'DS1/' + 'DS1_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_10_005_R_limit_32_20_radial_bins')]
file_list_Soft_D2_Rlimit32_20bins_Run_5_10 = [(text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_5_005_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_5_005_R_limit_32_20_radial_bins'),
                                              (text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_10_005_R_limit_32_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_10_005_R_limit_32_20_radial_bins')]
file_list_E_Rlimit32_50bins_Run_5_10 = [(text_files_path + 'E/' + 'E_E_G2P_5_005_R_limit_32_50_radial_bins.txt', text_files_path + 'E_E_G2P_5_005_R_limit_32_50_radial_bins'),
                                        (text_files_path + 'E/' + 'E_E_G2P_10_005_R_limit_32_50_radial_bins.txt', text_files_path + 'E_E_G2P_10_005_R_limit_32_50_radial_bins')]
'''

file_list_Soft_B_Rlimit10_20bins = [(text_files_path + 'Soft_B/' + 'Soft_B_E_G2P_0_000_R_limit_10_20_radial_bins.txt',text_files_path + 'Soft_B_E_G2P_0_000_R_limit_10_20_radial_bins'),
                                    (text_files_path + 'Soft_B/' + 'Soft_B_E_G2P_20_005_R_limit_10_20_radial_bins.txt',text_files_path + 'Soft_B_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_Soft_B_control_Rlimit10_20bins = [(text_files_path + 'Soft_B/' + 'Soft_B_E_20_005_R_limit_10_20_radial_bins.txt',text_files_path + 'Soft_B_E_20_005_R_limit_10_20_radial_bins')]
file_list_CS1_Rlimit10_20bins = [(text_files_path + 'CS1/' + 'CS1_E_G2P_0_000_R_limit_10_20_radial_bins.txt',text_files_path + 'CS1_E_G2P_0_000_R_limit_10_20_radial_bins'),
                                 (text_files_path + 'CS1/' + 'CS1_E_G2P_20_005_R_limit_10_20_radial_bins.txt',text_files_path + 'CS1_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_CS1_control_Rlimit10_20bins =  [ (text_files_path + 'CS1/' + 'CS1_E_20_005_R_limit_10_20_radial_bins.txt',text_files_path + 'CS1_E_20_005_R_limit_10_20_radial_bins')]
file_list_CS4_Rlimit10_20bins = [(text_files_path + 'CS4/' + 'CS4_E_G2P_0_000_R_limit_10_20_radial_bins.txt',text_files_path + 'CS4_E_G2P_0_000_R_limit_10_20_radial_bins'),
                                 (text_files_path + 'CS4/' + 'CS4_E_G2P_20_005_R_limit_10_20_radial_bins.txt',text_files_path + 'CS4_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_CS4_control_Rlimit10_20bins =  [ (text_files_path + 'CS4/' + 'CS4_E_20_005_R_limit_10_20_radial_bins.txt',text_files_path + 'CS4_E_20_005_R_limit_10_20_radial_bins')]
file_list_CS5_Rlimit10_20bins = [(text_files_path + 'CS5/' + 'CS5_E_G2P_0_000_R_limit_10_20_radial_bins.txt',text_files_path + 'CS5_E_G2P_0_000_R_limit_10_20_radial_bins'),
                                 (text_files_path + 'CS5/' + 'CS5_E_G2P_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'CS5_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_CS5_control_Rlimit10_20bins = [(text_files_path + 'CS5/' + 'CS5_E_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'CS5_E_20_005_R_limit_10_20_radial_bins')]
file_list_CS6_Rlimit10_20bins = [(text_files_path + 'CS6/' + 'CS6_E_G2P_0_000_R_limit_10_20_radial_bins.txt', text_files_path + 'CS6_E_G2P_0_000_R_limit_10_20_radial_bins'),
                                 (text_files_path + 'CS6/' + 'CS6_E_G2P_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'CS6_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_CS6_control_Rlimit10_20bins = [(text_files_path + 'CS6/' + 'CS6_E_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'CS6_E_20_005_R_limit_10_20_radial_bins')]
file_list_DS1_Rlimit10_20bins = [(text_files_path + 'DS1/' + 'DS1_E_G2P_0_000_R_limit_10_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_0_000_R_limit_10_20_radial_bins'),
                                 (text_files_path + 'DS1/' + 'DS1_E_G2P_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'DS1_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_DS1_control_Rlimit10_20bins = [(text_files_path + 'DS1/' + 'DS1_E_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'DS1_E_20_005_R_limit_10_20_radial_bins')]
file_list_Soft_D2_Rlimit10_20bins = [(text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_0_000_R_limit_10_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_0_000_R_limit_10_20_radial_bins'),
                                     (text_files_path + 'Soft_D2/' + 'Soft_D2_E_G2P_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'Soft_D2_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_Soft_D2_control_Rlimit10_20bins =  [ (text_files_path + 'Soft_D2/' + 'Soft_D2_E_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'Soft_D2_20_005_R_limit_10_20_radial_bins')]
file_list_E_Rlimit10_20bins = [(text_files_path + 'E/' + 'E_E_G2P_0_000_R_limit_10_20_radial_bins.txt', text_files_path + 'E_E_G2P_0_000_R_limit_10_20_radial_bins'),
                               (text_files_path + 'E/' + 'E_E_G2P_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'E_E_G2P_20_005_R_limit_10_20_radial_bins')]
file_list_E_control_Rlimit10_20bins = [(text_files_path + 'E/' + 'E_E_20_005_R_limit_10_20_radial_bins.txt', text_files_path + 'E_E_20_005_R_limit_10_20_radial_bins')]

# Sparre data
datalist_Martin_IC = [(pylab.loadtxt(f), l) for f, l in file_list_Martin_IC]
datalist_Martin_Final = [(pylab.loadtxt(f), l ) for f, l in file_list_Martin_Final]

# mass bins
# datalist_mass_bins_Soft_B = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_Soft_B]
# datalist_mass_bins_Soft_B_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_Soft_B_control]
# datalist_mass_bins_CS1 = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS1]
# datalist_mass_bins_CS1_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS1_control]
# datalist_mass_bins_CS4 = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS4]
# datalist_mass_bins_CS4_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS4_control]
# datalist_mass_bins_CS5 = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS5]
# datalist_mass_bins_CS5_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS5_control]
# datalist_mass_bins_CS6 = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS6]
# datalist_mass_bins_CS6_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_CS6_control]
# datalist_mass_bins_DS1 = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_DS1]
# datalist_mass_bins_DS1_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_DS1_control]
# datalist_mass_bins_Soft_D2 = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_Soft_D2]
# datalist_mass_bins_Soft_D2_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_Soft_D2_control]
# datalist_mass_bins_E = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_E]
# datalist_mass_bins_E_control = [(pylab.loadtxt(f), l) for f, l in file_list_mass_bins_E_control]

# Rlimit32
# datalist_Soft_B_Rlimit32_50bins = [(pylab.loadtxt(f), l) for f, l in file_list_Soft_B_Rlimit32_50bins]
# datalist_Soft_B_control_Rlimit32_50bins = [(pylab.loadtxt(f), l) for f, l in file_list_Soft_B_control_Rlimit32_50bins]
# datalist_CS1_Rlimit32_10bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS1_Rlimit32_10bins]
# datalist_CS1_control_Rlimit32_10bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS1_control_Rlimit32_10bins]
datalist_CS4_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS4_Rlimit32_20bins]
# datalist_CS4_control_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS4_control_Rlimit32_20bins]
datalist_CS5_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS5_Rlimit32_20bins]
# datalist_CS5_control_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS5_control_Rlimit32_20bins]
datalist_CS6_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS6_Rlimit32_20bins]
# datalist_CS6_control_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_CS6_control_Rlimit32_20bins]
datalist_DS1_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_DS1_Rlimit32_20bins]
# datalist_DS1_control_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_DS1_control_Rlimit32_20bins]
datalist_Soft_D2_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_Soft_D2_Rlimit32_20bins]
# datalist_Soft_D2_control_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_Soft_D2_control_Rlimit32_20bins]
# datalist_E_Rlimit32_50bins = [(pylab.loadtxt(f), l) for f, l in file_list_E_Rlimit32_50bins]
# datalist_E_control_Rlimit32_50bins = [(pylab.loadtxt(f), l) for f, l in file_list_E_control_Rlimit32_50bins]
# datalist_Test_CS4_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_Test_CS4_Rlimit32_20bins]
# datalist_Test_D2_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_Test_D2_Rlimit32_20bins]
# datalist_Test_CS4_10tdyn_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_Test_CS4_10tdyn_Rlimit32_20bins]

# R32, IC and Final, DeltaG analysis code
# datalist_DeltaG_DS1_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_DeltaG_DS1_Rlimit32_20bins]
# datalist_DeltaG_DS1_control_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_DeltaG_DS1_control_Rlimit32_20bins]
# datalist_DeltaG_Soft_D2_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_DeltaG_Soft_D2_Rlimit32_20bins]
# datalist_DeltaG_Soft_D2_control_Rlimit32_20bins = [(pylab.loadtxt(f), l) for f, l in file_list_DeltaG_Soft_D2_control_Rlimit32_20bins]

'''
# Rlimit32, Run 5 and 10
datalist_Soft_B_Rlimit32_50bins_Run_5_10 = [(pylab.loadtxt(f), l) for f, l in file_list_Soft_B_Rlimit32_50bins_Run_5_10]
datalist_CS4_Rlimit32_20bins_Run_5_10 = [(pylab.loadtxt(f), l) for f, l in file_list_CS4_Rlimit32_20bins_Run_5_10]
datalist_CS5_Rlimit32_20bins_Run_5_10 = [(pylab.loadtxt(f), l) for f, l in file_list_CS5_Rlimit32_20bins_Run_5_10]
datalist_CS6_Rlimit32_20bins_Run_5_10 = [(pylab.loadtxt(f), l) for f, l in file_list_CS6_Rlimit32_20bins_Run_5_10]
datalist_DS1_Rlimit32_20bins_Run_5_10 = [(pylab.loadtxt(f), l) for f, l in file_list_DS1_Rlimit32_20bins_Run_5_10]
datalist_Soft_D2_Rlimit32_20bins_Run_5_10 = [(pylab.loadtxt(f), l) for f, l in file_list_Soft_D2_Rlimit32_20bins_Run_5_10]
datalist_E_Rlimit32_50bins_Run_5_10 = [(pylab.loadtxt(f), l) for f, l in file_list_E_Rlimit32_50bins_Run_5_10]
'''
