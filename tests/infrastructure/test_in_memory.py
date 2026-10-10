"""Unit tests for the in-memory calculation history repository."""

from __future__ import annotations

from datetime import UTC, datetime

from math_toolkit_jala.domain.entities import Calculation
from math_toolkit_jala.infrastructure.in_memory import InMemoryCalculationHistory


def _calculation(name: str) -> Calculation:
    return Calculation(
        operation=name,
        arguments=(1,),
        result=1,
        timestamp=datetime(2026, 10, 13, tzinfo=UTC),
    )


class TestInMemoryCalculationHistory:
    def test_starts_empty(self) -> None:
        assert InMemoryCalculationHistory().all() == ()

    def test_add_appends_in_insertion_order(self) -> None:
        repo = InMemoryCalculationHistory()
        repo.add(_calculation("first"))
        repo.add(_calculation("second"))
        assert [c.operation for c in repo.all()] == ["first", "second"]

    def test_all_returns_immutable_snapshot(self) -> None:
        repo = InMemoryCalculationHistory()
        repo.add(_calculation("only"))
        snapshot = repo.all()
        repo.add(_calculation("later"))
        assert len(snapshot) == 1

    def test_clear_removes_every_record(self) -> None:
        repo = InMemoryCalculationHistory()
        repo.add(_calculation("a"))
        repo.add(_calculation("b"))
        repo.clear()
        assert repo.all() == ()
