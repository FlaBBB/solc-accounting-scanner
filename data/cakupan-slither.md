# Analisis Hasil Slither pada Repo Korpus

Dihasilkan oleh `scripts/analyze_slither.py` dari 3 batch eksekusi. **32 repo berhasil dianalisis** dari 187 repo unik yang dicoba. 44 berkas JSON hasil terbaca.

## 1. Tingkat keberhasilan

| Status | Repo | Pangsa |
| --- | ---: | ---: |
| Berhasil dianalisis | 32 | 17% |
| Repo tidak dapat di-clone (dihapus/privat) | 109 | 58% |
| Gagal kompilasi / dependency hilang | 46 | 25% |
| **Total dicoba** | **187** | 100% |

**Temuan penting:** mayoritas kegagalan bukan karena alat, melainkan karena **repo kontrak sudah tidak tersedia publik**. Ini keterbatasan struktural dataset berbasis laporan audit: kode yang diaudit sering dihapus atau diprivatkan setelah audit selesai, sehingga evaluasi tidak dapat direproduksi sepenuhnya.

## 2. Repo yang berhasil

| Laporan | Temuan produksi |
| --- | ---: |
| 2023-10-DopexV2-CLAMM | 2067 |
| Spectra-security-review | 1166 |
| Hyperlend-security-review_2025-01-11 | 959 |
| Interpol-security-review_2024-12-24 | 869 |
| 2025-04-Sickle | 820 |
| Bunni-security-review-August | 692 |
| Dyad-security-review | 570 |
| Ambire-second-security-review | 466 |
| Level-security-review_2025-04-09 | 448 |
| Tanssi-security-review_2025-04-30 | 445 |
| Bunni-security-review-October | 403 |
| Burve-security-review_2025-01-29 | 341 |
| BearCave-second-security-review | 282 |
| IonProtocol-security-review-July | 222 |
| Bloom-security-review | 197 |
| HYTOPIAWallet-security-review | 179 |
| Brrito-security-review | 155 |
| Arcadia-security-review | 137 |
| OpenDollar-security-review | 120 |
| Arcana-security-review | 86 |
| Metalabel-security-review | 76 |
| 2024-01-Inverse-sDOLA-yAudit-Report | 73 |
| IonProtocol-security-review | 65 |
| 2023-12-Euler-EVC | 64 |
| IPNFT-security-review | 54 |
| Cryptex-security-review | 46 |
| Zerem-security-review | 32 |
| MoleculeVesting-security-review | 29 |
| RollingDutchAuction-security-review | 27 |
| Overload-security-review | 22 |
| YuzuUSD-security-review_2026-01-14 | 13 |
| 2024-03-Cove-yAudit-Report | 13 |

## 3. Detector yang paling sering menyala

| Detector | Temuan | Kelas |
| --- | ---: | --- |
| naming-convention | 2553 | — |
| assembly | 1918 | — |
| calls-loop | 887 | dos |
| unused-return | 770 | input-validation |
| too-many-digits | 654 | — |
| reentrancy-events | 472 | reentrancy |
| divide-before-multiply | 448 | arithmetic-rounding |
| unindexed-event-address | 279 | — |
| timestamp | 259 | timelock-timing |
| reentrancy-no-eth | 236 | reentrancy |
| missing-zero-check | 218 | input-validation |
| dead-code | 209 | — |
| uninitialized-local | 186 | input-validation |
| reentrancy-benign | 177 | reentrancy |
| low-level-calls | 160 | — |
| solc-version | 146 | — |
| unused-state | 101 | — |
| constable-states | 98 | upgradeability |
| shadowing-local | 81 | — |
| incorrect-equality | 80 | input-validation |

**Kebisingan:** 6095 dari 10663 temuan (57%) berasal dari detector gaya penulisan / informasi (naming-convention, assembly, too-many-digits, dll), bukan kerentanan.

## 4. Temuan Slither yang dapat dipetakan ke kelas skripsi

| Kelas | Temuan Slither |
| --- | ---: |
| input-validation | 1260 |
| dos | 988 |
| reentrancy | 970 |
| arithmetic-rounding | 485 |
| timelock-timing | 259 |
| upgradeability | 116 |
| token-integration | 84 |
| access-control | 13 |
| **Total terpetakan** | **4175** |

Dari 10663 temuan produksi, hanya 4175 (39%) yang dapat dipetakan ke taksonomi skripsi. Sisanya tidak punya padanan kelas.

## 5. Kelas yang dilaporkan auditor vs yang terdeteksi Slither

Untuk tiap repo yang berhasil, dibandingkan kelas yang dilaporkan auditor dengan ada/tidaknya detector Slither yang menyala untuk kelas itu.

| Laporan | Kelas auditor | Kelas terdeteksi Slither |
| --- | --- | --- |
| Ambire-second-security-review | signature-auth | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration |
| Arcana-security-review | access-control | arithmetic-rounding, input-validation |
| BearCave-second-security-review | access-control | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing |
| Bloom-security-review | token-integration | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing |
| IPNFT-security-review | token-integration | dos, input-validation, reentrancy, timelock-timing, upgradeability |
| RollingDutchAuction-security-review | arithmetic-rounding, token-integration | input-validation, reentrancy, timelock-timing |
| Arcadia-security-review | accounting, liquidation | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing |
| Brrito-security-review | price-manipulation | arithmetic-rounding, dos, input-validation, reentrancy |
| Bunni-security-review-August | dos, price-manipulation, timelock-timing | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration |
| Dyad-security-review | accounting, liquidation | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration, upgradeability |
| HYTOPIAWallet-security-review | price-manipulation | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing |
| Hyperlend-security-review_2025-01-11 | arithmetic-rounding | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration, upgradeability |
| Interpol-security-review_2024-12-24 | dos | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration, upgradeability |
| Spectra-security-review | price-manipulation | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing |
| YuzuUSD-security-review_2026-01-14 | dos | input-validation, reentrancy |
| Bunni-security-review-October | dos | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, upgradeability |
| Cryptex-security-review | access-control | arithmetic-rounding, input-validation, reentrancy, timelock-timing |
| IonProtocol-security-review | dos | input-validation, reentrancy, token-integration |
| IonProtocol-security-review-July | input-validation | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration |
| Metalabel-security-review | timelock-timing | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing |
| MoleculeVesting-security-review | input-validation | dos, input-validation, timelock-timing |
| OpenDollar-security-review | dos | arithmetic-rounding, dos, input-validation, timelock-timing, token-integration |
| Overload-security-review | token-integration | input-validation, reentrancy |
| Zerem-security-review | dos | access-control, dos, input-validation, reentrancy, timelock-timing, token-integration |
| 2023-10-DopexV2-CLAMM | token-integration | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration, upgradeability |
| 2023-12-Euler-EVC | none | access-control, dos, input-validation, reentrancy, timelock-timing |
| 2024-01-Inverse-sDOLA-yAudit-Report | none | arithmetic-rounding, input-validation, reentrancy, timelock-timing, token-integration |
| 2024-03-Cove-yAudit-Report | dos | input-validation, timelock-timing |
| Burve-security-review_2025-01-29 | dos, token-integration | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, upgradeability |
| 2025-04-Sickle | dos | arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing |
| Level-security-review_2025-04-09 | input-validation | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, token-integration, upgradeability |
| Tanssi-security-review_2025-04-30 | oracle | access-control, arithmetic-rounding, dos, input-validation, reentrancy, timelock-timing, upgradeability |

## 6. Kelas yang auditor laporkan tetapi Slither tidak punya detector

| Kelas | Laporan (di subset ini) | Ada detector Slither? |
| --- | ---: | --- |
| dos | 10 | ya (sebagian) |
| token-integration | 6 | ya (sebagian) |
| price-manipulation | 4 | tidak |
| access-control | 3 | ya (sebagian) |
| input-validation | 3 | ya (sebagian) |
| arithmetic-rounding | 2 | tidak |
| liquidation | 2 | tidak |
| accounting | 2 | tidak |
| timelock-timing | 2 | tidak |
| none | 2 | ya (sebagian) |
| signature-auth | 1 | ya (sebagian) |
| oracle | 1 | ya (sebagian) |

## 7. Keterbatasan

- N = 32 repo berhasil dianalisis. Cukup untuk indikasi, belum untuk klaim statistik kuat.
- Pemetaan detector→kelas dilakukan manual dan bisa diperdebatkan; beberapa detector melintasi beberapa kelas.
- Slither menemukan *pola*, bukan *bug*. Detector yang menyala tidak berarti auditor akan melaporkan hal yang sama, dan sebaliknya.
- Banyak temuan berasal dari kode library/vendor yang bukan bagian audit.
- 109 repo gagal di-clone karena sudah tidak publik; ini bias seleksi yang tidak bisa dihindari.

