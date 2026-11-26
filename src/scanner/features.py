"""Ekstraksi fitur per fungsi dari AST Solidity.

Fitur dihitung **per fungsi**, bukan per kontrak, karena satu kontrak dapat
memuat beberapa fungsi dengan karakteristik berbeda dan label berbeda pula.

Empat kelompok fitur (lihat Tabel 3.4 naskah):

1. Aritmatika   — jumlah operasi, keberadaan `mulDiv`, arah pembulatan
2. Kontrol akses — modifier, `msg.sender`, `tx.origin`, fungsi publik terbuka
3. Interaksi token — transfer/approve, SafeERC20, pemeriksaan kembalian
4. Tanda tangan & pola state — ecrecover, nonce, EIP-712, urutan assignment

Status: kerangka. Implementasi menyusul pada tahap 3.5 naskah.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Nama fitur dalam urutan tetap; menjadi urutan kolom matriks fitur.
FEATURE_NAMES: tuple[str, ...] = (
    # aritmatika
    "n_add", "n_sub", "n_mul", "n_div", "n_mod",
    "has_muldiv", "rounds_down", "rounds_up",
    "n_arith_on_return_path",
    # kontrol akses
    "has_modifier", "uses_msg_sender_cmp", "has_owner_check",
    "uses_tx_origin", "is_public_unrestricted",
    # interaksi token
    "n_transfer", "n_transfer_from", "n_approve",
    "uses_safe_erc20", "checks_return_value", "checks_zero_address",
    # tanda tangan & pola state
    "uses_ecrecover", "uses_nonce", "uses_eip712",
    "assignment_before_transfer", "reads_mutable_public_state",
)


@dataclass
class FunctionFeatures:
    """Vektor fitur untuk satu fungsi."""

    contract: str
    function: str
    values: dict[str, float] = field(default_factory=dict)

    def as_vector(self) -> list[float]:
        """Kembalikan nilai fitur sesuai urutan `FEATURE_NAMES`."""
        return [float(self.values.get(n, 0.0)) for n in FEATURE_NAMES]


def extract(ast: dict[str, Any]) -> list[FunctionFeatures]:
    """Telusuri AST dan hasilkan fitur untuk setiap fungsi.

    Belum diimplementasikan.
    """
    raise NotImplementedError("implementasi menyusul pada tahap ekstraksi fitur")


__all__ = ["FEATURE_NAMES", "FunctionFeatures", "extract"]
