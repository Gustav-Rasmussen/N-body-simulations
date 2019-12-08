# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import h5py
import numpy as np
from pathlib import Path

data_folder = Path.home() / 'Documents/Hdf5/'


@dataclass
class LoadHalo:
    """Class for loading a halo."""
    V: np.ndarray = field(init=False, repr=False)
    x: np.ndarray = field(init=False, repr=False)
    y: np.ndarray = field(init=False, repr=False)
    z: np.ndarray = field(init=False, repr=False)
    vx: np.ndarray = field(init=False, repr=False)
    vy: np.ndarray = field(init=False, repr=False)
    vz: np.ndarray = field(init=False, repr=False)
    ID_minV: np.ndarray = field(init=False, repr=False)
    filename: str = '0G00_IC_000.hdf5'
    r_cut: int = 100

    def __post_init__(self):
        self.read_arepo_snapshot()
        self.centralized_coords()
        self.radial_cut()
        self.centralized_velocities()

    def __repr__(self):
        return (f'Filename: {self.filename}\n'
                f'x: {self.x}\n'
                f'y: {self.y}\n'
                f'z: {self.z}\n'
                f'vx: {self.vx}\n'
                f'vy: {self.vy}\n'
                f'vz: {self.vz}\n'
                f'Potential: {self.V}\n'
                f'ID_minV: {self.ID_minV}')

    def read_arepo_snapshot(self):
        filepath = data_folder / self.filename
        with h5py.File(filepath, 'r') as snapshotfile:
            pos = snapshotfile['PartType1/Coordinates']
            vel = snapshotfile['PartType1/Velocities']
            self.V = snapshotfile['PartType1/Potential'][:]
            self.x = pos[:, 0]
            self.y = pos[:, 1]
            self.z = pos[:, 2]
            self.vx = vel[:, 0]
            self.vy = vel[:, 1]
            self.vz = vel[:, 2]
            self.ID_minV = np.argmin(self.V)

    def radial_cut(self):
        good_ids = np.where(self.x ** 2 + self.y ** 2 + self.z ** 2 < self.r_cut ** 2)
        # r_cut_min = 400.
        # r_cut_max = 500.
        # Removes all particles that is far away from the cluster.
        # good_ids = np.where(R < r_cut_max)
        # good_ids = np.where(R < r_cut)
        # good_ids = np.where((R < r_cut_max) * (R > r_cut_min))
        # Now slice the cluster into a rectangular shape still 1_000 kpc wide,
        # but only 100 kpc tall
        # good_ids = np.where((R < r_cut) * (yC - 50.0 < y) * (y < yC + 50.0))
        self.x = self.x[good_ids]
        self.y = self.y[good_ids]
        self.z = self.z[good_ids]
        self.vx = self.vx[good_ids]
        self.vy = self.vy[good_ids]
        self.vz = self.vz[good_ids]
        self.V = self.V[good_ids]

    def centralized_coords(self):
        """Changes x, y and z so that the cluster is centered."""
        self.x = self.x - self.x[self.ID_minV]
        self.y = self.y - self.y[self.ID_minV]
        self.z = self.z - self.z[self.ID_minV]

    def centralized_velocities(self):
        """Changes vx, vy and vz so that the velocities are centered."""
        self.vx = self.vx - np.median(self.vx)
        self.vy = self.vy - np.median(self.vy)
        self.vz = self.vz - np.median(self.vz)


def main():
    halo = LoadHalo('0G00_IC_000.hdf5')
    print(halo)


if __name__ == '__main__':
    main()
