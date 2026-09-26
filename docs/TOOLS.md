# Ekspor dan pemeriksaan

## PDF

Buka PPTX final di PowerPoint dan ekspor sebagai PDF. Periksa hasil karena substitusi font/aplikasi dapat mengubah layout. PDF tidak membawa notes presenter, animasi, atau editabilitas objek PowerPoint.

Jika LibreOffice tersedia, script opsional memakai Python 3.10+ dan pustaka standar:

```sh
python scripts/export_pdf.py outputs/kuliah.pptx --out-dir outputs
```

Tambahkan `--soffice /path/to/soffice` untuk executable eksplisit. Script tidak memasang aplikasi dan menolak menimpa PDF. Parameter mengikuti [dokumentasi LibreOffice](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html).

PDF Marketing, komunikasi kelompok, statika, dan metode penelitian telah diekspor langsung dari PPTX final memakai PowerPoint 16.0 pada Windows. Seluruh halaman diperiksa dan teksnya dapat dipilih. PDF Mean dan median berasal dari model layout yang sama dengan PPTX. Script LibreOffice belum diuji end-to-end. [Status dan batas pemeriksaan](COMPATIBILITY.md).

## Pemeriksaan PPTX

```sh
python scripts/check_pptx.py outputs/kuliah.pptx --slides 20 --require-notes
```

Sesuaikan jumlah slide. Script memeriksa paket, urutan, teks/catatan, placeholder umum, grafik/tabel, dan objek tingkat atas di luar kanvas. Tidak mengukur overflow teks, mutu tulisan, ketepatan ilmiah, atau desain secara menyeluruh.

`--allow-placeholders` hanya untuk pustaka template. Render dan periksa tiap slide serta sumber, rumus, jawaban, dan cakupan tujuan. Pemeriksaan struktur dijalankan secara lokal dengan perintah di atas. Tidak ada workflow GitHub Actions bawaan. Hasil berhasil bukan sertifikasi akademik atau kompatibilitas semua aplikasi.
