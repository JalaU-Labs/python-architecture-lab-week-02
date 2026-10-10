# Examples

## Compute a factorial

```bash
uv run math-utils factorial 10
# 3628800
```

## Check primality

```bash
uv run math-utils is-prime 7919
# true

uv run math-utils is-prime 7917
# false
```

## Aggregate statistics

```bash
uv run math-utils mean 1 2 3 4 5
# 3.0

uv run math-utils median 1 2 3 4
# 2.5

uv run math-utils variance 1 2 3 4 5
# 2.0
```

## Handle errors gracefully

```bash
uv run math-utils factorial -1
# error: factorial is undefined for negative integers: -1
# (exit code 1)
```

## Use inside another Python program

```python
from math_utils import gcd, lcm, is_prime

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