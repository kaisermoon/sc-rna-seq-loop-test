import pytest
from src.utils.math import mean, median


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


def test_median_odd_length():
    """median() of an odd-length list returns the middle element."""
    assert median([3.0, 1.0, 2.0]) == pytest.approx(2.0)


def test_median_even_length():
    """median() of an even-length list returns the mean of the two middle values."""
    assert median([1.0, 2.0, 3.0, 4.0]) == pytest.approx(2.5)


def test_median_empty_raises():
    """median() of an empty list raises ValueError."""
    with pytest.raises(ValueError, match="median of empty sequence"):
        median([])
