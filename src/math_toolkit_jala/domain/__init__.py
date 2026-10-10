"""Domain layer: pure business rules and entities.

This package has no dependencies on the application, infrastructure, or
presentation layers. It defines the mathematical operations, the domain
entities, the exception hierarchy, and the abstract ports that the
application layer consumes.
"""

from __future__ import annotations

from math_toolkit_jala.domain.arithmetic import factorial, gcd, is_prime, lcm
from math_toolkit_jala.domain.entities import (
    Calculation,
    CalculationArgument,
    CalculationValue,
)
from math_toolkit_jala.domain.exceptions import (
    DomainError,
    InvalidInputError,
    MathUtilsError,
)
from math_toolkit_jala.domain.statistics import mean, median, variance

__all__ = [
    "Calculation",
    "CalculationArgument",
    "CalculationValue",
    "DomainError",
    "InvalidInputError",
    "MathUtilsError",
    "factorial",
    "gcd",
    "is_prime",
    "lcm",
    "mean",
    "median",
    "variance",
]
