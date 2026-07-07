import cv2
import sqlite3
from datetime import datetime
from deepface import DeepFace

DATABASE = "database/classroom.db"


def save_emotion(emotion, confidence):
    """Save detected emotion to the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emotions (student_id, emotion, confidence, detected_at)
        VALUES (?, ?, ?, ?)
    """, (
        None,  # Replace with student_id after integrating face recognition
        emotion,
        confidence,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def start_emotion_detection():
    camera = cv2.VideoCapture(0)

    print("Emotion Detection Started")
    print("Press 'Q' to Exit")

    while True:
        ret, frame = camera.read()

        if not ret:
            break

        try:
            result = DeepFace.analyze(
                frame,
                actions=["emotion"],
                enforce_detection=False,
                silent=True
            )

            # Handle single or multiple face output
            if isinstance(result, list):
                result = result[0]

            emotion = result["dominant_emotion"]
            confidence = result["emotion"][emotion]

            save_emotion(emotion, confidence)

            cv2.putText(
                frame,
                f"{emotion} ({confidence:.1f}%)",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        except Exception as e:
            cv2.putText(
                frame,
                "Face Not Detected",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        cv2.imshow("AI Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_emotion_detection()
