"""Pure, side-effect-free domain logic for math_utils."""

from __future__ import annotations

from math_utils.core.arithmetic import factorial, gcd, is_prime, lcm
from math_utils.core.statistics import mean, median, variance

__all__ = [
    "factorial",
    "gcd",
    "is_prime",
    "lcm",
    "mean",
    "median",
    "variance",
]
