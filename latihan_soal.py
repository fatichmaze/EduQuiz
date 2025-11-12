import json
import random
import os
from datetime import datetime

# ===== UTILITAS JSON =====
def load_json(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ===== FUNGSI TAMBAHAN UNTUK HISTORY =====
def add_history(username, subject, level, score, total):
    """Menyimpan hasil latihan ke file history.json"""
    history_file = "data/history.json"
    history = load_json(history_file)

    entry = {
        "username": username,
        "activity": "Latihan Soal",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": f"{subject.title()} ({level.title()}) - Skor: {score}/{total}"
    }

    if isinstance(history, list):
        history.append(entry)
    else:
        history = [entry]

    save_json(history_file, history)

# ===== FUNGSI MEMBACA SOAL =====
def load_quiz_data(filename="data/latihan_soall.json"):
    if not os.path.exists(filename):
        print("❌ File latihan_soall.json tidak ditemukan!")
        return {}
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# ===== INPUT JAWABAN =====
def get_valid_answer():
    while True:
        answer = input("Jawaban kamu (A/B/C/D atau STOP untuk keluar): ").strip().upper()
        if answer == "STOP":
            return "STOP"
        if len(answer) != 1 or answer not in ["A", "B", "C", "D"]:
            print("⚠️ Masukkan hanya satu huruf: A, B, C, D, atau STOP untuk berhenti.")
        else:
            return answer

# ===== JALANKAN QUIZ =====
def run_quiz(username, subject, level, quiz):
    score = 0
    total = len(quiz)
    random.shuffle(quiz)

    for i, q in enumerate(quiz, 1):
        print(f"\nSoal {i}/{total}: {q['question']}")
        for option in q["options"]:
            print(option)

        answer = get_valid_answer()

        if answer == "STOP":
            print("\n⛔ Kuis dihentikan oleh pengguna.")
            break

        if answer == q["answer"]:
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah. Jawaban yang benar adalah {q['answer']}")

        if "explanation" in q and q["explanation"]:
            print(f"🧾 Pembahasan: {q['explanation']}")

    # simpan ke history
    add_history(username, subject, level, score, total)

    print(f"\n📊 Skor akhir kamu: {score}/{total}")
    print(f"Persentase benar: {score / total * 100:.1f}%")

# ===== MENU LATIHAN SOAL =====
def latsol(username=None):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=== PILIH MATA PELAJARAN (User: {username}) ===")
    print("1. Fisika")
    print("2. Kimia")
    print("3. Biologi")
    print("4. Matematika Wajib")
    pilihan_mapel = input("Pilih mata pelajaran (1/2/3/4): ").strip()

    subjects = {
        "1": "fisika",
        "2": "kimia",
        "3": "biologi",
        "4": "matematika wajib"
    }

    if pilihan_mapel not in subjects:
        print("Pilihan tidak valid.")
        return

    subject = subjects[pilihan_mapel]

    print("\nTingkat kesulitan:")
    print("1. Mudah")
    print("2. Sedang")
    print("3. Sulit")
    tingkat = input("Pilih tingkat kesulitan (1/2/3): ").strip()

    levels = {
        "1": "mudah",
        "2": "sedang",
        "3": "sulit"
    }

    if tingkat not in levels:
        print("Pilihan tidak valid.")
        return

    level = levels[tingkat]

    data = load_quiz_data()
    if subject not in data or level not in data[subject]:
        print("Data soal tidak ditemukan.")
        return

    print(f"\n📘 Mulai Latihan Soal {subject.title()} ({level.title()})\n")
    run_quiz(username, subject, level, data[subject][level])
    input("\nTekan Enter untuk kembali ke menu utama...")

# ===== MAIN (JIKA DIJALANKAN TERPISAH) =====
if __name__ == "__main__":
    latsol("guest")
