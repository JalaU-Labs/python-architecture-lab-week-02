"""Public API for the math_toolkit_jala package.

The public API is deliberately small: it re-exports the mathematical
functions and the exception hierarchy from the domain layer. Application
and infrastructure components are not part of the public API; consumers
that need them must import from ``math_toolkit_jala.application`` or
``math_toolkit_jala.infrastructure`` explicitly.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from math_toolkit_jala.domain.arithmetic import factorial, gcd, is_prime, lcm
from math_toolkit_jala.domain.exceptions import (
    DomainError,
    InvalidInputError,
    MathUtilsError,
)
from math_toolkit_jala.domain.statistics import mean, median, variance

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
