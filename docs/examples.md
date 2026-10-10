# Examples

## Compute a factorial

```bash
uv run math-toolkit-jala factorial 10
# 3628800
```

## Check primality

```bash
uv run math-toolkit-jala is-prime 7919
# true

uv run math-toolkit-jala is-prime 7917
# false
```

## Aggregate statistics

```bash
uv run math-toolkit-jala mean 1 2 3 4 5
# 3.0

uv run math-toolkit-jala median 1 2 3 4
# 2.5

uv run math-toolkit-jala variance 1 2 3 4 5
# 2.0
```

## Handle errors gracefully

```bash
uv run math-toolkit-jala factorial -1
# error: factorial is undefined for negative integers: -1
# (exit code 1)
```

## Use inside another Python program

```python
from math_toolkit_jala import gcd, lcm, is_prime

# Simplify a fraction.
numerator, denominator = 42, 56
divisor = gcd(numerator, denominator)
print(f"{numerator // divisor}/{denominator // divisor}")  # 3/4

# Find the next prime after a given number.
candidate = 100
while not is_prime(candidate):
    candidate += 1
print(candidate)  # 101
```
## Inspect the calculation history

```bash
uv run math-toolkit-jala demo
```

This runs `factorial(5)`, `gcd(12, 18)`, `is_prime(97)`, and
`mean(1, 2, 3, 4, 5)` through the use cases and prints the recorded
history:

```
Demonstration of Clean Architecture layers:

  factorial(5) = 120
  gcd(12, 18) = 6
  is_prime(97) = True
  mean(1.0, 2.0, 3.0, 4.0, 5.0) = 3.0
```

## Use the use cases directly

```python
from math_toolkit_jala.application import ComputeFactorialUseCase
from math_toolkit_jala.infrastructure import (
    InMemoryCalculationHistory,
    SystemClock,
)

history = InMemoryCalculationHistory()
use_case = ComputeFactorialUseCase(history, SystemClock())
assert use_case.execute(5) == 120
assert history.all()[0].formatted() == "factorial(5) = 120"
```
