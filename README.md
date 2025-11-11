# EduQuiz 📝
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

EduQuiz adalah aplikasi kuis berbasis terminal yang dirancang untuk membantu siswa SMA mempersiapkan diri menghadapi TKA Saintek.  
Aplikasi ini berisi latihan soal interaktif seputar **Matematika, Fisika, Kimia, dan Biologi** untuk belajar secara praktis dan menantang langsung dari command line.

---

## 📝 Persyaratan
- **Python 3.10+**  
- **Library / Modul Python**:
  - `json`
  - `os`
  - `sys`
  - `re`
  - `google-generativeai`
  - `python-dotenv`
  - **API Key Google Gemini** (untuk fitur Chatbot)  
  > Chatbot Quizzy memerlukan API Key dari Google Gemini.  
  > Pastikan sudah mendaftar dan menyiapkan key sebelum menggunakan fitur Chatbot.

---

## 🚀 Fitur
- 🏆 **Contest**: Mode kompetisi untuk berpartisipasi dan membandingkan hasil dengan peserta lain.  
- 🧠 **Quiz**: Kuis singkat berbagai topik Saintek untuk melatih kecepatan berpikir.  
- 📚 **Latihan Soal (Latsol)**: Koleksi soal latihan untuk memperdalam pemahaman materi.  
- 🕓 **Riwayat**: Menampilkan riwayat hasil kuis dan latihan agar pengguna bisa memantau progres belajar.  
- 📈 **Papan Peringkat**: Menampilkan peringkat pengguna berdasarkan skor tertinggi untuk meningkatkan motivasi.  
- 🤖 **Chatbot**: Asisten AI siap membantu menjawab pertanyaan dan memberi penjelasan tambahan.

---

## 💻 Instalasi
1. Clone repositori:  
    ```bash
    git clone https://github.com/Dylanslps/EduQuiz.git
    ```
2. Masuk ke folder proyek:  
    ```bash
    cd EduQuiz
    ```
3. Install dependensi:  
    ```bash
    pip install google-generativeai python-dotenv
    ```
4. Jalankan program:  
    ```bash
    python main.py
    ```

---

## 🎮 Cara Penggunaan
Berikut alur penggunaan EduQuiz untuk pengguna baru:

1. Jalankan program utama:  
    ```bash
    python main.py
    ```
2. Setelah program berjalan, akan muncul menu utama dengan pilihan fitur.  
3. Masukkan angka sesuai fitur yang ingin digunakan, lalu tekan Enter.  
4. Ikuti instruksi yang muncul di terminal untuk masing-masing fitur.  
5. Setelah selesai, program akan kembali ke menu utama. Pilih fitur lain atau ketik `exit` untuk menutup program.

> Pastikan API key sudah diatur di file `.env` sebelum menggunakan Chatbot.

---

## 🛠 Contribution / Alur Kerja Tim
Jika ingin berkontribusi ke proyek:

1. **Fork** repositori  
2. Buat branch baru untuk fitur yang dikerjakan:  
    ```bash
    git checkout -b nama-feature
    ```
3. Kerjakan perubahan di branch tersebut  
4. Commit & push ke repositori fork:  
    ```bash
    git add .
    git commit -m "Menambahkan fitur X"
    git push origin nama-feature
    ```
5. Buat Pull Request (PR) ke branch utama repositori  
6. Setelah direview, PR bisa di-merge oleh pemilik repositori  

> Tips: Gunakan branch terpisah untuk setiap fitur supaya tim mudah mengelola kode dan menghindari konflik.

---

## ⚠️ Troubleshooting / Tips
- **Chatbot tidak merespons** → cek API key di `.env`  
- **Module not found** → pastikan `pip install google-generativeai python-dotenv` berhasil  
- **Program tidak jalan** → gunakan Python 3.10+ dan jalankan dari folder proyek  
- **Error lain** → pastikan semua file proyek lengkap dan dependencies terinstal  


---

## ⚖ Lisensi
MIT License
