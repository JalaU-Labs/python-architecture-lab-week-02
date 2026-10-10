# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-10-13

### Added

- **Domain layer** at `math_toolkit_jala.domain`, containing the pure
  mathematical functions, the `Calculation` entity, the exception
  hierarchy, and the domain-facing definitions.
- **Application layer** at `math_toolkit_jala.application`, containing
  the ports consumed by the use cases and eight use case classes:
  `ComputeFactorialUseCase`, `ComputeGcdUseCase`, `ComputeLcmUseCase`,
  `IsPrimeUseCase`, `ComputeMeanUseCase`, `ComputeMedianUseCase`,
  `ComputeVarianceUseCase`, `GetHistoryUseCase`, and
  `ClearHistoryUseCase`.
- **Infrastructure layer** at `math_toolkit_jala.infrastructure`,
  containing `InMemoryCalculationHistory` (an in-memory implementation
  of `CalculationHistoryRepository`) and `SystemClock` (an adapter for
  the `Clock` port).
- **Presentation layer** at `math_toolkit_jala.presentation`, containing
  the `argparse`-based CLI.
- New `history` subcommand that prints the calculations recorded during
  the current session.
- New `clear-history` subcommand that resets the in-memory history.
- New `demo` subcommand that exercises the four layers end-to-end in a
  single invocation.
- `CHANGELOG.md` (this file), following the Keep a Changelog format.

### Changed

- Reorganized the source tree to make the four layers of Clean
  Architecture explicit: `domain/`, `application/`, `infrastructure/`,
  and `presentation/`.
- The CLI is now driven by use cases instead of calling the domain
  functions directly, and it delegates the composition of its
  dependencies to a single `_build_context` factory.

### Removed

- The `math_toolkit_jala.core` package, whose contents now live in
  `math_toolkit_jala.domain`.
- The top-level `math_toolkit_jala.exceptions` module, whose contents now
  live in `math_toolkit_jala.domain.exceptions`. The three public
  exception classes remain re-exported from the top-level package.
- The `_build_parser` subparser-level handlers; commands are now
  dispatched through a `_HANDLERS` dictionary keyed by subcommand name.

### Breaking changes

- Imports of the form `from math_toolkit_jala.core.arithmetic import ...`
  or `from math_toolkit_jala.exceptions import ...` no longer work.
  Use `from math_toolkit_jala.domain.arithmetic import ...` or
  `from math_toolkit_jala import MathUtilsError` instead.
- The top-level public API (`from math_toolkit_jala import factorial,
  mean, ...`) is unchanged.
- The CLI commands and their output are unchanged. New commands are
  additive.

## [0.1.0] - 2026-10-10

### Added

- Initial release of `math-toolkit-jala`.
- Seven mathematical utilities: `factorial`, `gcd`, `lcm`, `is_prime`,
  `mean`, `median`, and `variance`.
- `math-toolkit-jala` console script and `python -m math_toolkit_jala`
  entry point.
- Exception hierarchy: `MathUtilsError`, `InvalidInputError`, and
  `DomainError`.
- Comprehensive test suite with 100% line and branch coverage.
- Multi-stage `Dockerfile` and `docker-compose.yml`.
- GitHub Actions and GitLab CI pipelines.
- `Makefile` with targets for tests, lint, type check, documentation, and
  Docker.
- MkDocs Material documentation site deployed to GitHub Pages and GitLab
  Pages.
- Publication of the container image to the GitHub Container Registry.
- Publication of the package to the Python Package Index.
- `CONTRIBUTING.md` with the full contributor workflow.

[Unreleased]: https://gitlab.com/jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02/-/compare/v0.2.0...main
[0.2.0]: https://gitlab.com/jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02/-/compare/v0.1.0...v0.2.0
[0.1.0]: https://gitlab.com/jala-university1/cohort-5/ES.CSSD-245.GA.T2.26.M2/SD/group-b/individual-laboratories/alejandro-botina/week-02/python-architecture-lab-week-02/-/releases/v0.1.0
