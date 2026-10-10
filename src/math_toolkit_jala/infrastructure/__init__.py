"""Infrastructure layer: concrete adapters for the application's ports.

This package contains the adapters that satisfy the protocols defined in
``math_toolkit_jala.application.ports``. The current implementation
provides an in-memory calculation history and a system clock.
"""

from __future__ import annotations

from math_toolkit_jala.infrastructure.clock import SystemClock
from math_toolkit_jala.infrastructure.in_memory import InMemoryCalculationHistory

__all__ = [
    "InMemoryCalculationHistory",
    "SystemClock",
]
