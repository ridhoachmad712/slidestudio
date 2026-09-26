# Berkontribusi

Kontribusi dapat berupa skill, template, contoh kuliah, dokumentasi, atau laporan masalah. Untuk perubahan besar, jelaskan kebutuhan dan dampaknya terlebih dahulu.

1. Buat perubahan pada salinan atau cabang.
2. Jelaskan masalah, hasil perubahan, dan cara pemeriksaan dalam pull request.
3. Sertakan sumber akademik dan label kasus/data hipotetis.
4. Untuk deck, sertakan brief, sumber/asumsi, PPTX editable, dan pratinjau. PDF opsional mengikuti isi final yang sama.
5. Render dan periksa seluruh slide, sumber, perhitungan, serta notes. Jalankan pemeriksa struktur yang relevan.

```sh
python scripts/check_pptx.py examples/marketing/manajemen-pemasaran.pptx --slides 16 --require-notes
```

Jangan sertakan font berlisensi, logo tanpa izin, data mahasiswa, bahan terbatas, rahasia, atau path lokal pribadi. Pastikan hak distribusi materi tambahan.

Pertahankan penyesuaian terhadap dosen. Gaya satu contoh tidak menjadi kewajiban semua mata kuliah. Hindari runtime privat. Sebutkan pemeriksaan yang tidak tersedia dan jangan mengklaim pengecekan dalam aplikasi yang tidak digunakan.
