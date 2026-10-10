"""Unit tests for :mod:`math_toolkit_jala.domain.entities`."""

from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

import pytest

from math_toolkit_jala.domain.entities import Calculation


def _make_calculation() -> Calculation:
    return Calculation(
        operation="factorial",
        arguments=(5,),
        result=120,
        timestamp=datetime(2026, 10, 13, 12, 0, 0, tzinfo=UTC),
    )


class TestCalculation:
    def test_stores_every_field_verbatim(self) -> None:
        timestamp = datetime(2026, 10, 13, 12, 0, 0, tzinfo=UTC)
        calc = Calculation(
            operation="gcd",
            arguments=(12, 18),
            result=6,
            timestamp=timestamp,
        )
        assert calc.operation == "gcd"
        assert calc.arguments == (12, 18)
        assert calc.result == 6
        assert calc.timestamp == timestamp

    def test_is_frozen(self) -> None:
        calc = _make_calculation()
        with pytest.raises(FrozenInstanceError):
            calc.result = 999  # type: ignore[misc]

    def test_equality_is_value_based(self) -> None:
        assert _make_calculation() == _make_calculation()

    def test_formatted_with_single_argument(self) -> None:
        assert _make_calculation().formatted() == "factorial(5) = 120"

    def test_formatted_with_multiple_arguments(self) -> None:
        calc = Calculation(
            operation="gcd",
            arguments=(12, 18),
            result=6,
            timestamp=datetime(2026, 10, 13, tzinfo=UTC),
        )
        assert calc.formatted() == "gcd(12, 18) = 6"

    def test_formatted_with_boolean_result(self) -> None:
        calc = Calculation(
            operation="is_prime",
            arguments=(97,),
            result=True,
            timestamp=datetime(2026, 10, 13, tzinfo=UTC),
        )
        assert calc.formatted() == "is_prime(97) = True"
