import pytest
from src.utils.math import mean


def test_mean_normal_list():
    """mean() of a normal list returns the arithmetic average."""
    assert mean([1.0, 2.0, 3.0, 4.0]) == pytest.approx(2.5)


def test_mean_single_element():
    """mean() of a single-element list returns that element."""
    assert mean([42.0]) == pytest.approx(42.0)


def test_mean_empty_raises():
    """mean() of an empty list raises ValueError."""
    with pytest.raises(ValueError, match="mean of empty sequence"):
        mean([])
