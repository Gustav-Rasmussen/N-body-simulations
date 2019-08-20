# -*- coding: utf-8 -*-        
import h5py
import numpy as np
import IPython

path = '/Users/gustav.c.rasmussen/Desktop/RunGadget/'

OldSnaps_list = ['G_HQ_1000000_B/output/Hernquist10000_G1.0_198_093',
                 'G_HQ_1000000_B/output/Hernquist10000_G1.0_199_093',
                 'G_OM_100000_C4/output/Osipkov_Merritt10000_G1.0_48_093',
                 'G_OM_100000_C5/output/Osipkov_Merritt10000_G1.0_48_093',
                 'G_OM_100000_C6/output/Osipkov_Merritt10000_G1.0_48_093',
                 'G_OM_100000_D1/output/Osipkov_Merritt10000_G1.0_49_093',
                 'G_Edd_100000_D2/output/Hernquist10000_G1.0_49_093'
                ]

OldSnapfile = h5py.File(path + OldSnaps_list[0] + '.hdf5', 'r')

NewSnaps_list = ['B_G1.0_198_093_no_free_par',
                 'B_G1.0_199_093_rfp',
                 'C4_G1.0_48_093_rfp',
                 'C5_G1.0_48_093_rfp',
                 'C6_G1.0_48_093_rfp',
                 'D1_G1.0_49_093_rfp',
                 'D2_G1.0_49_093_rfp
                ]

NewSnapfile = h5py.File(NewSnaps_list[0] + '.hdf5', 'w')

# copy header to new snapshot:
OldSnapfile.copy('/Header', NewSnapfile, '/Header')

Masses = OldSnapfile['PartType1/Masses'].value   
Pos = OldSnapfile['PartType1/Coordinates'].value 
Vel = OldSnapfile['PartType1/Velocities'].value  
V = OldSnapfile['PartType1/Potential'].value     

x = Pos[:, 0]
y = Pos[:, 1]
z = Pos[:, 2]
vx = Vel[:, 0]
vy = Vel[:, 1]
vz = Vel[:, 2]
v = (vx ** 2 + vy ** 2 + vz ** 2) ** .5  # Speed
E_tot = V + .5 * v ** 2
GoodIDs = np.where(E_tot <= 0.)  # Bound particles
x = x[GoodIDs]
y = y[GoodIDs]
z = z[GoodIDs]
vx = vx[GoodIDs]
vy = vy[GoodIDs]
vz = vz[GoodIDs] 

# print(x.shape)
Pos = np.array([x, y, z])
Pos = Pos.transpose()
# print('Pos.shape: ', Pos.shape)
Vel = np.array([vx, vy, vz])
Vel = Vel.transpose()
# print('Vel.shape: ', Vel.shape)
# V = V[GoodIDs]  # Potential
# IPython.embed()
Masses = Masses[GoodIDs]

NewSnapfile['PartType1/Masses'] = Masses          
NewSnapfile['PartType1/Coordinates'] = Pos
NewSnapfile['PartType1/Velocities'] = Vel
# NewSnapfile['PartType1/Potential'] = V

# Set Ndm:
Ndm = NewSnapfile['PartType1/Coordinates'].shape[0]
# print('Ndm: ', Ndm)
# Ndm = NewSnapfile['PartType1/Masses'].shape[0]
Narray = np.array([0, Ndm, 0, 0, 0, 0], dtype=np.int32)
NewSnapfile['Header'].attrs.modify('NumPart_ThisFile', Narray)
NewSnapfile['Header'].attrs.modify('NumPart_Total', Narray)

NewSnapfile.close()       
OldSnapfile.close()

if __name__ == '__main__':
        pass
