import json
import os

# Nama file JSON utama
CONTEST_FILE = "contests.json"
QUIZ_FILE = "quizzes.json"
LEADERBOARD_FILE = "leaderboard.json"
HISTORY_FILE = "history.json"

# Fungsi untuk baca file JSON (Baca data dari file JSON, kalau belum ada kembalikan default_data.)
def load_data(filename, default_data):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return default_data

# Fungsi untuk simpan data ke file JSON (Simpan data ke file JSON dengan format rapi (indentasi).)
def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
