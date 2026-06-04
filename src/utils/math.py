def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers.

    Args:
        values: A list of float values.

    Returns:
        The arithmetic mean as a float.

    Raises:
        ValueError: If the input list is empty.
    """
    if not values:
        raise ValueError("mean of empty sequence")
    return sum(values) / len(values)
