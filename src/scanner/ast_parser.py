"""Pembentukan AST dari berkas Solidity.

Modul ini membungkus `solc --ast-compact-json` sehingga berkas `.sol` tunggal
maupun direktori proyek dapat diubah menjadi pohon AST yang siap ditelusuri.

Alasan memakai keluaran AST dan bukan teks: AST mencerminkan struktur sintaksis
program sehingga analisis tidak terpengaruh oleh perbedaan format penulisan,
komentar, atau penamaan variabel.

Status: kerangka. Implementasi menyusul pada tahap 3.5 naskah.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


class SolcNotFound(RuntimeError):
    """Dilempar bila executable `solc` tidak tersedia pada PATH."""


class CompilationError(RuntimeError):
    """Dilempar bila `solc` gagal menghasilkan AST."""


@dataclass
class AstResult:
    """Hasil pembentukan AST untuk satu berkas sumber."""

    source: Path
    ast: dict[str, Any] = field(default_factory=dict)
    solc_version: str = ""

    @property
    def ok(self) -> bool:
        return bool(self.ast)


def solc_available() -> bool:
    """True bila `solc` dapat ditemukan pada PATH."""
    return shutil.which("solc") is not None


def solc_version() -> str:
    """Kembalikan versi `solc` yang terpasang."""
    if not solc_available():
        raise SolcNotFound("executable `solc` tidak ditemukan pada PATH")
    out = subprocess.run(
        ["solc", "--version"], capture_output=True, text=True, check=False
    ).stdout
    for line in out.splitlines():
        if line.lower().startswith("version:"):
            return line.split(":", 1)[1].strip()
    return ""


def parse_file(path: str | Path) -> AstResult:
    """Bentuk AST untuk satu berkas `.sol`.

    Belum diimplementasikan. Rencana pemanggilan:

        solc --ast-compact-json <berkas>

    Keluaran berupa teks yang perlu dipangkas pada blok JSON sebelum di-*parse*.
    """
    raise NotImplementedError("implementasi menyusul pada tahap ekstraksi AST")


__all__ = [
    "AstResult",
    "CompilationError",
    "SolcNotFound",
    "parse_file",
    "solc_available",
    "solc_version",
]
