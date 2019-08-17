"""
Unit tests for the Read program
"""

import Read
import numpy as np


class TestRead:

    def test_get_sphere_volume(self):
        assert 4 / 3 * np.pi * 100 ** 3 == Read.get_sphere_volume(100)

