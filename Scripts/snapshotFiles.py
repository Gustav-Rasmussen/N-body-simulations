from definePaths import *
import h5py

# Filename = hdf5Path + '0G00_IC_000.hdf5'
# Filename = hdf5Path + '0G20_Final_000.hdf5'
# Filename = hdf5Path + 'OMG00_001_IC_000.hdf5'
# Filename = hdf5Path + 'OMG20_Final_000.hdf5'

# Filename = 'HQ1000000_150311_000.hdf5'
# Filename = 'OM_150310_000.hdf5'

testPath = "GHQ1000000test/output/"
# Filename = GADGET_Gpath + test_path + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G1.2_1_005.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G0.8_2_000.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G0.8_2_005.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G1.2_3_005.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G1.2_5_005.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G1.2_7_005.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G1.2_9_005.hdf5'
# Filename = GADGET_Gpath + test_path + 'HQ10000G1.0_10_009.hdf5'

test2Path = "GHQ1000000test2/output/"
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_5_005.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_10_005.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_15_005.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_005.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_010.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_015.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_020.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_025.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_030.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_035.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_040.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_045.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_18_053.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_20_005.hdf5'
# Filename = GADGET_Gpath + test2Path + 'HQ10000G1.0_25_005.hdf5'

Apath = "GHQ1000000A/output/"
# Below 3 files are already run in VDF.py, from test2. re-use those ones.
# Filename = GADGET_Gpath + Apath + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + Apath + 'HQ10000G1.0_5_005.hdf5'
# Filename = GADGET_Gpath + Apath + 'HQ10000G1.0_10_005.hdf5'

# Filename = GADGET_Gpath + Apath + 'HQ10000G1.0_40_005.hdf5'
# Filename = GADGET_Gpath + Apath + 'HQ10000G1.0_48_009.hdf5'
# Filename = GADGET_Gpath + Apath + 'HQ10000G1.0_48_093.hdf5'

# Below 2 files has not yet been analysed:
# Filename = GADGET_Gpath + Apath + 'HQ10000G1.2_46_005.hdf5'
# Filename = GADGET_Gpath + Apath + 'HQ10000G0.8_47_005.hdf5'

Bpath = "GHQ1000000B/output/"
# This file is already run in VDF.py, from test2. re-use that one:
# Filename = GADGET_Gpath + Bpath + 'HQ10000G1.0_0_000.hdf5'

# Filename = GADGET_Gpath + Bpath + 'HQ10000G1.0_5_005.hdf5'
# Filename = GADGET_Gpath + Bpath + 'HQ10000G1.0_10_005.hdf5'
# Filename = GADGET_Gpath + Bpath + 'HQ10000G1.0_198_000.hdf5'
# Filename = GADGET_Gpath + Bpath + 'HQ10000G1.0_198_093.hdf5'
# Filename = GADGET_Gpath + Bpath + 'HQ10000G1.0_199_093.hdf5'
# #Filename = GADGET_Gpath + Bpath + 'HQ10000G1.0_160_005.hdf5'
# #Filename = GADGET_Gpath + Bpath + 'HQ10000G1.05_196_005.hdf5'
# #Filename = GADGET_Gpath + Bpath + 'HQ10000G0.95_197_005.hdf5'

SoftBpath = "SoftGHQ1000000B/output/"
# Filename = GADGET_Gpath + SoftBpath + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + SoftBpath + 'HQ10000G1.0_5_005.hdf5'
# Filename = GADGET_Gpath + SoftBpath + 'HQ10000G1.0_10_005.hdf5'
# Filename = GADGET_Gpath + SoftBpath + 'HQ10000G1.0_198_000.hdf5'
# Filename = GADGET_Gpath + SoftBpath + 'HQ10000G1.0_198_093.hdf5'
# Filename = GADGET_Gpath + SoftBpath + 'HQ10000G1.0_199_093.hdf5'

CPath = "GHQ1000000C/output/"
# Filename = GADGET_Gpath + CPath + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + CPath + 'HQ10000G1.0_5_005.hdf5'
# Filename = GADGET_Gpath + CPath + 'HQ10000G1.0_10_005.hdf5'
# Filename = GADGET_Gpath + CPath + 'HQ10000G1.0_40_005.hdf5'
# Filename = GADGET_Gpath + CPath + 'HQ10000G1.2_46_005.hdf5'
# Filename = GADGET_Gpath + CPath + 'HQ10000G0.8_47_005.hdf5'
# Filename = GADGET_Gpath + CPath + 'HQ10000G1.0_48_009.hdf5'
# Filename = GADGET_Gpath + CPath + 'HQ10000G1.0_48_093.hdf5'

DPath = "GHQ1000000_D/output/"
# Filename = GADGET_Gpath + DPath + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + DPath + 'HQ10000G1.0_5_005.hdf5'
# Filename = GADGET_Gpath + DPath + 'HQ10000G1.0_10_005.hdf5'
# Filename = GADGET_Gpath + DPath + 'HQ10000G1.0_160_005.hdf5'
# Filename = GADGET_Gpath + DPath + 'HQ10000G1.05_196_005.hdf5'
# Filename = GADGET_Gpath + DPath + 'HQ10000G0.95_197_005.hdf5'
# Filename = GADGET_Gpath + DPath + 'HQ10000G1.0_198_009.hdf5'
# Filename = GADGET_Gpath + DPath + 'HQ10000G1.0_198_093.hdf5'

CS1path = "GOM10000C1/output/"
# Filename = GADGET_Gpath + CS1path + 'OM10000G1.0_0_000.hdf5'

CS2path = "GOM10000C2/output/"
# Filename = GADGET_Gpath + CS2path + 'OM10000G1.0_0_000.hdf5'

CS3path = "GOM10000C3/output/"
# Filename = GADGET_Gpath + CS3path + 'OM10000G1.0_0_000.hdf5'

CS4path = "GHQ100000CS4/output/"
# Filename = GADGET_Gpath + CS4path + 'OM10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + CS4path + 'OM10000G1.0_48_093.hdf5'

CS5path = "GHQ100000CS5/output/"
# Filename = GADGET_Gpath + CS5path + 'OM10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + CS5path + 'OM10000G1.0_48_093.hdf5'

CS6path = "GHQ100000CS6/output/"
# Filename = GADGET_Gpath + CS6path + 'OM10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + CS6path + 'OM10000G1.0_48_093.hdf5'

DS1path = "G0_5_100000DS1/output/"
# Filename = GADGET_Gpath + DS1path + 'OM10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + DS1path + 'OM10000G1.0_48_093.hdf5'
# Filename = GADGET_Gpath + DS1path + 'OM10000G1.0_49_093.hdf5'

D2path = "G0_5_100000D2/output/"
# Filename = GADGET_Gpath + D2path + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + D2path + 'HQ10000G1.0_48_093.hdf5'
# Filename = GADGET_Gpath + D2path + 'HQ10000G1.0_49_093.hdf5'

SoftD2path = "SoftG0_5_100000D2/output/"
# Filename = GADGET_Gpath + SoftD2path + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + SoftD2path + 'HQ10000G1.0_48_093.hdf5'
# Filename = GADGET_Gpath + SoftD2path + 'HQ10000G1.0_49_093.hdf5'

Epath = "GHQ1000000E/output/"
# Filename = GADGET_Gpath + Epath + 'HQ10000G1.0_0_000.hdf5'
# Filename = GADGET_Gpath + Epath + 'HQ10000G1.0_5_005.hdf5'
# Filename = GADGET_Gpath + Epath + 'HQ10000G1.0_10_005.hdf5'
# Filename = GADGET_Gpath + Epath + 'HQ10000G1.0_160_005.hdf5'
# Filename = GADGET_Gpath + Epath + 'HQ10000G1.05_196_005.hdf5'
# Filename = GADGET_Gpath + Epath + 'HQ10000G0.95_197_005.hdf5'
# Filename = GADGET_Gpath + Epath + 'HQ10000G1.0_198_009.hdf5'
# Filename = GADGET_Gpath + Epath + 'HQ10000G1.0_198_093.hdf5'

# Bound particles only:
BrfpPath = "GHQ1000000B/rfpOutput/"
# Filename = GADGET_Gpath + BrfpPath + 'BG1.0_200rfp011.hdf5'
# Filename = GADGET_Gpath + BrfpPath + 'BG1.0_200rfp093.hdf5'

SoftBrfpPath = "SoftGHQ1000000B/rfpOutput/"
# Filename = GADGET_Gpath + Soft_B_rfp_path + 'B_G1.0_200_rfp_011.hdf5'
# Filename = GADGET_G_path + Soft_B_rfp_path + 'B_G1.0_200_rfp_093.hdf5'

CS4_rfp_path = "G_HQ_100000_CS4/rfp_output/"
# Filename = GADGET_G_path + CS4_rfp_path + 'CS4_G1.0_49_rfp_093.hdf5'

CS5_rfp_path = "G_HQ_100000_CS5/rfp_output/"
# Filename = GADGET_G_path + CS5_rfp_path + 'CS5_G1.0_49_rfp_093.hdf5'

CS6_rfp_path = "G_HQ_100000_CS6/rfp_output/"
# Filename = GADGET_G_path + CS6_rfp_path + 'CS6_G1.0_49_rfp_093.hdf5'

DS1_rfp_path = "G_0_5_100000_DS1/rfp_output/"
# Filename = GADGET_G_path + DS1_rfp_path + 'DS1_G1.0_50_rfp_093.hdf5'

D2_rfp_path = "G_0_5_100000_D2/rfp_output/"
# Filename = GADGET_G_path + D2_rfp_path  + 'D2_G1.0_50_rfp_093.hdf5'

Soft_D2_rfp_path = "Soft_G_0_5_100000_D2/rfp_output/"
# Filename = GADGET_G_path + Soft_D2_rfp_path + 'D2_G1.0_50_rfp_093.hdf5'

SnapshotFile = h5py.File(Filename, "r")

# F = 'test_' + Filename[len(GADGET_G_path + test_path):-5]
# F = 'A_' + Filename[len(GADGET_G_path + A_path):-5]
# F = 'A_' + Filename[len(nosync_path + A_path):-5]
# F = 'B_' + Filename[len(GADGET_G_path + B_path):-5]
# F = 'Soft_B_' + Filename[len(GADGET_G_path + Soft_B_path):-5]
# F = 'CS1_' + Filename[len(GADGET_G_path + CS1_path):-5]
# F = 'CS2_' + Filename[len(GADGET_G_path + CS2_path):-5]
# F = 'CS3_' + Filename[len(GADGET_G_path + CS3_path):-5]
# F = 'CS4_' + Filename[len(GADGET_G_path + CS4_path):-5]
# F = 'CS5_' + Filename[len(GADGET_G_path + CS5_path):-5]
# F = 'CS6_' + Filename[len(GADGET_G_path + CS6_path):-5]
# F = 'DS1_' + Filename[len(GADGET_G_path + DS1_path):-5]
# F = 'D2_' + Filename[len(GADGET_G_path + D2_path):-5]
# F = 'Soft_D2_' + Filename[len(GADGET_G_path + Soft_D2_path):-5]
# F = 'E_' + Filename[len(GADGET_G_path + E_path):-5]

# Bound particles only:
# F = 'B_bound_particles_' + Filename[len(GADGET_G_path + B_rfp_path + 'B_'):-5]
# F = 'Soft_B_bound_particles_' + Filename[len(GADGET_G_path + Soft_B_rfp_path + 'B_'):-5]
# F = 'CS4_bound_particles_' + Filename[len(GADGET_G_path + CS4_rfp_path + 'CS4_'):-5]
# F = 'CS5_bound_particles_' + Filename[len(GADGET_G_path + CS5_rfp_path + 'CS5_'):-5]
# F = 'CS6_bound_particles_' + Filename[len(GADGET_G_path + CS6_rfp_path + 'CS6_'):-5]
# F = 'DS1_bound_particles_' + Filename[len(GADGET_G_path + DS1_rfp_path + 'DS1_'):-5]
# F = 'D2_bound_particles_' + Filename[len(GADGET_G_path + D2_rfp_path + 'D2_'):-5]
# F = 'Soft_D2_bound_particles_' + Filename[len(GADGET_G_path + Soft_D2_rfp_path + 'D2_'):-5]
# F = 'E_bound_particles_' + Filename[len(GADGET_G_path + E_rfp_path + 'E_'):-5]

test = 0
A = 0
B = 0
CS1 = 0
CS2 = 0
CS3 = 0
CS4 = 0  # These files are not yet incorporated into VDF.py
CS5 = 0
CS6 = 0
DS1 = 0
D2 = 0
E = 0
