"""
Unit tests for the Read program
"""

import Scripts.Attractor.Read as Read
# import sys
# sys.path.append("..")


def test_get_sphere_volume():
    assert 4188790.2047863905 == Read.get_sphere_volume(100)
