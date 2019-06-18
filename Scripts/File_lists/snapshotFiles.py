from definePaths import *
import h5py

'''
test = 0
A = 0
B = 0
CS1 = 0
CS2 = 0
CS3 = 0
CS4 = 0
CS5 = 0
CS6 = 0
DS1 = 0
D2 = 0
E = 0
'''

hdf5_str = "hdf5Path{}"

Sparre_sims = ['0G00_IC_000.hdf5', '0G20_Final_000.hdf5',
               'OMG00_001_IC_000.hdf5', 'OMG20_Final_000.hdf5',
               'OM_150310_000.hdf5']

# Filename = hdf5_str.format(Sparre_sims[0])
# 'HQ1000000_150311_000.hdf5'

testPath = "GHQ1000000test/output/"
test_str = GADGET_Gpath + testPath

HQ = "HQ10000G{}.hdf5"

test_sims = [HQ.format(1.0_0_000), HQ.format(1.2_1_005), HQ.format(0.8_2_000),
             HQ.format(0.8_2_005), HQ.format(1.2_3_005), HQ.format(1.2_5_005),
             HQ.format(1.2_7_005), HQ.format(1.2_9_005), HQ.format(1.0_10_009)]

# Filename = test_str + test_sims[0]

test2Path = "GHQ1000000test2/output/"
test2_str = GADGET_Gpath + test2Path

test2_sims = [HQ.format(1.0_0_000), HQ.format(1.0_5_005),
              HQ.format(1.0_10_005), HQ.format(1.0_15_005),
              HQ.format(1.0_18_005), HQ.format(1.0_18_010),
              HQ.format(1.0_18_015), HQ.format(1.0_18_020),
              HQ.format(1.0_18_025), HQ.format(1.0_18_030),
              HQ.format(1.0_18_035), HQ.format(1.0_18_040),
              HQ.format(1.0_18_045), HQ.format(1.0_18_053),
              HQ.format(1.0_20_005), HQ.format(1.0_25_005)]

# Filename = test2_str + test2_sims[0]

Apath = "GHQ1000000A/output/"
A_str = GADGET_Gpath + Apath

A_sims = [HQ.format(1.0_0_000), HQ.format(1.0_5_005), HQ.format(1.0_10_005),
          HQ.format(1.0_40_005), HQ.format(1.0_48_009), HQ.format(1.0_48_093),
          HQ.format(1.2_46_005), HQ.format(0.8_47_005)]

# Filename = A_str + A_sims[0]

Bpath = "GHQ1000000B/output/"
B_str = GADGET_Gpath + Bpath

B_sims = [HQ.format(1.0_0_000), HQ.format(1.0_5_005), HQ.format(1.0_10_005),
          HQ.format(1.0_198_000), HQ.format(1.0_198_093),
          HQ.format(1.0_199_093), HQ.format(1.0_160_005),
          HQ.format(1.05_196_005), HQ.format(0.95_197_005)]

# Filename = B_str + B_sims[0]

SoftBpath = "SoftGHQ1000000B/output/"
SoftB_str = GADGET_Gpath + SoftBpath

SoftB_sims = [HQ.format(1.0_0_000), HQ.format(1.0_5_005),
              HQ.format(1.0_10_005), HQ.format(1.0_198_000),
              HQ.format(1.0_198_093), HQ.format(1.0_199_093)]

# Filename = SoftB_str + SoftB_sims[0]

CPath = "GHQ1000000C/output/"
C_str = GADGET_Gpath + CPath

C_sims = [HQ.format(1.0_0_000), HQ.format(1.0_5_005), HQ.format(1.0_10_005),
          HQ.format(1.0_40_005), HQ.format(1.2_46_005), HQ.format(0.8_47_005),
          HQ.format(1.0_48_009), HQ.format(1.0_48_093)]

# Filename = C_str + C_sims[0]

DPath = "GHQ1000000_D/output/"
D_str = GADGET_Gpath + DPath

D_sims = [HQ.format(1.0_0_000), HQ.format(1.0_5_005), HQ.format(1.0_10_005),
          HQ.format(1.0_160_005), HQ.format(1.05_196_005),
          HQ.format(0.95_197_005), HQ.format(1.0_198_009),
          HQ.format(1.0_198_093)]

# Filename = D_str + D_sims[0]

OM_0 = 'OM10000G1.0_0_000.hdf5'
OM_48 = 'OM10000G1.0_48_093.hdf5'

CS1path = "GOM10000C1/output/"
# Filename = GADGET_Gpath + CS1path + OM_0

CS2path = "GOM10000C2/output/"
# Filename = GADGET_Gpath + CS2path + OM_0

CS3path = "GOM10000C3/output/"
# Filename = GADGET_Gpath + CS3path + OM_0

CS4path = "GHQ100000CS4/output/"
# Filename = GADGET_Gpath + CS4path + OM_0
# Filename = GADGET_Gpath + CS4path + OM_48

CS5path = "GHQ100000CS5/output/"
# Filename = GADGET_Gpath + CS5path + OM_0
# Filename = GADGET_Gpath + CS5path + OM_48

CS6path = "GHQ100000CS6/output/"
# Filename = GADGET_Gpath + CS6path + OM_0
# Filename = GADGET_Gpath + CS6path + OM_48

DS1path = "G0_5_100000DS1/output/"
# Filename = GADGET_Gpath + DS1path + OM_0
# Filename = GADGET_Gpath + DS1path + OM_48
# Filename = GADGET_Gpath + DS1path + 'OM10000G1.0_49_093.hdf5'

D2path = "G0_5_100000D2/output/"
# Filename = GADGET_Gpath + D2path + HQ.format(1.0_0_000)
# Filename = GADGET_Gpath + D2path + HQ.format(1.0_48_093)
# Filename = GADGET_Gpath + D2path + HQ.format(1.0_49_093)

SoftD2path = "SoftG0_5_100000D2/output/"
# Filename = GADGET_Gpath + SoftD2path + HQ.format(1.0_0_000)
# Filename = GADGET_Gpath + SoftD2path + HQ.format(1.0_48_093)
# Filename = GADGET_Gpath + SoftD2path + HQ.format(1.0_49_093)

Epath = "GHQ1000000E/output/"
E_str = GADGET_Gpath + Epath

E_sims = [HQ.format(1.0_0_000), HQ.format(1.0_5_005), HQ.format(1.0_10_005),
          HQ.format(1.0_160_005), HQ.format(1.05_196_005),
          HQ.format(0.95_197_005), HQ.format(1.0_198_009),
          HQ.format(1.0_198_093)]

# Filename = E_str + E_sims[0]

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

F_str = f"{}_{Filename[len(GADGET_G_path{}):-5]}"

sim_and_path = [('test', test_path), ('A', A_path), ('B', B_path),
                ('Soft_B', Soft_B_path), ('CS1', CS1_path), ('CS2', CS2_path),
                ('CS3', CS3_path), ('CS4', CS4_path), ('CS5', CS5_path),
                ('CS6', CS6_path), ('DS1', DS1_path), ('D2', D2_path),
                ('Soft_D2', Soft_D2_path), ('E', E_path),
                ('B_bound_particles', B_rfp_path + 'B_'),
                ('Soft_B_bound_particles', Soft_B_rfp_path + 'B_'),
                ('CS4_bound_particles', CS4_rfp_path + 'CS4_'),
                ('CS5_bound_particles', CS5_rfp_path + 'CS5_'),
                ('CS6_bound_particles', CS6_rfp_path + 'CS6_'),
                ('DS1_bound_particles', DS1_rfp_path + 'DS1_'),
                ('D2_bound_particles', D2_rfp_path + 'D2_'),
                ('Soft_D2_bound_particles', Soft_D2_rfp_path + 'D2_'),
                ('E_bound_particles', E_rfp_path + 'E_')]

# F = F_str.format(sim_and_path[0][0], sim_and_path[0][1])
# F = F_str.format(sim_and_path[1][0], sim_and_path[1][1])
# F = 'A_' + Filename[len(nosync_path + A_path):-5]
