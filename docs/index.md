# math-utils

A small, well-structured Python package of mathematical utilities built as
the Week 02 laboratory for the Software Development 4 course at Jala
University.

The project demonstrates professional software architecture practices:
layered design with pure domain logic, strict static typing, comprehensive
testing, deterministic dependency management, and reproducible container
images.

## Design principles

- **Layered architecture.** The `core` package contains pure,
  side-effect-free functions. The `cli` module is the only place that
  performs I/O and translates user input into calls against the core.
- **Strict typing.** Every module ships a `py.typed` marker (PEP 561) and
  is checked with `mypy` in strict mode.
- **Test-driven quality.** The test suite covers 100% of lines and
  branches in the `math_utils` package.
- **Reproducibility.** Dependencies are resolved deterministically via
  `uv.lock`. The container image is built from a multi-stage
  `Dockerfile` using the same lock file.

## Next steps

- [Quickstart](quickstart.md) — install the package and run your first
  command in under a minute.
- [API Reference](api.md) — every public function, with signatures and
  behaviour.
- [Examples](examples.md) — usage patterns for the CLI and the library.
