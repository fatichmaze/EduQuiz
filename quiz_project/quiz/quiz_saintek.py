import os

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== QUIZ SAINTEK TKA ===")
        print("1. Fisika")
        print("2. Kimia")
        print("3. Biologi")
        print("4. Matematika Wajib")
        print("0. Keluar")

        pilihan_mapel = input("Pilih mata pelajaran (1-4): ").strip()

        if pilihan_mapel == "1":
            jalankan_quiz("Fisika")
        elif pilihan_mapel == "2":
            jalankan_quiz("Kimia")
        elif pilihan_mapel == "3":
            jalankan_quiz("Biologi")
        elif pilihan_mapel == "4":
            jalankan_quiz("Matematika Wajib")
        elif pilihan_mapel == "0":
            print("Terima kasih telah mengikuti Quiz Saintek TKA! 👋")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

# === DATA SOAL PILIHAN GANDA (10 SOAL PER MAPEL) ===
SOAL = {
    "Fisika": [
        {"soal": "Satuan gaya dalam SI adalah ...", "pilihan": ["A. Joule", "B. Newton", "C. Watt", "D. Pascal"], "jawaban": "B"},
        {"soal": "Hukum Newton II berbunyi ...", "pilihan": ["A. Gaya aksi = gaya reaksi", "B. F = m × a", "C. Benda tetap diam tanpa gaya", "D. Momentum tetap"], "jawaban": "B"},
        {"soal": "Kecepatan adalah ...", "pilihan": ["A. Jarak dibagi waktu", "B. Percepatan dibagi waktu", "C. Waktu dikali gaya", "D. Gaya dibagi massa"], "jawaban": "A"},
        {"soal": "Energi kinetik dirumuskan sebagai ...", "pilihan": ["A. ½mv²", "B. mgh", "C. F × s", "D. p × v"], "jawaban": "A"},
        {"soal": "1 Joule sama dengan ...", "pilihan": ["A. 1 N/m", "B. 1 N·m", "C. 1 N/s", "D. 1 kg/m"], "jawaban": "B"},
        {"soal": "Alat untuk mengukur kuat arus listrik adalah ...", "pilihan": ["A. Voltmeter", "B. Amperemeter", "C. Ohmmeter", "D. Wattmeter"], "jawaban": "B"},
        {"soal": "Daya diukur dalam satuan ...", "pilihan": ["A. Watt", "B. Joule", "C. Newton", "D. Ampere"], "jawaban": "A"},
        {"soal": "Cahaya termasuk gelombang ...", "pilihan": ["A. Longitudinal", "B. Mekanik", "C. Elektromagnetik", "D. Bunyi"], "jawaban": "C"},
        {"soal": "Perpindahan kalor tanpa medium adalah ...", "pilihan": ["A. Konduksi", "B. Konveksi", "C. Radiasi", "D. Difusi"], "jawaban": "C"},
        {"soal": "Besaran pokok yang satuannya meter adalah ...", "pilihan": ["A. Massa", "B. Panjang", "C. Waktu", "D. Suhu"], "jawaban": "B"},
    ],

    "Kimia": [
        {"soal": "Rumus kimia air adalah ...", "pilihan": ["A. CO2", "B. H2O", "C. O2", "D. HCl"], "jawaban": "B"},
        {"soal": "Atom terdiri atas ...", "pilihan": ["A. Proton, Neutron, Elektron", "B. Molekul, Ion, Atom", "C. Senyawa, Unsur, Campuran", "D. Inti, Kulit, Orbit"], "jawaban": "A"},
        {"soal": "Nomor atom menunjukkan jumlah ...", "pilihan": ["A. Neutron", "B. Proton", "C. Elektron valensi", "D. Isotop"], "jawaban": "B"},
        {"soal": "Gas mulia terdapat pada golongan ...", "pilihan": ["A. I A", "B. II A", "C. VII A", "D. VIII A"], "jawaban": "D"},
        {"soal": "Ikatan ion terbentuk karena ...", "pilihan": ["A. Pertukaran elektron", "B. Pemakaian bersama elektron", "C. Pelepasan proton", "D. Tarikan antar neutron"], "jawaban": "A"},
        {"soal": "pH air murni adalah ...", "pilihan": ["A. 5", "B. 6", "C. 7", "D. 8"], "jawaban": "C"},
        {"soal": "Unsur paling elektronegatif adalah ...", "pilihan": ["A. Oksigen", "B. Klor", "C. Fluorin", "D. Hidrogen"], "jawaban": "C"},
        {"soal": "Senyawa NaCl termasuk ...", "pilihan": ["A. Kovalen", "B. Ionik", "C. Logam", "D. Kompleks"], "jawaban": "B"},
        {"soal": "Larutan yang menghantarkan listrik disebut ...", "pilihan": ["A. Elektrolit", "B. Non-elektrolit", "C. Isotonik", "D. Hipotonik"], "jawaban": "A"},
        {"soal": "Massa atom relatif hidrogen = 1 artinya ...", "pilihan": ["A. Berat atom 1 g", "B. Standar pembanding", "C. Tidak bermassa", "D. Termasuk gas mulia"], "jawaban": "B"},
    ],

    "Biologi": [
        {"soal": "Organisme autotrof memperoleh makanan dengan cara ...", "pilihan": ["A. Parasitisme", "B. Fotosintesis", "C. Fermentasi", "D. Memangsa"], "jawaban": "B"},
        {"soal": "Bagian sel yang berfungsi mengatur seluruh kegiatan sel adalah ...", "pilihan": ["A. Mitokondria", "B. Inti sel", "C. Sitoplasma", "D. Ribosom"], "jawaban": "B"},
        {"soal": "Fotosintesis berlangsung di ...", "pilihan": ["A. Kloroplas", "B. Nukleus", "C. Ribosom", "D. Mitokondria"], "jawaban": "A"},
        {"soal": "DNA berfungsi untuk ...", "pilihan": ["A. Pembentuk energi", "B. Penyimpan informasi genetik", "C. Pengatur suhu", "D. Pencernaan protein"], "jawaban": "B"},
        {"soal": "Alat pernapasan pada ikan adalah ...", "pilihan": ["A. Paru-paru", "B. Insang", "C. Trakea", "D. Kulit"], "jawaban": "B"},
        {"soal": "Sel tumbuhan berbeda dari sel hewan karena memiliki ...", "pilihan": ["A. Dinding sel dan kloroplas", "B. Nukleus dan membran", "C. Lisosom", "D. Mitokondria"], "jawaban": "A"},
        {"soal": "Proses pembelahan sel secara mitosis menghasilkan ...", "pilihan": ["A. 2 sel anak identik", "B. 4 sel anak", "C. 1 sel baru", "D. 3 sel anak"], "jawaban": "A"},
        {"soal": "Enzim berfungsi sebagai ...", "pilihan": ["A. Pengatur tekanan", "B. Katalis reaksi biokimia", "C. Hormon", "D. Zat makanan"], "jawaban": "B"},
        {"soal": "Organ terbesar pada tubuh manusia adalah ...", "pilihan": ["A. Jantung", "B. Otak", "C. Kulit", "D. Hati"], "jawaban": "C"},
        {"soal": "Zat hijau daun disebut ...", "pilihan": ["A. Kloroplas", "B. Klorofil", "C. Xilem", "D. Floem"], "jawaban": "B"},
    ],

    "Matematika Wajib": [
        {"soal": "Hasil dari 2² + 3² adalah ...", "pilihan": ["A. 10", "B. 12", "C. 13", "D. 14"], "jawaban": "C"},
        {"soal": "Turunan dari f(x)=x² adalah ...", "pilihan": ["A. 2x", "B. x²", "C. x", "D. 3x²"], "jawaban": "A"},
        {"soal": "Integral dari 2x dx adalah ...", "pilihan": ["A. x² + C", "B. 2x + C", "C. 2x² + C", "D. x + C"], "jawaban": "A"},
        {"soal": "Nilai sin(90°) adalah ...", "pilihan": ["A. 0", "B. 1", "C. ½", "D. √3/2"], "jawaban": "B"},
        {"soal": "Jika f(x)=2x+3, maka f(2)=...", "pilihan": ["A. 4", "B. 5", "C. 7", "D. 9"], "jawaban": "C"},
        {"soal": "Nilai dari log₁₀100 adalah ...", "pilihan": ["A. 0", "B. 1", "C. 2", "D. 10"], "jawaban": "C"},
        {"soal": "Rumus luas lingkaran adalah ...", "pilihan": ["A. πr", "B. 2πr", "C. πr²", "D. r²/π"], "jawaban": "C"},
        {"soal": "Peluang muncul angka genap dari dadu adalah ...", "pilihan": ["A. 1/3", "B. 1/2", "C. 2/3", "D. 1/6"], "jawaban": "B"},
        {"soal": "Jika 2x = 10, maka x = ...", "pilihan": ["A. 4", "B. 5", "C. 6", "D. 10"], "jawaban": "B"},
        {"soal": "Nilai dari (3 + 2)² adalah ...", "pilihan": ["A. 10", "B. 15", "C. 20", "D. 25"], "jawaban": "D"},
    ]
}

# === FUNGSI MENJALANKAN QUIZ ===
def jalankan_quiz(mapel):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=== QUIZ {mapel.upper()} ===")

    soal_list = SOAL[mapel]
    skor = 0

    for i, s in enumerate(soal_list, start=1):
        print(f"\nSoal {i}: {s['soal']}")
        for pilihan in s["pilihan"]:
            print(pilihan)
        jawaban = input("Jawaban kamu (A/B/C/D): ").upper().strip()

        if jawaban == s["jawaban"]:
            print("✅ Benar!")
            skor += 1
        else:
            print(f"❌ Salah! Jawaban benar adalah {s['jawaban']}.")

    print("\n=== HASIL AKHIR ===")
    print(f"Skor kamu: {skor}/{len(soal_list)}")
    print(f"Persentase: {(skor / len(soal_list)) * 100:.1f}%")
    input("\nTekan Enter untuk kembali ke menu utama...")

# === JALANKAN PROGRAM ===
if __name__ == "__main__":
    main()
