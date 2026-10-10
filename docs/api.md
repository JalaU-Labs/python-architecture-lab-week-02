# API Reference

The package is organized into four layers. This page documents the public
surface of each layer, from the innermost (Domain) to the outermost
(Presentation). The top-level package re-exports the most commonly used
names from the Domain layer for convenience.

## Domain

Package: `math_toolkit_jala.domain`

The Domain layer contains the mathematical rules and the value objects
that describe the business model. It has no dependency on any other
layer.

### Arithmetic functions

#### `factorial(n: int) -> int`

Return `n!` for a non-negative integer `n`.

**Raises:**

- `InvalidInputError` if `n` is not a genuine `int` (booleans are
  rejected).
- `DomainError` if `n` is negative.

#### `gcd(a: int, b: int) -> int`

Return the greatest common divisor of `a` and `b`. The result is always
non-negative. `gcd(0, 0)` is defined as `0`.

#### `lcm(a: int, b: int) -> int`

Return the least common multiple of `a` and `b`. `lcm(0, x)` is defined
as `0` for any integer `x`.

#### `is_prime(n: int) -> bool`

Return `True` if `n` is a prime number, `False` otherwise. Uses trial
division with a `sqrt(n)` bound.

### Statistics functions

#### `mean(values: Sequence[float]) -> float`

Return the arithmetic mean of `values`.

**Raises:** `DomainError` if `values` is empty.

#### `median(values: Sequence[float]) -> float`

Return the median of `values`. For even-length sequences, returns the
average of the two middle elements.

**Raises:** `DomainError` if `values` is empty.

#### `variance(values: Sequence[float]) -> float`

Return the population variance of `values`.

**Raises:** `DomainError` if `values` is empty.

### Entity: `Calculation`

A frozen dataclass that represents a single operation recorded in the
history.

| Field | Type | Description |
| --- | --- | --- |
| `operation` | `str` | The name of the operation, e.g. `"factorial"`. |
| `arguments` | `tuple[int \| float, ...]` | The positional arguments of the operation. |
| `result` | `int \| float \| bool` | The value returned by the operation. |
| `timestamp` | `datetime` | A timezone-aware timestamp. |

Method: `formatted() -> str` returns a compact string such as
`"factorial(5) = 120"`.

### Exceptions

All exceptions inherit from `MathUtilsError`:

- `InvalidInputError` — raised when an argument has an unsupported type.
- `DomainError` — raised when a value violates a mathematical domain
  constraint.

The three classes are also re-exported from the top-level package for
convenience.

## Application

Package: `math_toolkit_jala.application`

The Application layer orchestrates the Domain to fulfill use cases. It
depends on the Domain and on abstract ports, never on concrete
infrastructure.

### Ports

Two `Protocol` classes define the contracts that infrastructure adapters
must satisfy.

#### `CalculationHistoryRepository`

- `add(calculation: Calculation) -> None`
- `all() -> tuple[Calculation, ...]`
- `clear() -> None`

#### `Clock`

- `now() -> datetime` — must return a timezone-aware datetime.

### Use cases

Each use case is a class with an `execute` method. Use cases that perform
a mathematical operation record the result in the history repository.

| Use case | Method | Description |
| --- | --- | --- |
| `ComputeFactorialUseCase` | `execute(n: int) -> int` | `factorial(n)`, records the result. |
| `ComputeGcdUseCase` | `execute(a: int, b: int) -> int` | `gcd(a, b)`, records the result. |
| `ComputeLcmUseCase` | `execute(a: int, b: int) -> int` | `lcm(a, b)`, records the result. |
| `IsPrimeUseCase` | `execute(n: int) -> bool` | `is_prime(n)`, records the result. |
| `ComputeMeanUseCase` | `execute(values: Sequence[float]) -> float` | `mean(values)`, records the result. |
| `ComputeMedianUseCase` | `execute(values: Sequence[float]) -> float` | `median(values)`, records the result. |
| `ComputeVarianceUseCase` | `execute(values: Sequence[float]) -> float` | `variance(values)`, records the result. |
| `GetHistoryUseCase` | `execute() -> tuple[Calculation, ...]` | Returns a snapshot of the history. |
| `ClearHistoryUseCase` | `execute() -> None` | Removes every record. |

## Infrastructure

Package: `math_toolkit_jala.infrastructure`

Concrete adapters that satisfy the ports defined by the Application
layer.

### `InMemoryCalculationHistory`

List-backed implementation of `CalculationHistoryRepository`. Replacing
this class with a SQLite, Redis, or PostgreSQL implementation requires no
change in the Domain or Application layers.

### `SystemClock`

Implements the `Clock` port by returning timezone-aware UTC datetimes
from `datetime.now(UTC)`.

## Presentation

Package: `math_toolkit_jala.presentation`

The `argparse`-based command-line interface. It contains no business
logic: it parses arguments, invokes use cases, and formats results.

### Commands

| Command | Arguments | Description |
| --- | --- | --- |
| `factorial` | `n` (int) | Compute `n!`. |
| `gcd` | `a b` (ints) | Compute the greatest common divisor. |
| `lcm` | `a b` (ints) | Compute the least common multiple. |
| `is-prime` | `n` (int) | Determine whether `n` is prime. |
| `mean` | `values...` (floats) | Compute the arithmetic mean. |
| `median` | `values...` (floats) | Compute the median. |
| `variance` | `values...` (floats) | Compute the population variance. |
| `history` | — | Print the recorded calculations. |
| `clear-history` | — | Discard the recorded calculations. |
| `demo` | — | Run a fixed sequence that exercises all four layers. |

### Global flags

- `--version` prints the installed version of the package.
- `--help` prints the usage message.

## Public API

The top-level `math_toolkit_jala` package re-exports the most commonly
used names:

```python
from math_toolkit_jala import (
    # functions
    factorial, gcd, lcm, is_prime, mean, median, variance,
    # exceptions
    MathUtilsError, InvalidInputError, DomainError,
    # metadata
    __version__,
)
```

Consumers who need the Application, Infrastructure, or Presentation
layers must import from the corresponding subpackage explicitly. This
keeps the top-level namespace small and stable.
