# Scanner Kerentanan Smart Contract Solidity

Perangkat lunak untuk mendeteksi **kesalahan akuntansi keuangan** pada smart
contract Solidity berbasis analisis *Abstract Syntax Tree* (AST) dan
pembelajaran mesin.

Repositori ini merupakan luaran produk skripsi:

> **Pengembangan Scanner Kerentanan Smart Contract Solidity Berbasis Analisis AST
> dan Pembelajaran Mesin untuk Deteksi Kesalahan Akuntansi Keuangan**
>
> Fikri Muhammad Abdillah — NIM 2341720092
> D-IV Teknik Informatika, Jurusan Teknologi Informasi
> Politeknik Negeri Malang, 2026
> Pembimbing: Ade Ismail, S.Kom., M.T.

---

## Status

🚧 **Tahap perancangan.** Struktur proyek dan rencana arsitektur sudah disusun;
implementasi sedang berjalan bertahap sesuai Bab III naskah skripsi.

| Komponen | Status |
| --- | --- |
| Parser AST (`solc --ast-compact-json`) | belum |
| Ekstraktor fitur per fungsi | belum |
| Mesin aturan (pembulatan, biaya, porsi) | belum |
| Pengklasifikasi (SVM / RF / LogReg) | belum |
| Bahan rekomendasi perbaikan | belum |
| Antarmuka CLI | belum |

---

## Masalah yang Disasar

Alat analisis statis yang ada mencocokkan **pola sintaksis**. Sebagian besar
temuan audit nyata berupa **kesalahan semantik** yang tidak memiliki bentuk
sintaksis, sehingga tidak dapat dideteksi dengan pencocokan pola.

Pengukuran awal pada 138 laporan audit dari empat lembaga independen
(pashov, Zellic, OtterSec, yAudit) dengan 32 repositori yang dianalisis
menggunakan Slither:

| Temuan | Jumlah |
| --- | ---: |
| Total temuan Slither pada kode produksi | 10.663 |
| Berasal dari detektor gaya penulisan (bukan kerentanan) | 6.095 (57%) |
| Dapat dipetakan ke taksonomi kerentanan | 4.175 (39%) |
| Temuan untuk kelas *accounting* | 0 |
| Temuan untuk kelas *price-manipulation* | 0 |

Angka tersebut menjadi dasar perancangan scanner ini.

---

## Cakupan

### Kelas yang dideteksi

Kelas "kesalahan akuntansi keuangan" dipecah menjadi tiga sub-kelas operasional
yang dapat dianalisis melalui AST:

| Sub-kelas | Definisi | Indikator AST |
| --- | --- | --- |
| Pembulatan | Operasi pembagian pada jalur penyerahan aset/porsi dibulatkan ke arah yang menguntungkan pengguna sehingga protokol kehilangan nilai | `BinaryOperation` dengan operator `/` pada fungsi yang mengembalikan nilai aset, diperiksa terhadap `mulDiv` dan arah pembulatan |
| Biaya | Rumus biaya tidak konsisten antar fungsi, atau biaya dihitung setelah *state* berubah | Urutan `Assignment` dan `FunctionCall` tipe transfer relatif terhadap pembacaan variabel biaya |
| Porsi | Rasio porsi dihitung terhadap nilai yang dapat berubah sehingga dapat dipengaruhi pihak luar | `BinaryOperation` pembagian dengan operand berupa variabel *state* yang dapat diubah melalui pemanggilan publik |

### Batasan

- Hanya Solidity. Rust (Solana), Move (Aptos/Sui), dan Cairo tidak termasuk.
- Analisis statis terhadap AST; tidak ada eksekusi kontrak atau pembuktian formal.
- Rekomendasi perbaikan bersifat *rule-based*, bukan generasi bebas model bahasa.

---

## Rencana Arsitektur

```
berkas .sol
    │
    ▼
[1] Parser AST          solc --ast-compact-json
    │
    ▼
[2] Ekstraktor fitur    telusuri AST → vektor fitur per fungsi
    │
    ▼
[3] Mesin aturan        aturan deterministik → kandidat temuan
    │
    ▼
[4] Pengklasifikasi     skor tambahan untuk kandidat ambigu
    │
    ▼
[5] Bahan perbaikan     pemetaan sub-kelas + konteks → potongan kode pengganti
    │
    ▼
daftar temuan: sub-kelas, keparahan, lokasi, penjelasan, saran perbaikan
```

Mesin aturan dijalankan **sebelum** model statistik karena keluarannya
deterministik dan dapat ditelusuri. Pengklasifikasi hanya dipakai untuk kandidat
yang tidak dapat diputuskan secara struktural.

### Fitur yang diekstraksi

| Kelompok | Rincian |
| --- | --- |
| Aritmatika | Jumlah operasi `+ - * / %`; keberadaan `mulDiv`; arah pembulatan; jumlah operasi pada jalur pengembalian aset |
| Kontrol akses | Keberadaan `modifier`; penggunaan `msg.sender` sebagai pembanding; pemeriksaan pemilik; `tx.origin`; fungsi publik tanpa pembatas |
| Interaksi token | Pemanggilan `transfer`, `transferFrom`, `approve`; penggunaan `SafeERC20`; pemeriksaan nilai kembalian; pemeriksaan `address(0)` |
| Tanda tangan dan pola *state* | `ecrecover`, `nonce`, `EIP-712`; urutan `Assignment` terhadap `FunctionCall`; pembacaan variabel *state* yang dapat diubah publik |

Fitur dihitung **per fungsi**, bukan per kontrak.

---

## Rancangan Pengujian

- Pembagian data latih/uji 80:20, **berlapis menurut sub-kelas**, dilakukan pada
  **tingkat repositori** untuk mencegah kebocoran data (*data leakage*).
- Metrik: presisi, *recall*, F1 — dilaporkan per sub-kelas dan secara agregat.
- Pembanding: Slither (dipetakan ke sub-kelas) dan pengklasifikasi berbasis judul
  temuan saja. Pembanding kedua membuktikan tambahan kinerja berasal dari
  analisis kode, bukan dari teks.

---

## Struktur Repositori

```
.
├── README.md
├── pyproject.toml
├── src/
│   └── scanner/
│       ├── ast_parser.py     # pembentukan AST dari berkas .sol
│       ├── features.py       # ekstraksi fitur per fungsi
│       ├── rules.py          # mesin aturan per sub-kelas
│       ├── classifier.py     # pengklasifikasi untuk kasus ambigu
│       ├── fixes.py          # bahan rekomendasi perbaikan
│       └── cli.py            # antarmuka baris perintah
├── tests/
├── data/                     # ringkasan korpus & hasil (bukan data mentah)
└── docs/                     # catatan metodologi
```

---

## Kebutuhan

- Python 3.11+
- `solc` (Solidity compiler) — mendukung `--ast-compact-json`
- Dependensi Python tercantum pada `pyproject.toml`

---

## Lisensi

Kode dirilis di bawah MIT. Data dan naskah skripsi tidak termasuk.

## Sitasi

```
Abdillah, F. M. (2026). Pengembangan Scanner Kerentanan Smart Contract
Solidity Berbasis Analisis AST dan Pembelajaran Mesin untuk Deteksi
Kesalahan Akuntansi Keuangan [Skripsi, Politeknik Negeri Malang].
```
