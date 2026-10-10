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

A small, well-structured Python package of mathematical utilities built as
the Week 02 laboratory for the Software Development 4 course at Jala
University. Its primary purpose is to demonstrate professional software
architecture practices: layered design, pure domain logic, strict typing,
comprehensive testing, and reproducible tooling.

## Features

- Pure, side-effect-free mathematical functions in a dedicated core layer.
- Strict static typing enforced by `mypy` with `py.typed` marker (PEP 561).
- Command-line interface built on the standard library `argparse`.
- Comprehensive test suite powered by `pytest` with 100% line and branch coverage.
- Deterministic dependency management via `uv` and `uv.lock`.
- Linting and formatting with `ruff`.
- Reproducible container image built with a multi-stage `Dockerfile`
  and published to the GitHub Container Registry.
- Published on PyPI as `math-toolkit-jala`.
- Documentation site built with MkDocs and Material, deployed to both
  GitHub Pages and GitLab Pages.
- Continuous integration on GitHub Actions and GitLab CI.
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
├── docs/
│   ├── api.md
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

The `core` package contains pure functions with no knowledge of the
command-line interface, the filesystem, or any external system. The `cli`
module is the only place that performs I/O and translates user input into
calls against the core. This separation keeps the domain logic trivial to
test and reuse.

## Requirements

- Python 3.14 or newer
- [uv](https://github.com/astral-sh/uv) 0.13 or newer (for development)
- Docker 29 or newer (only for container workflows)

## Installation

### From PyPI

The package is published on PyPI. Install it with `pip` or `uv`:

```bash
pip install math-toolkit-jala
```

```bash
uv add math-toolkit-jala
```

### From source

Clone the repository and install it in editable mode with `uv`:

```bash
git clone git@gitlab.com:jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02.git
cd python-architecture-lab-week-02
uv sync
```

## Usage

### Command-line interface

The package exposes a `math-toolkit-jala` console script:

```bash
math-toolkit-jala factorial 5
# 120

math-toolkit-jala is-prime 97
# true

math-toolkit-jala mean 1 2 3 4 5
# 3.0
```

The equivalent module entry point works as well:

```bash
python -m math_utils median 3 1 4 1 5 9 2 6
# 3.5
```

### Library

```python
from math_utils import factorial, is_prime, mean

assert factorial(5) == 120
assert is_prime(97) is True
assert mean([1, 2, 3, 4, 5]) == 3.0
```

## Documentation

The full documentation is available at:

- GitHub Pages: [https://jalau-labs.github.io/python-architecture-lab-week-02/](https://jalau-labs.github.io/python-architecture-lab-week-02/)
- GitLab Pages: [https://jala-university1.pages.gitlab.com/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02/](https://jala-university1.pages.gitlab.com/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02/)

It covers installation, the CLI, the full API reference, and examples.

## Development

All routine tasks are wrapped in the `Makefile`. Run `make help` to list
the available targets.

### Running tests

```bash
make test
```

This executes `pytest` against the `tests/` directory with coverage
reporting enabled. The project enforces 100% line and branch coverage on
the `math_utils` package.

### Linting and formatting

```bash
make lint      # ruff check
make format    # ruff format
```

### Type checking

```bash
make typecheck # mypy src
```

### Documentation

```bash
make docs-serve   # serve with live reload at http://127.0.0.1:8000
make docs-build   # build the static site into site/
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
# 120
```

The following tags are published:

| Tag | Description |
| --- | --- |
| `latest` | Most recent build from the default branch. |
| `main` | Latest commit pushed to the `main` branch. |
| `sha-<short>` | Immutable reference to a specific commit. |
| `vX.Y.Z` | Semver tag, published when a `v*` Git tag is pushed. |

The image uses `math-toolkit-jala` as its `ENTRYPOINT`, so any argument passed
to `docker run` is forwarded directly to the CLI.

### Build the image locally

```bash
docker build -t math-toolkit-jala:latest .
```

### Run with Docker Compose

```bash
docker compose run --rm math-toolkit-jala factorial 10
```

The image is built using a multi-stage `Dockerfile`: the first stage
installs dependencies with `uv` into a virtual environment, and the final
stage copies only the runtime artifacts into a slim base image.

## Continuous Integration

Every push to `main` and every merge request triggers:

| Platform | Pipeline | Jobs |
| --- | --- | --- |
| GitHub Actions | `ci.yml` | lint, format, typecheck, test, publish image to GHCR |
| GitHub Actions | `docs.yml` | build and deploy to GitHub Pages |
| GitHub Actions | `publish.yml` | build and publish to PyPI on `v*` tags |
| GitLab CI | `.gitlab-ci.yml` | docs (Pages), lint, format, typecheck, test |

Both platforms enforce the same quality gate: `ruff check`, `ruff format --check`,
`mypy`, and `pytest` with 100% coverage.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow: cloning,
running tests, code style, and submitting changes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE)
for details.
