"""Domain entities: immutable value objects that describe the business model."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

type CalculationArgument = int | float
type CalculationValue = int | float | bool


@dataclass(frozen=True, slots=True)
class Calculation:
    """Immutable record of a single operation performed by the application.

    Attributes:
        operation: The name of the operation (e.g. ``"factorial"``).
        arguments: The positional arguments passed to the operation.
        result: The value returned by the operation.
        timestamp: A timezone-aware timestamp marking when the operation
            was recorded.
    """

    operation: str
    arguments: tuple[CalculationArgument, ...]
    result: CalculationValue
    timestamp: datetime

    def formatted(self) -> str:
        """Return a compact human-readable representation of the record."""
        args = ", ".join(repr(arg) for arg in self.arguments)
        return f"{self.operation}({args}) = {self.result!r}"
