import os
import cv2
import sqlite3
import face_recognition
from datetime import datetime

# -----------------------------
# Paths
# -----------------------------
FACE_DATASET = "attendance/faces"
DATABASE = "database/classroom.db"

known_face_encodings = []
known_face_names = []


# -----------------------------
# Load Registered Faces
# -----------------------------
def load_faces():
    print("Loading registered students...")

    if not os.path.exists(FACE_DATASET):
        print("Face dataset folder not found.")
        return

    for student in os.listdir(FACE_DATASET):

        student_path = os.path.join(FACE_DATASET, student)

        if not os.path.isdir(student_path):
            continue

        for image_name in os.listdir(student_path):

            image_path = os.path.join(student_path, image_name)

            try:
                image = face_recognition.load_image_file(image_path)

                encodings = face_recognition.face_encodings(image)

                if len(encodings) > 0:
                    known_face_encodings.append(encodings[0])
                    known_face_names.append(student)

            except Exception:
                pass

    print(f"Loaded {len(known_face_names)} face images.")


# -----------------------------
# Save Attendance
# -----------------------------
def mark_attendance(student_name):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM students WHERE name=?",
        (student_name,)
    )

    student = cursor.fetchone()

    if student is None:
        conn.close()
        return

    student_id = student[0]

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        SELECT * FROM attendance
        WHERE student_id=? AND date=?
        """,
        (student_id, today)
    )

    exists = cursor.fetchone()

    if exists is None:

        cursor.execute(
            """
            INSERT INTO attendance
            (student_id,date,time,status)
            VALUES (?,?,?,?)
            """,
            (
                student_id,
                today,
                datetime.now().strftime("%H:%M:%S"),
                "Present"
            )
        )

        conn.commit()

        print(student_name, "Attendance Marked")

    conn.close()


# -----------------------------
# Start Camera
# -----------------------------
def start_attendance():

    load_faces()

    video = cv2.VideoCapture(0)

    while True:

        ret, frame = video.read()

        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb)

        face_encodings = face_recognition.face_encodings(
            rgb,
            face_locations
        )

        for face_encoding, face_location in zip(
                face_encodings,
                face_locations):

            matches = face_recognition.compare_faces(
                known_face_encodings,
                face_encoding
            )

            name = "Unknown"

            if True in matches:

                index = matches.index(True)

                name = known_face_names[index]

                mark_attendance(name)

            top, right, bottom, left = face_location

            cv2.rectangle(
                frame,
                (left, top),
                (right, bottom),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                name,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

        cv2.imshow("AI Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_attendance()
