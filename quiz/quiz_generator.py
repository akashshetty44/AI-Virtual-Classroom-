import os
from transformers import pipeline

# -----------------------------------
# Folders
# -----------------------------------
NOTES_FOLDER = "notes/generated_notes"
OUTPUT_FILE = "quiz/generated_quiz.txt"

os.makedirs("quiz", exist_ok=True)


# -----------------------------------
# Get Latest Notes
# -----------------------------------
def get_latest_notes():

    files = [
        os.path.join(NOTES_FOLDER, f)
        for f in os.listdir(NOTES_FOLDER)
        if f.endswith(".txt")
    ]

    if not files:
        return None

    return max(files, key=os.path.getmtime)


# -----------------------------------
# Generate Quiz
# -----------------------------------
def generate_quiz():

    notes_file = get_latest_notes()

    if notes_file is None:
        print("No lecture notes found.")
        return

    with open(notes_file, "r", encoding="utf-8") as file:
        notes = file.read()

    print("Loading AI model...")

    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

    prompt = f"""
Generate 10 multiple-choice questions from the following lecture.

For each question provide:
Question
A)
B)
C)
D)
Correct Answer

Lecture:
{notes[:3000]}
"""

    result = generator(
        prompt,
        max_length=1024,
        do_sample=False
    )

    quiz = result[0]["generated_text"]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(quiz)

    print("\n===========================")
    print("Quiz Generated Successfully")
    print("===========================")

    print(quiz)


# -----------------------------------
# Main
# -----------------------------------
if __name__ == "__main__":
    generate_quiz()
