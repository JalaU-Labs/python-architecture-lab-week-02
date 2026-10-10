"""Unit tests for :mod:`math_toolkit_jala.core.arithmetic`."""

from __future__ import annotations

import pytest

from math_toolkit_jala.core.arithmetic import factorial, gcd, is_prime, lcm
from math_toolkit_jala.exceptions import DomainError, InvalidInputError


class TestFactorial:
    @pytest.mark.parametrize(
        ("n", "expected"),
        [
            (0, 1),
            (1, 1),
            (2, 2),
            (5, 120),
            (10, 3_628_800),
        ],
    )
    def test_returns_expected_value_for_non_negative_inputs(self, n: int, expected: int) -> None:
        assert factorial(n) == expected

    def test_raises_domain_error_for_negative_input(self) -> None:
        with pytest.raises(DomainError, match="negative"):
            factorial(-1)

    def test_raises_invalid_input_error_for_float_argument(self) -> None:
        with pytest.raises(InvalidInputError, match="must be an int"):
            factorial(2.5)  # type: ignore[arg-type]

    def test_raises_invalid_input_error_for_bool_argument(self) -> None:
        with pytest.raises(InvalidInputError, match="must be an int"):
            factorial(True)


class TestGcd:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (12, 18, 6),
            (18, 12, 6),
            (17, 5, 1),
            (0, 5, 5),
            (5, 0, 5),
            (0, 0, 0),
            (-12, 18, 6),
            (-12, -18, 6),
        ],
    )
    def test_returns_expected_value(self, a: int, b: int, expected: int) -> None:
        assert gcd(a, b) == expected


class TestLcm:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (4, 6, 12),
            (21, 6, 42),
            (0, 5, 0),
            (5, 0, 0),
            (7, 13, 91),
            (-4, 6, 12),
        ],
    )
    def test_returns_expected_value(self, a: int, b: int, expected: int) -> None:
        assert lcm(a, b) == expected


class TestIsPrime:
    @pytest.mark.parametrize(
        ("n", "expected"),
        [
            (-7, False),
            (-1, False),
            (0, False),
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (9, False),
            (97, True),
            (100, False),
            (7919, True),
        ],
    )
    def test_returns_expected_value(self, n: int, expected: bool) -> None:
        assert is_prime(n) is expected
