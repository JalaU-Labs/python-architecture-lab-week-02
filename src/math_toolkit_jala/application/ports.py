"""Abstract ports required by the application layer.

These protocols define the contracts that infrastructure adapters must
satisfy. The application depends only on these abstractions, never on
concrete implementations.
"""

from __future__ import annotations

from datetime import datetime
from typing import Protocol

from math_toolkit_jala.domain.entities import Calculation


class CalculationHistoryRepository(Protocol):
    """Persistence port for the calculation history."""

    def add(self, calculation: Calculation) -> None:
        """Append a calculation to the history."""
        ...  # pragma: no cover

    def all(self) -> tuple[Calculation, ...]:
        """Return every recorded calculation, in insertion order."""
        ...  # pragma: no cover

    def clear(self) -> None:
        """Remove every recorded calculation."""
        ...  # pragma: no cover


class Clock(Protocol):
    """Time source port."""

    def now(self) -> datetime:
        """Return the current moment as a timezone-aware datetime."""
        ...  # pragma: no cover
