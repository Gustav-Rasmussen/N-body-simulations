# -*- coding: utf-8 -*-

import h5py
import numpy as np

OldSnapfile = h5py.File('SNAPSHOT_FILENAME', 'r')
NewSnapfile = h5py.File('NEW_SNAPSHOT_FILENAME', 'w')

# Copy header to new snapshot:
OldSnapfile.copy('/Header', NewSnapfile, '/Header')

# Set masses positions and velocities of new halos
NewSnapfile['PartType1/Masses'] = Masses
NewSnapfile['PartType1/Positions'] = Pos
NewSnapfile['PartType1/Velocities'] = Vel

# Set Ndm:
Ndm = NewSnapfile['PartType1/Masses'].shape[0]
Narray = np.array([0, Ndm, 0, 0, 0, 0], dtype=np.int32)
NewSnapfile['Header'].attrs.modify('NumPart_ThisFile', Narray)
NewSnapfile['Header'].attrs.modify('NumPart_Total', Narray)

NewSnapfile.close()
OldSnapfile.close()
