import pytest
from src.utils.math import mean, median, variance


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


def test_mean_strict_valid():
    """mean(values, strict=True) with int/float-only values succeeds."""
    assert mean([1.0, 2.0], strict=True) == pytest.approx(1.5)


def test_mean_strict_rejects_str():
    """mean(values, strict=True) raises TypeError when a string is present."""
    with pytest.raises(TypeError, match="strict mode requires int or float, got str"):
        mean([1.0, "x"], strict=True)


def test_mean_strict_rejects_bool():
    """mean(values, strict=True) raises TypeError for bool even though bool
    is technically an int subclass."""
    with pytest.raises(TypeError, match="strict mode requires int or float, got bool"):
        mean([True, False], strict=True)


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


def test_variance_population():
    """variance(ddof=0) computes the population variance."""
    assert variance([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]) == pytest.approx(4.0)


def test_variance_sample():
    """variance(ddof=1) computes the sample variance."""
    assert variance([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0], ddof=1) == pytest.approx(4.571428571428571)


def test_variance_empty_raises():
    """variance() of an empty list raises ValueError."""
    with pytest.raises(ValueError, match="variance of empty sequence"):
        variance([])


def test_variance_ddof_too_large_raises():
    """variance() with ddof >= len raises ValueError."""
    with pytest.raises(ValueError, match="ddof must be < len"):
        variance([1.0, 2.0], ddof=2)
