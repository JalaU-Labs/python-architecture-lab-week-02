# Architecture

The project follows the four-layer structure of Clean Architecture. The
dependency rule is strict: source-code dependencies always point inward,
toward the domain.

## Layers

### Domain (`math_toolkit_jala.domain`)

The innermost layer. Contains the business rules and has no knowledge of
any external system.

- `arithmetic.py` and `statistics.py` define the pure mathematical
  functions.
- `entities.py` defines the `Calculation` value object.
- `exceptions.py` defines the domain exception hierarchy.

### Application (`math_toolkit_jala.application`)

Orchestrates the domain to fulfill use cases. Depends on the domain and
on abstract ports, never on concrete infrastructure.

- `ports.py` declares the `CalculationHistoryRepository` and `Clock`
  protocols.
- `use_cases.py` contains the use case classes that the CLI invokes.

### Infrastructure (`math_toolkit_jala.infrastructure`)

Concrete adapters that satisfy the ports declared by the application.

- `in_memory.py` provides `InMemoryCalculationHistory`.
- `clock.py` provides `SystemClock`.

### Presentation (`math_toolkit_jala.presentation`)

The `argparse`-based CLI. It is a thin translation layer: it parses
arguments, invokes use cases, and formats results. It contains no
business logic.

## Dependency rule in practice

The composition root is the `main` function in
`math_toolkit_jala.presentation.cli`. It is the only place in the
codebase where all four layers are instantiated together:

```python
def _build_context(repository=None, clock=None):
    repo = repository if repository is not None else InMemoryCalculationHistory()
    clk = clock if clock is not None else SystemClock()
    return CommandContext(
        factorial=ComputeFactorialUseCase(repo, clk),
        ...
    )
```

Every other module imports only from inner layers. This guarantees that
the domain can be tested without any external dependency, and that
replacing the in-memory repository with a persistent one requires no
change outside `infrastructure/`.
