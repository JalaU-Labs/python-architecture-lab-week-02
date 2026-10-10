"""Pure, side-effect-free domain logic for math_toolkit_jala."""

from __future__ import annotations

from math_toolkit_jala.core.arithmetic import factorial, gcd, is_prime, lcm
from math_toolkit_jala.core.statistics import mean, median, variance

__all__ = [
    "factorial",
    "gcd",
    "is_prime",
    "lcm",
    "mean",
    "median",
    "variance",
]
