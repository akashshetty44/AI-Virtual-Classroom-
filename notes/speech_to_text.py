import os
import whisper
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
AUDIO_FOLDER = "notes/audio"
OUTPUT_FOLDER = "notes/generated_notes"

os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

AUDIO_FILE = os.path.join(AUDIO_FOLDER, "lecture.wav")


# -----------------------------
# Speech to Text
# -----------------------------
def speech_to_text():

    if not os.path.exists(AUDIO_FILE):
        print(f"Audio file not found: {AUDIO_FILE}")
        print("Please place your lecture recording as 'lecture.wav' in the notes/audio folder.")
        return

    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing lecture...")

    result = model.transcribe(AUDIO_FILE)

    transcript = result["text"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = os.path.join(
        OUTPUT_FOLDER,
        f"lecture_notes_{timestamp}.txt"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(transcript)

    print("\n====================================")
    print("Speech Successfully Converted to Text")
    print("Saved to:", output_file)
    print("====================================\n")

    print("Transcript Preview:\n")
    print(transcript[:1000])


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    speech_to_text()
