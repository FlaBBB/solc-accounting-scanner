# Data

Folder ini hanya memuat **ringkasan** korpus dan hasil pengukuran. Data mentah
(repositori kontrak, PDF laporan, keluaran JSON Slither) tidak disimpan di
repositori ini karena ukurannya besar dan hak publikasinya milik pihak lain.

## Berkas

| Berkas | Isi |
| --- | --- |
| `korpus-ringkas.csv` | 138 laporan audit dengan repo terverifikasi, severity, dan label kelas |
| `cakupan-slither.md` | Hasil pengukuran Slither terhadap 32 repositori |

## Sumber korpus

Empat lembaga audit independen, laporan publik:

| Lembaga | Laporan | Temuan inti |
| --- | ---: | ---: |
| pashov | 63 | 419 |
| Zellic | 58 | 278 |
| OtterSec | 9 | 28 |
| yAudit | 8 | 56 |
| **Total** | **138** | **781** |

## Cara memperoleh ulang

Pipeline lengkap ada pada folder `scripts/` di workspace penelitian (tidak
disertakan di repositori ini). Ringkasnya:

1. Klon repositori laporan auditor (pashov, Zellic, OtterSec, yAudit).
2. Parse laporan menjadi TSV; saring bahasa selain Solidity.
3. Verifikasi setiap repositori kontrak dengan `git ls-remote`.
4. Jalankan Slither pada repositori yang masih tersedia.
5. Petakan detektor Slither ke taksonomi kelas.

Catatan: 127 dari 250 repositori yang diperiksa (51%) sudah tidak tersedia
publik. Ini keterbatasan yang tidak dapat dihindari pada dataset berbasis laporan
audit, dan menjadi alasan mengapa hasil pengukuran tidak sepenuhnya dapat
direproduksi dari nol.
