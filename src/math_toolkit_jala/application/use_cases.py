"""Use cases: orchestrators that connect the domain to the outer layers.

Every use case that performs a mathematical operation records the result
in the history repository, providing a uniform audit trail regardless of
which operation was executed.
"""

from __future__ import annotations

from collections.abc import Sequence

from math_toolkit_jala.application.ports import (
    CalculationHistoryRepository,
    Clock,
)
from math_toolkit_jala.domain.arithmetic import factorial, gcd, is_prime, lcm
from math_toolkit_jala.domain.entities import (
    Calculation,
    CalculationArgument,
    CalculationValue,
)
from math_toolkit_jala.domain.statistics import mean, median, variance


class _RecordedUseCase:
    """Base class for use cases that record their result in the history."""

    def __init__(
        self,
        history: CalculationHistoryRepository,
        clock: Clock,
    ) -> None:
        self._history = history
        self._clock = clock

    def _record(
        self,
        operation: str,
        arguments: tuple[CalculationArgument, ...],
        result: CalculationValue,
    ) -> None:
        self._history.add(
            Calculation(
                operation=operation,
                arguments=arguments,
                result=result,
                timestamp=self._clock.now(),
            )
        )


class ComputeFactorialUseCase(_RecordedUseCase):
    """Compute ``n!`` and record the result."""

    def execute(self, n: int) -> int:
        result = factorial(n)
        self._record("factorial", (n,), result)
        return result


class ComputeGcdUseCase(_RecordedUseCase):
    """Compute the greatest common divisor and record the result."""

    def execute(self, a: int, b: int) -> int:
        result = gcd(a, b)
        self._record("gcd", (a, b), result)
        return result


class ComputeLcmUseCase(_RecordedUseCase):
    """Compute the least common multiple and record the result."""

    def execute(self, a: int, b: int) -> int:
        result = lcm(a, b)
        self._record("lcm", (a, b), result)
        return result


class IsPrimeUseCase(_RecordedUseCase):
    """Determine whether ``n`` is prime and record the result."""

    def execute(self, n: int) -> bool:
        result = is_prime(n)
        self._record("is_prime", (n,), result)
        return result


class ComputeMeanUseCase(_RecordedUseCase):
    """Compute the arithmetic mean and record the result."""

    def execute(self, values: Sequence[float]) -> float:
        result = mean(values)
        self._record("mean", tuple(values), result)
        return result


class ComputeMedianUseCase(_RecordedUseCase):
    """Compute the median and record the result."""

    def execute(self, values: Sequence[float]) -> float:
        result = median(values)
        self._record("median", tuple(values), result)
        return result


class ComputeVarianceUseCase(_RecordedUseCase):
    """Compute the population variance and record the result."""

    def execute(self, values: Sequence[float]) -> float:
        result = variance(values)
        self._record("variance", tuple(values), result)
        return result


class GetHistoryUseCase:
    """Return every calculation recorded during the current session."""

    def __init__(self, history: CalculationHistoryRepository) -> None:
        self._history = history

    def execute(self) -> tuple[Calculation, ...]:
        return self._history.all()


class ClearHistoryUseCase:
    """Remove every calculation recorded during the current session."""

    def __init__(self, history: CalculationHistoryRepository) -> None:
        self._history = history

    def execute(self) -> None:
        self._history.clear()
