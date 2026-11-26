"""Bahan rekomendasi perbaikan kode.

Saran perbaikan dihasilkan dari basis aturan yang memetakan sub-kelas dan
konteks kode ke pola perbaikan yang lazim dipakai pada laporan audit.

Pendekatan *rule-based* dipilih agar keluaran dapat direproduksi; generasi bebas
oleh model bahasa tidak dipakai karena hasilnya bervariasi antar pemanggilan dan
tidak dapat dipertanggungjawabkan dalam konteks penelitian.

Status: kerangka. Implementasi menyusul pada tahap 3.6 naskah.
"""

from __future__ import annotations

from dataclasses import dataclass

from .rules import SubClass


@dataclass
class FixSuggestion:
    """Saran perbaikan untuk satu temuan."""

    subclass: SubClass
    rule_id: str
    explanation: str
    before: str
    after: str


# Contoh pola perbaikan per aturan. Isi lengkap menyusul.
FIX_TEMPLATES: dict[str, FixSuggestion] = {
    "RD-01": FixSuggestion(
        subclass=SubClass.ROUNDING,
        rule_id="RD-01",
        explanation=(
            "Pembulatan ke bawah pada nilai yang diserahkan kepada pengguna "
            "menguntungkan pengguna secara akumulatif. Bulatkan ke arah yang "
            "menguntungkan protokol, dan gunakan operasi `mulDiv` agar presisi "
            "tidak hilang sebelum pembulatan."
        ),
        before="uint256 shares = amount / price;",
        after="uint256 shares = Math.mulDiv(amount, 1e18, price, Math.Rounding.Floor);",
    ),
    "FE-01": FixSuggestion(
        subclass=SubClass.FEE,
        rule_id="FE-01",
        explanation=(
            "Biaya dibaca setelah state diperbarui, sehingga nilai acuan sudah "
            "berubah. Hitung dan simpan biaya sebelum mengubah state."
        ),
        before="feeBps = newFeeBps;\\nuint256 fee = amount * feeBps / 10_000;",
        after="uint256 fee = amount * feeBps / 10_000;\\nfeeBps = newFeeBps;",
    ),
    "SH-01": FixSuggestion(
        subclass=SubClass.SHARE,
        rule_id="SH-01",
        explanation=(
            "Rasio porsi dihitung terhadap nilai yang dapat dipengaruhi pihak "
            "luar. Gunakan nilai yang disimpan sebelum interaksi eksternal, atau "
            "kunci mekanisme penyumbangan yang dapat mengubah nilai tersebut."
        ),
        before="uint256 shares = amount * totalSupply / totalAssets;",
        after=(
            "uint256 cachedTotalAssets = totalAssets; // dibaca sebelum interaksi eksternal\\n"
            "uint256 shares = Math.mulDiv(amount, totalSupply, cachedTotalAssets);"
        ),
    ),
}


def suggest(rule_id: str) -> FixSuggestion | None:
    """Kembalikan saran perbaikan untuk kode aturan tertentu."""
    return FIX_TEMPLATES.get(rule_id)


__all__ = ["FIX_TEMPLATES", "FixSuggestion", "suggest"]
