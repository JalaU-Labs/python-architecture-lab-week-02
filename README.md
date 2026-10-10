# python-architecture-lab-week-02

[![Python](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/math-toolkit-jala.svg)](https://pypi.org/project/math-toolkit-jala/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/math-toolkit-jala.svg)](https://pypi.org/project/math-toolkit-jala/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/math-toolkit-jala.svg)](https://pypi.org/project/math-toolkit-jala/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/JalaU-Labs/python-architecture-lab-week-02/actions/workflows/ci.yml/badge.svg)](https://github.com/JalaU-Labs/python-architecture-lab-week-02/actions/workflows/ci.yml)
[![Docs](https://github.com/JalaU-Labs/python-architecture-lab-week-02/actions/workflows/docs.yml/badge.svg)](https://github.com/JalaU-Labs/python-architecture-lab-week-02/actions/workflows/docs.yml)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)

A small, well-structured Python package of mathematical utilities built
as the Week 02 laboratory for the Software Development 4 course at Jala
University. The package is organized into the four layers of Clean
Architecture (Domain, Application, Infrastructure, and Presentation) and
demonstrates professional practices across the entire delivery pipeline.

## Features

- Four-layer Clean Architecture with a strict inward-pointing dependency
  rule.
- Pure, side-effect-free mathematical functions in a dedicated domain
  layer.
- Use cases that orchestrate the domain and depend only on abstract
  ports.
- An in-memory repository adapter that satisfies the history port.
- Strict static typing enforced by `mypy` with a `py.typed` marker
  (PEP 561).
- Command-line interface built on the standard library `argparse`.
- Comprehensive test suite with 100% line and branch coverage.
- Deterministic dependency management via `uv` and `uv.lock`.
- Linting and formatting with `ruff`.
- Reproducible container image built with a multi-stage `Dockerfile`
  and published to the GitHub Container Registry.
- Published on PyPI as `math-toolkit-jala`.
- Documentation site built with MkDocs and Material, deployed to both
  GitHub Pages and GitLab Pages.
- Continuous integration on GitHub Actions and GitLab CI.
- Convenience targets for common workflows via `Makefile`.

## Architecture

The source code is organized into four packages that mirror the four
layers of Clean Architecture:

| Layer | Package | Responsibility |
| --- | --- | --- |
| Domain | `math_toolkit_jala.domain` | Pure mathematical rules, `Calculation` entity, exception hierarchy. |
| Application | `math_toolkit_jala.application` | Ports and use case classes. |
| Infrastructure | `math_toolkit_jala.infrastructure` | In-memory repository and system clock adapters. |
| Presentation | `math_toolkit_jala.presentation` | `argparse`-based CLI. |

Dependencies always point inward: the domain knows nothing about the
other layers, the application depends only on the domain and on abstract
ports, and the infrastructure and presentation layers depend on the inner
layers. The composition root lives in
`math_toolkit_jala.presentation.cli` and is the only place where all four
layers are instantiated together.

## Project Structure

```
.
├── src/
│   └── math_toolkit_jala/
│       ├── __init__.py              # Public API re-exports and __version__
│       ├── __main__.py              # Entry point for `python -m math_toolkit_jala`
│       ├── py.typed                 # PEP 561 typing marker
│       ├── domain/                  # Business rules and entities
│       │   ├── __init__.py
│       │   ├── arithmetic.py
│       │   ├── entities.py
│       │   ├── exceptions.py
│       │   └── statistics.py
│       ├── application/             # Use cases and ports
│       │   ├── __init__.py
│       │   ├── ports.py
│       │   └── use_cases.py
│       ├── infrastructure/          # Concrete adapters
│       │   ├── __init__.py
│       │   ├── clock.py
│       │   └── in_memory.py
│       └── presentation/            # CLI
│           ├── __init__.py
│           └── cli.py
├── tests/
│   ├── __init__.py
│   ├── test_public_api.py
│   ├── domain/
│   │   ├── test_arithmetic.py
│   │   ├── test_entities.py
│   │   ├── test_exceptions.py
│   │   └── test_statistics.py
│   ├── application/
│   │   └── test_use_cases.py
│   ├── infrastructure/
│   │   ├── test_clock.py
│   │   └── test_in_memory.py
│   └── presentation/
│       └── test_cli.py
├── docs/
│   ├── api.md
│   ├── architecture.md
│   ├── examples.md
│   ├── index.md
│   └── quickstart.md
├── .github/workflows/
│   ├── ci.yml
│   ├── docs.yml
│   └── publish.yml
├── .dockerignore
├── .gitignore
├── .python-version
├── CHANGELOG.md
├── CONTRIBUTING.md
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── Makefile
├── mkdocs.yml
├── pyproject.toml
├── README.md
└── uv.lock
```

## Requirements

- Python 3.14 or newer
- [uv](https://github.com/astral-sh/uv) 0.13 or newer (for development)
- Docker 29 or newer (only for container workflows)

## Installation

### From PyPI

```bash
pip install math-toolkit-jala
```

```bash
uv add math-toolkit-jala
```

### From source

```bash
git clone git@gitlab.com:jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02.git
cd python-architecture-lab-week-02
uv sync
```

## Usage

### Command-line interface

```bash
math-toolkit-jala factorial 5     # 120
math-toolkit-jala is-prime 97     # true
math-toolkit-jala mean 1 2 3 4 5  # 3.0
math-toolkit-jala demo            # shows the whole stack in action
math-toolkit-jala history         # prints the session's calculation history
```

### Library

```python
from math_toolkit_jala import factorial, is_prime, mean

assert factorial(5) == 120
assert is_prime(97) is True
assert mean([1, 2, 3, 4, 5]) == 3.0
```

### Use cases and infrastructure

```python
from math_toolkit_jala.application import ComputeFactorialUseCase
from math_toolkit_jala.infrastructure import (
    InMemoryCalculationHistory,
    SystemClock,
)

history = InMemoryCalculationHistory()
use_case = ComputeFactorialUseCase(history, SystemClock())
use_case.execute(5)
print(history.all()[0].formatted())  # factorial(5) = 120
```

## Documentation

- GitHub Pages: [https://jalau-labs.github.io/python-architecture-lab-week-02/](https://jalau-labs.github.io/python-architecture-lab-week-02/)
- GitLab Pages: [https://jala-university1.pages.gitlab.com/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02/](https://jala-university1.pages.gitlab.com/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02/)

## Development

```bash
make help         # list every available target
make check        # ruff check + mypy + pytest with 100% coverage
make format       # ruff format + ruff check --fix
make docs-serve   # live-reload documentation at http://127.0.0.1:8000
make docs-build   # build the static documentation site
```

## Docker

### Pull the published image from GHCR

```bash
docker pull ghcr.io/jalau-labs/python-architecture-lab-week-02:latest
docker run --rm ghcr.io/jalau-labs/python-architecture-lab-week-02:latest factorial 5
```

The image is public; no authentication is required.

### Build the image locally

```bash
docker build -t math-toolkit-jala:latest .
```

### Run with Docker Compose

```bash
docker compose run --rm math-toolkit-jala factorial 10
```

## Continuous Integration

| Platform | Pipeline | Jobs |
| --- | --- | --- |
| GitHub Actions | `ci.yml` | lint, format, typecheck, test, publish image to GHCR |
| GitHub Actions | `docs.yml` | build and deploy to GitHub Pages |
| GitHub Actions | `publish.yml` | build and publish to PyPI on `v*` tags |
| GitLab CI | `.gitlab-ci.yml` | docs (Pages), lint, format, typecheck, test |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).
