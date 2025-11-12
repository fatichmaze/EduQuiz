from utils import load_data, save_data, CONTEST_FILE, QUIZ_FILE
from quiz_project import quiz_saintek
import os

#BUAT QUIZ
def buat_quiz():
    quizzes = load_data(QUIZ_FILE, [])

    #Cegah ID duplikat
    while True:
        quiz_id = input("Masukkan ID Quiz (misal: Q1): ")
        id_sama = False
        for q in quizzes:
            if q["Id"] == quiz_id:
                id_sama = True
                break

        if id_sama:
            print("❌ ID Quiz sudah ada! Silahkan buat ID yang lain.")
        else:
            break

    judul = input("Masukkan Judul Quiz: ")

    questions = []
    while True:
        pertanyaan = input("Masukkan pertanyaan (atau ketik 'selesai' untuk berhenti): ")
        if pertanyaan.lower() == "selesai":
            break
        jawaban = input("Masukkan jawaban benar: ")
        questions.append({"Pertanyaan": pertanyaan, "Jawaban": jawaban})
    
    quiz = {"Id": quiz_id, "Judul": judul, "Questions": questions}
    quizzes.append(quiz)
    save_data(QUIZ_FILE, quizzes)
    print("✅ Quiz berhasil dibuat!\n")

#EDIT QUIZ
def edit_quiz():
    quizzes = load_data(QUIZ_FILE, [])
    if not quizzes:
        print("Belum ada quiz.")
        return

    print("\n=== Daftar Quiz ===")
    for i, q in enumerate(quizzes, start=1):
        print(f"{i}. {q['Id']} - {q['Judul']}")
    pilih = int(input("Pilih quiz yang ingin diedit: ")) - 1

    judul_baru = input("Masukkan judul baru (biarkan kosong jika tidak diubah): ")
    if judul_baru != "":
        quizzes[pilih]["Judul"] = judul_baru

    print("\nMasukkan pertanyaan baru:")
    questions = []
    while True:
        pertanyaan = input("Masukkan pertanyaan (atau ketik 'selesai' untuk berhenti): ")
        if pertanyaan.lower() == "selesai":
            break
        jawaban = input("Masukkan jawaban benar: ")
        questions.append({"Pertanyaan": pertanyaan, "Jawaban": jawaban})

    if questions:
        quizzes[pilih]["Questions"] = questions

    save_data(QUIZ_FILE, quizzes)
    print("✅ Quiz berhasil diupdate!\n")

#HAPUS QUIZ
def hapus_quiz():
    quizzes = load_data(QUIZ_FILE, [])
    if not quizzes:
        print("Belum ada quiz.")
        return

    print("\n=== Daftar Quiz ===")
    for i, q in enumerate(quizzes, start=1):
        print(f"{i}. {q['Id']} - {q['Judul']}")
    pilih = int(input("Pilih quiz yang ingin dihapus: ")) - 1

    hapus = quizzes.pop(pilih)
    save_data(QUIZ_FILE, quizzes)
    print(f"🗑️ Quiz '{hapus['Id']}' berhasil dihapus.\n")

#BUAT CONTEST
def buat_contest():
    contests = load_data(CONTEST_FILE, [])
    quizzes = load_data(QUIZ_FILE, [])

    if not quizzes:
        print("❌ Belum ada quiz. Silahkan buat quiz terlebih dahulu.")
        return

    nama = input("Masukkan nama contest: ")

    # Input jumlah quiz yang ingin dimasukkan
    while True:
        try:
            jumlah_quiz = int(input("Jumlah quiz yang akan dimasukkan ke contest: "))
            if jumlah_quiz <= 0 or jumlah_quiz > len(quizzes):
                print(f"Jumlah harus antara 1 sampai {len(quizzes)}.")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid!")

    print("\nPilih quiz yang akan dimasukkan:")
    for i, q in enumerate(quizzes, start=1):
        print(f"{i}. {q['Id']} - {q['Judul']}")

    ids = []
    for n in range(jumlah_quiz):
        while True:
            try:
                pilih = int(input(f"Pilih quiz ke-{n+1}: ")) - 1
                if pilih < 0 or pilih >= len(quizzes):
                    print("Nomor quiz tidak valid!")
                else:
                    ids.append(quizzes[pilih]["Id"])
                    break
            except ValueError:
                print("Masukkan angka yang valid!")

    contests.append({"Nama": nama, "Quiz_Ids": ids})
    save_data(CONTEST_FILE, contests)
    print("✅ Contest berhasil dibuat!\n")

#LIHAT CONTEST
def lihat_contest():
    contests = load_data(CONTEST_FILE, [])
    if not contests:
        print("Belum ada contest.")
        return

    print("\n=== Daftar Contest ===")
    for i, c in enumerate(contests, start=1):
        teks_quiz = ""
        for qid in c["Quiz_Ids"]:
            teks_quiz += qid + ", "
        teks_quiz = teks_quiz[:-2]
        print(f"{i}. {c['Nama']} → Quiz: {teks_quiz}")
    print()

#MENU ADMIN
def admin_menu():
    while True:
        print("""
=== MENU ADMIN ===
1. Buat Quiz
2. Edit Quiz
3. Hapus Quiz
4. Buat Contest
5. Lihat Contest
6. Logout
""")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            buat_quiz()
        elif pilih == "2":
            edit_quiz()
        elif pilih == "3":
            hapus_quiz()
        elif pilih == "4":
            buat_contest()
        elif pilih == "5":
            lihat_contest()
        elif pilih == "6":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid.\n")
