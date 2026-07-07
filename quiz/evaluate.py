import sqlite3
from datetime import datetime

DATABASE = "database/classroom.db"


# ---------------------------------------
# Save Result
# ---------------------------------------
def save_result(student_id, score, total):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO quiz_results
        (student_id, score, total_marks, submitted_at)
        VALUES (?, ?, ?, ?)
    """, (
        student_id,
        score,
        total,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# ---------------------------------------
# Quiz Questions
# ---------------------------------------
questions = [

{
    "question":"AI stands for?",
    "options":["Artificial Intelligence",
               "Artificial Internet",
               "Advanced Interface",
               "Automatic Input"],
    "answer":1
},

{
    "question":"Python is a?",
    "options":["Programming Language",
               "Database",
               "Operating System",
               "Compiler"],
    "answer":1
},

{
    "question":"Which library is used for face recognition?",
    "options":["NumPy",
               "OpenCV",
               "face_recognition",
               "Matplotlib"],
    "answer":3
},

{
    "question":"DeepFace is mainly used for?",
    "options":["Emotion Detection",
               "Video Editing",
               "Database",
               "Networking"],
    "answer":1
},

{
    "question":"Flask is a?",
    "options":["Python Web Framework",
               "Database",
               "IDE",
               "Machine"],
    "answer":1
}

]


# ---------------------------------------
# Quiz Evaluation
# ---------------------------------------
def start_quiz():

    print("\n===== AI Virtual Classroom Quiz =====\n")

    student_id = int(input("Enter Student ID: "))

    score = 0

    total = len(questions)

    for i, q in enumerate(questions):

        print("\n-----------------------------------")
        print(f"Question {i+1}")

        print(q["question"])

        for index, option in enumerate(q["options"], start=1):
            print(f"{index}. {option}")

        try:
            answer = int(input("Your Answer: "))
        except:
            answer = 0

        if answer == q["answer"]:
            score += 1

    percentage = (score / total) * 100

    save_result(student_id, score, total)

    print("\n==============================")
    print("Quiz Completed")
    print("==============================")
    print("Score :", score, "/", total)
    print("Percentage :", round(percentage,2), "%")

    if percentage >= 80:
        print("Grade : Excellent")

    elif percentage >= 60:
        print("Grade : Good")

    elif percentage >= 40:
        print("Grade : Average")

    else:
        print("Grade : Needs Improvement")


# ---------------------------------------
# Main
# ---------------------------------------
if __name__ == "__main__":
    start_quiz()
