"""System clock adapter."""

from __future__ import annotations

from datetime import UTC, datetime


class SystemClock:
    """Clock that reads the real system time in UTC.

    All datetimes returned are timezone-aware. This is a deliberate
    choice: naive datetimes are a common source of bugs, and the domain
    entity requires an unambiguous timestamp.
    """

    def now(self) -> datetime:
        return datetime.now(UTC)
