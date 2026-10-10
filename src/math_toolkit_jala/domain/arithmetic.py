"""Pure arithmetic functions covering integers only."""

from __future__ import annotations

from math_toolkit_jala.domain.exceptions import DomainError, InvalidInputError


def _ensure_int(value: object, name: str) -> int:
    """Validate that ``value`` is a genuine ``int`` (and not a ``bool``)."""
    if isinstance(value, bool):
        raise InvalidInputError(f"{name} must be an int, got bool")
    if not isinstance(value, int):
        raise InvalidInputError(f"{name} must be an int, got {type(value).__name__}")
    return value


def factorial(n: int) -> int:
    """Return ``n!`` for a non-negative integer ``n``.

    Raises:
        InvalidInputError: If ``n`` is not a genuine ``int``.
        DomainError: If ``n`` is negative.
    """
    _ensure_int(n, "n")
    if n < 0:
        raise DomainError(f"factorial is undefined for negative integers: {n}")
    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of ``a`` and ``b``.

    The result is always non-negative. ``gcd(0, 0)`` is defined as ``0``.
    """
    _ensure_int(a, "a")
    _ensure_int(b, "b")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of ``a`` and ``b``.

    ``lcm(0, x)`` is defined as ``0`` for any integer ``x``.
    """
    _ensure_int(a, "a")
    _ensure_int(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_prime(n: int) -> bool:
    """Return ``True`` if ``n`` is a prime number, ``False`` otherwise."""
    _ensure_int(n, "n")
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True
