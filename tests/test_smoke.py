"""Uji dasar untuk paket scanner."""

from scanner import __version__
from scanner.rules import RULES, SubClass


def test_version_ada() -> None:
    assert __version__


def test_tiga_subkelas() -> None:
    assert {s.value for s in SubClass} == {"rounding", "fee", "share"}


def test_aturan_terdaftar() -> None:
    assert "RD-01" in RULES
    assert len(RULES) >= 3
