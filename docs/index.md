# math-toolkit-jala

A small, well-structured Python package of mathematical utilities built as
the Week 02 laboratory for the Software Development 4 course at Jala
University.

The project demonstrates professional software architecture practices:
layered design with pure domain logic, strict static typing, comprehensive
testing, deterministic dependency management, and reproducible container
images.

## Design principles

- **Layered architecture.** The package is organized into four layers
  that follow the dependency rule of Clean Architecture: `domain`,
  `application`, `infrastructure`, and `presentation`. Dependencies
  always point inward, toward the domain.
- **Strict typing.** Every module ships a `py.typed` marker (PEP 561) and
  is checked with `mypy` in strict mode.
- **Test-driven quality.** The test suite covers 100% of lines and
  branches in the `math_toolkit_jala` package.
- **Reproducibility.** Dependencies are resolved deterministically via
  `uv.lock`. The container image is built from a multi-stage
  `Dockerfile` using the same lock file.

## Next steps

- [Architecture](architecture.md) — the four layers and the dependency
  rule.
- [Quickstart](quickstart.md) — install the package and run your first
  command in under a minute.
- [API Reference](api.md) — every public function, with signatures and
  behaviour.
- [Examples](examples.md) — usage patterns for the CLI and the library.
