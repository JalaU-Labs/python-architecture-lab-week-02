"""In-memory implementation of the calculation history repository."""

from __future__ import annotations

from math_toolkit_jala.domain.entities import Calculation


class InMemoryCalculationHistory:
    """List-backed implementation of ``CalculationHistoryRepository``.

    The history is stored in a plain Python list. It is intentionally
    simple: it exists to demonstrate that the application layer depends on
    an abstraction, not on a specific storage technology. Replacing this
    class with a SQLite, Redis, or PostgreSQL implementation requires no
    change in the application or domain layers.
    """

    def __init__(self) -> None:
        self._calculations: list[Calculation] = []

    def add(self, calculation: Calculation) -> None:
        self._calculations.append(calculation)

    def all(self) -> tuple[Calculation, ...]:
        return tuple(self._calculations)

    def clear(self) -> None:
        self._calculations.clear()
