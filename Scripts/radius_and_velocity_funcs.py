import numpy as np


def radius(x, y, z):
    """Return radius given 3 cartesian coordinates."""
    return (x ** 2 + y ** 2 + z ** 2) ** .5


def phi(x, y):
    """."""
    return np.arctan2(y, x)


def theta(r, z):
    """."""
    return np.arccos(z / r)


def speed(vx, vy, vz):
    """."""
    return (vx ** 2 + vy ** 2 + vz ** 2) ** .5


def v_R(vx, vy, vz, Theta, Phi):
    """Return radial velocity given cartesian velocities and angles."""
    return (
            np.sin(Theta) * np.cos(Phi) * vx
            + np.sin(Theta) * np.sin(Phi) * vy
            + np.cos(Theta) * vz
            )


def v_theta(vx, vy, vz, Theta, Phi):
    """Return theta-velocity given cartesian velocities and angles."""
    return (
            np.cos(Theta) * np.cos(Phi) * vx
            + np.cos(Theta) * np.sin(Phi) * vy
            - np.sin(Theta) * vz
            )


def v_phi(vx, vy, Phi):
    """Return phi-velocity given cartesian velocities and angle phi."""
    return -np.sin(Phi) * vx + np.cos(Phi) * vy


def v_tan(VTheta, VPhi):
    """Return tangential velocity given angular velocities."""
    return VTheta + VPhi


def spherical_coords_and_velocities():
    """."""
    r = ravf.radius(x, y, z)
    Phi = ravf.phi(x, y)
    Theta = ravf.theta(r, z)
    VR = ravf.v_R(vx, vy, vz, Theta, Phi)
    VTheta = ravf.v_theta(vx, vy, vz, Theta, Phi)
    VPhi = ravf.v_phi(vx, vy, Phi)
    VT = ravf.v_tan(VTheta, VPhi)
    return r, Phi, Theta, VR, VTheta, VPhi, VT


def main():
    # Define test coordinates and velocities
    x = np.array(1, 2, 3)
    y = np.array(4, 5, 6)
    z = np.array(7, 8, 9)

    vx = np.array(1, 2, 3)
    vy = np.array(4, 5, 6)
    vz = np.array(7, 8, 9)

    r = radius(x, y, z)
    Phi = phi(x, y)
    Theta = theta(r, z)

    speed(vx, vy, vz)
    v_R(vx, vy, vz, Theta, Phi)
    v_theta(vx, vy, vz, Theta, Phi)
    v_phi(vx, vy, Phi)
    v_tan(VTheta, VPhi)
    spherical_coords_and_velocities()


if __name__ == '__main__':
    main()
