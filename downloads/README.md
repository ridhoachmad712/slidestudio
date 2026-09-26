# Paket ChatGPT

**[Unduh SlideStudio untuk ChatGPT](slidestudio-chatgpt.zip)** lalu ekstrak.

Pilih satu paket berdasarkan contoh yang paling membantu menjelaskan kebutuhan Anda. Instruksi inti sama; contoh, brief, dan sumber mengikuti bidangnya.

| Paket | Contoh dan pendekatan |
|---|---|
| [Marketing](slidestudio-chatgpt.zip) | 16 slide, teori dan keputusan bisnis, desain editorial |
| [Komunikasi kelompok](slidestudio-chatgpt-social.zip) | 8 slide, konsep dan pembahasan dialog |
| [Statika](slidestudio-chatgpt-statics.zip) | 8 slide, diagram editable, langkah hitung, grafik |
| [Metodologi penelitian](slidestudio-chatgpt-methods.zip) | 8 slide, rancangan dan kritik kesimpulan |

| File | Penggunaan |
|---|---|
| `MULAI-DI-SINI.txt` | Langkah penggunaan dan prompt siap pakai |
| `SLIDESTUDIO-INSTRUCTIONS.txt` | Satu panduan gabungan, unggah ke ChatGPT |
| `BRIEF-KULIAH.txt` | Isi dan unggah, atau jelaskan kebutuhan lewat chat |
| `contoh-marketing.pptx` | Acuan visual dan kedalaman; bukan materi untuk semua topik |
| `sumber-contoh-marketing.txt` | Sumber dan asumsi contoh |
| `LICENSE.txt` | Lisensi paket |
| `BRIEF-CONTOH.txt` | Kebutuhan yang digunakan untuk membuat contoh |
| `CONTOH-REVISI.txt` | Permintaan revisi yang dapat disesuaikan |
| `KEDALAMAN-DAN-REVISI.txt` | Pilihan fungsi, kedalaman, dan perubahan isi |
| `PERTEMUAN-PERTAMA.txt` | Panduan percobaan pertama, prompt, pemeriksaan, dan revisi |
| `contoh-marketing.pdf` | Acuan tampilan yang diekspor dari PPTX contoh |

Setiap paket berisi 11 file. Nama contoh PPTX, PDF, dan sumber menyesuaikan paket. Baca langkah pada `MULAI-DI-SINI.txt`; unggah instruksi, contoh, brief Anda, dan sumber. Dokumen tambahan dipakai sesuai kebutuhan. Jangan menganggap brief contoh cocok untuk semua kelas. PPTX contoh memakai font yang disebut pada brief; font tidak disertakan. PDF merupakan salinan slide, tanpa notes dosen. [Panduan pertemuan pertama](../docs/FIRST_LECTURE.md).

Tambahkan materi kuliah Anda sendiri. Tidak perlu mengunggah seluruh repositori atau script. Paket menggunakan format TXT untuk memudahkan pembacaan instruksi; kemampuan menghasilkan file tetap bergantung pada alat yang tersedia di ChatGPT.

Paket dibangun dari skill dan contoh yang dipelihara di repositori. Setelah mengubah keduanya, pengelola menjalankan:

```sh
python scripts/build_chatgpt_pack.py
```

Perintah tersebut membangun keempat paket. Untuk satu bidang, tambahkan `--example statics` (pilihan lain: `marketing`, `social`, `methods`). [Catatan kompatibilitas](../docs/COMPATIBILITY.md) membedakan pemeriksaan lokal dari penggunaan yang belum diuji.

Untuk agen proyek, gunakan [repositori lengkap](../docs/GETTING_STARTED.md#untuk-agen-proyek).
