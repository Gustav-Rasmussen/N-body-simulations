import numpy as np


def modulus(*args):
    """Modulus of vector of arbitrary size."""
    return sum([i ** 2 for i in args]) ** .5


def phi(x, y):
    """."""
    return np.arctan2(y, x)


def theta(r, z):
    """."""
    return np.arccos(z / r)


def v_R(vx, vy, vz, Theta, Phi):
    """Return radial velocity given cartesian velocities and angles."""
    return (np.sin(Theta) * np.cos(Phi) * vx
            + np.sin(Theta) * np.sin(Phi) * vy + np.cos(Theta) * vz)


def v_theta(vx, vy, vz, Theta, Phi):
    """Return theta-velocity given cartesian velocities and angles."""
    return (np.cos(Theta) * np.cos(Phi) * vx
            + np.cos(Theta) * np.sin(Phi) * vy - np.sin(Theta) * vz)


def v_phi(vx, vy, Phi):
    """Return phi-velocity given cartesian velocities and angle phi."""
    return -np.sin(Phi) * vx + np.cos(Phi) * vy


def v_tan(VTheta, VPhi):
    """Return tangential velocity given angular velocities."""
    return VTheta + VPhi


def spherical_coords(x, y, z):
    """."""
    r = modulus(x, y, z)
    Phi = phi(x, y)
    Theta = theta(r, z)
    return r, Phi, Theta


def spherical_velocities(vx, vy, vz, Theta, Phi):
    """."""
    VR = v_R(vx, vy, vz, Theta, Phi)
    VTheta = v_theta(vx, vy, vz, Theta, Phi)
    VPhi = v_phi(vx, vy, Phi)
    VT = v_tan(VTheta, VPhi)
    return VR, VTheta, VPhi, VT


def main():
    # Define test coordinates and velocities
    x = np.array(1, 2, 3)
    y = np.array(4, 5, 6)
    z = np.array(7, 8, 9)
    vx = np.array(1, 2, 3)
    vy = np.array(4, 5, 6)
    vz = np.array(7, 8, 9)
    r, Phi, Theta = spherical_coords(x, y, z)
    VR, VTheta, VPhi, VT = spherical_velocities(vx, vy, vz, Theta, Phi)
    Speed = modulus(vx, vy, vz)
    print(r, Phi, Theta, VR, VTheta, VPhi, VT, Speed)


if __name__ == '__main__':
    main()
