# Pertemuan 05 Perulangan Python

**Nama:** Arya Kusmana Anas
**NIM:** 2225250118  
**Kelas:** 3 B  

## Deskripsi

Repository ini berisi latihan dan Kuis 2 pada Pertemuan 05 mata kuliah Algoritma dan Pemrograman.

Materi yang dipelajari adalah perulangan menggunakan `for` dan `while` dalam Python, termasuk penggunaan `range`, validasi input, seleksi di dalam perulangan, akumulasi, pencacahan, tracing, dan debugging.

## Tujuan

Tujuan pembelajaran pada Pertemuan 05 adalah:

- Memahami konsep perulangan atau iterasi.
- Menggunakan `for` dengan `range`.
- Menggunakan `while` dengan kondisi berhenti.
- Menentukan nilai awal, kondisi, dan pembaruan variabel kontrol.
- Menggunakan seleksi `if` di dalam perulangan.
- Menggunakan akumulasi dan pencacahan.
- Melakukan pengujian dan debugging program di VS Code.
- Mengelola dan mengunggah hasil pekerjaan melalui GitHub.

## Cara Menjalankan
Pastikan Python sudah terpasang dan folder proyek sudah dibuka melalui VS Code.

### Menjalankan Latihan 1
python latihan/01_tabel_perkalian.py
### Menjalankan Latihan 2
python latihan/02_jumlah_bilangan.py
### Menjalankan Latihan 3
python latihan/03_validasi_input.py
### Menjalankan Latihan 4
python latihan/04_hitung_genap.py
### Menjalankan Kuis 2
python kuis/kuis2_deret_aritmetika.py

## Algoritma kuis
kuis/kuis2_deret_aritmetika.py

Langkah algoritma:

Masukkan suku pertama a.
Masukkan beda d.
Masukkan banyak suku n.
Validasi nilai n.
Jika n <= 0, program meminta input kembali.
Inisialisasi total = 0.
Gunakan for untuk melakukan perulangan sebanyak n kali.
Hitung nilai setiap suku dengan:
suku = a + i × d
Tambahkan setiap suku ke dalam total.
Tampilkan nomor suku dan nilai suku.
Setelah perulangan selesai, tampilkan jumlah seluruh suku.

## Hasil Pengujian
Kuis 2 - Test Case 1
Input	Nilai
a	2
d	3
n	5

Suku yang dihasilkan:

2, 5, 8, 11, 14

Jumlah:

40

Status: Berhasil

Kuis 2 - Test Case 2
Input	Nilai
a	10
d	-2
n	4

Suku yang dihasilkan:

10, 8, 6, 4

Jumlah:

28

Status: Berhasil

Kuis 2 - Test Case 3
Input	Nilai
a	1.5
d	0.5
n	3

Suku yang dihasilkan:

1.5, 2.0, 2.5

Jumlah:

6.0

Status: Berhasil

## Refleksi
Pada Pertemuan 05, saya mempelajari penggunaan perulangan for dan while dalam Python.

Saya memahami bahwa for dapat digunakan ketika jumlah iterasi sudah diketahui, sedangkan while digunakan ketika perulangan dikendalikan oleh suatu kondisi.

Saya juga mempelajari pentingnya menentukan nilai awal, kondisi, dan pembaruan variabel agar perulangan dapat berhenti dengan benar.

Kesalahan yang perlu diperhatikan dalam perulangan adalah kesalahan batas range, variabel kontrol yang tidak diperbarui sehingga menyebabkan infinite loop, serta kesalahan penempatan akumulator.

Melalui proses pengujian dan tracing, saya dapat mengetahui perubahan nilai variabel pada setiap iterasi dan memastikan hasil program sesuai dengan yang diharapkan.

## Kesimpulan
Pertemuan 05 memberikan pemahaman tentang penggunaan perulangan for dan while dalam menyelesaikan masalah secara iteratif.

Penggunaan perulangan dapat membuat kode lebih singkat, terstruktur, dan mudah dikembangkan dibandingkan menuliskan perintah yang sama secara berulang.

## Sumber
Bahan Ajar Algoritma dan Pemrograman Pertemuan 05, Program Studi S1 Pendidikan Matematika FKIP Untirta.
Python Documentation.
Visual Studio Code Documentation.
GitHub Documentation.