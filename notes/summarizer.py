import os
from datetime import datetime
from transformers import pipeline

# ----------------------------------
# Folders
# ----------------------------------
NOTES_FOLDER = "notes/generated_notes"
SUMMARY_FOLDER = "notes/generated_notes/summary"

os.makedirs(SUMMARY_FOLDER, exist_ok=True)


# ----------------------------------
# Find Latest Notes File
# ----------------------------------
def get_latest_notes():

    files = [
        os.path.join(NOTES_FOLDER, f)
        for f in os.listdir(NOTES_FOLDER)
        if f.endswith(".txt")
    ]

    if not files:
        return None

    return max(files, key=os.path.getmtime)


# ----------------------------------
# Generate Summary
# ----------------------------------
def summarize_notes():

    latest_file = get_latest_notes()

    if latest_file is None:
        print("No lecture notes found.")
        return

    with open(latest_file, "r", encoding="utf-8") as file:
        text = file.read()

    print("Loading AI Summarizer...")

    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )

    # Handle long notes by splitting into chunks
    chunk_size = 1000
    summaries = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        if len(chunk.strip()) < 50:
            continue

        summary = summarizer(
            chunk,
            max_length=150,
            min_length=50,
            do_sample=False
        )

        summaries.append(summary[0]["summary_text"])

    final_summary = "\n\n".join(summaries)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = os.path.join(
        SUMMARY_FOLDER,
        f"summary_{timestamp}.txt"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_summary)

    print("\n==============================")
    print("Summary Generated Successfully")
    print("==============================")
    print("Saved:", output_file)

    print("\nSummary Preview:\n")
    print(final_summary)


# ----------------------------------
# Main
# ----------------------------------
if __name__ == "__main__":
    summarize_notes()
