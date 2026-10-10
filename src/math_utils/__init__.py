"""Public API for the math_utils package."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from math_utils.core.arithmetic import factorial, gcd, is_prime, lcm
from math_utils.core.statistics import mean, median, variance
from math_utils.exceptions import DomainError, InvalidInputError, MathUtilsError

try:
    __version__: str = version("math-toolkit-jala")
except PackageNotFoundError:  # pragma: no cover - only hit when running from source
    __version__ = "0.0.0"

__all__ = [
    "DomainError",
    "InvalidInputError",
    "MathUtilsError",
    "__version__",
    "factorial",
    "gcd",
    "is_prime",
    "lcm",
    "mean",
    "median",
    "variance",
]
