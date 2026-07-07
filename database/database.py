import sqlite3
import os

# Database folder
DB_FOLDER = "database"
DB_NAME = "classroom.db"

os.makedirs(DB_FOLDER, exist_ok=True)

DATABASE = os.path.join(DB_FOLDER, DB_NAME)


def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # -----------------------------
    # Students Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        usn TEXT UNIQUE NOT NULL,
        department TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # -----------------------------
    # Attendance Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        time TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    # -----------------------------
    # Emotion Detection Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emotions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        emotion TEXT,
        confidence REAL,
        detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    # -----------------------------
    # Lecture Notes Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # -----------------------------
    # Quiz Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        answer TEXT
    )
    """)

    # -----------------------------
    # Quiz Results Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        score REAL,
        total_marks REAL,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    # -----------------------------
    # Performance Prediction Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS performance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        attendance_percentage REAL,
        quiz_score REAL,
        predicted_grade TEXT,
        prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    conn.commit()
    conn.close()

    print("===================================")
    print(" AI Virtual Classroom Database Ready")
    print(" Database Created Successfully")
    print("===================================")


if __name__ == "__main__":
    create_database()
