from collections.abc import Sequence


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers.

    Args:
        values: A sequence of float values.

    Returns:
        The arithmetic mean as a float.

    Raises:
        ValueError: If the input sequence is empty.
    """
    if not values:
        raise ValueError("mean of empty sequence")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median of a non-empty sequence of numbers.

    For even-length sequences, returns the mean of the two middle values.

    Args:
        values: A sequence of float values.

    Returns:
        The median as a float.

    Raises:
        ValueError: If the input sequence is empty.
    """
    if not values:
        raise ValueError("median of empty sequence")
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_values[mid])
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0


def variance(values: Sequence[float], *, ddof: int = 0) -> float:
    """Return the variance of a non-empty sequence of numbers.

    Args:
        values: A sequence of float values.
        ddof: Delta degrees of freedom. Use 0 for population variance,
              1 for sample variance.

    Returns:
        The variance as a float.

    Raises:
        ValueError: If the input sequence is empty.
        ValueError: If ddof is not less than len(values).
    """
    if not values:
        raise ValueError("variance of empty sequence")
    n = len(values)
    if ddof >= n:
        raise ValueError("ddof must be < len(values)")
    mu = mean(values)
    return sum((x - mu) ** 2 for x in values) / (n - ddof)
