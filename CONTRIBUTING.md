# Contributing to python-architecture-lab-week-02

Thanks for your interest in improving this project. This document
describes the workflow for cloning the repository, running the tests,
and submitting changes.

## Prerequisites

- Python 3.14 or newer
- [uv](https://github.com/astral-sh/uv) 0.13 or newer
- Git
- Docker 29 or newer (only if you intend to work on the container image)

## Cloning the repository

The canonical repository is hosted on GitLab. A read-only mirror is
maintained on GitHub.

```bash
git clone git@gitlab.com:jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02.git
cd python-architecture-lab-week-02
uv sync
```

`uv sync` installs both the runtime and development dependencies from
`uv.lock`, creating an isolated `.venv` in the project root.

## Running the tests

The full quality gate is available through the `Makefile`:

```bash
make check
```

This runs, in order:

1. `ruff check` against `src/` and `tests/`.
2. `mypy` against `src/` and `tests/`.
3. `pytest` with coverage reporting.

To run the test suite alone:

```bash
make test
```

The project enforces 100% line and branch coverage on the `math_toolkit_jala`
package. Any change that reduces coverage below 100% is considered a
regression.

## Code style

- Formatting and linting are enforced by `ruff` with a strict rule set
  configured in `pyproject.toml`.
- Type checking is enforced by `mypy` in strict mode.
- All public functions, classes, and modules must carry docstrings.
- Use `from __future__ import annotations` at the top of every module.

Before committing, always run:

```bash
make format
make check
```

## Submitting changes

1. Create a topic branch off `main`:
   ```bash
   git switch -c feat/short-description
   ```
2. Make your changes, ensuring `make check` passes.
3. Write a commit message following the Conventional Commits
   specification. Examples:
   - `feat: add support for geometric mean`
   - `fix: handle empty input in variance`
   - `docs: clarify installation steps`
   - `test: cover negative integers in gcd`
4. Push the branch to `origin`:
   ```bash
   git push -u origin feat/short-description
   ```
5. Open a merge request on GitLab. The CI pipeline will run the same
   checks you ran locally.

## Continuous integration

Every push to `main` and every merge request triggers:

- **GitLab CI**: `lint`, `format`, `typecheck`, and `test` jobs.
- **GitHub Actions**: the same quality jobs, plus publication of the
  container image to GHCR on pushes to `main` and on `v*` tags.

Both pipelines must be green before a merge request can be merged.

## Reporting issues

Open an issue on the GitLab repository with:

- A clear description of the problem.
- The exact command that reproduces it.
- The expected and observed behaviour.
- Your Python version and operating system.

## License

By contributing, you agree that your contributions will be licensed
under the MIT License. See [LICENSE](LICENSE) for details.
