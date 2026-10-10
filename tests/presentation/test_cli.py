"""Integration tests for the math_toolkit_jala command-line interface."""

from __future__ import annotations

import pytest

from math_toolkit_jala.presentation.cli import (
    CommandContext,
    _build_context,
    main,
)


class TestSuccessfulInvocations:
    @pytest.mark.parametrize(
        ("argv", "expected"),
        [
            (["factorial", "5"], "120"),
            (["gcd", "12", "18"], "6"),
            (["lcm", "4", "6"], "12"),
            (["is-prime", "97"], "true"),
            (["is-prime", "100"], "false"),
            (["mean", "1", "2", "3", "4", "5"], "3.0"),
            (["median", "1", "2", "3", "4"], "2.5"),
            (["variance", "1", "2", "3", "4", "5"], "2.0"),
        ],
    )
    def test_returns_zero_and_prints_result(
        self,
        argv: list[str],
        expected: str,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        exit_code = main(argv)
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == expected


class TestErrorHandling:
    def test_domain_error_is_reported_with_non_zero_exit_code(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        exit_code = main(["factorial", "-1"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert captured.out == ""
        assert "error:" in captured.err


class TestVersionFlag:
    def test_version_flag_exits_successfully(self, capsys: pytest.CaptureFixture[str]) -> None:
        with pytest.raises(SystemExit) as exc_info:
            main(["--version"])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "math-toolkit-jala" in captured.out


class TestHistoryCommand:
    def test_reports_empty_history(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["history"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "no calculations recorded" in captured.out


class TestClearHistoryCommand:
    def test_reports_confirmation(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["clear-history"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "history cleared"


class TestDemoCommand:
    def test_runs_every_operation_and_prints_history(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        exit_code = main(["demo"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "Demonstration of Clean Architecture layers" in captured.out
        assert "factorial(5) = 120" in captured.out
        assert "gcd(12, 18) = 6" in captured.out
        assert "is_prime(97) = True" in captured.out
        assert "mean(1.0, 2.0, 3.0, 4.0, 5.0) = 3.0" in captured.out


class TestHistoryWithEntries:
    """Exercise the history and clear-history commands with a shared context.

    Because ``main`` builds a fresh context on every call by default, we
    inject a shared context to make the history survive between
    invocations of the CLI.
    """

    def _make_shared_context(self) -> CommandContext:
        return _build_context()

    def test_history_lists_recorded_calculations(self, capsys: pytest.CaptureFixture[str]) -> None:
        ctx = self._make_shared_context()
        assert main(["factorial", "5"], ctx=ctx) == 0
        assert main(["gcd", "12", "18"], ctx=ctx) == 0
        capsys.readouterr()  # discard the output of the two operations
        exit_code = main(["history"], ctx=ctx)
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "factorial(5) = 120" in captured.out
        assert "gcd(12, 18) = 6" in captured.out

    def test_clear_history_empties_the_shared_context(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        ctx = self._make_shared_context()
        main(["factorial", "5"], ctx=ctx)
        capsys.readouterr()
        assert main(["clear-history"], ctx=ctx) == 0
        capsys.readouterr()
        main(["history"], ctx=ctx)
        captured = capsys.readouterr()
        assert "no calculations recorded" in captured.out
