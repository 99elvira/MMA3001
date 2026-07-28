"""Unit tests for utility functions."""

import pytest
import numpy as np
from sphero_monash_student.utils import cartesian_to_polar


class TestCartesianToPolar:
    def test_positive_x_axis(self):
        r, theta = cartesian_to_polar(1.0, 0.0)
        assert r == pytest.approx(1.0)
        assert theta == pytest.approx(0.0)

    def test_positive_y_axis(self):
        r, theta = cartesian_to_polar(0.0, 1.0)
        assert r == pytest.approx(1.0)
        assert theta == pytest.approx(90.0)

    def test_origin(self):
        r, theta = cartesian_to_polar(0.0, 0.0)
        assert r == pytest.approx(0.0)
        assert theta == pytest.approx(0.0)

    def test_diagonal(self):
        r, theta = cartesian_to_polar(3.0, 4.0)
        assert r == pytest.approx(5.0)
        assert theta == pytest.approx(np.degrees(np.arctan2(4, 3)))
