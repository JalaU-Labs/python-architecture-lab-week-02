"""Public API for the math_toolkit_jala package."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from math_toolkit_jala.core.arithmetic import factorial, gcd, is_prime, lcm
from math_toolkit_jala.core.statistics import mean, median, variance
from math_toolkit_jala.exceptions import DomainError, InvalidInputError, MathUtilsError

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
