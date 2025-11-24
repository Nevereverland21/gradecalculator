import pytest
from extra_points_policy import ExtraPointsPolicy

def test_shouldCountExtraPointsCorrectly():
    policy = ExtraPointsPolicy([True, False, True])
    assert policy.compute_extra_points() == 2

def test_shouldFailWithInvalidTeacherFlag():
    with pytest.raises(ValueError):
        ExtraPointsPolicy([True, "x"])

