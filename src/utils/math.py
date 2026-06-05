from collections.abc import Sequence


def mean(values: Sequence[float], *, strict: bool = False) -> float:
    """计算一个数值序列的算术平均值。

    Args:
        values: 浮点数序列。
        strict: 严格模式开关。为 True 时要求每个元素必须是 int 或 float
            （不含 bool 子类），否则抛出 TypeError。默认 False，行为与原版一致。

    Returns:
        算术平均值（float）。

    Raises:
        ValueError: 当 values 为空序列时抛出。
        TypeError: strict=True 且元素类型非 int/float 时抛出。

    Examples:
        >>> mean([1.0, 2.0, 3.0])
        2.0
        >>> mean([10.0])
        10.0
    """
    if not values:
        raise ValueError("mean of empty sequence")
    if strict:
        for v in values:
            if not (isinstance(v, (int, float)) and not isinstance(v, bool)):
                raise TypeError(
                    f"strict mode requires int or float, got {type(v).__name__}"
                )
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


def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b
