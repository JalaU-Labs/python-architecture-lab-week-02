"""Unit tests for the system clock adapter."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from math_toolkit_jala.infrastructure.clock import SystemClock


class TestSystemClock:
    def test_now_returns_timezone_aware_datetime(self) -> None:
        moment = SystemClock().now()
        assert moment.tzinfo is not None
        assert moment.tzinfo == UTC

    def test_now_is_close_to_the_real_time(self) -> None:
        before = datetime.now(UTC)
        moment = SystemClock().now()
        after = datetime.now(UTC)
        assert before - timedelta(seconds=1) <= moment <= after + timedelta(seconds=1)
