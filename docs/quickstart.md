# Quickstart

## Installation

Clone the repository and install the project with `uv`:

```bash
git clone git@gitlab.com:jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02.git
cd python-architecture-lab-week-02
uv sync
```

## Run the CLI

```bash
uv run math-toolkit-jala factorial 5
# 120

uv run math-toolkit-jala is-prime 97
# true

uv run math-toolkit-jala mean 1 2 3 4 5
# 3.0
```

The equivalent module entry point works as well:

```bash
uv run python -m math_toolkit_jala median 3 1 4 1 5 9 2 6
# 3.5
```

## Use the library

```python
from math_toolkit_jala import factorial, is_prime, mean

assert factorial(5) == 120
assert is_prime(97) is True
assert mean([1, 2, 3, 4, 5]) == 3.0
```

## Run with Docker

The published image is available on GHCR and requires no authentication:

```bash
docker run --rm ghcr.io/jalau-labs/python-architecture-lab-week-02:latest factorial 5
# 120
```

## Next steps

- Read the [API Reference](api.md) for the full list of functions.
- Browse [Examples](examples.md) for more usage patterns.
