"""Build the ChatGPT distribution from maintained skill and example files (stdlib only)."""
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def build():
    skill = (ROOT / 'skills/lecture-slides/SKILL.md').read_text(encoding='utf-8-sig')
    body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', skill, count=1, flags=re.S)
    body = body.replace('[needs alignment](references/needs-alignment.md)', 'the needs-alignment section included below')
    alignment = (ROOT / 'skills/lecture-slides/references/needs-alignment.md').read_text(encoding='utf-8-sig')
    instructions = '''# SlideStudio — instruksi untuk ChatGPT

Gunakan isi file ini sebagai panduan pembuatan presentasi ketika diminta pengguna. Kebutuhan pertemuan pengguna mengambil prioritas atas default panduan. Contoh PPTX adalah acuan desain/struktur, bukan sumber fakta untuk mata kuliah lain.

File ini menggabungkan skill dan panduan kebutuhan. Tidak perlu membaca file skill terpisah. Jalur seperti course/, templates/, dan docs/ merujuk repositori lengkap; dalam paket ChatGPT gunakan brief dan contoh yang dilampirkan. Jika template institusi tersedia, prioritaskan sesuai permintaan pengguna. Jika tidak ada alat pembuat PPTX/PDF atau render, sampaikan keterbatasannya dan jangan mengklaim file selesai. Jangan menganggap file yang disebut namun belum dilampirkan telah dibaca.

''' + body + '\n\n' + alignment
    brief = '''BRIEF PERTEMUAN — SLIDESTUDIO

Isi yang diketahui. Boleh diganti dengan penjelasan bebas dalam chat.

Mata kuliah dan topik:
Jenjang/semester dan pengetahuan awal mahasiswa:
Tujuan pembelajaran:
Cakupan wajib dan bagian yang tidak dibahas:
Durasi dan jumlah slide total:
Fungsi slide: pendamping ceramah / belajar mandiri / gabungan
Kedalaman penjelasan dan pendekatan mengajar:
Sumber yang dilampirkan:
Pengembangan: setia pada sumber / terbatas / dengan riset
Contoh dan latihan yang dibutuhkan:
Desain: contoh Marketing / template institusi / pilihan lain
Hal yang disukai atau tidak disukai dari contoh:
Keluaran: PPTX editable / PDF / keduanya
Contoh tiga slide dahulu: ya / tidak / bila perlu
Preferensi yang hanya berlaku pada pertemuan ini:

Jika belum jelas, agen merangkum asumsi dan hanya menanyakan informasi yang memengaruhi hasil.
'''
    guide = '''SLIDESTUDIO — PAKET CHATGPT

1. Ekstrak ZIP ini. Tidak perlu mengunggah ZIP atau seluruh repositori.
2. Unggah SLIDESTUDIO-INSTRUCTIONS.txt dan contoh-marketing.pptx ke chat atau Project. Isi BRIEF-KULIAH.txt lalu unggah, atau jelaskan kebutuhan dalam pesan.
3. Unggah RPS, catatan, atau bacaan Anda. Sumber-contoh-marketing.txt menjelaskan contoh, bukan menggantikan sumber mata kuliah Anda.
4. Kirim prompt di bawah. Tinjau file, sumber, dan jawaban latihan sebelum digunakan.

PROMPT SIAP PAKAI

Ikuti SLIDESTUDIO-INSTRUCTIONS.txt yang saya unggah. Gunakan brief dan sumber saya untuk membuat presentasi kuliah. Contoh Marketing adalah acuan desain dan kedalaman, bukan sumber materi untuk topik baru. Rangkum kebutuhan dan asumsi, tanyakan hanya kekosongan penting, lalu buat PPTX yang bisa diedit dengan notes dosen, contoh, latihan, dan sumber. Periksa setiap slide. Buat PDF jika alat ekspor tersedia, dan laporkan pemeriksaan yang belum dapat dilakukan.

UNTUK PROJECT

Tambahkan instruksi Project: “Saat membuat atau merevisi slide kuliah, ikuti SLIDESTUDIO-INSTRUCTIONS.txt. Kebutuhan pertemuan dalam brief atau chat mengambil prioritas.” Pastikan file panduan dan sumber tersedia dalam Project tersebut.

PENTING

Mengunggah instruksi bukan pemasangan otomatis atau penambahan alat. Pembuatan PPTX/PDF bergantung pada kemampuan ChatGPT yang tersedia. Garamond dan Franklin Gothic Book perlu tersedia untuk mempertahankan tampilan contoh; font tidak disertakan. Contoh Kopi Sela dan semua angkanya hipotetis. Jangan menjanjikan hasil identik hanya dari instruksi teks. Jika upload TXT tidak tersedia, salin isi instruksi ke chat.

Repositori lengkap: https://github.com/ridhoachmad712/slidestudio
'''
    entries = {
        'SLIDESTUDIO-INSTRUCTIONS.txt': instructions.encode('utf-8'),
        'BRIEF-KULIAH.txt': brief.encode('utf-8'),
        'MULAI-DI-SINI.txt': guide.encode('utf-8'),
        'contoh-marketing.pptx': (ROOT / 'examples/marketing/manajemen-pemasaran.pptx').read_bytes(),
        'sumber-contoh-marketing.txt': (ROOT / 'examples/marketing/SOURCES.md').read_bytes(),
        'LICENSE.txt': (ROOT / 'LICENSE').read_bytes(),
    }
    dest = ROOT / 'downloads/slidestudio-chatgpt.zip'
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, 'w') as archive:
        for name, payload in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, payload)
    with zipfile.ZipFile(dest) as archive:
        assert archive.testzip() is None
    print(f'Built {dest.name}: {len(entries)} files')
    return dest

if __name__ == '__main__':
    build()
