"""Pure descriptive statistics functions for non-empty numeric sequences."""

from __future__ import annotations

from collections.abc import Sequence

from math_toolkit_jala.domain.exceptions import DomainError


def _ensure_non_empty(values: Sequence[float]) -> None:
    if len(values) == 0:
        raise DomainError("statistics operations require at least one value")


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of ``values``.

    Raises:
        DomainError: If ``values`` is empty.
    """
    _ensure_non_empty(values)
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median of ``values``.

    Raises:
        DomainError: If ``values`` is empty.
    """
    _ensure_non_empty(values)
    ordered = sorted(values)
    length = len(ordered)
    midpoint = length // 2
    if length % 2 == 1:
        return float(ordered[midpoint])
    return (ordered[midpoint - 1] + ordered[midpoint]) / 2.0


def variance(values: Sequence[float]) -> float:
    """Return the population variance of ``values``.

    Raises:
        DomainError: If ``values`` is empty.
    """
    _ensure_non_empty(values)
    average = sum(values) / len(values)
    squared_deviations = [(value - average) ** 2 for value in values]
    return sum(squared_deviations) / len(squared_deviations)
