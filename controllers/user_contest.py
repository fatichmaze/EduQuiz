from utils import load_data, save_data, CONTEST_FILE, QUIZ_FILE, LEADERBOARD_FILE, HISTORY_FILE

def enter_contest(username):
    contests = load_data(CONTEST_FILE, [])
    quizzes = load_data(QUIZ_FILE, [])
    leaderboard = load_data(LEADERBOARD_FILE, [])
    history = load_data(HISTORY_FILE, [])

    if not contests:
        print("❌ Belum ada contest tersedia.")
        return

    print("\n=== Daftar Contest ===")
    for i, c in enumerate(contests, start=1):
        print(f"{i}. {c['nama']}")
    try:
        pilih = int(input("Pilih contest (nomor): ")) - 1
        contest = contests[pilih]
    except (ValueError, IndexError):
        print("Pilihan tidak valid.")
        return

    total_score = 0
    print(f"\nMasuk ke contest: {contest['nama']}\n")

    for quiz_id in contest["quiz_ids"]:
        quiz = next((q for q in quizzes if q["id"] == quiz_id), None)
        if quiz:
            print(f"Pertanyaan: {quiz['pertanyaan']}")
            jawaban = input("Jawabanmu: ")
            if jawaban.strip().lower() == quiz["jawaban"].strip().lower():
                print("✅ Benar!\n")
                total_score += 10
            else:
                print(f"❌ Salah. Jawaban benar: {quiz['jawaban']}\n")

    print(f"Skor akhir kamu: {total_score}\n")

    leaderboard.append({"username": username, "contest": contest["nama"], "score": total_score})
    history.append({"username": username, "contest": contest["nama"], "score": total_score})

    save_data(LEADERBOARD_FILE, leaderboard)
    save_data(HISTORY_FILE, history)
    print("✅ Skor tersimpan ke leaderboard dan history!\n")

def show_leaderboard():
    leaderboard = load_data(LEADERBOARD_FILE, [])
    if not leaderboard:
        print("Belum ada data leaderboard.\n")
        return
    print("\n=== Leaderboard ===")
    for entry in sorted(leaderboard, key=lambda x: x["score"], reverse=True):
        print(f"{entry['username']} - {entry['contest']} - {entry['score']} poin")
    print()

def show_history(username):
    history = load_data(HISTORY_FILE, [])
    user_history = [h for h in history if h["username"] == username]

    if not user_history:
        print("Belum ada riwayat kamu.\n")
        return

    print(f"\n=== History {username} ===")
    for h in user_history:
        print(f"{h['contest']} - Skor: {h['score']}")
    print()
