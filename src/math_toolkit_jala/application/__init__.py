"""Application layer: use cases and the ports they depend on.

Use cases orchestrate the domain layer to fulfill specific operations
requested by the outside world. They depend on abstract ports, not on
concrete infrastructure, which keeps the application testable in
isolation.
"""

from __future__ import annotations

from math_toolkit_jala.application.ports import (
    CalculationHistoryRepository,
    Clock,
)
from math_toolkit_jala.application.use_cases import (
    ClearHistoryUseCase,
    ComputeFactorialUseCase,
    ComputeGcdUseCase,
    ComputeLcmUseCase,
    ComputeMeanUseCase,
    ComputeMedianUseCase,
    ComputeVarianceUseCase,
    GetHistoryUseCase,
    IsPrimeUseCase,
)

__all__ = [
    "CalculationHistoryRepository",
    "ClearHistoryUseCase",
    "Clock",
    "ComputeFactorialUseCase",
    "ComputeGcdUseCase",
    "ComputeLcmUseCase",
    "ComputeMeanUseCase",
    "ComputeMedianUseCase",
    "ComputeVarianceUseCase",
    "GetHistoryUseCase",
    "IsPrimeUseCase",
]
