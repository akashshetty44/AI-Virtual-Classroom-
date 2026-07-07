import os

# ==========================================
# Base Directory
# ==========================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ==========================================
# Flask Configuration
# ==========================================
SECRET_KEY = "AI_VIRTUAL_CLASSROOM_2026"

DEBUG = True

HOST = "0.0.0.0"

PORT = 5000

# ==========================================
# Database
# ==========================================
DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "classroom.db"
)

# ==========================================
# Attendance Module
# ==========================================
FACE_DATASET = os.path.join(
    BASE_DIR,
    "attendance",
    "faces"
)

ATTENDANCE_FILE = os.path.join(
    BASE_DIR,
    "attendance",
    "attendance.csv"
)

ATTENDANCE_THRESHOLD = 0.50

CAMERA_INDEX = 0

# ==========================================
# Emotion Detection
# ==========================================
EMOTION_MODEL = "DeepFace"

EMOTION_LOG = os.path.join(
    BASE_DIR,
    "emotion",
    "emotion_log.csv"
)

# ==========================================
# Notes Generation
# ==========================================
AUDIO_FOLDER = os.path.join(
    BASE_DIR,
    "notes",
    "audio"
)

NOTES_FOLDER = os.path.join(
    BASE_DIR,
    "notes",
    "generated_notes"
)

PDF_FOLDER = os.path.join(
    NOTES_FOLDER,
    "pdf"
)

SUMMARY_FOLDER = os.path.join(
    NOTES_FOLDER,
    "summary"
)

# ==========================================
# Quiz Generation
# ==========================================
QUIZ_FOLDER = os.path.join(
    BASE_DIR,
    "quiz"
)

QUIZ_OUTPUT = os.path.join(
    QUIZ_FOLDER,
    "generated_quiz.txt"
)

# ==========================================
# Performance Prediction
# ==========================================
MODEL_PATH = os.path.join(
    BASE_DIR,
    "prediction",
    "student_model.pkl"
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "prediction",
    "student_dataset.csv"
)

# ==========================================
# Uploads
# ==========================================
UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "wav",
    "mp3",
    "pdf",
    "txt"
}

# ==========================================
# Reports
# ==========================================
REPORT_FOLDER = os.path.join(
    BASE_DIR,
    "reports"
)

# ==========================================
# Create Required Folders Automatically
# ==========================================
folders = [
    FACE_DATASET,
    AUDIO_FOLDER,
    NOTES_FOLDER,
    PDF_FOLDER,
    SUMMARY_FOLDER,
    QUIZ_FOLDER,
    UPLOAD_FOLDER,
    REPORT_FOLDER,
    os.path.dirname(DATABASE)
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
