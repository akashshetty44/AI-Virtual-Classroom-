import joblib
import os
import sqlite3
from datetime import datetime

# -----------------------------------
# Configuration
# -----------------------------------
MODEL_PATH = "prediction/student_model.pkl"
DATABASE = "database/classroom.db"


# -----------------------------------
# Save Prediction
# -----------------------------------
def save_prediction(student_id,
                    attendance,
                    quiz_score,
                    assignment_score,
                    prediction):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO performance
        (
            student_id,
            attendance_percentage,
            quiz_score,
            predicted_grade,
            prediction_date
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        student_id,
        attendance,
        quiz_score,
        prediction,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# -----------------------------------
# Prediction
# -----------------------------------
def predict():

    if not os.path.exists(MODEL_PATH):
        print("Model not found!")
        print("Run train_model.py first.")
        return

    model = joblib.load(MODEL_PATH)

    print("\n===== Student Performance Prediction =====\n")

    student_id = int(input("Student ID: "))
    attendance = float(input("Attendance (%): "))
    quiz = float(input("Quiz Score: "))
    assignment = float(input("Assignment Score: "))

    prediction = model.predict([[attendance, quiz, assignment]])[0]

    print("\n==============================")
    print("Prediction Result")
    print("==============================")
    print("Predicted Performance :", prediction)

    save_prediction(
        student_id,
        attendance,
        quiz,
        assignment,
        prediction
    )

    print("\nPrediction saved successfully.")


# -----------------------------------
# Main
# -----------------------------------
if __name__ == "__main__":
    predict()
