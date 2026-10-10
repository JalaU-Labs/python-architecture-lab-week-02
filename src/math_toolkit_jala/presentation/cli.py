"""Command-line interface for the math_toolkit_jala package.

The CLI is a thin presentation layer: it parses arguments, delegates to
the use cases defined in the application layer, and formats the results.
It contains no business logic and no direct dependency on the domain
functions.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass

from math_toolkit_jala import __version__
from math_toolkit_jala.application.ports import (
    CalculationHistoryRepository,
    Clock,
)
from math_toolkit_jala.application.use_cases import (
    ClearHistoryUseCase,
    ComputeFactorialUseCase,
    ComputeGcdUseCase,
    ComputeLcmUseCase,
    ComputeMeanUseCase,
    ComputeMedianUseCase,
    ComputeVarianceUseCase,
    GetHistoryUseCase,
    IsPrimeUseCase,
)
from math_toolkit_jala.domain.exceptions import MathUtilsError
from math_toolkit_jala.infrastructure.clock import SystemClock
from math_toolkit_jala.infrastructure.in_memory import InMemoryCalculationHistory

type Handler = Callable[[argparse.Namespace, "CommandContext"], str]


@dataclass(frozen=True, slots=True)
class CommandContext:
    """Bundle of use cases available to every command handler."""

    factorial: ComputeFactorialUseCase
    gcd: ComputeGcdUseCase
    lcm: ComputeLcmUseCase
    is_prime: IsPrimeUseCase
    mean: ComputeMeanUseCase
    median: ComputeMedianUseCase
    variance: ComputeVarianceUseCase
    history: GetHistoryUseCase
    clear_history: ClearHistoryUseCase


def _build_context(
    repository: CalculationHistoryRepository | None = None,
    clock: Clock | None = None,
) -> CommandContext:
    """Compose the use cases with their concrete dependencies."""
    repo = repository if repository is not None else InMemoryCalculationHistory()
    clk = clock if clock is not None else SystemClock()
    return CommandContext(
        factorial=ComputeFactorialUseCase(repo, clk),
        gcd=ComputeGcdUseCase(repo, clk),
        lcm=ComputeLcmUseCase(repo, clk),
        is_prime=IsPrimeUseCase(repo, clk),
        mean=ComputeMeanUseCase(repo, clk),
        median=ComputeMedianUseCase(repo, clk),
        variance=ComputeVarianceUseCase(repo, clk),
        history=GetHistoryUseCase(repo),
        clear_history=ClearHistoryUseCase(repo),
    )


def _handle_factorial(args: argparse.Namespace, ctx: CommandContext) -> str:
    return str(ctx.factorial.execute(args.n))


def _handle_gcd(args: argparse.Namespace, ctx: CommandContext) -> str:
    return str(ctx.gcd.execute(args.a, args.b))


def _handle_lcm(args: argparse.Namespace, ctx: CommandContext) -> str:
    return str(ctx.lcm.execute(args.a, args.b))


def _handle_is_prime(args: argparse.Namespace, ctx: CommandContext) -> str:
    return "true" if ctx.is_prime.execute(args.n) else "false"


def _handle_mean(args: argparse.Namespace, ctx: CommandContext) -> str:
    return repr(ctx.mean.execute(args.values))


def _handle_median(args: argparse.Namespace, ctx: CommandContext) -> str:
    return repr(ctx.median.execute(args.values))


def _handle_variance(args: argparse.Namespace, ctx: CommandContext) -> str:
    return repr(ctx.variance.execute(args.values))


def _handle_history(args: argparse.Namespace, ctx: CommandContext) -> str:
    entries = ctx.history.execute()
    if not entries:
        return "(no calculations recorded in this session)"
    return "\n".join(f"  {entry.formatted()}" for entry in entries)


def _handle_clear_history(args: argparse.Namespace, ctx: CommandContext) -> str:
    ctx.clear_history.execute()
    return "history cleared"


def _handle_demo(args: argparse.Namespace, ctx: CommandContext) -> str:
    """Run a fixed sequence of operations to exercise every layer."""
    ctx.factorial.execute(5)
    ctx.gcd.execute(12, 18)
    ctx.is_prime.execute(97)
    ctx.mean.execute((1.0, 2.0, 3.0, 4.0, 5.0))
    entries = ctx.history.execute()
    lines = ["Demonstration of Clean Architecture layers:", ""]
    lines.extend(f"  {entry.formatted()}" for entry in entries)
    return "\n".join(lines)


_HANDLERS: dict[str, Handler] = {
    "factorial": _handle_factorial,
    "gcd": _handle_gcd,
    "lcm": _handle_lcm,
    "is-prime": _handle_is_prime,
    "mean": _handle_mean,
    "median": _handle_median,
    "variance": _handle_variance,
    "history": _handle_history,
    "clear-history": _handle_clear_history,
    "demo": _handle_demo,
}


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="math-toolkit-jala",
        description="Mathematical utilities from the math_toolkit_jala package.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    factorial_parser = subparsers.add_parser(
        "factorial",
        help="Compute n! for a non-negative integer.",
    )
    factorial_parser.add_argument("n", type=int)

    gcd_parser = subparsers.add_parser(
        "gcd",
        help="Compute the greatest common divisor of two integers.",
    )
    gcd_parser.add_argument("a", type=int)
    gcd_parser.add_argument("b", type=int)

    lcm_parser = subparsers.add_parser(
        "lcm",
        help="Compute the least common multiple of two integers.",
    )
    lcm_parser.add_argument("a", type=int)
    lcm_parser.add_argument("b", type=int)

    prime_parser = subparsers.add_parser(
        "is-prime",
        help="Determine whether an integer is prime.",
    )
    prime_parser.add_argument("n", type=int)

    mean_parser = subparsers.add_parser(
        "mean",
        help="Compute the arithmetic mean of one or more numbers.",
    )
    mean_parser.add_argument("values", nargs="+", type=float)

    median_parser = subparsers.add_parser(
        "median",
        help="Compute the median of one or more numbers.",
    )
    median_parser.add_argument("values", nargs="+", type=float)

    variance_parser = subparsers.add_parser(
        "variance",
        help="Compute the population variance of one or more numbers.",
    )
    variance_parser.add_argument("values", nargs="+", type=float)

    subparsers.add_parser(
        "history",
        help="Print the calculations recorded in this session.",
    )

    subparsers.add_parser(
        "clear-history",
        help="Discard every calculation recorded in this session.",
    )

    subparsers.add_parser(
        "demo",
        help="Run a fixed sequence of operations that exercises the four layers.",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the ``math-toolkit-jala`` console script."""
    parser = _build_parser()
    args = parser.parse_args(argv)
    ctx = _build_context()
    handler = _HANDLERS[args.command]
    try:
        output = handler(args, ctx)
    except MathUtilsError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
