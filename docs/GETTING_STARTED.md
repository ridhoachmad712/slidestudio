# Mulai menggunakan

## Untuk dosen

**Jalur ChatGPT yang disarankan:** unduh [paket ChatGPT](../downloads/slidestudio-chatgpt.zip) dan ekstrak. Baca `MULAI-DI-SINI.txt`. Unggah `SLIDESTUDIO-INSTRUCTIONS.txt`, `contoh-marketing.pptx`, brief yang diisi, dan materi sumber Anda. Panduan sudah digabung; tidak perlu memilih dua file Markdown secara manual. Gunakan chat biasa atau Project yang mendukung file dan pembuatan presentasi. Paket memberi instruksi serta acuan, bukan menambahkan kemampuan alat. [Isi paket](../downloads/README.md).

Langkah di bawah merupakan alternatif memilih file dari repositori lengkap:

Tidak perlu menjalankan script. Gunakan agen yang mampu membaca materi dan membuat PPTX, atau edit template langsung di PowerPoint.

1. Unduh template bila ingin mengikuti tampilannya.
2. Siapkan `skills/lecture-slides/SKILL.md` **dan** `skills/lecture-slides/references/needs-alignment.md`. Keduanya perlu tersedia.
3. Isi `course/brief.md` atau jelaskan kebutuhan dengan bahasa biasa. Sertakan sumber dan contoh tampilan bila diperlukan.
4. Lampirkan file tersebut pada agen. Minta PPTX editable, catatan dosen, dan PDF bila dibutuhkan.
5. Periksa isi, sumber, dan jawaban latihan sebelum mengajar. Berikan koreksi spesifik.

Jika aplikasi hanya menghasilkan teks, kit tidak mengubahnya menjadi pembuat file. Lihat [contoh prompt](PROMPTS.md) dan [panduan kebutuhan](LECTURER_GUIDE.md).

## Untuk agen proyek

Gunakan salinan repositori sebagai folder proyek. Baca `AGENTS.md`, skill, brief, serta sumber yang diberikan.

> Baca AGENTS.md dan skills/lecture-slides/SKILL.md. Buat presentasi berdasarkan course/brief.md. Baca profil bila tersedia, nyatakan asumsi, dan hubungkan tujuan dengan penjelasan serta latihan. Simpan hasil di outputs/. Periksa seluruh slide setelah dirender dan laporkan format atau pemeriksaan yang belum tersedia.

Instruksi proyek tidak membutuhkan instalasi skill global. Sebutkan file secara eksplisit jika agen tidak membacanya otomatis. Untuk pemasangan skill terpisah, salin **seluruh folder** `skills/lecture-slides/`, termasuk referensinya, sesuai mekanisme agen Anda.

## Berkas kerja

| Lokasi | Isi |
|---|---|
| `course/brief.md` | Kebutuhan pertemuan |
| `course/lecturer-profile.md` | Preferensi berulang opsional |
| `course/coverage-map.md` | Peta tujuan dan pemeriksaan brief |
| `course/materials/` | Sumber pribadi, diabaikan Git |
| `work/` | Berkas sementara, diabaikan Git |
| `outputs/` | Hasil pribadi, diabaikan Git |

Contoh publik ada di `examples/`. Kit tidak bergantung pada jalur komputer pembuatnya.
