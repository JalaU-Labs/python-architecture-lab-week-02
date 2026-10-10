"""Unit tests for the application use cases.

The tests use in-memory fakes for the ports and exercise each use case in
isolation, verifying both the returned value and the recorded side
effect.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

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
from math_toolkit_jala.domain.exceptions import DomainError
from math_toolkit_jala.infrastructure.clock import SystemClock
from math_toolkit_jala.infrastructure.in_memory import InMemoryCalculationHistory


class FakeClock:
    """Deterministic clock that always returns the same timestamp."""

    def __init__(self, moment: datetime) -> None:
        self._moment = moment

    def now(self) -> datetime:
        return self._moment


@pytest.fixture
def history() -> InMemoryCalculationHistory:
    return InMemoryCalculationHistory()


@pytest.fixture
def clock() -> FakeClock:
    return FakeClock(datetime(2026, 10, 13, 12, 0, 0, tzinfo=UTC))


class TestComputeFactorialUseCase:
    def test_returns_result_and_records_it(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        use_case = ComputeFactorialUseCase(history, clock)
        assert use_case.execute(5) == 120
        entries = history.all()
        assert len(entries) == 1
        assert entries[0].operation == "factorial"
        assert entries[0].arguments == (5,)
        assert entries[0].result == 120
        assert entries[0].timestamp == clock.now()

    def test_propagates_domain_error(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        use_case = ComputeFactorialUseCase(history, clock)
        with pytest.raises(DomainError):
            use_case.execute(-1)
        assert history.all() == ()


class TestComputeGcdUseCase:
    def test_returns_result_and_records_it(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        use_case = ComputeGcdUseCase(history, clock)
        assert use_case.execute(12, 18) == 6
        assert history.all()[0].formatted() == "gcd(12, 18) = 6"


class TestComputeLcmUseCase:
    def test_returns_result_and_records_it(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        use_case = ComputeLcmUseCase(history, clock)
        assert use_case.execute(4, 6) == 12
        assert history.all()[0].formatted() == "lcm(4, 6) = 12"


class TestIsPrimeUseCase:
    @pytest.mark.parametrize(("n", "expected"), [(97, True), (100, False)])
    def test_returns_result_and_records_it(
        self,
        history: InMemoryCalculationHistory,
        clock: FakeClock,
        n: int,
        expected: bool,
    ) -> None:
        use_case = IsPrimeUseCase(history, clock)
        assert use_case.execute(n) is expected
        assert history.all()[0].result is expected


class TestComputeMeanUseCase:
    def test_returns_result_and_records_it(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        use_case = ComputeMeanUseCase(history, clock)
        assert use_case.execute([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0
        assert history.all()[0].arguments == (1.0, 2.0, 3.0, 4.0, 5.0)


class TestComputeMedianUseCase:
    def test_returns_result_and_records_it(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        use_case = ComputeMedianUseCase(history, clock)
        assert use_case.execute([1.0, 2.0, 3.0, 4.0]) == 2.5
        assert history.all()[0].operation == "median"


class TestComputeVarianceUseCase:
    def test_returns_result_and_records_it(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        use_case = ComputeVarianceUseCase(history, clock)
        assert use_case.execute([1.0, 2.0, 3.0, 4.0, 5.0]) == 2.0
        assert history.all()[0].operation == "variance"


class TestGetHistoryUseCase:
    def test_returns_snapshot_of_history(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        ComputeFactorialUseCase(history, clock).execute(3)
        ComputeGcdUseCase(history, clock).execute(4, 6)
        entries = GetHistoryUseCase(history).execute()
        assert len(entries) == 2

    def test_returns_empty_tuple_when_history_is_empty(
        self, history: InMemoryCalculationHistory
    ) -> None:
        assert GetHistoryUseCase(history).execute() == ()


class TestClearHistoryUseCase:
    def test_removes_every_record(
        self, history: InMemoryCalculationHistory, clock: FakeClock
    ) -> None:
        ComputeFactorialUseCase(history, clock).execute(3)
        ClearHistoryUseCase(history).execute()
        assert history.all() == ()


class TestComposition:
    def test_use_cases_accept_the_production_clock(self) -> None:
        """The SystemClock is compatible with the Clock protocol."""
        repo = InMemoryCalculationHistory()
        use_case = ComputeFactorialUseCase(repo, SystemClock())
        assert use_case.execute(3) == 6
        assert len(repo.all()) == 1
