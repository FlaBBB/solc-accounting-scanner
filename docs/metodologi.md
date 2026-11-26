# Panduan Metodologi

Ringkasan keputusan metodologis yang menjadi dasar perancangan scanner. Rujukan
lengkap ada pada Bab III naskah skripsi.

## 1. Definisi sub-kelas

Kelas "kesalahan akuntansi keuangan" tidak dapat dipakai langsung sebagai label
pelatihan karena terlalu luas. Kelas ini dipecah menjadi tiga sub-kelas yang
masing-masing punya definisi operasional dan indikator AST.

| Sub-kelas | Definisi | Indikator AST |
| --- | --- | --- |
| `rounding` | Pembagian pada jalur penyerahan aset/porsi dibulatkan ke arah yang menguntungkan pengguna | `BinaryOperation` operator `/`, diperiksa terhadap `mulDiv` dan arah pembulatan |
| `fee` | Biaya dihitung setelah *state* berubah, atau rumus tidak konsisten antar fungsi | Urutan `Assignment` vs `FunctionCall` tipe transfer |
| `share` | Rasio porsi dihitung terhadap nilai yang dapat dipengaruhi pihak luar | Pembagian dengan operand variabel *state* yang dapat diubah publik |

Urutan ini penting: **definisi disusun sebelum label diberikan**. Apabila label
diberikan lebih dahulu, definisi cenderung dibentuk agar sesuai label yang sudah
ada dan validitas pengukuran menjadi dipertanyakan.

## 2. Mesin aturan sebelum model

Mesin aturan deterministik dijalankan lebih dahulu karena:

1. Keluarannya dapat diuji ulang oleh pihak lain.
2. Setiap temuan dapat ditelusuri ke aturan yang menyala.
3. Tidak memerlukan data latih.

Pengklasifikasi hanya dipakai untuk kandidat yang tidak dapat diputuskan secara
struktural.

## 3. Pembatasan algoritma

Algoritma dibatasi pada SVM, Random Forest, dan Logistic Regression. Alasannya
bukan keterbatasan teknis, melainkan jumlah data: korpus memuat 1.021 judul
temuan. Melatih model *deep learning* pada ukuran itu berisiko menghasilkan model
yang menghafal data latih dan tidak dapat dipertanggungjawabkan.

## 4. Pencegahan kebocoran data

Pembagian data latih/uji 80:20 dilakukan **pada tingkat repositori**, bukan pada
tingkat fungsi atau berkas. Tanpa ini, fungsi-fungsi dari kontrak yang sama dapat
muncul pada data latih dan data uji sekaligus, sehingga kinerja yang dilaporkan
menjadi terlalu tinggi secara palsu.

## 5. Baseline ganda

Dua pembanding dipakai:

1. **Slither** — dipetakan ke daftar sub-kelas, dihitung dengan metrik yang sama.
2. **Pengklasifikasi berbasis judul** — memakai judul temuan saja, tanpa analisis
   kode.

Pembanding kedua penting untuk menunjukkan bahwa tambahan kinerja benar-benar
berasal dari analisis AST, bukan dari teks semata.

## 6. Metrik

$$
\text{Presisi} = \frac{TP}{TP + FP}, \qquad
\text{Recall} = \frac{TP}{TP + FN}, \qquad
F_1 = \frac{2 \cdot \text{Presisi} \cdot \text{Recall}}{\text{Presisi} + \text{Recall}}
$$

Metrik dilaporkan **per sub-kelas**, bukan hanya agregat. Angka agregat akan
menyembunyikan fakta bahwa Slither memiliki detektor untuk sebagian kelas dan
tidak memiliki detektor untuk kelas lainnya.
