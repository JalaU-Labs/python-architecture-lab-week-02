"""Unit tests for :mod:`math_toolkit_jala.core.statistics`."""

from __future__ import annotations

import pytest

from math_toolkit_jala.core.statistics import mean, median, variance
from math_toolkit_jala.exceptions import DomainError


class TestMean:
    @pytest.mark.parametrize(
        ("values", "expected"),
        [
            ([1], 1.0),
            ([1, 2, 3, 4, 5], 3.0),
            ([2, 4, 6], 4.0),
            ([1.5, 2.5, 3.5], 2.5),
            ([-1, 0, 1], 0.0),
        ],
    )
    def test_returns_expected_value(self, values: list[float], expected: float) -> None:
        assert mean(values) == pytest.approx(expected)

    def test_raises_domain_error_for_empty_input(self) -> None:
        with pytest.raises(DomainError, match="at least one value"):
            mean([])


class TestMedian:
    @pytest.mark.parametrize(
        ("values", "expected"),
        [
            ([1], 1.0),
            ([1, 3, 2], 2.0),
            ([1, 2, 3, 4], 2.5),
            ([5, 4, 3, 2, 1], 3.0),
            ([2, 2, 2, 2], 2.0),
        ],
    )
    def test_returns_expected_value(self, values: list[float], expected: float) -> None:
        assert median(values) == pytest.approx(expected)

    def test_raises_domain_error_for_empty_input(self) -> None:
        with pytest.raises(DomainError, match="at least one value"):
            median([])


class TestVariance:
    @pytest.mark.parametrize(
        ("values", "expected"),
        [
            ([1], 0.0),
            ([1, 1, 1], 0.0),
            ([1, 2, 3, 4, 5], 2.0),
            ([2, 4, 4, 4, 5, 5, 7, 9], 4.0),
        ],
    )
    def test_returns_expected_value(self, values: list[float], expected: float) -> None:
        assert variance(values) == pytest.approx(expected)

    def test_raises_domain_error_for_empty_input(self) -> None:
        with pytest.raises(DomainError, match="at least one value"):
            variance([])
