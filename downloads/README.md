# Paket ChatGPT

**[Unduh SlideStudio untuk ChatGPT](slidestudio-chatgpt.zip)** lalu ekstrak.

| File | Penggunaan |
|---|---|
| `MULAI-DI-SINI.txt` | Langkah penggunaan dan prompt siap pakai |
| `SLIDESTUDIO-INSTRUCTIONS.txt` | Satu panduan gabungan, unggah ke ChatGPT |
| `BRIEF-KULIAH.txt` | Isi dan unggah, atau jelaskan kebutuhan lewat chat |
| `contoh-marketing.pptx` | Acuan visual dan kedalaman; bukan materi untuk semua topik |
| `sumber-contoh-marketing.txt` | Sumber dan asumsi contoh |
| `LICENSE.txt` | Lisensi paket |

Tambahkan materi kuliah Anda sendiri. Tidak perlu mengunggah seluruh repositori atau script. Paket menggunakan format TXT untuk memudahkan pembacaan instruksi; kemampuan menghasilkan file tetap bergantung pada alat yang tersedia di ChatGPT.

Paket dibangun dari skill dan contoh yang dipelihara di repositori. Setelah mengubah keduanya, pengelola menjalankan:

```sh
python scripts/build_chatgpt_pack.py
```

Untuk agen proyek, gunakan [repositori lengkap](../docs/GETTING_STARTED.md#untuk-agen-proyek).
