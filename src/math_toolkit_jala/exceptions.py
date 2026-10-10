"""Domain-specific exceptions raised by the math_toolkit_jala package."""

from __future__ import annotations


class MathUtilsError(Exception):
    """Base class for every exception raised by math_toolkit_jala."""


class InvalidInputError(MathUtilsError):
    """Raised when an argument has a type that is not supported."""


class DomainError(MathUtilsError):
    """Raised when a value violates a mathematical domain constraint."""
