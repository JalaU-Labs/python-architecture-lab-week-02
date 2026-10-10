# python-architecture-lab-week-02

[![Python](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)

A small, well-structured Python package of mathematical utilities built as
the Week 02 laboratory for the Software Development 4 course at Jala
University. Its primary purpose is to demonstrate professional software
architecture practices: layered design, pure domain logic, strict typing,
comprehensive testing, and reproducible tooling.

## Features

- Pure, side-effect-free mathematical functions in a dedicated core layer.
- Strict static typing enforced by `mypy` with `py.typed` marker (PEP 561).
- Command-line interface built on the standard library `argparse`.
- Comprehensive test suite powered by `pytest`.
- Deterministic dependency management via `uv` and `uv.lock`.
- Linting and formatting with `ruff`.
- Reproducible container image built with a multi-stage `Dockerfile`
  and published to the GitHub Container Registry.
- Convenience targets for common workflows via `Makefile`.

## Project Structure

```
.
├── src/
│   └── math_utils/
│       ├── __init__.py          # Public API re-exports and __version__
│       ├── __main__.py          # Entry point for `python -m math_utils`
│       ├── cli.py               # Presentation layer (argparse)
│       ├── exceptions.py        # Domain exception hierarchy
│       ├── py.typed             # PEP 561 typing marker
│       └── core/                # Pure domain logic
│           ├── __init__.py
│           ├── arithmetic.py
│           └── statistics.py
├── tests/
│   ├── __init__.py
│   ├── test_arithmetic.py
│   ├── test_cli.py
│   └── test_statistics.py
├── .dockerignore
├── .gitignore
├── .python-version
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
└── uv.lock
```

The `core` package contains pure functions with no knowledge of the
command-line interface, the filesystem, or any external system. The `cli`
module is the only place that performs I/O and translates user input into
calls against the core. This separation keeps the domain logic trivial to
test and reuse.

## Requirements

- Python 3.14 or newer
- [uv](https://github.com/astral-sh/uv) 0.13 or newer
- Docker 29 or newer (only for container workflows)

## Installation

Clone the repository and install the project in editable mode together
with its development dependencies:

```bash
git clone git@gitlab.com:jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02.git
cd python-architecture-lab-week-02
uv sync
```

## Usage

### Command-line interface

The package exposes a `math-utils` console script and the equivalent
module entry point:

```bash
uv run math-utils factorial 5
uv run math-utils is-prime 97
uv run math-utils mean 1 2 3 4 5
uv run python -m math_utils median 3 1 4 1 5 9 2 6
```

### Library

```python
from math_utils import factorial, is_prime, mean

assert factorial(5) == 120
assert is_prime(97) is True
assert mean([1, 2, 3, 4, 5]) == 3.0
```

## Development

All routine tasks are wrapped in the `Makefile`. Run `make help` to list
the available targets.

### Running tests

```bash
make test
```

This executes `pytest` against the `tests/` directory with coverage
reporting enabled.

### Linting and formatting

```bash
make lint      # ruff check
make format    # ruff format
```

### Type checking

```bash
make typecheck # mypy src
```

### Cleaning build artifacts

```bash
make clean
```

## Docker

### Pull the published image from GHCR

The image is published publicly to the GitHub Container Registry on every
push to `main` and on every `v*` tag. The package is public, so no
authentication is required to pull it:

```bash
docker pull ghcr.io/jalau-labs/python-architecture-lab-week-02:latest
```

Run the CLI directly with the published image:

```bash
docker run --rm ghcr.io/jalau-labs/python-architecture-lab-week-02:latest factorial 5
docker run --rm ghcr.io/jalau-labs/python-architecture-lab-week-02:latest is-prime 97
docker run --rm ghcr.io/jalau-labs/python-architecture-lab-week-02:latest mean 1 2 3 4 5
```

The following tags are published:

| Tag | Description |
| --- | --- |
| `latest` | Most recent build from the default branch. |
| `main` | Latest commit pushed to the `main` branch. |
| `sha-<short>` | Immutable reference to a specific commit. |
| `vX.Y.Z` | Semver tag, published when a `v*` Git tag is pushed. |

The image uses `math-utils` as its `ENTRYPOINT`, so any argument passed
to `docker run` is forwarded directly to the CLI.

### Build the image locally

Build the runtime image:

```bash
docker build -t math-utils:latest .
```

### Run with Docker Compose

Run the CLI through Docker Compose using the locally built image:

```bash
docker compose run --rm math-utils factorial 10
```

The image is built using a multi-stage `Dockerfile`: the first stage
installs dependencies with `uv` into a virtual environment, and the final
stage copies only the runtime artifacts into a slim base image.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE)
for details.
