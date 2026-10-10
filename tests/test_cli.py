"""Integration tests for the math_utils command-line interface."""

from __future__ import annotations

import pytest

from math_utils.cli import main


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
