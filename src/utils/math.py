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
