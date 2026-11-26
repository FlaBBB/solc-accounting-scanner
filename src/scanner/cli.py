"""Antarmuka baris perintah scanner.

Rencana keluaran::

    $ solc-scan scan Contoh.sol
    [HIGH]   rounding   Contoh.sol:142  withdraw()
             Pembagian dibulatkan ke bawah pada jalur penyerahan aset
             SARAN: gunakan Math.mulDiv(..., Rounding.Floor)

Status: kerangka. Implementasi menyusul setelah mesin aturan tersedia.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="solc-scan",
        description="Scanner kerentanan smart contract Solidity (deteksi kesalahan akuntansi keuangan)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="pindai berkas atau direktori Solidity")
    scan.add_argument("path", type=Path, help="berkas .sol atau direktori proyek")
    scan.add_argument(
        "--format", choices=["text", "json"], default="text", help="format keluaran"
    )
    scan.add_argument(
        "--min-severity",
        choices=["info", "low", "medium", "high"],
        default="low",
        help="ambang keparahan minimal yang dilaporkan",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "scan":
        if not args.path.exists():
            print(f"berkas tidak ditemukan: {args.path}", file=sys.stderr)
            return 2
        print(
            "Scanner belum diimplementasikan. "
            "Tahap mesin aturan dan ekstraksi AST masih dikerjakan.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
