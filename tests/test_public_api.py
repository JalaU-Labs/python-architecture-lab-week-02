"""Tests that the top-level public API of the package is stable."""

from __future__ import annotations

import pytest

import math_toolkit_jala


@pytest.mark.parametrize(
    "name",
    [
        "factorial",
        "gcd",
        "lcm",
        "is_prime",
        "mean",
        "median",
        "variance",
        "MathUtilsError",
        "InvalidInputError",
        "DomainError",
        "__version__",
    ],
)
def test_public_name_is_exported(name: str) -> None:
    assert hasattr(math_toolkit_jala, name)


def test_all_matches_exports() -> None:
    expected = {
        "DomainError",
        "InvalidInputError",
        "MathUtilsError",
        "__version__",
        "factorial",
        "gcd",
        "is_prime",
        "lcm",
        "mean",
        "median",
        "variance",
    }
    assert set(math_toolkit_jala.__all__) == expected


def test_domain_reexports_are_the_same_objects() -> None:
    from math_toolkit_jala.domain.arithmetic import factorial as domain_factorial

    assert math_toolkit_jala.factorial is domain_factorial
