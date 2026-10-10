# API Reference

Every public function is exported from the top-level `math_toolkit_jala`
package. The `core` subpackage contains the pure domain logic; the
top-level re-exports exist for convenience.

## Arithmetic

### `factorial(n: int) -> int`

Return `n!` for a non-negative integer `n`.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `int` | A non-negative integer. |

**Raises:**

- `InvalidInputError` if `n` is not a genuine `int` (booleans are
  rejected).
- `DomainError` if `n` is negative.

### `gcd(a: int, b: int) -> int`

Return the greatest common divisor of `a` and `b`. The result is always
non-negative. `gcd(0, 0)` is defined as `0`.

### `lcm(a: int, b: int) -> int`

Return the least common multiple of `a` and `b`. `lcm(0, x)` is defined
as `0` for any integer `x`.

### `is_prime(n: int) -> bool`

Return `True` if `n` is a prime number, `False` otherwise. Uses trial
division with a `sqrt(n)` bound.

## Statistics

### `mean(values: Sequence[float]) -> float`

Return the arithmetic mean of `values`.

**Raises:** `DomainError` if `values` is empty.

### `median(values: Sequence[float]) -> float`

Return the median of `values`. For even-length sequences, returns the
average of the two middle elements.

**Raises:** `DomainError` if `values` is empty.

### `variance(values: Sequence[float]) -> float`

Return the population variance of `values`.

**Raises:** `DomainError` if `values` is empty.

## Exceptions

All exceptions inherit from `MathUtilsError`:

- `InvalidInputError` — raised when an argument has an unsupported type.
- `DomainError` — raised when a value violates a mathematical domain
  constraint.
