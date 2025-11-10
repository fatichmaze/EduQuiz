from utils import load_data, save_data, CONTEST_FILE, QUIZ_FILE

def buat_quiz():
    quizzes = load_data(QUIZ_FILE, [])
    quiz_id = input("Masukkan ID Quiz (misal: Q1): ")
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

def edit_quiz():
    quizzes = load_data(QUIZ_FILE, [])
    if not quizzes:
        print("Belum ada quiz.")
        return

    for i, q in enumerate(quizzes, start=1):
        print(f"{i}. {q['id']} - {q['pertanyaan']}")
    pilih = int(input("Pilih quiz yang ingin diedit: ")) - 1

    pertanyaan = input("Pertanyaan baru: ")
    jawaban = input("Jawaban baru: ")

    quizzes[pilih]["pertanyaan"] = pertanyaan
    quizzes[pilih]["jawaban"] = jawaban
    save_data(QUIZ_FILE, quizzes)
    print("✅ Quiz berhasil diupdate!\n")

def hapus_quiz():
    quizzes = load_data(QUIZ_FILE, [])
    if not quizzes:
        print("Belum ada quiz.")
        return

    for i, q in enumerate(quizzes, start=1):
        print(f"{i}. {q['id']} - {q['pertanyaan']}")
    pilih = int(input("Pilih quiz yang ingin dihapus: ")) - 1

    hapus = quizzes.pop(pilih)
    save_data(QUIZ_FILE, quizzes)
    print(f"🗑️ Quiz '{hapus['id']}' berhasil dihapus.\n")


# Fungsi untuk kelola CONTEST
def buat_contest():
    contests = load_data(CONTEST_FILE, [])
    quizzes = load_data(QUIZ_FILE, [])

    if not quizzes:
        print("❌ Belum ada quiz. Silahkan buat quiz terlebih dahulu.")
        return

    nama = input("Masukkan nama contest: ")
    print("\nPilih quiz yang akan dimasukkan:")
    for i, q in enumerate(quizzes, start=1):
        print(f"{i}. {q['id']} - {q['pertanyaan']}")

    pilih = input("Masukkan nomor quiz (pisahkan dengan koma, contoh: 1,3,5): ")
    ids = [quizzes[int(i.strip()) - 1]["id"] for i in pilih.split(",")]

    contests.append({"nama": nama, "quiz_ids": ids})
    save_data(CONTEST_FILE, contests)
    print("✅ Contest berhasil dibuat!\n")

def lihat_contest():
    contests = load_data(CONTEST_FILE, [])
    if not contests:
        print("Belum ada contest.")
        return

    print("\n=== Daftar Contest ===")
    for i, c in enumerate(contests, start=1):
        print(f"{i}. {c['nama']} → Quiz: {', '.join(c['quiz_ids'])}")
    print()

# Menu Admin
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
