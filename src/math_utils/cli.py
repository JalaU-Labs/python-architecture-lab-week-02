"""Command-line interface for the math_utils package."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable, Sequence

from math_utils import __version__
from math_utils.core.arithmetic import factorial, gcd, is_prime, lcm
from math_utils.core.statistics import mean, median, variance
from math_utils.exceptions import MathUtilsError

Handler = Callable[[argparse.Namespace], str]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="math-toolkit-jala",
        description="Mathematical utilities from the math_utils package.",
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
    factorial_parser.set_defaults(func=lambda args: str(factorial(args.n)))

    gcd_parser = subparsers.add_parser(
        "gcd",
        help="Compute the greatest common divisor of two integers.",
    )
    gcd_parser.add_argument("a", type=int)
    gcd_parser.add_argument("b", type=int)
    gcd_parser.set_defaults(func=lambda args: str(gcd(args.a, args.b)))

    lcm_parser = subparsers.add_parser(
        "lcm",
        help="Compute the least common multiple of two integers.",
    )
    lcm_parser.add_argument("a", type=int)
    lcm_parser.add_argument("b", type=int)
    lcm_parser.set_defaults(func=lambda args: str(lcm(args.a, args.b)))

    prime_parser = subparsers.add_parser(
        "is-prime",
        help="Determine whether an integer is prime.",
    )
    prime_parser.add_argument("n", type=int)
    prime_parser.set_defaults(func=lambda args: "true" if is_prime(args.n) else "false")

    mean_parser = subparsers.add_parser(
        "mean",
        help="Compute the arithmetic mean of one or more numbers.",
    )
    mean_parser.add_argument("values", nargs="+", type=float)
    mean_parser.set_defaults(func=lambda args: repr(mean(args.values)))

    median_parser = subparsers.add_parser(
        "median",
        help="Compute the median of one or more numbers.",
    )
    median_parser.add_argument("values", nargs="+", type=float)
    median_parser.set_defaults(func=lambda args: repr(median(args.values)))

    variance_parser = subparsers.add_parser(
        "variance",
        help="Compute the population variance of one or more numbers.",
    )
    variance_parser.add_argument("values", nargs="+", type=float)
    variance_parser.set_defaults(func=lambda args: repr(variance(args.values)))

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the ``math-toolkit-jala`` console script.

    Returns:
        ``0`` on success, ``1`` when a domain error is raised.
    """
    parser = _build_parser()
    args = parser.parse_args(argv)
    handler: Handler = args.func
    try:
        output = handler(args)
    except MathUtilsError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
