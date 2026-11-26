"""Mesin aturan deterministik untuk sub-kelas akuntansi keuangan.

Mesin aturan dijalankan **sebelum** pengklasifikasi karena keluarannya
deterministik, dapat diuji ulang, dan dapat dijelaskan kepada pengguna.

Tiga sub-kelas yang disasar:

- ``rounding`` : arah pembulatan merugikan protokol pada jalur penyerahan aset
- ``fee``      : biaya dihitung setelah state berubah, atau rumus tidak konsisten
- ``share``    : rasio porsi dihitung terhadap nilai yang dapat dipengaruhi pihak luar

Status: kerangka. Implementasi menyusul pada tahap 3.6 naskah.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class SubClass(str, Enum):
    """Sub-kelas kerentanan akuntansi keuangan."""

    ROUNDING = "rounding"
    FEE = "fee"
    SHARE = "share"


class Severity(str, Enum):
    """Tingkat keparahan temuan."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


@dataclass
class Finding:
    """Satu temuan yang dihasilkan mesin aturan atau pengklasifikasi."""

    subclass: SubClass
    severity: Severity
    contract: str
    function: str
    file: str
    line: int
    rule_id: str
    message: str
    confidence: float = 1.0
    fix_hint: str = ""
    evidence: dict[str, object] = field(default_factory=dict)

    def as_dict(self) -> dict[str, object]:
        return {
            "subclass": self.subclass.value,
            "severity": self.severity.value,
            "contract": self.contract,
            "function": self.function,
            "file": self.file,
            "line": self.line,
            "rule_id": self.rule_id,
            "message": self.message,
            "confidence": self.confidence,
            "fix_hint": self.fix_hint,
            "evidence": self.evidence,
        }


# Aturan dicatat di sini agar dapat dirujuk pada naskah dan lampiran.
RULES: dict[str, str] = {
    "RD-01": "Pembagian pada fungsi yang mengembalikan aset, dibulatkan ke bawah",
    "RD-02": "Pembagian pada perhitungan porsi pengguna tanpa `mulDiv`",
    "FE-01": "Biaya dibaca setelah state biaya diperbarui",
    "FE-02": "Rumus biaya berbeda antar fungsi untuk peran yang sama",
    "SH-01": "Rasio porsi memakai total supply/saldo yang dapat diubah publik",
}


def run(features: list[object]) -> list[Finding]:
    """Terapkan seluruh aturan pada daftar fitur fungsi.

    Belum diimplementasikan.
    """
    raise NotImplementedError("implementasi menyusul pada tahap mesin aturan")


__all__ = ["Finding", "RULES", "Severity", "SubClass", "run"]
